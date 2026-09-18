Ognuno ha sicuramente già sentito un amplificatore sovramodulato o una registrazione audio sovraeccitata. Se durante la registrazione o la riproduzione si alza troppo il volume, possono verificarsi distorsioni.

Se, ad esempio, si applica un segnale audio troppo forte all’ingresso di un trasmettitore, possono generarsi armoniche che vengono poi trasmesse. Nella figura [ref:uebersteuerung_ft8] è rappresentato un segnale FT8 sovramodulato nel diagramma a cascata: a sinistra, in giallo, è visibile il segnale desiderato e, alla sua destra, le armoniche indesiderate.

<margin>
[picture:720:uebersteuerung_ft8:Un segnale FT8 sovramodulato, a sinistra il segnale desiderato, a destra le armoniche indesiderate]
[photo:328:uebersteuerung_ft8_wsjtx:Un segnale FT8 sovramodulato nella visualizzazione a cascata del software WSJTX]
</margin>

Anche nell’amplificatore di trasmissione possono verificarsi distorsioni dovute a sovramodulazione. Per evitarlo, molti apparecchi radio dispongono di una regolazione automatica del livello (in inglese: Automatic Level Control, ALC). Essa può intervenire riducendo il guadagno.

---

Nelle trasmissioni con metodi digitali a ampiezza costante, come ad esempio FT8, WSPR o RTTY, l’intervento dell’ALC è spesso un’indicazione che il segnale audio proveniente dal PC è troppo forte e sovramodulato. Questo può portare a *splatter* indesiderati sulla banda. Pertanto, con questi metodi di trasmissione, il segnale audio deve essere sempre attentamente controllato. Una riduzione del livello da parte dell’ALC, di per sé, non sarebbe critica, poiché in questi metodi l’informazione è codificata nella modulazione a spostamento di frequenza. Tuttavia, l’attivazione dell’ALC è un forte indizio che il segnale BF è già sovramodulato.

<indepth>
Il [manuale](https://wsjt.sourceforge.io/wsjtx-main_en.html#TRANSCEIVER) del software WSJTX fornisce un’utile raccomandazione: come primo passo, premendo il tasto TUNE si deve portare il trasmettitore-ricevitore in modalità trasmissione per generare un tono uniforme. Questo tono può essere verificato uditivamente tramite la funzione di monitoraggio dell’apparecchio o controllato visivamente nella visualizzazione a cascata del trasmettitore-ricevitore. Non devono verificarsi distorsioni, clic o altri disturbi. Successivamente, si regola il controllo PWR dal suo massimo verso il basso, finché l’uscita RF del trasmettitore non inizia a diminuire leggermente: questo livello è generalmente considerato ottimale per l’eccitazione del segnale audio. Anche la visualizzazione dell’ALC e la potenza d’uscita del trasmettitore-ricevitore possono aiutare a trovare il livello ottimale del segnale BF.
</indepth>

Nei metodi di trasmissione digitali con ampiezza variabile (ad esempio PSK31, QPSK, 16-QAM), l’ALC può invece causare nuovi problemi. Il segnale, a seconda del volume o della frequenza, può attivare l’ALC in momenti diversi e con intensità variabile, modificando così l’ampiezza nel tempo. Ciò significa che il nostro segnale utile viene ulteriormente modulato in ampiezza. Di conseguenza, si generano ulteriori componenti di frequenza che vengono trasmesse come emissioni laterali. Da un lato, questo può disturbare altri radioamatori o servizi di radiocomunicazione su frequenze adiacenti. Dall’altro, la decodifica del segnale ricevuto risulta più difficile.

Se l’ALC causi problemi e quanto questi siano gravi dipende da molti fattori. Oltre al metodo di trasmissione utilizzato, anche l’implementazione concreta dell’ALC nel trasmettitore-ricevitore, ad esempio in termini di tempo di reazione e di mantenimento, gioca un ruolo importante. Anche la visualizzazione dell’ALC varia a seconda dei dispositivi. Una lettura del manuale può chiarire quando la regolazione del livello interviene e come viene indicato. In generale, tuttavia, si può affermare: se l’ALC non interviene, non crea problemi.

Regola: nei metodi di trasmissione digitali tramite segnale audio, occorre assicurarsi che il livello audio sia sufficientemente basso da evitare sovramodulazione e che la regolazione automatica del livello non intervenga.

[question:EJ218]
[question:EJ217]
[question:EJ219]
