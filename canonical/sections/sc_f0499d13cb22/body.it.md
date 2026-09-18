Anche la visualizzazione della frequenza di un ricevitore può essere verificata. A differenza di un trasmettitore, la frequenza di ricezione impostata normalmente non può essere misurata semplicemente all’uscita dell’apparecchio radio con un frequenzimetro. Il segnale RF ricevuto viene già elaborato precocemente nel ricevitore e, ad esempio, convertito su una frequenza intermedia.

Per verificare la visualizzazione della frequenza si utilizza quindi un segnale di riferimento il più possibile preciso. A tale scopo, un generatore di frequenza o un oscillatore di riferimento preciso con frequenza nota viene collegato all’ingresso antenna del ricevitore. Successivamente, il ricevitore viene sintonizzato su questo segnale e la sua visualizzazione della frequenza viene confrontata con la frequenza nota del segnale di riferimento.

Più precisa è la frequenza di riferimento utilizzata, più accurata può essere la verifica o la calibrazione della visualizzazione della frequenza del ricevitore. Particolarmente adatti sono, ad esempio, oscillatori sincronizzati GPS o oscillatori al quarzo ad alta stabilità termica (OCXO).

<attention>
Un generatore di frequenza collegato direttamente può danneggiare facilmente l’ingresso del ricevitore. In caso di dubbio, la misurazione dovrebbe iniziare con la tensione più bassa del generatore e con un attenuatore.
</attention>

[question:AI511]
[question:AI504]

---

Nei trasmettitori, la misurazione della frequenza è più semplice. Un frequenzimetro viene collegato tramite un attenuatore alla presa dell’antenna. Naturalmente, questa misurazione ha senso solo con una portante non modulata, cioè un segnale sinusoidale il più possibile puro.

<indepth>
I trasmettitori SSB non generano alcun segnale senza modulazione. Per misurare la loro frequenza di trasmissione, è possibile iniettare un segnale audio di frequenza nota nella presa del microfono. Dal valore misurato del frequenzimetro all’uscita del trasmettitore, per USB si sottrae la frequenza audio per ottenere la frequenza della portante non trasmessa. Per LSB, invece, la si somma.
</indepth>

[question:AI502]
[question:AI501]

Una frequenza può anche essere determinata con un oscilloscopio. Tuttavia, per misurazioni precise della frequenza, un oscilloscopio è generalmente meno adatto di un frequenzimetro dedicato, poiché la sua base dei tempi e la procedura di misurazione sono specificamente progettate per un’elevata precisione e risoluzione della frequenza.

[question:AI503]

---

I frequenzimetri semplici spesso funzionano con un cosiddetto *tempo di porta*. Durante questo periodo, l’apparecchio conta i periodi, i fronti o i passaggi per lo zero del segnale di ingresso. Successivamente, la frequenza viene calcolata in base al numero di oscillazioni contate e al tempo di porta noto. Esempio: con un tempo di porta di un secondo, la determinazione della frequenza è particolarmente semplice: se, ad esempio, vengono contati $\num{1000}$ periodi, la frequenza misurata è $\qty{1000}{\hertz}$.

<margin>
[picture:1126:a_frequenzmessung_torzeit:Conteggio di un segnale con una frequenza di $\qty{1,1}{\kilo\hertz}$ con tempi di porta molto brevi]
</margin>

La *risoluzione della frequenza* $\Delta f$ indica quanto piccolo può essere la differenza di frequenza tra due valori misurati che il frequenzimetro può ancora distinguere o visualizzare. In un frequenzimetro che conta direttamente in modo semplice, la risoluzione della frequenza è determinata dal tempo di porta $T_\mathrm{G}$:

$\Delta f = \frac{1}{T_\mathrm{G}}$

L’effetto del tempo di porta, ovvero della risoluzione della frequenza, sul risultato della misurazione è illustrato nella figura [ref:a_frequenzmessung_torzeit]. In entrambi i casi viene misurato lo stesso segnale con una frequenza reale di $\qty{1,1}{\kilo\hertz}$.

Con un tempo di porta di soli $\qty{1}{\milli\second}$, viene contato solo un periodo. Il frequenzimetro calcola da questo un valore misurato di $\qty{1}{\kilo\hertz}$. Il breve tempo di porta consente qui una risoluzione della frequenza di $\qty{1}{\kilo\hertz}$.

Se il tempo di porta viene esteso a $\qty{10}{\milli\second}$, possono essere contati già $\num{11}$ periodi. Da questo risulta un valore misurato di $\qty{1,1}{\kilo\hertz}$. La risoluzione della frequenza è ora di $\qty{100}{\hertz}$, consentendo di visualizzare anche la cifra aggiuntiva della frequenza.

Più lungo è il tempo di porta, più periodi vengono contati e più fine è la risoluzione della frequenza. Un tempo di porta breve, invece, ha il vantaggio di poter aggiornare la visualizzazione più frequentemente. La scelta del tempo di porta comporta quindi un compromesso tra aggiornamento rapido e alta risoluzione della frequenza. La precisione della misurazione della frequenza è da distinguere dalla risoluzione. Essa dipende in particolare dalla precisione della base dei tempi del frequenzimetro.

[question:AI505]