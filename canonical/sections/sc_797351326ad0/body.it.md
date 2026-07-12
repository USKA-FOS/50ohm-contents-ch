Come ricevitore più semplice, abbiamo conosciuto il ricevitore a rilevatore nel capitolo precedente. Il ricevitore a rilevatore è un cosiddetto ricevitore diretto, che abbiamo già conosciuto nella classe N. Nel ricevitore diretto, come mostrato nella figura [ref:e_geradeausempfänger], il segnale, dopo la ricezione ed eventuale amplificazione, viene solo demodulato. Questo concetto di ricevitore ha tuttavia lo svantaggio di una scarsa selettività (poder). Per migliorare ciò, si potrebbe combinare il blocco del filtro di ingresso (2) con più filtri per aumentare la selettività. Ma in tal caso, ogni volta che si cambia la frequenza di ricezione, tutti questi filtri dovrebbero essere adattati, il che è molto laborioso. Per questo motivo è stato sviluppato il *ricevitore supereterodina* (cfr. figura [ref:ueberlagerungsempfaenger_einfachsuper]), chiamato anche nel gergo tecnico *Superheterodyn* o *Superhet*.

<margin>
[picture:736:e_geradeausempfänger:Geradeausempfänger]
</margin>

<margin>
[picture:803:ueberlagerungsempfaenger_einfachsuper:Überlagerungsempfänger mit Verstärkern]
</margin>

---

L'idea del ricevitore supereterodina è tanto semplice quanto geniale. Invece di filtri accordabili, viene utilizzato un oscillatore variabile (VFO) con il quale il segnale ricevuto viene prima convertito in una frequenza fissa, la cosiddetta frequenza intermedia $f_z$ (spesso chiamata anche ZF). Per questa frequenza intermedia fissa è possibile realizzare filtri molto selettivi e di alta qualità. La figura [ref:ueberlagerungsempfaenger_einfachsuper_filter] illustra questo principio.

<margin>
[picture:913:ueberlagerungsempfaenger_einfachsuper_filter:Überlagerungsempfänger mit Filtern]
</margin>

Il filtro di ingresso lascia passare inizialmente solo la banda di frequenza desiderata, ad esempio la banda delle onde corte. Successivamente, un mixer converte il segnale di ingresso insieme alla frequenza del VFO nella frequenza intermedia costante, ad esempio a $\qty{455}{\kilo\hertz}$. Nell'esempio concreto, il VFO può essere impostato tra $\qty{3,455}{\mega\hertz}$ e $\qty{30,455}{\mega\hertz}$ per poter miscelare l'intera banda delle onde corte verso il basso. Il vantaggio decisivo del ricevitore supereterodina rispetto al ricevitore diretto risiede proprio in questa frequenza intermedia costante: la filtratura del segnale può essere ottimizzata per una frequenza fissa, raggiungendo così una selettività molto elevata, ovvero potere.

---

Poiché i filtri non devono essere accordabili, possono essere ottimizzati in modo mirato per quanto riguarda la larghezza di banda e la pendenza dei fianchi, ad esempio utilizzando filtri al quarzo, ceramici o digitali. In questo modo è possibile utilizzare, ad esempio, filtri con una larghezza di banda di circa $\qty{2,4}{\kilo\hertz}$ per la trasmissione vocale (SSB) e filtri a banda stretta di circa $\qty{300}{\hertz}$ per la telegrafia (CW). È inoltre possibile utilizzare filtri adattati per altre modalità di trasmissione come AM, FM o modalità digitali.

Grazie a questo concetto, il ricevitore supereterodina raggiunge un potere molto più elevato rispetto al ricevitore diretto. Un altro vantaggio è che tutti i gruppi successivi lavorano sempre con la stessa frequenza intermedia e quindi non devono essere eseguiti accordabili, il che semplifica la struttura e migliora la qualità di ricezione.

[question:EF102]

I ricevitori supereterodina possono funzionare con una o più frequenze intermedie. Nel caso più semplice, si tratta di un ricevitore a sovraeterodina diretta, in cui la frequenza intermedia è la frequenza audio desiderata. A tal fine, la frequenza dell'oscillatore deve essere molto vicina alla frequenza di ricezione.

[question:EF208]

Un ricevitore supereterodina ha tuttavia anche alcuni svantaggi, in particolare l'insorgenza delle cosiddette frequenze immagine. Affronteremo questa problematica e concetti di ricevitore avanzati come il supereterodina multiplo con più frequenze intermedie più in dettaglio solo nella classe A.

<indepth>
L'inventore del ricevitore supereterodina non può essere identificato in modo univoco. Ciò è dovuto, tra l'altro, al fatto che il suo sviluppo risale al periodo della Prima Guerra Mondiale, durante il quale tutte le parti belligeranti coinvolte lavorarono intensamente al miglioramento della tecnologia radio e radiotrasmittente. Indipendentemente l'uno dall'altro, diversi ricercatori lavorarono intorno al 1918 su questo principio di funzionamento, tra cui Edwin Armstrong negli USA, Lucien Lévy in Francia e Walter Schottky in Germania.
  
Il termine Heterodyn o Superheterodyn è una nuova parola. È composto dal latino super ("sopra") e dalle parole greche hetero ("diverso") e dynamis ("forza" o "effetto"). Il nome descrive il principio di funzionamento fondamentale del ricevitore supereterodina: la miscelazione di due segnali di frequenza diversa per generare una nuova frequenza.
</indepth>