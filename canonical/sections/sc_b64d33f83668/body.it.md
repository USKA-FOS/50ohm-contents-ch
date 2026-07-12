Una stazione radio ripetitrice permette una maggiore portata rispetto a quanto spesso sia possibile con una connessione diretta tra due stazioni radioamatoriali. Le stazioni radio ripetitrici sono solitamente installate in posizioni esposte, ad esempio sulle cime delle montagne, in grattacieli, su campanili e altre torri. Esistono anche stazioni radio ripetitrici sui satelliti che orbitano attorno alla Terra. La struttura e la funzione di una tale stazione radio sono mostrate nella figura [ref:n_relaisfunkstellen_aufbau]. 

[picture:648:n_relaisfunkstellen_aufbau:Rappresentazione schematica di una stazione radio ripetitrice con utenti]

Se, ad esempio, c'è una montagna tra due stazioni radio, è impossibile trasmettere attraverso la montagna. Una stazione radio ripetitrice sulla cima della montagna consente comunque di stabilire un collegamento, poiché entrambe le stazioni possono raggiungere direttamente il ripetitore.

Le stazioni radio ripetitrici sono anche chiamate brevemente ripetitori. Si possono riconoscere dal fatto che trasmettono regolarmente il loro nominativo. Il nominativo di una stazione radio ripetitrice inizia, secondo il [piano dei nominativi](https://50ohm.de/rzp), di solito con DB0, DM0 o DO0.

La definizione ufficiale di ripetitori suona un po' più arida: *"Stazione radio ripetitrice": una stazione radioamatoriale telecomandata (anche su satelliti), che ritrasmette le trasmissioni radioamatoriali ricevute, parti di esse o altri segnali immessi o memorizzati, attivati da remoto e che serve ad aumentare la raggiungibilità delle stazioni radioamatoriali.*

La seguente domanda su questa definizione può essere risolta bene per esclusione, se si sa quanto segue:
* Le stazioni radio ripetitrici non sono gestite con nominativi personali.
* Le stazioni radio ripetitrici di solito non sono presidiate permanentemente.
* Le stazioni radio ripetitrici non devono necessariamente essere gestite in posizioni geograficamente esposte.

[question:VN007]

[question:VD118]

---

Una stazione radio ripetitrice riceve il segnale di una stazione radioamatoriale sulla sua frequenza di ingresso e lo trasmette contemporaneamente sulla sua frequenza di uscita. Affinché il trasmettitore della stazione radio ripetitrice non disturbi il proprio ricevitore, la frequenza di trasmissione e quella di ricezione sono generalmente diverse. La distanza tra la frequenza di trasmissione e quella di ricezione è chiamata spostamento di frequenza o semplicemente spostamento. Gli spostamenti comunemente usati in Germania si trovano nella tabella [ref:n_relaisfunkstellen_ablage].

<margin>
| r: Banda | X: Spostamento |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Spostamento di frequenza]
</margin>

Ad esempio, la frequenza di un ripetitore da $\qty{70}{\centi\meter}$ è indicata come:
* Frequenza di ingresso: $\qty{431,275}{\mega\hertz}$
* Spostamento: $\qty{+7,600}{\mega\hertz}$
* Frequenza di uscita: $\qty{438,875}{\mega\hertz}$

[question:BE401]
[question:BE402]
[question:BE403]

<indepth>
Alcune stazioni radio ripetitrici operano anche nel cosiddetto *funzionamento crossband*. Ciò significa che una stazione trasmette e riceve su una banda (ad esempio, $\qty{70}{\centi\meter}$), un'altra stazione sullo stesso ripetitore, ma su una banda diversa (ad esempio, $\qty{2}{\meter}$). Il controllo del ripetitore media le conversazioni tra le due bande. È anche possibile una conversione del modo di trasmissione, ad esempio da SSB a FM.
</indepth>

Una stazione ripetitrice che trasmette dati invece di voce è chiamata digipeater. Un digipeater è in grado di ricevere e ritrasmettere pacchetti di dati. La particolarità è che la trasmissione può avvenire solo in parte o con ritardo temporale. Allo stesso modo, i pacchetti di dati possono essere ripetuti o singoli campi di dati modificati.

[question:NF118]

---

Prima di poter iniziare le operazioni radio tramite una stazione radio ripetitrice, è necessario conoscerne le particolarità tecniche e i parametri. Per alcuni ripetitori, oltre alla frequenza, sono necessarie ulteriori regolazioni sul tuo trasmettitore-ricevitore per garantire un funzionamento privo di disturbi. Oltre all'FM analogico (modulazione di frequenza), vengono utilizzati anche metodi digitali, come DMR e D-Star, come metodi di trasmissione vocale.

<tip>
Informazioni sulle stazioni radio ripetitrici, sui parametri tecnici e sulle particolarità si possono ottenere dalla sezione DARC più vicina, dalla persona responsabile del ripetitore o da Internet.
</tip>

[question:NE309]
[question:NE308]

Una regolazione importante è la larghezza di banda del canale in modalità FM. Ricordiamo: la larghezza di banda indica quanto "spazio" si occupa nello spettro di frequenza con la trasmissione. Da un lato c'è l'FM larga (Wide-FM), la cui larghezza di banda è di $\qty{25}{\kilo\hertz}$ e viene visualizzata sul display, ad esempio, come *FM-W*. Dall'altro c'è l'FM stretta (Narrow-FM), che occupa una larghezza di banda di soli $\qty{12,5}{\kilo\hertz}$ e viene visualizzata sull'apparecchio radio, ad esempio, come *FM-N*. Molti ripetitori non gradiscono segnali troppo ampi. Ciò può causare segnali distorti e disturbare le frequenze dei ripetitori adiacenti.

[question:BE407]
[question:BE417]

Il funzionamento radio tramite stazioni radioamatoriali telecomandate è generalmente consentito a tutti i radioamatori con un nominativo assegnato. Per garantire un funzionamento privo di disturbi, l'operatore può tuttavia escludere altri radioamatori dall'uso della stazione radioamatoriale. La BNetzA deve essere informata di ciò.

[question:VD504]

Quando si opera tramite stazioni radio ripetitrici, le trasmissioni dovrebbero essere mantenute il più brevi possibile, in modo che le stazioni mobili e portatili possano utilizzare più facilmente il ripetitore, soprattutto se si trovano nell'area di ricezione solo per breve tempo. Tra una trasmissione e l'altra si dovrebbe fare una pausa per dare ad altre stazioni la possibilità di farsi sentire.

[question:BE406]
[question:BE404]

In caso di immissione vocale simultanea di due stazioni diverse, la trasmissione del ripetitore viene disturbata fino a diventare illeggibile. Per evitare questo cosiddetto raddoppio, dovrebbe sempre esserci un passaggio corretto tra gli utenti del ripetitore. Ciò significa anche iniziare a trasmettere solo dopo che la stazione precedente ha terminato la sua trasmissione.

[question:NE310]
[question:BE405]

Nell'Allegato 1 della AFuV, già discusso, si trovano anche le disposizioni relative alla potenza di trasmissione delle stazioni ripetitrici. Al di sopra dei 30 MHz, una stazione che opera automaticamente può essere utilizzata con un massimo di 50 W ERP.

[question:VD503]

Una particolarità si presenta nella valutazione di un collegamento radio tramite una stazione radio ripetitrice. Poiché la potenza del segnale con cui si riceve il corrispondente radio è la potenza del segnale della stazione ripetitrice e non la potenza del segnale del corrispondente radio, si rinuncia alla sua indicazione. Nel rapporto viene valutata solo la leggibilità (R).

[question:BE408]
