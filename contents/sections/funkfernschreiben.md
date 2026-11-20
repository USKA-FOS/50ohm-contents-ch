Für die Kommunikation mittels Funkfernschreiben zwischen Amateurfunkstationen gibt es verschiedenste Verfahren. Damit eine Verbindung zustande kommt, müssen beide Kommunikationspartner das gleiche Übertragungsverfahren und die gleichen Parameter verwenden. Das gilt um so mehr, weil nicht jedem Verfahren eindeutige Frequenzbereiche zugeordnet sind.

%[photo:0:n_funkfernschreiben_telegraphie_20m:Morsetelegrafie, FT8 und FT4 im $\qty{20}{\meter}$-Band]
%[photo:0:n_funkfernschreiben_digimodes:Häufig verwendete Digimodes von K1JT vergrößert im Wasserfalldiagramm]
%[photo:0:n_funkfernschreiben_olivia:Ausschnitt aus einer Olivia-Aussendung im Wasserfalldiagramm]
%[photo:0:n_funkfernschreiben_fm:Musterbild FM]
%[photo:0:n_funkfernschreiben_am:Musterbild AM]
%[photo:0:n_funkfernschreiben_ft8:Ein FT8-Signal bei $\qty{1500}{\hertz}$ oberhalb der eingestellten Frequenz]
%[photo:0:n_funkfernschreiben_ft8_20m:Mehrere FT8-Signale in einem SSB-Kanal im $\qty{20}{\meter}$-Band]

Seitlich ist ein üblicher Ablauf einer kurzen Telegrafieverbindung dargestellt. Mit der Tabelle [ref:n_funkfernschreiben_abkuerzungen] kann die Bedeutung dahinter entschlüsselt werden.

<qso>
CQ CQ CQ DE HB4CY HB4CY HB4CY PSE K
> HB4CY DE HB9ARK K
HB9ARK DE HB4CY = UR RST 599 599 = HB9ARK DE HB4CY K
> HB4CY DE HB9ARK = TNX RPRT, UR 479 479 BK
BK QSL = VY 73 DE HB4CY SK
> R 73 DE HB9ARK SK
</qso>

<webmargin>
| l: | X: |
| Abkz. | Bedeutung |
| CQ | Allgemeiner Anruf |
| QSL | Ich bestätige den Empfang |
| R | Received (Empfangsbestätigung) |
| K | Aufforderung zum Senden |
| BK | Unterbrechung der Sendung; Formlose Übergabe (vom Englischen "Break")  |
| RPRT | Rapport (vom Englischen „Report“) |
| RST | RST-Rapport |  
| UR | du bist (im Sinne von "dein Signal ist", vom Englischen "you are") |
| DE | von |
| PSE | Bitte (vom Englischen "Please") |
| TNX | Danke (vom Englischen "Thanks") |
| SK | Ende der Verbindung (vom Englischen "Silent Key") |
| VY | sehr (vom Englischen "very") |
| 73 | viele Grüße |
| = | Trennzeichen |
[table:n_funkfernschreiben_abkuerzungen:Betriebliche Abkürzungen in der Telegrafie]
</webmargin>

<tip>
Eine vollständige Liste befindet sich in [sec:betriebliche_abkuerzungen]
</tip>

<indepth>
*Funkfernschreiben (RTTY, Radio Teletype)*

**Historische Bedeutung**

Das Funkfernschreiben hatte historisch eine grosse Bedeutung bei der
Nachrichtenübermittlung. Es wurde insbesondere im internationalen
Handel, für Hotel- und Flugreservationen, bei Nachrichtenagenturen sowie
in der militärischen Telekommunikation eingesetzt.

Mit dem Funkfernschreiben konnten geschriebene Nachrichten über
Funkverbindungen zwischen räumlich weit entfernten Teilnehmern
ausgetauscht werden. Es stellte damit eine frühe Form der digitalen
Datenübertragung über Funk dar.

Im englischen Sprachgebrauch wird das klassische Funkfernschreiben als
*Radio Teletype (RTTY)* bezeichnet.

**Funktionsprinzip und Modulation**

