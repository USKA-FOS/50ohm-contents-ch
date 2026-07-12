Comme la résistance de charge $R_L$ est en parallèle avec $R_2$, les deux résistances doivent d'abord être regroupées en une résistance de remplacement.

Le circuit en parallèle donne:

$ R_\mathrm{2L} = \frac{R_2 \cdot R_L}{R_2 + R_L} $

Insérer les valeurs:

$ R_\mathrm{2L} = \frac{\qty{2,2}{\kilo\ohm} \cdot \qty{8,2}{\kilo\ohm}}
{\qty{2,2}{\kilo\ohm} + \qty{8,2}{\kilo\ohm}} $

$ R_\mathrm{2L} \approx \qty{1,74}{\kilo\ohm} $

Maintenant, le circuit ne se compose plus que d'un simple diviseur de tension composé de $R_1$ et $R_\mathrm{2L}$.

La tension de sortie est calculée avec:

$ U_2 = U_B \cdot \frac{R_\mathrm{2L}}{R_1 + R_\mathrm{2L}} $

Insérer les valeurs:

$ U_2 = \qty{12}{\volt} \cdot \frac{\qty{1,74}{\kilo\ohm}}{\qty{10}{\kilo\ohm} + \qty{1,74}{\kilo\ohm}} = \approx \qty{1,8}{\volt} $