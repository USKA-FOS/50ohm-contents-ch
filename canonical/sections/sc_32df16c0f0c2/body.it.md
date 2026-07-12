Nella comunicazione wireless, diverse procedure di accesso svolgono un ruolo centrale per consentire a più utenti di utilizzare contemporaneamente uno spettro di frequenza comune. Le procedure più comuni sono il multiplexing a divisione di frequenza (FDMA), il multiplexing a divisione di tempo (TDMA) e il multiplexing a divisione di codice (CDMA). Ciascuna di queste procedure divide lo spettro di frequenza in modi diversi per minimizzare le interferenze e garantire una trasmissione efficiente. La scelta della procedura dipende dai requisiti specifici di larghezza di banda, numero di utenti e suscettibilità alle interferenze. Di seguito vengono descritte le differenze tra queste procedure.

---

Nella procedura di multiplexing a divisione di frequenza (FDMA – Frequency Division Multiple Access), la banda di frequenza disponibile viene suddivisa in diversi canali di frequenza separati (cfr. figura [ref:e_fdma]). Ciascuno di questi canali viene assegnato in modo fisso a un singolo utente, consentendo l'uso simultaneo del sistema da parte di più partecipanti. La separazione degli utenti avviene esclusivamente tramite frequenze diverse, il che impedisce ai segnali dei singoli partecipanti di interferire tra loro, purché vengano rispettate le distanze tra i canali. FDMA è una procedura tecnicamente semplice e consolidata da molti anni, particolarmente adatta per sistemi con pochi utenti e basso fabbisogno di interferenza. Uno svantaggio, tuttavia, è la relativamente scarsa efficienza della larghezza di banda con un gran numero di utenti, poiché a ciascun partecipante viene riservato permanentemente un proprio intervallo di frequenza, anche se in quel momento non trasmette dati. Esempi tipici di applicazione per FDMA sono i primi sistemi di telefonia mobile analogica come AMPS (Advanced Mobile Phone Service) negli USA o GSM (Global System for Mobile Communications) in Europa, nonché varie forme di comunicazione satellitare.

[question:EE410]

<margin>
[picture:845:e_fdma:Frequenzmultiplexing]
</margin>

---

Nella procedura di multiplexing a divisione di tempo (TDMA – Time Division Multiple Access), più partecipanti utilizzano lo stesso canale di frequenza, condividendo l'accesso nel tempo. A ciascun utente vengono assegnati intervalli di tempo definiti, chiamati time slot, durante i quali può trasmettere e ricevere (cfr. figura [ref:e_tdma]). Questa separazione temporale delle trasmissioni impedisce che i segnali dei singoli partecipanti si sovrappongano o interferiscano tra loro.

TDMA consente un utilizzo relativamente efficiente delle risorse di frequenza disponibili, in particolare nei sistemi con molti utenti e un elevato volume di dati. Tuttavia, un prerequisito per il funzionamento senza problemi è una sincronizzazione temporale molto precisa di tutti i partecipanti, il che aumenta la complessità tecnica e del sistema. Esempi noti di applicazione per TDMA sono il sistema di telefonia mobile GSM di seconda generazione, il sistema telefonico cordless DECT e, nel radioamatore, DMR.

[question:EE409]

<margin>
[picture:844:e_tdma:Zeitmultiplexing]
</margin>

---

Nella procedura di multiplexing a divisione di codice (CDMA – Code Division Multiple Access), tutti i partecipanti utilizzano contemporaneamente la stessa banda di frequenza e lo stesso tempo. La separazione dei singoli utenti non avviene tramite frequenza o tempo, ma tramite codici di diffusione individuali (cfr. figura [ref:e_cdma]). A ciascun utente viene assegnato un codice proprio con cui viene modulato il suo segnale. Questi codici sono scelti in modo tale che i segnali sovrapposti possano essere nuovamente separati dal ricevitore, sebbene vengano trasmessi contemporaneamente nella stessa banda di frequenza. CDMA si distingue per un'elevata flessibilità e una grande capacità di sistema, poiché molti utenti possono essere attivi contemporaneamente. Inoltre, la procedura è molto robusta contro interferenze e propagazione multi-percorso. A ciò si contrappongono tuttavia un'elaborazione del segnale relativamente complessa e requisiti hardware maggiori, soprattutto con un gran numero di partecipanti attivi. Esempi tipici di applicazione per CDMA sono i sistemi di telefonia mobile di terza generazione come UMTS e il sistema di navigazione satellitare GPS.

[question:EE411]

<margin>
[picture:846:e_cdma:Codemultiplexing]  
</margin>

In sintesi, FDMA è il metodo più semplice, mentre TDMA e CDMA diventano sempre più efficienti e complessi, soprattutto nell'uso di larghezze di banda limitate e con un elevato numero di utenti. CDMA offre la massima flessibilità, ma richiede anche la tecnologia più complessa per l'implementazione.
