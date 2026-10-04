#!/usr/bin/env python3
"""Build rights-filtered HH companions; audit independent staged data without publishing.

Reads only SIMBAD, V/104 and the pinned DSO identity map, never Chen2026 or the
derived mixed-source research table. Output defaults outside hosted v1/.
"""
import argparse
import collections
import contextlib
import csv
import hashlib
import json
import math
import re
import sqlite3
from pathlib import Path

import numpy as np
from astropy.coordinates import FK4, ICRS, SkyCoord
from astropy.time import Time
import astropy.units as u
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/hh"
LIMITS = {"core": 8 * 1024**2, "enrichment": 2 * 1024**2, "media": 1024**2}
ODBL_URL = "https://opendatacommons.org/licenses/odbl/1-0/"
FOOTPRINT = {"model": "gnomonic-rectangle-v1", "camera": "S30 Pro main",
             "widthDeg": 2.24, "heightDeg": 3.99, "positionAngleDeg": 0,
             "boundary": "inclusive-1e-12-tangent-tolerance", "centerPolicy": "one-reference-per-parent"}
HH_NAME = re.compile(r"^HH\s*(\d+)(.*)$", re.I)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, allow_nan=False,
                       separators=(",", ":")) + "\n").encode()


def load(path):
    return json.loads(Path(path).read_text())


def rows(path):
    with Path(path).open(newline="") as stream:
        return list(csv.DictReader(stream))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def position(ra, dec, role="parent_center", input_frame="ICRS"):
    try:
        ra, dec = float(ra), float(dec)
    except (ValueError, TypeError):
        return None
    if not (math.isfinite(ra) and math.isfinite(dec) and 0 <= ra < 360 and -90 <= dec <= 90):
        return None
    return {"raDeg": ra, "decDeg": dec, "frame": "ICRS", "equinox": "J2000",
            "inputFrame": input_frame, "role": role, "epoch": None,
            "uncertaintyArcsec": None, "precisionArcsec": None}


def contained(center, positions, width=2.24, height=3.99):
    """Gnomonic rectangle; handles wrap/poles and rejects the back hemisphere."""
    require(0 < width < 180 and 0 < height < 180, "invalid footprint")
    if not positions:
        return np.array([], dtype=bool)
    ra0, dec0 = np.deg2rad(center)
    ra, dec = np.deg2rad(np.array(positions).T)
    dra = ra - ra0
    denominator = np.sin(dec0) * np.sin(dec) + np.cos(dec0) * np.cos(dec) * np.cos(dra)
    with np.errstate(divide="ignore", invalid="ignore"):
        x = np.cos(dec) * np.sin(dra) / denominator
        y = (np.cos(dec0) * np.sin(dec) - np.sin(dec0) * np.cos(dec) * np.cos(dra)) / denominator
    return ((denominator > 0) & (abs(x) <= math.tan(math.radians(width / 2)) + 1e-12)
            & (abs(y) <= math.tan(math.radians(height / 2)) + 1e-12))


def source_allowed(rights, source, field, excluded=()):
    decision = rights["sources"].get(source, {})
    return (source not in excluded and decision.get("status") == "cleared"
            and bool(decision.get("license")) and bool(decision.get("evidenceURL"))
            and field in decision.get("allowedFields", []))


def natural(value):
    return re.sub(r"\d+", lambda match: match[0].zfill(10), value)


