Durante il funzionamento dei trasmettitori – specialmente di quelli ad alta potenza – possono verificarsi varie interferenze su dispositivi e impianti elettronici. Abbiamo già conosciuto queste *interferenze disturbanti* e alcune indicazioni di base nel capitolo [sec:stoerungen_vermeiden]. L'obiettivo è evitare il più possibile queste interferenze o eliminarne le cause attraverso appropriate contromisure. In questa lezione vogliamo esaminare più da vicino cause e contromisure. In linea di principio, i dispositivi elettronici possono essere influenzati in due modi:

- *Irraggiamento* si verifica quando l'alta frequenza raggiunge direttamente l'elettronica di un dispositivo tramite l'antenna ricevente (figura [ref:e_antenne_einstrahlung]) o a causa di un alloggiamento insufficientemente schermato (figura [ref:e_direkteinstrahlung]), causando interferenze.
- *Correnti entranti* si verificano quando l'alta frequenza entra in un dispositivo tramite conduttori o cavi, come ad esempio il cavo di alimentazione, il cavo dell'antenna, i cavi degli altoparlanti, ecc. (figura [ref:e_einstroemung])

<margin>
[picture:744:e_antenne_einstrahlung:Irraggiamento tramite l'antenna ricevente]
[picture:746:e_direkteinstrahlung:Irraggiamento diretto in un dispositivo]
[picture:747:e_einstroemung:Afflusso tramite cavi di collegamento]
</margin>

<indepth>
Si distingue tra:
  
- *Disturbi condotti* – vengono trasmessi tramite conduttori elettrici (ad es. cavi di alimentazione, di segnale o dati).
  
- *Disturbi irradiati (o a campo)* – si propagano come onde elettromagnetiche attraverso lo spazio libero.
  
</indepth>

[question:EJ102]
[question:EJ101]

Anche durante l'operazione conforme alla legge di un trasmettitore, possono verificarsi interferenze nella ricezione di altre frequenze su ricevitori nelle immediate vicinanze. A causa delle elevate potenze di trasmissione delle stazioni radioamatoriali e dell'uso di antenne ad alto guadagno, possono verificarsi intensità di campo molto elevate localmente e nell'area di radiazione delle antenne. Queste possono sovraeccitare i ricevitori e i loro stadi di ricezione, il che può portare a una riduzione della sensibilità del ricevitore fino al blocco completo della ricezione. Ciò può ad esempio causare il malfunzionamento dei comandi dei cancelli del garage. Spesso anche le luci a LED, controllate da sensori capacitivi, vengono influenzate dalle emissioni. In questo caso si parla di *sovraeccitazione* o *interferenza disturbante* dei dispositivi.

[question:EJ106]
[question:EJ107]
[question:EJ103]
[question:EJ112]

Spesso le interferenze disturbanti nel vicinato vengono associate all'operazione di una stazione radioamatoriale. Per dimostrare un eventuale collegamento con le emissioni della stazione radioamatoriale, è molto utile la valutazione e, se necessario, la tenuta di un registro delle emissioni e delle connessioni effettuate. In questo modo si può anche eventualmente escludere che le presunte interferenze nel vicinato siano attribuibili alla stazione radioamatoriale.

[question:EJ122]

Il radioamatore dovrebbe supportare il vicinato in modo cooperativo e orientato alla soluzione, nonché presentare proposte per un rimedio. Spesso i problemi possono essere risolti più facilmente con una conversazione diretta piuttosto che coinvolgendo le autorità. Solo dopo che tutti gli sforzi sono falliti, si può chiedere all'UFCOM di verificare la situazione. Tuttavia, questo dovrebbe essere veramente l'ultima risorsa per risolvere il problema.

[question:EJ124]
[question:VN004]

A questi sforzi appartengono varie misure, come ad esempio:

%- Riduzione della potenza di trasmissione dell'impianto radioamatoriale % Questa dovrebbe essere l'ultima risorsa!
- Schermatura di dispositivi o cavi sensibili
- Installazione di filtri e induttanze di modo comune sul lato ricevente del vicino
- Realizzazione di una messa a terra HF efficace
- Utilizzo di antenne esterne per la ricezione

Queste misure le vogliamo esaminare più da vicino di seguito.

Per evitare interferenze disturbanti sui dispositivi, un radioamatore dovrebbe sempre utilizzare solo la *potenza di trasmissione necessaria per una comunicazione soddisfacente* per le sue emissioni.

[question:EJ104]
[question:EJ105]

Se in un impianto di ricezione sono presenti contemporaneamente più segnali di ricezione forti (ad esempio a causa della ricezione di un trasmettitore locale di un altro servizio radio e di una forte stazione radioamatoriale nelle vicinanze), nel ricevitore possono generarsi armoniche indesiderate e i loro prodotti di miscelazione a causa della sovraeccitazione degli stadi di ricezione del ricevitore. Questo si chiama *intermodulazione*. L'intermodulazione genera *segnali fantasma* che si verificano solo in presenza dei segnali coinvolti.

[question:EJ120]

Anche in un impianto stereo spento, forti segnali HF possono, attraverso la rettifica nello stadio finale BF su componenti non lineari come transistor, portare a rumori udibili negli altoparlanti. Anche i contatti corrosi tra metalli (ossidi metallici) hanno la proprietà di poter formare effetti di rettifica a causa di non linearità. In questo modo, durante le emissioni della stazione radioamatoriale, possono generarsi prodotti di miscelazione indesiderati sul lato di trasmissione o di ricezione, che possono portare a un'interferenza disturbante nella ricezione televisiva e radiofonica.

[question:EJ113]
[question:EJ121]


Non tutte le interferenze disturbanti possono essere risolte con misure sul lato trasmittente. Spesso anche il dispositivo influenzato stesso non è adatto per la rispettiva ubicazione, non soddisfa i requisiti legali vigenti o i cavi di alimentazione e le schermature non sono dimensionati sufficientemente contro irraggiamenti o correnti entranti ad alta frequenza. In tali casi, è opportuno suggerire ai soggetti interessati delle misure in modo che i problemi possano essere risolti.

Una possibile misura consiste nello schermare i moduli HF il più possibile con un alloggiamento metallico chiuso.

[question:EJ108]

Se un'antenna trasmittente in onde corte si trova vicino e parallela a una linea di corrente alternata da $\qty{230}{\volt}$, correnti ad alta frequenza possono essere accoppiate nella rete elettrica. Per mantenere le interferenze nella propria casa il più basse possibile, si consiglia di utilizzare per le antenne trasmittenti una linea di terra HF separata.

[question:EJ109]
[question:EJ111]

Un'altra possibilità è l'*installazione di filtri nei cavi di alimentazione dei dispositivi* nonché *induttanze di modo comune (soppressione delle correnti sulla calza)* dei cavi di alimentazione.

In particolare, i filtri possono essere installati sul lato del dispositivo influenzato (TV, ricevitore DVB-T2, ricevitore DAB, ecc.) nel percorso di ricezione. Ad esempio, l'intensità di campo di un trasmettitore radioamatoriale in onde corte (ad esempio nell'intervallo di $\qtyrange{3}{30}{\mega\hertz}$) può influenzare la ricezione TV (ad esempio $\qtyrange{470}{690}{\mega\hertz}$). Installando un filtro passa-alto, l'influenza del segnale del trasmettitore radioamatoriale può essere significativamente ridotta: le componenti di frequenza al di fuori dell'intervallo di ricezione TV – in questo esempio quindi le onde corte – vengono soppresse, in modo che gli stadi di ricezione del dispositivo non possano più essere sovraeccitati.

