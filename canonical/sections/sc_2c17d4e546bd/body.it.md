L'idea di base della telegrafia in codice Morse, ovvero trasmettere singoli caratteri di un testo, è chiamata telegrafia ed è stata continuamente sviluppata. Una pietra miliare è stata il collegamento di telescriventi a radio tramite modem. In questo modo è stato inventato il telescrivente radio per inviare e ricevere testi via radio in modo automatizzato. L'abbreviazione RTTY del termine inglese radio teletype si ritrova ancora oggi come denominazione. Oggi, il computer ha generalmente assunto il compito del telescrivente radio. Oltre alla classica procedura RTTY, è possibile utilizzare molti altri metodi di trasmissione digitale, definiti anche modi digitali.

<indepth>
Un *telescrivente* è un apparecchio per trasmettere messaggi in forma testuale tramite segnali elettrici.
</indepth>

<margin>
[photo:92:n_computersteuerung_funkfernschreiber:Telescrivente radio controllato da computer]
</margin>

---

Innanzitutto, un computer adatto deve essere collegato all'apparecchio radio. Nel caso più semplice, il collegamento può avvenire direttamente tramite l'ingresso audio o l'interfaccia USB. Fondamentalmente è necessaria una connessione audio e, se necessario, segnali di controllo. La figura [ref:n_computersteuerung_verbindungen] mostra alcune varianti. Una connessione per segnali di controllo spesso presente sui trasmettitori-ricevitori è la cosiddetta interfaccia CAT. CAT sta per Computer Aided Tuning o Computer Aided Transceiver. Tramite questa interfaccia è possibile controllare il trasmettitore-ricevitore e interrogare valori, ad esempio Frequenza, potenza di trasmissione e stato PTT.

<margin>
[picture:630:n_computersteuerung_verbindungen:Esempi di collegamenti tra computer e apparecchio radio]
</margin>

Tuttavia, il collegamento tra computer e trasmettitore-ricevitore può causare disturbi ai segnali trasmessi o ripercussioni dell'apparecchio radio sul PC. Diverse interfacce per modi digitali come soluzione hardware semplificano il collegamento e includono misure contro tali problemi. Tali interfacce possono essere utilizzate anche per altri scopi, ad esempio per il funzionamento remoto o per registrare il traffico radio con software appropriato. Per alcune procedure esistono anche modem hardware, in cui la conversione tra dati e segnali audio avviene in un apparecchio separato.

[question:NF114]
[question:NF116]

Ci sono anche altri effetti indesiderati. Il computer potrebbe passare inaspettatamente in trasmissione o emettere suoni di notifica da altri programmi in esecuzione. A volte si sente, ad esempio, altri radioamatori trasmettere accidentalmente il suono di avvio del sistema operativo. Se l'apparecchio radio trasmette inaspettatamente, le persone che lavorano all'impianto dell'antenna o che si trovano nelle immediate vicinanze potrebbero essere messe in pericolo.

[question:NF117]

---

Per alcune procedure di trasmissione, l'ingresso microfonico dell'apparecchio radio è inadatto, poiché gli stadi di amplificazione e filtraggio successivi sono ottimizzati per la voce e toni di diversa altezza o profondità vengono trattati in modo diverso. Pertanto, gli apparecchi radio hanno spesso un proprio ingresso dati analogico, contrassegnato ad esempio con DATA o 9600. Utilizzando questo ingresso speciale, alcuni stadi di amplificazione e filtraggio vengono bypassati e i segnali vengono trasmessi nel modo più privo di distorsioni possibile.

<indepth>
La denominazione *9600* deriva dal fatto che questo ingresso è stato introdotto per il Packet Radio, molto utilizzato in passato, in modo da poter trasmettere dati a $\qty{9600}{\baud}$. Oggi l'ingresso viene utilizzato, ad esempio, per la trasmissione vocale digitale e talvolta viene utilizzato anche a velocità più elevate.
</indepth>

[question:NF115]
