# Données
* Fréquence de la balise : $f_\text{balise} = \qty{144,4}{\mega\hertz}$
* Bande passante SSB : $f_{B,max} = \qty{2,7}{\kilo\hertz}$
* Précision : $\qty{1}{\ppm}$

# Considérations préliminaires
L’écart ($f_\text{écart}$) par rapport à la fréquence de la balise ($f_\text{balise}$) est composé de la bande passante SSB ($f_{B,max}$) et de l’écart (de sécurité) ($\Delta f$) dû à l’imprécision de $\qty{1}{\ppm}$. $\unit{ppm}$ signifie *parties par million*, $\qty{1}{\ppm}$ correspond donc à $1$ pour $10^6$. 

# Méthode de résolution
$\Delta f = \qty{144,4}{\mega\hertz} \cdot \frac{1}{10^6} = \frac{\qty{144,4 \cdot \cancel{10^6}}{\hertz}}{\cancel{10^6}} = \qty{144,4}{\hertz}= \qty{0,1444}{\kilo\hertz}$

$f_\text{écart} = f_{B,max} + \Delta f = \qty{2,7}{\kilo\hertz} + \qty{0,1444}{\kilo\hertz} = \qty{2,8444}{\kilo\hertz}$