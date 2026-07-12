* La Hamnet, la Rete solo per radioamatori, si basa sul protocollo Internet (IP).
* Per questo motivo è possibile utilizzare la Hamnet con lo stesso software utilizzato per Internet.
* Nel caso più semplice si tratta di un browser web.

---

* Il protocollo Internet (IP) assegna indirizzi IP ai computer coinvolti, in modo che possano raggiungersi a vicenda.
* Gli indirizzi IP sono scritti come quattro numeri decimali con un punto in mezzo. Esempio: 141.17.5.18
* Ogni numero decimale ha una lunghezza di 8 bit, quindi il numero più grande possibile è 255 (binario: 11111111).

<note>
Esistono le versioni IPv4 e IPv6. Qui ci occupiamo della versione 4.
</note>

---

* Gli indirizzi IP sono suddivisi in una parte di rete e una parte host.
* Su tutti i computer che si trovano nella stessa Rete, l'inizio degli indirizzi IP è uguale, questo inizio è chiamato parte di rete.
* La parte di rete ha dimensioni diverse, a seconda di quanti computer (host) devono essere gestiti nella Rete.

---

Esempi:

     *10*.100.234.22 (piccola parte di rete, grande parte host)
     
     *192.168.1*.252 (grande parte di rete, piccola parte host)
     
Questo principio è noto dalla rete telefonica. Le grandi città hanno prefissi più brevi delle piccole città.

---

[picture:699:netzmaske:Indirizzo IPv4 e maschera di sottorete in notazione decimale e binaria]

* Una maschera di sottorete indica la suddivisione di un indirizzo IP in parte di rete e parte host, rappresentando tutti i bit della parte di rete come 1.

---

* Esistono due modi per scriverlo, esempio per una parte di rete di 24:
* 255.255.255.0, che in binario è 11111111.11111111.11111111.00000000.
* La notazione con la barra, ad esempio 192.168.111.90/24

<note>
Il numero dopo la barra indica il numero di uni nella maschera di sottorete.
</note>

---

[picture:706:netzwerk:Estratto da un'infrastruttura di rete]

* I dispositivi di rete possono comunicare direttamente tra loro solo all'interno della propria Rete locale.

--- data-transition="none"

[picture:706:netzwerk:Estratto da un'infrastruttura di rete]

* Li si riconosce dal fatto che dal proprio indirizzo IP e dalla maschera di sottorete si ottiene la stessa parte di rete del partner.

--- data-transition="none"

[picture:706:netzwerk:Estratto da un'infrastruttura di rete]

* In tutti gli altri casi, inviano i dati a un router. Questa è una stazione intermedia che collega due o più Reti per inoltrare i pacchetti di dati.

---
[question:EE412]

---
[question:EE414]

---
[question:EE413]
