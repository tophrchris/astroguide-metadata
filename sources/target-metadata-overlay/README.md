# Target Metadata Overlay Sources

This folder stores human-curated source inputs for the target metadata overlay
package published under `v1/packages/target-metadata`.

The runtime app does not read these spreadsheets directly. They are versioned
here so the curated source material used to build the JSON package stays close
to the metadata publication workflow and can be reviewed through pull requests.

## 2026-05 Curated Workbooks

`2026-05-curated-workbooks/` contains the workbook names cited by
`target_metadata_overlay_v1.json` source citations:

- `seasonal_nebula_targets_southern_hemisphere_expanded.xlsx`
- `galaxy_halpha_consolidated_index_v2.xlsx`

The overlay also cites GitHub issue/comment sources for media overrides and
alias fixes; those remain linked in the JSON citation fields rather than copied
as spreadsheet inputs.
