# ISQ Source Changes

This file records source corrections that must remain explicit when an
upstream import changes a reference without preserving the referenced asset.

## 2026-09-17: drawing 689 photo reference

- `canonical/drawings/dr_cd00c6e1a305/689.de.tex` changed from `foto/205` to
  `foto/6` during commit `a9bdfe7ac` (`Import German source revision
  0ebada583d`), while the French and Italian TeX files still reference
  `foto/205`.
- The photo object for `205` was also modified by that import. The previous
  `205.de.png` blob was `a98ad3981eeb8971ee9cf67a70080768735c0e3c`; the current
  imported blob is `9a96dfae5a3dd6eefe0e338c8293216504fc6809`.
- To preserve the previous rendering for the new German reference, the
  previous `205.de.png` was copied to
  `canonical/photos/ph_24f64631b390/6.de.png`.
- The renderer now treats additional `<number>.<language>.png` files in the
  same photo object as explicit filename aliases. Thus `foto/6` resolves to
  `6.de.png`, while `foto/205` continues to resolve to the current
  `205.de.png`.

This entry must be reported with the source import because it is a source
change, not a translation change.
