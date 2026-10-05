In diesem Kapitel werden Grundlagen über Linkstrecken und zugehörige Vorschriften für den Betrieb behandelt. Eine erweiterte Behandlung technischer Aspekte erfolgt im Kapitel [sec:paketvermittelte_netzwerke].

Eine Linkstrecke ist eine fest eingerichtete Funkverbindung, die der Vernetzung von Amateurfunkstellen, beispielsweise Relais, Digipeatern oder HAMNET-Knoten, dient. Linkstrecken können Bestandteil unbedienter Amateurfunkanlagen sein. Der Betrieb solcher Anlagen ist dem BAKOM entsprechend den geltenden [Vorschriften](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) zu melden. Für eine unbediente Amateurfunkanlage ist ein Amateurfunkrufzeichen der Kategorie HB9 erforderlich. Der technische Leiter muss während des Betriebs permanent erreichbar sein. Das Bild [ref:n_linkstrecken_HB9AK-14] zeigt eine Antennenanlage auf dem Titlis auf 2992 Meter über Meer. An solchen Standorten wie im Bild [ref:n_linkstrecken_HB9AK] herrschen anspruchsvolle Wetterbedingungen. Eine genaue und stabile Ausrichtung auf die zu erreichende Gegenstation wird im Bild [ref:n_linkstrecken_HB9] vorbereitet.

<margin>
%[photo:127:n_linkstrecken_db0fc:Wartungsarbeiten am HAMNET-Knoten DB0FC, im Vordergrund die Richtantenne %für die Linkstrecke zu DB0BWL]
%
[photo:1001:n_linkstrecken_HB9AK-14:Standort Titlis Anlage der SWISS-ARTG, Versuche mit 10 m-Antennen; oben Peter HB9PAE, unten Martin HB9AUR] 

[photo:1002:n_linkstrecken_HB9AK:Hochgebirgsanlagen müssen harschen Umweltbedingen standhalten]

[photo:1003:n_linkstrecken_HB9:Standort Titlis Anlage der SWISS-ARTG, Dieter HB9CJD am Einrichten des HAMNET-Links nach HB9BA (Weissenstein), ein 85 cm Spiegel für 5 GHz]
</margin>

%TODO ARK: im Text auf die Bilder bezugnehmen!
%TODO ARK: Beim Titlisbild, 1001, den linken, schwarzen Rand abschneiden! 
%TODO ARK: Eines der Bilder in den Abschnitt 16.11 Paketvermittelte Netzwerke verschieben!  

<law>
- Ausführliche "Erläuternde Angaben zum Amateurfunkdienst" findet man im [Merkblatt Amateurfunk](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) des BAKOM.

- Direktlink zur Meldung sogenannter "Spezieller Frequenznutzungen" ans BAKOM im [eGov](https://www.egov.swiss/de/amateurfunk/spezielle-frequenznutzung-detail)

</law>

Linkstrecken können digitale Daten übertragen oder als analoge Brücke zwischen Relais dienen. Linkstrecken arbeiten häufig im $\unit{\giga\hertz}$-Bereich des Amateurfunkspektrums. Mehrere miteinander verbundene Linkstrecken können beispielsweise das HAMNET (Highspeed Amateurradio Multimedia NETwork) aufbauen, ein von Funkamateuren betriebenes IP-Datennetz.

[question:NE405]

<indepth>
*Linkberechnung*

Mit einem [Linkberechnungstool](http://ham.remote-area.net/linktool/index.php) lässt sich beurteilen, ob eine Richtfunkverbindung zwischen zwei Standorten technisch möglich ist. Es berücksichtigt unter anderem Frequenz, Entfernung, Sendeleistung, Antennengewinne, Kabelverluste und das *Geländeprofil* zwischen den Standorten. Das Tool berechnet unter anderem Freiraumdämpfung, Empfangsleistung und Linkreserve und unterstützt damit die Planung von Richtfunk- und HAMNET-Verbindungen.

Für eine zuverlässige Richtfunkverbindung ist neben der direkten Sichtverbindung auch eine möglichst freie Fresnelzone wichtig. Die Fresnelzone bezeichnet einen räumlichen Bereich um die direkte Verbindungslinie, in dem Hindernisse die Funkübertragung durch Beugung und zusätzliche Dämpfung beeinträchtigen können.
</indepth>

% Änderungen 
% Echolink entfernt, es gehört zu Relais.
% Beschreibungen zu den Links erstellt bzw. ergänzt 
% Linkberechnungstool beschrieben, wozu es dient.
