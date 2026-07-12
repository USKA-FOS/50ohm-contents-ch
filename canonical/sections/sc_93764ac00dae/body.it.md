Dalla classe N è già nota la funzione base della Diode: essa lascia fluire la corrente solo in una direzione, ovvero quando la tensione applicata all'anodo ($U_a$) è maggiore della tensione al catodo ($U_k$), cfr. figura [ref:e_diode_u_i].

<margin>
[picture:859:e_diode_u_i:Tensioni e corrente su una diodo con resistenza in serie]
</margin>

Matematicamente possiamo scrivere questa condizione così:

$U_d = U_a - U_k > 0$

Tuttavia, se $U_d$ è solo leggermente maggiore di 0, non scorre ancora alcuna corrente apprezzabile. Ciò è dovuto alla *caratteristica esponenziale* di una diodo. La corrente di diodo è infatti:

$I_d = I_S \left(e^{\frac{U_d}{U_T}}-1\right)$

$e$ è il cosiddetto numero di Eulero ($e\approx 2,718$), $U_T$ una costante che a temperatura ambiente è di circa $\qty{26}{\milli\volt}$.

$I_S$ è qui la *corrente di saturazione inversa*, che è la corrente molto piccola che scorre attraverso la diodo a tensioni negative. Il valore di $I_S$ dipende, oltre ad alcuni parametri della diodo come l'area della diodo, soprattutto dal materiale semiconduttore utilizzato. Per materiali come il germanio (Ge) con una bassa *banda proibita* (tratteremo questo più in dettaglio nella formazione per la classe A), $I_S$ è maggiore, per materiali con una banda proibita più ampia, $I_S$ è minore.

<margin>
[picture:861:e_diode_kennlinie_iu:Caratteristica di una diodo]
</margin>

[question:EC501]

Considerando una caratteristica di diodo nella figura [ref:e_diode_kennlinie_iu], la corrente di diodo aumenta ripidamente a $U_d$ positivi a partire da una certa tensione. Questa tensione è chiamata anche *tensione di soglia* $U_{th}$, ma è solo un'espressione delle diverse $I_S$: minore è $I_S$, maggiore è la tensione di soglia.

Come indicazioni per la tensione di soglia delle diodi pn, possiamo indicare per Ge circa $\qtyrange{0,2}{0,3}{\volt}$ e per Si circa $\qtyrange{0,6}{0,7}{\volt}$.

I *diodi a emissione luminosa* (LED) sono anch'essi diodi pn, in cui il materiale semiconduttore è tale che, quando la diodo è polarizzata in direzione diretta, emette luce. Ciò è possibile solo con determinati materiali - non con Si e Ge. Il colore della luce è dato dalla banda proibita. Maggiore è la banda proibita, più corta è la lunghezza d'onda della luce, minore è la corrente di saturazione inversa e quindi maggiore è la tensione di soglia. Pertanto, i LED rossi hanno una tensione di soglia di circa $\qty{1,7}{\volt}$ e i LED verdi di circa $\qty{2,5}{\volt}$. Le diverse caratteristiche sono rappresentate nella figura [ref:e_diode_kennlinien].

[question:EC513]
[question:EC510]
[question:EC509]
[question:EC511]
[question:EC512]

---

<margin>
[picture:858:e_diode_kennlinien:Caratteristiche di diverse diodi]
</margin>


[question:EC503]
[question:EC506]
[question:EC507]
[question:EC508]

Dato che i LED vengono utilizzati in direzione diretta, è importante collegare una resistenza $R_V$ tra la fonte di tensione $U$ e il LED. $R_V$ imposta la corrente desiderata $I$. La tensione di soglia $U_{th}$ del LED deve essere considerata:

$ I=\frac{U-U_{th}}{R_V}$

[question:EC514]
[question:EC515]
[question:EC516]

---

Nel nostro modello semplice, per $U_d$ negativi scorre solo una piccola corrente inversa. Tuttavia, ciò non è vero per tensioni molto negative. Ad un certo punto, il campo elettrico attraverso la zona di svuotamento tra n e p diventa troppo elevato e la diodo "va in breakdown", la corrente in direzione inversa aumenta estremamente, come mostrato nella figura [ref:n_diode_kennlinie_uz].

Questo *breakdown inverso* può avere diverse cause fisiche, che non possiamo trattare in dettaglio qui. La tensione alla quale si verifica questo breakdown è comunemente chiamata *tensione Zener* $U_z$, anche se l'effetto Zener (un effetto tunnel quantomeccanico) è solo un possibile meccanismo di breakdown. Le *diodi Zener* vengono utilizzate per la stabilizzazione della tensione. È importante limitare la corrente di breakdown tramite una resistenza in serie.

<margin>
[picture:862:n_diode_kennlinie_uz:Caratteristica di una diodo Zener]
</margin>

---

Il simbolo di circuito di una diodo Zener (figura [ref:e_zener_symbol]) è quello di una diodo normale, in cui la linea del catodo riceve un'ulteriore estensione a $\qty{90}{\degree}$. Questo dovrebbe ricordare la "piegatura" della caratteristica nel breakdown.

<margin>
[picture:860:e_zener_symbol:Simbolo di circuito di una diodo Zener]
</margin>



[question:EC517]
[question:EC520]
[question:EC521]
[question:EC522]

Le diodi trattate finora erano tutte *diodi pn*, la proprietà di diodo deriva da una giunzione semiconduttrice. La *diodo Schottky* è una diodo le cui proprietà derivano da una giunzione metallo-semiconduttore. La tensione di soglia è circa la metà di quella di una diodo pn dello stesso materiale, o inferiore, a seconda della progettazione esatta della giunzione metallo-semiconduttore. Le diodi Schottky vengono utilizzate quando la tensione di soglia deve essere bassa, o come diodi di commutazione molto veloci.

[question:EC504]
[question:EC505]

<margin>
Le diodi metallo-semiconduttore sono i più antichi elementi raddrizzatori a base semiconduttrice. Ferdinand Braun scoprì il loro effetto raddrizzatore già nel 1874, senza però poter spiegare la sua osservazione.
</margin>

Riassumendo:

Le diodi lasciano fluire la corrente solo in una direzione. Pertanto, sono adatte per la rettifica della corrente alternata.

Tuttavia, a tensioni inverse elevate ($U_d < U_z$), la corrente in direzione inversa aumenta fortemente. Questo punto di funzionamento può essere utilizzato molto bene per la stabilizzazione della tensione (*diodo Zener*).

Inoltre, possono essere utilizzate come capacità controllate in tensione in direzione inversa, ma ciò verrà trattato solo nella formazione per la classe A.

[question:EC502]
[question:EC518]
[question:EC519]
