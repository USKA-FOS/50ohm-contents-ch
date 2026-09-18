Pour les antennes, il faut distinguer la *longueur mécanique* de la *longueur électrique*. La longueur mécanique correspond simplement à la longueur mesurable du fil ou du radiateur de l'antenne. La longueur électrique, en revanche, décrit comment l'antenne se comporte électriquement à la fréquence considérée. Elle peut être modifiée, entre autres, par des bobines et des condensateurs, sans que la longueur mécanique du radiateur ne soit changée.

Considérons d'abord les antennes proches de leur résonance fondamentale. Un dipôle demi-onde est approximativement résonant pour une longueur totale d'environ $\lambda/2$, une antenne groundplane avec un seul radiateur vertical l'est pour une longueur de radiateur d'environ $\lambda/4$. Si une telle antenne est trop courte pour la fréquence souhaitée, son impédance d'alimentation présente une composante réactive *capacitive*. Une bobine peut compenser cette composante réactive capacitive. On parle alors d'*allongement électrique* de l'antenne. Si l'antenne est au contraire trop longue pour la fréquence souhaitée, son impédance d'alimentation présente une composante réactive *inductive*. Celle-ci peut être compensée par un condensateur. On parle alors de *raccourcissement électrique*. Une bobine allonge donc une antenne électriquement, un condensateur la raccourcit électriquement. La longueur mécanique du radiateur reste inchangée.

<margin>
[picture:1134:a_5_8_lambda_strahlung:Diagramme de rayonnement et distribution de courant d'antennes verticales avec terre idéale]
</margin>

---

Un exemple intéressant est l'antenne verticale $\frac{5}{8}\lambda$ avec une longueur convertie de $\qty{0.625}{\lambda}$ (cf. figure [ref:a_5_8_lambda]). Le radiateur est ainsi mécaniquement environ 2,5 fois plus long que celui d'une groundplane $\frac{\lambda}{4}$ normale ($\qty{0.25}{\lambda}$). La plus grande longueur du radiateur modifie avantageusement le diagramme de rayonnement vertical, comme illustré dans la figure [ref:a_5_8_lambda_strahlung] : davantage de la puissance rayonnée est concentrée vers l'horizon, moins est rayonnée vers le haut ou vers le bas. Cela permet généralement d'obtenir une portée plus grande pour les liaisons terrestres à puissance égale. Une longueur de radiateur d'environ $\frac{5}{8} \lambda$ est optimale pour cet effet : si le radiateur est prolongé davantage, une partie plus importante de la puissance est à nouveau perdue vers le haut et vers le bas.

Cependant, cette antenne n'est pas résonante à une longueur de radiateur de $\frac{5}{8}\lambda=\qty{0.625}{\lambda}$. Pour la résonance, la longueur du radiateur devrait être réduite à $\frac{\lambda}{2}=\qty{0.5}{\lambda}$ ou augmentée à $\frac{3}{4}\lambda=\qty{0.75}{\lambda}$. Les deux options réduiraient la puissance au niveau de l'horizon. Il est donc recommandé, pour une meilleure concentration, de conserver la longueur de radiateur à $\frac{5}{8}\lambda$ et d'obtenir la résonance électriquement, c'est-à-dire d'allonger l'antenne électriquement. Une des possibilités pour y parvenir est d'utiliser une bobine de pied. La bobine fournit une composante réactive inductive qui compense la composante réactive capacitive du radiateur $\frac{5}{8}\lambda$. L'impédance ainsi obtenue est très similaire à celle d'une antenne avec une longueur de radiateur $\frac{3}{4}\lambda=\qty{0.75}{\lambda}$.

<margin>
[picture:650:a_5_8_lambda:$\qty{5}{8}\lambda$-Antenne verticale]
</margin>

[question:AG106]

---

Inversement, une antenne qui est mécaniquement un peu trop longue près de sa résonance fondamentale peut être raccourcie électriquement par un condensateur (cf. figure [ref:a_verkuerzung]). Le condensateur fournit une composante réactive capacitive et compense ainsi la composante réactive inductive du radiateur trop long.

[question:AG107]

<margin>
[picture:563:a_verkuerzung:Antenne verticale avec condensateur de raccourcissement]
</margin>

---

Pour un dipôle, on peut également estimer d'abord, à partir de sa longueur mécanique, si un allongement ou un raccourcissement électrique est nécessaire pour obtenir la résonance fondamentale souhaitée.

[question:AG108]