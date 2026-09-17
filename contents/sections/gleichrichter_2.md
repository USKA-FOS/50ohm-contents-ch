Wie bereits im Kapitel "Gleichrichter I" der Klasse E gezeigt, lässt eine einzelne Diode nur die positive Halbwelle durch. Damit daraus eine nutzbare Gleichspannung entsteht, wird zusätzlich mindestens ein Kondensator benötigt, der die pulsierende Ausgangsspannung glättet (siehe Schaltung [ref:a_einweggleichrichtung_c]).

<margin>
[picture:795:a_einweggleichrichtung_c:Einweggleichrichtung mit Kondensator]
</margin>

---

Bei der positiven Halbwelle leitet die Diode $D$ und lässt Strom fließen. In dieser Zeit lädt sich der Kondensator $C_L$ auf den Spitzenwert der Wechselspannung auf. Zum Zeitpunkt der negativen Halbwelle sperrt die Diode $D$ den Strom und der Kondensator $C_L$ entlädt sich über den Lastwiderstand $R_L$.

Somit stellt sich am Lastwiderstand $R_L$ eine leicht pulsierende Gleichspannung $U_L$ ein (vgl. Abb.[ref:a_Restwelligkeit]). Um so größer die Kapazität des Kondensator ist, desto gleichmäßiger wird die Gleichspannung am Lastwiderstand geglättet.

<margin>
[picture:75:a_Restwelligkeit:Welligkeit der Ausgangsgleichspannung $U_L$]
</margin>

Bei der Bemessung von Diode und Kondensator müssen wir jedoch wissen, dass die Trafo-Spannungen als Effektivspannungen $U_{\mathrm{eff}}$ angegeben werden. Somit müssen wir die Spitzenspannung $\hat{U}$ vorher bestimmen.

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}}$

Wenn an einem Transformator z. B. die Spannung $U_a = \qty{15}{\volt}$ angegeben ist, rechnen wir:

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}} = \sqrt{2} \cdot \qty{15}{\volt} = \qty{21,21}{\volt}$

Somit wird sich ohne Last eine Leerlaufspitzenspannung von ca. $\qty{21}{\volt}$ einstellen.

[question:AD302]

Bei nachfolgender Frage müssen wir das Übersetzungsverhältnis vom Trafo anwenden, um unsere Ausgangsspannung zu ermitteln. Wir setzten also für die effektive Eingangsspannung $U_{\mathrm{eff}}$ ein zwanzigstel der Trafoeingangsspannung von $\qty{230}{\volt}$ ein. Von der Spitzenspannung können wir dann die Hälfte der Spannung nochmal addieren um den Sicherheitsaufschlag zu berücksichtigen.

[question:AD303]

Für die Lösung der folgenden Aufgabe müssen wir erkennen, dass der Spitzenwert der negativen Halbwelle und die Kondensatorspannung sich addieren und die Diode in Sperrrichtung belasten. Dies ist die höchste Spannung, die an der Diode in Sperrrichtung auftreten kann.

Wir rechnen: $U_{\mathrm{sperr}} = 2 \cdot \hat{u}$
Zu berücksichtigen sind dann noch das Übersetzungsverhältnis $5 : 1$  des Netztransformators und der Sicherheitsaufschlag von $\qty{20}{\percent}$.

[question:AD304]

%TODO Simulation einbauen: https://tinyurl.com/22m65xlw