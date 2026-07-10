---

Viele Funkgeräte verfügen über einen sogenannten DATA-Anschluss, der häufig auch als *DATA* oder *$\qty{9600}{\baud}$* gekennzeichnet ist, wie in Abbildung [ref:e_9600_port] dargestellt. Dieser Port wurde ursprünglich für Packet-Radio-Anwendungen entwickelt, die heute weitgehend durch HAMNET abgelöst wurden. Nichtsdestotrotz lässt sich dieser Anschluss auch für andere Verfahren nutzen, etwa für das digitale Sprachübertragungsverfahren M17. In diesem Fall wird ein entsprechendes Modem – oft auch als TNC bezeichnet – angeschlossen, wie in Abbildung [ref:m17_tnc] dargestellt.

<margin>
[photo:303:e_9600_port:Funkgerät mit DATA-Port]
[photo:185:m17_tnc:Module M17 ein TNC für das M17 Übertragungsverfahren]
</margin>

Der $\qty{9600}{\baud}$-Anschluss bietet eine direkte Verbindung zum Modulator und Demodulator des Transceivers, um die Signale mit hoher Präzision und geringen Verzerrungen zu verarbeiten. Für höhere Datenraten, wie sie bei digitalen Signalen z. B. im $\qty{9600}{\baud}$-Packet-Radio (AX.25-Protokoll) verwendet werden, ist es notwendig, den gesamten Audiopfad mit seinen begrenzten Frequenzgang und Filterungen zu umgehen (z.B. Mikrofonfilter und Vorverstärker). Der Audio-Pfad eines Transceivers ist normalerweise auf Sprachsignale abgestimmt und hat eine eingeschränkte Bandbreite, die oft zwischen $\qty{300}{\hertz}$ und $\qty{3000}{\hertz}$ liegt. Diese Bandbreite reicht nicht aus, um $\qty{9600}{\baud}$ zuverlässig zu übertragen, da eine so hohe Rate eine größere Signalbreite benötigt. Über den Datenanschluss werden die Signale ohne die Filter, DSP-Verarbeitung und den De-Emphasis-Prozess übertragen, die im Audiopfad vorhanden sind. Das reduziert Verzerrungen und Latenzen, was für digitale Übertragungen kritisch ist, um die Fehlerquote zu minimieren. 

Zusammengefasst: Der $\qty{9600}{\baud}$-Anschluss ist speziell dafür gedacht, digitale Daten direkt und ohne die Einschränkungen des Audio-Wegs zu verarbeiten, was für zuverlässige und effiziente Hochgeschwindigkeits-Datenübertragung erforderlich ist.


---

In den Folgenden Fragen wird ein FM transceiver verwendet. Zum Senden sollten der DATA-Port vor den FM-Modulator angeschlossen werden und beim Empfang nach dem FM-Demodulator.

[question:EF309]
[question:EF219]

<indepth>
Warum eigentlich $\qty{9600}{\baud}$?
  
$\qty{9600}{\baud}$ ($\qty{9,6}{\kilo\bit\per\second}$, wenn eine Modulation mit einem Bit pro Symbol verwendet wird) ist eine gängige Geschwindigkeit für digitale Kommunikation im Amateurfunk, insbesondere im Packet-Radio. Diese Datenrate stellt einen Kompromiss zwischen erreichbarer Geschwindigkeit und der technischen Machbarkeit im VHF/UHF-Frequenzbereich dar, wo die meisten FM-Transceiver arbeiten.
</indepth>