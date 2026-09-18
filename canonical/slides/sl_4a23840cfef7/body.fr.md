<left>
* Au lieu d'une valeur numérique, un codage par anneaux de couleur est imprimé sur les résistances
* Chaque couleur correspond à une valeur numérique
  1. Anneau de couleur pour le 1er chiffre
  2. Anneau de couleur pour le 2e chiffre
  3. Anneau de couleur pour le multiplicateur
</left>
<right>
[picture:665:n_widerstandsfarbcodes: Une résistance avec 4 anneaux de couleur]
</right>

--- style="font-size: 0.6em;"
| X:Couleur | l:Valeur | l:Multiplicateur | l:Tolérance |
| Argent | - | $\num{0,01}$ | $\qty{\pm 10}{\percent}$ |
| Or | - | $\num{0,1}$ | $\qty{\pm 5}{\percent}$ |
| Noir | 0 | $\num{1}$ | - |
| Brun | 1 | $\num{10}$ | $\qty{\pm 1}{\percent}$ |
| Rouge | 2 | $\num{100}$ | $\qty{\pm 2}{\percent}$ |
| Orange | 3 | $\num{1000}$ | - |
| Jaune | 4 | $\num{10000}$ | - |
| Vert | 5 | $\num{100000}$ | - |
| Bleu | 6 | $\num{1000000}$ | $\qty{\pm 0,25}{\percent}$ |
| Violet | 7 | $\num{10000000}$ | $\qty{\pm 0,1}{\percent}$ |
| Gris | 8 | $\num{100000000}$ | - |
| Blanc | 9 | $\num{1000000000}$ | - |
| Aucun | - | - | $\qty{\pm 20}{\percent}$ |
[table:n_widerstandsfarbcodes_tabelle:Tableau des codes de couleur des résistances]

<note>
* Le tableau se trouve dans le recueil de formules
</note>

---

<left>
* Dans cet exemple :
  1. Anneau de couleur 4
  2. Anneau de couleur 7
  3. Anneau de couleur $\cdot \num{1000}$
* $\begin{split}&47 \cdot \qty{1000}{\ohm}\\ &= \qty{47000}{\ohm}\\ &= \qty{47}{\kilo\ohm}\end{split}$
</left>
<right>
[picture:665:n_widerstandsfarbcodes: Une résistance avec 4 anneaux de couleur]
</right>

---
## Tolérance

* Écart par rapport à la valeur réelle
* Exemple : argent signifie $\qty{\pm 10}{\percent}$
* $\qty{10}{\percent} \cdot \qty{47}{\kilo\ohm} = \qty{4,7}{\kilo\ohm}$
* Valeur de résistance comprise entre $\qty{42,3}{\kilo\ohm}$ et $\qty{51,7}{\kilo\ohm}$

---

[question:NC107]
---
[question:NC105]
---
[question:NC106]
---
[question:NC104]
---
[question:NC103]
---
[question:NC102]
---
[question:NC108]
---
[question:NC109]
---
[question:NC110]
