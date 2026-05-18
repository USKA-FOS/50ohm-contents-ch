Einen Spannungswandler benötigt man immer dann, wenn eine elektrische Spannung in eine andere Spannung umgewandelt werden soll. Im Amateurfunk kann dies beispielsweise die Erzeugung von $\qty{5}{\volt}$ für einen Mikrocontroller aus einer $\qty{13,8}{\volt}$-Versorgung sein oder die Versorgung eines Laptops mit $\qty{19}{\volt}$ aus einer $\qty{12}{\volt}$-Batterie. Solche Schaltungen bezeichnet man als DC/DC-Wandler. Wird die Spannung erhöht, spricht man von einem Step-UP-Wandler (Hochsetzsteller), wird sie verringert, von einem Step-DOWN-Wandler (Tiefsetzsteller).

Bei jeder Spannungswandlung entstehen Verluste. Deshalb ist die abgegebene Leistung stets kleiner als die zugeführte Leistung. Das Verhältnis aus Ausgangsleistung und Eingangsleistung bezeichnet man als Wirkungsgrad $\eta$:

$ \eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} $

Für die folgenden Fragen muss die Leistungsformel $P = U \cdot I$ angewendet werden, um die Eingangs- und Ausgangsleistung zu berechnen. Anschließend kann der Wirkungsgrad bestimmt werden.

[question:AB213]
[question:AB214]

<indepth>
[photo:300:StepUpWandler: Abwärts- (Buck) Aufwärts- (Boost) Wandler. Hier als Aufwärtsspannungswandler von $\qty{7,2}{\volt}$ auf $\qty{24}{\volt}$ eingestellt]
Dieser Buck-Boost Converter kann von $\qty{0,5}{\volt}$ bis $\qty{25}{\volt}$ am Ausgang eingestellt werden. Die maximale Leistung beträgt $\qty{25}{\watt}$. Da der Wirkungsgrad sehr hoch ist, kommen die Schalttransistoren ohne Kühlkörper aus.  Die Betriebsart Abwärtswandler (Step Down = Buck Mode) oder Aufwärtswandler (Step Up = Boost Mode) kann mit dem rechten Minischalter aktiviert werden.
</indepth>