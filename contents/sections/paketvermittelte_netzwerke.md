<margin>
[include:hamnet_map]
</margin>

Eine besondere Rolle im Amateurfunk nimmt das HAMNET ein – ein Netzwerk, das ausschließlich Funkamateuren vorbehalten ist. HAMNET (Highspeed Amateurradio Multimedia Network) ist ein von Funkamateuren entwickeltes und betriebenes IP-basiertes Netzwerk. In seiner Funktionsweise ähnelt es dem Internet, nutzt jedoch überwiegend Funkstrecken zur Datenübertragung.

Ursprünglich wurde HAMNET als schrittweiser Ersatz für das seit den 1980er-Jahren bestehende Packet-Radio-Netz konzipiert und hat dieses inzwischen nahezu vollständig abgelöst. Die schnellen Datenverbindungen zwischen den einzelnen Einstiegspunkten und Knoten werden hauptsächlich über die Mikrowellenbänder 6 cm, 9 cm und 13 cm realisiert. Für den Zugang zum HAMNET benötigt man freie Sicht zu einem HAMNET-Knoten mit Benutzerzugang sowie einen geeigneten WLAN-Transceiver mit Richtantenne.

---

<margin>
Der *SWISS-ARTG* bietet für ihre Mitglieder einen VPN-Zugang über die sogenannten [HAMCloud](https://www.swiss-artg.ch/index.php?id=37) an. Dies ermöglicht den Zugang zum HAMNET, auch wenn kein direkter Einstieg über Funk möglich ist.   

[Jetzt Mitglied der USKA werden!](https://uska.ch/wieso-uska-mitglied-werden/)
</margin>

Nutzen kann man das Hamnet genauso wie das Internet, im einfachsten Fall mit einem Webbrowser. Das ist möglich, weil das sogenannte Internet-Protokoll (IP) und alles, was darauf aufbaut, auch für andere Zwecke als für das Internet verwendet werden kann.

[question:EE414]

Das Hamnet ist genau wie das Internet ein Verbund aus vielen einzelnen Netzwerken. Wenn sich zwei Teilnehmer nicht direkt erreichen können, dann werden die Datenpakete entsprechend über andere Knoten weitergeleitet.

[question:EE412]

In so großen Gebilden schafft man dadurch Ordnung, dass alle Computer nummeriert sind. Die Nummern der Teilnehmern heißen IP-Adressen. Es existieren die Versionen IPv4 und IPv6. Für unser Hobby genügt es meistens, sich mit der einfacheren Version 4 zu befassen.

IPv4-Adressen sind Dualzahlen mit einer Länge von 32 Bit. Geschrieben werden vier Dezimalzahlen, von denen jede für 8 Bit steht, mit Punkten dazwischen. Die größtmögliche Zahl ist 255 entsprechend der Dualzahl 11111111.

Bei allen Computern, die sich im selben Netzwerk befinden, ist der Anfang der IP-Adressen gleich. Dieser Netzanteil hat eine variable Länge. Große Netzwerke brauchen viele der 32 Bits, um hinten im sogenannten Hostanteil ihre Computer zu nummerieren. Sie verwenden dafür einen kürzeren Netzanteil. Bei kleinen Netzwerken ist es genau umgekehrt. Dieses Prinzip kennt man vom Telefonnetz. Die größten Städte haben dreistellige Vorwahlen, zum Beispiel 089, und kleine Ortsnetze fünf- oder sechsstellige wie 038725.

---

Die Länge des Netzanteils gibt man am einfachsten mit einem Schrägstrich hinter der IP-Adresse an. 141.17.5.18/24 bedeutet zum Beispiel, dass der Netzanteil 24 Bit lang ist. Bei allen Rechnern im gleichen Netzwerk beginnt die Adresse mit 141.17.5. Zum Durchnummerieren aller Stationen bleiben nur 8 der 32 Bits übrig. Es handelt sich also um ein relativ kleines Netzwerk.

<indepth>
Manchmal werden Netzwerke einer sogenannten Klasse zugeordnet, obwohl dieses System schon lange abgeschafft wurde. Klasse A bedeutete /8, Klasse B /16 und Klasse C /24.
</indepth>


---

Die meisten Netzwerkgeräte verlangen eine andere Schreibweise, nämlich die Subnetzmaske (siehe Abbildung [ref:netzmaske]). Das sind 32 Bit in der gleichen Notation wie IP-Adressen. Bits, die für den Netzanteil stehen, werden mit einer 1 gekennzeichnet und Bits des Hostanteils mit einer 0. Die Netzmaske beginnt also mit so vielen Einsen, wie der Netzanteil lang ist. Der Rest wird mit Nullen aufgefüllt. Heimnetze und kleine Firmennetze verwenden fast immer die Netzmaske 255.255.255.0, die das Gleiche bedeutet wie /24.

Netzwerkgeräte können nur innerhalb ihres eigenen lokalen Netzwerks direkt miteinander kommunizieren. Das erkennen sie daran, dass sich aus ihrer eigenen IP-Adresse und Subnetzmaske derselbe Netzanteil ergibt wie beim Partner. In allen anderen Fällen schicken sie die Daten an einen Router. Das ist eine Zwischenstation, die zwei oder mehr Netzwerke miteinander verbindet. Wenn ein Gerät mit mehreren Netzwerken direkt verbunden ist, hat es in jedem eine eigene IP-Adresse.

<margin>
[picture:699:netzmaske:IPv4-Adresse und Netzmaske in Dezimal- und Dualschreibweise]
</margin>

<margin>
[picture:706:netzwerk:Ausschnitt aus einer Netzwerk-Infrastruktur]
</margin>

Alle Teilnehmer eines Netzwerks sollen den Router quasi gleichzeitig nutzen können. Deshalb werden in IP-Netzen keine festen Leitungen geschaltet. Stattdessen teilen die Computer alle Datenströme in Pakete auf, also in kurze Abschnitte. Die Weiterleitung dieser einzelnen Pakete nennt man Paketvermittlung.

[question:EE413]
