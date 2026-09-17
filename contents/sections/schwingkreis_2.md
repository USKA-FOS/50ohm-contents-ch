In der Formelsammlung finden wir die folgende Formel für die Berechnung der Grenzfrequenz von RC-Gliedern, z.B. von Hoch- oder Tiefpassfiltern:

$f_g = \frac{1}{2 \pi \cdot R \cdot C}$

Mit dieser Formel können wir eine Reihe von Prüfungsfragen lösen.

<indepth>
Für mathematisch interessierte Leser: Die Formel für die Grenzfrequenz eines RC-Gliedes lässt sich auch durch die Betrachtung der komplexen Impedanzen von Widerstand und Kondensator herleiten. Wir betrachten den RC-Tiefpass als frequenzabhängigen Spannungsteiler.

[picture:175:a_rc_tiepass:RC-Tiefpass als frequenzabhängiger Spannungsteiler]

Für das Verhältnis von Ausgangs- zu Eingangsspannung gilt:

$\frac{|U_A|}{|U_E|} = \frac{|X_C|}{|R + X_C|}$

Der kapazitive Blindwiderstand des Kondensators lautet:

$X_C = \frac{1}{j\omega C}$

Damit ergibt sich:

$\frac{|U_A|}{|U_E|} = \frac{\left|\frac{1}{j\omega C}\right|}{\left|R + \frac{1}{j\omega C}\right|}$

Für die Beträge erhalten wir:

$\frac{|U_A|}{|U_E|} = \frac{\frac{1}{\omega C}}{\sqrt{R^2 + \frac{1}{\omega^2 C^2}}}$

Multipliziert man Zähler und Nenner mit $\omega C$, vereinfacht sich der Ausdruck zu:

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{1 + R^2\omega^2 C^2}}$

Die Grenzfrequenz ist so definiert, dass die Ausgangsspannung auf den Faktor $\frac{1}{\sqrt{2}} \approx 0{,}707$ des ursprünglichen Wertes abgefallen ist. Dies entspricht etwa $\qty{70}{\percent}$ der Ausgangsspannung bzw. einem Pegelabfall von $\qty{3}{\dB}$.

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{2}}$

Daraus folgt:

$\frac{1}{\sqrt{1 + R^2\omega^2 C^2}} = \frac{1}{\sqrt{2}}$

Damit muss gelten:

$R^2\omega^2 C^2 = 1$

und somit:

$\omega R C = 1$

Mit $\omega = 2\pi f$ ergibt sich:

$2\pi f_g R C = 1$

Daraus folgt für die Grenzfrequenz:

$f_g = \frac{1}{2\pi R C}$
</indepth>

[question:AD201] 
[question:AD202] 
[question:AD203] 

---

Der Betragsfrequenzgang eines Serienschwingkreises aus einem Widerstand, einer Spule und einem Kondensator, wie in Abbildung [ref:a_serienschwingkreis] dargestellt, berechnet sich nach folgender Formel:
  
$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$

<margin>
[picture:181:a_serienschwingkreis:Serienschwingkreis]
</margin>

---

Wenn der Blindwiderstand der Spule genau so groß ist wie der Blindwiderstand des Kondensators, also $X_\text{L} = X_\text{C}$, dann ergibt sich für die Impedanz:

$Z=\sqrt{R^2+\left(0\right)^2}=\sqrt{R^2}=R$

In diesem Fall handelt es sich um die sogenannte *Resonanzfrequenz* $f_0$ des Schwingkreises, bei der die Impedanz nur noch durch den ohmschen Widerstand bestimmt wird. Bei Frequenzen über und unter der Resonanzfrequenz ist die Impedanz größer als der ohmsche Widerstand, da entweder die Spule oder der Kondensator einen höheren Blindwiderstand hat. Abbildung [ref:a_serienschwingkreis_frequenzgang] zeigt den Betragsfrequenzgang eines Serienschwingkreises, bei dem die Resonanzfrequenz deutlich zu erkennen ist. Bei Frequenzen über und unter der Resonanzfrequenz haben wir beim Serienschwingkreis daher jeweils einen hohen Gesamtwiderstand (Impedanz). Bei hoher Frequenz hat die Spule einen hohen Widerstand. Bei niedriger Frequenz hat der Kondensator einen hohen Widerstand. 

<margin>
[picture:1037:a_serienschwingkreis_frequenzgang:Betragsfrequenzgang eines Serienschwingkreises]
</margin>

[question:AD206]
[question:AD207] 
[question:AD204] 

Bei Parallel- und Serienschwingkreisen gilt im Resonanzfall, wie oben gezeigt, also folgender Zusammenhang:

$X_\text{C} = X_\text{L}$

