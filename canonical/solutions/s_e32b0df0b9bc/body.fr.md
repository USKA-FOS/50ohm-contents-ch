Tout d'abord, nous devons déterminer la fréquence de résonance du circuit oscillant à partir des valeurs de *L* et *C* selon la formule du circuit oscillant de Thomson, car les équations mentionnées ne s'appliquent qu'au cas de résonance !

$f = \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}$

Avec les valeurs insérées :

$\begin{split} f &= \frac{1}{2 \pi \cdot \sqrt{100 \cdot \qty{10^{-6}}{\henry} \cdot 0,01 \cdot 10^{-6}\text{ F}}} \\ &\approx \qty{159154,94}{\hertz} \approx 159,2 \cdot \qty{10^3}{\hertz}\\ &\approx \qty{159,2}{\kilo\hertz}\end{split}$
  
Ainsi, la résistance inductive $X_\text{L}$ peut être calculée comme suit (formules du recueil de formules) :

Vitesse angulaire : $\omega = 2 \pi \cdot f$

Résistance inductive : $X_\text{L} = \omega \cdot L$

Avec les valeurs insérées :
$\begin{split}X_\text{L} &= 2 \pi \cdot 159,2 \cdot \qty{10^3}{\hertz} \cdot 100 \cdot \qty{10^{-6}}{\henry}\\ &\approx \qty{100,03}{\ohm}\end{split}$
  
La qualité se calcule ensuite en tenant compte de la résistance ohmique $R_\text{S}$ :
  
$\begin{split}Q &= \frac{X_\text{L}}{R_\text{S}}\\\text{Avec les valeurs insérées :}\\Q &= \frac{\qty{100,03}{\ohm}}{\qty{10}{\ohm}} \approx 10\end{split}$