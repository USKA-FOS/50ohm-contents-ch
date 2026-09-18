Calculons d'abord le courant de base :

$ I_B = \frac{I_C}{B} = \frac{\qty{2}{\milli\ampere}}{200} = \qty{10}{\micro\ampere} $

Un courant dix fois supérieur doit circuler dans $R_2$ :

$ I_2 = 10 \cdot I_B = \qty{100}{\micro\ampere} $

Le courant traversant $R_1$ est donc :

$ I_1 = I_2 + I_B = \qty{110}{\micro\ampere} $

Une tension de $\qty{1}{\volt}$ chute aux bornes de la résistance d'émetteur. 
De plus, la jonction base-émetteur nécessite environ $\qty{0,6}{\volt}$.

La tension de base est donc de :

$ U_B = \qty{1}{\volt} + \qty{0,6}{\volt} = \qty{1,6}{\volt} $

La tension aux bornes de $R_1$ est donc :

$ U_1 = \qty{10}{\volt} - \qty{1,6}{\volt} = \qty{8,4}{\volt} $

Nous obtenons alors, grâce à la loi d'Ohm :

$ R_1 = \frac{U_{R_1}}{I_{R_1}} = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} \approx \qty{76,4}{\kilo\ohm} $