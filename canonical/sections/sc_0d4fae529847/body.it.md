**IN LAVORAZIONE**

<attention>
A causa delle frequenze utilizzate dai satelliti, il radioamatore via satellite richiede purtroppo una licenza HB9. Poiché questo argomento riguarda principalmente normative e tecnica operativa, viene trattato già nel corso HB3.
</attention>

<margin>
[photo:124:n_satellit_oscar1:Modello del primo satellite radioamatoriale OSCAR 1, che nel 1961 trasmise per 22 giorni dal suo orbita intorno alla terra una beacon nella banda dei $\qty{2}{\meter}$ e fu ricevuto da 570 radioamatori di 28 paesi]
</margin>

---
I satelliti orbitano intorno alla terra seguendo traiettorie circolari od ellittiche e a diverse altitudini. Maggiori dettagli seguiranno nella sezione [sec:satelliten_2]. Dal 1961 esistono anche satelliti radioamatoriali. Questi vengono denominati OSCAR, che è l’acronimo di "Orbiting Satellite Carrying Amateur Radio" ("Satellite in orbita che trasporta apparecchiature radioamatoriali"). Il primo satellite radioamatoriale fu chiamato OSCAR 1 ([ref:n_satellit_oscar1]). OSCAR 1 fu solo l’inizio. Negli anni successivi – fino ad oggi – sono stati lanciati nello spazio numerosi carichi utili radioamatoriali sempre più sofisticati.

[question:BE415]
Le stazioni radio ripetitori trasportate vengono definite "transponder". La frequenza di ingresso, cioè il percorso radio dalla terra al satellite, nel radioamatoriale via satellite viene chiamata "Uplink". La frequenza di uscita, cioè il percorso radio dal satellite alla terra, viene invece denominata "Downlink". Per uplink e downlink vengono spesso utilizzate bande di frequenza diverse, poiché ciò consente una separazione più semplice tra segnale trasmesso e segnale ricevuto e riduce le dimensioni dei filtri a bordo del satellite.<indepth>
*Caratterizzazione delle orbite dei satelliti (orbits)*

Le orbite dei satelliti possono essere descritte in base a diverse proprietà. I termini LEO, MEO e GEO si riferiscono principalmente all'altezza dell'orbita. Termini come HEO o orbita polare descrivono invece altre caratteristiche dell'orbita, in particolare la sua forma o inclinazione. Queste classificazioni possono quindi sovrapporsi. Di seguito presentiamo le principali altezze di volo o orbite.*Orbite basse (Low Earth Orbit - LEO)*
I satelliti in orbita bassa si trovano a un'altezza compresa tra circa 400 e 2'000 metri sopra la superficie terrestre. Si tratta di orbite che si trovano relativamente vicine alla superficie terrestre. In questa fascia si muovono molti satelliti per l'osservazione della terra e meteorologici, nonché numerosi satelliti radioamatoriali. La vicinanza alla terra consente un'elevata risoluzione nella raccolta di dati e immagini. La breve distanza dalla terra permette percorsi radio relativamente brevi e quindi una minore attenuazione nello spazio libero. Allo stesso tempo, i satelliti LEO si muovono rapidamente nel cielo e sono visibili da una determinata stazione radio solo durante un passaggio di durata limitata.*Orbite medie (Medium Earth Orbit - MEO)*
Le orbite medie si trovano approssimativamente tra 2'000 e 35'786 chilometri di altezza. In questa fascia si trovano, ad esempio, molti satelliti di navigazione, come quelli utilizzati per il noto sistema GPS. Poiché i satelliti impiegano più tempo a orbitare intorno alla terra, offrono un equilibrio ottimale tra copertura e precisione per la navigazione e la localizzazione. Con l'aumentare dell'altezza dell'orbita, aumenta anche il periodo orbitale. Allo stesso tempo, si amplia l'area raggiungibile da un satellite.*Orbite alte (Geostationary Orbit - GEO)*

