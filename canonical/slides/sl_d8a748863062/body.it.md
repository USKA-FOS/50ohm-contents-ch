## Collegamento in serie

In un collegamento in serie i valori delle resistenze si sommano

[picture:812:e_reihenschaltung_von_r:Collegamento in serie di 3 resistenze]

$R_{\mathrm{ges}} = R_{1} + R_{2} + R_{3}$
Esempio: $R_{\mathrm{ges}} = \qty{100}{\ohm} + \qty{200}{\ohm} + \qty{300}{\ohm}$

---
## Collegamento in parallelo

In un collegamento in parallelo di resistenze, la resistenza totale è inferiore al valore della resistenza più piccola

[picture:811:e_parallelschaltung_von_r:Collegamento in parallelo di 3 resistenze]

$\frac{1}{R_{\mathrm{ges}}} = \frac{1}{R_{1}} + \frac{1}{R_{2}} + \frac{1}{R_{3}}$

---

Semplificazione per due resistenze:
$R_{\mathrm{ges}} = \dfrac{R_{1} \cdot R_{2}}{R_{1} + R_{2}}$

---

Semplificazione per resistenze uguali:
$R_{\mathrm{ges}} = \dfrac{R}{n}$
$n$ indica il numero delle resistenze

---
[question:ED104]

---
[question:ED105]

---
[question:ED106]

---
## Circuiti misti

---

### Variante 1: Due in parallelo e una in serie

[picture:813:e_gemischte_schaltung_1:Circuito misto - Variante 1]

<fragment>
In questo caso si calcola prima il collegamento in parallelo di $R_2$ e $R_3$ e poi si aggiunge $R_1$.
</fragment>

<fragment>
$R_{\mathrm{ges}} = \dfrac{R_{2} \cdot R_{3}}{R_{2} + R_{3}} + R_{1}$
</fragment>

---
### Variante 2: Due in serie e una in parallelo

[picture:814:e_gemischte_schaltung_2:Circuito misto - Variante 2]

<fragment>
In questo caso si sommano prima $R_1$ e $R_2$ e poi si calcola il collegamento in parallelo con $R_3$.
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
### Capacità di carico delle resistenze nei collegamenti in serie e in parallelo

* In un collegamento in serie le tensioni si suddividono.
* In un collegamento in parallelo le correnti si suddividono.
* Pertanto, nel calcolo con $P = U \cdot I$, un valore rimane costante e l’altro diminuisce di conseguenza.
* $\rightarrow$ la capacità di carico totale è in entrambi i casi maggiore della capacità di carico individuale.

---
[question:ED107]
