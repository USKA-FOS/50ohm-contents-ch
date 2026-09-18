Nella comunicazione senza fili, diverse tecniche di accesso svolgono un ruolo centrale per consentire a più utenti di utilizzare contemporaneamente uno spettro di frequenze condiviso. I metodi più comuni sono la multiplazione di frequenza (FDMA), la multiplazione a divisione di tempo (TDMA) e la tecnica di multiplazione a codice (CDMA). Ognuna di queste tecniche suddivide lo spettro di frequenza in modo diverso, al fine di minimizzare le interferenze e garantire una trasmissione efficiente. La scelta del metodo dipende dalle esigenze specifiche in termini di larghezza di banda, numero di utenti e suscettibilità alle interferenze. Di seguito vengono descritte le differenze tra questi metodi.

---

Nella tecnica di multiplazione di frequenza (FDMA – Frequency Division Multiple Access), la banda di frequenza disponibile viene suddivisa in più canali di frequenza separati tra loro (cfr. figura [ref:e_fdma]). A ogni canale viene assegnato in modo permanente un singolo utente, consentendo così l’utilizzo simultaneo del sistema da parte di più partecipanti. La separazione degli utenti avviene esclusivamente tramite frequenze diverse, evitando che i segnali dei singoli partecipanti si disturbino a vicenda, purché siano rispettati gli intervalli tra i canali. FDMA è un metodo tecnicamente semplice e consolidato da molti anni, particolarmente adatto a sistemi con pochi utenti e basse esigenze di interferenza. Uno svantaggio consiste tuttavia nella minore efficienza in termini di larghezza di banda quando il numero di utenti è elevato, poiché a ogni partecipante viene riservata in modo permanente una propria porzione di frequenza, anche quando non trasmette dati per un certo periodo. Esempi tipici di applicazione di FDMA sono i primi sistemi di telefonia mobile analogica come AMPS (Advanced Mobile Phone Service) negli USA o GSM (Global System for Mobile Communications) in Europa, nonché varie forme di comunicazione satellitare.

[question:EE410]

<margin>
[picture:845:e_fdma:Multiplazione di frequenza]
</margin>

---

Nella tecnica di multiplazione a divisione di tempo (TDMA – Time Division Multiple Access), più utenti condividono lo stesso canale di frequenza, accedendovi in modo sequenziale. A ogni utente vengono assegnati intervalli temporali definiti, detti *time slot*, durante i quali può trasmettere e ricevere (cfr. figura [ref:e_tdma]). Questa separazione temporale delle trasmissioni impedisce che i segnali dei singoli utenti si sovrappongano o si disturbino reciprocamente.

TDMA consente un utilizzo relativamente efficiente delle risorse di frequenza disponibili, soprattutto in sistemi con molti utenti e un elevato volume di dati. Tuttavia, per il corretto funzionamento è necessaria una sincronizzazione temporale molto precisa tra tutti i partecipanti, il che aumenta la complessità tecnica e il costo del sistema. Esempi noti di applicazione di TDMA sono il sistema di telefonia mobile GSM di seconda generazione, il sistema telefonico cordless DECT e, nel radioamatoriale, il DMR.

[question:EE409]

<margin>
[picture:844:e_tdma:Multiplazione a divisione di tempo]
</margin>

---

Nella tecnica di multiplazione a codice (CDMA – Code Division Multiple Access), tutti gli utenti utilizzano contemporaneamente la stessa banda di frequenza e lo stesso intervallo di tempo. La separazione dei singoli utenti non avviene tramite frequenza o tempo, ma tramite codici di spreading individuali (cfr. figura [ref:e_cdma]). A ogni utente viene assegnato un proprio codice, con cui il suo segnale viene modulato. Questi codici sono scelti in modo che i segnali sovrapposti possano essere separati al ricevitore, nonostante vengano trasmessi contemporaneamente nella stessa banda di frequenza. CDMA si distingue per un’elevata flessibilità e una grande capacità del sistema, poiché molti utenti possono essere attivi contemporaneamente. Inoltre, il metodo è molto robusto nei confronti di disturbi e della propagazione per cammini multipli. Tuttavia, richiede una complessa elaborazione del segnale e requisiti hardware più elevati, soprattutto in presenza di un gran numero di utenti attivi. Esempi tipici di applicazione di CDMA sono i sistemi di telefonia mobile di terza generazione come UMTS e il sistema di navigazione satellitare GPS.

[question:EE411]

<margin>
[picture:846:e_cdma:Multiplazione a codice]
</margin>

In sintesi, FDMA rappresenta il metodo più semplice, mentre TDMA e CDMA diventano via via più efficienti e complessi, soprattutto quando si utilizzano bande di frequenza limitate e un elevato numero di utenti. CDMA offre la maggiore flessibilità, ma richiede anche la tecnologia più sofisticata per la sua implementazione.