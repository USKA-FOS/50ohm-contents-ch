Nous avons maintenant appris à connaître la *résistance* et son *unité* $\unit{\ohm}$ (ohm). En pratique, la valeur numérique n'est généralement pas imprimée sur les résistances. À la place, des anneaux colorés sont utilisés. Ces anneaux codent la valeur de la résistance.

<margin>
[picture:665:n_widerstandsfarbcodes: Une résistance avec 4 anneaux colorés]
</margin>

L'illustration [ref:n_widerstandsfarbcodes] montre une résistance avec quatre anneaux colorés. Chaque couleur correspond à une valeur numérique, comme indiqué dans le tableau [ref:n_widerstandsfarbcodes_tabelle] dans la colonne *Valeur* :
* Le premier anneau coloré correspond au premier chiffre, dans ce cas *jaune*, soit quatre.
* Le deuxième anneau coloré correspond au deuxième chiffre, dans notre exemple *violet*, soit sept.
* Le troisième anneau coloré est le *multiplicateur* (voir tableau [ref:n_widerstandsfarbcodes_tabelle]), dans notre cas *orange*, soit la valeur 1000.

<webmargin>
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
[table:n_widerstandsfarbcodes_tabelle:Tableau des codes couleur des résistances]
</webmargin>

Le premier et le deuxième anneau donnent ensemble le nombre 47. Si l'on multiplie ce nombre par le multiplicateur, on peut calculer la valeur de la résistance :

$ 47 \cdot \qty{1000}{\ohm} = \qty{47000}{\ohm} = \qty{47}{\kilo\ohm} $

---

Il reste un quatrième anneau coloré. Celui-ci indique la *tolérance*, qui spécifie dans quelle mesure la valeur réelle de la résistance peut s'écarter de la valeur indiquée.
D'autres détails à ce sujet sont disponibles dans le chapitre [sec:widerstand_toleranz].

<indepth>
*Approfondissement* : Dans notre exemple, le dernier anneau est *argent*, ce qui correspond à une tolérance de $\qty{\pm 10}{\percent}$. La valeur réelle de la résistance peut donc être supérieure ou inférieure de $\qty{10}{\percent} \cdot \qty{47}{\kilo\ohm} = \qty{4,7}{\kilo\ohm}$ à la valeur indiquée. Elle peut donc se situer entre $\qty{42,3}{\kilo\ohm}$ et $\qty{51,7}{\kilo\ohm}$.
</indepth>

---

Le tableau des codes couleur n'a pas besoin d'être mémorisé. Il est fourni comme partie du *recueil de formules* lors de l'examen en tant qu'outil d'aide. Il est toutefois conseillé de retenir l'ordre des anneaux et leur signification. Pour s'entraîner, les questions suivantes peuvent être résolues à l'aide du code couleur afin de s'habituer à cette méthode.

<indepth>
*Approfondissement* : Il existe également des résistances avec plus de quatre anneaux colorés. Cependant, celles-ci ne sont pas pertinentes pour l'examen. D'autres composants sont également souvent marqués par des anneaux colorés.
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
