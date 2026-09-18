## In serie

* Poiché la tensione è determinante per la formazione del campo elettrico (e questa si suddivide nel collegamento in serie), il calcolo della capacità è esattamente l'opposto rispetto a quello delle resistenze.
* Caso d'uso: per tensioni elevate, diversi condensatori vengono collegati in serie per evitare il rischio di perforazione. È utile il fatto che la tensione totale si suddivida tra i condensatori.

---

* In un collegamento in serie di condensatori, la capacità totale è inferiore al valore del condensatore più piccolo

[picture:823:e_reihenschaltung_kondensatoren:Collegamento in serie di 3 condensatori]

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$


---

* Semplificazione per due condensatori:

$C_{\mathrm{ges}} = \dfrac{C_{1} \cdot C_{2}}{C_{1} + C_{2}}$


---

* Semplificazione per condensatori identici:

$C_{\mathrm{ges}} = \dfrac{C}{n}$


$n$ indica il numero dei condensatori


---

[question:ED119]


---

[question:ED120]


---

## Collegamento in parallelo

* Qui è esattamente l'opposto rispetto alle resistenze, perché su tutti i condensatori è presente la stessa tensione, che è determinante per la formazione del campo elettrico.
* Caso d'uso: i condensatori vengono collegati in parallelo per ottenere dalla serie normativa il valore desiderato.

<note>
* I condensatori collegati in parallelo agiscono come un unico condensatore di capacità maggiore
</note>

---

* In un collegamento in parallelo le capacità si sommano

[picture:822:e_parallelschaltung_kondensatoren:Collegamento in parallelo di 3 condensatori]

$C_{\mathrm{ges}} = C_{1} + C_{2} + C_{3}$


---

[question:ED117]


---

[question:ED118]


---

## Circuiti misti

--- style="font-size: 0.7em;"

### Variante 1: Due in parallelo e uno in serie

<left>
* Qui si calcola prima il collegamento in parallelo di $C_{2}$ e $C_{3}$


$C_{\mathrm{ges,p}} = C_{2} + C_{3}$


* Successivamente si calcola il collegamento in serie di $C_{1}$ e $C_{\mathrm{ges,p}}$


$C_{\mathrm{ges}} = \frac{C_{1} \cdot C_{\mathrm{ges,p}}}{C_{1} + C_{\mathrm{ges,p}}}$
</left>
<right>
[picture:820:e_gemischt_variante_1:Circuito misto - Variante 1]
</right>


---

[question:ED123]


---

[question:ED124]


---

[question:ED122]


--- style="font-size: 0.7em;"

### Variante 2: Due in serie e uno in parallelo

<left>
* Qui si calcola prima il collegamento in serie di $C_{1}$ e $C_{2}$


$C_{\mathrm{ges,r}} = \frac{C_{1} \cdot C_{2}}{C_{1} + C_{2}}$


* Successivamente si calcola il collegamento in parallelo di $C_{3}$ e $C_{\mathrm{ges,r}}$


$C_{\mathrm{ges}} = \frac{C_{3} \cdot C_{\mathrm{ges,r}}}{C_{3} + C_{\mathrm{ges,r}}}$
</left>
<right>
[picture:457:e_gemischt_variante_2:Circuito misto - Variante 2]
</right>


---

[question:ED121]

