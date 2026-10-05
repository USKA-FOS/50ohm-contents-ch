<attention>
*Questo argomento non è rilevante per l'esame.*
I satelliti e i viaggi spaziali stanno assumendo un ruolo sempre più importante. Grazie al servizio radioamatoriale, noi radioamatori possiamo essere attivi anche in questo campo entusiasmante tramite i satelliti. Pertanto, riteniamo che questa introduzione debba far parte di un corso radioamatoriale, anche se attualmente l'argomento non è oggetto d'esame.
</attention>

Alcune basi sono già note dal capitolo [sec:satelliten]. Qui vengono trattati ulteriori termini della comunicazione satellitare.

## Orbite e leggi di Keplero

I satelliti non si muovono arbitrariamente attorno alla Terra. Le loro orbite sono determinate dalla gravità e possono essere descritte con le leggi di Keplero. Un'orbita circolare è un caso speciale di un'orbita ellittica ([ref:a_kepler_ellipse]).

### 1a legge di Keplero - Legge delle ellissi

L'orbita di un satellite attorno alla Terra è fondamentalmente un'ellisse. La Terra si trova in uno dei due fuochi dell'ellisse. In un'orbita circolare, i due fuochi coincidono.

---

### 2a legge di Keplero - Legge delle aree

La linea di connessione tra la Terra e il satellite copre aree uguali in tempi uguali. Ne consegue: un satellite su un'orbita ellittica si muove più velocemente nel punto più vicino alla Terra, il perigeo, e più lentamente nel punto più lontano dalla Terra, l'apogeo.

Questo comportamento è interessante anche per la pratica radio, perché la velocità relativa tra il satellite e la stazione radio cambia durante un sorvolo.

### 3a legge di Keplero - Legge dei periodi

Per i satelliti che orbitano attorno allo stesso oggetto centrale vale:

$$T^2 \propto a^3$$

Dove $T$ è il periodo orbitale e $a$ è il semiasse maggiore dell'ellisse orbitale. Più grande è il semiasse maggiore dell'orbita, più lungo è il periodo orbitale.
Per la pratica satellitare, ciò significa: i satelliti in orbite basse orbitano attorno alla Terra molto più velocemente dei satelliti in orbite più alte.

<margin>
[picture:10100:a_kepler_ellipse:Ellisse di Keplero con satellite in orbita]
</margin>

### Periodo orbitale di un satellite

Nel capitolo [sec:satelliten] abbiamo conosciuto diverse orbite satellitari. Il periodo orbitale di un satellite attorno alla Terra dipende dal semiasse maggiore della sua orbita. Per le orbite circolari, questo corrisponde all'altezza dell'orbita più il raggio terrestre. Questa relazione è illustrata nell'immagine
[ref:a_umlaufzeiten].

<indepth>
*Periodo orbitale di un satellite*
[picture:10101:a_umlaufzeiten:Periodi orbitali in funzione dell'altezza dell'orbita]
</indepth>

Per la pratica del satellite radio, sono particolarmente importanti il periodo orbitale, la visibilità e la velocità del satellite.

## Visibilità di un satellite

Per una stazione radio sulla Terra, non è decisivo se un satellite orbita fondamentalmente attorno alla Terra, ma se si trova attualmente sopra l'orizzonte locale. Un sorvolo inizia con l'"Acquisition of Signal" (AOS), quando il satellite diventa visibile o ricevibile per la stazione. Termina con il "Loss of Signal" (LOS), quando scende di nuovo sotto l'orizzonte.

La posizione di un satellite nel cielo è indicata dall'azimut, cioè la direzione lungo l'orizzonte, e dall'elevazione, cioè l'angolo sopra l'orizzonte. Durante un sorvolo, entrambi i valori cambiano continuamente.

L'area sulla superficie terrestre in cui un satellite o il suo carico utile radio può essere ricevuto è chiamata footprint. Più alto vola il satellite, più grande può essere quest'area.

---

## Effetto Doppler nel satellite radio

Poiché un satellite si muove relativamente alla stazione radio sulla Terra, in un collegamento radio con il satellite si verifica l'effetto Doppler. In questo caso, la frequenza ricevuta cambia rispetto alla frequenza effettivamente trasmessa.

Quando il satellite si avvicina alla stazione radio, la frequenza ricevuta aumenta rispetto alla frequenza nominale. Quando il satellite si allontana di nuovo, la frequenza ricevuta diminuisce.

Per piccole velocità rispetto alla velocità della luce, lo spostamento di frequenza può essere approssimato con

$$\Delta f \approx f_0 \frac{v_r}{c}$$

Dove $f_0$ è la frequenza di trasmissione, $v_r$ è la velocità relativa nella direzione del collegamento radio e $c$ è la velocità della luce. Decisiva è quindi la velocità radiale e non l'intera velocità orbitale del satellite. Sia $v_r > 0$ quando trasmettitore e ricevitore si avvicinano.

Per i satelliti LEO, lo spostamento Doppler può essere particolarmente evidente, specialmente a frequenze più alte e con modalità operative a banda stretta. Pertanto, la frequenza potrebbe dover essere continuamente corretta durante un sorvolo satellitare. Le moderne stazioni satellitari possono eseguire automaticamente la compensazione Doppler.

<indepth>
Questa applet visualizza l'effetto Doppler. Con il cursore è possibile impostare la *velocità relativa tra trasmettitore e ricevitore*.