[question:EJ116]
[question:EJ117]

Spesso il segnale di trasmissione di una stazione radioamatoriale nelle immediate vicinanze di altri dispositivi viene accoppiato in ricevitori o dispositivi disturbati tramite la calza di cavi coassiali o cavi di alimentazione. Se qui si verificano interferenze, dovrebbe essere installata una cosiddetta *induttanza di modo comune* sui cavi di alimentazione del dispositivo influenzato. Un'induttanza di modo comune blocca le *correnti di modo comune* sulla calza e sul conduttore interno del dispositivo influenzato. Come induttanze di modo comune vengono tipicamente utilizzati nuclei toroidali o nuclei a clip in ferrite. Un'altra possibilità per evitare interferenze nei cavi di controllo di impianti e dispositivi elettrici è l'uso di cavi di controllo schermati (ad esempio negli impianti citofonici, linee telefoniche, ecc.)

[question:EJ118]
[question:EJ119]
[question:EJ115]
[question:EJ114]

%Anche condizioni di ricezione scadenti sul lato del dispositivo influenzato (ad es. antenna da interno TV per la ricezione) possono portare più facilmente a interferenze nella %ricezione. Una possibile contromisura sarebbe l'uso di un'antenna esterna eventualmente con pre-filtri appropriati.

%[question:EJ123]