Wenn wir nun die Formeln für die Blindwiderstände von Spule und Kondensator in die obige Gleichung einsetzen, erhalten wir:

$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$
  
So ergibt sich die Formel: 
  
$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$

---

Diese Formel heißt Thomsonsche Schwingungsformel und gilt sowohl für Parallel- als auch für Serienschwingkreise. In der Formelsammlung finden wir sie beim Thema "Schwingkreise". Sie besagt, dass die Resonanzfrequenz eines Schwingkreises nur von der Induktivität der Spule und der Kapazität des Kondensators abhängt. Ohmsche Widerstände und Verluste haben keinen Einfluss auf die Resonanzfrequenz. Mit der Formel können wir die Resonanzfrequenz von Schwingkreisen berechnen. 

<indepth>
Ohmsche Widerstände in Parallel- und Serienschwingkreisen wirken sich jedoch auf die Güte ($Q$) und damit auf die Bandbreite ($B$) des Schwingkreises aus - hierauf werden wir später noch genauer eingehen.
</indepth>


[question:AD208] 
[question:AD209]
[question:AD210] 

---

Die Resonanzfrequenz von Parallelschwingkreisen wird genau wie bei Serienschwingkreisen mit der zuvor genannten Thomsonschen Schwingungsformel berechnet. 

[question:AD211] 
[question:AD212] 

---

Um die Resonanzfrequenz von Schwingkreisen zu verändern, kann entweder die Induktivität der Spule oder die Kapazität des Kondensators im Schwingkreis verändert werden.
Wie aus der Thomsonschen Schwingkreisformel ersichtlich befinden sich die Größen $L$ und $C$ jeweils unter dem Bruchstrich. Hierdurch bewirkt eine Vergrößerung von $L$ oder $C$ eine Verringerung der Schwingkreisfrequenz, da der Nenner der Formel größer wird. Bei einer Verkleinerung von $L$ und $C$ gilt umgekehrt, dass die Resonanzfrequenz des Schwingkreises sich vergrößert.

<indepth>
Die Quadratwurzel hat auf diesen Zusammenhang keinen Einfluss, da die Wurzel aus einer größeren Zahl ebenfalls eine größere Zahl ist. Der Zusammenhang hierbei ist jedoch nicht linear.
</indepth>

Die Induktivität einer Spule kann durch Vergrößern der Windungszahl, durch Zusammenschieben oder Einführen eines Ferritkerns vergrößert werden.
Umgekehrt kann die Induktivität einer Spule verringert werden durch Verringerung der Windungszahl, durch Auseinanderziehen oder durch Entfernen eines Ferritkerns oder durch Einführen eines Kupferkerns. Die Kapazität von Kondensatoren kann durch Austausch oder die Verwendung von Trimm- oder Drehkondensatoren beeinflusst werden.

Mit diesem Wissen können wir nun die folgenden Fragen beantworten.

[question:AD213] 
[question:AD214] 
[question:AD215] 
[question:AD216] 
[question:AD217] 

Eine Kombination aus Parallel- und Serienschwingkreisen kann bei geeigneter Anordnung als Bandpassfilter verwendet werden. Im Resonanzfall verhalten sich die parallelen Schwingkreise wie hochohmige Widerstände und der Serienschwingkreis wie ein niederohmiger Widerstand.

[question:AD205]

Die Bandbreite von Filtern und Bandpässen wird häufig in Bezug auf einen bestimmten Dämpfungswert angegeben. Dabei beschreibt die Dämpfung, wie stark ein Signal gegenüber dem maximalen Durchlass abgeschwächt wird.

Üblicherweise wird die *Bandbreite* eines Filters über den sogenannten $\qty{-3}{\dB}$-Punkt definiert.

Am $\qty{-3}{\dB}$-Punkt gilt:

- Nur noch die halbe Leistung passiert das Filter
- Die Signalspannung beträgt noch etwa das $0{,}7$-fache des Maximalwertes

Die Bandbreite ergibt sich aus der Differenz zwischen oberer und unterer Grenzfrequenz bei $\qty{-3}{\dB}$:

$ B = f_\mathrm{o} - f_\mathrm{u} $

[question:AD220]

Dabei sind:

- $f_\mathrm{o}$: obere Grenzfrequenz
- $f_\mathrm{u}$: untere Grenzfrequenz

Die $\qty{-3}{\dB}$-Bandbreite wird verwendet, um die Eignung eines Filters für bestimmte Betriebsarten zu beschreiben:

- Schmalbandiges Filter mit etwa $\qty{500}{\hertz}$ Bandbreite: geeignet für CW (Telegrafie)
- Breitbandigeres Filter mit etwa $\qty{2,7}{\kilo\hertz}$ Bandbreite: geeignet für SSB-Sprachübertragung

