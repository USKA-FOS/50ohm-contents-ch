## Explication

Une résistance de décharge à haute impédance sert à décharger de manière contrôlée les condensateurs d’alimentation. Elle limite le courant de décharge et réduit ainsi le risque de formation d’arc électrique, de dommages aux composants ainsi que les dangers électriques.

### Pourquoi une résistance à haute impédance ?

Lors de la décharge d’un condensateur, le courant circule à travers la résistance de décharge $R$. Celle-ci est dimensionnée de manière à ce que :

* le courant initial reste limité :

    $I_0 = \frac{U_0}{R}$

* aucune pointe de courant dangereusement élevée ne se produise,
* aucune formation d’arc électrique n’apparaisse,
* les composants et les pistes ne soient pas surchargés,
* la décharge s’effectue dans un délai raisonnable.

Une résistance à faible impédance ou un court-circuit entraînerait en revanche :

* des courants initiaux très élevés,
* des dommages possibles au condensateur et aux pistes,
* des pointes de courant et de tension incontrôlées,
* un risque accru d’incendie et de blessure.

### Pourquoi la puissance de la résistance doit-elle être suffisante ?

L’énergie stockée dans le condensateur est donnée par :

$E = \frac{1}{2} \cdot C \cdot {U_0}^2$

Cette énergie est entièrement convertie en chaleur dans la résistance lors de la décharge.

La puissance dissipée initiale est :

$P_0 = \frac{{U_0}^2}{R}$

Pour $R = \qty{100}{\kilo\ohm}$ et $U_0 = \qty{400}{\volt}$, cela donne une puissance de $P_0 = \qty{1,6}{\watt}$.

Par conséquent, la résistance doit :

* avoir une puissance nominale suffisante,
* pouvoir supporter des surcharges de courte durée (fonctionnement en impulsions),
* être dimensionnée thermiquement pour éviter une surchauffe.