def read_simbad(path, retrieved):
    records, conflicts = [], []
    input_hash = sha(path)
    seen = set()
    for row in rows(path):
        oid = str(int(row["oid"]))
        require(oid not in seen, f"duplicate SIMBAD OID {oid}")
        seen.add(oid)
        aliases = sorted(set(x.strip() for x in row["ids"].split("|") if x.strip()))
        numbered = [x for x in aliases if HH_NAME.match(x)]
        if row["otype"] != "HH":
            if numbered:
                conflicts.append({"oid": oid, "mainType": row["otype"],
                                  "hhAliases": numbered, "decision": "exclude-main-type-not-HH"})
            continue
        preferred = row["main_id"].strip()
        numbers = {int(HH_NAME.match(x)[1]) for x in numbered}
        if len(numbers) > 1:
            conflicts.append({"oid": oid, "hhAliases": numbered,
                              "decision": "quarantine-ambiguous-parent"})
            continue
        name = preferred if HH_NAME.match(preferred) else (min(numbered, key=lambda x: (len(x), x)) if numbered else preferred)
        match = HH_NAME.match(name)
        parent = f"hh:{int(match[1])}" if match else f"hh:simbad:{oid}"
        is_component = bool(match and match[2].strip())
        record_id = f"{parent}:component:simbad-{oid}" if is_component else parent
        records.append({"id": record_id, "group": parent,
                        "parentID": parent if is_component else None,
                        "name": name, "aliases": aliases, "kind": "component" if is_component else "parent",
                        "classification": {"source": "SIMBAD", "mainType": "HH", "status": "source-classified",
                                           "conflict": False, "confirmation": "not-independent-spectroscopic-confirmation"},
                        "position": position(row["ra"], row["dec"], "component_center" if is_component else "parent_center"),
                        "provenance": [{"source": "SIMBAD", "sourceID": oid, "retrievedAt": retrieved,
                                        "inputSHA256": input_hash, "sourceURL": "https://simbad.cds.unistra.fr/simbad/"}]})
    return records, conflicts


def read_v104(path, retrieved):
    records = []
    input_hash = sha(path)
    for line in Path(path).read_text().splitlines():
        if not line.startswith("HH"):
            continue
        number = int(line[3:6])
        ra = 15 * (float(line[27:29]) + float(line[30:32]) / 60 + float(line[33:37]) / 3600)
        dec = (float(line[39:41]) + float(line[42:44]) / 60 + float(line[45:47]) / 3600) * (-1 if line[38] == "-" else 1)
        coord = SkyCoord(ra * u.deg, dec * u.deg, frame=FK4(equinox=Time("B1950"))).transform_to(ICRS())
        record_id = f"hh:{number}"
        records.append({"id": record_id, "group": record_id, "parentID": None,
                        "name": f"HH {number}", "aliases": [line[7:27].strip()] if line[7:27].strip() else [],
                        "kind": "parent", "classification": {"source": "V104", "mainType": "HH",
                        "status": "historical-source-listed", "conflict": False,
                        "confirmation": "not-independent-spectroscopic-confirmation"},
                        "position": position(coord.ra.deg, coord.dec.deg, input_frame="FK4/B1950"),
                        "provenance": [{"source": "V104", "sourceID": str(number), "retrievedAt": retrieved,
                                        "inputSHA256": input_hash, "sourceURL": "https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/V/104"}]})
    require(len({r["id"] for r in records}) == len(records), "duplicate V104 parents")
    return records


def assemble(candidates, conflicts=()):
    """Reference selection is parent first, then SIMBAD, then natural name order.

    Positions from withheld sources cannot win selection in a deliverable build.
    Components never increase parent counts. Preserve all position alternatives.
    """
    grouped = collections.defaultdict(list)
    conflict_ids = {f"hh:{int(HH_NAME.match(alias)[1])}" for c in conflicts for alias in c.get("hhAliases", [])}
    for record in candidates:
        grouped[record["group"]].append(record)
    output = []
    for parent_id, entries in sorted(grouped.items()):
        entries.sort(key=lambda r: (r["kind"] != "parent", r["classification"]["source"] != "SIMBAD",
                                    natural(r["name"]), r["provenance"][0]["sourceID"]))
        located = [r for r in entries if r["position"]]
        selected = located[0] if located else entries[0]
        parent = {k: v for k, v in selected.items() if k != "group"}
        parent.update(id=parent_id, parentID=None, kind="parent",
                      name=f"HH {parent_id.split(':')[1]}" if not parent_id.startswith("hh:simbad:") else selected["name"])
        parent["classification"] = dict(parent["classification"], conflict=parent_id in conflict_ids)
        parent["aliases"] = sorted({x for r in entries for x in [r["name"], *r["aliases"]]})
        parent["provenance"] = [p for r in entries for p in r["provenance"]]
        parent["classifications"] = [r["classification"] for r in entries]
        parent["classifications"].extend({"source": "SIMBAD", "mainType": conflict["mainType"],
                                           "status": "source-classified", "conflict": True,
                                           "confirmation": "divergent classification preserved, not overwritten"}
                                          for conflict in conflicts if conflict.get("mainType")
                                          and any(f"hh:{int(HH_NAME.match(alias)[1])}" == parent_id
                                                  for alias in conflict.get("hhAliases", [])))
        parent["positionAlternatives"] = [{"position": r["position"], "provenance": r["provenance"]}
                                          for r in entries if r["position"]]
        if parent["position"] and selected["kind"] == "component":
            parent["position"] = dict(parent["position"], role="representative_component_proxy")
        output.append(parent)
        output.extend({k: v for k, v in r.items() if k != "group"} for r in entries if r["kind"] == "component")
    require(len({r["id"] for r in output}) == len(output), "duplicate record IDs")
    return sorted(output, key=lambda r: r["id"])


