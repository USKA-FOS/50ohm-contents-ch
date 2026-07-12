Ognuno ha sicuramente già sentito un amplificatore sovraeccitato o una registrazione audio sovraeccitata. Se il volume viene alzato troppo durante la registrazione o la riproduzione, possono verificarsi distorsioni.

Ad esempio, se viene applicato un segnale audio troppo forte all'ingresso di un trasmettitore, possono generarsi e essere trasmessi armoniche. Nella figura [ref:uebersteuerung_ft8] è rappresentato un segnale FT8 sovraeccitato in questo modo nel diagramma a cascata: a sinistra si vede il segnale desiderato in giallo e a destra le armoniche indesiderate.

<margin>
[picture:720:uebersteuerung_ft8:Un segnale FT8 sovraeccitato, a sinistra il segnale desiderato, a destra le armoniche indesiderate]
[photo:328:uebersteuerung_ft8_wsjtx:Un segnale FT8 sovraeccitato nel waterfall del software WSJTX]
</margin>

Si possono verificare distorsioni dovute a sovraeccitazione anche nell'amplificatore di trasmissione. Per evitarlo, molti apparecchi radio dispongono di una regolazione automatica del livello (in inglese: Automatic Level Control, ALC). Questa può intervenire riducendo l'amplificazione.

---

Nelle trasmissioni con metodi di trasmissione digitale come FT8, WSPR o RTTY con ampiezza costante, l'intervento dell'ALC è spesso un'indicazione che il segnale audio dal PC è troppo forte e viene sovraeccitato. Ciò può portare a uno *splatter* indesiderato sulla banda. Pertanto, il segnale audio in questi metodi di trasmissione deve sempre essere controllato attentamente. Una riduzione del livello da parte dell'ALC non sarebbe inizialmente critica di per sé, poiché in questi metodi l'informazione risiede nella modulazione di frequenza. Ciononostante, l'attivazione dell'ALC è un forte indizio che il segnale AF è già sovraeccitato.

<indepth>
Il [manuale](https://wsjt.sourceforge.io/wsjtx-main_en.html#TRANSCEIVER) del software WSJTX fornisce una buona raccomandazione a riguardo: nel primo passo, si dovrebbe mettere il trasmettitore-ricevitore in modalità di trasmissione premendo il tasto TUNE, per generare un tono costante. Questo tono può essere verificato ascoltandolo con la funzione monitor dell'apparecchio o controllato visivamente nel waterfall del TRX. Non dovrebbero verificarsi distorsioni, clic o altri disturbi. Successivamente, si regola lentamente il controllo PWR dal suo massimo verso il basso, finché l'uscita RF del trasmettitore non scende leggermente – questo è generalmente considerato un buon livello per la modulazione audio. Anche l'indicatore ALC e la potenza d'uscita del trasmettitore-ricevitore possono aiutare a trovare il livello ottimale del segnale AF.
</indepth>

Nei metodi di trasmissione digitale con ampiezza variabile (ad es. PSK31, QPSK, 16-QAM), tuttavia, l'ALC può portare a nuovi problemi. A seconda del volume o della frequenza, il segnale potrebbe attivare l'ALC in misura diversa in momenti diversi, modificando così indesideratamente l'ampiezza nel tempo. Ciò significa che il nostro segnale utile effettivo viene ulteriormente modulato in ampiezza. Ciò crea ulteriori componenti di frequenza che vengono trasmesse come emissioni spurie. Da un lato, ciò può disturbare altri radioamatori o servizi radio su frequenze adiacenti. Dall'altro, la decodifica nel ricevitore viene resa più difficile.

Se si verificano problemi a causa dell'ALC e quanto sono gravi, dipende da molti fattori. Oltre al metodo di trasmissione utilizzato, anche l'implementazione specifica dell'ALC nel trasmettitore-ricevitore, ad esempio in termini di tempo di reazione e di mantenimento, gioca un ruolo. Anche l'indicazione dell'ALC è diversa in vari apparecchi. Uno sguardo al manuale può fornire informazioni su quando interviene la regolazione del livello e come viene indicata. In generale, tuttavia, si può dire: se l'ALC non interviene, non crea problemi.

Ricorda: nei metodi di trasmissione digitale tramite segnale AF, è importante mantenere il livello AF così basso da evitare la sovraeccitazione e che la regolazione automatica del livello non intervenga.

[question:EJ218]
[question:EJ217]
[question:EJ219]
