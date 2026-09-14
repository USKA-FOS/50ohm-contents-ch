# Analyse de `Review_result.xlsx`

Date de l'analyse : 2026-08-21

## Périmètre

- 174 dessins examinés ;
- français : 152 `Ok`, 17 `partially translated`, 3 `other`,
  1 `Not translated`, 1 sans décision ;
- italien : 153 `Ok`, 16 `partially translated`, 3 `other`,
  1 `Not translated`, 1 sans décision ;
- 21 lignes comportent un commentaire ;
- le dessin `1075` est le seul dessin sans décision.

## Causes identifiées

| Dessin | Cause observée |
| --- | --- |
| 202 | Les libellés des courbes ont été traduits, mais l'extracteur ne couvre pas les propriétés PGFPlots `xlabel` et `ylabel`. Elles restent donc en allemand dans les TeX français et italiens. Ce dessin n'est pas une simple copie PDF. |
| 260, 315, 954 | `MWS` dispose de traductions approuvées, mais ses trois candidats sont marqués `to_be_translated=false`. |
| 434, 435 | `Auf das`, `Störsignal` et `abgestimmt` ont été traduits indépendamment alors qu'ils forment une phrase visuelle répartie sur trois lignes. L'ordre et la casse doivent être corrigés ensemble. |
| 438 | `D/A Umsetzer` a été traduit par `Convertisseur N/A` en français. Il s'agit d'une erreur terminologique. |
| 439 | `6 dB Verstärkung` a produit `6 dB d'amplification`. Le réviseur décide finalement de conserver ce résultat. |
| 471 | Le SVG allemand mesure `707.636 x 211.2 pt`, contre environ `299 x 80` pour les variantes localisées. Le renderer impose actuellement une largeur générique de 9 cm au lieu de préserver les propriétés du dessin allemand. |
| 496 | `HF-Diode` a été extrait, puis marqué `to_be_translated=false`. Il reste identique dans les variantes localisées. |
| 501 | `Kontrollsignale`, `Steuer- und` et les deux lignes audio sont traduits séparément malgré leur dépendance sémantique. `Steuer-` doit employer le terme français `commande`, pas `contrôle`. |
| 628 | `Ort` a été traduit par `emplacement`. Le réviseur demande `position` en français ; l'italien est accepté. |
| 680 | La traduction est correcte, mais la phrase localisée est trop longue pour la ligne unique conservée par l'import. Une coupure contrôlée est nécessaire. |
| 689 | La photo canonique 205 contient déjà les libellés allemands. Le TeX ajoute une seconde couche de texte. Les deux couches se confondent en allemand et se superposent visiblement en français et en italien. |
| 694 | `Spannungsmessgerät` a été traduit par une périphrase. Le réviseur demande `voltmètre`. |
| 808 | Le libellé mathématique `$f_\text{ZF}$` est traité comme un token protégé. Les traductions `ZF -> FI/IF` présentes dans le glossaire ne lui sont donc pas appliquées. |
| 810 | `HF`, `1.ZF`, `2.ZF` et `NF` sont des valeurs Circuitikz non entourées d'accolades. L'extracteur Circuitikz ne couvre actuellement que les valeurs entre accolades. |
| 828 | `Eingangssignal`, `Verstärkung` et `Ausgangssignal` se trouvent dans des propriétés PGFPlots `title={...}` non prises en charge par l'extracteur. Seul le nœud `Begrenzung` est traduit. |
| 1004 | `Reales Spannungsmessgerät` utilise la même périphrase que 694 au lieu de `voltmètre réel`. |
| 1007 | `Reales Strommessgerät` utilise une périphrase au lieu de `ampèremètre réel`. Aucune entrée exacte `Strommessgerät` n'existe actuellement dans le glossaire. |
| 1072 | `\textcolor{DARCblue}{phys. Stromrichtung!}` est extrait comme `DARCblue phys. Stromrichtung!`, puis marqué `to_be_translated=false`. Le nom de couleur est confondu avec le texte visible. |
| 1075 | Aucune décision de revue n'est enregistrée dans le classeur. Ce cas n'est pas classé comme erreur. |

