Nel capitolo dedicato ai circuiti di base abbiamo già incontrato vari amplificatori a transistor. Nel trasmettitore ci occupiamo ora in particolare degli *amplificatori di potenza*. Essi amplificano il segnale RF generato negli stadi precedenti fino a raggiungere la potenza d’uscita desiderata del trasmettitore.

Negli amplificatori di potenza RF si possono distinguere fondamentalmente due tipologie:

1. Gli *amplificatori RF a larga banda* presentano un guadagno il più possibile uniforme su un ampio intervallo di frequenza, ad esempio su gran parte della banda delle onde corte da $\qtyrange{1}{30}{\mega\hertz}$, cfr. figura [ref:a_breitbandverstärker].
2. Gli *amplificatori RF selettivi* sono invece sintonizzati su un intervallo di frequenza relativamente ristretto, ad esempio su una singola banda radioamatoriale, cfr. figura [ref:a_selektiver_verstaerker].

Gli amplificatori RF a larga banda si riconoscono spesso per la presenza di trasformatori di accoppiamento a larga banda tra i vari stadi amplificatori. Questi, insieme ai condensatori, non formano circuiti oscillanti sintonizzati su una frequenza specifica. Anche il noto principio dell’amplificatore in controfase (Gegentakt) si ritrova in molti amplificatori di potenza RF.

<margin>
[picture:491:a_breitbandverstärker:Amplificatore di potenza RF a larga banda con circuito in controfase]
</margin>

[question:AF412]


Gli amplificatori RF selettivi, invece, si caratterizzano tipicamente per la loro progettazione selettiva in frequenza, ottenuta mediante circuiti oscillanti in serie o in parallelo nel percorso del segnale RF.

<margin>
[picture:778:a_selektiver_verstaerker:Amplificatore di potenza RF selettivo con progettazione selettiva in frequenza]
</margin>

[question:AF408]


---


Gli amplificatori delle tipologie sopra descritte possono essere realizzati anche con più stadi collegati in cascata.

[question:AF413]


Tra gli stadi amplificatori di un amplificatore di potenza e tra ingresso e uscita è necessario effettuare un adattamento dell’impedenza. Questo è necessario affinché l’impedenza di uscita RF di uno stadio venga adattata nel modo migliore all’impedenza di ingresso RF dello stadio successivo per massimizzare il guadagno, minimizzare le distorsioni e ottimizzare il rendimento (evitando riflessioni e non linearità).


L’adattamento dell’impedenza può essere realizzato in modo a larga banda mediante un trasformatore con un opportuno rapporto di trasformazione oppure in modo selettivo in frequenza mediante un circuito oscillante con presa intermedia.


Nel caso dell’adattamento selettivo in frequenza, esistono due metodi fondamentali per realizzarlo:
- mediante un partitore di tensione induttivo (bobina con presa intermedia e condensatore in parallelo)
- mediante un partitore di tensione capacitivo (due condensatori in serie con una bobina in parallelo)

Queste bobine e questi condensatori possono essere disposti in diverse configurazioni (circuito in parallelo o in serie) per ottenere la trasformazione d’impedenza desiderata e, eventualmente, sopprimere armoniche indesiderate (filtro a π).


[question:AF409]
[question:AF410]
[question:AF414]
[question:AF407]
[question:AF406]


---


La figura [ref:a_fet_verstaerker] mostra un amplificatore per onde corte con transistor a effetto di campo LDMOS. LDMOS sta per *Laterally Diffused Metal-Oxide-Semiconductor* e indica un particolare transistor a effetto di campo per amplificatori di potenza RF. Il circuito amplificatore vero e proprio (parte superiore) è molto semplice: si tratta di nuovo di un amplificatore in controfase con due FET che lavorano in configurazione push-pull. I due transistor sono pilotati tramite un trasformatore d’ingresso comune. L’uscita dell’amplificatore viene prelevata tramite un ulteriore trasformatore. La parte inferiore del circuito, invece, è meno complessa di quanto possa sembrare: in sostanza, qui viene generata tramite un partitore di tensione la tensione di BIAS per i transistor.

Non bisogna lasciarsi ingannare dalla nota proprietà di un transistor a effetto di campo: in corrente continua il gate è praticamente privo di corrente e presenta quindi un’impedenza d’ingresso molto elevata. Alle alte frequenze, tuttavia, le capacità parassite del transistor giocano un ruolo importante, in particolare le capacità tra gate e source e tra gate e drain. La loro reattanza capacitiva diminuisce all’aumentare della frequenza, consentendo il passaggio di una corrente RF al gate. Nei transistor di potenza RF, l’impedenza d’ingresso può quindi essere notevolmente inferiore a quanto ci si aspetterebbe dalla considerazione in corrente continua di un FET. Il trasformatore d’ingresso $T_1$ serve quindi per adattare i $\qty{50}{\ohm}$ all’impedenza d’ingresso, più bassa, dei transistor.

<margin>
[picture:786:a_fet_verstaerker:Amplificatore per onde corte con transistor a effetto di campo]
</margin>