def read_catalog(path, identity_path, expected_sha):
    require(sha(path) == expected_sha, "catalog hash differs from research pin")
    with contextlib.closing(sqlite3.connect(f"file:{Path(path).resolve()}?mode=ro", uri=True)) as connection:
        metadata = dict(connection.execute("SELECT key,value FROM metadata"))
        dso = {name: position(float(ra) * 15 if ra is not None else None, dec)
               for name, ra, dec in connection.execute("SELECT object_id,ra_hours,dec_degrees FROM deep_sky_objects")}
    membership = rows(identity_path)
    require(len(membership) == len(dso), "identity map must cover every catalog row")
    require(len({r["member"] for r in membership}) == len(dso), "duplicate identity-map member")
    require({r["member"] for r in membership} == set(dso), "identity map/catalog mismatch")
    groups = collections.defaultdict(list)
    offsets = []
    for row in membership:
        require(row["representative"] in dso, "unknown representative")
        groups[row["representative"]].append(row["member"])
        offset = float(row["center_offset_arcmin"]) if row["center_offset_arcmin"] else math.nan
        if math.isfinite(offset) and offset > 1:
            offsets.append({"representative": row["representative"], "member": row["member"], "offsetArcmin": offset})
    for representative, members in groups.items():
        require(representative in members, "representative does not belong to own group")
    return groups, dso, {"version": metadata["catalog_version"], "sha256": sha(path),
                        "fingerprint": metadata["catalog_fingerprint"], "identityMapSHA256": sha(identity_path),
                        "identityPolicy": "research-20261004-exact-oid-or-reciprocal-alias-within-1arcmin; representative-center",
                        "rowCount": len(dso)}, offsets


def eligibility(records, groups, dsos):
    parents = [r for r in records if r["kind"] == "parent"]
    located = [r for r in parents if r["position"]]
    positions = [(r["position"]["raDeg"], r["position"]["decDeg"]) for r in located]
    links, covered, histogram = [], set(), collections.Counter()
    samples = {}
    unknown = 0
    for representative, members in sorted(groups.items()):
        center = dsos[representative]
        if center:
            mask = contained((center["raDeg"], center["decDeg"]), positions)
            ids = sorted(located[i]["id"] for i in np.flatnonzero(mask))
            covered.update(ids)
            histogram[len(ids)] += 1
        else:
            ids = None
            unknown += 1
        samples[representative] = None if ids is None else len(ids)
        for member in sorted(members):
            links.append({"targetID": member, "identityID": representative, "hhIDs": ids,
                          "status": "located" if center else "unknown"})
    eligible = [r for r in records if (r["parentID"] or r["id"]) in covered]
    counts = {"inputRecords": len(records), "parentGroups": len(parents), "locatedGroups": len(located),
              "unlocatedGroups": len(parents) - len(located), "coveredGroups": len(covered),
              "uncoveredLocatedGroups": len(located) - len(covered), "eligibleRecords": len(eligible),
              "dsoIdentities": len(groups), "locatedDSOIdentities": len(groups) - unknown,
              "unknownDSOIdentities": unknown, "hitDSOIdentities": sum(v for k, v in histogram.items() if k > 0),
              "pairs": sum(k * v for k, v in histogram.items()),
              "histogram": {str(k): histogram[k] for k in range(max(histogram, default=0) + 1)},
              "samples": {name: samples.get(name) for name in ["NGC7000", "IC5070", "IC5067", "NGC281", "M8", "M20", "M42", "M78", "NGC1333", "IC348"]}}
    return eligible, sorted(links, key=lambda r: r["targetID"]), counts


