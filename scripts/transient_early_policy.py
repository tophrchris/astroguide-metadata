"""Local, evidence-only early opportunity evaluation; no publication side effects."""
import datetime as dt
import hashlib
import json
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class RisePolicy:
    # Exploratory defaults, NOT approved for automatic publication.
    minimum_rate: float = 0.3
    minimum_significance: float = 3.0
    minimum_days: float = 0.25
    maximum_days: float = 7.0
    maximum_age_days: float = 3.0

    def __post_init__(self):
        values = (self.minimum_rate, self.minimum_significance, self.minimum_days,
                  self.maximum_days, self.maximum_age_days)
        if not all(math.isfinite(value) and value > 0 for value in values) or self.maximum_days < self.minimum_days:
            raise ValueError("Rise policy requires finite positive thresholds and an ordered interval")


def date(value):
    try:
        result = dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return result if result.tzinfo else None
    except ValueError:
        return None


def evaluate(candidate, *, now, policy=RisePolicy()):
    """Distinguish score eligibility from a measured crossing; fail closed."""
    if not isinstance(now, dt.datetime) or now.tzinfo is None:
        raise ValueError("Evaluation requires an explicit timezone-aware reference time")
    reasons = []
    audit = []
    kind = candidate.get("classification", {}).get("kind")
    if (kind in {"contaminant", "unsupported"}
            or candidate.get("recommendedDecision") == "reject"
            or candidate.get("decisionReason")):
        return [], ["protected_or_invalid"]
    classification = candidate.get("classification", {})
    type_name = str(classification.get("type") or "").strip()
    classified = bool(type_name) and not any(token in type_name.lower() for token in ("?", "candidate", "unclassified"))
    score = candidate.get("score")
    valid_score = isinstance(score, (int, float)) and not isinstance(score, bool) and math.isfinite(score) and 0 <= score <= 100
    if not valid_score:
        audit.append("missing_or_invalid_score")
    if classified and kind in {"supernova", "superluminous_supernova", "nova", "tidal_disruption_event"} and valid_score and score >= 70:
        reasons.append({"code": "classified_score", "score": candidate["score"],
                        "classification": classification, "sourceURL": candidate.get("sourceURL"),
                        "triggeredAtUTC": candidate.get("lastModifiedUTC") or candidate.get("discovery", {}).get("dateUTC"),
                        "evidence": [], "confidence": "score_eligibility", "automaticEligible": True})
    valid = []
    for item in candidate.get("tnsContext", {}).get("publicPhotometry", []):
        stamp = date(item.get("observationDateUTC"))
        value, error = item.get("value"), item.get("error")
        if (not stamp or not item.get("band") or not item.get("source")
                or item.get("isUpperLimit") or item.get("units") != "mag"
                or not item.get("system") or not item.get("correction")
                or not all(isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) for x in (value, error))
                or error <= 0 or stamp > now):
            audit.append("incompatible_or_incomplete_photometry")
            continue
        valid.append((stamp, item))
    valid.sort(key=lambda pair: (pair[0], json.dumps(pair[1], sort_keys=True)))
    for index, (end, second) in enumerate(valid):
        for start, first in valid[:index]:
            if any(first[k] != second[k] for k in ("band", "system", "correction")):
                continue
            days = (end - start).total_seconds() / 86400
            if not policy.minimum_days <= days <= policy.maximum_days or (now - end).total_seconds() / 86400 > policy.maximum_age_days:
                continue
            delta = first["value"] - second["value"]
            uncertainty = math.hypot(first["error"], second["error"])
            if delta / days >= policy.minimum_rate and delta / uncertainty >= policy.minimum_significance:
                reasons.append({"code": "rapid_rise", "triggeredAtUTC": second["observationDateUTC"],
                                "rateMagnitudePerDay": delta / days, "rateUncertainty": uncertainty / days,
                                "band": second["band"], "confidence": "provisional_measured_rise",
                                "automaticEligible": False, "evidence": [first, second]})
                break
        if reasons and reasons[-1]["code"] == "rapid_rise":
            break  # Earliest qualifying pair remains stable on append-only refreshes.
    for reason in reasons:
        identity = [candidate["id"], reason["code"], reason["evidence"]]
        reason["stableTriggerID"] = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
    return reasons, audit
