<margin>
[picture:542:n_digital_voice_repeaternetwork:Repeaternetzwerk für Digital Voice: Relaisfunkstelle DB0FZ mit Internetanschluss, Hotspot DN9YI und Relaisfunkstelle DB0HOB mit Richtfunkanbindung an DB0FZ]
</margin>

Auch Sprache kann digital übertragen werden, z. B. mit den Übertragungsverfahren DMR, D-Star, C4FM und M17. Dies kann, je nach Verfahren, mit einem Computer oder auch mit einem dafür geeigneten Funkgerät erfolgen. Damit kann man über vernetzte VHF- oder UHF-Relaisfunkstellen mit Funkamateuren auf der ganzen Welt funken. Wenn zwei oder mehr Relaisfunkstellen vernetzt sind, können Sendungen, die von einer der Funkstellen empfangen wurden, über ein Netzwerk, z. B. das HAMNET oder das Internet, weitergeleitet und auf anderen verbundenen Stationen wieder ausgestrahlt werden. Um sich den Zugriff auf einen solchen Relaisverbund zu ermöglichen, kann man auch zu Hause einen sogenannten Hotspot betreiben. Solange keine entsprechende Genehmigung für eine fernbediente Station vorliegt, darf der Betrieb eines Hotspots nur als besetzte Station erfolgen, d. h. man muss den Sender abschalten, wenn er nicht vor Ort beaufsichtigt wird. Auf Kurzwelle werden digitale Sprachverbindungen hauptsächlich direkt hergestellt, beispielsweise mit FreeDV.

<webmargin>
| l: Abkürzung | X: Übertragungsverfahren |
| D-STAR | Digital Smart Technologies for Amateur Radio |
| C4FM | Continuous 4-level frequency modulation |
| DMR | Digital Mobile Radio |
| M17 | Open-Source Übertragungsverfahren |
[table:n_dv_uebertragungsverfahren:Häufig genutzte Übertragungsverfahren für digitalen Sprechfunk]
</webmargin>

[question:NE404]

---

Bei digitaler Sprachübertragung werden die Sprachsignale vor der Übertragung in einen Datenstrom umgewandelt. Mehrere solcher Datenströme können auch in schnell abwechselnder, periodischer Folge übertragen werden. Das nennt man TDMA (Time Division Multiple Access) oder Zeitmultiplexverfahren. So nutzen zwei oder mehr Sprachverbindungen quasi gleichzeitig dieselbe Frequenz. Für ein Funkgerät bedeutet das, dass es bei gedrückter PTT-Taste ständig schnell zwischen Sende- und Empfangsbetrieb umschalten muss, damit es den Takt nicht verliert. 

<margin>
[picture:474:n_digital_voice_tdma:TDMA mit drei Verbindungen auf einer Frequenz]
</margin>

<tip>
Die meisten externen Leistungsverstärker können nicht so schnell zwischen Sende- und Empfangsbetrieb umschalten, wie es für TDMA notwendig wäre. Daher dürfen für DMR und andere Verfahren, die Zeitslots verwenden, ausschließlich dafür geeignete Leistungsverstärker verwendet werden. Ansonsten kommt es dazu, dass die Frequenz nicht nur während des eigenen Zeitslots belegt wird. Das kann Sendungen anderer Stationen auf derselben Frequenz stören.
</tip>

[question:NE403]

---

Im Gegensatz zu analogen Sendungen, bei denen meist nur Frequenz und Modulationsart für die Herstellung einer Verbindung zu einem anderen Teilnehmer bekannt sein müssen, sind für digitale Sprache oft mehr Einstellungen zu berücksichtigen, beispielsweise Sprechgruppe, Raum oder Reflektor zum Zusammenschalten von Relaisfunkstellen oder der zu nutzende TDMA-Zeitschlitz.

<indepth>
Je nach Verfahren kann es auch eine Vielzahl weiterer Einstellungen geben, beispielsweise bei DMR den Color-Code, mit dem sich mehrere Nutzergruppen eine Frequenz teilen können, ohne sich gegenseitig zu hören. Solche Parameter müssen vor Beginn einer Verbindung korrekt am Gerät eingestellt werden, damit diese zustande kommt.
</indepth>

[question:NE402]

Über VHF/UHF-Handfunksprechgeräte und über Relaisstellen werden neben FM-Sprechfunk oft auch die digitalen Verfahren DMR, D-Star oder C4FM verwendet.

[question:NE307]

% TODO: Auf die Tabelle wird nicht eingegangen und sie ist nicht komplett ... 
%<webmargin>
%| l: Verfahren | l: Eigene Kennung | l: Gruppenruf | l: Direktruf | X: Sonstige |
%| M17 | Rufzeichen | - | Rufzeichen | Channel Access Number (CAN), Übertragungsrate (1600 oder 3200 Bit/s) |
%| FreeDV | - | - | - | Mode (1600, 700C, 700D, 700E, 2020) |
%| DMR | DMR-ID | Talkgroup | DMR-ID | Color-Code (1 bis 4, im Amateurfunk meist 1), Zeitschlitz (TS 1 oder TS 2) |
%| C4FM | Rufzeichen | Reflektor | - | |
%| D-Star | Rufzeichen | ? | ? | |
%[table:n_digital_voice_verfahren:Verfahren für Digital Voice und mögliche Einstellungen]
%</webmargin>

<latexonly>
\newpage
</latexonly>