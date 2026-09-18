Durante il funzionamento di trasmettitori – in particolare di trasmettitori ad alta potenza – possono verificarsi varie forme di disturbi su apparecchi e impianti elettronici. Questi *disturbi indesiderati* e alcune indicazioni di base su come evitarli sono già stati trattati nel capitolo [sec:stoerungen_vermeiden]. L'obiettivo è evitare tali disturbi o eliminarne le cause mediante misure appropriate. In questa lezione esamineremo più in dettaglio le cause e le contromisure. In linea generale, i dispositivi elettronici possono essere influenzati in due modi:

- Si parla di *irradiazione* quando l'alta frequenza penetra nell'elettronica di un apparecchio tramite l'antenna di ricezione (Figura [ref:e_antenne_einstrahlung]) o direttamente attraverso un involucro non sufficientemente schermato (Figura [ref:e_direkteinstrahlung]) causando disturbi.
- Si parla di *correnti entranti* quando l'alta frequenza penetra in un apparecchio tramite cavi o conduttori, ad esempio tramite la linea di alimentazione di rete, la linea di antenna, i cavi degli altoparlanti ecc. (Figura [ref:e_einstroemung])

<margin>
[picture:744:e_antenne_einstrahlung:Irradiazione tramite antenna di ricezione]
[picture:746:e_diretteinstrahlung:Irradiazione diretta in un apparecchio]
[picture:747:e_einstroemung:Correnti entranti tramite cavi di collegamento]
</margin>

<indepth>
Si distinguono:
  
1 Disturbi condotti – trasmessi tramite linee elettriche (ad esempio linee di rete, segnale o dati).
  
2 Disturbi radiati (o a campo) – si propagano come onde elettromagnetiche nello spazio libero.
  
</indepth>

[question:EJ102]
[question:EJ101]

Anche durante il funzionamento conforme alla legge di un trasmettitore, possono verificarsi disturbi su ricevitori nelle immediate vicinanze durante la ricezione di altre frequenze. Grazie all'elevata potenza di trasmissione delle stazioni radioamatoriali e all'uso di antenne ad alto guadagno, possono verificarsi localmente e nell'area di irradiazione dell'antenna livelli di intensità di campo molto elevati. Questi possono sovraeccitare i ricevitori e i loro stadi di ricezione, riducendo la sensibilità del ricevitore fino a bloccarne completamente la ricezione. Questo può ad esempio impedire il corretto funzionamento dei telecomandi per porte da garage. Spesso anche le lampade a LED, che vengono comandate tramite sensori capacitivi, vengono influenzate dalle trasmissioni. In questi casi si parla di *sovraeccitazione* o *disturbo indesiderato* degli apparecchi.

[question:EJ106]
[question:EJ107]
[question:EJ103]
[question:EJ112]

Spesso i disturbi nelle vicinanze vengono associati al funzionamento di una stazione radioamatoriale. Per dimostrare un eventuale nesso causale con le trasmissioni della stazione radioamatoriale, è molto utile valutare e, se necessario, tenere un registro delle trasmissioni e dei collegamenti effettuati. In questo modo è anche possibile escludere che i presunti disturbi nelle vicinanze siano da attribuire alla stazione radioamatoriale.

[question:EJ122]

Il radioamatore dovrebbe collaborare in modo costruttivo e orientato alle soluzioni con i vicini e proporre anche possibili soluzioni. Spesso i problemi possono essere risolti più facilmente parlando direttamente piuttosto che coinvolgendo le autorità. Solo se tutti i tentativi falliscono, è possibile rivolgersi alla sede competente dell'Agenzia federale delle reti per una verifica della situazione. Tuttavia, questo dovrebbe essere davvero l'ultimo mezzo per risolvere il problema.

[question:EJ124]
[question:VN004]

A tali sforzi appartengono varie misure, come ad esempio:

%- Riduzione della potenza di trasmissione dell'impianto radioamatoriale % Questo dovrebbe essere l'ultima risorsa!
- Schermatura di apparecchi o cavi sensibili
- Installazione di filtri e induttanze di modo comune sul lato ricevente del vicino
- Realizzazione di un efficace collegamento a terra HF
- Utilizzo di antenne esterne per la ricezione

Queste misure verranno esaminate più in dettaglio nel seguito.

Per evitare disturbi indesiderati sugli apparecchi, un radioamatore dovrebbe utilizzare solo la potenza di trasmissione necessaria per una *comunicazione soddisfacente*.

