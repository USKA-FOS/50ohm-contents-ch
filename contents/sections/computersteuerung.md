Die grundsätzliche Idee hinter der Morsetelegrafie, einzelne Zeichen eines Textes zu übermitteln, wird als Telegrafie bezeichnet und wurde stetig weiterentwickelt. Ein Meilenstein war es, Fernschreiber mittels Modem an Funkgeräte anzuschließen. Somit war der Funkfernschreiber erfunden, um automatisiert Texte per Funk zu senden und zu empfangen. Die Abkürzung RTTY des englischen Begriffes radio teletype findet sich immer noch als Bezeichnung wieder. Heute hat die Aufgabe des Funkfernschreibers in der Regel der Computer übernommen. Damit kann man neben dem klassischen RTTY-Verfahren viele andere digitale Übertragungsverfahren benutzen, die auch als Digimodes bezeichnet werden.

<indepth>
Ein *Fernschreiber* ist ein Gerät, um Nachrichten in Textform mittels elektrischer Signale zu übermitteln.
</indepth>

<margin>
[photo:92:n_computersteuerung_funkfernschreiber:Funkfernschreiber]
</margin>

---

Zunächst muss dafür ein geeigneter Computer mit dem Funkgerät verbunden werden. Die Verbindung kann im einfachsten Fall direkt über den Audioanschluss oder die USB-Schnittstelle erfolgen. Man benötigt grundsätzlich eine Audio-Verbindung sowie gegebenenfalls Steuersignale. In Abbildung [ref:n_computersteuerung_verbindungen] sind einige Varianten dargestellt. Ein häufig an Transceivern vorhandener Anschluss für Steuersignale ist die sogenannte CAT-Schnittstelle. CAT steht für Computer Aided Tuning oder Computer Aided Transceiver. Über diese Schnittstelle kannst du den Transceiver steuern und Werte abfragen, beispielsweise Frequenz, Sendeleistung und PTT-Zustand.

<margin>
[picture:630:n_computersteuerung_verbindungen:Beispiele für Verbindungen zwischen Computer und Funkgerät]
</margin>

Durch die Verbindung zwischen Computer und Transceiver kann es aber zu Störungen der übertragenen Signale oder Rückwirkungen des Funkgeräts auf den PC kommen. Verschiedene Digimode-Interfaces als Hardwarelösung vereinfachen den Anschluss und enthalten Maßnahmen gegen derartige Probleme. Solche Interfaces kann man auch für andere Zwecke verwenden, zum Beispiel für Remote-Betrieb oder zum Aufzeichnen des Funkverkehrs mit passender Software. Für einige Verfahren gibt es auch Hardware-Modems, bei denen die Umsetzung zwischen Daten und Audio-Signalen in einem eigenen Gerät erfolgt.

[question:NF114]
[question:NF116]

Es gibt auch noch andere unbeabsichtigte Effekte. Der Computer könnte unerwartet auf Sendung schalten oder Benachrichtigungstöne anderer laufender Programme aussenden. Manchmal hört man beispielsweise, wie andere Funkamateure versehentlich den Startsound des Betriebssystems aussenden. Wenn das Funkgerät unerwartet sendet, können eventuell Menschen gefährdet werden, die gerade an der Antennenanlage arbeiten oder sich zufällig in deren direkter Umgebung befinden.

[question:NF117]

---

Für einige Übertragungsverfahren ist der Mikrofonanschluss des Funkgeräts ungeeignet, da die nachfolgenden Verstärker- und Filterstufen für Sprache optimiert sind und verschieden hohe bzw. tiefe Töne unterschiedlich behandelt werden. Deshalb haben Funkgeräte oft einen eigenen analogen Datenanschluss, der zum Beispiel mit DATA oder 9600 beschriftet ist. Durch die Verwendung dieses speziellen Anschlusses werden bestimmte Verstärker- und Filterstufen umgangen und Signale möglichst verzerrungsfrei übertragen.

<indepth>
Die Bezeichnung *9600* kommt daher, dass dieser Anschluss für das früher viel verwendete Packet-Radio eingeführt wurde, damit Daten mit $\qty{9600}{\baud}$ übertragen werden konnten. Heute wird der Anschluss z. B. für digitale Sprachübertragung benutzt und teils auch mit höherer Geschwindigkeit betrieben.
</indepth>

[question:NF115]
