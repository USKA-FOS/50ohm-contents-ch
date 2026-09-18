Comme nous l’avons déjà appris, un dipôle demi-onde peut également être alimenté à une extrémité. L’impédance d’alimentation pour une longueur de fil de $\lambda / 2$ ou de multiples de celle-ci est élevée (environ $\qtyrange{2000}{2500}{\ohm}$).

Pour adapter une telle antenne alimentée à une extrémité, il existe différentes possibilités. Nous allons examiner ci-dessous trois variantes typiques :

* Circuit de Fuchs
* Transformateur pour l’adaptation d’impédance
* Antenne Zeppelin

Une possibilité d’adaptation est le circuit de Fuchs déjà abordé (cf. figure [ref:a_fuchskreis]). Il s’agit d’un circuit résonant parallèle accordé sur la fréquence de fonctionnement. Il transforme l’impédance faible de la ligne d’alimentation en l’impédance d’alimentation élevée de l’antenne demi-onde alimentée à une extrémité et compense en même temps les composantes réactives présentes.

<margin>
[picture:310:a_fuchskreis:Circuit de Fuchs pour l’adaptation d’un dipôle demi-onde alimenté à une extrémité]
</margin>

[question:AG419]

---

Une autre possibilité est un transformateur (cf. figure [ref:a_unun_1_49]) avec un rapport de transformation de $ü = 1:7$. Comme la tension et le courant sont multipliés ou divisés par le facteur $\num{7}$, cela donne pour la résistance une transformation de $1:7^2 = 1:49$, soit $(1 \cdot \qty{50}{\ohm}) : (49 \cdot \qty{50}{\ohm}) = \qty{50}{\ohm} : \qty{2450}{\ohm}$.

<margin>
[photo:332:a_unun_1_49:Un-Un 1 à 49 pour l’adaptation d’un dipôle demi-onde alimenté à une extrémité]
[picture:315:a_endspeisung_1:Dipôle demi-onde alimenté à une extrémité avec câble pigtail]
[picture:260:a_endspeisung_2:Dipôle demi-onde alimenté à une extrémité avec câble coaxial comme contrepoids]
</margin>

<attention>
En ce qui concerne la *transformation d’impédance*, le rapport de spires d’un transformateur intervient au carré, c’est-à-dire qu’un transformateur avec un rapport de spires de 1:7 assure une transformation d’impédance de 1:49. Pour les Baluns et les Un-Uns, il n’est pas toujours indiqué s’il s’agit du rapport de spires ou du rapport d’impédance. Il existe donc un risque de confusion. L’indication du rapport d’impédance est courante. Par exemple, pour un transformateur avec un rapport de spires ($ü$) de 1:7, on parle d’un Un-Un 1:49.
</attention>

Comme contrepoids, on utilise souvent un court fil (au moins un vingtième de la longueur d’onde), cf. figure [ref:a_endspeisung_1], ou une partie de la ligne coaxiale (au moins $\qty{0.05}{\lambda}$), cf. figure [ref:a_endspeisung_2]. Une self de mode commun (abréviation MWS) empêche le câble d’alimentation supplémentaire de devenir partiellement une partie de l’antenne.

[question:AG123]
[question:AG124]

---

Au lieu d’un circuit de Fuchs ou d’un transformateur, on peut également utiliser une ligne bifilaire d’une longueur de $\lambda / 4$. On parle alors d’*antenne Zeppelin* (cf. figure [ref:a_zeppelinantenn]). Nous verrons plus tard dans une section dédiée comment une ligne peut transformer une impédance.

Le nom de cette antenne remonte à son utilisation sur les dirigeables. Grâce à la ligne bifilaire de $\lambda / 4$, la haute tension n’apparaît qu’à son extrémité, donc loin du dirigeable rempli de gaz (cf. figure [ref:a_zeppelinantenne_foto]).

<margin>
[picture:314:a_zeppelinantenne:Structure d’une antenne Zeppelin]
[photo:336:a_zeppelinantenne_foto:Antenne Zeppelin (image symbolique)]
</margin>

