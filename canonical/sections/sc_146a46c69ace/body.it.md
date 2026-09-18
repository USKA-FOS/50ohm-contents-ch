Una "radiofaro" (in inglese: *beacon*) è un impianto trasmittente radioamatoriale che funziona automaticamente e trasmette in modo continuo o a intervalli regolari segnali definiti. Essa serve in particolare per monitorare le condizioni di propagazione, valutare la ricezione e per misurazioni tecniche. I radiofari esistono anche a bordo di satelliti radioamatoriali. Nei satelliti radioamatoriali, i radiofari hanno spesso anche una funzione importante per l'identificazione e il monitoraggio del [sec:satelliten] e per la trasmissione di telemetria.

I radiofari trasmettono generalmente su una frequenza prestabilita e possono essere installati in posizioni fisse o su piattaforme mobili, ad esempio satelliti. Poiché la loro ricezione dipende fortemente dalle mutevoli condizioni di propagazione della rispettiva banda radio, un radiofaro può fungere da indicatore delle condizioni attuali di propagazione lungo il percorso tra il radiofaro e il punto di ricezione.

Se, ad esempio, su onde corte si riceve bene un radiofaro dal Sud America, questo è un indizio che le condizioni di propagazione per i collegamenti radio in quella direzione potrebbero essere favorevoli.

I radiofari *Aurora* nella banda VHF possono indicare se al momento è presente una propagazione *Aurora* e quindi se sono possibili collegamenti DX in direzione della Scandinavia. Con radiofari noti nelle bande VHF, UHF e SHF, è possibile verificare l'impianto di ricezione e accertare se un'antenna direzionale è correttamente orientata. I radiofari servono anche per controllare la sensibilità del ricevitore, il livello del segnale e la precisione della frequenza.

<indepth>
Altre possibilità per monitorare le condizioni di propagazione

Oltre ai radiofari, oggi esistono altri sistemi per monitorare le condizioni attuali di propagazione. Tra questi vi sono, ad esempio:

- [PSK Reporter](https://pskreporter.info/pskmap.html) e
- [Reverse Beacon Network](https://www.reversebeacon.net/).

Questi sistemi non sono radiofari. Essi raccolgono automaticamente rapporti di ricezione o informazioni su trasmissioni rilevate da stazioni radioamatoriali e le visualizzano quasi in tempo reale su una mappa.

Anche [WSPR](https://www.wsprnet.org/) viene spesso utilizzato per studiare le condizioni di propagazione. In questo caso, vengono trasmessi segnali molto deboli e standardizzati, che vengono ricevuti ed elaborati da numerose stazioni riceventi automatiche.

Una descrizione dettagliata di questi sistemi andrebbe oltre l'ambito di questo capitolo. Tuttavia, nel pratico funzionamento radio sono utili integrazioni per monitorare le condizioni attuali di propagazione.
</indepth>

<tip>
Dove trovare i *radiofari VHF, UHF e SHF*?

Per la Svizzera, l'USKA offre una [panoramica delle frequenze dei radiofari](https://uska.ch/wp-content/uploads/2026/03/251116-Baken-Schweiz.pdf).
</tip>

[question:BE409]

---

Il progetto internazionale dei radiofari [IBP](https://www.ncdxf.org/beacon/) consiste in un numero elevato di radiofari distribuiti in diversi paesi su tutti i continenti. I singoli radiofari trasmettono in sequenza a intervalli prestabiliti sulle cinque frequenze IBP, utilizzando ciascuna frequenza per circa 10 secondi. In questo modo è possibile valutare rapidamente quanto siano buone le condizioni attuali di propagazione sulla rispettiva banda.

Nei piani di banda IARU sono previsti specifici banda di frequenza per i radiofari. Queste bande di frequenza dei radiofari non devono essere utilizzate per traffico radio normale. Nella tabella [ref:n_baken_frequenzbereiche] sono elencate le bande di frequenza dei radiofari delle bande ad onde corte previste nel piano di banda IARU-Regione 1.

<margin>
*Bande di frequenza dei radiofari delle bande ad onde corte*

| l: Banda | X: Banda di frequenza | Frequenza IBP |
| $\qty{10}{\meter}$ | $\qtyrange{28190}{28225}{\kilo\hertz}$ | $\qty{28.200}{\mega\hertz}$ |
| $\qty{12}{\meter}$ | $\qtyrange{24929}{24931}{\kilo\hertz}$ | $\qty{24.930}{\mega\hertz}$ |
| $\qty{15}{\meter}$ | $\qtyrange{21149}{21151}{\kilo\hertz}$ | $\qty{21.150}{\mega\hertz}$ |
| $\qty{17}{\meter}$ | $\qtyrange{18109}{18111}{\kilo\hertz}$ | $\qty{18.110}{\mega\hertz}$ |
| $\qty{20}{\meter}$ | $\qtyrange{14099}{14101}{\kilo\hertz}$ | $\qty{14.100}{\mega\hertz}$ |
[table:n_baken_frequenzbereiche:Bande di frequenza dei radiofari secondo il piano di banda IARU e frequenze IBP]
</margin>

% [question:BE410]
% [question:VD119]

% Modifiche nella revisione
% Correzioni di errori e precisazioni
% Approfondimento su Reverse Beacon Network, pskreporter e WSPR