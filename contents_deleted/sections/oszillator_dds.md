Die Direkte Digitale Synthese (Direct Digital Synthesis oder kurz DDS) dient der Erzeugung periodischer, bandbegrenzter Signale mit hoher Frequenzauflösung.
Neben der Synthese von Signalen mittels PLL-Regelschleifen ist diese Methode der Signalerzeugung heutzutage in der Nachrichten- und Messtechnik weit verbreitet und stellt den aktuellen Stand der Technik dar. Signale sind hierbei in der Frequenz sehr fein einstellbar im Gegensatz zu einer klassischen PLL.

Grundlegendes Funktionsprinzip einer DDS:

Mittels eines Taktgenerators mit fester Frequenz wird ein Adresszähler laufend hochgezählt. Bei Überlauf des Adresszählers startet dieser wieder von vorne. Hierdurch wird eine aufsteigende Folge von binären Werten an dessen Ausgang erzeugt. Mittels dieser Werte wird eine Sinustabelle laufend durchfahren. Hierdurch werden am Ausgang der Sinustabelle digitale Amplitudenwerte für eine Sinusschwingung generiert, die anschließend einem Register übergeben werden. Die digitalen Amplitudenwerte werden dann mittels Taktung des Registers einem nachgeschalteten D/A-Wandler zugeführt, der diese dann in ein analoges Signal (Sinus-Schwingung) umsetzt und ausgibt.

<indepth>
Eine DDS kann auch unterschiedliche Wertetabellen durchfahren, so dass auch beliebige zyklische Signalformen generiert werden können. Durch Steuerung des Adresszählers (mittels eines Tuning-Words), welches die Schrittweite des Zählers laufend beeinflusst, kann die Frequenz, mit der die Wertetabelle durchfahren wird, in weiten Grenzen gesteuert werden.
Für das Adressregister verwendet man oft Register mit $\qty{32}{\bit}$ oder mehr, wovon dann nur eine kleinere Anzahl der höherwertigen Bits (z.B. obere $\qty{14}{\bit}$) für das Durchfahren der Wertetabelle verwendet werden. Hierdurch ist es möglich, auch Bruchteile der Taktfrequenz auszugeben, und die Frequenzauflösung der DDS wird hierdurch erhöht.
Der Vorteil einer DDS gegenüber einer PLL besteht darin, dass durch Steuerung der vorgenannten Parameter eine nahezu beliebige Frequenzauflösung erreicht werden kann. Zudem kann ohne Einschwingvorgang zwischen verschiedenen Frequenzen (durch Steuerung mittels des Tuning-Words) schnell hin und her gewechselt werden.

Die Qualität des Ausgangssignals einer DDS hängt im wesentlichen von der Qualität des verwendeten Taktgenerators ab (Stabilität, Jitter). Zudem ist auch die Amplitudenauflösung (Quantisierung) des D/A-Wandlers und dessen Linearität für die Qualität des Ausgangssignals entscheidend.
</indepth>

[question:AD620]