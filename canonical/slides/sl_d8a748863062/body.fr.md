## Circuit en série

Dans un circuit en série, les valeurs des résistances s'additionnent

[picture:812:e_reihenschaltung_von_r:Circuit en série de 3 résistances]

$R_{\mathrm{ges}} = R_{1} + R_{2} + R_{3}$
Exemple : $R_{\mathrm{ges}} = \qty{100}{\ohm} + \qty{200}{\ohm} + \qty{300}{\ohm}$

---

## Circuit en parallèle

Dans un circuit en parallèle de résistances, la résistance totale est inférieure à la valeur de la plus petite résistance

[picture:811:e_parallelschaltung_von_r:Circuit en parallèle de 3 résistances]

$\frac{1}{R_{\mathrm{ges}}} = \frac{1}{R_{1}} + \frac{1}{R_{2}} + \frac{1}{R_{3}}$



---

Simplification pour deux résistances :
$R_{\mathrm{ges}} = \dfrac{R_{1} \cdot R_{2}}{R_{1} + R_{2}}$

---

Simplification pour des résistances égales :
$R_{\mathrm{ges}} = \dfrac{R}{n}$
$n$ représente le nombre de résistances

---

[question:ED104]

---

[question:ED105]

---

[question:ED106]

---

## Circuits mixtes

---

### Variante 1 : Deux en parallèle et un en série

[picture:813:e_gemischte_schaltung_1:Circuit mixte - Variante 1]

<fragment>
Ici, on calcule d'abord le circuit en parallèle de $R_2$ et $R_3$ et on ajoute ensuite $R_1$.
</fragment>

<fragment>
$R_{\mathrm{ges}} = \dfrac{R_{2} \cdot R_{3}}{R_{2} + R_{3}} + R_{1}$
</fragment>

---

### Variante 2 : Deux en série et un en parallèle

[picture:814:e_gemischte_schaltung_2:Circuit mixte - Variante 2]

<fragment>
Ici, on additionne d'abord $R_1$ et $R_2$ pour calculer ensuite le circuit en parallèle avec $R_3$.
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

### Capacité de charge des résistances en circuits en série et en parallèle

* Dans un circuit en série, les tensions se répartissent.
* Dans un circuit en parallèle, les courants se répartissent.
* Ainsi, lors du calcul à l'aide de $P = U \cdot I$, une valeur est toujours constante et l'autre est en conséquence plus petite.
* $\rightarrow$ la capacité de charge totale est dans les deux cas supérieure à la capacité de charge individuelle.

---

[question:ED107]
