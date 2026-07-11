# Dato
* Frequenza di trasmissione: $\qty{14,2}{\mega\hertz}$
* Precisione: $\qty{10}{\ppm}$

# Percorso di soluzione
$\unit{ppm}$ sta per *parts per million*, quindi $\qty{10}{\ppm}$ significa $10$ per $10^6$.  
La frequenza di trasmissione effettiva si trova tra $f_\text{min}$ e $f_\text{max}$.
$f_\text{min} = f - 10 \cdot \frac{f}{10^6} = \qty{14,2}{\mega\hertz} - 10 \cdot \frac{14,2\cdot \qty{\cancel{10^6}}{\mega\hertz}}{\cancel{10^6}} = \qty{14,2}{\mega\hertz} - \qty{142}{\hertz} = \qty{14,199858}{\mega\hertz}$
$f_\text{max} = f + 10 \cdot \frac{f}{10^6} = \qty{14,2}{\mega\hertz} + 10 \cdot \frac{14,2\cdot \qty{\cancel{10^6}}{\mega\hertz}}{\cancel{10^6}} = \qty{14,2}{\mega\hertz} + \qty{142}{\hertz} = \qty{14,200142}{\mega\hertz}$