* Das Hamnet, das Netzwerk nur für Funkamateure, basiert auf dem Internet-Protokoll (IP).
* Deswegen kann man das Hamnet mit der gleichen Software, die auch für das Internet verwendet wird, nutzen.
* Im einfachsten Fall ist das ein Webbrowser.

---

* Das Internet-Protokoll (IP) weist den beteiligten Computern IP-Adressen zu, damit sie sich gegenseitig erreichen können.
* IP-Adressen werden als vier Dezimalzahlen mit einem Punkt dazwischen geschrieben. Beispiel: 141.17.5.18
* Jede Dezimalzahl hat eine Länge von 8 Bit, deswegen ist die größtmögliche Zahl 255 (binär: 11111111).

<note>
Es existieren die Versionen IPv4 und IPv6. Wir befassen uns hier mit der Version 4.
</note>

---

* IP-Adressen sind in einen Netz- und einen Hostanteil aufgeteilt.
* Bei allen Computern, die sich im selben Netzwerk befinden, ist der Anfang der IP-Adressen gleich, diesen Anfang nennt man Netzanteil.
* Der Netzanteil ist unterschiedlich groß, je nachdem wie viele Computer (Hosts) im Netzwerk verwaltet werden sollen.

---

Beispiele:

     *10*.100.234.22 (kleiner Netzanteil, großer Hostanteil)
     
     *192.168.1*.252 (großer Netzanteil, kleiner Hostanteil)
     
Dieses Prinzip kennt man vom Telefonnetz. Die großen Städte haben kürzere Vorwahlen als kleine Städte.

---

[picture:699:netzmaske:IPv4-Adresse und Netzmaske in Dezimal- und Dualschreibweise]

* Eine Subnetzmaske gibt die Aufteilung einer IP-Adresse in Netz- und Hostanteil an, indem sie alle Bits des Netzanteils als 1 darstellt.

---

* Es zwei Möglichkeiten dieses niederzuschreiben, Beispiel für einen Netzanteil von 24:
* 255.255.255.0, was binär 11111111.11111111.11111111.00000000 ist.
* Die Schreibweise mit dem Schrägstrich, zum Beispiel 192.168.111.90/24

<note>
Die Zahl hinter dem Schrägstrich gibt die Anzahl der Einsen in der Subnetzmaske an.
</note>

---

[picture:706:netzwerk:Ausschnitt aus einer Netzwerk-Infrastruktur]

* Netzwerkgeräte können nur innerhalb ihres eigenen lokalen Netzwerks direkt miteinander kommunizieren.

--- data-transition="none"

[picture:706:netzwerk:Ausschnitt aus einer Netzwerk-Infrastruktur]

* Man erkennt sie daran, dass sich aus ihrer eigenen IP-Adresse und Subnetzmaske derselbe Netzanteil ergibt wie beim Partner.

--- data-transition="none"

[picture:706:netzwerk:Ausschnitt aus einer Netzwerk-Infrastruktur]

* In allen anderen Fällen schicken sie die Daten an einen Router. Das ist eine Zwischenstation, die zwei oder mehr Netzwerke miteinander verbindet, um die Datenpakete weiterzuleiten.

---
[question:EE412]

---
[question:EE414]

---
[question:EE413]
