# Données
* Fréquence d'émission : $\qty{14,2}{\mega\hertz}$
* Précision : $\qty{10}{\ppm}$

# Solution
$\unit{ppm}$ signifie *parts per million*, $\qty{10}{\ppm}$ signifie donc $10$ pour $10^6$.  
La fréquence d'émission réelle se situe entre $f_\text{min}$ et $f_\text{max}$.
$f_\text{min} = f - 10 \cdot \frac{f}{10^6} = \qty{14,2}{\mega\hertz} - 10 \cdot \frac{14,2\cdot \qty{\cancel{10^6}}{\mega\hertz}}{\cancel{10^6}} = \qty{14,2}{\mega\hertz} - \qty{142}{\hertz} = \qty{14,199858}{\mega\hertz}$
$f_\text{max} = f + 10 \cdot \frac{f}{10^6} = \qty{14,2}{\mega\hertz} + 10 \cdot \frac{14,2\cdot \qty{\cancel{10^6}}{\mega\hertz}}{\cancel{10^6}} = \qty{14,2}{\mega\hertz} + \qty{142}{\hertz} = \qty{14,200142}{\mega\hertz}$