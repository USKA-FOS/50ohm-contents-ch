Die Brückenschaltung ist eine Anordnung aus vier Widerständen, die unter anderem zur präzisen Widerstandsmessung eingesetzt wird. Ein bekanntes praktisches Beispiel ist die Wheatstone-Messbrücke. Die Schaltung besteht aus zwei parallel geschalteten Spannungsteilern. Zwischen den Mittelpunkten der beiden Spannungsteiler befindet sich der sogenannte Brückenzweig, an dem die Brückenspannung $U_\mathrm{AB}$ gemessen werden kann.

<margin>
[picture:343:a_Brückenschaltung:Typische Brückenschaltung mit 4 Widerständen]
</margin>

Besonders interessant ist der Fall der abgeglichenen Brücke. Dieser liegt vor, wenn die Spannungsteilerverhältnisse auf beiden Seiten gleich groß sind. Dann besitzen die beiden Mittelpunkte dasselbe elektrische Potential und es fließt kein Strom durch den Brückenzweig beziehungsweise das angeschlossene Messinstrument.

Dabei müssen die einzelnen Widerstände nicht denselben Wert besitzen. Entscheidend ist lediglich, dass das Verhältnis der Widerstände auf beiden Seiten übereinstimmt.

Für den abgeglichenen Zustand gilt daher:

$ U_\mathrm{AB} = \qty{0}{\volt} $

und damit:

$ \frac{R_1}{R_2} = \frac{R_3}{R_4} $

Die Wheatstone-Brücke eignet sich deshalb besonders gut zur Bestimmung unbekannter Widerstände oder kleiner Widerstandsänderungen. Wie genau das funktioniert, wird in der nebenstehenden Vertiefung beschrieben.

<indepth>
Der Sonderfall, dass die Spannungsteilerverhältnisse in der Brückenschaltung links und rechts gleich groß sind, wird zur Messung unbekannter Widerstände angewendet. Charles Wheatstone (britischer Physiker) erkannte bereits 1833 die Bedeutung der Brückenschaltung für die Messung unbekannter Widerstände. 

Bei der Messung wird ein einstellbarer Präzisionswiderstand so lange verändert, bis das empfindliche Messwerk im Brückenzweig keinen Stromfluss mehr anzeigt. Dann ist die Brücke abgeglichen, und man kann den Wert des unbekannten Widerstandes mithilfe der Skala und des Messbereichsmultiplikators ermitteln.

Ein Beispiel sieht man in der Abbildung [ref:a_pontavi]. Hier gibt es einen Multiplikator der Werte von 0,1/1/10/100 annehmen kann. Für die Feineinstellung gibt es den Großen Drehknopf. 
[photo:286:a_pontavi:Widerstandsmessbrücke nach Wheatstone (Pontavi)]

Die Abbildung [ref:a_pontavi_schaltung] zeigt den verinfachten Schaltplan dieses Messgeräts. An der Stelle $X$ wird der unbekannte Widerstand angeschlossen. Zunächst stellt man mit dem Multiplikator die geschätzte Größenordnung des unbekannten Widerstandes ein. Dann wird mit dem Großen Drehknopf der Präzisionswiderstand so lange verändert, bis die Brücke abgeglichen ist. Das Messwerk zeigt dann an, dass kein Strom mehr durch den Brückenzweig fließt.

[picture:1076:a_pontavi_schaltung:Schaltplan Widerstandsmessbrücke (Pontavi)]
</indepth>

[question:AD111]

Da bei der folgenden Aufgabe alle Widerstände gleich groß sind, müssen auch die Spannungsteilerverhältnisse gleich sein. Dies entspricht dem beschriebenen Sonderfall.

[question:AD112]

In der folgenden Frage trifft der Sonderfall nicht zu, da die Spannungsteilerverhältnisse ungleich sind. Es sind zwar ähnliche Widerstände vorhanden, jedoch von oben nach unten betrachtet vertauscht. Die Aufgabe kann mit dem Wissen zum unbelasteten Spannungsteiler gelöst werden.

[question:AD113]

Auf der linken Seite finden wir das Verhältnis $\qty{1}{\kilo\ohm}$ zu $\qty{10}{\kilo\ohm} = 1/10$.
Unter der Voraussetzung, dass das Messwerk sehr hochohmig oder abgeklemmt ist, messen wir bei einer Betriebsspannung von $\qty{11}{\volt}$ auf der linken Seite am oberen Widerstand ($R_1$) genau $\qty{1}{\volt}$ und am unteren Widerstand ($R_2$) $\qty{10}{\volt}$. Das Potenzial am Messpunkt A beträgt somit $\qty{10}{\volt}$ gegen Masse gemessen.

Auf der rechten Seite finden wir das Verhältnis $\qty{10}{\kilo\ohm}$ zu $\qty{1}{\kilo\ohm} = 10/1$ und messen deshalb $\qty{10}{\volt}$ am oberen Widerstand ($R_3$) und $\qty{1}{\volt}$ am unteren Widerstand ($R_4$). Das Potenzial am Messpunkt B beträgt somit $\qty{1}{\volt}$ gegen Masse gemessen.

Der Potenzialunterschied zwischen A und B beträgt damit $\qty{9}{\volt}$, wobei der Messpunkt A um $\qty{9}{\volt}$ positiver als der Messpunkt B ist.
