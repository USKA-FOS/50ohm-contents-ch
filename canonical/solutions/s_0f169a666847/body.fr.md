Comme indiqué dans le circuit, pour la fréquence de sortie du VCO en état verrouillé par la PLL, on a :

$f_{VCO} = n \cdot f_A$

En réarrangeant pour obtenir le rapport de division *n*, on obtient :

$n = \frac{f_{VCO}}{f_A}$

Pour la *limite inférieure* de la plage de sortie souhaitée avec $f_{VCO} = \qty{12,000}{\mega\hertz}$ et $f_A = \qty{12,5}{\kilo\hertz}$, on a :

$n_{min} = \frac{\qty{12000000}{\hertz}}{\qty{12500}{\hertz}} = 960$

Pour la *limite supérieure* avec $f_{VCO} = \qty{14,000}{\mega\hertz}$, on obtient :

$n_{max} = \frac{\qty{14000000}{\hertz}}{\qty{12500}{\hertz}} = 1120$

Le rapport de division *n* doit donc se situer dans la plage allant de *960* à *1120*.