def optional_records(records, family, core_ids, rights, excluded):
    output = []
    for record in records:
        if record["id"] not in core_ids:
            continue
        if family == "enrichment":
            fields = {name: value for name, value in record["fields"].items()
                      if source_allowed(rights, value["source"], name, excluded)}
            if fields:
                output.append({"id": record["id"], "fields": fields})
        elif (source_allowed(rights, record["source"], "media", excluded)
              and record["reuseVerified"] and record["identityVerified"]):
            output.append(record)
    return sorted(output, key=lambda r: (r["id"], r.get("assetID", "")))


def image_audit(ids, candidates, rights, excluded):
    ids = set(ids)
    eligible = [r for r in candidates if r["id"] in ids]
    found = {r["id"] for r in eligible}
    reusable = {r["id"] for r in eligible if r["reuseVerified"] and r["identityVerified"]
                and source_allowed(rights, r["source"], "media", excluded)}
    by_role = {}
    for role in ["dedicated", "regional_identified", "survey_cutout"]:
        subset = [r for r in eligible if r["role"] == role]
        by_role[role] = {"foundHHs": len({r["id"] for r in subset}),
                         "reusableHHs": len({r["id"] for r in subset if r["id"] in reusable
                            and r["reuseVerified"] and source_allowed(rights, r["source"], "media", excluded)}),
                         "assets": len({r["assetID"] for r in subset})}
    return {"denominator": len(ids), "foundHHs": len(found), "reusableHHs": len(reusable),
            "deduplicatedFoundAssets": len({r["assetID"] for r in eligible}),
            "noVerifiedReusableImage": len(ids - reusable), "roles": by_role,
            "noImageIDs": sorted(ids - reusable), "examples": eligible,
            "scope": "Only checked-in official archive inventory searched; no-image means no suitable verified asset in that inventory, not proof no image exists anywhere."}


