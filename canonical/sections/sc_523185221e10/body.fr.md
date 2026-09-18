Lors du calcul des distances de sécurité, l’**atténuation angulaire** des antennes directives joue un rôle important. La **puissance rayonnée** maximale est émise au centre du lobe de rayonnement. Dans les autres directions, elle est plus faible. Si l’antenne est suffisamment haute, une grande partie du rayonnement passe au-dessus de la zone *non contrôlable*, c’est-à-dire la zone où les valeurs limites doivent impérativement être respectées.

<margin>
[picture:950:a_richtantenne_personenschutz:À un angle de $\qty{40}{\degree}$ sous l’axe du lobe principal de rayonnement, la **puissance rayonnée** est $\qty{6}{\decibel}$ plus faible qu’à l’angle $\qty{0}{\degree}$.]
</margin>

Dans l’illustration [ref:a_richtantenne_personenschutz], une zone non contrôlable est représentée à un angle critique de $\qty{40}{\degree}$ sous l’antenne, où des personnes peuvent se trouver. La **puissance rayonnée** y est inférieure de $\qty{6}{\decibel}$ à celle au centre du diagramme de rayonnement. Il en résulte que la distance de sécurité peut être réduite en conséquence.

$\qty{6}{\decibel}$ correspondent à un facteur de $\num{0,25}$ ou $\dfrac{1}{4}$ (recueil de formules).

$ E = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{d}$
Réarrangement de la formule pour obtenir $d$ (distance de sécurité).
$ d = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}$

La **puissance rayonnée** $P_\textrm{EIRP}$ n’est pas connue. Cependant, nous savons que, dans ce calcul, il faut prendre en compte seulement un quart de la **puissance rayonnée** maximale.

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}\cdot \dfrac{1}{4}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}\cdot \sqrt{\dfrac{1}{4}}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}\cdot \mathbf{\dfrac{1}{2}}\end{split}$

Si la **puissance rayonnée** est réduite à $\dfrac{1}{4}$, la distance de sécurité de $\qty{20}{\meter}$ est divisée par deux. Elle passe dans cet exemple concret à $\qty{10}{\meter}$.

[question:AK105]