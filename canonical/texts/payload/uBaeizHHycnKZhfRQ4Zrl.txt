# Gegeben
* Sendefrequenz: $\qty{14,2}{\mega\hertz}$
* Genauigkeit: $\qty{10}{\ppm}$

# Lösungsweg
$\unit{ppm}$ steht für *parts per million*, $\qty{10}{\ppm}$ bedeutet also $10$ pro $10^6$.  
Die tatsächliche Sendefrequenz befindet sich zwischen $f_\text{min}$ und $f_\text{max}$.
$f_\text{min} = f - 10 \cdot \frac{f}{10^6} = \qty{14,2}{\mega\hertz} - 10 \cdot \frac{14,2\cdot \qty{\cancel{10^6}}{\mega\hertz}}{\cancel{10^6}} = \qty{14,2}{\mega\hertz} - \qty{142}{\hertz} = \qty{14,199858}{\mega\hertz}$
$f_\text{max} = f + 10 \cdot \frac{f}{10^6} = \qty{14,2}{\mega\hertz} + 10 \cdot \frac{14,2\cdot \qty{\cancel{10^6}}{\mega\hertz}}{\cancel{10^6}} = \qty{14,2}{\mega\hertz} + \qty{142}{\hertz} = \qty{14,200142}{\mega\hertz}$