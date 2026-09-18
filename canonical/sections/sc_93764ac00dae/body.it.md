Già dal capitolo [sec:halbleiter] è nota la funzione di base del diodo: esso lascia fluire la corrente solo in una direzione, cioè quando la tensione applicata all'anodo ($U_a$) è maggiore della tensione al catodo ($U_k$), cfr. figura [ref:e_diode_u_i].

<margin>
[picture:859:e_diode_u_i:Tensioni e corrente in un diodo con resistenza in serie]
</margin>

Matematicamente possiamo esprimere questa condizione come:

$U_d = U_a - U_k > 0$

Tuttavia, se $U_d$ è solo leggermente maggiore di 0, non scorre ancora una corrente apprezzabile. Questo è dovuto alla *caratteristica esponenziale* di un diodo. La corrente del diodo è infatti:

$I_d = I_S \left(e^{\frac{U_d}{U_T}}-1\right)$

$e$ è il numero di Euler ($e\approx 2,718$), $U_T$ è una costante che a temperatura ambiente ammonta a circa $\qty{26}{\milli\volt}$.

$I_S$ è qui la *corrente di saturazione inversa*, cioè la corrente molto piccola che fluisce attraverso il diodo in caso di tensioni negative. Il valore di $I_S$ dipende, oltre che da alcuni parametri del diodo come la superficie del diodo, soprattutto dal materiale semiconduttore utilizzato. Con materiali come il germanio (Ge) con una piccola *banda proibita* (su cui ci soffermeremo nel capitolo [sec:diode_2] della formazione per HB9) $I_S$ è maggiore, mentre con materiali con banda proibita più ampia $I_S$ è minore.

<margin>
[picture:861:e_diode_kennlinie_iu:Caratteristica corrente-tensione di un diodo]
</margin>

[question:EC501]

Osservando la caratteristica di un diodo in figura [ref:e_diode_kennlinie_iu], la corrente del diodo aumenta bruscamente a partire da una certa tensione positiva. Questa tensione viene anche chiamata *tensione di soglia* $U_{th}$, ma è solo l'espressione dei diversi valori di $I_S$: più $I_S$ è piccolo, più alta è la tensione di soglia.

Come riferimento per la tensione di soglia delle diodi pn possiamo indicare circa $\qtyrange{0,2}{0,3}{\volt}$ per il Ge e circa $\qtyrange{0,6}{0,7}{\volt}$ per il Si.

<attention>
La tensione di soglia $U_{th}$ viene anche chiamata *tensione diretta*, perché solo oltre questa tensione la corrente inizia a fluire in modo marcato.
</attention>

I *diodi a emissione luminosa* (LED) sono anch'essi diodi pn, nei quali il materiale semiconduttore è tale da emettere luce quando il diodo è polarizzato in direzione diretta. Questo è possibile solo con materiali specifici, non con Si e Ge. Il colore della luce è determinato dalla banda proibita. Più la banda proibita è ampia, più corta è la lunghezza d'onda della luce, minore è la corrente di saturazione inversa e, di conseguenza, più alta è la tensione di soglia. Pertanto, i LED rossi hanno una tensione di soglia di circa $\qty{1,7}{\volt}$ e i LED verdi di circa $\qty{2,5}{\volt}$. Le diverse caratteristiche sono mostrate nella figura [ref:e_diode_kennlinien].

[question:EC513]
[question:EC510]
[question:EC509]
[question:EC511]
[question:EC512]

---

<margin>
[picture:858:e_diode_kennlinien:Caratteristiche di diversi diodi]
</margin>

[question:EC503]
[question:EC506]
[question:EC507]
[question:EC508]

Poiché i LED funzionano in direzione diretta, è importante inserire una resistenza $R_V$ tra la sorgente di tensione $U$ e il LED. $R_V$ regola la corrente desiderata $I$. In questo caso, occorre tenere conto della tensione di soglia $U_{th}$ del LED:

$ I=\frac{U-U_{th}}{R_V}$

[question:EC514]
[question:EC515]
[question:EC516]

---

Nel nostro modello semplice, per $U_d$ negative scorre solo una piccola corrente inversa. Tuttavia, questo non è vero per tensioni molto negative. A un certo punto, il campo elettrico nella zona di svuotamento tra n e p diventa troppo intenso e il diodo "cede", la corrente in direzione inversa aumenta drasticamente, come mostrato nella figura [ref:n_diode_kennlinie_uz].

Questa *rottura in polarizzazione inversa* può avere diverse cause fisiche, che non tratteremo in dettaglio qui. La tensione alla quale avviene questa rottura è generalmente chiamata *tensione di Zener* $U_z$, anche se l'effetto Zener (un effetto tunnel quantistico) è solo uno dei possibili meccanismi di rottura. Le *diodi Zener* vengono utilizzate per la stabilizzazione della tensione. In questo caso, è importante limitare la corrente di rottura con una resistenza in serie.

<margin>
[picture:862:n_diode_kennlinie_uz:Caratteristica di una diodo Zener]
</margin>

---

Il simbolo elettrico di una diodo Zener (figura [ref:e_zener_symbol]) è quello di un diodo regolare, in cui il trattino del catodo presenta un'estensione aggiuntiva a $\qty{90}{\degree}$. Questo serve a ricordare il "ripiegamento" della caratteristica in corrispondenza della rottura.

<margin>
[picture:860:e_zener_symbol:Simbolo elettrico di una diodo Zener]
</margin>

[question:EC517]
[question:EC520]
[question:EC521]
[question:EC522]

Finora abbiamo trattato solo *diodi pn*, le cui proprietà derivano da una giunzione semiconduttore. Nei *diodi Schottky* le proprietà derivano da una giunzione metallo-semiconduttore. La tensione di soglia è circa la metà di quella di un diodo pn dello stesso materiale, o inferiore, a seconda della progettazione specifica della giunzione metallo-semiconduttore. I diodi Schottky vengono utilizzati quando si desidera una bassa tensione di soglia o come diodi di commutazione molto veloci.

[question:EC504]
[question:EC505]

<margin>
I diodi metallo-semiconduttore sono i più antichi componenti rettificatori a semiconduttore. Ferdinand Braun scoprì il loro effetto rettificatore già nel 1874, senza però poterlo spiegare.
</margin>

Riassumendo:

I diodi lasciano fluire la corrente solo in una direzione. Pertanto, sono adatti alla rettificazione della corrente alternata.

Tuttavia, a tensioni inverse elevate ($U_d < U_z$), la corrente in direzione inversa aumenta notevolmente. Questo punto di funzionamento può essere utilizzato molto bene per la stabilizzazione della tensione (*diodo Zener*).

Inoltre, in polarizzazione inversa possono essere utilizzati come capacità controllate in tensione, ma questo lo tratteremo solo nella formazione per la classe A.

[question:EC502]
[question:EC518]
[question:EC519]