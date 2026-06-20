Wir Menschen sind es gewohnt, die zehn Ziffern von $\num{0}$ bis $\num{9}$ zu benutzen. Man spricht von einem Zehnersystem oder Dezimalsystem.

Für Computer ist es hingegen einfacher, mit nur $\num{2}$ Ziffern zu arbeiten: der $\num{0}$ und der $\num{1}$. Dies entspricht zwei Zuständen: Beispielsweise ausgeschaltet und eingeschaltet, "Transistor gesperrt" und "Transistor leitend" oder auch $\qty{0}{\volt}$ und $\qty{5}{\volt}$. Es entsteht ein binäres Zahlensystem oder Dualsystem.

[question:EA201]

Das Zählen geht in allen Zahlensystemen gleich (siehe Tabelle [ref:binaer_zahlensysteme]): Man fängt bei $\num{0}$ an und zählt die Ziffern hoch. Wenn der Ziffernvorrat zu Ende ist, fängt man von vorne an und schreibt dabei vor jede Zahl eine $\num{1}$. Deshalb kommt im Dezimalsystem nach der $\num{9}$ die $\num{10}$. Die Ziffer ganz rechts hat den Wert, den sie selbst darstellt. Man nennt das den Stellenwert $\num{1}$. 

---

Im Dezimalsystem ist die zweite Ziffer von rechts zehnmal so viel Wert wie sie selbst, hat also den Stellenwert $\num{10}$. Jede weiter links stehende Stelle ist jeweils zehnmal so viel Wert, wie die rechts daneben stehende. Beispielsweise bedeutet die Dezimalzahl $\num{5573}$ aus der Tabelle [ref:binaer_stellenwert_dezimal] also eigentlich $5 \cdot 1000 + 5 \cdot 100 + 7 \cdot 10 + 3 \cdot 1$.

<margin>
|c: |c: |c: |c: |
|$\num{1000}$ | $\num{100}$ | $\num{10}$ | $\num{1}$ |
| $\num{5}$ | $\num{5}$ | $\num{7}$ | $\num{3}$ |
[table:binaer_stellenwert_dezimal:Stellenwerte der vierstelligen Dezimalzahl $\num{5573}$]

|r: Dezimal | r: Dual |
| $\num{0}$ | $\num{0}$ |
| $\num{1}$ | $\num{1}$ |
| $\num{2}$ | $\num{10}$ |
| $\num{3}$ | $\num{11}$ |
| $\num{4}$ | $\num{100}$ |
| $\num{5}$ | $\num{101}$ |
| $\num{6}$ | $\num{110}$ |
| $\num{7}$ | $\num{111}$ |
| $\num{8}$ | $\num{1000}$ |
| $\num{9}$ | $\num{1001}$ |
| $\num{10}$ | $\num{1010}$ |
| $\num{11}$ | $\num{1011}$ |
| $\num{12}$ | $\num{1100}$ |
| $\num{13}$ | $\num{1101}$ |
| $\num{14}$ | $\num{1110}$ |
| $\num{15}$ | $\num{1111}$ |
[table:binaer_zahlensysteme:Zahlen im Dezimal- und im Dualsystem]
</margin>

Im Binärsystem gibt es nur zwei Ziffern, nämlich $\num{0}$ und $\num{1}$. Wie in Tabelle [ref:binar_stellenwert_dual] zu sehen ist, hat die erste Stelle von rechts den Stellenwert $\num{1}$, die zweite $\num{2}$, die dritte $\num{4}$, die vierte $\num{8}$ und so weiter. Die Stellenwerte verdoppeln sich, statt sich zu verzehnfachen, weil es nur zwei Ziffern gibt und nicht zehn. Eine Stelle im Binärsystem nennt man auch Bit ($\unit{\bit}$).

|c: |c: |c: |c: |c: |c: |c: |c: |
| $\num{128}$ | $\num{64}$ | $\num{32}$ | $\num{16}$ | $\num{8}$ | $\num{4}$ | $\num{2}$ | $\num{1}$ |
| $\num{1}$ | $\num{0}$ | $\num{0}$ | $\num{0}$ | $\num{1}$ | $\num{1}$ | $\num{1}$ | $\num{0}$ |
[table:binar_stellenwert_dual:Stellenwerte der achtstelligen Dualzahl $\num{10001110}$]

Wenn man die Stellenwerte kennt, ist das Übertragen von Binärzahlen in das Dezimalsystem einfach. Nehmen wir ein Beispiel aus Tabelle [ref:binar_stellenwert_dual]. Die Bimärzahl $\num{10001110}$ soll in eine Dezimalzahl umgerechnet werden.

1. Man schreibt über jede Ziffer der Binärzahl ihren Stellenwert.
2. Man addiert alle Stellenwerte, unter denen eine $\num{1}$ steht: $128+8+4+2=142$

[question:EA206]
[question:EA207]
[question:EA208]

Auf dem Papier kann man Binärzahlen mit so vielen Bits schreiben, wie man gerade braucht. In der Digitaltechnik ist das anders. Die Hard- oder Software gibt eine bestimmte Stellenzahl vor, die man auch Breite nennt. Beispielsweise haben Mikrocontroller oder Computer häufig Breiten von $\num{8}$, $\num{16}$, $\num{32}$ oder $\qty{64}{\text{Bits}}$. In der Darstellung werden Binärzahlen oft vorne mit Nullen aufgefüllt, bis diese Breite erreicht ist. Am Wert der Zahl ändert das nichts.

[question:EA205]

Eine feste Breite begrenzt den Wertebereich. Mit einem Bit sind zwei Werte möglich ($\num{0}$ und $\num{1}$), mit zwei Bits schon vier ($\num{00}$, $\num{01}$, $\num{10}$ und $\num{11}$) und mit jedem weiteren Bit jeweils doppelt so viele. Mit $n$ Bits lassen sich $2^n$ verschiedene Zahlen darstellen.

[question:EA204]
[question:EA202]
[question:EA203]
