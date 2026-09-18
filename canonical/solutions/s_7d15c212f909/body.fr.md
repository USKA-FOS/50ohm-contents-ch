Calculons d'abord le courant de base nécessaire :

$I_B = \frac{I_C}{B} = \frac{\qty{2}{\milli\ampere}}{200} = \qty{10}{\micro\ampere}$

Un courant dix fois supérieur au courant de base doit circuler dans la résistance de polarisation $R_2$ :

$I_2 = 10 \cdot I_B = \qty{100}{\micro\ampere}$

Le courant traversant $R_1$ est la somme du courant traversant $R_2$ et du courant de base :

$I_1 = I_2 + I_B = \qty{100}{\micro\ampere} + \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$


Une chute de tension de $U_1 = \qty{10}{\volt} - \qty{0,6}{\volt} = \qty{9,4}{\volt}$ apparaît aux bornes de $R_1$ (tension de service moins la tension base-émetteur).


On obtient ainsi :

$R_1 = \frac{U_1}{I_1} = \frac{\qty{9,4}{\volt}}{\qty{110}{\micro\ampere}} \approx \qty{85,5}{\kilo\ohm}$