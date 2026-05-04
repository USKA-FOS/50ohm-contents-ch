## Reihenschaltung

Bei einer Reihenschaltung addieren sich die Widerstandswerte

[picture:812:e_reihenschaltung_von_r:Reihenschaltung von 3 Widerständen]

$R_{\mathrm{ges}} = R_{1} + R_{2} + R_{3}$
Beispiel: $R_{\mathrm{ges}} = \qty{100}{\ohm} + \qty{200}{\ohm} + \qty{300}{\ohm}$

--- style="font-size: 0.7em;"

## Parallelschaltung

Bei einer Parallelschaltung von Widerständen ist der Gesamtwiderstand kleiner als der Wert des kleinsten Widerstandes

[picture:811:e_parallelschaltung_von_r:Parallelschaltung von 3 Widerständen]

$\frac{1}{R_{\mathrm{ges}}} = \frac{1}{R_{1}} + \frac{1}{R_{2}} + \frac{1}{R_{3}}$



---

Vereinfachung für zwei Widerstände:
$R_{\mathrm{ges}} = \dfrac{R_{1} \cdot R_{2}}{R_{1} + R_{2}}$

---

Vereinfachung für gleiche Widerstände:
$R_{\mathrm{ges}} = \dfrac{R}{n}$
$n$ steht für die Anzahl der Widerstände

---

[question:ED104]

---

[question:ED105]

---

[question:ED106]

---

## Gemischte Schaltungen

--- style="font-size: 0.7em;"

### Variante 1: Zwei Parallel und dazu einer in Reihe

[picture:813:e_gemischte_schaltung_1:Gemischte Schaltung - Variante 1]

<fragment>
Hier berechnet man zuerst die Parallelschaltung von $R_2$ und $R_3$ und addiert dann $R_1$ hinzu.
</fragment>

<fragment>
$R_{\mathrm{ges}} = \dfrac{R_{2} \cdot R_{3}}{R_{2} + R_{3}} + R_{1}$
</fragment>

---

### Variante 2: Zwei in Reihe und dazu einer Parallel

[picture:814:e_gemischte_schaltung_2:Gemischte Schaltung - Variante 2]

<fragment>
Hier addiert man zuerst $R_1$ und $R_2$ um mit diesem Ergebnis die Parallelschaltung zu $R_3$ zu berechnen.
</fragment>

<fragment>
$R_{\mathrm{ges}} = \dfrac{(R_{1} + R_{2}) \cdot R_{3}} {(R_{1} + R_{2}) + R_{3}}$
</fragment>

---

[question:ED110]

---

[question:ED111]

---

[question:ED108]

---

[question:ED109]

---

[question:ED112]

---

[question:ED113]

---

### Belastbarkeit von Widerständen in Reihen- und Parallelschaltung

* Bei einer Reihenschaltung teilen sich die Spannungen auf.
* Bei einer Parallelschaltung teilen sich die Ströme auf.
* Somit ist bei der Berechnung mittels $P = U \cdot I$ immer ein Wert konstant und der andere entsprechend kleiner.
* $\rightarrow$ die Gesamtbelastbarkeit ist in beiden Fällen größer als die Einzelbelastbarkeit.

---

[question:ED107]
