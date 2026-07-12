<margin>
[include:hamnet_map]
</margin>

Un ruolo particolare nel radioamatore è svolto da HAMNET, una rete riservata esclusivamente ai radioamatori. HAMNET (Highspeed Amateurradio Multimedia Network) è una rete basata su IP sviluppata e gestita da radioamatori. Nella sua funzionalità, assomiglia a Internet, ma utilizza prevalentemente collegamenti radio per la trasmissione dei dati.

Originariamente, HAMNET è stato concepito come un sostituto graduale della rete Packet-Radio esistente dagli anni '80 e l'ha quasi completamente sostituita. I veloci collegamenti dati tra i singoli punti di accesso e i nodi sono realizzati principalmente tramite le bande delle microonde da 6 cm, 9 cm e 13 cm. Per accedere a HAMNET è necessaria una linea di vista libera verso un nodo HAMNET con accesso utente e un trasmettitore-ricevitore WLAN adatto con antenna direzionale.

---

<margin>
La [*SWISS-ARTG*](https://www.swiss-artg.ch/index.php?id=9) offre ai suoi membri un accesso VPN tramite il cosiddetto [HAMCloud](https://www.swiss-artg.ch/index.php?id=37). Ciò consente l'accesso a HAMNET anche quando non è possibile un accesso diretto via radio.   

[Diventa subito membro della USKA!](https://uska.ch/wieso-uska-mitglied-werden/)
</margin>

Si può utilizzare Hamnet proprio come Internet, nel caso più semplice con un browser web. Ciò è possibile perché il cosiddetto Internet Protocol (IP) e tutto ciò che si basa su di esso possono essere utilizzati anche per scopi diversi da Internet.

[question:EE414]

Hamnet, proprio come Internet, è un insieme di molte reti individuali. Se due partecipanti non possono raggiungersi direttamente, i pacchetti di dati vengono inoltrati attraverso altri nodi.

[question:EE412]

In strutture così grandi, si crea ordine numerando tutti i computer. I numeri dei partecipanti si chiamano indirizzi IP. Esistono le versioni IPv4 e IPv6. Per il nostro hobby, di solito è sufficiente occuparsi della versione 4, più semplice.

Gli indirizzi IPv4 sono numeri binari con una lunghezza di 32 bit. Vengono scritti quattro numeri decimali, ciascuno dei quali rappresenta 8 bit, separati da punti. Il numero massimo possibile è 255, corrispondente al numero binario 11111111.

In tutti i computer che si trovano nella stessa rete, l'inizio degli indirizzi IP è lo stesso. Questa parte di rete ha una lunghezza variabile. Le grandi reti necessitano di molti dei 32 bit per numerare i propri computer nella parte finale, detta parte host. Utilizzano per questo una parte di rete più corta. Nelle piccole reti è esattamente il contrario. Questo principio è noto dalla rete telefonica. Le città più grandi hanno prefissi a tre cifre, ad esempio 089, e le piccole reti locali prefissi a cinque o sei cifre come 038725.

---

La lunghezza della parte di rete viene indicata più semplicemente con una barra obliqua dopo l'indirizzo IP. Ad esempio, 141.17.5.18/24 significa che la parte di rete è lunga 24 bit. Per tutti i computer nella stessa rete, l'indirizzo inizia con 141.17.5. Per numerare tutte le stazioni rimangono solo 8 dei 32 bit. Si tratta quindi di una rete relativamente piccola.

<indepth>
A volte le reti vengono assegnate a una cosiddetta classe, anche se questo sistema è stato abolito da tempo. Classe A significava /8, Classe B /16 e Classe C /24.
</indepth>
%TODO Aggiungere Classless Inter-Domain Routing (CIDR) come approfondimento.

---

La maggior parte dei dispositivi di rete richiede una diversa notazione, ovvero la subnet mask (vedi figura [ref:netzmaske]). Si tratta di 32 bit nella stessa notazione degli indirizzi IP. I bit che rappresentano la parte di rete sono contrassegnati con 1 e i bit della parte host con 0. La subnet mask inizia quindi con tanti uno quanti è lunga la parte di rete. Il resto viene riempito con zeri. Le reti domestiche e le piccole reti aziendali utilizzano quasi sempre la subnet mask 255.255.255.0, che significa la stessa cosa di /24.

I dispositivi di rete possono comunicare direttamente tra loro solo all'interno della propria rete locale. Lo riconoscono dal fatto che dal proprio indirizzo IP e dalla subnet mask si ottiene la stessa parte di rete del partner. In tutti gli altri casi, inviano i dati a un router. Questa è una stazione intermedia che collega due o più reti. Se un dispositivo è collegato direttamente a più reti, ha un proprio indirizzo IP in ciascuna.

<margin>
[picture:699:netzmaske:Indirizzo IPv4 e subnet mask in notazione decimale e binaria]
</margin>

<margin>
[picture:706:netzwerk:Estratto da un'infrastruttura di rete]
</margin>

Tutti i partecipanti di una rete dovrebbero poter utilizzare il router quasi contemporaneamente. Per questo motivo, nelle reti IP non vengono stabiliti collegamenti fissi. Invece, i computer suddividono tutti i flussi di dati in pacchetti, cioè in brevi segmenti. L'inoltro di questi singoli pacchetti è chiamato commutazione di pacchetto.

[question:EE413]