[question:AD221] 
[question:AD222]

Bei der folgenden Frage muss nicht der $\qty{-3}{\dB}$-Punkt, sondern die Bandbreite am $\qty{-60}{\dB}$-Punkt abgelesen werden.

[question:AD219]

Die Güte eines Schwingkreises (im Englischen Q-Faktor) wird durch das Verhältnis der Blindwiderstände von Kapazität und Induktivität im Resonanzfall zum ohmschen Verlustwiderstand bestimmt. Wenn ein Schwingkreis keinerlei ohmschen Verlustwiderstände enthalten würde, so wäre dessen Q-Faktor unendlich. Reale Bauteile sind jedoch immer verlustbehaftet. Induktivitäten haben immer einen ohmschen Verlustwiderstand, Kapazitäten haben dielektrische Verluste, die sich ebenfalls als ohmscher Widerstand auswirken. Je größer die ohmschen Widerstände in einem Schwingkreis sind, desto geringer wird dessen Q-Faktor. Für Filter mit hoher Güte und steilen Flanken werden häufig Quarzfilter eingesetzt.

Für die Berechnung des Q-Faktors verwenden wir die entsprechenden Formeln aus der Formelsammlung je nachdem ob es sich um einen Parallel- oder Serienschwingkreis handelt:

Für den Serienschwingkreis gilt im Resonanzfall ($X_\text{L} = X_\text{C}$):

$Q = \frac{f_0}{B} = \frac{X_\text{L}}{R_\text{S}}$

Für den Parallelschwingkreis gilt im Resonanzfall ($X_\text{L} = X_\text{C}$):

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD225]


---

Entsprechend dem obigen Rechenbeispiel können wir jetzt auch den Gütefaktor des Parallelschwingkreises errechnen. Die Resonanzfrequenz wird wie im vorigen Beispiel berechnet. Es ist jedoch zu beachten, dass für die Berechnung von $Q$ die Formel für den Parallelschwingkreis zu verwenden ist:

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD226]

Die Bandbreite von Parallel- und Serienschwingkreisen lässt sich nun ebenfalls einfach aus der Resonanzfrequenz des Schwingkreises und dessen Gütefaktor wie folgt berechnen (Formel hierzu in der Formelsammlung):

$Q = \frac{f_0}{B}$

Durch Umstellen der Formel ergibt sich die Bandbreite $B$:

$B = \frac{f_0}{Q}$

Die vorgenannte Formel gilt sowohl für den Serien- als auch den Parallelschwingkreis!

[question:AD224]

Entsprechend kann nun auch mit dem zuvor beschriebenen Wissen die folgende Frage schrittweise berechnet werden.
[question:AD223]

---

Zur Übertragung von Signalen zwischen Schaltungsstufen sowie in Filtern in Sendern und Empfängern werden häufig gekoppelte Schwingkreise verwendet. Hierbei werden zwei Schwingkreise induktiv oder kapazitiv aneinander gekoppelt. Die Abbildung [ref:a_gekoppelte_schwingkreise] zeigt eine induktive Kopplung. Diese Kopplung kann je nach Anwendung 

- *lose* (d),
- *unterkritisch* (c),
- *kritisch* (b) oder 
- *überkritisch* (a)

erfolgen. Der Grad der Kopplung bestimmt die gegenseitige Beeinflussung und damit die Bandbreite und Durchlasskurve der gesamten Anordnung.

<margin>
[picture:184:a_gekoppelte_schwingkreise:Kopplung von Schwingkreisen]
</margin>

Bei loser und unterkritischer Kopplung gibt es kaum eine gegenseitige Beeinflussung; Dafür ist die Durchlassdämpfung der Anordnung relativ hoch und die Bandbreite relativ gering.

Bei kritischer Kopplung beeinflussen sich beide Schwingkreise gerade so, dass eine im Durchlassbereich flache Durchlasskurve mit geringer Dämpfung entsteht und diese im gewünschten Durchlassbereich völlig eben ist (Plateau). Die Bandbreite der Anordnung ist hierbei größer als bei loser und unterkritischer Kopplung. Hieran ist eine kritische Kopplung auch gut zu erkennen.

Bei überkritischer Kopplung ist die gegenseitige Beeinflussung der beiden Schwingkreise sehr stark, was zu einer starken Änderung beider Resonanzfrequenzen und damit zu einer großen Bandbreite führt. Hierdurch wird die Durchlasskurve im Durchlassbereich stark verzerrt und es bilden sich links und rechts der Mittenfrequenz zwei Resonanzpunkte. Die Durchlasskurve bekommt eine "Delle". Hieran ist die überkritische Kopplung gut zu erkennen.

[question:AD227] 
[question:AD228] 
[question:AD229] 