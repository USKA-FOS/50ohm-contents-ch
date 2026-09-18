* Il **Hamnet**, la **rete** riservata esclusivamente ai radioamatori, si basa sul protocollo Internet (IP).
* Per questo motivo, è possibile utilizzare il **Hamnet** con lo stesso software impiegato per Internet.
* Nel caso più semplice, si tratta di un browser web.

---

* Il protocollo Internet (IP) assegna agli **computer** coinvolti degli indirizzi IP, in modo che possano comunicare tra loro.
* Gli indirizzi IP sono scritti come quattro numeri decimali separati da un punto. Esempio: 141.17.5.18
* Ogni numero decimale ha una **lunghezza** di 8 **bit**, pertanto il valore massimo possibile è 255 (in binario: 11111111).

<note>
Esistono le versioni IPv4 e IPv6. Qui ci occupiamo della versione 4.
</note>

---

* Gli indirizzi IP sono suddivisi in una parte di rete e una parte di host.
* Per tutti i **computer** che si trovano nella stessa **rete**, l'inizio degli indirizzi IP è identico; questa parte iniziale viene chiamata parte di rete.
* La parte di rete può avere dimensioni diverse a seconda del numero di **computer** (host) che devono essere gestiti nella **rete**.

---

Esempi:

     *10*.100.234.22 (parte di rete piccola, parte di host grande)
     
     *192.168.1*.252 (parte di rete grande, parte di host piccola)
     
Questo principio è simile a quello della rete telefonica: le città più grandi hanno prefissi più brevi rispetto a quelle più piccole.

---

[picture:699:netzmaske:Indirizzo IPv4 e maschera di sottorete in notazione decimale e binaria]

* Una maschera di sottorete indica la suddivisione di un indirizzo IP in parte di rete e parte di host, rappresentando tutti i **bit** della parte di rete come 1.

---

* Esistono due modi per scriverla, ad esempio per una parte di rete di 24:
* 255.255.255.0, che in binario corrisponde a 11111111.11111111.11111111.00000000.
* La notazione con la barra obliqua, ad esempio 192.168.111.90/24

<note>
Il numero dopo la barra obliqua indica il numero di 1 nella maschera di sottorete.
</note>

---

[picture:706:netzwerk:Sezione di un'infrastruttura di rete]

* I dispositivi di rete possono comunicare direttamente tra loro solo all'interno della propria **rete** locale.

--- data-transition="none"

[picture:706:netzwerk:Sezione di un'infrastruttura di rete]

* Ci si accorge di ciò perché, dalla propria indirizzo IP e dalla maschera di sottorete, si ottiene la stessa parte di rete del partner.

--- data-transition="none"

[picture:706:netzwerk:Sezione di un'infrastruttura di rete]

* In tutti gli altri casi, inviano i dati a un router. Si tratta di una stazione intermedia che collega due o più **reti** tra loro per inoltrare i pacchetti di dati.

---
[question:EE412]

---
[question:EE414]

---
[question:EE413]
