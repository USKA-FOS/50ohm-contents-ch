Nella classe N abbiamo già conosciuto le emissioni indesiderate. Tali emissioni devono assolutamente essere evitate, cosa che può essere ottenuta attraverso varie misure tecniche – su queste ci soffermeremo in questa lezione. Le emissioni indesiderate nei trasmettitori radio si generano frequentemente a causa delle *armoniche superiori*, ovvero multipli interi della frequenza fondamentale, nonché delle cosiddette *emissioni spurie*, come mostrato nella figura [ref:e_unerwuenschte_aussendungen_uebersicht]. Inizialmente ci occupiamo delle armoniche superiori, poiché possono compromettere o disturbare altri servizi radio. Si parla di disturbo quando una stazione radioamatoriale irradia componenti di frequenza indesiderate in modo così forte da superare i limiti consentiti. Un esempio tipico è l'emissione di un'armonica superiore di un trasmettitore-ricevitore nella banda della radiodiffusione VHF, come illustrato nella figura [ref:e_unerwuenschte_aussendungen_oberwelle]. Qui la frequenza quadrupla ($\qty{145,9}{\mega\hertz}\cdot 4 = \qty{583,6}{\mega\hertz}$) della frequenza fondamentale causa un disturbo. Le emissioni spurie saranno trattate alla fine di questa lezione.

<margin>
[picture:1008:e_unerwuenschte_aussendungen_uebersicht:Emissioni indesiderate: Armoniche superiori (OW) ed emissioni spurie (NA)]
</margin>

<margin>
[picture:745:e_unerwuenschte_aussendungen_oberwelle:Disturbo della ricezione DVB-T2 di un televisore da parte dell'armonica superiore di un'emissione radioamatoriale]
</margin>

---

La misurazione delle emissioni indesiderate di un trasmettitore avviene – a differenza della misurazione PEP – sempre all'uscita del trasmettitore, includendo l'eventuale SWR-meter utilizzato, dispositivi di adattamento aggiuntivi ed eventuali filtri passa-basso impiegati (cfr. figura [ref:e_unerwuenschte_aussendungen_trx]).
Ciò garantisce che vengano misurate solo le emissioni indesiderate che possono effettivamente raggiungere l'antenna. Uno spettroanalizzatore è il dispositivo di misurazione più adatto a questo scopo. Come venga condotta esattamente una tale verifica, come appare lo spettro di frequenza delle armoniche superiori e quali prescrizioni legali si applichino, sarà esaminato più in dettaglio solo nella classe A.

<margin>
[picture:917:e_unerwuenschte_aussendungen_trx:Misurazione delle emissioni indesiderate]
</margin>

[question:EJ209]

Un segnale di trasmissione ideale, che trasmette solo su una frequenza desiderata, dovrebbe essere un seno ideale. Questo non contiene altre componenti di frequenza oltre alla frequenza fondamentale.

[question:EJ201]

<indepth>
Forme d'onda che non sono sinusoidali e che contengono in particolare "angoli e spigoli" netti, sono composte da molte diverse componenti di frequenza sinusoidale e contengono molte componenti armoniche superiori. In particolare, quando i trasmettitori vengono sovra-modulati, i segnali precedentemente sinusoidali vengono spesso distorti o la loro ampiezza viene tagliata. Ciò genera anche massicce componenti armoniche superiori. Ogni deviazione dalla forma sinusoidale ideale deve quindi essere evitata per segnali di trasmissione ideali. Affronteremo questo argomento più in dettaglio nella classe A. Con questo applet, tuttavia, il problema può già essere sperimentato.

[include:fourier]

</indepth>

---

