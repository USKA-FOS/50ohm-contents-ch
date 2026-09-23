**IN BEARBEITUNG**

<attention>
„Der Satellitenfunk wird im HB3-Kurs bereits unter den grundlegenden Vorschriften und der Betriebstechnik behandelt. Die weiterführenden technischen Aspekte werden im HB9-Kurs im Kapitel [sec:satelliten_2] vertieft.“
</attention>

<margin>
[photo:124:n_satellit_oscar1:Modell des ersten Amateurfunksatelliten OSCAR 1, der 1961 für 22 Tage aus dem Orbit der Erde eine Bake im $\qty{2}{\meter}$-Band sendete und von 570 Funkamateuren aus 28 Ländern gehört wurde]
</margin>

---

Satelliten umrunden die Erde in kreisförmigen oder elliptischen Bahnen und in unterschiedlichen Höhen. Mehr dazu folgt in [sec:satelliten_2]. Seit 1961 gehören dazu auch Amateurfunksatelliten. Diese werden als OSCAR bezeichnet. Das ist die Abkürzung für "Orbiting Satellite Carrying Amateur Radio" ("Umkreisender Satellit, der Amateurfunk mitführt"). Der erste Amateurfunksatellit wurde OSCAR 1 ([ref:n_satellit_oscar1]) genannt. OSCAR 1 war nur der Anfang. In den Folgejahren - bis heute - wurde eine ganze Reihe immer umfangreicher ausgestatteter Amateurfunknutzlasten ins All gebracht. 
(Quellenangabe: [History of AMSAT](https://www.amsat.org/amsat-history/))
[question:BE415]

Die mitgeführten Relaisfunkstellen werden als "Transponder" bezeichnet. Die Eingabefrequenz, also die Funkstrecke von der Erde zum Satelliten, wird im Satellitenfunk als "Uplink" bezeichnet. Die Ausgabefrequenz, also die Funkstrecke vom Satelliten zur Erde, wird hingegen "Downlink" genannt . Für Uplink und Downlink werden oftmals unterschiedliche Frequenzbänder benutzt, weil dies eine einfachere Trennung von Sende- und Empfangssignal ermöglicht und die Baugröße von Filtern auf dem Satelliten reduziert wird.

<indepth>
*Charakterisierung von Satellitenbahnen (orbits)*

Satellitenbahnen können nach verschiedenen Eigenschaften beschrieben werden. Die Begriffe LEO, MEO und GEO beziehen sich hauptsächlich auf die Bahnhöhe. Begriffe wie HEO oder Polar Orbit beschreiben dagegen andere Eigenschaften der Bahn, insbesondere deren Form oder Neigung. Diese Einteilungen können sich daher überschneiden. Im Folgenden stellen wir die wichtigsten Flughöhen bzw. Umlaufbahnen vor.

*Niedrige Umlaufbahnen (Low Earth Orbit - LEO)*
Satelliten in niedrigen Umlaufbahnen befinden sich in Höhen von etwa 400 bis 2'000 Kilometern über über der Erdoberfläche. Das sind Umlaufbahnen, die sich relativ nahe an der Erdoberfläche befinden. In diesem Bereich bewegen sich viele Erdbeobachtungs- und Wettersatelliten sowie zahlreiche Amateurfunksatelliten. Die Nähe zur Erde ermöglicht eine hohe Auflösung bei der Erfassung von Daten und Bildern. Die geringe Entfernung zur Erde ermöglicht relativ kurze Funkstrecken und damit geringe Freiraumdämpfung. Gleichzeitig bewegen sich LEO-Satelliten schnell über den Himmel und sind von einer bestimmten Funkstation nur während eines zeitlich begrenzten Überflugs sichtbar.

*Mittlere Umlaufbahnen (Medium Earth Orbit - MEO)*
Mittlere Umlaufbahnen liegen grob zwischen 2'000 und 35'786 Kilometern Höhe. In diesem Bereich befinden sich beispielsweise viele Navigationssatelliten, wie sie für das weltbekannte GPS-System verwendet werden. Da die Satelliten hier länger brauchen, um die Erde zu umkreisen, bieten sie eine ausgeglichene Balance zwischen Abdeckung und Genauigkeit für Navigation und Positionierung. Mit zunehmender Bahnhöhe verlängert sich die Umlaufzeit. Gleichzeitig vergrössert sich das von einem Satelliten erreichbare Gebiet.

*Geostationäre Umlaufbahn (Geostationary Orbit – GEO)*
Eine geosynchrone Umlaufbahn hat eine Umlaufzeit von ungefähr einem siderischen Tag, also 23 Stunden, 56 Minuten und 4 Sekunden. Eine besondere Form davon ist die geostationäre Umlaufbahn (Geostationary Orbit, GEO) in einer Höhe von etwa 35.786 Kilometern über dem Äquator.

Ein geostationärer Satellit bewegt sich auf einer nahezu kreisförmigen Bahn über dem Äquator in derselben Drehrichtung und mit derselben Winkelgeschwindigkeit wie die Erde. Dadurch erscheint er von der Erde aus gesehen nahezu ortsfest am Himmel. Dies ermöglicht es einer Bodenstation, ihre Antenne dauerhaft auf dieselbe Position auszurichten. Geostationäre Satelliten eignen sich daher besonders für Kommunikationsanwendungen und ermöglichen eine konstante Abdeckung eines bestimmten Gebiets.

[QO-100](https://amsat-dl.org/p4-a-nb-transponder-bandplan-und-betriebsrichtlinien/) ist die Amateurfunknutzlast auf dem geostationären Satelliten Es’hail-2 und ist die erste Amateurfunknutzlast in einer geostationären Umlaufbahn.

*Hochelliptische Umlaufbahnen (Highly Elliptical Orbit - HEO)*

Hochelliptische Umlaufbahnen besitzen eine stark exzentrische Ellipsenform. Der Satellit ist dabei während eines Teils der Bahn wesentlich weiter von der Erde entfernt als während des restlichen Umlaufs. HEO-Bahnen können so ausgelegt werden, dass ein Satellit lange über hohen geografischen Breiten sichtbar bleibt. Sie eignen sich deshalb beispielsweise für Anwendungen, bei denen eine gute Abdeckung der Polarregionen benötigt wird. HEO ist keine reine Höhenklasse wie LEO oder MEO, sondern beschreibt vor allem die Form der Bahn. 

*Polarumlaufbahnen (Polar Orbit)*
Satelliten, die in Polumlaufbahnen operieren, fliegen über die Pole der Erde hinweg. Bei einer Polarumlaufbahn ist die Bahnneigung ungefähr 90 Grad. Da sich die Erde unter der Bahn des Satelliten weiterdreht, können bei geeigneter Bahn im Laufe der Zeit nahezu alle Regionen der Erdoberfläche überflogen werden. Auch eine Polarumlaufbahn ist keine eigene Höhenklasse. Ein Satellit kann beispielsweise gleichzeitig in einer LEO- und in einer Polarumlaufbahn betrieben werden.
</indepth>

[question:BE416]
[question:BE411]
[question:BE412]
[question:NF113]

---

Bei der Nutzung von Satellitenkommunikation ist die Ausrichtung von Antennen von zentraler Bedeutung. Die Begriffe *Azimut* und *Elevation* spielen dabei eine Schlüsselrolle. Sie beschreiben die horizontale Ausrichtung und den vertikalen Winkel, unter denen ein Satellit von der Erdoberfläche aus wahrgenommen wird.
* Das *Azimut* ist die Richtung entlang des Horizonts, in die man schaut, um den Satelliten zu sehen. Er wird meist in Grad gemessen und reicht von $\qty{0}{\degree}$ (Norden) über $\qty{90}{\degree}$ (Osten), $\qty{180}{\degree}$ (Süden) bis $\qty{270}{\degree}$ (Westen).
* Die *Elevation* ist der vertikale Winkel, unter dem ein Satellit über dem Horizont steht. Sie wird ebenfalls in Grad gemessen und variiert von $\qty{0}{\degree}$ (direkt am Horizont) bis $\qty{90}{\degree}$ (senkrecht über einem).

<margin>
[picture:876:n_azimut_elevation:Azimut und Elevation im Raum]
</margin>

<wordorigin>
Der Begriff *Azimut* stammt von arabisch *as-sumūt*, ("die Wege") ab. *Elevation* leitet sich vom lateinischen elevare ("erheben") ab.
</wordorigin>

[question:BE413]
[question:BE414]

Im Amateurfunkdienst über Satelliten gilt eine Ausnahme von der Pflicht, nur offene Sprache zu verwenden. Es ist erlaubt, Steuersignale zwischen Bodenstationen und Amateurfunksatelliten zum Zwecke der Verschleierung zu verschlüsseln. Das heißt, dass hierfür ausnahmsweise Verschlüsselungsverfahren genutzt werden dürfen, die verhindern, dass der Inhalt der Steuersignale von Dritten mitgelesen werden kann. Dies dient der Sicherheit der Satelliten vor Steuerkommandos von Unbefugten.

[question:VA303]
[question:VN026]


%Im deutschen Recht - nicht aber international - gilt diese Regelung auch für die Steuersignale an automatische und fernbediente Stationen sowie Remote-Stationen. Entsprechende Frage VD104 gelöscht.

---

**XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX**
*******DIESER TEIL GEHÖRT IN DAS FORTSETZUNGSKAPITEL FÜR DEN HB9-TEIL******

---

<attention>
*Dieser Stoff ist nicht prüfungsrelevant.*
Satelliten und Raumfahrt spielen eine immer wichtigere Rolle. Wir Funkamateure können dank des Amateurfunktdiensts über Satelliten auch auf diesem spannenden Feld tätig werden. Deshalb sind wir der Meinung, dass diese Einführung in einen Amateurfunkkurs reingehört, auch wenn das Thema aktuell nicht geprüft wird.
</attention>

## Umlaufbahnen und Keplersche Gesetze

Satelliten bewegen sich nicht beliebig um die Erde. Ihre Bahnen werden durch die Gravitation bestimmt und lassen sich mit den Keplerschen Gesetzen beschreiben. Eine Kreisbahn ist dabei ein Sonderfall einer elliptischen Bahn ([ref:a_kepler_ellipse]).

### 1. Keplersches Gesetz - Ellipsengesetz

Die Bahn eines Satelliten um die Erde ist grundsätzlich eine Ellipse. Die Erde befindet sich dabei in einem der beiden Brennpunkte der Ellipse. Bei einer kreisförmigen Bahn fallen die beiden Brennpunkte zusammen.

---

### 2. Keplersches Gesetz - Flächengesetz

Die Verbindungslinie zwischen Erde und Satellit überstreicht in gleichen Zeiten gleiche Flächen. Daraus folgt: Ein Satellit bewegt sich auf einer elliptischen Bahn beim erdnächsten Punkt, dem Perigäum, schneller und beim erdfernsten Punkt, dem Apogäum, langsamer.

Dieses Verhalten ist auch für die Funkpraxis interessant, weil sich dadurch die Relativgeschwindigkeit zwischen Satellit und Funkstation während eines Überflugs verändert.

### 3. Keplersches Gesetz - Umlaufgesetz

Für Satelliten, die dasselbe Zentralobjekt umkreisen, gilt:

$$T^2 \propto a^3$$

Dabei ist $T$ die Umlaufzeit und $a$ die grosse Halbachse der Bahnellipse. Je grösser die grosse Halbachse der Bahn ist, desto länger dauert ein Umlauf.
Für die Satellitenpraxis bedeutet dies: Satelliten in niedrigen Umlaufbahnen umkreisen die Erde wesentlich schneller als Satelliten in höheren Umlaufbahnen.

<margin>
[picture:10100:a_kepler_ellipse:Kepler Ellipse mit Satellit im Umlauf] 
</margin>

Im Kapitel [sec:satelliten] haben wir verschiedene Satellitenbahnen kennengelernt. Die Umlaufzeit eines Satelliten um die Erde hängt von der Höhe seiner Bahn ab. Dieser Zusammenhang ist im Bild 
[ref: a_umlaufzeiten] dargestellt. 

<indepth>
*Umlaufzeit eines Satelliten* 
[picture:10101:a_umlaufzeiten:Umlaufzeiten in Funktion der Höhe der Bahn] 
</indepth>

## Sichtbarkeit eines Satelliten

Für eine Funkstation auf der Erde ist nicht entscheidend, ob ein Satellit grundsätzlich die Erde umkreist, sondern ob er sich gerade über dem lokalen Horizont befindet. Ein Überflug beginnt mit dem "Acquisition of Signal" (AOS), wenn der Satellit für die Station sichtbar beziehungsweise empfangbar wird. Er endet mit dem "Loss of Signal" (LOS), wenn er wieder unter den Horizont sinkt.

Die Position eines Satelliten am Himmel wird durch das Azimut, also die Richtung entlang des Horizonts, und die Elevation, also den Winkel über dem Horizont, angegeben. Während eines Überflugs ändern sich beide Werte laufend.

Der Bereich auf der Erdoberfläche, von dem aus ein Satellit grundsätzlich über dem Horizont gesehen werden kann, wird als Footprint bezeichnet. Je höher der Satellit fliegt, desto grösser kann dieser Bereich sein.

---

## Dopplereffekt beim Satellitenfunk

Da sich ein Satellit relativ zur Funkstation auf der Erde bewegt, tritt bei einer Funkverbindung mit dem Satelliten der Dopplereffekt auf. Dabei verändert sich die empfangene Frequenz gegenüber der tatsächlich ausgesendeten Frequenz.

Nähert sich der Satellit der Funkstation, wird die empfangene Frequenz gegenüber der Nennfrequenz erhöht. Entfernt sich der Satellit wieder, wird die empfangene Frequenz erniedrigt.

Für kleine Geschwindigkeiten gegenüber der Lichtgeschwindigkeit kann die Frequenzverschiebung näherungsweise mit

$$\Delta f \approx f_0 \frac{v_r}{c}$$

beschrieben werden. Dabei ist $f_0$ die Sendefrequenz, $v_r$ die Relativgeschwindigkeit in Richtung der Funkstrecke und $c$ die Lichtgeschwindigkeit. Entscheidend ist also die radiale Geschwindigkeit und nicht die gesamte Bahngeschwindigkeit des Satelliten. Dabei sei v<sub>r</sub>>0, wenn sich Sender und Empfänger einander nähern.

Bei LEO-Satelliten kann die Dopplerverschiebung insbesondere bei höheren Frequenzen und bei schmalbandigen Betriebsarten deutlich bemerkbar sein. Deshalb muss die Frequenz während eines Satellitenüberflugs gegebenenfalls laufend nachgeführt werden. Moderne Satellitenstationen können die Dopplerkompensation automatisch durchführen.

<indepth>
Dieses Applet visualisiert den Dopplereffekt. Mit dem Schieberegler kann die *Relativgeschwindigkeit zwischen Sender und Empfänger* eingestellt werden.
  
- Wenn sich die *Quelle auf einem zubewegt*, treffen mehr Wellenfronten pro Zeiteinheit ein, was einer *Erhöhung der empfangenen Frequenz* entspricht. Obwohl der Sender immer mit der gleichen Frequenz sendet. 
  
- Wenn sich die *Quelle von einem wegbewegt*, treffen weniger Wellenfronten pro Zeiteinheit ein, was einer *Erniedrigung der empfangenen Frequenz* entspricht. Obwohl der Sender immer mit der gleichen Frequenz sendet.

[include:doppler_visualisierung]

</indepth>

## Freiraumdämpfung und Funkverbindung

Das Funksignal eines Satelliten muss eine grosse Entfernung zwischen Bodenstation und Satellit zurücklegen. Dabei entsteht die sogenannte Freiraumdämpfung. Sie nimmt mit zunehmender Entfernung und mit steigender Frequenz zu.

Für eine ideale Freiraumverbindung gilt die Friis'sche Freiraumformel, welche die Basis für jedes Linkbudget bildet:

$$L_{FS}=20\log_{10}\left(\frac{4\pi d}{\lambda}\right)$$

Dabei ist $d$ die Entfernung zwischen Sender und Empfänger und $\lambda$ die Wellenlänge.

Für eine funktionierende Satellitenverbindung müssen deshalb Sendeleistung, Antennengewinn, Kabelverluste, Freiraumdämpfung und Empfängerempfindlichkeit gemeinsam betrachtet werden. Diese Betrachtung wird als Linkbudget bezeichnet.

<indepth>
*Vereinfachtes Downlink-Budget eines LEO-CubeSats im 2-Meterband*
Der Begiff dB (Dezibel) wird erst im Kapitel [sec:dezibel_1] ausführlich behandelt. Hier genügt es, zu wissen, dass dB eine Verhältniszahl und dBm einen absoluten Leistungspegel darstellt.
Ein stark vereinfachtes Beispiel für einen Downlink von einem LEO-CubeSat zu einer Bodenstation könnte so aussehen:

| Grösse | Beispielwert |
| Frequenz | 145.9 MHz |
| Sendeleistung 1 W | 30 dB<sub>m</sub>  |
| Verluste TX-Kabel und Stecker | −1 dB |
| Gewinn Sendeantenne | +3 dB<sub>i</sub> |
| EIRP | +32 dB<sub>m</sub> |
| Entfernung | 2 000 km |
| Freiraumdämpfung | −141,7 dB |
| Gewinn Empfangsantenne | +8 dB<sub>i</sub> |
| Vorverstärker | +15 dB |
| Verluste RX-Kabel und Stecker | −2 dB |
| Leistung am Rx-Eingang| −88,7 dB<sub>m</sub> |
| angenommene Empfängerempfindlichkeit | -104 dB<sub>m</sub>  |
|  |   | 
| Linkmargin  |  +15.3 dB |

In einem echten Linkbudget kommen weitere Faktoren hinzu, z. B. Modulationsart, Datenrate, Empfängerrauschen und Linkreserve.
</indepth>

## Antennen und Polarisation

Da sich der Satellit während eines Überflugs bewegt, verändert sich auch seine Richtung relativ zur Bodenstation. Für viele Satellitenverbindungen werden deshalb Antennen mit geeignetem Gewinn und einer ausreichenden Richtwirkung eingesetzt. Bei stärker richtenden Antennen kann eine Nachführung der Antenne erforderlich sein.

Auch die Polarisation des Signals muss berücksichtigt werden. Durch die Bewegung und die Lage des Satelliten kann sich die Orientierung der Polarisation relativ zur Bodenstation verändern. Bei Satellitenfunk werden deshalb je nach Anwendung lineare oder zirkulare Polarisationen eingesetzt.

## Transponder und Digipeater

Amateurfunksatelliten können unterschiedliche Arten von Funknutzlasten besitzen.

Ein linearer Transponder empfängt einen Frequenzbereich und setzt ihn in einen anderen Frequenzbereich um. Mehrere Signale können gleichzeitig innerhalb der verfügbaren Transponderbandbreite übertragen werden. Typische Betriebsarten sind beispielsweise SSB und CW.

Ein FM-Transponder arbeitet dagegen mit FM-Signalen für die gleichzeitige Übertragung eines einzelnen Gesprächs.

Ein Digipeater empfängt digitale Daten und sendet sie nach einem definierten Verfahren wieder aus. Er unterscheidet sich damit grundsätzlich von einem linearen Transponder, der das empfangene Frequenzspektrum umsetzt, ohne die einzelnen Nutzsignale als Datenpakete zu verarbeiten.

## Satellitenbaken

Viele Amateurfunksatelliten verfügen über eine Bake. [sec:baken] senden automatisch in regelmässigen Abständen oder kontinuierlich definierte Signale aus. Sie können dazu dienen, die Empfangbarkeit des Satelliten, die Ausbreitungsbedingungen und den Zustand der Funknutzlast zu beobachten.

Beim Empfang einer Bake kann eine Funkstation beispielsweise feststellen, ob der Satellit bereits über dem Horizont steht, wie sich die Empfangsfrequenz durch den Dopplereffekt verändert und wie gut die Funkverbindung funktioniert.

## Satellitenverfolgung

Für den praktischen Satellitenfunk werden die aktuelle Bahn und die Position des Satelliten benötigt. Dazu werden Bahnelemente, beispielsweise sogenannte TLE (Two-Line Elements), verwendet. Tracking-Programme berechnen daraus die voraussichtliche Position des Satelliten und zeigen unter anderem Azimut, Elevation, AOS und LOS sowie den zu erwartenden Dopplereffekt an.

Damit lassen sich Überflüge planen und Funkgeräte sowie Antennen automatisch nachführen.

---

<tip>
Mit Amateurfunk über Satelliten befassen sich weltweit die AMSAT-Organisationen, in der Schweiz ist das [AMSAT-HB](https://amsat-hb.org/) 
</tip>

