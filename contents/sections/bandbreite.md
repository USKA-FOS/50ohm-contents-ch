IN BEARBEITUNG
%YPA: Issue #11 von ARK beachten.
% Für HB erst ab Zeile 36 relevant. Evtl aus IUARU bandplänen sinnvollen Inhalt "erfinden"

Das Spektrum der elektromagnetischen Wellen stellt eine wertvolle, nicht vermehrbare Ressource dar. Für ein geordnetes Miteinander sind deshalb international und national Frequenzbereiche verschiedenen Nutzern zugeordnet.

Die für den Amateurfunk zulässigen Frequenzen sind in der [Verordnung des BAKOM über die Nutzung des Funkfrequenzspektrums
(VVNF)](https://www.fedlex.admin.ch/eli/cc/2020/914/de) festgelegt und unterscheiden sich für die HB3-Lizenz (Novice) und HB9-Lizenz (CEPT).

Die HB3-Lizenz (Novice) ist im [Artikel 44](https://www.fedlex.admin.ch/eli/cc/2020/1024/de#art_44) beschrieben.
Die HB9-Lizenz (CEPT)  ist XXXXXX

Die vollständige [Verordnung über die Nutzung des Funkfrequenzspektrums(VNF)](https://www.fedlex.admin.ch/eli/cc/2020/1024/de) YYYYYYYY

Aussendungen dürfen nur die für eine einwandfreie Übermittlung notwendige Bandbreite belegen.

Dabei ist auf folgende Punkte zu achten. (Später: Nebenaussendungen und Oberwellen verweisen)

<indepth>
**1.152 notwendige Bandbreite:** Für eine gegebene Emissionsklasse die Breite des Frequenzbandes, die gerade ausreicht, um die Übertragung von Informationen mit der erforderlichen Geschwindigkeit und Qualität unter festgelegten Bedingungen sicherzustellen.

---

### 1. Berechnungsformeln nach Modulationsart (ITU-R SM.1138)
Die notwendige Bandbreite ($B_n$) wird je nach Modulationsart mit spezifischen Formeln berechnet. Hier sind die wichtigsten Standardbeispiele:

* **Amplitudenmodulation (AM – Zweiseitenband, z. B. Rundfunk):**
  Die Formel lautet $B_n = 2 \cdot M$. Dabei steht $M$ für die höchste Modulationsfrequenz in Hertz (bei einer maximalen Audiofrequenz von 4,5 kHz beträgt $B_n$ also 9 kHz).
* **Einseitenbandmodulation (SSB, z. B. Amateurfunk oder Seefunk):**
  Die Formel lautet $B_n = M$. Es wird nur ein Seitenband ohne Träger übertragen, wodurch sich die Bandbreite halbiert (bei 3 kHz Audiofrequenz beträgt $B_n$ genau 3 kHz).
* **Frequenzmodulation (FM, z. B. UKW-Rundfunk oder Sprechfunk):**
  Die Formel lautet $B_n = 2 \cdot M + 2 \cdot D \cdot K$. Hierbei ist $M$ die höchste Modulationsfrequenz, $D$ der maximale Frequenzhub und $K$ ein Korrekturfaktor (meistens $K = 1$).
* **Morsetelegrafie (CW – unmoduliert):**
  Die Formel lautet $B_n = B \cdot K$. Dabei ist $B$ die Telegrafiergeschwindigkeit in Baud und $K$ ein Faktor für die Signalformung (typischerweise $K = 3$ bis $5$).

---

### 2. Unterschied: Notwendige vs. Belegte Bandbreite

Während die **notwendige Bandbreite** ein theoretischer Planungswert ist, beschreibt die **belegte Bandbreite** (*occupied bandwidth*, ITU-Vorschrift Nr. 1.153) die tatsächliche, messbare Leistungsverteilung eines realen Senders im Frequenzspektrum.

| Merkmal | Notwendige Bandbreite (1.152) | Belegte Bandbreite (1.153) |
| :--- | :--- | :--- |
| **Charakter** | Theoretischer Richt- und Planungswert. | Realer, physikalisch messbarer Wert. |
| **Definition** | Mindestbreite für fehlerfreie Übertragung bei geforderter Rate und Qualität. | Frequenzbereich, in dem 99 % der gesamten abgestrahlten Sendeleistung liegen. |
| **Grenzwerte** | Durch Modulationsparameter (Formeln) festgelegt. | Ober- und unterhalb der Grenzen werden jeweils genau **0,5 %** der Gesamtleistung abgestrahlt. |
| **Verwendung** | Frequenzplanung, Lizenzierung und Angabe im Emissionsbezeichner. | Überprüfung von Sendern auf unerwünschte Nebenaussendungen und Störungen. |
</indepth>

<tip>
xxxxxxxx Innerhalb der zugewiesen Frequenzbänder ist es üblich, Betriebsarten nach belegter Bandbreite anzuordnen.
Bild einfügen 
</tip>

Wie wir gelernt haben, hängt die belegte Sendebandbreite von der Modulationsart und bei FM auch noch vom Hub ab. Für die verschiedenen Amateurfunkbänder sind jeweils maximal zulässige Bandbreiten festgelegt. Diese findet man in der [Anlage 1](https://50ohm.de/a1) der Amateurfunkverordnung, aus der wir auch schon die Bandgrenzen entnommen haben. Diese Bandbreiten dürfen nicht überschritten werden. Jeder Funkamateur ist selbst für die Einhaltung verantwortlich.

---

Besonders aufpassen muss man bei Sendungen in der Nähe der Grenzen der Amateurfunkbänder. Ein Beispiel: Nehmen wir an, ein FM-Signal belegt eine Bandbreite von $\qty{15}{\kilo\hertz}$, und wir stellen den Sender auf die untere Bandgrenze des $\qty{70}{\centi\meter}$-Bandes ein, also auf $\qty{430}{\mega\hertz}$. Das Sendesignal befindet sich um die Trägerfrequenz herum, also jeweils $\qty{7,5}{\kilo\hertz}$ unterhalb und oberhalb. Es würde sich also von $\qty{429,9925}{\mega\hertz}$ bis $\qty{430,0075}{\mega\hertz}$ erstrecken. Da das Signal somit zur Hälfte außerhalb des Bandes wäre, dürfen wir nicht auf PTT drücken! Wir müssen also bei FM, aber auch bei AM, immer mindestens einen Abstand von der halben belegten Bandbreite zur Bandgrenze hin einhalten.

<indepth>
[picture:908:n_bandbreite_falsch:Falsch -- Senden außerhalb der Bandgrenzen]
[picture:909:n_bandbreite_richtig:Richtig -- Senden innerhalb der Bandgrenzen]
</indepth>

<indepth>
Bei SSB verhält es sich an der Bandgrenze ein wenig anders. Hier ist das Signal nur auf einer Seite der (unterdrückten) Trägerfrequenz zu finden. Bei LSB ist das Signal vollständig unterhalb der Trägerfrequenz, bei USB ist es vollständig oberhalb der Trägerfrequenz. Wenn man also beispielsweise als Sendefrequenz die obere Bandgrenze einstellt, dann dürfte man mit LSB durchaus senden, da das gesamte Signal innerhalb des Bandes bleibt. Mit USB dürfte man dort allerdings nicht senden, da das gesamte Signal außerhalb des Bandes wäre.
</indepth>

[question:NE305]
[question:BC225]
