Im Gegensatz zur Sprachübertragung benötigen viele digitale Übertragungsverfahren (Digimodes) nur eine sehr geringe Bandbreite. Während Sprachsignale in SSB typischerweise eine Bandbreite von etwa $\qty{2,4}{\kilo\hertz}$ beanspruchen, kommen Digimodes mit deutlich schmaleren Frequenzbereichen aus. So benötigt beispielsweise BPSK31 nur etwa $\qty{31,25}{\hertz}$ Bandbreite, während FT8 mit rund $\qty{50}{\hertz}$ auskommt. Die bei Digimodes erzeugten Signale werden auf Kurzwelle üblicherweise ebenfalls in SSB moduliert. Die HF-Bandbreite des ausgestrahlten Signals entspricht dann genau der NF-Bandbreite des Digimodes.

[question:EE402]
[question:EE403]

Innerhalb der üblichen SSB-Empfangsbandbreite von etwa $\qty{2,4}{\kilo\hertz}$ können mehrere solcher schmalbandigen Digimode-Signale gleichzeitig empfangen werden.

<margin>
[picture:718:e_digimode_ssb_empfang_mehrerer_digimodes:Wasserfalldiagramm vom Empfang von mehreren Digimode-Signalen innerhalb der SSB-Bandbreite von 2,4 kHz. Jede Spalte ist die Übertragung eines anderen Signals]
</margin>

[question:EE404]

Rein rechnerisch lassen sich in einer $\qty{2,4}{\kilo\hertz}$-SSB-Bandbreite bis zu 48 FT8-Signale ($\frac{\qty{2400}{\hertz}}{\qty{50}{\hertz}}$) oder sogar bis zu 76 BPSK31-Signale ($\frac{\qty{2400}{\hertz}}{\qty{31,25}{\hertz}}$) unterbringen. Am Computer kann anschließend entweder gezielt ein einzelnes Digimode-Signal ausgewählt oder – je nach Software – auch eine Vielzahl dieser Signale gleichzeitig dekodiert werden. Genau diese hohe spektrale Effizienz macht schmalbandige Digimodes besonders attraktiv für den Amateurfunkbetrieb.

---

Slow-Scan Television (SSTV) bezeichnet die Übertragung von Standbildern mithilfe digitalisierte Bilddaten. Dabei werden Bilder zeilenweise übertragen, was eine vergleichsweise geringe Übertragungsgeschwindigkeit erlaubt. Es existieren verschiedene SSTV-Verfahren, die sich unter anderem in Auflösung, Farbtiefe und Übertragungsdauer unterscheiden. Ein wesentlicher Vorteil von SSTV ist die geringe benötigte Bandbreite: Sie liegt typischerweise unter $\qty{3}{\kilo\hertz}$ und entspricht damit in etwa der Bandbreite eines SSB-Sprachsignals. Dadurch kann SSTV auch in den Kurzwellenbändern eingesetzt werden und ist besonders für weltweite Bildübertragungen im Amateurfunk geeignet. Abbildung [ref:e_digimode_ssb_sstv] zeigt ein Typisches SSTV-Bild.

Im Gegensatz dazu steht Amateur Television (ATV), bei dem Bewegtbilder – also echtes Fernsehen – übertragen werden. Aufgrund der deutlich höheren Informationsmenge erfordert ATV eine wesentlich größere Bandbreite, typischerweise mehrere Megahertz, oft $\qty{6}{\mega\hertz}$ oder mehr. Aus diesem Grund ist ATV auf den Kurzwellenbändern nicht realisierbar und wird erst in höheren Frequenzbereichen eingesetzt, meist ab dem $\qty{70}{\centi\meter}$-Band aufwärts oder z.B. im $\unit{\giga\hertz}$-Bereich über QO-100. Dort stehen ausreichend breite Frequenzbereiche zur Verfügung, um die für Bewegtbildübertragungen notwendige Bandbreite bereitzustellen.

[question:EE415]

<margin>
[photo:84:e_digimode_ssb_sstv:Bestätigung eines SSTV Verbindung an F1BIB von ON1GA mit dem RST 575 und zusätzlich dem ursprünglich empfangenen Bild]
</margin>