- Quando la *sorgente si avvicina al ricevitore*, arrivano più fronti d'onda per unità di tempo, il che corrisponde a un *aumento della frequenza ricevuta*. Anche se il trasmettitore trasmette sempre alla stessa frequenza.

- Quando la *sorgente si allontana dal ricevitore*, arrivano meno fronti d'onda per unità di tempo, il che corrisponde a una *diminuzione della frequenza ricevuta*. Anche se il trasmettitore trasmette sempre alla stessa frequenza.

[include:doppler_visualisierung]

</indepth>

## Attenuazione nello spazio libero e collegamento radio

Il segnale radio di un satellite deve percorrere una grande distanza tra la stazione di terra e il satellite. In questo processo si crea la cosiddetta attenuazione nello spazio libero. Aumenta con la distanza crescente e con la frequenza crescente.

Per un collegamento ideale nello spazio libero vale la formula di Friis per lo spazio libero, che costituisce la base per ogni budget di collegamento:

$$L_{FS}=20\log_{10}\left(\frac{4\pi d}{\lambda}\right)$$

Dove $d$ è la distanza tra trasmettitore e ricevitore e $\lambda$ è la lunghezza d’onda.

Per un collegamento satellitare funzionante, quindi, potenza di trasmissione, guadagno d'antenna, perdite del cavo, attenuazione nello spazio libero e sensibilità del ricevitore devono essere considerati insieme. Questa considerazione è chiamata budget di collegamento.

<indepth>
*Budget di downlink semplificato di un CubeSat LEO nella banda dei 2 metri*
Il termine dB (decibel) sarà trattato in dettaglio solo nel capitolo [sec:dezibel_1]. Qui è sufficiente sapere che dB rappresenta un numero di rapporto e dBm rappresenta un livello di potenza assoluto.
Un esempio molto semplificato per un downlink da un CubeSat LEO a una stazione di terra potrebbe essere così:

| Quantità | Valore di esempio |
| Frequenza | 145.9 MHz |
| Potenza di trasmissione 1 W | 30 dB<sub>m</sub>  |
| Perdite cavo TX e connettori | −1 dB |
| Guadagno antenna di trasmissione | +3 dB<sub>i</sub> |
| EIRP | +32 dB<sub>m</sub> |
| Distanza | 2000 km |
| Attenuazione spazio libero | −141.7 dB |
| Guadagno antenna di ricezione | +8 dB<sub>i</sub> |
| Preamplificatore | +15 dB |
| Perdite cavo RX e connettori | −2 dB |
| Potenza all'ingresso Rx| −88.7 dB<sub>m</sub> |
| sensibilità del ricevitore assunta | -104 dB<sub>m</sub>  |
|  |   |
| Margine di collegamento  |  +15.3 dB |

In un budget di collegamento reale, si aggiungono ulteriori fattori, ad esempio tipo di modulazione, velocità dei dati, rumore del ricevitore e rumore di fondo.
</indepth>

## Antenne e polarizzazione

Poiché il satellite si muove durante un sorvolo, cambia anche la sua direzione relativa alla stazione di terra. Per molti collegamenti satellitari vengono quindi utilizzate antenne con un guadagno adeguato e una direttività sufficiente. Con antenne più direttive, potrebbe essere necessario un inseguimento dell'antenna.

Anche la polarizzazione del segnale deve essere considerata. A causa del movimento e della posizione del satellite, l'orientamento della polarizzazione relativa alla stazione di terra può cambiare. Nella radio via satellite vengono quindi utilizzate polarizzazioni lineari o circolari a seconda dell'applicazione.

## Transponder e digipeater

I satelliti radioamatoriali possono avere diversi tipi di carichi utili radio.

Un transponder lineare riceve una banda di frequenza e la converte in un'altra banda di frequenza. Più segnali possono essere trasmessi simultaneamente all'interno della larghezza di banda del transponder disponibile. Le modalità operative tipiche sono, ad esempio, SSB e CW.

Un transponder FM, invece, lavora con segnali FM per la trasmissione simultanea di una singola conversazione.

Un digipeater riceve dati digitali e li ritrasmette secondo una procedura definita. Si differenzia quindi fondamentalmente da un transponder lineare, che converte lo spettro di frequenza ricevuto senza elaborare i singoli segnali utili come pacchetti di dati.

## Beacon satellitari

Molti satelliti radioamatoriali sono dotati di un beacon. [sec:baken] trasmettono automaticamente a intervalli regolari o continuamente segnali definiti. Possono servire per osservare la ricevibilità del satellite, le condizioni di propagazione e lo stato del carico utile radio.

Durante la ricezione di un beacon, una stazione radio può, ad esempio, determinare se il satellite è già sopra l'orizzonte, come la frequenza di ricezione cambia a causa dell'effetto Doppler e quanto bene funziona il collegamento radio.

## Tracciamento satellitare

Per la pratica del satellite radio, sono necessarie l'orbita attuale e la posizione del satellite. A questo scopo vengono utilizzati elementi orbitali, ad esempio i cosiddetti TLE (Two-Line Elements). I programmi di tracciamento calcolano da questi la posizione prevista del satellite e mostrano, tra l'altro, azimut, elevazione, AOS e LOS, nonché l'effetto Doppler previsto.

Ciò consente di pianificare i sorvoli e di inseguire automaticamente le apparecchiature radio e le antenne.

---

<tip>
Le organizzazioni AMSAT in tutto il mondo si occupano di radioamatoriale via satellite, in Svizzera è l'[AMSAT-HB](https://amsat-hb.org/).
</tip>

