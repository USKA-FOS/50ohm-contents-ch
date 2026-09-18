%TODO spostare eventualmente il capitolo altrove

Nel sottocapitolo *Decibel* del blocco dedicato a "corrente, tensione, resistenza, potenza, energia" è già stato accennato che i suffissi $\unit{\dBd}$ e $\unit{\dBi}$, utilizzati per indicare il guadagno d'antenna, specificano il riferimento di base. In questo caso il valore in decibel non si riferisce a una potenza o a una tensione, ma a un particolare radiatore di riferimento. I riferimenti più comuni sono $\unit{\dBi}$, riferito al radiatore isotropico sferico, e $\unit{\dBd}$, riferito al dipolo a semionda.

Il *radiatore isotropico* (cfr. figura [ref:e_Kugelstrahler]) è un'antenna ipotetica ideale che irradia con la stessa intensità in tutte le direzioni. Se un'antenna reale presenta una direttività, l'irradiazione sarà più intensa in alcune direzioni e meno intensa in altre rispetto a quella del radiatore isotropico ipotetico.

<margin>
[picture:751:e_Kugelstrahler:Radiatore isotropico al centro di una sfera, che genera la stessa potenza irradiata in tutti i punti della superficie sferica]
</margin>

Il guadagno in una direzione specifica (ad esempio nella direzione di massima irradiazione, che è quella con il massimo guadagno d'antenna) rispetto a un radiatore isotropico può essere espresso in decibel $\unit{\dB}$. Al posto di $\unit{\dB}$ si scrive $\unit{\dBi}$ per indicare chiaramente che ci si riferisce al radiatore isotropico.

[question:EG220]

Anche un semplice dipolo a semionda presenta un guadagno, poiché irradia perpendicolarmente al conduttore con un'intensità maggiore di $\qty{2,15}{\dB}$ rispetto a un radiatore isotropico. Pertanto, un dipolo a semionda ha un guadagno di $\qty{2,15}{\dBi}$.

Talvolta interessa il guadagno che supera quello di un dipolo a semionda, cioè il guadagno riferito a un dipolo a semionda. Questo viene espresso in $\unit{\dBd}$, dove la lettera $\text{d}$ sta per dipolo. Un dipolo a semionda ha quindi un guadagno di $\qty{0}{\dBd}$. Le antenne con un guadagno maggiore di un dipolo a semionda hanno un valore superiore a $\qty{0}{\dBd}$, mentre quelle con un guadagno inferiore hanno un valore inferiore a $\qty{0}{\dBd}$.

Confrontiamo ancora una volta il guadagno di un dipolo a semionda espresso in $\unit{\dBi}$ e in $\unit{\dBd}$: il dipolo a semionda ha un guadagno di $\qty{2,15}{\dBi}$ nella direzione di massima irradiazione, poiché irradia con un'intensità maggiore di $\qty{2,15}{\dB}$ rispetto al radiatore isotropico. Espresso in $\unit{\dBd}$, invece, il valore è $\qty{0}{\dBd}$. L'indicazione in $\unit{\dBi}$ è sempre superiore di $\qty{2,15}{\dB}$ rispetto a quella in $\unit{\dBd}$.

Questo è anche riportato nella raccolta di formule:

$g_i = g_d + \qty{2,15}{\dB}$

[question:EG221]