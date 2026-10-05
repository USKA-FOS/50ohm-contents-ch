I preamplificatori o convertitori di ricezione montati sull'antenna e posizionati a distanza richiedono un'alimentazione in corrente continua. Per risparmiare una linea di alimentazione in corrente continua aggiuntiva, la tensione di alimentazione può essere trasmessa anche attraverso il cavo coassiale, parallelamente al segnale ad alta frequenza, senza che i due segnali si disturbino a vicenda. Per immettere la tensione continua nel cavo coassiale viene quindi utilizzato un accoppiatore per alimentazione remota o, in inglese, BIAS-T. La figura [ref:a_qo100_bias_t] mostra una stazione QO-100 con accoppiatore per alimentazione remota per l'alimentazione elettrica del preamplificatore (LNB).

<margin>
[picture:1080:a_qo100_bias_t:Stazione QO-100 con accoppiatore per alimentazione remota per l'alimentazione dell'LNB]
</margin>

[question:AD322]

<wordorigin>
*Terminologia*

- BIAS-T: Circuito a forma di T, con il quale una tensione continua (BIAS) e un segnale ad alta frequenza possono essere condotti insieme su una linea o separati l'uno dall'altro.

- BIAS = Tensione di polarizzazione o tensione continua, che viene sovrapposta a un segnale. In elettronica, bias indica generalmente una tensione continua o una corrente continua per l'impostazione del punto di lavoro.

</wordorigin>

Tecnicamente, questa struttura, come mostrato nella figura [ref:a_bias_t], può essere realizzata con un circuito molto semplice. L'accoppiatore per alimentazione remota (BIAS-T) consiste, oltre ai collegamenti, solo di due condensatori e un'induttanza. Abbiamo già conosciuto questo circuito con l'MMIC nella sezione [sec:integrierte_schaltkreise], la cui tensione di alimentazione viene immessa attraverso l'uscita con un BIAS-T.

<margin>
[picture:399:a_bias_t:Accoppiatore per alimentazione remota (BIAS-T)]
</margin>

<wordorigin>
*altri termini*

  - LNA = *L*ow *N*oise *A*mplifier, un preamplificatore a basso rumore

  - LNB = *L*ow *N*oise *B*lock, un preamplificatore e down-converter a basso rumore
    L'LNB è trattato in dettaglio nella sezione [sec:low_noise_block].

</wordorigin>

[question:AD323]

Un BIAS-T si riconosce dal fatto che da un lato il segnale ad alta frequenza viene condotto al ricevitore (RX), mentre dall'altro lato è collegato un preamplificatore o un convertitore di ricezione (LNA). Inoltre, attraverso il connettore DC viene immessa una tensione di alimentazione continua. Questa tensione continua arriva attraverso l'induttanza al conduttore interno del cavo coassiale e alimenta così l'LNA collegato. L'induttanza agisce come alta impedenza per l'alta frequenza, in modo che il segnale ad alta frequenza non fluisca nell'alimentazione elettrica.

Il condensatore di accoppiamento $C_1$ impedisce che la tensione continua immessa raggiunga l'ingresso del ricevitore. Senza il condensatore $C_1$, la tensione di alimentazione potrebbe quindi essere cortocircuitata a massa.

[question:AD324]

---

L'induttanza serve a immettere la tensione di alimentazione continua nella linea, mentre per l'alta frequenza rappresenta un'alta resistenza. In questo modo, la tensione continua può raggiungere l'LNA senza che il segnale ad alta frequenza fluisca nell'alimentazione elettrica. Il condensatore $C_2$ conduce le rimanenti componenti ad alta frequenza verso massa. Ciò impedisce che i segnali ad alta frequenza si accoppino nell'alimentazione elettrica.

<indepth>
[photo:288:a_Bias T Platine:Placcato BIAS-T - creato con KiCAD]
Così potrebbe apparire l'implementazione pratica dello schema circuitale raffigurato in un circuito stampato. $C_2$ e $C_3$ sono condensatori di blocco per diverse bande di frequenza, in modo che la funzione sia garantita su un'ampia banda di frequenza. $L_1$ serve per la linea di alimentazione della tensione continua e deve essere dimensionata specificamente per la corrente di carico. Il condensatore di blocco $C_2$ sul lato della tensione continua deve sopprimere la tensione ad alta frequenza. Deve essere scelto in modo che alla frequenza operativa ad alta frequenza rappresenti una reattanza inferiore a 1 ohm.
</indepth>

La bobina tra il lato DC (lato della tensione continua, ad esempio $\qty{12}{\volt}$) e il lato HF (ad esempio, segnale ricevuto a $\qty{10}{\giga\hertz}$) non deve far passare le componenti ad alta frequenza verso il lato DC. Si tratta quindi di un'induttanza di blocco, che alla frequenza operativa deve agire come alta impedenza (ad esempio, $X_L = \qty{10}{\kilo\ohm}$). Attraverso questa induttanza di blocco scorre la corrente di alimentazione per il preamplificatore o il convertitore (LNA). Il diametro del filo dell'induttanza di blocco deve essere abbastanza grande da evitare che la corrente continua di alimentazione causi il riscaldamento dell'induttanza di blocco. In altre parole: la bobina deve avere una corrispondente capacità di carico di corrente.

[question:AD325]
