Lors du calcul des distances de sécurité, l'atténuation angulaire des antennes directionnelles joue un rôle important. La puissance de rayonnement la plus élevée est émise au centre du lobe de rayonnement. Dans les autres directions, elle est moindre. Si l'antenne est suffisamment haute, l'antenne rayonne en grande partie au-dessus de la zone <u>non</u> contrôlable, c'est-à-dire la zone dans laquelle les limites doivent absolument être respectées. 

Dans l'angle critique de $\qty{40}{\degree}$ en dessous de l'antenne se trouve une zone non contrôlable. La puissance de rayonnement y est inférieure de $\qty{6}{\dB}$ à celle du centre du diagramme de rayonnement. La conséquence directe est que la distance de sécurité peut y être réduite en conséquence.

$\qty{6}{\dB}$ correspondent à un facteur de $\num{0,25}$ ou $\dfrac{1}{4}$ (recueil de formules).

$ E = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{d}$
Réarrangement de la formule pour $d$ (distance de sécurité).
$ d = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}$

La puissance de rayonnement $P_\textrm{EIRP}$ n'est pas connue. Cependant, nous savons que pour ce calcul, nous ne devons utiliser qu'un quart de la puissance de rayonnement par rapport à la puissance de rayonnement maximale.

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}\cdot \dfrac{1}{4}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}\cdot \sqrt{\dfrac{1}{4}}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}\cdot \mathbf{\dfrac{1}{2}}\end{split}$

Si la puissance de rayonnement est réduite à $\dfrac{1}{4}$, la distance de sécurité de $\qty{20}{\meter}$ est divisée par deux. Elle se réduit à $\qty{10}{\meter}$.

[question:AK105]

<margin>
[picture:950:a_richtantenne_personenschutz:Dans un angle de 40° en dessous de l'axe du lobe principal de rayonnement, la puissance de rayonnement est 6 dB inférieure à celle de l'angle 0°.] 
</margin>