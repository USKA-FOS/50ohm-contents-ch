<margin>
[include:hamnet_map]
</margin>

Nel capitolo [sec:linkstrecken] abbiamo appreso le basi delle tratte di collegamento e le relative normative del BAKOM. Ora ci concentreremo sulla tecnologia di HAMNET.

Una particolare importanza nel radioamatoriale riveste HAMNET – una rete riservata esclusivamente ai radioamatori. HAMNET (Highspeed Amateurradio Multimedia Network) è una rete IP sviluppata e gestita da radioamatori. Funziona in modo simile a Internet, ma utilizza prevalentemente collegamenti radio per la trasmissione dei dati.

Inizialmente, HAMNET è stato concepito come sostituzione graduale della rete Packet Radio, esistente sin dagli anni '80, e oggi l'ha quasi completamente sostituita. I collegamenti dati ad alta velocità tra i singoli punti di accesso e nodi vengono realizzati principalmente tramite le bande delle microonde da 6 cm, 9 cm e 13 cm. Per accedere a HAMNET è necessario avere una linea di vista verso un nodo HAMNET con accesso utente, nonché un trasmettitore-ricevitore WLAN adatto con antenna direzionale.

---

<margin>
Il [*SWISS-ARTG*](https://www.swiss-artg.ch/index.php?id=9) offre ai propri membri un accesso VPN tramite le cosiddette [HAMCloud](https://www.swiss-artg.ch/index.php?id=37). Questo consente l'accesso a HAMNET anche in assenza di un collegamento radio diretto.

[Ora diventa membro dell'USKA!](https://uska.ch/wieso-uska-mitglied-werden/)
</margin>

HAMNET può essere utilizzato allo stesso modo di Internet, ad esempio con un browser web. Questo è possibile perché il protocollo Internet (IP) e tutto ciò che si basa su di esso può essere impiegato anche per scopi diversi da Internet.

[question:EE414]

HAMNET, come Internet, è una rete composta da molte reti individuali. Se due partecipanti non possono comunicare direttamente, i pacchetti di dati vengono inoltrati tramite altri nodi.

[question:EE412]

In reti così estese si crea ordine numerando tutti i computer. I numeri dei partecipanti sono chiamati indirizzi IP. Esistono le versioni IPv4 e IPv6. Per il nostro hobby è sufficiente occuparsi della versione più semplice, IPv4.

Gli indirizzi IPv4 sono numeri binari con una lunghezza di 32 bit. Vengono scritti come quattro numeri decimali, ciascuno dei quali rappresenta 8 bit, separati da punti. Il numero massimo possibile è 255, corrispondente al numero binario 11111111.

In tutti i computer che si trovano nella stessa rete, l'inizio degli indirizzi IP è identico. Questa parte di rete ha una lunghezza variabile. Le reti più grandi necessitano di molti dei 32 bit per numerare i computer nella cosiddetta parte host. Per questo utilizzano una parte di rete più corta. Nelle reti piccole avviene il contrario. Questo principio è noto anche dalla rete telefonica. Le città più grandi hanno prefissi a tre cifre, ad esempio 089, mentre le reti locali più piccole hanno prefissi a cinque o sei cifre come 038725.

---

La lunghezza della parte di rete viene indicata più semplicemente con una barra obliqua dopo l'indirizzo IP. Ad esempio, 141.17.5.18/24 significa che la parte di rete è lunga 24 bit. In tutti i computer della stessa rete, l'indirizzo inizia con 141.17.5. Rimangono solo 8 dei 32 bit per numerare tutte le stazioni. Si tratta quindi di una rete relativamente piccola.

<indepth>
A volte le reti vengono assegnate a una cosiddetta classe, anche se questo sistema è stato abolito da tempo. La classe A corrispondeva a /8, la classe B a /16 e la classe C a /24.
</indepth>
%TODO Aggiungere approfondimento su Classless Inter-Domain Routing (CIDR).

---

La maggior parte dei dispositivi di rete richiede una notazione diversa, ovvero la maschera di sottorete (vedi figura [ref:netzmaske]). Si tratta di 32 bit nella stessa notazione degli indirizzi IP. I bit che rappresentano la parte di rete vengono contrassegnati con un 1, mentre quelli della parte host con un 0. La maschera di sottorete inizia quindi con tanti 1 quante sono le cifre della parte di rete, mentre il resto viene riempito con 0. Le reti domestiche e le piccole reti aziendali utilizzano quasi sempre la maschera di sottorete 255.255.255.0, che equivale a /24.

I dispositivi di rete possono comunicare direttamente tra loro solo all'interno della propria rete locale. Lo riconoscono dal fatto che, dalla loro indirizzo IP e maschera di sottorete, risulta la stessa parte di rete del partner. In tutti gli altri casi, inviano i dati a un router. Si tratta di una stazione intermedia che collega due o più reti tra loro. Se un dispositivo è collegato direttamente a più reti, ha un proprio indirizzo IP in ciascuna di esse.

<margin>
[picture:699:netzmaske:Indirizzo IPv4 e maschera di sottorete in notazione decimale e binaria]
</margin>

<margin>
[picture:706:netzwerk:Sezione di una infrastruttura di rete]
</margin>

Tutti i partecipanti di una rete devono poter utilizzare il router quasi contemporaneamente. Per questo motivo, nelle reti IP non vengono stabilite connessioni fisse. Al contrario, i computer suddividono tutti i flussi di dati in pacchetti, cioè in brevi segmenti. L'inoltro di questi singoli pacchetti viene chiamato commutazione di pacchetto.

[question:EE413]