Un'orbita geosincrona ha un periodo orbitale di circa un giorno siderale, cioè 23 ore, 56 minuti e 4 secondi. Una forma particolare di questa orbita è l'orbita geostazionaria (Geostationary Orbit, GEO) a un'altezza di circa 35.786 chilometri sopra l'equatore.Un satellite geostazionario si muove su un'orbita quasi circolare sopra l'equatore, nella stessa direzione di rotazione e con la stessa velocità angolare della terra. Da terra, appare quindi quasi fisso nel cielo. Ciò consente a una stazione di terra di puntare la propria antenna in modo permanente verso la stessa posizione. I satelliti geostazionari sono quindi particolarmente adatti per applicazioni di comunicazione e consentono una copertura costante di una determinata area.[QO-100](https://amsat-dl.org/p4-a-nb-transponder-bandplan-und-betriebsrichtlinien/) è finora il primo satellite geostazionario con un payload radioamatoriale.*Orbite altamente ellittiche (Highly Elliptical Orbit - HEO)*

Le orbite altamente ellittiche hanno una forma ellittica fortemente eccentrica. In questo caso, durante una parte dell'orbita, il satellite si trova a una distanza dalla terra notevolmente maggiore rispetto al resto del percorso. Le orbite HEO possono essere progettate in modo che un satellite rimanga visibile a lungo sopra le alte latitudini geografiche. Pertanto, sono adatte, ad esempio, per applicazioni che richiedono una buona copertura delle regioni polari. HEO non è una semplice classe di altitudine come LEO o MEO, ma descrive soprattutto la forma dell'orbita.

*Orbite polari (Polar Orbit)*
I satelliti che operano in orbite polari sorvolano i poli della terra. In un'orbita polare, l'inclinazione orbitale è di circa 90°. Poiché la terra ruota sotto l'orbita del satellite, con un'orbita adeguata è possibile sorvolare quasi tutte le regioni della superficie terrestre nel corso del tempo. Anche un'orbita polare non è una classe di altitudine a sé stante. Un satellite può, ad esempio, essere utilizzato contemporaneamente in un'orbita LEO e in un'orbita polare.
</indepth>
[question:BE416]
[question:BE411]
[question:BE412]
[question:NF113]

---

Nella comunicazione via satellite, l'orientamento delle antenne riveste un ruolo centrale. I termini *azimut* ed *elevazione* assumono in questo contesto un'importanza fondamentale. Essi descrivono l'orientamento orizzontale e l'angolo verticale sotto cui un satellite viene percepito dalla superficie terrestre:
* L'*azimut* è la direzione lungo l'orizzonte in cui si guarda per vedere il satellite. Viene solitamente misurato in gradi e varia da $\qty{0}{\degree}$ (nord) a $\qty{90}{\degree}$ (est), $\qty{180}{\degree}$ (sud) fino a $\qty{270}{\degree}$ (ovest).
* L'*elevazione* è l'angolo verticale con cui un satellite si trova sopra l'orizzonte rispetto alla posizione dell'osservatore. Viene anch'essa misurata in gradi e varia da $\qty{0}{\degree}$ (direttamente sull'orizzonte) a $\qty{90}{\degree}$ (sopra la testa dell'osservatore).

<margin>
[picture:876:n_azimut_elevation:Azimut ed elevazione nello spazio]
</margin>

<wordorigin>
Il termine *azimut* deriva dall'arabo *as-sumūt* ("le vie"). *Elevazione* trae origine dal latino *elevare* ("sollevare").
</wordorigin>

[question:BE413]
[question:BE414]

Nel servizio di radioamatore via satellite vige un'eccezione all'obbligo di utilizzare esclusivamente comunicazioni in chiaro. È consentito cifrare i segnali di comando tra stazioni terrestri e satelliti amatoriali allo scopo di occultamento. Ciò significa che, in via eccezionale, possono essere utilizzati metodi di cifratura che impediscono a terzi di leggere il contenuto dei segnali di comando. Questo serve a proteggere i satelliti da comandi di controllo da parte di persone non autorizzate.

[question:VA303]
[question:VN026]


Nel diritto tedesco – ma non a livello internazionale – questa regolamentazione si applica anche ai segnali di comando per stazioni automatiche, telecomandate e remote. La domanda corrispondente VD104 è stata eliminata.

---

**XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX**
**QUESTA PARTE APPARTIENE A UN CAPITOLO DI APPROFONDIMENTO PER LA PARTE HB9**

---

<attention>
*Questo argomento non è rilevante per l'esame.*
I satelliti e l'esplorazione spaziale stanno assumendo un ruolo sempre più importante. Grazie al servizio di radioamatore, possiamo operare anche in questo affascinante settore tramite satelliti. Pertanto, riteniamo che questa introduzione debba far parte di un corso di radioamatore, anche se attualmente non è oggetto di esame.
</attention>

## Orbite e leggi di Keplero

I satelliti non si muovono arbitrariamente intorno alla terra. Le loro orbite sono determinate dalla forza di gravità e possono essere descritte con le leggi di Keplero. Un'orbita circolare rappresenta un caso particolare di orbita ellittica ([ref:a_kepler_ellipse]).

### 1ª legge di Keplero – Legge delle ellissi

L'orbita di un satellite intorno alla terra è fondamentalmente un'ellisse. La terra si trova in uno dei due fuochi dell'ellisse. In un'orbita circolare, i due fuochi coincidono.

---

### 2. Seconda legge di Keplero - Legge delle aree

La linea che congiunge la terra e il satellite spazza aree uguali in tempi uguali. Ne consegue che un satellite si muove più velocemente nel punto più vicino alla terra, il perigeo, e più lentamente nel punto più lontano, l'apogeo, lungo la sua orbita ellittica.

Questo comportamento è interessante anche per la pratica radioamatoriale, poiché la velocità relativa tra satellite e stazione radio varia durante un passaggio.

### 3. Seconda legge di Keplero - Legge dei periodi

Per i satelliti che orbitano intorno allo stesso corpo centrale vale:

$$T^2 \propto a^3$$

Qui, $T$ rappresenta il periodo orbitale e $a$ il semiasse maggiore dell'orbita ellittica. Maggiore è il semiasse maggiore e quindi la distanza media orbitale, più lungo sarà il periodo orbitale.

Per la pratica satellitare questo significa: i satelliti in orbite basse compiono un giro intorno alla terra molto più velocemente rispetto a quelli in orbite più alte.

<margin>
[immagine:10100:a_kepler_ellipse:Ellisse di Keplero con satellite in orbita] 
</margin>

## Visibilità di un satellite

Per una stazione radio sulla terra, non è importante se un satellite orbiti effettivamente intorno alla terra, ma se si trovi attualmente sopra l’orizzonte locale. Un passaggio inizia con l’"Acquisition of Signal" (AOS), quando il satellite diventa visibile o ricevibile per la stazione. Termina con il "Loss of Signal" (LOS), quando il satellite scompare nuovamente sotto l’orizzonte.

La posizione di un satellite nel cielo viene indicata tramite l’azimut, cioè la direzione lungo l’orizzonte, e l’elevazione, cioè l’angolo sopra l’orizzonte. Durante un passaggio, entrambi i valori cambiano continuamente.

La zona sulla superficie terrestre da cui un satellite può essere visto sopra l’orizzonte viene chiamata footprint. Più alto vola il satellite, maggiore può essere questa zona.

---

## Effetto Doppler nella radio via satellite

Poiché un satellite si muove rispetto a una stazione radio sulla terra, in un collegamento radio con il satellite si verifica l’effetto Doppler. In questo caso, la frequenza ricevuta cambia rispetto a quella effettivamente trasmessa.

Quando il satellite si avvicina alla stazione radio, la frequenza ricevuta aumenta rispetto alla frequenza nominale. Quando il satellite si allontana, la frequenza ricevuta diminuisce.

Per velocità piccole rispetto alla velocità della luce, lo spostamento di frequenza può essere approssimato con

$$\Delta f \approx f_0 \frac{v_r}{c}$$

dove $f_0$ è la frequenza di trasmissione, $v_r$ la velocità relativa nella direzione del collegamento radio e $c$ la velocità della luce. Ciò che conta, quindi, è la velocità radiale e non la velocità orbitale totale del satellite.

Nei satelliti LEO la variazione Doppler può essere particolarmente evidente alle frequenze più elevate e nelle modalità operative a banda stretta. Pertanto, durante il passaggio del satellite, potrebbe essere necessario regolare continuamente la frequenza. Le stazioni satellitari moderne possono eseguire automaticamente la compensazione Doppler.<indepth>
Questa applet visualizza l'effetto Doppler. Con la barra di scorrimento è possibile impostare la *velocità relativa tra trasmettitore e ricevitore*.
- Se la *sorgente si avvicina al ricevitore*, arrivano più fronti d'onda per unità di tempo, corrispondenti a un *aumento della frequenza ricevuta*. Nonostante il trasmettitore invii sempre la stessa frequenza.- Se la *sorgente si allontana dal ricevitore*, arrivano meno fronti d'onda per unità di tempo, corrispondenti a una *diminuzione della frequenza ricevuta*. Nonostante il trasmettitore invii sempre la stessa frequenza.[include:doppler_visualisierung]

</indepth>

## Attenuazione nello spazio libero e collegamento radio

Il segnale radio di un satellite deve percorrere una grande distanza tra la stazione di terra e il satellite. In questo processo si verifica la cosiddetta attenuazione nello spazio libero. Essa aumenta con l'aumentare della distanza e con l'aumentare della frequenza.Per un collegamento ideale nello spazio libero vale la formula di Friis, che costituisce la base per ogni bilancio di collegamento:

$$L_{FS}=20\log_{10}\left(\frac{4\pi d}{\lambda}\right)$$In questo caso, $d$ è la distanza tra trasmettitore e ricevitore e $\lambda$ è la lunghezza d’onda.

Per una connessione satellitare funzionante, è necessario considerare congiuntamente la potenza di trasmissione, il guadagno d'antenna, le perdite del cavo, l’attenuazione dello spazio libero e la sensibilità del ricevitore. Questa valutazione viene chiamata *link budget*.

<indepth>
*Esempio semplificato di downlink di un CubeSat LEO a 145 MHz*

Un esempio fortemente semplificato di un downlink da un
CubeSat LEO a una stazione di terra potrebbe essere il seguente:

| Grandezza | Valore di esempio |
| Frequenza | 145 MHz |
| Potenza di trasmissione | 1 W = 0 dBW |
| Cavo TX e connettori | −1 dB |
| Antenna trasmittente | +3 dBi |
| EIRP | +2 dBW |
| Distanza | 1 000 km |
| Attenuazione dello spazio libero | −135,7 dB |
| Antenna ricevente | +15 dBi |
| Cavo RX e connettori | −2 dB |
| Potenza ricevuta | −120,7 dBW = −90,7 dBm |

In un *link budget* reale si aggiungono altri fattori, ad esempio il tipo di modulazione, il tasso di dati, il rumore del ricevitore e la riserva di collegamento.
</indepth>

## Antenne e polarizzazione

Poiché il satellite si muove durante un passaggio, anche la sua direzione rispetto alla stazione di terra cambia. Per molte connessioni satellitari si utilizzano quindi antenne con un guadagno adeguato e una direttività sufficiente. Con antenne più direttive può essere necessaria una tracciatura (*tracking*) dell’antenna.

Anche la polarizzazione del segnale deve essere considerata. A causa del movimento e dell’orientamento del satellite, l’orientamento della polarizzazione può variare rispetto alla stazione di terra. Nelle comunicazioni satellitari, a seconda dell’applicazione, si utilizzano quindi polarizzazioni lineari o circolari.

## Trasponder e digipeater

I satelliti per radioamatori possono avere diversi tipi di carichi utili radio.Un transponder lineare riceve una banda di frequenza e la converte in un'altra banda di frequenza. Più segnali possono essere trasmessi contemporaneamente all'interno della larghezza di banda disponibile del transponder. Le modalità operative tipiche sono, ad esempio, SSB e CW.Un transponder FM, invece, opera con segnali FM ed è generalmente progettato per la trasmissione simultanea di una singola conversazione o di pochi segnali pianificati di conseguenza.Un digipeater riceve dati digitali e li ritrasmette secondo una procedura definita. Si differenzia quindi fondamentalmente da un transponder lineare, che converte lo spettro di frequenza ricevuto senza elaborare i singoli segnali utili come pacchetti di dati.## Stazioni radio beacon dei satellitiMolti satelliti per radioamatori sono dotati di una stazione beacon. [sec:baken] trasmettono automaticamente a intervalli regolari o in modo continuo segnali definiti. Possono servire a monitorare la ricezione del satellite, le condizioni di propagazione e lo stato del carico utile radio.Ricevendo un beacon, una stazione radio può ad esempio determinare se il satellite si trova già sopra l'orizzonte, come la frequenza di ricezione cambi a causa dell'effetto Doppler e quanto sia buona la qualità del collegamento radio.## Tracciamento dei satellitiPer la pratica del satellite radio sono necessarie la traiettoria attuale e la posizione del satellite. A tal fine si utilizzano elementi orbitali, ad esempio i cosiddetti TLE (Two-Line Elements). I programmi di tracciamento calcolano da questi la posizione prevista del satellite e mostrano tra l'altro l'azimut, l'elevazione, l'AOS e il LOS, nonché l'effetto Doppler atteso.In questo modo è possibile pianificare i passaggi e far seguire automaticamente le apparecchiature radio e le antenne.---

I satelliti radioamatoriali dispongono di una beacon. Una beacon trasmette automaticamente a intervalli regolari o in modo continuo segnali definiti. Può servire a monitorare la ricezione del satellite, le condizioni di propagazione e lo stato del carico utile radio.

Durante la ricezione di una beacon, una stazione radio può ad esempio determinare se il satellite si trova già sopra l’orizzonte, come la frequenza di ricezione cambi a causa dell’effetto Doppler e quanto sia buona la qualità del collegamento radio.

Nel capitolo [sec:satelliten] abbiamo imparato a conoscere diverse orbite dei satelliti. Il periodo orbitale di un satellite intorno alla terra dipende dall’altezza della sua orbita. Questa relazione è illustrata nell’immagine [ref: a_umlaufzeiten].

<indepth>
*Periodo orbitale di un satellite*
[immagine:10101:a_umlaufzeiten:Periodi orbitali in funzione dell’altezza dell’orbita]
</indepth>

<tip>
Le organizzazioni AMSAT si occupano a livello mondiale di radioamatoriale via satellite; in Svizzera è [AMSAT-HB](https://amsat-hb.org/)
</tip>

