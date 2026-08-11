# Comet Orbit Geometry v1

The `cometOrbitGeometry` package family publishes lightweight heliocentric
orbit and trajectory geometry for the same curated comet stable IDs used by
`cometSnapshot`.

This family is intentionally separate from `cometSnapshot`:

- `cometSnapshot` carries geocentric RA/Dec/magnitude samples for comet search,
  list, and sky-position behavior.
- `cometOrbitGeometry` carries heliocentric path vectors, dated heliocentric
  samples, rendering intent, and a planning tail model for Solar System Comet
  Mode visualizations.

## Package Shape

The stable manifest points directly at:

```text
v1/packages/comet-orbit-geometry/comet_orbit_geometry_v1.json
```

The generated `2026-08-11` package contains 20 records:

- 12 `closedOrbit` records
- 8 `trajectoryArc` records
- 3,514 total path samples
- 2,460 total dated samples

Each record is keyed by `stableID`, for example `COMET:10P`, and preserves the
same stable ID set as the comet snapshot seed bundle.

## Coordinates And Samples

Path and dated samples use the `heliocentric-ecliptic-j2000-au` frame:

- origin: Sun
- plane: ecliptic
- equinox: J2000
- unit: astronomical units
- path sample row: `[xAU, yAU, zAU]`
- dated sample row: `[julianDate, xAU, yAU, zAU]`

These vectors are planning/rendering metadata generated from osculating SBDB
elements. They are not precision navigation products.

## Rendering Policy

The generator validates rendering kind explicitly:

- `closedOrbit` is only for periodic, reasonably closed short-period comet
  records, and the path samples must close.
- `trajectoryArc` is used for long-period, non-periodic, hyperbolic, parabolic,
  or poorly closed objects.

Clients should not turn a `trajectoryArc` record into a fake closed loop.

## Tail Model

Records include a small anti-solar planning envelope:

```json
{
  "direction": "antiSolar",
  "extent": "estimatedPlanningEnvelope",
  "estimatedLengthDegrees": 1.5
}
```

The app should compute actual anti-solar sky orientation at display time.

## Rebuild And Validation

```bash
scripts/build_comet_orbit_geometry_package.py \
  --app-repo ../DSOPlanneriOS \
  --generated-at 2026-08-11T00:00:00Z

scripts/build_comet_orbit_geometry_package.py --validate-only
```

The builder writes compact JSON, updates the stable manifest descriptor, and
validates record shape, stable-ID coverage, rendering kind, sample frames,
sample array shape, byte size, and SHA-256 checksum.

## iOS Boundary

Existing app builds ignore this unknown manifest family. DSOPlanneriOS follow-up
for comet mode should add the dynamic metadata family, remote-package decoding,
and bundled/cache fallback behavior while retaining bundled orbit geometry as
the offline release-safety baseline.
