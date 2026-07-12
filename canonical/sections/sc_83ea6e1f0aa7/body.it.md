I preamplificatori montati sull'antenna, o i convertitori di ricezione remoti, necessitano di un'alimentazione in corrente continua. Per evitare una linea di alimentazione in corrente continua aggiuntiva, la tensione di alimentazione può essere trasmessa anche tramite il cavo coassiale, parallelamente al segnale RF, senza che i due segnali si disturbino a vicenda. Per immettere la corrente continua nel cavo coassiale, viene quindi utilizzato uno splitter di alimentazione remota o, in inglese, BIAS-T. La figura [ref:a_qo100_bias_t] mostra una stazione QO-100 con splitter di alimentazione remota per l'alimentazione del preamplificatore (LNB).

<margin>
[picture:1080:a_qo100_bias_t:Stazione QO-100 con splitter di alimentazione remota per l'alimentazione dell'LNB]
</margin>

[question:AD322]

Tecnicamente, questa struttura può essere realizzata con un circuito molto semplice, come mostrato nella figura [ref:a_bias_t]. Lo splitter di alimentazione remota (BIAS-T) consiste, oltre ai collegamenti, solo in due condensatori e un'induttanza. Abbiamo già incontrato questo circuito con il MMIC, la cui tensione di alimentazione viene immessa tramite l'uscita con un BIAS-T.

<margin>
[picture:399:a_bias_t:Splitter di alimentazione remota (BIAS-T)]
</margin>

[question:AD323]

Un BIAS-T si riconosce dal fatto che da un lato il segnale RF viene convogliato verso il ricevitore (RX), mentre dall'altro lato è collegato un preamplificatore o un convertitore di ricezione (LNA). Inoltre, tramite l'uscita DC viene immessa una tensione di alimentazione continua. Questa tensione continua arriva tramite l'induttanza sul conduttore interno del cavo coassiale e alimenta così l'LNA collegato. L'induttanza agisce come un'alta impedenza per le alte frequenze, in modo che il segnale RF non defluisca nell'alimentazione elettrica.

Il condensatore di accoppiamento $C_1$ impedisce che la tensione continua immessa raggiunga l'ingresso del ricevitore. Senza il condensatore $C_1$, la tensione di alimentazione potrebbe quindi essere messa a massa in corto circuito.

[question:AD324]

---

L'induttanza serve a immettere la tensione di alimentazione continua nella linea, mentre rappresenta un'alta resistenza per le alte frequenze. In questo modo la tensione continua può raggiungere l'LNA senza che il segnale RF defluisca nell'alimentazione elettrica. Il condensatore $C_2$ scarica le restanti componenti ad alta frequenza verso massa. Ciò impedisce che i segnali RF si accoppino nell'alimentazione elettrica.

<indepth>
[photo:288:a_Bias T Platine:Scheda BIAS - T - creata con KiCAD]
L'implementazione pratica dello schema mostrato potrebbe apparire così su una scheda. $C_2$ e $C_3$ sono condensatori di disaccoppiamento per diverse bande di frequenza, in modo che la funzione sia garantita su un ampio campo di frequenza. $L_1$ serve per l'alimentazione della tensione continua e deve essere dimensionata in modo mirato per la corrente di carico. Il condensatore di disaccoppiamento $C_2$ sul lato della tensione continua deve sopprimere la tensione RF. Deve essere scelto in modo tale che presenti un'impedenza inferiore a 1 ohm alla frequenza di utilizzo RF.
</indepth>

La bobina tra il lato DC (lato corrente continua, ad es. $\qty{12}{\volt}$) e il lato RF (ad es. segnale ricevuto $\qty{10}{\giga\hertz}$) non deve lasciar passare componenti ad alta frequenza verso il lato DC. Si tratta quindi di una bobina di arresto, che deve avere un'alta impedenza alla frequenza di utilizzo (ad es. $X_L = \qty{10}{\kilo\ohm}$). Attraverso questa bobina di arresto scorre la corrente di alimentazione per il preamplificatore o convertitore (LNA). Il diametro del filo della bobina di arresto deve essere tale che la corrente continua di alimentazione non provochi un riscaldamento della bobina di arresto. In altre parole: la bobina deve avere un'adeguata capacità di carico.

[question:AD325]