I preamplificatori o convertitori di ricezione montati sulle antenne e separati dal ricevitore necessitano di un'alimentazione in corrente continua. Per evitare di dover aggiungere una linea di alimentazione in corrente continua dedicata, la tensione di alimentazione può essere trasmessa anche tramite il cavo coassiale, in parallelo al segnale ad alta frequenza, senza che i due segnali si disturbino reciprocamente. Per iniettare la tensione continua nel cavo coassiale si utilizza quindi un accoppiatore per alimentazione remota, detto anche BIAS-T in inglese. La figura [ref:a_qo100_bias_t] mostra una stazione QO-100 con accoppiatore per alimentazione remota per l'alimentazione del preamplificatore (LNB).

<margin>
[picture:1080:a_qo100_bias_t:Stazione QO-100 con accoppiatore per alimentazione remota per l'alimentazione dell'LNB]
</margin>

[question:AD322]

Tecnicamente, questa struttura può essere realizzata con un circuito molto semplice, come mostrato nella figura [ref:a_bias_t]. L'accoppiatore per alimentazione remota (BIAS-T) consiste, oltre ai connettori, solo di due condensatori e un'induttanza. Questo circuito lo abbiamo già incontrato nel MMIC, la cui tensione di alimentazione viene iniettata tramite un BIAS-T sull'uscita.

<margin>
[picture:399:a_bias_t:Accoppiatore per alimentazione remota (BIAS-T)]
</margin>

[question:AD323]

Un BIAS-T si riconosce dal fatto che su un lato viene trasmesso il segnale ad alta frequenza verso il ricevitore (RX), mentre sull'altro lato è collegato un preamplificatore o un convertitore di ricezione (LNA). Inoltre, tramite il connettore in corrente continua (DC) viene iniettata una tensione continua di alimentazione. Questa tensione continua raggiunge il conduttore interno del cavo coassiale tramite l'induttanza e alimenta così l'LNA collegato. L'induttanza, per l'alta frequenza, presenta un'elevata impedenza, in modo che il segnale ad alta frequenza non si scarichi nell'alimentazione.

Il condensatore di accoppiamento $C_1$ impedisce che la tensione continua iniettata raggiunga l'ingresso del ricevitore. Senza il condensatore $C_1$, la tensione di alimentazione potrebbe essere cortocircuitata verso massa.

[question:AD324]

---

L'induttanza serve per iniettare la tensione continua di alimentazione nella linea, mentre per l'alta frequenza rappresenta un'elevata resistenza. In questo modo, la tensione continua può raggiungere l'LNA senza che il segnale ad alta frequenza si scarichi nell'alimentazione. Il condensatore $C_2$ scarica verso massa eventuali residui di segnale ad alta frequenza. In questo modo si impedisce che i segnali ad alta frequenza si accoppino nell'alimentazione.

<indepth>
[photo:288:a_Bias T Platine:Scheda BIAS-T creata con KiCAD]
Ecco come potrebbe apparire la realizzazione pratica del circuito rappresentato su una scheda. $C_2$ e $C_3$ sono condensatori di disaccoppiamento per diverse bande di frequenza, garantendo il corretto funzionamento su un ampio spettro di frequenze. $L_1$ serve per l'alimentazione in corrente continua e deve essere dimensionata in base alla corrente di carico. Il condensatore di disaccoppiamento $C_2$ sul lato della tensione continua deve sopprimere la tensione ad alta frequenza. Deve essere scelto in modo che, alla frequenza di utilizzo dell'alta frequenza, presenti una reattanza inferiore a 1 ohm.
</indepth>

La bobina tra il lato DC (lato tensione continua, ad esempio $\qty{12}{\volt}$) e il lato ad alta frequenza (ad esempio $\qty{10}{\giga\hertz}$ segnale ricevuto) non deve far passare le componenti ad alta frequenza verso il lato DC. Si tratta quindi di una bobina di blocco che, alla frequenza di utilizzo, deve presentare un'elevata impedenza (ad esempio $X_L = \qty{10}{\kilo\ohm}$). Attraverso questa bobina di blocco passa la corrente di alimentazione per il preamplificatore o il convertitore (LNA). Il diametro del filo della bobina di blocco deve essere sufficientemente grande affinché la corrente continua di alimentazione non provochi un riscaldamento della bobina. In altre parole: la bobina deve avere una capacità di corrente adeguata.

[question:AD325]