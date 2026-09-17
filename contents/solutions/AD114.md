Da der Lastwiderstand $R_L$ parallel zu $R_2$ liegt, müssen zunächst beide Widerstände zu einem Ersatzwiderstand zusammengefasst werden.

Die Parallelschaltung ergibt:

$ R_\mathrm{2L} = \frac{R_2 \cdot R_L}{R_2 + R_L} $

Werte einsetzen:

$ R_\mathrm{2L} = \frac{\qty{2,2}{\kilo\ohm} \cdot \qty{8,2}{\kilo\ohm}}
{\qty{2,2}{\kilo\ohm} + \qty{8,2}{\kilo\ohm}} $

$ R_\mathrm{2L} \approx \qty{1,74}{\kilo\ohm} $

Nun besteht die Schaltung nur noch aus einem einfachen Spannungsteiler aus $R_1$ und $R_\mathrm{2L}$.

Die Ausgangsspannung berechnet sich mit:

$ U_2 = U_B \cdot \frac{R_\mathrm{2L}}{R_1 + R_\mathrm{2L}} $

Werte einsetzen:

$ U_2 = \qty{12}{\volt} \cdot \frac{\qty{1,74}{\kilo\ohm}}{\qty{10}{\kilo\ohm} + \qty{1,74}{\kilo\ohm}} = \approx \qty{1,8}{\volt} $