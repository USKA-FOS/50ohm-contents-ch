Die Brückenschaltung ist eine Schaltung aus 4 Widerständen, die für Widerstandsmessungen eingesetzt werden kann. Ein Beispiel aus der Praxis ist die Messbrücke nach Wheatstone.
%todo Bild einer Wheatstone Messbrücke
Die Messbrücke besteht immer aus zwei Spannungsteilern, die parallel geschaltet sind.
[picture:343:a_Brückenschaltung:Typische Brückenschaltung mit 4 Widerständen]
In dem Sonderfall, dass die Spannungsteilerverhältnisse links und rechts gleich groß sind, fließt durch das Messinstrument,  im sogenannten Brückenzweig, kein Strom.
Die Widerstandswerte können unterschiedliche Werte aufweisen, wichtig ist, dass das Spannungsteilerverhältnis links und rechts gleich sein muss.

In einer Formel dargestellt lautet dieser Zusammenhang: $\frac{R_1}{R_2} = \frac{R_3}{R_4}$
---
[question:AD111]
<tip>
In der Mitte der Schaltung lässt sich die sogenannte Brückenspannung abgreifen.
Für den Sonderfall, dass die Spannungsteilerverhältnisse gleich groß sind, ergibt sich die Brückenspannung zu Null Volt
</tip>

<indepth>
[photo:286:a_Pontavi:Widerstandsmessbrücke nach Wheatstone (Pontavi)]
 Der Sonderfall, dass die Spannungsteilerverhältnisse in der Brückenschaltung links und rechts gleich groß sind, wird zur Messung unbekannter Widerstände angewendet. Charles Wheatstone (britischer Physiker) erkannte bereits 1833 die Bedeutung der Brückenschaltung zur Messung unbekannter Widerstände. Bei der Messung wird ein einstellbarer Präzisionswiderstand solange verändert, bis das empfindliche Messwerk im Brückenzweig keinen Stromfluss mehr anzeigt. Dann ist die Brücke abgeglichen und man kann den Wert des unbekannten Widerstandes mit Hilfe der Skala und des Messbereichsmultiplikators ermitteln. 
</indepth>

[question:AD112]

Da bei der Aufgabe alle Widerstände gleich groß sind, müssen auch die Spannungsteilerverhältnisse gleich sein. Dies entspricht dem beschriebenen Sonderfall.

In der folgenden Frage trifft der Sonderall nicht zu, da die Spannungsteilerverhältnisse ungleich sind.
Es sind zwar ähnliche Widerstände vorhanden, aber von oben nach unten betrachtet vertauscht.

---
[question:AD113]
<tip>
Es ist sehr hilfreich, sich die Schaltung zu skizzieren und die Spannungspotenziale einzutragen. Danach sieht man deutlicher den Potenzialunterschied zwischen A und B.
</tip>

<margin>
Auf der linken Seite finden wir was Verhältnis $\qty{1}{\kilo\ohm}$ zu $\qty{10}{\kilo\ohm} = 1/10$.
Unter der Voraussetzung, dass das Messwerk sehr hochohmig oder abgeklemmt ist, messen wir bei $\qty{11}{\volt}$ Betriebsspannung auf der linken Seite am oberen Widerstand ($R_1$) genau $\qty{1}{\volt}$ und am unteren Widerstand ($R_2$) $\qty{10}{\volt}$. Das Potenzial am Messpunkt A beträgt somit $\qty{10}{\volt}$ gegen Masse gemessen.
Auf der rechten Seite finden wir was Verhältnis $\qty{10}{\kilo\ohm}$ zu $\qty{1}{\kilo\ohm} = 10/1$ und messen deshalb $\qty{10}{\volt}$ am oberen Widerstand ($R_3$) und $\qty{1}{\volt}$ am unteren Widerstand ($R_4$). Das Potenzial am Messpunkt B beträgt somit $\qty{1}{\volt}$ gegen Masse gemessen.
Der Potenzialunterschied zwischen A und B beträgt $\qty{9}{\volt}$, wobei der Messpunkt A um $\qty{9}{\volt}$ positiver als der Messpunkt B ist
</margin>

%todo Zusammenfassung, Formelsammlung