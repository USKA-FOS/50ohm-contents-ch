Données :

* Signal vocal avec une bande passante $f_\text{max}=\qty{4}{\kilo\hertz}$

Recherché :

* Fréquence d’échantillonnage $f_\text{s}$

Solution :

Pour qu’un échantillonnage sans erreur soit possible, la condition de Nyquist doit être respectée :

$f_\text{s} > 2 \cdot f_\text{max}$

Nous insérons :

$\begin{split} f_\text{s} &> 2 \cdot f_\text{max}\\ &> 2 \cdot \qty{4000}{\hertz}\\ &> \qty{8000}{\hertz} \end{split}$

La seule solution restante est donc $\qty{9600}{\sps}$, car cette valeur est la seule supérieure à $\qty{8000}{\hertz}$. 