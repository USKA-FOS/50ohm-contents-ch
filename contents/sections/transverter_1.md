*Konverter* und *Transverter* werden im Amateurfunk eingesetzt, um mit vorhandenen Funkgeräten zusätzliche Frequenzbereiche zu erschließen, die diese Geräte ursprünglich nicht abdecken. Ein *Konverter* setzt das Signal dabei nur in eine Richtung um, entweder im Sendepfad oder im Empfangspfad. Ein *Transverter* hingegen verfügt über eine interne Sende-/Empfangsumschaltung und übernimmt die Frequenzumsetzung sowohl im Sende- als auch im Empfangsbetrieb. Die Frequenzumsetzung bei Konvertern und Transvertern erfolgt hierbei immer durch Mischung in einem oder mehreren Mischern.

Beispielsweise kann man mit einem entsprechenden Transverter und einem vorhandenen Kurzwellen-Transceiver z.B. auch Betrieb im VHF/UHF/SHF-Bereich machen. Hierbei würde man z. B. das $\qty{10}{\meter}$-Band des Kurzwellen-Transceivers mittels eines Transverters auf $\qty{2}{\meter}$/$\qty{70}{\centi\meter}$ oder $\qty{23}{\centi\meter}$ in beide Richtungen umsetzen.

[question:EF501]
[question:EF502]

---

Betrachten wir im ersten Schritt das Blockschaltbild eines Konverters in Abbildung [ref:e_konverter]. Ein solcher Konverter könnte beispielsweise dazu verwendet werden, ein Signal aus einem VHF-Funkgerät für den Amateurfunksatelliten QO-100 umzusetzen, der eine Eingangsfrequenz im $\qty{2,4}{\giga\hertz}$-Band benötigt. Ein Transverter ist hier ggf. nicht nötig, da der Empfang über einen SDR-Stick und ein LNB erfolgt.

Aus dem Blockschaltbild ist ersichtlich, dass ein definierter Eingangsfrequenzbereich mithilfe mindestens eines Mischers auf einen anderen Ausgangsfrequenzbereich umgesetzt wird. Eine Sende- und Empfangsumschaltung ist dabei nicht vorgesehen. Ein Konverter kann daher ein Signal nur in eine Richtung umsetzen, entweder im Empfangs- (RX) oder im Sendepfad (TX). Bei Konvertern für den Sendebetrieb ist häufig eine PTT-Steuerung vorhanden, die im Sendefall die Verstärkerstufen des Konverters aktiviert.

Auf welches Frequenzband ein Konverter das Signal umsetzt, lässt sich aus der dem Mischer zugeführten Oszillatorfrequenz sowie der Ein- oder Ausgangsfrequenz rechnerisch bestimmen. Im konkreten Beispiel ergibt sich die Zielfrequenz aus dem Mischprodukt von
$\qty{144}{\mega\hertz} + \qty{2,256}{\giga\hertz} = \qty{2,4}{\giga\hertz}$,
wobei das gewünschte Produkt anschließend durch geeignete Filter selektiert wird.

<margin>
[picture:651:e_konverter:Konverterschaltung z. B. Für QO-100]
</margin>

[question:EF504]

---

Die Schaltung eines Transverters lässt sich gut von der eines Konverters unterscheiden. Die Abbildungen [ref:e_transverter_rx] und [ref:e_transverter_tx] zeigen das Blockdiagramm eines Transverters, der es ermöglicht, mit einem $\qty{10}{\meter}$-Kurzwellen-Transceiver auf dem $\qty{2}{\meter}$-Band Betrieb zu machen. Dazu werden eine Sende-/Empfangsumschaltung sowie zwei Mischer und zwei getrennte Signalpfade verwendet – jeweils einer für den Empfangs- (RX) und einer für den Sendebetrieb (TX).

Der TX-Zweig setzt im Sendefall das Ausgangssignal des Transceivers auf das gewünschte höhere Frequenzband um, während der RX-Zweig im Empfangsfall das von der Antenne kommende Signal auf das für den Transceiver geeignete Frequenzband heruntermischt. Zwischen welchen Frequenzbändern der Transverter arbeitet, lässt sich durch Kenntnis der Oszillatorfrequenz, die den Mischern zugeführt wird, sowie der jeweiligen Ein- und Ausgangsfrequenzen rechnerisch bestimmen. Diese Zusammenhänge sind in den Abbildungen dargestellt.

Der quarzstabilisierte Oszillator ($G$) erzeugt eine Frequenz von $\qty{38,666}{\mega\hertz}$, die mithilfe eines 1:3-Frequenzvervielfachers auf $\qty{116}{\mega\hertz}$ erhöht wird. Im Empfangsfall, dargestellt in Abbildung [ref:e_transverter_rx], wird das Eingangssignal aus dem Frequenzbereich $\qtyrange{144}{146}{\mega\hertz}$ auf den Bereich $\qtyrange{28}{30}{\mega\hertz}$ heruntergemischt. Im Sendefall, gezeigt in Abbildung [ref:e_transverter_tx], wird das Ausgangssignal des Funkgeräts aus dem Bereich $\qtyrange{28}{30}{\mega\hertz}$ auf den Frequenzbereich $\qtyrange{144}{146}{\mega\hertz}$ hochgemischt. Wie üblich kommen in beiden Signalpfaden geeignete Filter zur Selektion der gewünschten Mischprodukte zum Einsatz, die hier aus Gründen der Übersichtlichkeit nicht eingezeichnet sind.

[question:EF503]

<margin>
[picture:842:e_transverter_rx:Transverter im RX-Pfad]
[picture:843:e_transverter_tx:Transverter im TX-Pfad]
</margin>

Transverter und Konverter, die für hohe Eingangs- oder Ausgangsfrequenzen (im GHz-Bereich) ausgelegt werden, müssen über einen sehr stabilen Oszillator verfügen. Fehler in der Oszillatorfrequenz führen durch interne Frequenzvervielfachung aufgrund der hohen Ausgangsfrequenzen bei schmalbandigen Betriebsarten oder SSB zu unannehmbaren Abweichungen in der Zielfrequenz. Eine Abweichung in der Oszillatorfrequenz wird durch deren Vervielfachung ebenfalls vervielfacht. Oft verwendet man einen sog. TCXO oder OCXO, der auch zusätzlich noch über eine externe Referenzquelle synchronisiert werden kann (z.B. GPS), um die Oszillatorfrequenz möglichst gut zu stabilisieren und Abweichungen in der Zielfrequenz klein zu halten.

[question:EF505]