L'idea di base dietro la telegrafia Morse, cioè trasmettere singoli caratteri di un testo, viene chiamata telegrafia e si è evoluta costantemente. Un traguardo importante è stato quello di collegare telescriventi a apparecchi radio tramite modem. In questo modo è stato inventato il radiotelescrivente, per inviare e ricevere testi in modo automatizzato via radio. L'acronimo RTTY, derivante dall'inglese *radio teletype*, è ancora oggi utilizzato come denominazione. Oggi il computer ha generalmente preso il posto del radiotelescrivente. Con esso, oltre al classico metodo RTTY, si possono utilizzare molti altri metodi di trasmissione digitale, noti anche come *Digimodes*.


<indepth>
Un *telescrivente* è un apparecchio per trasmettere messaggi in forma testuale tramite segnali elettrici.
</indepth>

<margin>
[photo:92:n_computersteuerung_funkfernschreiber:Radiotelescrivente]
</margin>

---

Per prima cosa, un computer adatto deve essere collegato all'apparecchio radio. Il collegamento può avvenire, nel caso più semplice, direttamente tramite la presa audio o l'interfaccia USB. In generale, sono necessarie una connessione audio e, eventualmente, segnali di comando. Nella figura [ref:n_computersteuerung_verbindungen] sono illustrate alcune varianti. Una porta spesso presente nei trasmettitori-ricevitori per i segnali di comando è la cosiddetta interfaccia CAT. CAT sta per *Computer Aided Tuning* o *Computer Aided Transceiver*. Tramite questa interfaccia puoi controllare il trasmettitore-ricevitore e interrogare valori, ad esempio frequenza, potenza di trasmissione e stato del PTT.


<margin>
[picture:630:n_computersteuerung_verbindungen:Esempi di collegamenti tra computer e apparecchio radio]
</margin>

Collegando il computer al trasmettitore-ricevitore, tuttavia, possono verificarsi disturbi dei segnali trasmessi o retroazioni dell'apparecchio radio sul PC. Varie interfacce *Digimode* come soluzione hardware semplificano il collegamento e includono misure contro tali problemi. Tali interfacce possono essere utilizzate anche per altri scopi, ad esempio per il funzionamento remoto o per registrare il traffico radio con software appropriato. Per alcuni metodi esistono anche modem hardware in cui la conversione tra dati e segnali audio avviene in un apparecchio separato.

[question:NF114]
[question:NF116]

Ci sono anche altri effetti indesiderati. Il computer potrebbe attivare inaspettatamente la trasmissione o emettere suoni di notifica di altri programmi in esecuzione. A volte, ad esempio, si sente come altri radioamatori trasmettano accidentalmente il suono di avvio del sistema operativo. Se l'apparecchio radio trasmette inaspettatamente, potrebbero essere messi in pericolo persone che stanno lavorando sull'impianto d'antenna o si trovano accidentalmente nelle sue immediate vicinanze.

[question:NF117]

---

Per alcuni metodi di trasmissione, la presa del microfono dell'apparecchio radio non è adatta, poiché gli stadi di amplificazione e filtraggio successivi sono ottimizzati per la voce e trattano toni più alti o più bassi in modo diverso. Per questo motivo, gli apparecchi radio dispongono spesso di una propria porta dati analogica, contrassegnata ad esempio con *DATA* o *9600*. Utilizzando questa porta specifica, vengono bypassati determinati stadi di amplificazione e filtraggio e i segnali vengono trasmessi con la minor distorsione possibile.

<indepth>
La denominazione *9600* deriva dal fatto che questa porta era stata introdotta per il Packet-Radio, ampiamente utilizzato in passato, per trasmettere dati a $\qty{9600}{\baud}$. Oggi questa porta viene utilizzata, ad esempio, per la trasmissione digitale della voce ed è talvolta impiegata anche a velocità più elevate.
</indepth>

[question:NF115]