[question:EJ104]
[question:EJ105]

Se in un impianto di ricezione sono presenti contemporaneamente più segnali di ricezione forti (ad esempio a causa della ricezione di una stazione televisiva locale e di una stazione radioamatoriale potente nelle vicinanze), nello stadio ricevente del ricevitore possono formarsi armoniche indesiderate e i loro prodotti di miscelazione a causa della sovraeccitazione degli stadi di ricezione. Questo fenomeno è chiamato *intermodulazione*. L'intermodulazione genera *segnali fantasma* che si formano solo in presenza dei segnali coinvolti.

[question:EJ120]

Anche in un impianto stereo spento, forti segnali HF possono causare rumori udibili negli altoparlanti a causa del raddrizzamento nello stadio finale BF su componenti non lineari come i transistor. Anche i contatti corrosi tra metalli (ossidi metallici) hanno la proprietà di formare effetti di raddrizzamento a causa di non linearità. Ciò può generare prodotti di miscelazione indesiderati sul lato di trasmissione o di ricezione che portano a disturbi indesiderati nella ricezione televisiva e radiofonica durante le trasmissioni della stazione radioamatoriale.

[question:EJ113]
[question:EJ121]

Non tutti i disturbi possono essere risolti con misure sul lato trasmittente. Spesso l'apparecchio disturbato non è adatto al luogo di utilizzo, non soddisfa i requisiti legali vigenti o i cavi di alimentazione e le schermature non sono sufficientemente dimensionati per resistere alle irradiazioni o alle correnti entranti ad alta frequenza. In questi casi è opportuno suggerire ai soggetti interessati delle misure per risolvere il problema.

Una possibile misura consiste nel schermare i moduli HF con un involucro metallico chiuso.

[question:EJ108]

Se un'antenna trasmittente in onde corte si trova vicino e parallela a una linea di alimentazione a corrente alternata da $\qty{230}{\volt}$, le correnti ad alta frequenza possono essere accoppiate nella rete elettrica. Per ridurre al minimo i disturbi all'interno della propria abitazione, si consiglia di utilizzare un collegamento di terra HF separato per le antenne trasmittenti.

[question:EJ109]
[question:EJ111]

Un'altra possibilità è l'*installazione di filtri nei cavi di alimentazione degli apparecchi* e l'uso di *induttanze di modo comune (choke)* sui cavi di alimentazione.

In particolare, i filtri possono essere installati sul lato dell'apparecchio disturbato (TV, ricevitore DVB-T2, ricevitore DAB ecc.) nel percorso di ricezione. Ad esempio, l'intensità di campo di un trasmettitore radioamatoriale in onde corte (ad esempio nell'intervallo $\qtyrange{3}{30}{\mega\hertz}$) può influenzare la ricezione televisiva (ad esempio $\qtyrange{470}{690}{\mega\hertz}$). Installando un filtro passa-alto, l'influenza del segnale trasmittente radioamatoriale può essere notevolmente ridotta: le componenti di frequenza al di fuori dell'intervallo di ricezione TV – in questo esempio le onde corte – vengono attenuate, in modo che gli stadi di ricezione dell'apparecchio non vengano più sovraeccitati.

[question:EJ116]
[question:EJ117]

Spesso il segnale trasmittente di una stazione radioamatoriale nelle vicinanze viene accoppiato nei ricevitori o apparecchi disturbati tramite la calza dei cavi coassiali o dei cavi di alimentazione. Se si verificano disturbi, su questi cavi di alimentazione dell'apparecchio disturbato dovrebbe essere installata una cosiddetta *induttanza di modo comune*. Un'induttanza di modo comune blocca le *correnti in modo comune* sulla calza e sul conduttore interno dell'apparecchio disturbato. Come induttanze di modo comune vengono generalmente utilizzati nuclei toroidali o nuclei a pinza in ferrite. Un'altra possibilità per evitare disturbi nelle linee di comando di impianti e apparecchi elettrici è l'uso di cavi schermati (ad esempio per impianti citofonici, linee telefoniche ecc.).

[question:EJ118]
[question:EJ119]
[question:EJ115]
[question:EJ114]

%Anche le scarse condizioni di ricezione sul lato dell'apparecchio disturbato (ad esempio antenna TV interna per la ricezione) possono portare più facilmente a disturbi nella ricezione. Una possibile contromisura potrebbe essere l'uso di un'antenna esterna, eventualmente con filtri previ.

%[question:EJ123]