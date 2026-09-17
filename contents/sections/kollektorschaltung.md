Die Benennung der Grundschaltung eines bipolaren Transistors richtet sich danach, welcher Anschluss (Basis, Kollektor oder Emitter) gemeinsam vom Eingangs- und Ausgangssignal durchflossen wird.

Bei der *Kollektorschaltung* fließt das Eingangssignal von der Quelle über die Basis, den *Kollektor* und die Versorgungsspannung zurück zur Quelle. Das Ausgangssignal fließt vom Kollektor durch die Last (Senke) und über die Versorgungsspannung zurück in den *Kollektor*.

[question:AD401]

Für den Betrieb als linearer Strom-Verstärker benötigt der Transistor in der Kollektorschaltung einen definierten Arbeitspunkt (BIAS), der normalerweise durch einen Spannungsteiler an der Basis festgelegt wird.

Der Emitterwiderstand wandelt den Strom, der durch die Kollektor-Emitter-Strecke fließt, in einen Spannungsabfall um, der am Emitter abgegriffen wird. Der Emitterstrom des Transistors fließt (gemeinsam mit dem normalerweise vernachlässigbaren Basis-Strom-Anteil) über den Emitter durch den Emitterwiderstand gegen Masse. Der Strom durch den Emitterwiderstand verursacht durch den entstehenden Spannungsabfall an diesem eine Erhöhung des Emitterpotenzials (Emitterspannung) und wirkt somit als Gegenkopplung für die Basis-Spannung. Hierdurch wird der Arbeitspunkt des Transistors zusätzlich stabilisiert, weil thermisch bedingte Änderungen des Kollektorstroms hierdurch ausgeregelt werden.

Die Ein- und Auskopplung der Signale an Basis und Emitter erfolgt über sog. Koppelkondensatoren. Diese haben die Aufgabe, Gleichspannungsanteile von der Verstärkerstufe, die zu einer Veränderung des Arbeitspunktes führen würden, fernzuhalten.

Der Abblockkondensator in der Betriebsspannung (+) dient der Abführung von unerwünschten HF- und NF-Signalen, damit Rückkopplungseffekte auf die Stufe und die Versorgungsspannung vermieden werden. Zudem wird der Kollektor durch den Abblockkondensator signalmäßig (für Wechselspannung) auf Ein- und Ausgang gelegt.

Die Phasenverschiebung zwischen Ein- und Ausgangssignal beträgt bei der Kollektorschaltung $\qty{0}{\degree}$, da bei einer positiven Halbwelle in der Eingangsspannung der Emitterstrom steigt und damit der Spannungsabfall am Emitterwiderstand zunimmt. Hierdurch steigt die Spannung am Ausgangskondensator. Es kommt zu einer positiven Halbwelle am Ausgang der Verstärkerstufe.

Die Spannungsverstärkung der Kollektorschaltung bewegt sich bei entsprechender Auslegung im Bereich von $\num{0,9}$ bis $\num{0,98}$ und ist immer etwas kleiner als $1$. Die Stromverstärkung der Kollektorschaltung ist hingegen sehr groß, da die Eingangsimpedanz der Schaltung relativ hoch ist. Die Ausgangsimpedanz ist hingegen sehr niedrig im Vergleich zur Eingangsimpedanz.

[question:AD405]
[question:AD402]
[question:AD403]

Die *Kollektorschaltung wird häufig als Pufferstufe zwischen Oszillator und weiteren Schaltungsteilen*, die den Oszillator ansonsten niederohmig belasten würden, verwendet, um eine Entkopplung und bessere Frequenzstabilisierung des Oszillators zu erreichen.

[question:AD404]