## Familles de correction

Corrections de glossaire ou de traduction approuvée :

- 438, 628, 694, 1004 et 1007 ;
- 496 après activation explicite du candidat ;
- 439 est désormais accepté sans correction.

Corrections d'extraction ou d'import :

- propriétés PGFPlots : 202 et 828 ;
- token mathématique localisable : 808 ;
- valeurs Circuitikz sans accolades : 810 ;
- contenu visible enveloppé dans `\textcolor` : 1072 ;
- candidats désactivés : 260, 315, 954 et 496.

Corrections contextuelles ou graphiques :

- phrases réparties sur plusieurs nœuds : 434, 435 et 501 ;
- largeur de rendu : 471 ;
- coupure de ligne : 680 ;
- image allemande déjà annotée : 689.

## Contrainte de validation

Les fichiers localisés doivent conserver la structure et les propriétés
graphiques du TeX allemand. Seuls les textes explicitement approuvés peuvent
changer. Le succès de la compilation et l'égalité structurelle actuelle ne
suffisent pas à valider la mise en page finale.

## État des corrections du 2026-08-21

- Les corrections TeX approuvées ont été appliquées à `260`, `315`, `434`,
  `435`, `438`, `496`, `501`, `628`, `680`, `694`, `808`, `810`, `828`, `868`,
  `869`, `918`, `954`, `1004`, `1007`, `1008` et `1072`.
- Les traductions `OW` sont conservées sur deux lignes lorsque la source
  contient deux informations, par exemple `1ère HS\\H2` et `prima AS\\H2`.
- Les 20 TeX issus du dernier import ciblé ont passé la validation structurelle
  sans anomalie.
- `202` reste en attente d'une traduction éditorialement approuvée pour
  `Frequenz [MHz]` et
  `Grunddämpfung a_0 je 100 m Leitungslänge in dB`. L'extracteur prend désormais
  correctement ces propriétés PGFPlots en charge.
- `689` exige une correction manuelle de la photo canonique allemande déjà
  annotée; la superposition ne peut pas être corrigée par une traduction TeX.
- `1075` a été confirmé correct par le réviseur; aucune correction n'est
  nécessaire.

## Revue du 2026-08-22

La deuxième revue contient 174 dessins: 168 sont entièrement validés et six
comportent encore une remarque (`202`, `501`, `689`, `866`, `1002`, `1072`).

Corrections déterministes intégrées dans les TeX FR/IT:

- `202`: `Frequenz [MHz]` devient `Fréquence [MHz]` et `Frequenza [MHz]`;
- `501`: la phrase complète est répartie sur deux lignes comme `Signaux de
  commande / et de contrôle` et `Segnali di comando / e di controllo`;
- `866`: l'indication d'environ 1000 km passe sur une seconde ligne, alignée
  sous `longue` ou `lunga` avec `\phantom`;
- `1002`: `Direction physique/technique du courant` et les équivalents italiens;
- `1072`: `sens` est remplacé par `direction` en français.

Le nouveau fichier `canonical/photos/ph_24f64631b390/205.de.png` de `689` a été
inspecté: les annotations incorporées ont été retirées correctement. Aucun
travail graphique manuel supplémentaire n'est nécessaire; les trois SVG
doivent seulement être régénérés.

Le résidu `202` a ensuite été résolu par les entrées validées du glossaire:

- FR: `Atténuation de base a_0 par 100 m de longueur de câble en dB`;
- IT: `Attenuazione di base a_0 per 100 m di lunghezza del cavo in dB`.

Le token TeX protégé `a_0`, les formats `\textbf`/`\large` et l'espacement
`100\,m` sont conservés dans les TeX reconstruits. Il ne reste aucune
correction manuelle identifiée dans cette revue; une validation visuelle des
nouveaux SVG reste nécessaire après rendu.
