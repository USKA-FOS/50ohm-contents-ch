Dal capitolo [sec:halbleiter] è già nota la funzione base del diodo: permette il passaggio di corrente solo in una direzione, cioè quando la tensione applicata all'anodo ($U_a$) è maggiore della tensione al catodo ($U_k$), cfr. figura [ref:e_diode_u_i].

<margin>
[picture:859:e_diode_u_i:Tensioni e corrente in un diodo con resistenza in serie]
</margin>

Matematicamente possiamo esprimere questa condizione così:

$U_d = U_a - U_k > 0$

Tuttavia, se $U_d$ è solo leggermente maggiore di 0, non scorre ancora una corrente apprezzabile. Non appena $U_d$ supera una tensione di soglia, scorre una corrente elevata. Questa tensione di soglia dipende dal tipo di diodo e viene anche chiamata tensione di conduzione, perché quando viene superata la corrente scorre abbondantemente. Ciò è dovuto alla *caratteristica esponenziale* di un diodo.

<margin>
[picture:861:e_diode_kennlinie_iu:Caratteristica di un diodo]
</margin>

<indepth>
La corrente del diodo è data da un'equazione esponenziale. Si dice "esponenziale" perché la variabile indipendente $U_d$ si trova nell'esponente, cioè nella "potenza".

$I_d = I_S \left(e^{\frac{U_d}{U_T}}-1\right)$

$e$ è il cosiddetto numero di Eulero ($e\approx 2,718$), $U_T$ è una costante che a temperatura ambiente è circa $\qty{26}{\milli\volt}$.

$I_S$ qui è la *corrente di saturazione inversa*, cioè la corrente molto piccola che scorre attraverso il diodo per tensioni negative. Il valore di $I_S$ dipende, oltre che da alcuni parametri del diodo come l'area del diodo, soprattutto dal materiale semiconduttore utilizzato. Per materiali come il germanio (Ge) con un piccolo *bandgap* (ci torneremo più in dettaglio nella sezione [sec:diode_2]), $I_S$ è maggiore; per materiali con bandgap maggiore, $I_S$ è minore.
</indepth>

[question:EC501]

Considerando una caratteristica di un diodo nella figura [ref:e_diode_kennlinie_iu], la corrente del diodo per $U_d$ positivi aumenta bruscamente oltre una certa tensione. Questa tensione è anche chiamata *tensione di soglia* $U_{th}$, ma è solo un'espressione dei diversi $I_S$: più piccolo è $I_S$, più alta è la tensione di soglia.

Come riferimento per la tensione di soglia dei diodi, possiamo indicare per il germanio (Ge) circa $\qtyrange{0,2}{0,3}{\volt}$ e per il silicio (Si) circa $\qtyrange{0,6}{0,7}{\volt}$.

<attention>
La tensione di soglia $U_{th}$ è anche chiamata *tensione di conduzione*, perché è solo oltre questa tensione che la corrente inizia a scorrere in modo significativo.
</attention>

%<margin>
%*Analogia di un diodo con un canale d'acqua:*
%
%Una valvola di ritegno a sfera caricata a molla blocca finché la forza del flusso $F_{\text{Strom}}$ è minore della forza della molla $F_{\text{Feder}}$ (sopra); quando supera la forza di soglia, la sfera si solleva e il canale diventa conduttivo (sotto) – analogo al comportamento di un diodo al di sopra della sua tensione di soglia $U_S$.
%[picture:10102:e_diode_wasserkanal_analogie:Analogia_canale_acqua]
%</margin>
% commentato perché il testo è distorto.

I *diodi luminosi* (LED) sono diodi speciali in cui il materiale semiconduttore è tale da emettere luce quando il diodo è polarizzato in conduzione. Ciò è possibile solo con materiali specifici - non con Si e Ge. Il colore della luce è determinato dal bandgap. Maggiore è il bandgap, più corta è la lunghezza d'onda della luce, minore è la corrente di saturazione inversa e quindi più alta è la tensione di soglia. Pertanto, i LED rossi hanno circa $\qty{1,7}{\volt}$ di tensione di soglia e i LED verdi $\qty{2,5}{\volt}$. Le diverse caratteristiche sono mostrate nella figura [ref:e_diode_kennlinien].

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

Poiché i LED operano in polarizzazione diretta, è importante collegare una resistenza $R_V$ tra la sorgente di tensione $U$ e il LED. $R_V$ imposta la corrente desiderata $I$. In questo caso, va considerata la tensione di soglia $U_{th}$ del LED:

$ I=\frac{U-U_{th}}{R_V}$

[question:EC514]
[question:EC515]
[question:EC516]

---

Nel nostro semplice modello, per $U_d$ negative scorre solo una piccola corrente inversa. Tuttavia, ciò non vale per tensioni molto negative. Ad un certo punto, il campo elettrico attraverso lo strato di sbarramento diventa troppo alto e il diodo "va in breakdown", la corrente in direzione inversa aumenta estremamente, come mostrato nella figura [ref:n_diode_kennlinie_uz].

Questo *breakdown inverso* può avere diverse cause fisiche, che non possiamo trattare qui in dettaglio. La tensione alla quale avviene questo breakdown è comunemente chiamata *tensione Zener* $U_z$, anche se l'effetto Zener (un effetto tunnel quantomeccanico) è solo un possibile meccanismo di breakdown. I *diodi Zener* sono utilizzati per la stabilizzazione della tensione. In questo caso, è importante limitare la corrente di breakdown con una resistenza in serie.

<margin>
[picture:862:n_diode_kennlinie_uz:Caratteristica di un diodo Z]
</margin>

---

Il simbolo elettrico di un diodo Zener (figura [ref:e_zener_symbol]) è quello di un diodo regolare, in cui la linea del catodo ha un'ulteriore estensione a $\qty{90}{\degree}$. Questo dovrebbe ricordare la "piegatura" della caratteristica nel breakdown.

<margin>
[picture:860:e_zener_symbol:Simbolo elettrico di un diodo Zener]
</margin>



[question:EC517]
[question:EC520]
[question:EC521]
[question:EC522]

I diodi trattati finora erano diodi la cui proprietà di diodo deriva da una giunzione semiconduttore, che sarà trattata solo in [sec:diode_2]. Il *diodo Schottky* è un diodo le cui proprietà derivano da una giunzione metallo-semiconduttore. La tensione di soglia è circa la metà di quella di un diodo a semiconduttore convenzionale dello stesso materiale, o inferiore, a seconda della configurazione esatta della giunzione metallo-semiconduttore. I diodi Schottky sono utilizzati quando la tensione di soglia deve essere bassa, o come diodi di commutazione molto veloci.

[question:EC504]
[question:EC505]

<margin>
I diodi metallo-semiconduttore sono i più antichi componenti raddrizzatori a base di semiconduttori. Ferdinand Braun scoprì il loro effetto raddrizzatore già nel 1874, senza però poter spiegare la sua osservazione.
</margin>

Riassumendo:

I diodi permettono il passaggio di corrente solo in una direzione. Pertanto, sono adatti per la raddrizzatura della corrente alternata.

Tuttavia, ad alte tensioni inverse ($U_d < U_z$), la corrente in direzione inversa aumenta fortemente. Questo punto di funzionamento può essere utilizzato molto bene per la stabilizzazione della tensione (*diodo Zener*).

Inoltre, in polarizzazione inversa possono essere utilizzati come capacità controllate in tensione, ma questo lo tratteremo solo nella sezione [sec:oszillator_vco].

[question:EC502]
[question:EC518]
[question:EC519]
