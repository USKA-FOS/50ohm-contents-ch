Nel capitolo [sec:unerwuenschte_aussendungen_1] abbiamo già affrontato le emissioni indesiderate. Queste emissioni devono essere assolutamente evitate e ciò può essere ottenuto con diverse misure tecniche – su queste ci soffermeremo in questa lezione. Le emissioni indesiderate nei trasmettitori radio sono spesso causate da *armoniche*, cioè multipli interi della frequenza fondamentale, nonché da cosiddette *emissioni secondarie*, come mostrato nella figura [ref:e_unerwuenschte_aussendungen_uebersicht]. Iniziamo con le armoniche, poiché possono disturbare o interferire con altri servizi di radiocomunicazione. Si parla di disturbo quando una stazione di radioamatore emette componenti di frequenza indesiderate in modo tale da superare i valori limite consentiti. Un esempio tipico è l'emissione di un'onda armonica di un ricetrasmettitore nella banda di radiodiffusione FM, come illustrato nella figura [ref:e_unerwuenschte_aussendungen_oberwelle]. In questo caso, la frequenza quadrupla ($\qty{145,9}{\mega\hertz}\cdot 4 = \qty{583,6}{\mega\hertz}$) della frequenza fondamentale causa un disturbo. Le emissioni secondarie verranno trattate alla fine di questa lezione.

<margin>
[picture:1008:e_unerwuenschte_aussendungen_uebersicht:Emissioni indesiderate causate da armoniche (OW) e emissioni secondarie (NA)]
</margin>

<margin>
[picture:745:e_unerwuenschte_aussendungen_oberwelle:Disturbo della ricezione DVB-T2 di un televisore causato dall'armonica superiore di una trasmissione radioamatoriale]
</margin>

---

La misurazione delle emissioni indesiderate di un trasmettitore avviene – a differenza della misurazione della PEP – sempre all'uscita del trasmettitore, includendo l'eventuale uso di un ROSmetro, dispositivi di adattamento aggiuntivi e filtri passa-basso utilizzati (cfr. figura [ref:e_unerwuenschte_aussendungen_trx]).
In questo modo si garantisce che vengano misurate solo le emissioni indesiderate che possono effettivamente raggiungere l'antenna. Lo strumento più adatto per questa misurazione è uno analizzatore di spettro. Come venga eseguita questa verifica, come si presenti lo spettro di frequenza delle armoniche e quali siano i requisiti legali verranno trattati solo nel corso di classe A.

<margin>
[picture:917:e_unerwuenschte_aussendungen_trx:Misurazione delle emissioni indesiderate]
</margin>

[question:EJ209]

Un segnale di trasmissione ideale, che trasmette solo su una frequenza desiderata, dovrebbe essere un seno perfetto. Questo contiene, oltre alla frequenza fondamentale, nessun'altra componente di frequenza.

[question:EJ201]

<indepth>
Le forme d'onda che non sono sinusoidali e che presentano in particolare spigoli vivi e angoli acuti sono composte da molte diverse componenti di frequenza sinusoidali e contengono molte armoniche. In particolare, quando i trasmettitori sono sovramodulati, i segnali precedentemente sinusoidali vengono spesso distorti o limitati in ampiezza. Ciò comporta anche la formazione di armoniche significative. Ogni deviazione dalla forma sinusoidale ideale deve quindi essere evitata nei segnali di trasmissione ideali. Questo argomento verrà approfondito nel corso di classe A. Tuttavia, con questo applet è già possibile sperimentare la situazione.
[include:fourier]

</indepth>

---

Per la soppressione delle armoniche, nella banda delle onde corte vengono generalmente utilizzati *filtri per armoniche*. La loro caratteristica è progettata in modo che le frequenze al di sotto di una certa frequenza di taglio passino attraverso il filtro quasi senza attenuazione, mentre le frequenze al di sopra di questa soglia non vengano fatte passare o vengano fortemente attenuate. Un *filtro per armoniche* è quindi un *filtro passa-basso*, come quelli che abbiamo già conosciuto nel capitolo sui circuiti oscillanti. La risposta in frequenza di un tale filtro passa-basso è mostrata nella figura [ref:e_ua_tiefpass]. La figura [ref:e_ua_tiefpass_selbstbau] mostra un filtro passa-basso autocostruito composto da condensatori e induttanze avvolte su nuclei toroidali. Quando si passa da una banda all'altra in un trasmettitore multibanda, di solito viene selezionato anche un filtro per armoniche adatto. Spesso si sente il clic di un relè che esegue questa commutazione.

L'importanza di questo argomento è dimostrata dal gran numero di domande d'esame a riguardo. Tuttavia, con le conoscenze sulle armoniche e sui filtri passa-basso, queste domande possono essere facilmente risolte.

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

Un'altra possibilità per sopprimere le armoniche è l'impiego di un filtro passa-banda. I filtri passa-banda vengono spesso utilizzati nei trasmettitori a singola banda e nei trasmettitori per le bande VHF/UHF/SHF. In questi casi, è necessario spesso sopprimere anche le componenti di segnale che si formano all'interno della preparazione del segnale di trasmissione e che possono trovarsi anche al di sotto della frequenza di trasmissione.
</indepth>

Come già menzionato in precedenza, i segnali sinusoidali sono essenziali per evitare componenti armoniche. Questo viene ottenuto, tra l'altro, facendo lavorare gli stadi del trasmettitore, in particolare gli stadi finali di potenza, in modo lineare. Se viene regolato il punto di lavoro di uno stadio finale di un trasmettitore, è necessario verificare la linearità e la qualità della trasmissione in termini di assenza di armoniche.

[question:EF404]

Le emissioni indesiderate possono verificarsi anche in prossimità del segnale di trasmissione vero e proprio (cfr. figura [ref:e_unerwuenschte_aussendungen_uebersicht]) e quindi spesso disturbano altri radioamatori sulla stessa banda. Tali disturbi possono essere difficilmente o per nulla soppressi con i filtri e dovrebbero quindi essere evitati già nella fase iniziale della preparazione del segnale con misure adeguate. Spesso questi *prodotti secondari* – anche chiamati prodotti di intermodulazione e comunemente indicati come "splatter" – sono causati da un'impostazione troppo elevata dell'amplificatore del microfono nel trasmettitore, che provoca un allargamento indesiderato del segnale di trasmissione.

[question:EJ213]
[question:EJ214]

Lo stesso vale anche per i metodi di trasmissione digitali, come ad esempio il Packet Radio. Per evitare prodotti secondari e il superamento della larghezza di banda consentita, in particolare nei trasmettitori FM modulati AFSK, è possibile limitare la deviazione o ridurre l'uscita BF.

[question:EJ212]

Anche la stabilità dell'oscillatore utilizzato nel trasmettitore può causare emissioni al di fuori dei limiti di banda o disturbare stazioni vicine. Questo è possibile soprattutto nei vecchi apparecchi autocostruiti privi di oscillatori stabilizzati al quarzo. I moderni ricetrasmettitori per onde corte, ma anche i dispositivi autocostruiti e i kit attuali, dispongono generalmente di oscillatori di riferimento molto stabili.

[question:EJ216]