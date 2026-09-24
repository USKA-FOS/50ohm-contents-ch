*IN ABSCHLUSSREDAKTION DURCH DEN AUTOR*

<attention>
„Der Satellitenfunk wird im HB3-Kurs bereits unter den grundlegenden Vorschriften und der Betriebstechnik behandelt. Die weiterführenden technischen Aspekte werden im HB9-Kurs im Kapitel [sec:satelliten_2] vertieft.“
</attention>

<margin>
[photo:124:n_satellit_oscar1:Modell des ersten Amateurfunksatelliten OSCAR 1, der 1961 für 22 Tage aus dem Orbit der Erde eine Bake im $\qty{2}{\meter}$-Band sendete und von 570 Funkamateuren aus 28 Ländern gehört wurde]
</margin>

---

Satelliten umrunden die Erde in kreisförmigen oder elliptischen Bahnen und in unterschiedlichen Höhen.
Seit 1961 gehören dazu auch Amateurfunksatelliten. Diese werden als OSCAR bezeichnet. Das ist die Abkürzung für "Orbiting Satellite Carrying Amateur Radio" ("Umkreisender Satellit, der Amateurfunk mitführt"). Der erste Amateurfunksatellit wurde OSCAR 1 ([ref:n_satellit_oscar1]) genannt. OSCAR 1 war nur der Anfang. In den Folgejahren - bis heute - wurde eine ganze Reihe immer umfangreicher ausgestatteter Amateurfunknutzlasten ins All gebracht. Wer sich für die Geschichte der Amateurfunksatelliten interessiert, findet in der [History of AMSAT](https://www.amsat.org/amsat-history/) mehr darüber.
[question:BE415]

In diesem Kapitel lernen wir "Was ist ein Amateurfunksatellit?" und "Wie bewegt er sich?". Im Kapitel [sec:satelliten_2] erfahren wir dann "Wie mache ich tatsächlich eine Satellitenfunkverbindung?"

Die mitgeführten Relaisfunkstellen werden als "Transponder" bezeichnet. Die Eingabefrequenz, also die Funkstrecke von der Erde zum Satelliten, wird im Satellitenfunk als "Uplink" bezeichnet. Die Ausgabefrequenz, also die Funkstrecke vom Satelliten zur Erde, wird hingegen "Downlink" genannt. Für Uplink und Downlink werden oftmals unterschiedliche Frequenzbänder benutzt, weil dies eine einfachere Entkopplung von Sende- und Empfangssignal ermöglicht.

<indepth>
*Charakterisierung von Satellitenbahnen (orbits)*

Satellitenbahnen können nach verschiedenen Eigenschaften beschrieben werden. Die Begriffe LEO, MEO und GEO beziehen sich hauptsächlich auf die Bahnhöhe. Begriffe wie HEO oder Polar Orbit beschreiben dagegen andere Eigenschaften der Bahn, insbesondere deren Form oder Neigung. Diese Einteilungen können sich daher überschneiden. Im Folgenden stellen wir die wichtigsten Bahnhöhen bzw. Umlaufbahnen vor.

*Niedrige Umlaufbahnen (Low Earth Orbit - LEO)*
Satelliten in niedrigen Umlaufbahnen befinden sich in Höhen von etwa 400 bis 2'000 Kilometern über der Erdoberfläche. Das sind Umlaufbahnen, die sich relativ nahe an der Erdoberfläche befinden. In diesem Bereich bewegen sich viele Erdbeobachtungs- und Wettersatelliten sowie zahlreiche Amateurfunksatelliten. Die Nähe zur Erde ermöglicht eine hohe Auflösung bei der Erfassung von Daten und Bildern. Die geringe Entfernung zur Erde ermöglicht relativ kurze Funkstrecken und damit geringe Freiraumdämpfung. Gleichzeitig bewegen sich LEO-Satelliten schnell über den Himmel und sind von einer bestimmten Funkstation nur während eines zeitlich begrenzten Überflugs sichtbar.

*Mittlere Umlaufbahnen (Medium Earth Orbit - MEO)*
Mittlere Umlaufbahnen liegen grob zwischen 2'000 und 35'786 Kilometern Höhe. In diesem Bereich befinden sich beispielsweise viele Navigationssatelliten, wie sie für das weltbekannte GPS-System verwendet werden. Da die Satelliten hier länger brauchen, um die Erde zu umkreisen, bieten sie eine ausgeglichene Balance zwischen Abdeckung und Genauigkeit für Navigation und Positionierung. Mit zunehmender Bahnhöhe verlängert sich die Umlaufzeit. Gleichzeitig vergrössert sich das von einem Satelliten erreichbare Gebiet.

*Geostationäre Umlaufbahn (Geostationary Orbit – GEO)*
Eine geosynchrone Umlaufbahn hat eine Umlaufzeit von ungefähr einem siderischen Tag, also 23 Stunden, 56 Minuten und 4 Sekunden. Eine besondere Form davon ist die geostationäre Umlaufbahn (Geostationary Orbit, GEO) in einer Höhe von etwa 35'786 Kilometern über dem Äquator.

Ein geostationärer Satellit bewegt sich auf einer nahezu kreisförmigen Bahn über dem Äquator in derselben Drehrichtung und mit derselben Winkelgeschwindigkeit wie die Erde. Dadurch erscheint er von der Erde aus gesehen nahezu ortsfest am Himmel. Dies ermöglicht es einer Bodenstation, ihre Antenne dauerhaft auf dieselbe Position auszurichten. Geostationäre Satelliten eignen sich daher besonders für Kommunikationsanwendungen und ermöglichen eine konstante Abdeckung eines bestimmten Gebiets.

[QO-100](https://amsat-dl.org/p4-a-nb-transponder-bandplan-und-betriebsrichtlinien/) ist die Amateurfunknutzlast auf dem geostationären Satelliten Es’hail-2 und war die erste Amateurfunknutzlast in einer geostationären Umlaufbahn.

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
* Das *Azimut* ist die Richtung entlang des Horizonts, in die man schaut, um den Satelliten zu sehen. Es wird meist in Grad gemessen und reicht von $\qty{0}{\degree}$ (Norden) über $\qty{90}{\degree}$ (Osten), $\qty{180}{\degree}$ (Süden) bis $\qty{270}{\degree}$ (Westen).
* Die *Elevation* ist der vertikale Winkel, unter dem ein Satellit über dem Horizont steht. Sie wird ebenfalls in Grad gemessen und variiert von $\qty{0}{\degree}$ (direkt am Horizont) bis $\qty{90}{\degree}$ (senkrecht über einem).

<margin>
[picture:876:n_azimut_elevation:Azimut und Elevation im Raum]
</margin>

<wordorigin>
Der Begriff *Azimut* stammt von arabisch *as-sumūt*, ("die Wege") ab. *Elevation* leitet sich vom lateinischen elevare ("erheben") ab.
</wordorigin>

[question:BE413]
[question:BE414]

Im Amateurfunkdienst über Satelliten gilt eine Ausnahme von der Pflicht, nur offene Sprache zu verwenden. Kommandostationen ist es ausnahmsweise erlaubt, Steuersignale zu Amateurfunksatelliten zum Zwecke der Verschleierung zu verschlüsseln. Das heißt, dass hierfür ausnahmsweise Verschlüsselungsverfahren genutzt werden dürfen, die verhindern, dass der Inhalt der Steuersignale von Dritten mitgelesen werden kann. Dies dient der Sicherheit der Satelliten vor Steuerkommandos von Unbefugten.

[question:VA303]
[question:VN026]


%Im deutschen Recht - nicht aber international - gilt diese Regelung auch für die Steuersignale an automatische und fernbediente Stationen sowie Remote-Stationen. Entsprechende Frage VD104 gelöscht.
