Come ricevitore più semplice abbiamo conosciuto nel capitolo precedente il ricevitore a rivelatore. Il ricevitore a rivelatore è un cosiddetto ricevitore lineare, che abbiamo già imparato a conoscere nella classe N. Nel ricevitore lineare, come mostrato nella figura [ref:e_geradeausempfänger], il segnale, dopo la ricezione e, se necessario, l’amplificazione, viene solo demodulato. Questo concetto di ricevitore presenta tuttavia lo svantaggio di una scarsa selettività (potere risolutivo). Per migliorare questo aspetto, si potrebbe combinare il blocco del filtro di ingresso (2) con più filtri per aumentare il potere risolutivo. Tuttavia, in tal caso, al variare della frequenza di ricezione tutti questi filtri dovrebbero essere adattati, il che risulta molto laborioso. Per questo motivo è stato sviluppato il *ricevitore supereterodina* (cfr. figura [ref:ueberlagerungsempfaenger_einfachsuper]), che nella terminologia tecnica viene anche chiamato *Superheterodyn* o semplicemente *Superhet*.


<margin>
[picture:736:e_geradeausempfänger:Ricevitore lineare]
</margin>

<margin>
[picture:803:ueberlagerungsempfaenger_einfachsuper:Ricevitore supereterodina con amplificatori]
</margin>

---


L’idea del ricevitore supereterodina è semplice quanto geniale. Al posto di filtri sintonizzabili, viene impiegato un oscillatore variabile (VFO), grazie al quale il segnale ricevuto viene prima convertito su una frequenza fissa, la cosiddetta frequenza intermedia $f_z$ (spesso chiamata anche IF). Per questa frequenza intermedia fissa è possibile realizzare filtri molto selettivi e di alta qualità. La figura [ref:ueberlagerungsempfaenger_einfachsuper_filter] illustra questo principio.


<margin>
[picture:913:ueberlagerungsempfaenger_einfachsuper_filter:Ricevitore supereterodina con filtri]
</margin>


Il filtro di ingresso lascia passare inizialmente solo la banda di frequenza desiderata, ad esempio la banda delle onde corte. Successivamente, un mixer converte il segnale di ingresso insieme alla frequenza del VFO sulla frequenza intermedia costante, ad esempio $\qty{455}{\kilo\hertz}$. Nel caso specifico, il VFO può essere impostato tra $\qty{3,455}{\mega\hertz}$ e $\qty{30,455}{\mega\hertz}$ per poter convertire verso il basso l’intera banda delle onde corte. Il vantaggio decisivo del ricevitore supereterodina rispetto al ricevitore lineare risiede proprio in questa frequenza intermedia costante: la filtrazione del segnale può essere ottimamente sintonizzata su una frequenza fissa, ottenendo così un’elevata selettività, cioè un elevato potere risolutivo.


---


Poiché i filtri non devono essere sintonizzabili, possono essere ottimizzati in modo mirato per quanto riguarda la larghezza di banda e la pendenza del fronte, ad esempio mediante l’impiego di filtri a quarzo, ceramici o digitali. In questo modo, ad esempio, per la trasmissione vocale (SSB) si possono utilizzare filtri con una larghezza di banda di circa $\qty{2,4}{\kilo\hertz}$ e per la telegrafia (CW) filtri a banda stretta con circa $\qty{300}{\hertz}$. Anche per altre modalità di trasmissione come AM, FM o modi digitali possono essere utilizzati filtri appositamente adattati.


Grazie a questo concetto, il ricevitore supereterodina raggiunge un potere risolutivo notevolmente superiore rispetto al ricevitore lineare. Un ulteriore vantaggio consiste nel fatto che tutti i moduli successivi lavorano sempre con la stessa frequenza intermedia e quindi non devono essere realizzati come sintonizzabili, il che semplifica la struttura e migliora la qualità della ricezione.


[question:EF102]


I ricevitori supereterodina possono funzionare con una o più frequenze intermedie. Nel caso più semplice si tratta di un ricevitore a conversione diretta, in cui la frequenza intermedia è la frequenza BF desiderata. A tal fine, la frequenza dell’oscillatore deve essere molto vicina alla frequenza di ricezione.


[question:EF208]


Un ricevitore supereterodina presenta tuttavia anche alcuni svantaggi, in particolare la comparsa delle cosiddette frequenze immagine. Questa problematica, così come concetti avanzati di ricevitore come il multiplo supereterodina con più frequenze intermedie, verranno trattati in modo approfondito solo nella classe A.


<indepth>
L’inventore del ricevitore supereterodina non può essere identificato in modo univoco. Ciò è dovuto anche al fatto che il suo sviluppo risale al periodo della Prima guerra mondiale, durante il quale tutte le parti in conflitto lavoravano intensamente al miglioramento delle tecniche radiofoniche e di radiocomunicazione. A partire dal 1918 circa, diversi ricercatori, indipendentemente l’uno dall’altro, si dedicarono a questo principio di funzionamento, tra cui Edwin Armstrong negli Stati Uniti, Lucien Lévy in Francia e Walter Schottky in Germania.

Il termine *eterodina* o *supereterodina* è una neoformazione lessicale. Deriva dal latino *super* («sopra») e dalle parole greche *hetero* («diverso») e *dynamis* («forza» o «effetto»). Il nome descrive il principio di funzionamento fondamentale del ricevitore supereterodina: la miscelazione di due segnali di frequenza diversa per generare una nuova frequenza.
</indepth>