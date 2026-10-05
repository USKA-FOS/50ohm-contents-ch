Nel capitolo sui circuiti fondamentali abbiamo già conosciuto diversi amplificatori a transistor. Nel trasmettitore consideriamo ora in particolare gli *amplificatori di potenza*. Essi amplificano il segnale RF generato negli stadi precedenti fino alla potenza d’uscita desiderata del trasmettitore.

Per gli amplificatori di potenza HF si possono fondamentalmente distinguere due tipologie:

1. Gli *amplificatori RF a banda larga* presentano un guadagno il più possibile uniforme su un intervallo di frequenza relativamente ampio, ad esempio su gran parte della gamma delle onde corte da $\qtyrange{1}{30}{\mega\hertz}$, cfr. figura [ref:a_breitbandverstärker].
2. Gli *amplificatori RF selettivi* sono invece sintonizzati su un intervallo di frequenza relativamente stretto, ad esempio su una singola banda radioamatoriale, cfr. figura [ref:a_selektiver_verstaerker].

Gli amplificatori RF a banda larga sono spesso riconoscibili per la presenza di trasformatori di accoppiamento a banda larga tra i singoli stadi amplificatori. Questi, insieme ai condensatori, non formano circuiti oscillanti sintonizzati su una frequenza specifica. Anche il principio già noto dell'amplificatore push-pull si ritrova in molti amplificatori di potenza HF.

<margin>
[picture:491:a_breitbandverstärker:Amplificatore di potenza HF a banda larga con circuito push-pull]
</margin>

[question:AF412]

Gli amplificatori RF selettivi, invece, sono tipicamente riconoscibili per la loro progettazione selettiva in frequenza, caratterizzata da circuiti oscillanti in serie o in parallelo nel percorso del segnale RF.

<margin>
[picture:778:a_selektiver_verstaerker:Amplificatore di potenza HF selettivo con progettazione selettiva in frequenza]
</margin>

[question:AF408]

---

Gli amplificatori dei tipi sopra menzionati possono essere realizzati anche in più stadi, concatenando singoli stadi.

[question:AF413]

Tra gli stadi amplificatori di un amplificatore di potenza e i loro ingressi e uscite è necessario effettuare un adattamento di impedenza. Ciò è necessario affinché l'impedenza di uscita RF di uno stadio precedente sia adattata nel modo migliore all'impedenza di ingresso RF dello stadio successivo, per ottenere il massimo guadagno, minime distorsioni e un rendimento ottimale (evitando riflessioni e non linearità).

L'adattamento di impedenza può essere realizzato a banda larga utilizzando un trasformatore con un rapporto di trasformazione adeguato, oppure in modo selettivo in frequenza mediante un circuito oscillante con presa intermedia.

Per l'adattamento selettivo in frequenza esistono due possibilità fondamentali:
- mediante un partitore di tensione induttivo (bobina con presa intermedia e condensatore in parallelo)
- mediante un partitore di tensione capacitivo (due condensatori in serie con bobina in parallelo)

Queste bobine e condensatori possono essere disposti in configurazioni diverse (circuito parallelo o serie) per ottenere la trasformazione di impedenza desiderata e, eventualmente, sopprimere contemporaneamente le armoniche (filtro Pi).

[question:AF409]
[question:AF410]
[question:AF414]
[question:AF407]
[question:AF406]

---

La figura [ref:a_fet_verstaerker] mostra un amplificatore per onde corte con transistor LDMOS a effetto di campo. LDMOS sta per *Laterally Diffused Metal-Oxide-Semiconductor* e indica un particolare transistor a effetto di campo per amplificatori di potenza RF. Il circuito amplificatore vero e proprio (parte superiore) è costruito in modo molto semplice. È di nuovo un amplificatore push-pull con due FET, che lavorano in configurazione push-pull. I due transistor sono pilotati da un trasformatore di ingresso comune. L'uscita dell'amplificatore viene prelevata tramite un ulteriore trasformatore. La parte inferiore del circuito è anche meno complessa di quanto si possa pensare: in sostanza, qui viene generata solo la tensione di polarizzazione (BIAS) per i transistor tramite un partitore di tensione.

Non bisogna farsi ingannare dalla nota proprietà di un transistor a effetto di campo: in tensione continua il gate è praticamente senza corrente e quindi ha un'impedenza di ingresso molto alta. Ad alte frequenze, tuttavia, le capacità parassite del transistor giocano un ruolo importante, in particolare le capacità tra gate e source e tra gate e drain. La loro reattanza capacitiva diminuisce con l'aumentare della frequenza, cosicché può scorrere una corrente RF sul gate. Nei transistor di potenza RF, l'impedenza di ingresso può quindi essere significativamente più bassa di quanto ci si aspetterebbe dall'analisi in corrente continua di un FET. Il trasformatore di ingresso $T_1$ serve quindi ad adattare i $\qty{50}{\ohm}$ alla bassa impedenza di ingresso dei transistor.

<margin>
[picture:786:a_fet_verstaerker:Amplificatore per onde corte con transistor a effetto di campo]
</margin>

[question:AF417]

---

