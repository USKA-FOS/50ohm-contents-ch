Analysons maintenant, de gauche à droite, ce que le circuit fait avec la puissance introduite.

On observe d’abord un montage en parallèle de résistances de $\qty{110}{\ohm}$, $\qty{110}{\ohm}$ et deux résistances de $\qty{330}{\ohm}$. Nous savons qu’un système à $\qty{50}{\ohm}$ doit avoir une résistance d’entrée de $\qty{50}{\ohm}$. Si on le souhaite, on peut également vérifier cela en calculant le réseau de résistances.

D’après le recueil de formules :

$\frac{1}{R} = \frac{1}{110} + \frac{1}{110} + \frac{1}{2 \cdot 330}$

Ainsi, $R = \frac{660}{13} \approx \qty{50}{\ohm}$

Si l’on introduit $\qty{1}{\watt}$ dans ce montage en parallèle, on obtient :

$U = \sqrt{P \cdot R} = \sqrt{1 \cdot 50} \approx \sqrt{49} \approx \qty{7}{\volt}$

Pour la diode, seule la demi-onde supérieure compte, c’est-à-dire la tension de crête :

$\hat{U} = U \cdot \sqrt{2} \approx \qty{10}{\volt}$

La tension d’entrée est divisée par deux par le diviseur de tension de $2 \cdot \qty{330}{\ohm}$ puis réduite de $U_F$ :

$U_A = \frac{\hat{U}}{2} - U_F = \qty{5}{\volt} - \qty{0,23}{\volt} \approx \qty{4,8}{\volt}$