[question:AF417]


---


Come già accennato in precedenza, gli elementi attivi di un amplificatore di potenza necessitano, oltre alla tensione di servizio richiesta, anche di una polarizzazione in corrente continua del punto di funzionamento (BIAS). Questo punto di funzionamento viene solitamente generato tramite partitori di tensione che, partendo da una tensione ausiliaria stabilizzata e utilizzando trimmer per una regolazione ottimale, forniscono la tensione BIAS desiderata agli elementi del circuito.

<tip>
Nel considerare la tensione BIAS e i suoi effetti sugli elementi del circuito, il circuito va analizzato solo in corrente continua. In questa analisi, i condensatori vengono ignorati in quanto elementi che trasmettono solo tensioni alternate. Gli avvolgimenti dei trasformatori e le bobine, invece, vengono considerati come cortocircuiti. In linea generale, per questi compiti è sufficiente applicare le nozioni di base acquisite nei corsi N ed E relative alla legge di Ohm e ai partitori di tensione!
</tip>

[question:AF420]


---


Il calcolo della tensione BIAS in un circuito dato nella domanda successiva si effettua applicando la legge di Ohm tenendo conto di resistenze in serie e in parallelo. È importante considerare che i terminali di gate dei transistor rappresentano capacità e, quindi, in un’analisi in corrente continua possono essere trascurati.

[question:AF421]


<indepth>
La resistenza $R_5=\qty{51}{\ohm}$ non influisce praticamente sulla tensione continua al gate, poiché nel gate del transistor LDMOS non scorre quasi nessuna corrente continua. Per il segnale RF, invece, $R_5$ è importante: insieme alla capacità di gate attenua possibili oscillazioni ad alta frequenza e migliora così la stabilità dell’amplificatore.

La resistenza $R_4=\qty{6,8}{\kilo\ohm}$ garantisce che il gate, anche in caso di interruzione della polarizzazione, abbia un potenziale definito rispetto a massa. Inoltre, scarica la capacità di gate evitando che il transistor diventi conduttivo in modo incontrollato a causa di un gate flottante, ad esempio in caso di guasto del potenziometro $R_3$. Poiché $R_4$ è in parallelo al ramo inferiore del partitore di tensione, deve essere considerato nel calcolo preciso della tensione di gate.
</indepth>

---


Il circuito nella figura [ref:a_fet_verstaerker_vhf] mostra un amplificatore di potenza VHF con transistor a effetto di campo. Anche in questo caso i due transistor lavorano come stadio finale in controfase, che rappresenta la parte più semplice del circuito. Le brevi linee coassiali servono come parte della rete di adattamento per trasformare la bassa impedenza dei transistor LDMOS in un’impedenza adatta al resto del circuito. Il resto del circuito è nuovamente dedicato alla generazione della tensione BIAS per i transistor, inclusa una compensazione della temperatura. I potenziometri $R_1$ e $R_2$ formano ciascuno un partitore di tensione che regola la tensione BIAS per il rispettivo transistor.

[question:AF424]
[question:AF423]


<margin>
[picture:783:a_fet_verstaerker_vhf:Amplificatore VHF con transistor a effetto di campo]
</margin>


---


Un filtro a π (cfr. figura [ref:a_pi_filter]) può adattare le impedenze all’ingresso e all’uscita mediante il rapporto tra le due capacità. La bobina del filtro a π, insieme alle due capacità, definisce la frequenza di progetto del filtro. Il filtro a π sopprime, grazie alle sue caratteristiche di filtro passa-basso, le armoniche indesiderate del segnale del trasmettitore.

<margin>
[picture:1100:a_pi_filter:Filtro a π]
</margin>

[question:AF405]


Una funzione simile è svolta da un circuito LC posto a valle di un amplificatore di potenza RF. Anche questo serve per l’adattamento dell’impedenza e la soppressione simultanea di armoniche.

[question:AF404]


Negli amplificatori di potenza è importante disaccoppiare nel modo migliore gli stadi tra loro in alta frequenza per evitare retroazioni tra gli stadi (tendenza all’oscillazione, effetti di modulazione, ecc.). A questo scopo, le linee di alimentazione in tensione di servizio degli stadi vengono disaccoppiate tra loro mediante induttanze in serie e condensatori di disaccoppiamento verso massa. Questa disposizione forma un filtro passa-basso, poiché in condizioni ideali lascia passare solo la tensione continua di servizio, mentre blocca le componenti ad alta frequenza.

[question:AF411]
[question:AF419]
[question:AF418]
[question:AF422]


Le proprietà RF dei condensatori reali sono dipendenti dalla frequenza. Grandi capacità, come i condensatori elettrolitici, possono essere utilizzati solo a basse frequenze e sono efficaci solo in modo limitato nella banda RF. Per bloccare anche frequenze più elevate, si utilizzano spesso combinazioni di diversi tipi e valori di condensatori che, insieme, possono bloccare un intervallo di frequenza più ampio.

[question:AF415]