def validate_packages(packages, rights, excluded=()):
    for family, package in packages.items():
        schema = load(SOURCE / f"hh-{family}-v1.schema.json")
        Draft202012Validator(schema).validate(package)
        require(len(encoded(package)) <= LIMITS[family], f"{family} exceeds size limit")
        require(len(package["records"]) <= 20000, "record limit exceeded")
    core = packages["core"]
    if any(p["source"] == "SIMBAD" for r in core["records"] for p in r["provenance"]):
        require(core.get("databaseLicense") == "ODbL-1.0", "SIMBAD derived database requires ODbL notice")
        require(core.get("databaseLicenseURL") == ODBL_URL, "missing database license URI")
        require(any(n["source"] == "SIMBAD" for n in core.get("sourceNotices", [])), "missing SIMBAD attribution")
    ids = {r["id"] for r in core["records"]}
    require(len(ids) == len(core["records"]), "duplicate core IDs")
    parents = {r["id"] for r in core["records"] if r["kind"] == "parent"}
    require(len(core["dsoLinks"]) <= 8000, "DSO link limit exceeded")
    targets = {r["targetID"] for r in core["dsoLinks"]}
    target_links = {r["targetID"]: r for r in core["dsoLinks"]}
    require(len(targets) == len(core["dsoLinks"]), "duplicate target links")
    require(core["footprint"] == FOOTPRINT, "unsupported static footprint")
    require(core["catalog"]["rowCount"] == len(targets), "catalog/link count mismatch")
    for record in core["records"]:
        require(record["kind"] == "parent" or record["parentID"] in parents, "orphan component")
        require((record["kind"] == "parent") == (record["parentID"] is None), "invalid parent identity")
        for item in record["provenance"]:
            require(source_allowed(rights, item["source"], "core", excluded), "uncleared core provenance")
        for alternative in record.get("positionAlternatives", []):
            for item in alternative["provenance"]:
                require(source_allowed(rights, item["source"], "core", excluded), "uncleared position alternative")
        for classification in [record["classification"], *record.get("classifications", [])]:
            require(source_allowed(rights, classification["source"], "core", excluded), "uncleared classification")
    linked_parents = set()
    for link in core["dsoLinks"]:
        require(link["identityID"] in targets, "missing identity representative")
        if link["status"] == "unknown":
            require(link["hhIDs"] is None, "unknown location must not have zero count")
        else:
            require(link["hhIDs"] is not None, "located link missing count")
            require(len(set(link["hhIDs"])) == len(link["hhIDs"]), "duplicate parent count")
            require(set(link["hhIDs"]) <= parents, "link references non-parent or unknown HH")
            linked_parents.update(link["hhIDs"])
        representative = target_links[link["identityID"]]
        require(link["status"] == representative["status"] and link["hhIDs"] == representative["hhIDs"],
                "alias count differs from representative")
    require(linked_parents == parents, "core contains ineligible parents")
    for family in ["enrichment", "media"]:
        seen = set()
        for record in packages[family]["records"]:
            require(record["id"] in ids, "unknown optional join")
            key = record.get("assetID", record["id"])
            require(key not in seen, "duplicate optional identity")
            seen.add(key)
            if family == "enrichment":
                for name, field in record["fields"].items():
                    require(source_allowed(rights, field["source"], name, excluded), "uncleared enrichment")
                    require(field["license"] == rights["sources"][field["source"]]["license"], "license mismatch")
                    if name == "distance" and field["value"] and field["value"]["range"]:
                        require(field["value"]["range"][0] <= field["value"]["range"][1], "reversed distance range")
            else:
                require(source_allowed(rights, record["source"], "media", excluded), "uncleared media")
                require(record["reuseVerified"] and record["identityVerified"], "unverified media")
                require(record["license"] == rights["sources"][record["source"]]["license"], "license mismatch")


def write_packages(destination, packages, rights, excluded=()):
    validate_packages(packages, rights, excluded)
    destination = Path(destination)
    require(not destination.resolve().is_relative_to((ROOT / "v1").resolve()), "hosted output forbidden; stage outside v1")
    destination.mkdir(parents=True, exist_ok=True)
    descriptors = []
    for family, package in packages.items():
        filename = f"hh-{family}-v1.json"
        data = encoded(package)
        (destination / filename).write_bytes(data)
        descriptors.append({"family": f"hh-{family}", "schemaVersion": 1,
                            "packageVersion": package["packageVersion"], "path": filename,
                            "sha256": hashlib.sha256(data).hexdigest(), "byteSize": len(data),
                            "recordCount": len(package["records"]), "maxByteSize": LIMITS[family],
                            "fallback": "bundled-compatible-core" if family == "core" else "absent-is-valid"})
    manifest = {"schemaVersion": 1, "delivery": "local-review-only-not-stable-channel",
                "catalog": packages["core"]["catalog"], "packages": descriptors}
    (destination / "manifest.json").write_bytes(encoded(manifest))
    notices = "# HH Companion Notices\n\n"
    if packages["core"].get("databaseLicense"):
        notices += ("Contains information from CDS/SIMBAD, made available under the Open Database License (ODbL).\n"
                    "Source: https://simbad.cds.unistra.fr/simbad/\n"
                    f"Derived HH companion database: ODbL-1.0, {ODBL_URL}\n"
                    "Credit: Wenger et al. (2000), A&AS 143, 9, 2000A&AS..143....9W.\n"
                    "This stage is not public distribution. Before public app use, provide recipients the\n"
                    "machine-readable derived companion free online under ODbL, or its complete alteration\n"
                    "method/data; preserve notices and offer an unencumbered copy if app distribution\n"
                    "imposes additional terms/technological restrictions. Do not fold it into canonical parquet.\n\n")
    notices += "Optional enrichment and imagery retain their per-field/per-asset licenses and full credits.\n"
    (destination / "NOTICE.md").write_text(notices)
    validate_directory(destination, rights, excluded)


