Donné : 

* Signal vocal avec $f_\text{max}=\qty{4}{\kilo\hertz}$ de bande passante

Recherché : 

* Fréquence d'échantillonnage $f_\text{s}$

Solution:

Pour qu'un échantillonnage sans erreur soit possible, la condition de Nyquist doit être remplie : 

 $f_\text{s} > 2 \cdot f_\text{max}$

Nous insérons : 

$\begin{split} f_\text{s} &> 2 \cdot f_\text{max}\\ &> 2 \cdot \qty{4000}{\hertz}\\ &> \qty{8000}{\hertz} \end{split}$

Il ne reste donc que la solution $\qty{9600}{\sps}$, car seule cette valeur est supérieure à $\qty{8000}{\hertz}$.
