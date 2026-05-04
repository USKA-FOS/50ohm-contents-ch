Die Benennung der Grundschaltung eines bipolaren Transistors richtet sich danach, welcher Anschluss (Basis, Kollektor oder Emitter) gemeinsam vom Eingangs- und Ausgangssignal durchflossen wird.

Bei der *Emitterschaltung* fließt das Eingangssignal von der Quelle über die Basis, den *Emitter* und die Masse zurück zur Quelle. Das Ausgangssignal fließt vom Kollektor durch die Last (Senke) und über die Masse zurück in den *Emitter*.

[question:AD409]

%TODO: Schaubild mit Stromläufen evtl. einfügen.

Funktionsweise eines Verstärkers in Emitterschaltung:

%TODO: Bild Emitterschaltung mit Spannungsteiler und Koppelkondensatoren einfügen

Für den Betrieb als linearer Spannungs-Verstärker benötigt der Transistor in der Emitterschaltung einen definierten Arbeitspunkt (BIAS), der normalerweise durch einen Spannungsteiler an der Basis festgelegt wird.

[question:AD411]

Der Kollerktorwiderstand wandelt den Strom, der durch die Kollektor-Emitter-Strecke, fließt in einen Spannungsabfall um, der am Kollektor abgegriffen wird. Der Kollektorstrom des Transistors fließt (gemeinsam mit dem normalerweise vernachlässigbaren Basis-Strom-Anteil) über den Emitter durch den Emitterwiderstand gegen Masse. Der Strom durch den Emitterwiderstand verursacht durch den entstehenden Spannungsabfall an diesem eine Erhöhung des Emitterpotenzials (Emitterspannung) und wirkt somit als Gegenkopplung für die Basis-Spannung. Hierdurch wird der Arbeitspunkt des Transistors zusätzlich stabilisiert, weil thermisch bedingte Änderungen des Kollektorstroms hierdurch ausgeregelt werden.

Um die Gegenkopplung für die Verstärkung von Wechselspannungssignalen möglichst gering zu halten, wird der Emitterwiderstand kapazitiv (durch einen Kondensator) überbrückt.

[question:AD413]

Die Ein- und Auskopplung der Signale an Basis und Kollektor erfolgt über sog. Koppelkondensatoren. Diese haben die Aufgabe, Gleichspannungsanteile von der Verstärkerstufe, die zu einer Veränderung des Arbeitspunktes führen würden, fernzuhalten.

[question:AD412]

Der Abblockkondensator in der Betriebsspannung (+) dient der Abführung von unerwünschten HF- und NF-Signalen, damit Rückkopplungseffekte auf die Stufe und die Versorgungsspannung vermieden werden.

Die Phasenverschiebung zwischen Ein- und Ausgangssignal beträgt bei der Emitterschaltung $\qty{180}{\degree}$, da bei einer positiven Halbwelle in der Eingangsspannung der Kollektorstrom steigt und damit der Spannungsabfall am Kollektorwiderstand zunimmt. Hierdurch sinkt die Spannung am Ausgangskondensator. Es kommt zu einer negativen Halbwelle am Ausgang der Verstärkerstufe.

[question:AD407]
[question:AD408]

Wird eine Emitterschaltung wie in der folgenden Frage ohne Arbeitspunktvoreinstellung durch einen Spannungsteiler betrieben, so erfolgt die Ansteuerung des Transistors allein durch das zugeführte Eingangssignal. Erst wenn dieses den Wert von ca. $\qty{0,6}{\volt}$ überschreitet, wird die Basis-Emitter-Strecke des Transistors leitend. Hierdurch fließt nur in den Spannungsspitzen ein Kollektorstrom, der einen Spannungsabfall am Ausgang hervorruft. Als Ausgangssignal erscheint die Versorgungsspannung, welche zu den Zeiten, zu denen der Transistor in den leitfähigen Bereich kommt, abfällt. So erklärt sich das entsprechende Ausgangssignal.

[question:AD406]

Die Spannungsverstärkung der Emitterschaltung bewegt sich bei entsprechender Auslegung im Bereich von $100\dots 300$ und ist damit hoch. Wird jedoch der Emitterkondensator entfernt, so sinkt der Verstärkungsfaktor der Schaltung erheblich. Er wird letztlich nur noch durch das Verhältnis von Kollektorwiderstand zu Emitterwiderstand definiert.

[question:AD414]
[question:AD415]
[question:AD410]









