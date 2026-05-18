Eine Reihenschaltung aus zwei Widerständen wird häufig als Spannungsteiler verwendet. In der Klasse E betrachten wir zunächst den *unbelasteten Spannungsteiler*, wie er auch in den folgenden Aufgaben vorkommt. Bei einem unbelasteten Spannungsteiler verhalten sich die Spannungen proportional zu den Widerständen. Das bedeutet beispielsweise, dass an einem hochohmigen Widerstand eine größere Spannung abfällt, während an einem niederohmigen Widerstand eine entsprechend kleinere Spannung messbar ist.

<margin>
[picture:819:E 63. Spannungsteiler:Spannungsteiler]
</margin>

<indepth>
Einen wichtigen Spannungsteiler findet man z.B. an der Basis eines Transistors in einer Verstärkerschaltung. 
Man spricht deshalb vom Basis-Spannungsteiler. Das Schauen wir uns im Kapitel Verstärker genauer an.
</indepth>

Dieser Zusammenhang kann in verschiedenen Formeln dargestellt werden, welche wir in der Formelsammlung finden.:

$\frac{U_{1}}{U_{2}} = \frac{R_{1}}{R_{2}}$

oder

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

% TODO implementiere Attention in CSS!
<danger>
Bei einem belasteten Spannungsteiler gelten diese Formeln nicht. Fragen dazu folgen in der Klasse A.
</danger>

Bei den folgenden Fragen wird der Begriff Spannungsteiler nicht direkt erwähnt, aber durch die Wortwahl : "Wie teilt sich die Spannung an zwei in Reihe geschalteten Widerständen auf ...." sollte man erkennen, dass es sich um einen Spannungsteiler handelt.

[question:ED101]

Es sind keine konkreten Widerstandswerte angegeben, deshalb ist das Ergebnis als allgemeine Formel darzustellen. 
Laut Fragestellung  ist $R_1$ 5-mal größer als $R_2$, also muss an ihm auch eine 5-mal größere Spannung gemessen werden können, bzw. $R_1 = 5 \cdot R_2$

Diesen Zusammenhang kann man als Formel angeben.

$\frac{U_{1}}{U_{2}} = \frac{5 \cdot R_2}{R_2}$

Die $R_2$ kürzen sich weg und es ergibt sich:

$\frac{U_{1}}{U_{2}} = \frac{5}{1}$

Nach etwas umformen erhalten wir das Ergebnis:

$U_{1} = U_{2} \cdot \frac{5}{1}$

$U_{1} = 5 \cdot U_{2}$

[question:ED102]

Bei dieser Frage besteht der umgekehrte Zusammenhang wie bei der Frage ED 101. Laut Fragestellung  ist $R_1$ 6-mal kleiner als $R_2$, also muss an ihm auch eine 6-mal kleinere Spannung gemessen werden können. 

Dieser Zusammenhang in einer Formel dargestellt lautet nun:

$\frac{U_{1}}{U_{2}} = \frac{1}{6}$
  
$U_{1} = U_{2} \cdot {\frac{1}{6}}$
  
$U_1 = \frac{U_2}{6}$

[question:ED103]

Bei dieser Frage sind konkrete Widerstandswerte angegeben, die zur Ermittlung des Spannungsteilerverhältnisses dienen. $R_1$ verhält sich zu $R_2$ wie $\qty{10}{\kilo\ohm}$ zu $\qty{20}{\kilo\ohm}$, also $1$ zu $2$. $U_2$ muss deshalb doppelt so groß sein wie $U_1$. Es ist aber die Gesamtspannung  $U_g$ angegeben. Diese liegt an einem Gesamtwiderstand von $\qty{30}{\kilo\ohm}$ und wird deshalb im Verhältnis $30$ zu $20$ (oder $3$ zu $2$) bezogen auf $R_2$ aufgeteilt. An $R_2$  muss deshalb die Spannung $2/3$ von $U_g$ gemessen werden können.

Selbstverständlich kann dieses Ergebnis auch mit der Formel aus der Formelsammlung berechnet werden:

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

und diese dann nach $U_2$ umgestellt:

$U_{2} = \frac{R_{2}}{R_{1} + R_{2}} \cdot U_g$
