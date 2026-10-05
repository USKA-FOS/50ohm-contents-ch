<attention>
La radio via satellite è già trattata nel corso HB3 sotto le normative di base e la tecnica operativa. Gli aspetti tecnici avanzati sono approfonditi nel corso HB9 nel capitolo [sec:satelliten_2].
</attention>

<margin>
[photo:124:n_satellit_oscar1:Modello del primo satellite radioamatoriale OSCAR 1, che nel 1961 trasmise per 22 giorni dal'orbita terrestre un segnale faro nella banda dei $\qty{2}{\meter}$ e fu ascoltato da 570 radioamatori di 28 paesi]
</margin>

---

I satelliti orbitano attorno alla terra in traiettorie circolari o ellittiche e a diverse altezze.
Dal 1961, tra questi ci sono anche i satelliti radioamatoriali. Questi sono chiamati OSCAR. È l'abbreviazione di "Orbiting Satellite Carrying Amateur Radio" ("Satellite orbitante che trasporta radioamatoriale"). Il primo satellite radioamatoriale fu chiamato OSCAR 1 ([ref:n_satellit_oscar1]). OSCAR 1 fu solo l'inizio. Negli anni successivi - fino ad oggi - è stata lanciata nello spazio una serie di carichi utili radioamatoriali sempre più completi. Chi è interessato alla storia dei satelliti radioamatoriali può trovare maggiori informazioni nella [History of AMSAT](https://www.amsat.org/amsat-history/).
% Con l'ultima frase è soddisfatto anche il requisito di una citazione della fonte.
[question:BE415]

In questo capitolo impariamo "Cos'è un satellite radioamatoriale?" e "Come si muove?". Nel capitolo [sec:satelliten_2] scopriremo poi "Come posso effettivamente effettuare una comunicazione radio via satellite?".

Le stazioni ripetitrici trasportate sono chiamate "transponder". La frequenza di ingresso, cioè il collegamento radio dalla terra al satellite, è chiamata "uplink" nella radio via satellite. La frequenza di uscita, cioè il collegamento radio dal satellite alla terra, è invece chiamata "downlink". Per uplink e downlink vengono spesso utilizzate bande di frequenza diverse, perché ciò consente un disaccoppiamento più semplice tra il segnale trasmesso e il segnale ricevuto.

<indepth>
Diverse altezze di volo e orbite dei satelliti consentono una vasta gamma di applicazioni satellitari, dalla comunicazione alla navigazione, fino alla ricerca scientifica e all'osservazione della terra. Di seguito presentiamo le principali altezze di volo o orbite.

*Caratterizzazione delle orbite satellitari (orbits)*

Le orbite satellitari possono essere descritte secondo diverse proprietà. I termini LEO, MEO e GEO si riferiscono principalmente all'altezza dell'orbita. Termini come HEO o Polar Orbit descrivono invece altre proprietà dell'orbita, in particolare la sua forma o inclinazione. Queste classificazioni possono quindi sovrapporsi. Di seguito presentiamo le principali altezze o orbite.

*Orbite basse (Low Earth Orbit - LEO)*
I satelliti in orbite basse sono tipicamente posizionati ad altezze di circa 160 a 2'000 chilometri sopra la terra. Si tratta di orbite che si trovano relativamente vicine alla superficie terrestre. In questa regione si muovono molti satelliti per l'osservazione della terra, come i satelliti meteorologici o i satelliti per il monitoraggio ambientale. La vicinanza alla terra consente un'alta risoluzione nell'acquisizione di dati e immagini. La breve distanza dalla terra consente collegamenti radio relativamente brevi e quindi una bassa attenuazione nello spazio libero. Allo stesso tempo, i satelliti LEO si muovono rapidamente nel cielo e sono visibili da una specifica stazione radio solo durante un sorvolo temporalmente limitato.

*Orbite medie (Medium Earth Orbit - MEO)*
Le orbite medie si estendono ad altezze di circa 2'000 a 35'786 chilometri sopra la terra. Questa regione ospita spesso satelliti di navigazione, come quelli utilizzati per il noto sistema GPS. Poiché i satelliti qui impiegano più tempo per orbitare attorno alla terra, offrono un equilibrio tra copertura e precisione per la navigazione e il posizionamento. Con l'aumentare dell'altezza dell'orbita, si allunga il periodo orbitale. Allo stesso tempo, aumenta l'area raggiungibile da un satellite.

*Orbita geostazionaria (Geostationary Orbit – GEO)*
Ad altezze di circa 35'786 chilometri sopra la superficie terrestre si trovano le orbite geostazionarie. Un satellite geostazionario si muove su un'orbita quasi circolare sopra l'equatore nella stessa direzione di rotazione e con la stessa velocità angolare della terra. Di conseguenza, visto dalla terra, appare quasi fermo nel cielo. Ciò consente a una stazione di terra di orientare la sua antenna permanentemente nella stessa posizione. I satelliti geostazionari sono quindi particolarmente adatti per applicazioni di comunicazione e consentono una copertura costante di una specifica area.
Un'orbita geosincrona ha un periodo orbitale di circa un giorno siderale, cioè 23 ore, 56 minuti e 4 secondi. Una forma particolare di questa è l'orbita geostazionaria (Geostationary Orbit, GEO) a un'altezza di circa 35'786 chilometri sopra l'equatore. [QO-100](https://amsat-dl.org/p4-a-nb-transponder-bandplan-und-betriebsrichtlinien/) è il carico utile radioamatoriale sul satellite geostazionario Es’hail-2 ed è stato il primo carico utile radioamatoriale in un'orbita geostazionaria.

*Orbite altamente ellittiche (Highly Elliptical Orbit - HEO)*
Le orbite altamente ellittiche hanno una forma ellittica fortemente eccentrica. Il satellite è significativamente più lontano dalla terra durante una parte dell'orbita rispetto al resto della rivoluzione. Le orbite HEO possono essere progettate in modo che un satellite rimanga visibile a lungo ad alte latitudini geografiche. Sono quindi adatte, ad esempio, per applicazioni che richiedono una buona copertura delle regioni polari. HEO non è una pura classe di altezza come LEO o MEO, ma descrive principalmente la forma dell'orbita.

*Orbite polari (Polar Orbit)*
I satelliti che operano in orbite polari volano sopra i poli della terra. In un'orbita polare, l'inclinazione dell'orbita è di circa 90 gradi. Poiché la terra ruota sotto l'orbita del satellite, nel corso del tempo possono essere sorvolate quasi tutte le regioni della superficie terrestre. Poiché queste orbite forniscono una copertura completa della superficie terrestre nel tempo, sono spesso utilizzate per indagini scientifiche, monitoraggio ambientale e osservazione della terra.

Anche un'orbita polare non è una propria classe di altezza. Un satellite può, ad esempio, operare contemporaneamente in un'orbita LEO e in un'orbita polare.
</indepth>

[question:BE416]
[question:BE411]
[question:BE412]
[question:NF113]

---

Nell'utilizzo della comunicazione satellitare, l'orientamento delle antenne è di fondamentale importanza. I termini *Azimut* ed *Elevazione* giocano un ruolo chiave. Descrivono l'orientamento orizzontale e l'angolo verticale sotto i quali un satellite è percepito dalla superficie terrestre.
* L'*Azimut* è la direzione lungo l'orizzonte in cui si guarda per vedere il satellite. È solitamente misurato in gradi e va da $\qty{0}{\degree}$ (nord) a $\qty{90}{\degree}$ (est), $\qty{180}{\degree}$ (sud) fino a $\qty{270}{\degree}$ (ovest).
* L'*Elevazione* è l'angolo verticale sotto il quale un satellite si trova sopra l'orizzonte. È anch'esso misurato in gradi e varia da $\qty{0}{\degree}$ (direttamente all'orizzonte) a $\qty{90}{\degree}$ (perpendicolarmente sopra di sé).

<margin>
[picture:876:n_azimut_elevation:Azimut ed Elevazione nello spazio]
</margin>

<wordorigin>
Il termine *Azimut* deriva dall'arabo *as-sumūt*, ("le vie"). *Elevazione* deriva dal latino elevare ("sollevare").
</wordorigin>

[question:BE413]
[question:BE414]

Nel servizio di radioamatore via satellite vale un'eccezione all'obbligo di utilizzare solo linguaggio aperto. Alle stazioni di comando è eccezionalmente permesso cifrare i segnali di comando ai satelliti radioamatoriali allo scopo di occultarli. Ciò significa che per questo scopo possono essere utilizzati eccezionalmente procedimenti di cifratura che impediscono a terzi di leggere il contenuto dei segnali di comando. Questo serve a proteggere i satelliti da comandi di controllo da parte di non autorizzati.

[question:VA303]
[question:VN026]


%Nella legge tedesca - ma non a livello internazionale - questa regola si applica anche ai segnali di comando per stazioni automatiche, telecomandate e remote. Domanda corrispondente VD104 eliminata.
