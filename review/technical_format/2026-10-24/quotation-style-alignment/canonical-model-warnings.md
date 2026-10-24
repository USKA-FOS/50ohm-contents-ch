# Les 29 avertissements du modèle canonical

État examiné : `bc3b62010c8b391d32d0ffe4d293e3232c516d27` et copie de travail actuelle. Le validateur signale 0 erreur et 29 avertissements.

Chaque avertissement indique une variante média présente dans `language_variants` dont la langue est absente de `languages`. Le contrôle des fichiers est distinct : tous les fichiers référencés dans ces 29 variantes existent. Ces avertissements ne proviennent pas des corrections de guillemets.

| Type | Référence | Langues des variantes non déclarées | Liste `languages` actuelle | Nombre d’avertissements | Métadonnées |
|---|---|---|---|---:|---|
| drawing | 10100 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_282cdb8ff94d/object.meta.json` |
| drawing | 10101 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_3039187f43fa/object.meta.json` |
| drawing | 1041 | de | `[]` | 1 | `canonical/drawings/dr_7c39a7d3740a/object.meta.json` |
| drawing | 1082 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_13830c29cac5/object.meta.json` |
| drawing | 1092 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_32262151b7f6/object.meta.json` |
| drawing | 1095 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_e3abae4ad554/object.meta.json` |
| drawing | 1106 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_b8b65dadf6a9/object.meta.json` |
| drawing | 1113 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_69da6883c65d/object.meta.json` |
| drawing | 1114 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_129e63aed749/object.meta.json` |
| drawing | 1115 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_fcdd6fda24d5/object.meta.json` |
| drawing | 1130 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_8fa8caf5275a/object.meta.json` |
| drawing | 1131 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_527786b406d9/object.meta.json` |
| drawing | 1132 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_609f6c62a896/object.meta.json` |
| drawing | hb_101 | fr, it | `["de"]` | 2 | `canonical/drawings/dr_d48a39a547c5/object.meta.json` |
| photo | 160 | de | `[]` | 1 | `canonical/photos/ph_ea5526674369/object.meta.json` |
| photo | 331 | de | `[]` | 1 | `canonical/photos/ph_3af2091d8130/object.meta.json` |

## Cause dans les outils

`tools/export_canonical_model.py` construit `languages` à partir des langues des textes exportés (`exported_languages`), puis construit séparément `language_variants` à partir des médias. Un objet sans texte peut donc avoir `languages: []` et une image allemande ; un dessin avec une description allemande seule peut déclarer uniquement `de`, même si des médias français et italiens sont présents.

Les fonctions `update_meta_for_tex` dans `tools/import_drawing_tex_translations.py` et `update_meta_for_svg` dans `tools/render_localized_drawing_svgs.py` enrichissent les variantes médias sans réconcilier `languages`. Le validateur, lui, attend que chaque langue des variantes médias figure dans cette liste. Il existe donc un désaccord entre la manière de produire cette métadonnée et la règle de validation.

## Conséquences et correction à prévoir

Le build de sites actuel sélectionne les fichiers via `metadata.language_asset` dans `overlay_object_assets`, avec repli sur `de`. Cette sélection ne repose pas sur `languages`. Ces avertissements ne prouvent donc pas une perte d’image lors du build. Ils rendent néanmoins l’inventaire des langues incohérent ; un outil qui utilise uniquement `languages` pourrait ignorer une variante existante.

La correction cohérente proposée consiste à définir `languages` comme l’union des langues des textes et des variantes médias, à synchroniser les métadonnées concernées, puis à appliquer la même règle dans les outils d’export, d’import et de génération des SVG. Si `languages` devait intentionnellement décrire uniquement les textes, le contrat et le contrôle des variantes devraient au contraire être explicitement distingués. Aucune de ces corrections n’est appliquée dans ce compte rendu.

## Détail des variantes concernées

| Objet | Référence | Langue | Fichiers présents |
|---|---|---|---|
| `dr_129e63aed749` | 1114 | fr | `1114.fr.svg`, `1114.fr.tex` |
| `dr_129e63aed749` | 1114 | it | `1114.it.svg`, `1114.it.tex` |
| `dr_13830c29cac5` | 1082 | fr | `1082.fr.svg`, `1082.fr.tex` |
| `dr_13830c29cac5` | 1082 | it | `1082.it.svg`, `1082.it.tex` |
| `dr_282cdb8ff94d` | 10100 | fr | `10100.fr.svg`, `10100.fr.tex` |
| `dr_282cdb8ff94d` | 10100 | it | `10100.it.svg`, `10100.it.tex` |
| `dr_3039187f43fa` | 10101 | fr | `10101.fr.svg`, `10101.fr.tex` |
| `dr_3039187f43fa` | 10101 | it | `10101.it.svg`, `10101.it.tex` |
| `dr_32262151b7f6` | 1092 | fr | `1092.fr.svg`, `1092.fr.tex` |
| `dr_32262151b7f6` | 1092 | it | `1092.it.svg`, `1092.it.tex` |
| `dr_527786b406d9` | 1131 | fr | `1131.fr.svg`, `1131.fr.tex` |
| `dr_527786b406d9` | 1131 | it | `1131.it.svg`, `1131.it.tex` |
| `dr_609f6c62a896` | 1132 | fr | `1132.fr.svg`, `1132.fr.tex` |
| `dr_609f6c62a896` | 1132 | it | `1132.it.svg`, `1132.it.tex` |
| `dr_69da6883c65d` | 1113 | fr | `1113.fr.svg`, `1113.fr.tex` |
| `dr_69da6883c65d` | 1113 | it | `1113.it.svg`, `1113.it.tex` |
| `dr_7c39a7d3740a` | 1041 | de | `1041.de.svg`, `1041.de.tex` |
| `dr_8fa8caf5275a` | 1130 | fr | `1130.fr.svg`, `1130.fr.tex` |
| `dr_8fa8caf5275a` | 1130 | it | `1130.it.svg`, `1130.it.tex` |
| `dr_b8b65dadf6a9` | 1106 | fr | `1106.fr.svg`, `1106.fr.tex` |
| `dr_b8b65dadf6a9` | 1106 | it | `1106.it.svg`, `1106.it.tex` |
| `dr_d48a39a547c5` | hb_101 | fr | `hb_101.fr.svg`, `hb_101.fr.tex` |
| `dr_d48a39a547c5` | hb_101 | it | `hb_101.it.svg`, `hb_101.it.tex` |
| `dr_e3abae4ad554` | 1095 | fr | `1095.fr.svg`, `1095.fr.tex` |
| `dr_e3abae4ad554` | 1095 | it | `1095.it.svg`, `1095.it.tex` |
| `dr_fcdd6fda24d5` | 1115 | fr | `1115.fr.svg`, `1115.fr.tex` |
| `dr_fcdd6fda24d5` | 1115 | it | `1115.it.svg`, `1115.it.tex` |
| `ph_3af2091d8130` | 331 | de | `331.de.png` |
| `ph_ea5526674369` | 160 | de | `160.de.png` |