Per la soppressione delle armoniche superiori, nel campo delle onde corte vengono solitamente impiegati *filtri per armoniche superiori*. La loro caratteristica è tale che le frequenze al di sotto di una determinata frequenza di taglio passano attraverso il filtro quasi senza attenuazione, mentre le frequenze al di sopra di questo limite vengono trasmesse solo in modo molto debole o per nulla. Un *filtro per armoniche superiori* è quindi un *filtro passa-basso*, come già conosciuto nel capitolo sui circuiti oscillanti. La risposta in frequenza di un tale filtro passa-basso è mostrata nella figura [ref:e_ua_tiefpass]. La figura [ref:e_ua_tiefpass_selbstbau] mostra un filtro passa-basso autocostruito composto da condensatori e bobine avvolte su nuclei toroidali. Quando si cambia banda in un trasmettitore multibanda, di solito viene selezionato anche un filtro per armoniche superiori appropriato. Spesso si sente il clic di un relè che effettua questo cambio.
Che questo argomento sia molto importante lo dimostra il gran numero di domande d'esame a riguardo. Con la conoscenza delle armoniche superiori e dei filtri passa-basso, tuttavia, queste possono essere risposte molto facilmente.

<margin>
[picture:591:e_ua_tiefpass:Risposta in frequenza di un filtro passa-basso]
</margin>

<margin>
[photo:320:e_ua_tiefpass_selbstbau:Filtro passa-basso autocostruito]
</margin>

---

[question:EJ202]
[question:EJ204]
[question:EJ205]
[question:EJ206]
[question:EJ207]
[question:EJ208]
[question:EJ203]

<indepth>
[picture:593:bandpass:Risposta in frequenza di un filtro passa-banda]

Un'altra possibilità per sopprimere le armoniche superiori è l'uso di un filtro passa-banda. I filtri passa-banda sono spesso utilizzati nei trasmettitori a banda singola e nei trasmettitori per le bande VHF/UHF/SHF. In questo caso, spesso è necessario sopprimere anche componenti del segnale che si verificano durante l'elaborazione del segnale di trasmissione e che possono trovarsi anche al di sotto della frequenza di trasmissione.
</indepth>

Come già detto, i segnali sinusoidali sono essenziali per evitare componenti armoniche superiori. Ciò si ottiene, tra l'altro, facendo lavorare le stadi del trasmettitore, in particolare gli stadi di potenza, senza distorsioni. Se si effettua una nuova regolazione del punto di funzionamento di uno stadio finale di un trasmettitore, è assolutamente necessario verificare successivamente la sua linearità e la qualità della trasmissione in termini di scarsità di armoniche superiori.

[question:EF404]

Le emissioni indesiderate possono verificarsi anche in prossimità del segnale di trasmissione effettivo (cfr. figura [ref:e_unerwuenschte_aussendungen_uebersicht]) e quindi spesso interessano altre stazioni radioamatoriali sulla stessa banda. Tali disturbi possono essere difficilmente o per nulla soppressi con i filtri e dovrebbero quindi essere evitati fin dall'inizio dell'elaborazione del segnale mediante misure appropriate. Spesso queste *emissioni spurie* – chiamate anche prodotti secondari e colloquialmente note come "splatter" – sono causate da un'impostazione troppo alta dell'amplificatore del microfono nel trasmettitore, il che allarga involontariamente il segnale di trasmissione.

[question:EJ213]
[question:EJ214]

Lo stesso vale anche per i metodi di trasmissione digitale, come ad esempio il Packet Radio. Per evitare emissioni spurie e superamenti della larghezza di banda consentita, in particolare nei trasmettitori FM modulati AFSK, è possibile limitare la deviazione o ridurre il guadagno del segnale audio.

[question:EJ212]

Anche la stabilità dell'oscillatore utilizzato nel trasmettitore può causare emissioni al di fuori dei limiti di banda o disturbare le stazioni adiacenti. Ciò è possibile in particolare nei vecchi apparecchi autocostruiti senza oscillatori stabilizzati al quarzo. I moderni trasmettitori-ricevitori per onde corte, ma anche gli attuali apparecchi autocostruiti e i kit, dispongono generalmente di oscillatori di riferimento molto stabili.

[question:EJ216]
