Nous utilisons la formule du recueil de formules :

$f_g = \frac{1}{2 \pi \cdot R \cdot C}$

Mais attention : quelles valeurs doivent être prises en compte ici ?

En examinant $C_2$, nous constatons qu'il ne fait pas partie du filtre passe-bas, mais sert uniquement à bloquer les perturbations dans la tension d'alimentation du circuit. Par conséquent, $C_2$ ne doit pas être pris en compte ici.

La fréquence de coupure élevée et l'impédance d'entrée très élevée de l'amplificateur audio peuvent être négligées et ne doivent pas non plus être prises en compte. Nous utilisons donc uniquement $R_1 = \qty{4,7}{\kilo\ohm}$ et $C_1 = \qty{6,8}{\nano\farad}$.

Avec les valeurs insérées :

$\begin{split}f_g &= \frac{1}{2 \pi \cdot 4,7 \cdot \qty{10^3}{\ohm} \cdot 6,8 \cdot \qty{10^{-9}}{\farad}}\\ &\approx \qty{4979}{\hertz}\end{split}$