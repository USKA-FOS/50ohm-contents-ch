In der Klasse E haben wir bereits kennengelernt, wie sich Kondensatoren in Reihen- und Parallelschaltung verhalten. Im vorherigen Kapitel wurde außerdem die Reihenschaltung von Spulen behandelt. In diesem Kapitel betrachten wir nun die Parallelschaltung von Spulen und Kondensatoren. Zunächst wiederholen wir jedoch noch einmal die grundlegenden Zusammenhänge bei Parallel- und Reihenschaltungen von Kapazitäten.

In Parallelschwingkreisen werden Spulen und Kondensatoren miteinander kombiniert. Dabei besitzt auch eine reale Spule eine gewisse Eigenkapazität. Diese entsteht beispielsweise durch die Wicklungen der Spule und die dadurch vorhandenen elektrischen Feldkopplungen zwischen den Windungen.

Für eine möglichst genaue Berechnung der Resonanzfrequenz müssen diese "unsichtbaren" Kapazitäten berücksichtigt werden. In der folgenden Aufgabe können die Kapazitäten der Kondensatoren und die Eigenkapazität der Spule direkt addiert werden, da sie parallel zueinander liegen.

Besonders wichtig ist dabei, auf die unterschiedlichen Einheiten zu achten. Vor der Berechnung sollten daher alle Werte in dieselbe Einheit umgerechnet werden, damit die Kapazitäten korrekt addiert werden können.

[question:AD103]

Bei der folgenden Aufgabe sind drei Kondensatoren in Reihe geschaltet. In der Klasse E haben wir gelenrt, dass sich bei Kondensatoren in Reihenschaltung die Kehrwerte der Kapazitäten addieren:

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

Auch hier müssen die Kapazitäten vor der Berechnung in die gleiche Einheit umgerechnet werden, damit die Kehrwerte korrekt addiert werden können.

[question:AD101]

---

In Wechselstromschaltungen treten neben den bekannten ohmschen Widerständen auch Blindwiderstände auf, wie wir sie bereits bei Kondensatoren und Spulen kennengelernt haben. Der normale ohmsche Widerstand wird als Wirkwiderstand $R$ bezeichnet. Blindwiderstände werden mit $X$ beschrieben. Beide Widerstandsarten beeinflussen den Stromfluss in der Schaltung gleichzeitig.

Da Wirk- und Blindwiderstand unterschiedlich wirken, können sie nicht einfach addiert werden. Stattdessen werden sie geometrisch zusammengesetzt. Man kann sich dies wie ein rechtwinkliges Dreieck wie in Abbildung [ref:a_dreieck] vorstellen:

---

- Der Wirkwiderstand $R$ bildet die waagerechte Seite.
- Der Blindwiderstand $X$ bildet die senkrechte Seite.
- Der daraus entstehende Gesamtwiderstand wird als Scheinwiderstand $|Z|$ bezeichnet.

<margin>
[picture:1067:a_dreieck:Rechtwinkliges Dreieck zur Veranschaulichung der Berechnung des Scheinwiderstandes $|Z|$ aus Wirkwiderstand $R$ und Blindwiderstand $X$]
</margin>

Der Scheinwiderstand lässt sich mit dem Satz des Pythagoras berechnen (vgl. Formelsammlung):

$ |Z| = \sqrt{R^2 + X^2} $

Der Buchstabe $Z$ wird für die sogenannte Impedanz verwendet. Für die Berechnungen in diesem Kapitel genügt es jedoch, den Betrag $|Z|$ als gesamten Wechselstromwiderstand der Schaltung zu betrachten.

<indepth>
Für mathematisch Interessierte: Die Impedanz $Z$ ist eine komplexe Größe, die den Wirkwiderstand $R$ als Realteil und den Blindwiderstand $X$ als Imaginärteil enthält:

$Z = R + jX$

Der Betrag $|Z|$ entspricht dann der Länge des Vektors in der komplexen Ebene, der durch die Kombination von $R$ und $X$ entsteht.
</indepth>

Für die nächste Frage muss, bevor wir den Satz des Pythagoras anwenden können, der Blindwiderstand $X_C$ des Kondensators bei $\qty{1}{\mega\hertz}$ berechnet werden. Dazu verwenden wir die Formel für den Blindwiderstand eines Kondensators.

[question:AD104]

Die nächste Frage beschäftigt sich mit der Berechnung des Scheinwiderstandes einer Reihenschaltung von einem Widerstand und einer Spule. Zunächst berechnen wir $X_L$, danach wenden wir wieder den Satz des Pythagoras an. Auch hier müssen die Zehnerpotenzen beachtet werden, damit die Berechnung korrekt durchgeführt werden kann.

[question:AD105]
