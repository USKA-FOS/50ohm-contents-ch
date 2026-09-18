Utilizziamo la formula dalla raccolta di formule:

$f_g = \frac{1}{2 \pi \cdot R \cdot C}$

Ma attenzione: quali valori devono essere considerati qui?

Osservando $C_2$, notiamo che questo non fa parte del filtro passa-basso, ma serve solo per bloccare disturbi nella tensione di alimentazione del circuito. Pertanto, $C_2$ non deve essere considerato qui.

L'alta frequenza di taglio e l'impedenza di ingresso molto elevata dell'amplificatore audio sono trascurabili e non devono essere considerate. Utilizziamo quindi solo $R_1 = \qty{4,7}{\kilo\ohm}$ e $C_1 = \qty{6,8}{\nano\farad}$.

Con i valori inseriti:

$\begin{split}f_g &= \frac{1}{2 \pi \cdot 4,7 \cdot \qty{10^3}{\ohm} \cdot 6,8 \cdot \qty{10^{-9}}{\farad}}\\ &\approx \qty{4979}{\hertz}\end{split}$