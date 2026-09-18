Comme la résistance de charge $R_L$ est montée en parallèle avec $R_2$, il faut d'abord regrouper les deux résistances en une résistance équivalente.

Le montage en parallèle donne :

$ R_\mathrm{2L} = \frac{R_2 \cdot R_L}{R_2 + R_L} $

Substitution des valeurs :

$ R_\mathrm{2L} = \frac{\qty{2,2}{\kilo\ohm} \cdot \qty{8,2}{\kilo\ohm}}
{\qty{2,2}{\kilo\ohm} + \qty{8,2}{\kilo\ohm}} $

$ R_\mathrm{2L} \approx \qty{1,74}{\kilo\ohm} $

Le circuit ne comprend plus alors qu'un simple diviseur de tension composé de $R_1$ et $R_\mathrm{2L}$.

La tension de sortie se calcule avec :

$ U_2 = U_B \cdot \frac{R_\mathrm{2L}}{R_1 + R_\mathrm{2L}} $

Substitution des valeurs :

$ U_2 = \qty{12}{\volt} \cdot \frac{\qty{1,74}{\kilo\ohm}}{\qty{10}{\kilo\ohm} + \qty{1,74}{\kilo\ohm}} = \approx \qty{1,8}{\volt} $