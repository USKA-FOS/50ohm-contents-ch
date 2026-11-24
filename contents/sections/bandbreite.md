Das Spektrum der elektromagnetischen Wellen stellt eine wertvolle, nicht vermehrbare Ressource dar. Für ein geordnetes Miteinander sind deshalb international und national Frequenzbereiche verschiedenen Nutzern zugeordnet.

<law>
Berechtigungen aufgrund von Fähigkeitszeugnissen
[VNF Art. 44–46](https://www.fedlex.admin.ch/eli/cc/2020/1024/de#art_44)

Frequenzbereiche für HB3 und HB9
[VVNF Art. 6 und Anhang 4](https://www.fedlex.admin.ch/eli/cc/2020/914/de#annex_4)
</law>

Die Voraussetzungen für die Teilnahme am Amateurfunkdienst sind in [Artikel 44](https://www.fedlex.admin.ch/eli/cc/2020/1024/de#art_44) der [Verordnung über die Nutzung des Funkfrequenzspektrums (VNF)](https://www.fedlex.admin.ch/eli/cc/2020/1024/de) beschrieben. Dort werden das *Fähigkeitszeugnis für den Amateurfunk* (HB9, CEPT) und der *Einsteigerausweis für Funkamateurinnen und Funkamateure* (HB3, Novice) unterschieden. Artikel 45 VNF legt fest, welche Betriebsarten mit welchem Fähigkeitszeugnis erlaubt sind, und nach Artikel 46 VNF bestimmt das BAKOM, welche Frequenzbereiche dem Amateurfunk zur Verfügung stehen.

Die für den Amateurfunk zulässigen Frequenzbereiche sind im [Anhang 4](https://www.fedlex.admin.ch/eli/cc/2020/914/de#annex_4) der [Verordnung des BAKOM über die Nutzung des Funkfrequenzspektrums (VVNF)](https://www.fedlex.admin.ch/eli/cc/2020/914/de) festgelegt, getrennt für die HB9- und die HB3-Lizenz (siehe [sec:frequenzzuteilung]).

Aussendungen dürfen nur die für eine einwandfreie Übermittlung notwendige Bandbreite belegen. Dieser Grundsatz stammt aus dem Radioreglement (RR) der ITU, auf dem auch der nationale Frequenzzuweisungsplan (NaFZ) beruht (Art. 3 VNF).

Dabei ist auf folgende Punkte zu achten:

* Die gewählte Betriebsart bestimmt die belegte Bandbreite: CW benötigt weniger als SSB, SSB weniger als AM oder FM.
* Die gesamte Aussendung muss innerhalb der zugeteilten Frequenzbereiche liegen, also auch in der Nähe der Bandgrenzen.
* Die Empfehlungen des IARU-Bandplans [sec:iaru_bandplan] zu Betriebsarten und Bandbreiten sollen eingehalten werden. Die Abbildung [ref:n_bandplan_20m] zeigt die Aufteilung der Betriebsarten innerhalb eines Amateurfunkbands exemplarisch für das 20-Meterband. 
* Unerwünschte Aussendungen wie Nebenaussendungen und Oberwellen müssen vermieden werden (siehe [sec:unerwuenschte_aussendungen_1]).

<indepth>
Die notwendige Bandbreite für eine gegebene Modulationsart ist die Breite des Frequenzbandes, die gerade ausreicht, um die Übertragung von Informationen mit der erforderlichen Geschwindigkeit und Qualität unter festgelegten Bedingungen sicherzustellen.

**Berechnungsformeln nach Modulationsart (ITU-R SM.1138)**
Die notwendige Bandbreite ($B_n$) wird je nach Modulationsart mit spezifischen Formeln berechnet. Hier sind die wichtigsten Standardbeispiele:

* *Amplitudenmodulation (AM – Zweiseitenband, z. B. Rundfunk):*
  Die Formel lautet $B_n = 2 \cdot M$. Dabei steht $M$ für die höchste Modulationsfrequenz in Hertz (bei einer maximalen Audiofrequenz von 4,5 kHz beträgt $B_n$ also 9 kHz).
  
* *Einseitenbandmodulation (SSB, z. B. Amateurfunk):*
  Die Formel lautet $B_n = M$. Es wird nur ein Seitenband ohne Träger übertragen, wodurch sich die Bandbreite halbiert (bei 3 kHz Audiofrequenz beträgt $B_n$ genau 3 kHz).
  
* *Frequenzmodulation (FM, z. B. UKW-Radio oder Sprechfunk):*
  Die Formel lautet $B_n = 2 \cdot M + 2 \cdot D \cdot K$. Hierbei ist $M$ die höchste Modulationsfrequenz, $D$ der maximale Frequenzhub und $K$ ein Korrekturfaktor (meistens $K = 1$).
  
* *Morsetelegrafie (CW – getasteter Träger ohne Modulation):*
  Die Formel lautet $B_n = B \cdot K$. Dabei ist $B$ die Telegrafiergeschwindigkeit in Baud und $K$ ein Faktor für die Signalformung (typischerweise $K = 3$ bis $5$).

Während die **notwendige Bandbreite** ein theoretischer Planungswert ist, beschreibt die **belegte Bandbreite** die tatsächliche, messbare Leistungsverteilung eines realen Senders im Frequenzspektrum.
</indepth>

<tip>
Innerhalb der zugewiesenen Frequenzbänder ist es üblich, Betriebsarten nach belegter Bandbreite anzuordnen.
Das ist keine behördliche Vorschrift, sondern eine Empfehlung des IARU-Bandplans (siehe [sec:iaru_bandplan]). Wer sich jedoch über diese Usanz hinwegsetzt, macht sich auf den Bändern äusserst unbeliebt. Abbildung [ref:n_bandplan_20m] zeigt das Beispiel des 20-m-Bands.
</tip>

Wie wir gelernt haben, hängt die belegte Sendebandbreite von der Modulationsart und bei FM auch noch vom Hub ab. Anders als in manchen anderen Ländern legt die Schweiz im Anhang 4 der VVNF für die Amateurfunkbänder keine maximal zulässigen Bandbreiten fest, sondern nur die Frequenzbereiche, ihren Status und die maximale Senderleistung. Umso wichtiger sind der Grundsatz der notwendigen Bandbreite und die Bandbreitenempfehlungen des IARU-Bandplans. Jeder Funkamateur ist selbst dafür verantwortlich, dass seine Aussendungen diese Vorgaben einhalten.

---

Besonders aufpassen muss man bei Sendungen in der Nähe der Grenzen der Amateurfunkbänder. Ein Beispiel: Nehmen wir an, ein FM-Signal belegt eine Bandbreite von $\qty{15}{\kilo\hertz}$, und wir stellen den Sender auf die untere Bandgrenze des $\qty{70}{\centi\meter}$-Bandes ein, also auf $\qty{430}{\mega\hertz}$. Das Sendesignal befindet sich um die Trägerfrequenz herum, also jeweils $\qty{7,5}{\kilo\hertz}$ unterhalb und oberhalb. Es würde sich also von $\qty{429,9925}{\mega\hertz}$ bis $\qty{430,0075}{\mega\hertz}$ erstrecken. Da das Signal somit zur Hälfte ausserhalb des Bandes wäre, dürfen wir nicht auf PTT drücken! Wir müssen also bei FM, aber auch bei AM, immer mindestens einen Abstand von der halben belegten Bandbreite zur Bandgrenze hin einhalten.

<indepth>
[picture:908:n_bandbreite_falsch:Falsch -- Senden ausserhalb der Bandgrenzen]
[picture:909:n_bandbreite_richtig:Richtig -- Senden innerhalb der Bandgrenzen]
</indepth>

<indepth>
Bei SSB verhält es sich an der Bandgrenze ein wenig anders. Hier ist das Signal nur auf einer Seite der (unterdrückten) Trägerfrequenz zu finden. Bei LSB ist das Signal vollständig unterhalb der Trägerfrequenz, bei USB ist es vollständig oberhalb der Trägerfrequenz. Wenn man also beispielsweise als Sendefrequenz die obere Bandgrenze einstellt, dann dürfte man mit LSB durchaus senden, da das gesamte Signal innerhalb des Bandes bleibt. Mit USB dürfte man dort allerdings nicht senden, da das gesamte Signal ausserhalb des Bandes wäre.
</indepth>

[picture:10104:n_bandplan_20m:20-m-Band nach IARU-Bandplan Region 1 mit maximalen Bandbreiten]

[question:NE305]
[question:BC225]
