Mit Hilfe eines Mischers kann eine bestimmte Frequenz (bzw. ein Frequenzbereich mit definierter Bandbreite) in eine höhere oder niedrigere Frequenz umgesetzt werden. Dafür werden die Signale miteinander Multipliziert. 

<indepth>
Eine Multiplikation von Signalen im Zeitbereich führt zu einer Addition (bzw. Subtraktion) im Frequenzbereich. Dieser Zusammenhang lässt sich anschaulich mit der folgenden trigonometrischen Identität (etwas vereinfacht, die Faktoren $2\pi\cdot t$ wurden der Übersicht halber weggelassen) erklären:  
  
$\sin(f_1)\cdot\sin(f_2) = \frac{1}{2}\left(\cos(f_1-f_2)-\cos(f_1+f_2)\right)$
  
Werden zwei Sinussignale miteinander multipliziert – eines mit der Frequenz $f_1$ und eines mit der Frequenz $f_2$ – entstehen im Frequenzbereich zwei neue Cosinussignale (was nichts anderes als ein phasenverschobener Sinus ist). Diese liegen bei den Frequenzen $f_1 - f_2$ und $f_1 + f_2$. Man kann sich das so vorstellen, dass ein Frequenzanteil nach unten und ein weiterer nach oben verschoben wird. Genau dieses Prinzip macht sich der Mischer zunutze.

Dabei entstehen grundsätzlich immer zwei Frequenzkomponenten. In der Praxis ist jedoch meist nur eine davon erwünscht, weshalb im Anschluss an den Mischer geeignete Filter eingesetzt werden, um das gewünschte Mischprodukt zu selektieren. Genau genommen können bei der Differenzbildung auch negative Frequenzen auftreten, weshalb man im Allgemeinen den Betrag $| f_1 \pm f_2 |$ betrachtet.
</indepth>

---

Ein Mischer nutzt nichtlineare Bauelemente, beispielsweise Dioden, um Signale miteinander zu multiplizieren. Dabei entstehen sogenannte Mischprodukte, deren Frequenzen mathematisch der Summe und der Differenz der Frequenzen der Eingangssignale entsprechen.

Aufgrund dieser Eigenschaft werden Mischer gezielt eingesetzt, um Signale in andere, gewünschte Frequenzbereiche umzusetzen – etwa zur Hoch- oder Heruntermischung in Sendern und Empfängern. In Blockschaltbildern wird ein Mischer, wie in Abbildung [ref:e_mischer] dargestellt, durch einen Kreis mit einem Multiplikationszeichen symbolisiert, das auf die multiplikative Wirkung dieser Baugruppe hinweist.

<margin>
[picture:903:e_mischer:Mischer]
</margin>

---

Die an einem Ausgang eines Mischers erzeugten Frequenzen bestehen hierbei vorwiegend aus den beiden Mischprodukten der zugeführten Signale $f_\text{e}$, dem Eingangssignal und $f_\text{o}$ dem Signal was von einem Oszillator kommt. Hierbei ergeben sich zwei erwünschte Mischprodukte als Summe und Betrag der Differenz der zugeführten Signale:

$f_\text{z}=|f_\text{e}\pm f_\text{o}|$

Wegen des $\pm$ muss eine Fallunterscheidung getroffen werden: Es ergibt sich somit $f_\text{z1} = f_\text{e}+f_\text{o}$ sowie $f_\text{z2}=|f_\text{e}-f_\text{o}|$.

Die Betragsstriche $|x|$ bedeuten, dass nur der Zahlenwert ohne Vorzeichen betrachtet wird. Ist $x$ negativ, wird es positiv gemacht. Ist $x$ bereits positiv, bleibt es unverändert.

Normalerweise wird nur eines der erwünschten Mischprodukte für die weitere Signalverarbeitung genutzt. Das andere Mischprodukt (sowie ggf. weitere unerwünschte Mischprodukte - siehe Vertiefung) müssen anschließend durch Filterung aus dem Signalgemisch entfernt werden.

<indepth>
Ein realer Mischer erzeugt neben den erwünschten Mischprodukten auch Mischprodukte höherer Ordnung wie z.B. $2 * f_\text{in1} + f_\text{in2}$ usw. Diese unerwünschten Mischprodukte müssen anschließend ebenfalls durch geeignete Filter entfernt werden. Auch die beiden Eingangsfrequenzen sind bei realen Mischern in deren Ausgangssignal nicht vollständig unterdrückt und müssen bei der weiteren Signalverarbeitung berücksichtigt werden. Durch Verwendung eines balancierten Ringmischers (Balance-Mixer) können die beiden Eingangssignale im Ausgangssignal sehr stark unterdrückt werden, weshalb dieser Mischer-Typ häufig zum Einsatz kommt.
</indepth>

[question:EF201]

Bei dieser Frage müssen wir einfach nur die Oszilatorfrequenz einmal addieren und einmal subtrahieren und dabei den Betrag beachten.

$f_\text{z1} = f_\text{e}+f_\text{o} = \qty{21}{\mega\hertz} + \qty{31,7}{\mega\hertz} = \qty{52,7}{\mega\hertz}$

$f_\text{z2}=|f_\text{e}-f_\text{o}| =|\qty{21}{\mega\hertz} - \qty{31,7}{\mega\hertz}| = |\qty{-10,7}{\mega\hertz}| = \qty{10,7}{\mega\hertz}$

Die folgenden Fragen funktionieren nach dem gleichen Prinzip.

[question:EF202]
[question:EF203]
[question:EF204]
[question:EF205]

Da in Mischern verschiedenste Frequenzen durch den Mischvorgang erzeugt werden, müssen *Mischstufen immer sehr gut geschirmt werden*, damit von diesen keine Abstrahlung in andere Stufen oder Geräte erfolgen kann und insbesondere andere Funkdienste nicht gestört werden!

[question:EF206]