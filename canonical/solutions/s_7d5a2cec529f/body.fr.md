Données :

$ U = \qty{15}{\volt} $

et

$ R_1 = R_2 = R_3 = \qty{10}{\kilo\ohm} $

On calcule d'abord la résistance équivalente du montage en parallèle de $R_2$ et $R_3$ :

$ R_{23} = \frac{R_2 \cdot R_3}{R_2 + R_3} $

Comme les deux résistances sont de même valeur, on obtient :

$ R_{23} = \qty{5}{\kilo\ohm} $

La résistance totale du circuit est donc :

$ R_\mathrm{ges} = R_1 + R_{23} = \qty{10}{\kilo\ohm} + \qty{5}{\kilo\ohm} = \qty{15}{\kilo\ohm} $

On peut maintenant calculer le courant total :

$ I_\mathrm{ges} = \frac{U}{R_\mathrm{ges}} = \frac{\qty{15}{\volt}}{\qty{15}{\kilo\ohm}} = \qty{1}{\milli\ampere} $

Ce courant traverse d'abord $R_1$ puis se divise entre les deux résistances de même valeur $R_2$ et $R_3$.

Comme les deux résistances sont égales, chaque branche est parcourue par la moitié du courant total :

$ I_3 = \frac{I_\mathrm{ges}}{2} = \frac{\qty{1}{\milli\ampere}}{2} = \qty{0,5}{\milli\ampere} $