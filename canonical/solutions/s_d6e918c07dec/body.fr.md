Comme toutes les résistances sont de même taille, on a :

$ R_1 = R_2 = R_3 = \qty{10}{\kilo\ohm} $

Un courant de:

$ I_{R_3} = \qty{1}{\milli\ampere} $

circule à travers $R_3$.

Comme $R_2$ et $R_3$ sont en parallèle et possèdent la même résistance, un courant de:

$ I_{R_2} = \qty{1}{\milli\ampere} $

circule également à travers $R_2$.

Le courant à travers $R_1$ est la somme des deux courants partiels:

$ I_{R_1} = I_{R_2} + I_{R_3} = \qty{1}{\milli\ampere} + \qty{1}{\milli\ampere} = \qty{2}{\milli\ampere} $

La résistance de remplacement du circuit en parallèle de $R_2$ et $R_3$ est ensuite calculée:

$ R_{23} = \frac{R_2 \cdot R_3}{R_2 + R_3} = \frac{\qty{10}{\kilo\ohm} \cdot \qty{10}{\kilo\ohm}}
{\qty{10}{\kilo\ohm} + \qty{10}{\kilo\ohm}} = \qty{5}{\kilo\ohm} $

La résistance totale du circuit est donc:

$ R_\mathrm{ges} = R_1 + R_{23} = \qty{10}{\kilo\ohm} + \qty{5}{\kilo\ohm} = \qty{15}{\kilo\ohm} $

Avec le courant total, la tension totale est:

$ U = I \cdot R = \qty{2}{\milli\ampere} \cdot \qty{15}{\kilo\ohm} = \qty{30}{\volt} $