Come accennato sopra, gli elementi attivi in un amplificatore di potenza richiedono, oltre alla tensione di servizio necessaria, anche una regolazione in tensione continua del punto di funzionamento (BIAS). Questo punto di funzionamento viene solitamente generato da partitori di tensione che, a partire da una tensione ausiliaria stabilizzata, utilizzando potenziometri di regolazione per un'impostazione ottimale, generano la tensione di polarizzazione desiderata sugli elementi.

<tip>
Quando si considera la tensione di polarizzazione e i suoi effetti sugli elementi del circuito, il circuito deve essere analizzato solo in termini di tensione continua. In questo caso, i condensatori, come elementi che possono trasmettere solo tensioni alternate, vengono ignorati. Gli avvolgimenti dei trasformatori e le bobine, nell'analisi in tensione continua, sono considerati come cortocircuiti. In linea di principio, per questi compiti è sufficiente applicare le conoscenze di base delle sezioni [sec:ohmsches_gesetz] legge di Ohm, [sec:spannungsteiler_1] e [sec:spannungsteiler_2]!
</tip>

[question:AF420]

---

Il calcolo della tensione di polarizzazione per un dato circuito nella domanda successiva avviene applicando la legge di Ohm, tenendo conto del collegamento in parallelo e in serie delle resistenze. È importante, nell'analisi della domanda, che i terminali di gate dei transistor rappresentino capacità e quindi siano trascurabili nell'analisi in tensione continua.

[question:AF421]

<indepth>
La resistenza $R_5=\qty{51}{\ohm}$ non influisce praticamente sulla tensione continua al gate, poiché nel gate del transistor LDMOS scorre quasi nessuna corrente continua. Per il segnale RF, tuttavia, $R_5$ è importante: insieme alla capacità del gate, smorza eventuali oscillazioni ad alta frequenza e migliora così la stabilità dell'amplificatore.

La resistenza $R_4=\qty{6,8}{\kilo\ohm}$ assicura che il gate abbia un potenziale definito rispetto alla massa anche in caso di interruzione della regolazione del punto di funzionamento. Scarica inoltre la capacità del gate e impedisce così che il transistor diventi conduttivo involontariamente a causa di un gate flottante, ad esempio se il potenziometro $R_3$ è difettoso. Poiché $R_4$ è in parallelo al ramo inferiore del partitore di tensione, deve essere considerato nel calcolo preciso della tensione del gate.
</indepth>

---

Il circuito in figura [ref:a_fet_verstaerker_vhf] mostra un amplificatore di potenza VHF con transistor a effetto di campo. Anche qui i due transistor lavorano come stadio finale push-pull, che è la parte semplice del circuito. I brevi cavi coassiali servono come parte della rete di adattamento per trasformare la bassa impedenza dei transistor LDMOS in un'impedenza adatta al resto del circuito. Il resto del circuito è nuovamente la generazione della tensione di polarizzazione per i transistor, inclusa una compensazione termica. I potenziometri $R_1$ e $R_2$ formano ciascuno un partitore di tensione che regola la tensione di polarizzazione per il rispettivo transistor.

[question:AF424]
[question:AF423]

<margin>
[picture:783:a_fet_verstaerker_vhf:Amplificatore VHF con transistor a effetto di campo]
</margin>


---

Un filtro Pi (cfr. figura [ref:a_pi_filter]) può adattare le impedenze al suo ingresso e uscita attraverso il rapporto delle due capacità. La bobina del filtro Pi definisce, insieme alle due capacità, la frequenza di progetto del filtro. Il filtro Pi sopprime contemporaneamente, grazie al suo carattere di filtro passa-basso, le armoniche indesiderate del segnale di trasmissione.

<margin>
[picture:1100:a_pi_filter:Filtro Pi]
</margin>

[question:AF405]

Una funzione simile ha un circuito LC dietro un amplificatore di potenza RF. Anche questo serve per l'adattamento di impedenza e la soppressione simultanea delle armoniche.

[question:AF404]

Negli amplificatori di potenza è importante disaccoppiare al meglio i singoli stadi in termini RF dalla tensione di servizio per evitare retroazioni su altri stadi (tendenza all'oscillazione, effetti di modulazione, ecc.). A questo scopo, le linee di alimentazione della tensione di servizio dei singoli stadi vengono disaccoppiate tra loro mediante induttanze collegate in serie e condensatori di disaccoppiamento verso massa. Questa disposizione costituisce un filtro passa-basso, poiché idealmente lascia passare solo la tensione di servizio CC desiderata, mentre blocca le componenti RF.

[question:AF411]
[question:AF419]
[question:AF418]
[question:AF422]

Le proprietà RF dei condensatori reali dipendono dalla frequenza. Grandi capacità come i condensatori elettrolitici possono essere utilizzate solo a basse frequenze e sono solo parzialmente efficaci nella gamma RF. Per disaccoppiare anche le frequenze più elevate mediante condensatori, si utilizza spesso una combinazione di diversi tipi di condensatori e valori di capacità, che insieme possono disaccoppiare un intervallo di frequenza più ampio.

[question:AF415]
