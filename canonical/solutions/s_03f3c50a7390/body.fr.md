# Donné
* Fréquence de la balise : $f_\text{Balise} = \qty{144,4}{\mega\hertz}$
* Largeur de bande SSB : $f_{B,max} = \qty{2,7}{\kilo\hertz}$
* Précision : $\qty{1}{\ppm}$

# Préconsidération
La distance ($f_\text{Distance}$) par rapport à la fréquence de la balise ($f_\text{Balise}$) se compose de la largeur de bande SSB ($f_{B,max}$) et de la distance (de sécurité) ($\Delta f$) due à l'imprécision de $\qty{1}{\ppm}$. $\unit{ppm}$ signifie *parts per million*, $\qty{1}{\ppm}$ signifie donc $1$ pour $10^6$. 

# Méthode de solution
$\Delta f = \qty{144,4}{\mega\hertz} \cdot \frac{1}{10^6} = \qty{144,4 \cdot \cancel{10^6}}{\hertz}\frac{1}{\cancel{10^6}} = \qty{144,4}{\hertz}= \qty{0,1444}{\kilo\hertz}$

$f_\text{Distance} = f_{B,max} + \Delta f = \qty{2,7}{\kilo\hertz} + \qty{0,1444}{\kilo\hertz} = \qty{2,8444}{\kilo\hertz}$