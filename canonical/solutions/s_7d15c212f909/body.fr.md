Tout d'abord, nous calculons le courant de base nécessaire :

$I_B = \frac{I_C}{B} = \frac{\qty{2}{\milli\ampere}}{200} = \qty{10}{\micro\ampere}$

Le courant à travers la résistance transversale $R_2$ doit être dix fois le courant de base :

$I_2 = 10 \cdot I_B = \qty{100}{\micro\ampere}$

Le courant à travers $R_1$ est composé du courant à travers $R_2$ et du courant de base :

$I_1 = I_2 + I_B = \qty{100}{\micro\ampere} + \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$

La tension aux bornes de $R_1$ est la tension de service moins la tension base-émetteur :

$U_1 = \qty{10}{\volt} - \qty{0,6}{\volt} = \qty{9,4}{\volt}$

Ainsi, nous obtenons :

$R_1 = \frac{U_1}{I_1} = \frac{\qty{9,4}{\volt}}{\qty{110}{\micro\ampere}} \approx \qty{85,5}{\kilo\ohm}$