In diesem Kapitel werden Grundlagen über Linkstrecken und zugehörige Vorschriften für den Betrieb behandelt. Eine erweiterte Behandlung technischer Aspekte erfolgt im Kapitel [sec:paketvermittelte_netzwerke].

Eine Linkstrecke ist eine fest eingerichtete Funkverbindung, die der Vernetzung von zwei Amateurfunkstellen, z. B. Relais oder HAMNET-Knoten, dient. Linkstrecken können Bestandteil unbedienter Amateurfunkanlagen sein. Der Betrieb unbedienter Anlagen ist dem BAKOM zu melden. Für die Nutzung als unbediente Anlage ist ein entsprechendes Amateurfunkrufzeichen erforderlich.

<margin>
[photo:127:n_linkstrecken_db0fc:Wartungsarbeiten am HAMNET-Knoten DB0FC, im Vordergrund die Richtantenne für die Linkstrecke zu DB0BWL]
</margin>

<law>
Direktlink zur Meldung sogenannter "Spezieller Frequenznutzungen" ans BAKOM im [eGov](https://www.egov.swiss/de/amateurfunk/spezielle-frequenznutzung-detail) 
</law>

<law>
Ausführliche "Erläuternde Angaben zum Amateurfunkdienst" findet man im [Merkblatt Amateurfunk](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) des BAKOM.
</law>

Eine Linkstrecke überträgt in der Regel Daten. Sie kann aber auch als analoge Brücke zwischen Relais dienen. Linkstrecken arbeiten häufig im $\unit{\giga\hertz}$-Bereich des Amateurfunkspektrums. Mehrere miteinander verbundene Linkstrecken können beispielsweise das HAMNET (Highspeed Amateurradio Multimedia NETwork) bilden, ein von Funkamateuren betriebenes IP-Datennetz.

[question:NE405]


<indepth>
*Linkberechnung*
Mit einem Linkberechnungstool lässt sich beurteilen, ob eine Funkverbindung zwischen zwei Standorten technisch möglich ist. Neben **Frequenz, Entfernung, Sendeleistung, Antennengewinn und Kabelverlusten** berücksichtigt das Tool auch das **Geländemodell** zwischen den beiden Standorten.

Aus den Höhendaten des Geländes kann beispielsweise ein **Höhenprofil der Funkstrecke** erstellt werden. Dadurch lässt sich erkennen, ob Hindernisse wie Hügel oder andere Erhebungen die direkte Funkverbindung beeinträchtigen. Zusätzlich kann die **Fresnelzone** berücksichtigt werden, da für eine zuverlässige Richtfunkverbindung nicht nur die direkte Sichtverbindung, sondern auch eine möglichst freie Fresnelzone wichtig ist.

Das Tool liefert daraus unter anderem die **Freiraumdämpfung, Empfangsleistung und Linkreserve** und hilft bei der Beurteilung und Planung von Richtfunk- und HAMNET-Verbindungen.
[Linkberechnungstool](http://ham.remote-area.net/linktool/index.php)
</indepth>
