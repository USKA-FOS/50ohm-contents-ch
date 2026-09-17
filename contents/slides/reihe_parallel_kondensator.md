## Reihenschaltung

* Da die Spannung entscheidend für das Entstehen des elektrischen Feldes ist (und diese sich bei der Reihenschaltung aufteilt), ist die Berechnung der Kapazität genau umgekehrt wie bei Widerständen.
* Anwendungsfall: Bei hohen Spannungen werden mehrere Kondensatoren in Reihe geschaltet, um die Gefahr eines Durchschlags zu verhindern. Dabei ist hilfreich, dass sich die Gesamtspannung an den Kondensatoren aufteilt.

---

* Bei einer Reihenschaltung von Kondensatoren ist die Gesamtkapazität kleiner als der Wert des kleinsten Kondensators

[picture:823:e_reihenschaltung_kondensatoren:Reihenschaltung von 3 Kondensatoren]

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

---

* Vereinfachung für zwei Kondensatoren:

$C_{\mathrm{ges}} = \dfrac{C_{1} \cdot C_{2}}{C_{1} + C_{2}}$

---

* Vereinfachung für gleiche Kondensatoren:

$C_{\mathrm{ges}} = \dfrac{C}{n}$

$n$ steht für die Anzahl der Kondensatoren

---

[question:ED119]

---

[question:ED120]

---

## Parallelschaltung

* Hier ist es genau umgekehrt wie bei Widerständen, weil an allen Kondensatoren die gleiche Spannung anliegt, welche ja entscheidend für die Entstehung des elektrischen Feldes ist.
* Anwendungsfall: Kondensatoren werden parallel geschaltet, um aus der Normreihe auf den Wert zu kommen, den man benötigt.

<note>
* Die parallel geschalteten Kondensatoren wirken wie ein großer Kondensator
</note>

---

* Bei einer Parallelschaltung addieren sich die Kapazitäten

[picture:822:e_parallelschaltung_kondensatoren:Parallelschaltung von 3 Kondensatoren]

$C_{\mathrm{ges}} = C_{1} + C_{2} + C_{3}$

---

[question:ED117]

---

[question:ED118]

---

## Gemischte Schaltungen

--- style="font-size: 0.7em;"

### Variante 1: Zwei Parallel und dazu einer in Reihe

<left>
* Hier berechnet man zuerst die Parallelschaltung von $C_{2}$ und $C_{3}$

$C_{\mathrm{ges,p}} = C_{2} + C_{3}$

* Danach berechnet man die Reihenschaltung von $C_{1}$ und $C_{\mathrm{ges,p}}$

$C_{\mathrm{ges}} = \frac{C_{1} \cdot C_{\mathrm{ges,p}}}{C_{1} + C_{Gp}}$
</left>
<right>
[picture:820:e_gemischt_variante_1:Gemischte Schaltung - Variante 1]
</right>

---

[question:ED123]

---

[question:ED124]

---

[question:ED122]

--- style="font-size: 0.7em;"

### Variante 2: Zwei in Reihe und dazu einer Parallel

<left>
* Hier berechnet man zuerst die Reihenschaltung von $C_{1}$ und $C_{2}$

$C_{\mathrm{ges,r}} = \frac{C_{1} \cdot C_{2}}{C_{1} + C_{2}}$

* Danach berechnet man die Parallelschaltung von $C_{3}$ und $C_{\mathrm{ges,r}}$

$C_{\mathrm{ges}} = \frac{C_{3} \cdot C_{\mathrm{ges,r}}}{C_{3} + C_{\mathrm{ges,r}}}$
</left>
<right>
[picture:457:e_gemischt_variante_2:Gemischte Schaltung - Variante 2]
</right>

---

[question:ED121]