def validate_directory(destination, rights, excluded=()):
    destination = Path(destination)
    manifest = load(destination / "manifest.json")
    require(manifest["schemaVersion"] == 1, "unsupported manifest")
    require({d["family"] for d in manifest["packages"]} == {"hh-core", "hh-enrichment", "hh-media"}, "missing families")
    require(len(manifest["packages"]) == 3, "duplicate manifest family")
    packages = {}
    for descriptor in manifest["packages"]:
        family = descriptor["family"].removeprefix("hh-")
        require(descriptor["path"] == f"hh-{family}-v1.json", "invalid package path")
        path = destination / descriptor["path"]
        data = path.read_bytes()
        require(len(data) == descriptor["byteSize"] <= LIMITS[family], "byte-size mismatch/limit")
        require(hashlib.sha256(data).hexdigest() == descriptor["sha256"], "checksum mismatch")
        packages[family] = load(path)
        require(packages[family]["packageVersion"] == descriptor["packageVersion"], "version mismatch")
        require(packages[family]["schemaVersion"] == descriptor["schemaVersion"] == 1, "schema mismatch")
        require(len(packages[family]["records"]) == descriptor["recordCount"], "record-count mismatch")
    require(packages["core"]["catalog"] == manifest["catalog"], "catalog pin mismatch")
    validate_packages(packages, rights, excluded)
    return packages