[question:AG120]

---

Tout comme pour un dipôle demi-onde alimenté à une extrémité, une ligne d’alimentation avec une impédance caractéristique différente peut également être utilisée pour l’adaptation sur d’autres types d’antennes. Pour la classe E, nous avons déjà rencontré les antennes en boucle à onde entière, dont la Delta-Loop et l’antenne Quad. Une antenne Delta-Loop (cf. figure [ref:a_delta_loop]) avec des côtés de longueur égale présente une impédance d’alimentation d’environ $\qty{100}{\ohm}$. En insérant une ligne de $\lambda / 4$ avec une impédance caractéristique de $\qty{75}{\ohm}$, on obtient une transformation vers les $\qty{50}{\ohm}$ habituels en radioamateurisme.

<margin>
[picture:311:a_delta_loop:Antenne Delta-Loop]
</margin>

[question:AG117]

<indepth>
La valeur optimale de l’impédance caractéristique d’une ligne d’alimentation de $\lambda / 4$ utilisée pour l’adaptation se calcule à partir de la *moyenne géométrique* des deux impédances, par exemple $\qty{50}{\ohm}$ et $\qty{100}{\ohm}$, ce qui donne $\sqrt{\qty{50}{\ohm} \cdot \qty{100}{\ohm}} \approx \qty{70,7}{\ohm}$.
</indepth>

Si l’on réalise la boucle à onde entière sous forme de carré, chaque côté doit alors avoir une longueur égale à un quart de la longueur d’onde.

[question:AG119]

<attention>
Comme pour le dipôle, la longueur mécanique d’une antenne en boucle à onde entière diffère de la longueur électrique. Contrairement au facteur de vélocité des dipôles, les boucles à onde entière présentent un *facteur d’allongement*, c’est-à-dire que l’antenne doit être quelques pourcents plus longue que la longueur d’onde dans l’espace libre.
</attention>

---

Comme les bandes de fréquences présentent des conditions de propagation différentes selon les moments de la journée, de l’année et du cycle solaire, les radioamateurs souhaitent souvent pouvoir fonctionner sur un maximum de bandes de fréquences. Deux exemples d’antennes multibandes sont l’*antenne G5RV à deux branches de même longueur* (cf. figure [ref:a_g5rv]) avec une ligne bifilaire, et l’*antenne Windom à excitation asymétrique* (cf. figure [ref:a_windom]), dont les dimensions bien choisies permettent d’obtenir de nombreuses résonances et donc une utilisation sur un maximum de bandes de radioamateurisme.

<margin>
[picture:313:a_g5rv:Antenne G5RV]
[picture:309:a_windom:Antenne Windom]
</margin>

[question:AG121]
[question:AG122]

---

% TODO: Vérifier la représentation de $5/8 \lambda$

Le fait qu’une antenne soit résonante ne signifie pas qu’elle présente également une bonne caractéristique de rayonnement. Souvent, on souhaite obtenir un rayonnement aussi plat que possible. Pour les antennes verticales excitées par rapport à la terre, une longueur d’environ $5/8 \lambda$ s’avère optimale.

<indepth>
Un simple fil avec la terre comme contrepoids n’est pas résonant à une longueur de $5/8 \lambda$. Les résonances n’apparaissent qu’à $1/4$, $3/4$, $5/4$, etc. Une adaptation est donc nécessaire. Cela se fait généralement en insérant une bobine qui allonge la longueur électrique de $5/8$ à $6/8$ (soit $3/4$). On voit souvent de telles bobines sur les antennes pour la bande HF automobile.
% TODO: Image antenne VHF ou CB automobile
</indepth>

<attention>
L’optimum de $5/8 \lambda$ ne s’applique qu’aux antennes verticales excitées par rapport à la terre. Si l’on considère par exemple des dipôles alimentés au centre, qui se trouvent soit dans l’espace libre, soit verticalement juste au-dessus du sol, l’optimum se situe alors à $5/4 \lambda$.
% TODO: La question est incorrecte, voir 2e révision de DL9JBE.
</attention>

[question:AG223]