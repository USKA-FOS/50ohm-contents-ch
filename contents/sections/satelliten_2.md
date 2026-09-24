IN ABSCHLUSSREDAKTION DURCH DEN AUTOR

<attention>
*Dieser Stoff ist nicht prüfungsrelevant.*
Satelliten und Raumfahrt spielen eine immer wichtigere Rolle. Wir Funkamateure können dank des Amateurfunkdiensts über Satelliten auch auf diesem spannenden Feld tätig werden. Deshalb sind wir der Meinung, dass diese Einführung in einen Amateurfunkkurs reingehört, auch wenn das Thema aktuell nicht geprüft wird.
</attention>

Ein paar Grundlagen sind aus dem Kapitel [sec:satelliten] bereits bekannt. Hier werden weitere Begriffe aus der Satellitenkommunikation behandelt.

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

### Umlaufzeit eines Satelliten

Im Kapitel [sec:satelliten] haben wir verschiedene Satellitenbahnen kennengelernt. Die Umlaufzeit eines Satelliten um die Erde hängt von der grossen Halbachse seiner Bahn ab. Bei Kreisbahnen entspricht diese der Bahnhöhe plus dem Erdradius. Dieser Zusammenhang ist im Bild 
[ref:a_umlaufzeiten] dargestellt. 

<indepth>
*Umlaufzeit eines Satelliten* 
[picture:10101:a_umlaufzeiten:Umlaufzeiten in Funktion der Höhe der Bahn] 
</indepth>

Für den praktischen Satellitenfunk sind insbesondere Umlaufzeit, Sichtbarkeit und die Geschwindigkeit des Satelliten von Bedeutung.

## Sichtbarkeit eines Satelliten

Für eine Funkstation auf der Erde ist nicht entscheidend, ob ein Satellit grundsätzlich die Erde umkreist, sondern ob er sich gerade über dem lokalen Horizont befindet. Ein Überflug beginnt mit dem "Acquisition of Signal" (AOS), wenn der Satellit für die Station sichtbar beziehungsweise empfangbar wird. Er endet mit dem "Loss of Signal" (LOS), wenn er wieder unter den Horizont sinkt.

Die Position eines Satelliten am Himmel wird durch das Azimut, also die Richtung entlang des Horizonts, und die Elevation, also den Winkel über dem Horizont, angegeben. Während eines Überflugs ändern sich beide Werte laufend.

Der Bereich auf der Erdoberfläche, in dem ein Satellit bzw. seine Funknutzlast empfangen werden kann, wird als Footprint bezeichnet. Je höher der Satellit fliegt, desto grösser kann dieser Bereich sein.

---

## Dopplereffekt beim Satellitenfunk

Da sich ein Satellit relativ zur Funkstation auf der Erde bewegt, tritt bei einer Funkverbindung mit dem Satelliten der Dopplereffekt auf. Dabei verändert sich die empfangene Frequenz gegenüber der tatsächlich ausgesendeten Frequenz.

Nähert sich der Satellit der Funkstation, wird die empfangene Frequenz gegenüber der Nennfrequenz erhöht. Entfernt sich der Satellit wieder, wird die empfangene Frequenz erniedrigt.

Für kleine Geschwindigkeiten gegenüber der Lichtgeschwindigkeit kann die Frequenzverschiebung näherungsweise mit

$$\Delta f \approx f_0 \frac{v_r}{c}$$

beschrieben werden. Dabei ist $f_0$ die Sendefrequenz, $v_r$ die Relativgeschwindigkeit in Richtung der Funkstrecke und $c$ die Lichtgeschwindigkeit. Entscheidend ist also die radiale Geschwindigkeit und nicht die gesamte Bahngeschwindigkeit des Satelliten. Dabei sei $v_r > 0$, wenn sich Sender und Empfänger einander nähern.

Bei LEO-Satelliten kann die Dopplerverschiebung insbesondere bei höheren Frequenzen und bei schmalbandigen Betriebsarten deutlich bemerkbar sein. Deshalb muss die Frequenz während eines Satellitenüberflugs gegebenenfalls laufend nachgeführt werden. Moderne Satellitenstationen können die Dopplerkompensation automatisch durchführen.

<indepth>
Dieses Applet visualisiert den Dopplereffekt. Mit dem Schieberegler kann die *Relativgeschwindigkeit zwischen Sender und Empfänger* eingestellt werden.
  
- Wenn sich die *Quelle auf den Empfänger zubewegt*, treffen mehr Wellenfronten pro Zeiteinheit ein, was einer *Erhöhung der empfangenen Frequenz* entspricht. Obwohl der Sender immer mit der gleichen Frequenz sendet. 
  
- Wenn sich die *Quelle vom Empfänger wegbewegt*, treffen weniger Wellenfronten pro Zeiteinheit ein, was einer *Erniedrigung der empfangenen Frequenz* entspricht. Obwohl der Sender immer mit der gleichen Frequenz sendet.

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
Der Begriff dB (Dezibel) wird erst im Kapitel [sec:dezibel_1] ausführlich behandelt. Hier genügt es, zu wissen, dass dB eine Verhältniszahl und dBm einen absoluten Leistungspegel darstellt.
Ein stark vereinfachtes Beispiel für einen Downlink von einem LEO-CubeSat zu einer Bodenstation könnte so aussehen:

| Grösse | Beispielwert |
| Frequenz | 145.9 MHz |
| Sendeleistung 1 W | 30 dB<sub>m</sub>  |
| Verluste TX-Kabel und Stecker | −1 dB |
| Gewinn Sendeantenne | +3 dB<sub>i</sub> |
| EIRP | +32 dB<sub>m</sub> |
| Entfernung | 2000 km |
| Freiraumdämpfung | −141.7 dB |
| Gewinn Empfangsantenne | +8 dB<sub>i</sub> |
| Vorverstärker | +15 dB |
| Verluste RX-Kabel und Stecker | −2 dB |
| Leistung am Rx-Eingang| −88.7 dB<sub>m</sub> |
| angenommene Empfängerempfindlichkeit | -104 dB<sub>m</sub>  |
|  |   | 
| Linkmargin  |  +15.3 dB |

In einem echten Linkbudget kommen weitere Faktoren hinzu, z. B. Modulationsart, Datenrate, Empfängerrauschen und Rauschboden.
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
Mit Amateurfunk über Satelliten befassen sich weltweit die AMSAT-Organisationen, in der Schweiz ist das [AMSAT-HB](https://amsat-hb.org/). 
</tip>

