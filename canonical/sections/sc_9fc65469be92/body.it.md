<margin>
[include:hamnet_map]
</margin>

Nel capitolo [sec:linkstrecken] abbiamo appreso le basi dei collegamenti punto a punto e le relative normative dell'UFCOM. Qui si tratta ora specificamente della tecnologia di HAMNET.

HAMNET svolge un ruolo speciale nel radioamatorismo: è una rete riservata esclusivamente ai radioamatori. HAMNET (Highspeed Amateurradio Multimedia Network) è una rete basata su IP sviluppata e gestita da radioamatori. Nel suo funzionamento, assomiglia a Internet, ma utilizza prevalentemente collegamenti radio per la trasmissione dei dati.

Originariamente, HAMNET è stato concepito come sostituto graduale della rete Packet-Radio esistente dagli anni '80 e l'ha ormai quasi completamente sostituita. Le veloci connessioni dati tra i singoli punti di accesso e nodi sono realizzate principalmente attraverso le bande delle microonde di 6 cm, 9 cm e 13 cm. Per accedere a HAMNET, è necessaria la visibilità libera verso un nodo HAMNET con accesso utente e un adeguato trasmettitore-ricevitore WLAN con antenna direzionale.

---

<margin>
Il [*SWISS-ARTG*](https://www.swiss-artg.ch/index.php?id=9) offre ai suoi membri un accesso VPN tramite la cosiddetta [HAMCloud](https://www.swiss-artg.ch/index.php?id=37). Ciò consente l'accesso a HAMNET, anche quando non è possibile un accesso diretto via radio.   

[Diventa ora membro dell'USKA!](https://uska.ch/de/uska-beitreten/)
</margin>

Si può utilizzare Hamnet proprio come Internet, nel caso più semplice con un browser web. Ciò è possibile perché il cosiddetto protocollo Internet (IP) e tutto ciò che vi si basa, può essere utilizzato anche per scopi diversi da Internet.

[question:EE414]

Hamnet, proprio come Internet, è un insieme di molte singole reti. Se due partecipanti non possono raggiungersi direttamente, i pacchetti di dati vengono instradati di conseguenza attraverso altri nodi.

[question:EE412]

In strutture così grandi, si crea ordine numerando tutti i computer. I numeri dei partecipanti sono chiamati indirizzi IP. Esistono le versioni IPv4 e IPv6. Per il nostro hobby, di solito è sufficiente occuparsi della versione più semplice, la 4.

Gli indirizzi IPv4 sono numeri binari con una lunghezza di 32 bit. Vengono scritti come quattro numeri decimali, ognuno dei quali rappresenta 8 bit, separati da punti. Il numero massimo possibile è 255, corrispondente al numero binario 11111111.

Per tutti i computer che si trovano nella stessa rete, l'inizio degli indirizzi IP è lo stesso. Questa parte di rete ha una lunghezza variabile. Le reti grandi necessitano di molti dei 32 bit per numerare i loro computer nella parte cosiddetta host alla fine. Per questo utilizzano una parte di rete più corta. Per le reti piccole è esattamente il contrario. Questo principio è noto dalla rete telefonica. Le città più grandi hanno prefissi a tre cifre, ad esempio 089, e le piccole reti locali hanno prefissi a cinque o sei cifre come 038725.

---

La lunghezza della parte di rete si indica più semplicemente con una barra dopo l'indirizzo IP. 141.17.5.18/24 significa, ad esempio, che la parte di rete è lunga 24 bit. Per tutti i computer nella stessa rete, l'indirizzo inizia con 141.17.5. Per numerare tutte le stazioni rimangono solo 8 dei 32 bit. Si tratta quindi di una rete relativamente piccola.

<indepth>
A volte le reti vengono assegnate a una cosiddetta classe, anche se questo sistema è stato abolito da tempo. Classe A significava /8, Classe B /16 e Classe C /24.
</indepth>
%TODO Aggiungere Classless Inter-Domain Routing (CIDR) come approfondimento.

---

La maggior parte dei dispositivi di rete richiede una notazione diversa, cioè la subnet mask (vedi figura [ref:netzmaske]). Sono 32 bit nella stessa notazione degli indirizzi IP. I bit che rappresentano la parte di rete sono contrassegnati con un 1 e i bit della parte host con uno 0. La maschera di rete inizia quindi con tanti uno quanti sono i bit della parte di rete. Il resto viene riempito con zeri. Le reti domestiche e le piccole reti aziendali utilizzano quasi sempre la maschera di rete 255.255.255.0, che significa la stessa cosa di /24.

I dispositivi di rete possono comunicare direttamente tra loro solo all'interno della propria rete locale. Lo riconoscono dal fatto che dalla propria combinazione di indirizzo IP e subnet mask risulta la stessa parte di rete del partner. In tutti gli altri casi, inviano i dati a un router. Questa è una stazione intermedia che collega due o più reti. Se un dispositivo è direttamente connesso a più reti, ha un proprio indirizzo IP in ciascuna.

<margin>
[picture:699:netzmaske:Indirizzo IPv4 e maschera di rete in notazione decimale e binaria]
</margin>

<margin>
[picture:706:netzwerk:Sezione di un'infrastruttura di rete]
</margin>

Tutti i partecipanti di una rete dovrebbero poter utilizzare il router quasi simultaneamente. Pertanto, nelle reti IP non vengono stabilite linee fisse. Invece, i computer suddividono tutti i flussi di dati in pacchetti, cioè in brevi segmenti. L'instradamento di questi singoli pacchetti è chiamato commutazione di pacchetto.

[question:EE413]
