# Gegeben
* Baken-Frequenz: $f_\text{Baken} = \qty{144,4}{\mega\hertz}$
* SSB-Bandbreite: $f_{B,max} = \qty{2,7}{\kilo\hertz}$
* Genauigkeit: $\qty{1}{\ppm}$

# Vorüberlegung
Der Abstand ($f_\text{Abstand}$) zur Baken-Frequenz ($f_\text{Baken}$) setzt sich aus der SSB-Bandbreite ($f_{B,max}$) und dem (Sicherheits-)Abstand ($\Delta f$) aufgrund der Ungenauigkeit von $\qty{1}{\ppm}$ zusammen. $\unit{ppm}$ steht für *parts per million*, $\qty{1}{\ppm}$ bedeutet also $1$ pro $10^6$. 

# Lösungsweg
$\Delta f = \qty{144,4}{\mega\hertz} \cdot \frac{1}{10^6} = \qty{144,4 \cdot \cancel{10^6}}{\hertz}\frac{1}{\cancel{10^6}} = \qty{144,4}{\hertz}= \qty{0,1444}{\kilo\hertz}$

$f_\text{Abstand} = f_{B,max} + \Delta f = \qty{2,7}{\kilo\hertz} + \qty{0,1444}{\kilo\hertz} = \qty{2,8444}{\kilo\hertz}$