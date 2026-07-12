Pour calculer les fréquences d'oscillateur nécessaires pour les transverters, il est nécessaire de connaître les fréquences d'entrée et de sortie souhaitées. De plus, il est nécessaire de savoir si l'oscillateur doit se trouver en dessous ou au-dessus du signal utile.

<indepth>
Si la fréquence de l'oscillateur se trouve en dessous du signal utile, la position de la bande latérale d'un signal SSB (USB/LSB) est conservée.
Si la fréquence de l'oscillateur se trouve au-dessus du signal utile, la position de la bande latérale d'un signal SSB est inversée (USB devient LSB et vice versa).
</indepth>

Exemple de calcul :

Si la fréquence de l'oscillateur se trouve en dessous du signal utile, la fréquence plus élevée du signal utile correspond également à la fréquence plus élevée du signal de sortie du convertisseur/transverter.

Par exemple, si une bande de fréquences de $\qtyrange{438}{440}{\mega\hertz}$ doit être convertie en une bande de fréquences de $\qtyrange{28}{30}{\mega\hertz}$ (en supposant que la fréquence de l'oscillateur se trouve en dessous du signal utile), une fréquence de l'oscillateur de $\qty{440}{\mega\hertz} - \qty{30}{\mega\hertz}$ ou $\qty{438}{\mega\hertz} - \qty{28}{\mega\hertz}$ est nécessaire, ce qui donne dans les deux cas $\qty{410}{\mega\hertz}$. Si cette fréquence de l'oscillateur est générée par multiplication de fréquence, il faut également tenir compte de la division lors du calcul inverse pour obtenir la fréquence nécessaire de l'oscillateur à quartz.

Il en va de même pour la bande de fréquences de $\qtyrange{436}{438}{\mega\hertz}$, si celle-ci doit être convertie en une bande de fréquences de $\qtyrange{28}{30}{\mega\hertz}$ (également en supposant que la fréquence de l'oscillateur se trouve en dessous du signal utile).
Dans ce cas, le calcul donne une fréquence de l'oscillateur de $\qty{438}{\mega\hertz} - \qty{30}{\mega\hertz}$ ou $\qty{436}{\mega\hertz} - \qty{28}{\mega\hertz}$, ce qui donne une fréquence de l'oscillateur de $\qty{408}{\mega\hertz}$.

Si les $\qty{408}{\mega\hertz}$ ou $\qty{410}{\mega\hertz}$ calculés ci-dessus sont obtenus par multiplication par neuf de la fréquence de l'oscillateur à quartz, les deux fréquences de l'oscillateur à quartz sont de $\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ et $\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (arrondi respectivement).

[question:AF501]
[question:AF502]

%TODO: La question 1472 ne devrait pas être ici, car il s'agit d'un émetteur et cette question n'a rien à voir avec les convertisseurs ou les transverters. Elle devrait peut-être être déplacée dans la section Émetteurs et étages d'émetteurs
[question:AF301]