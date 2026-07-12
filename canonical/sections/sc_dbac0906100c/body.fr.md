Comme nous l'avons déjà appris, un dipôle demi-onde peut également être alimenté à une extrémité. La résistance d'alimentation est élevée (environ $\qtyrange{2000}{2500}{\ohm}$) pour une longueur de fil de $\lambda / 2$ ou de ses multiples. Une possibilité d'adaptation est le cercle de Fuchs déjà mentionné.

[question:AG419]

---

Une autre possibilité est un transformateur avec un rapport de transformation de $ü = 1:7$. Puisque la tension et le courant sont multipliés ou divisés par un facteur $\num{7}$, le rapport de transformation pour la résistance est de $1:7^2 = 1:49$ correspondant à $(1 \cdot \qty{50}{\ohm}) : (49 \cdot \qty{50}{\ohm}) = \qty{50}{\ohm} : \qty{2450}{\ohm}$.

<attention>
En ce qui concerne la *transformation d'impédance* (transformation de la résistance), le rapport de spires d'un transformateur est au carré, c'est-à-dire qu'un transformateur avec un rapport de spires de 1:7 assure une transformation d'impédance de 1:49. Dans le cas des baluns et des Un-Un, il n'est souvent pas indiqué s'il s'agit du rapport de spires ou du rapport d'impédance. Il existe donc une possibilité de confusion. L'usage est l'indication du rapport d'impédance. Dans le cas d'un transformateur avec un rapport de spires ($ü$) de 1:7, on parle par exemple d'un Un-Un de 1:49.
</attention>

En guise de contrepoids, on utilise souvent une courte extrémité de fil (au moins un vingtième de la longueur d'onde) ou une partie de la ligne d'alimentation coaxiale. Un piège d'onde de mode commun (abréviation MWS) empêche que le reste du câble d'alimentation ne fasse partie de l'antenne.

[question:AG123]
[question:AG124]

Au lieu d'un cercle de Fuchs ou d'un transformateur, on peut également utiliser une ligne bifilaire de longueur $\lambda / 4$. On parle alors d'une *antenne Zeppelin*.

%TODO origine du nom zeppelin

[question:AG120]

---

Tout comme pour un dipôle demi-onde alimenté à une extrémité, une ligne d'alimentation avec une impédance de ligne différente peut également être utilisée pour l'adaptation d'autres formes d'antennes. Pour la classe E, nous avons déjà appris à connaître les antennes en boucle d'onde entière ; parmi celles-ci, la Delta-Loop et l'antenne Quad. Une antenne Delta-Loop a une impédance d'alimentation d'environ $\qty{100}{\ohm}$ pour des branches de longueur égale. En insérant une ligne de $\lambda / 4$ avec une impédance de ligne de $\qty{75}{\ohm}$, une transformation est effectuée sur les $\qty{50}{\ohm}$ habituels dans le radioamateur.

[question:AG117]

<indepth>
La valeur optimale pour l'impédance de ligne d'une ligne d'alimentation de $\lambda / 4$, qui est utilisée pour l'adaptation, se calcule à partir de la *moyenne géométrique* des deux impédances, par exemple $\qty{50}{\ohm}$ et $\qty{100}{\ohm}$ correspondant à $\sqrt{\qty{50}{\ohm} \cdot \qty{100}{\ohm}} \approx \qty{70,7}{\ohm}$.
</indepth>

Si l'on réalise la boucle d'onde entière sous forme de carré, alors la longueur de chaque côté doit correspondre à un quart de la longueur d'onde.

[question:AG119]

<attention>
Comme pour le dipôle, la longueur mécanique d'une antenne en boucle d'onde entière diffère de la longueur électrique. Contrairement au facteur de raccourcissement des dipôles, il existe cependant, de manière surprenante, un *facteur d'allongement* dans le cas des boucles d'onde entière, c'est-à-dire que l'antenne doit être quelques pour cent plus longue qu'une longueur d'onde dans l'espace libre.
</attention>

---

Comme les bandes de fréquences présentent des conditions de propagation différentes à différents moments de la journée, de l'année et du cycle solaire, les radioamateurs souhaitent pouvoir opérer sur autant de bandes de fréquences que possible. Deux exemples d'antennes multibandes sont l'*antenne G5RV avec deux branches de longueur égale* et une ligne bifilaire ainsi que l'*antenne Windom asymétrique*, pour lesquelles de nombreuses résonances et donc une utilisation sur autant de bandes de radioamateur que possible sont obtenues par des dimensions habiles.

[question:AG121]
[question:AG122]

---

% TODO: Vérifier la représentation de $5/8 \lambda$

Le fait qu'une antenne soit résonante ne signifie pas encore qu'elle présente également une bonne caractéristique de rayonnement. Souvent, on souhaite obtenir un rayonnement aussi plat que possible. Dans le cas des antennes verticales excitées par rapport à la terre, une longueur d'environ $5/8 \lambda$ est optimale.

<indepth>
Un simple fil avec la terre comme contrepoids n'est pas résonant pour une longueur de $5/8 \lambda$. Des résonances ne se produisent que pour $1/4$, $3/4$, $5/4$ etc. Par conséquent, une adaptation est nécessaire. Cela est généralement réalisé en insérant une bobine qui prolonge la longueur électrique de $5/8$ à $6/8$ (c'est-à-dire $3/4$). De telles bobines sont souvent visibles sur les antennes pour la bande des véhicules automobiles.
% TODO: Image VHF ou antenne CB automobile
</indepth>

<attention>
L'optimum de $5/8 \lambda$ ne s'applique qu'aux antennes excitées par rapport à la terre. Si l'on considère, par exemple, des dipôles alimentés au milieu, qui se trouvent soit dans l'espace libre, soit verticalement, juste au-dessus du sol, alors l'optimum se situe à $5/4 \lambda$.
% TODO: La question est fausse, voir 2ème révision de DL9JBE.
</attention>

[question:AG223]
