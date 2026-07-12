Utilizziamo la formula dalla raccolta di formule:

$f_g = \frac{1}{2 \pi \cdot R \cdot C}$

Ma attenzione: quali valori devono essere considerati qui?

Guardando più da vicino $C_2$, vediamo che non fa parte del filtro passa-basso, ma serve solo a bloccare i disturbi nella tensione di alimentazione del circuito. Pertanto, $C_2$ non deve essere considerato qui.

L'alta frequenza di taglio e l'altissima impedenza di ingresso dell'amplificatore Audio possono essere trascurate e non devono essere considerate. Pertanto, inseriamo solo i valori $R_1 = \qty{4,7}{\kilo\ohm}$ e $C_1 = \qty{6,8}{\nano\farad}$.

Con i valori inseriti:

$\begin{split}f_g &= \frac{1}{2 \pi \cdot 4,7 \cdot \qty{10^3}{\ohm} \cdot 6,8 \cdot \qty{10^{-9}}{\farad}}\\ &\approx \qty{4979}{\hertz}\end{split}$