def build(args):
    research = args.research
    provenance = load(research / "provenance.json")
    independent = research / "private_sources"
    pins = load(args.pins)
    rights = load(args.rights)
    excluded = set(args.exclude_source)
    require(excluded <= set(rights["sources"]), "unknown excluded source")
    require(sha(research / "dso_identity_groups.csv") == pins["identityMapSHA256"], "identity map changed")
    source_files = {"SIMBAD": ["simbad_full.csv", "simbad_hh_named.csv"], "V104": ["V104_catalog.dat"]}
    pinned_files = [independent / name for source, names in source_files.items() if source not in excluded for name in names]
    for path in pinned_files:
        require(sha(path) == pins["sourceHashes"][path.name] == provenance["source_hashes"][path.name], f"source hash changed: {path.name}")
    pin = next(v["sha256"] for k, v in provenance["files"].items() if k.endswith("catalog.sqlite"))
    require(pin == pins["catalogSHA256"], "catalog provenance changed")
    groups, dsos, catalog, offsets = read_catalog(args.catalog, research / "dso_identity_groups.csv", pin)
    require(catalog["version"] == pins["catalogVersion"], "catalog version changed")
    simbad, conflicts, v104 = [], [], []
    if "SIMBAD" not in excluded:
        simbad, conflicts = read_simbad(independent / "simbad_full.csv", provenance["retrieval_date"])
        _, named_conflicts = read_simbad(independent / "simbad_hh_named.csv", provenance["retrieval_date"])
        conflicts = list({encoded(conflict): conflict for conflict in conflicts + named_conflicts}.values())
    if "V104" not in excluded:
        v104 = read_v104(independent / "V104_catalog.dat", provenance["retrieval_date"])
    candidates = simbad + v104
    audit_records = assemble([r for r in candidates if r["provenance"][0]["source"] not in excluded], conflicts)
    audit_eligible, _, audit_counts = eligibility(audit_records, groups, dsos)
    accepted = [r for r in candidates if source_allowed(rights, r["provenance"][0]["source"], "core", excluded)]
    records, links, counts = eligibility(assemble(accepted, conflicts), groups, dsos)
    core_ids = {r["id"] for r in records}
    packages = {"core": {"schemaVersion": 1, "packageVersion": args.version, "records": records,
                         "catalog": catalog, "footprint": FOOTPRINT, "dsoLinks": links}}
    admitted_sources = sorted({p["source"] for r in records for p in r["provenance"]})
    packages["core"]["sourceNotices"] = [{"source": source, "credit": rights["sources"][source]["credit"],
                                         "license": rights["sources"][source]["license"],
                                         "evidenceURL": rights["sources"][source]["evidenceURL"]} for source in admitted_sources]
    if "SIMBAD" in admitted_sources:
        packages["core"].update(databaseLicense="ODbL-1.0", databaseLicenseURL=ODBL_URL)
    for family in ["enrichment", "media"]:
        input_path = args.enrichment if family == "enrichment" else args.media
        packages[family] = {"schemaVersion": 1, "packageVersion": getattr(args, f"{family}_version") or args.version,
                            "records": optional_records(load(input_path)["records"], family, core_ids, rights, excluded)}
    write_packages(args.output, packages, rights, excluded)
    audit_ids = {r["id"] for r in audit_eligible if r["kind"] == "parent"}
    media_audit = image_audit(audit_ids, load(args.media)["records"], rights, excluded)
    report = {"schemaVersion": 1, "scope": "local analysis; no source positions/prose/images redistributed in this report",
              "inputs": {p.name: sha(p) for p in [*pinned_files, research / "dso_identity_groups.csv", args.pins, args.rights, args.enrichment, args.media]},
              "catalog": catalog, "footprint": FOOTPRINT, "independentResearchCounts": audit_counts,
              "deliveryCounts": counts, "excludedSources": sorted(excluded | {"Chen2026"}),
              "scopeLoss": {"independentGroupsOmitted": sorted(audit_ids - {r["id"] for r in records if r["kind"] == "parent"}),
                            "pairDelta": audit_counts["pairs"] - counts["pairs"],
                            "hitDSODelta": audit_counts["hitDSOIdentities"] - counts["hitDSOIdentities"],
                            "policy": "Omit rather than invent replacement coordinates or grants. Chen-only loss is separate and reported in handoff, not imported."},
              "withheldSources": sorted(s for s in rights["sources"] if not source_allowed(rights, s, "core", excluded)
                                         and s in {"SIMBAD", "V104", "Chen2026"}),
              "classificationConflictCount": len(conflicts),
              "runtimeHeroAudit": image_audit({r["id"] for r in records if r["kind"] == "parent"},
                                             load(args.media)["records"], rights, excluded),
              "classificationPolicy": "exclude SIMBAD main types other than HH; flag historical HH parents with divergent SIMBAD aliases; ambiguous numbered parents quarantined",
              "dsoCenterOffsetsOver1Arcmin": offsets,
              "heroAudit": media_audit,
              "replacementScope": "Chen2026 positions, prose and derived tables never read. Replacements must supply independently verified source rights and identity evidence."}
    args.audit_output.parent.mkdir(parents=True, exist_ok=True)
    args.audit_output.write_bytes(encoded(report))
    print(json.dumps({"output": str(args.output), "audit": str(args.audit_output),
                      "independentCounts": {k: v for k, v in audit_counts.items() if k != "histogram"},
                      "deliveryCounts": {k: v for k, v in counts.items() if k != "histogram"},
                      "images": {k: v for k, v in media_audit.items() if k not in {"noImageIDs", "examples"}}}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--research", type=Path)
    parser.add_argument("--catalog", type=Path)
    parser.add_argument("--rights", type=Path, default=SOURCE / "rights.json")
    parser.add_argument("--pins", type=Path, default=SOURCE / "input-pins.json")
    parser.add_argument("--enrichment", type=Path, default=SOURCE / "enrichment.json")
    parser.add_argument("--media", type=Path, default=SOURCE / "media-candidates.json")
    parser.add_argument("--exclude-source", action="append", default=[])
    parser.add_argument("--version", default="2026-10-04.1")
    parser.add_argument("--enrichment-version")
    parser.add_argument("--media-version")
    parser.add_argument("--output", type=Path, default=ROOT / "outputs/hh/review")
    parser.add_argument("--audit-output", type=Path, default=ROOT / "reports/hh/latest.json")
    parser.add_argument("--validate", type=Path)
    args = parser.parse_args()
    if args.validate:
        validate_directory(args.validate, load(args.rights), args.exclude_source)
        print("HH packages validated")
    else:
        if not args.research or not args.catalog:
            parser.error("--research and --catalog required")
        build(args)


if __name__ == "__main__":
    main()
