Nous avons maintenant fait la connaissance de la résistance et de son unité $\unit{\ohm}$ (Ohm). En pratique, la valeur numérique n'est toutefois généralement pas imprimée sur les résistances. Au lieu de cela, des anneaux de couleur sont utilisés. Ces anneaux de couleur codent la valeur de la résistance.

<margin>
[picture:665:n_widerstandsfarbcodes: Une résistance avec 4 anneaux de couleur]
</margin>

L'image [ref:n_widerstandsfarbcodes] montre une résistance avec quatre anneaux de couleur. Chaque couleur correspond à une valeur numérique, comme le montre le tableau [ref:n_widerstandsfarbcodes_tabelle] dans la colonne *Valeur*:
* Le premier anneau de couleur correspond au premier chiffre, dans ce cas *jaune*, donc quatre.
* Le deuxième anneau de couleur correspond au deuxième chiffre, dans notre exemple donc *violet*, donc sept.
* Le troisième anneau de couleur est le soi-disant multiplicateur (voir tableau [ref:n_widerstandsfarbcodes_tabelle], dans notre cas *orange*, donc la valeur 1000.

<webmargin>
| X:Couleur | l:Valeur | l:Multiplicateur | l:Tolérance |
| Argent | - | $\num{0,01}$ | $\qty{\pm 10}{\percent}$ |
| Or | - | $\num{0,1}$ | $\qty{\pm 5}{\percent}$ |
| Noir | 0 | $\num{1}$ | - |
| Brun | 1 | $\num{10}$ | $\qty{\pm 1}{\percent}$ |
| Rouge | 2 | $\num{100}$ | $\qty{\pm 2}{\percent}$ |
| Orange| 3 | $\num{1000}$ | - |
| Jaune | 4 | $\num{10000}$ | - |
| Vert | 5 | $\num{100000}$ | - |
| Bleu | 6 | $\num{1000000}$ | $\qty{\pm 0,25}{\percent}$ |
| Violet | 7 | $\num{10000000}$ | $\qty{\pm 0,1}{\percent}$ |
| Gris | 8 | $\num{100000000}$ | - |
| Blanc | 9 | $\num{1000000000}$ | - |
| Aucun | - | - | $\qty{\pm 20}{\percent}$ |
[table:n_widerstandsfarbcodes_tabelle:Tableau des codes de couleur des résistances]
</webmargin>

Le premier et le deuxième anneau ensemble donnent le nombre 47. Si l'on multiplie ce nombre par le multiplicateur, on peut calculer la valeur de la résistance:

$ 47 \cdot \qty{1000}{\ohm} = \qty{47000}{\ohm} = \qty{47}{\kilo\ohm} $

---

Il reste encore un quatrième anneau de couleur. Celui-ci représente la tolérance dite, qui indique dans quelle mesure la valeur réelle de la résistance peut s'écarter de la valeur imprimée.
D'autres détails à ce sujet suivront dans la classe E. 

<indepth>
*Approfondissement:* Dans notre exemple, le dernier anneau est *argent*, ce qui signifie une tolérance de $\qty{\pm 10}{\percent}$. La valeur réelle de la résistance peut être $\qty{10}{\percent} \cdot \qty{47}{\kilo\ohm} = \qty{4,7}{\kilo\ohm}$ plus ou moins que la valeur indiquée. Elle peut donc être comprise entre $\qty{42,3}{\kilo\ohm}$ et $\qty{51,7}{\kilo\ohm}$.
</indepth>

---

Le tableau des codes de couleur ne doit pas être appris par cœur. Il est fourni comme partie du recueil de formules lors de l'examen en tant qu'outil auxiliaire. Il faut toutefois se souvenir de l'arrangement des anneaux et de leur signification. Pour s'exercer, les questions suivantes peuvent être résolues à l'aide du code de couleur, afin d'acquérir de la routine.

<indepth>
*Approfondissement:* Il existe également des résistances avec plus de quatre anneaux de couleur. Celles-ci ne sont toutefois pas pertinentes pour l'examen. D'autres composants sont souvent également marqués avec des anneaux de couleur.
</indepth>

[question:NC107]
[question:NC105]
[question:NC106]
[question:NC104]
[question:NC103]
[question:NC102]
[question:NC108]
[question:NC109]
[question:NC110]