RTTY verwendet das Modulationsverfahren Frequency Shift Keying (FSK).
Dabei werden zwei unterschiedliche Frequenzen zur Übertragung digitaler
Informationen verwendet.

Den beiden Frequenzen sind die binären Zustände 0 und 1 zugeordnet:

-   **Mark:** Frequenz für den binären Zustand 1.
-   **Space:** Frequenz für den binären Zustand 0.

Die Differenz zwischen den beiden Frequenzen wird als **Shift**
bezeichnet.

Die einzelnen Bits einer Nachricht werden zeitlich hintereinander
übertragen. Während der Übertragung wechselt das Sendesignal
entsprechend der zu übertragenden Bitfolge zwischen den beiden
Frequenzen.

Man unterscheidet dabei zwischen zwei technischen Realisierungen:

-   **FSK:** Der Sender verändert unmittelbar seine Sendefrequenz
    zwischen Mark und Space.
-   **AFSK (Audio Frequency Shift Keying):** Zwei unterschiedliche
    Audiofrequenzen werden erzeugt und über einen SSB-Sender übertragen.
    Durch die Einseitenbandmodulation entsteht daraus die entsprechende
    Frequenzverschiebung des HF-Signals.

**Zeichencodierung**

Das klassische RTTY verwendet den 5-Bit-Code ITA2 (International
Telegraph Alphabet No. 2), der auch als Baudot-Code bekannt ist.

Mit fünf Bits lassen sich 32 unterschiedliche Codekombinationen
darstellen. Das reicht nicht aus, um gleichzeitig Grossbuchstaben,
Ziffern und Sonderzeichen abzubilden.

Deshalb verwendet ITA2 zwei Zeichensätze:

-   **Letters:** Grossbuchstaben
-   **Figures:** Ziffern und Sonderzeichen

Zwischen diesen beiden Zeichensätzen wird mit speziellen Steuerzeichen
(LTRS und FIGS) umgeschaltet.

RTTY überträgt die Zeichen asynchron. Jedes Zeichen wird durch ein
Startbit eingeleitet und durch Stopbits abgeschlossen. Ein typischer
Übertragungsrahmen besteht aus:

-   1 Startbit (Space)
-   5 Datenbits
-   1,5 Stopbits (Mark)

Die Übertragung erfolgt somit nicht als kontinuierlicher,
synchronisierter Datenstrom, sondern jedes einzelne Zeichen besitzt
seine eigene zeitliche Rahmung. Die Abbildung [ref:Baudotzeichen] zeigt die Umsetzung der beispielhaften Bitfolge `1 0 1 0 1` in zwei unterschiedliche Frequenzen.

[picture:10103:Baudotzeichen:Serielle Übertragung der Bits]

**Übertragungsgeschwindigkeit**

Die Übertragungsgeschwindigkeit wird in Baud angegeben. Ein Baud
entspricht einem übertragenen Symbol pro Sekunde.

Im Amateurfunk sind insbesondere folgende Einstellungen gebräuchlich:

-   45,45 Baud
-   170 Hz Shift

Wichtig ist die Unterscheidung zwischen Baud [sec:symbole_symbolrate] und Zeichen pro Minute. Bei
45,45 Baud und dem üblichen RTTY-Zeichenrahmen (7,5 Bitzeiten pro
Zeichen) ergibt sich eine Übertragungsleistung von ungefähr 6 Zeichen
pro Sekunde, was etwa 73 Worte pro Minute ergibt und sich gut eignet für die direkte
Kommunikation zwischen Menschen über eine Tastatur.

**Fehleranfälligkeit**

Das klassische RTTY besitzt keine integrierte Fehlerkorrektur (Forward
Error Correction, FEC). Auch eine Fehlererkennung ist im eigentlichen
Übertragungsprotokoll nicht vorgesehen.

Wird ein Bit aufgrund von Störungen falsch erkannt, kann daraus
unmittelbar ein falsches Zeichen entstehen. Besonders problematisch ist
der Verlust eines Umschaltzeichens (LTRS oder FIGS), da dadurch auch
nachfolgende Zeichen falsch interpretiert werden können.

