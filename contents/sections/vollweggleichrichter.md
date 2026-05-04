An Stelle eines Brückengleichrichters, kann auch mit zwei Dioden und einem Transformator mit Mittelanzapfung eine Vollweggleichrichtung erreicht werden.

<margin>
[picture:946:Vollwegleichrichter D1 D2:Vollweggleichrichtung mit zwei Dioden]
</margin>

---

Zum Verständnis der Funktion muss die positive und negative Halbwelle getrennt betrachtet werden. Liegt an der oberen Wicklung eine positive Halbwelle gegenüber der Mittelanzapfung an der Anode der Diode $D_1$ an, dann leitet nur diese Diode und leitet die Halbwelle auf den Ausgang, der mit + bezeichnet ist, weiter. An der Diode $D_2$ liegt zu diesem Zeitpunkt eine negative Halbwelle an der Anode gegenüber der Mittelanzapfung an. Diese Diode bleibt bei dieser Halbwelle gesperrt.

Bei der nächsten Halbwelle ist die Diode  $D_1$ gesperrt und die Diode  $D_2$ leitet, da nun dort eine positive Halbwelle gegenüber der Trafomittelanzapfung anliegt. Am Gleichspannungsausgang erscheinen nun zwei Halbwellen, aber immer in positiver Richtung gegenüber der Mittelanzapfung. Die Mittelanzapfung bildet den Minuspol der Ausgangsgleichspannung.

<margin>
[include:applet_gleichrichter_1]
</margin>

<tip>
Die beiden Kathoden der Dioden liegen zusammen am Pluspol der Ausgangsspannung.
</tip>

[question:AD307]

Wenn zwei Anoden gemeinsam an einem Ausgangspol angeschlossen sind, dann wird dort die pulsierende Gleichspannung negativ gegenüber der Mittelanzapfung des Trafos sein. Beide Halbwellen befinden sich unterhalb der Nulllinie.

[question:AD308]

Würde man die pulsierende Gleichspannung über einen Spannungsteiler in einen Verstärker mit Lautsprecher einspeisen, dann könnte man einen $\qty{100}{\hertz}$ Brummton hören.
Gegenüber der $\qty{50}{\hertz}$ Sinusschwingung mit einer Periodendauer von $\qty{20}{\milli\second}$, enthält die pulsierende Gleichspannung prinzipiell 2 Schwingungen in der Zeit von $\qty{20}{\milli\second}$. Daraus lassen sich die $\qty{100}{\hertz}$ berechnen.
%todo $\qty{50}{\hertz}$ und $\qty{100}{\hertz}$ durch anklicken hörbar

[question:AD310]