Die Zuverlässigkeit der Übertragung hängt deshalb wesentlich von der
Qualität der Funkverbindung und der korrekten Einstellung des Empfängers
beziehungsweise Decoders ab.
</indepth>

[question:NE401]

Die Abwicklung einer Telegrafie-Verbindung erfolgt sowohl bei der Morsetelegrafie als auch mit dem Computer ähnlich wie im Sprechfunk, aber mit bestimmten Abkürzungen. Diese Abkürzungen vereinfachen die Abwicklung und verkürzen die Übertragungsdauer. Es gibt auch die sogenannten Q-Gruppen. Das sind weltweit einheitliche dreibuchstabige Abkürzungen, die immer mit dem Buchstaben Q beginnen. Darauf gehen wir im Kapitel Q-Gruppen und Locator näher ein.

[question:BB101]

---

%Vertiefungsbox erstellen mit der 2. Bedeutung von SK (verstorben). Die gibt es in einem andern Abschnitt bereits. Von dort kopieren. ARK: an einem Ort genügt es.

Es gibt auch digitale Übertragungsverfahren, bei denen die Abwicklung anders erfolgt. FT8 oder FT4 funktionieren beispielsweise auch bei widrigen Funkbedingungen, also wenn beim Empfänger im Vergleich zum Grundrauschen lediglich eine niedrige Signalstärke erreicht werden kann. Dafür können bei den genannten Verfahren aber nur ganz wenige Zeichen je Sendung übertragen werden. Entsprechend ist die Abwicklung noch kompakter. Andere digitale Verfahren übertragen gar keine Texte, sondern beispielsweise Bilder oder Video, mit an diese Umstände angepasster Betriebsabwicklung. Darauf wird in der Prüfung aber nicht eingegangen.

[question:BE112]
[question:BB109]
[question:BB110]
[question:BB108]

---

RTTY ist ein vergleichsweise einfaches digitales Übertragungsverfahren,
bei dem Informationen durch die Umschaltung zwischen zwei Frequenzen
übertragen werden. Es besitzt eine geringe Bandbreite und ist technisch
relativ einfach zu realisieren.

---

## Moderne digitale Betriebsarten

Moderne digitale Betriebsarten wie JS8Call und VARA/VARAC gehen
wesentlich weiter: Sie nutzen komplexere Modulationsverfahren und
Mechanismen zur Fehlerkorrektur beziehungsweise zur Wiederholung
fehlerhafter Datenübertragungen. Dadurch ermöglichen sie auch unter
schwierigen Ausbreitungsbedingungen eine zuverlässigere Kommunikation.


Im Amateurfunk werden heute neben dem klassischen RTTY verschiedene
moderne digitale Betriebsarten eingesetzt, die eine wesentlich
zuverlässigere Datenübertragung ermöglichen.

---

Zwei Beispiele sind:

**JS8Call**

JS8Call ist eine auf FT8 aufbauende digitale Kommunikationsanwendung.
Sie verwendet eine speziell entwickelte Mehrton-FSK-Modulation (8-FSK)
und eine leistungsfähige Fehlerkorrektur.

Im Gegensatz zu FT8, das primär für kurze standardisierte
Funkverbindungen und den Austausch von Stationsinformationen entwickelt
wurde, ermöglicht JS8Call den Austausch frei formulierter
Textnachrichten. Damit ist auch eine Tastatur-zu-Tastatur-Kommunikation
möglich.

---

**VARA HF / VARAC**

VARA HF ist ein Softwaremodem für die digitale Datenübertragung über
Kurzwelle. Es verwendet adaptive Modulationsverfahren und passt die
Übertragungsparameter an die aktuellen Eigenschaften des Funkkanals an.

Ein wesentliches Merkmal ist das Verfahren ARQ (Automatic Repeat
reQuest): Werden Datenblöcke nicht korrekt empfangen, fordert die
Gegenstation deren erneute Übertragung an.

VARAC ist eine Chat-Anwendung, welche das VARA-Modem für die
Kommunikation zwischen Funkstationen nutzt.
