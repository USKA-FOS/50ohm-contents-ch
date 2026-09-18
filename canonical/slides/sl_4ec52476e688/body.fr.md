## En série

* Puisque la tension est déterminante pour la formation du champ électrique (et qu'elle se répartit dans un circuit en série), le calcul de la capacité est exactement l'inverse de celui des résistances.
* Cas d'application : Pour des tensions élevées, plusieurs condensateurs sont montés en série afin de réduire le risque de claquage. Il est alors utile que la tension totale se répartisse sur les condensateurs.

---

* Dans un circuit en série de condensateurs, la capacité totale est inférieure à la valeur du plus petit condensateur

[picture:823:e_reihenschaltung_kondensatoren:Montage en série de 3 condensateurs]

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

---

* Simplification pour deux condensateurs :

$C_{\mathrm{ges}} = \dfrac{C_{1} \cdot C_{2}}{C_{1} + C_{2}}$

---

* Simplification pour des condensateurs identiques :

$C_{\mathrm{ges}} = \dfrac{C}{n}$

$n$ représente le nombre de condensateurs

---

[question:ED119]

---

[question:ED120]

---

## En parallèle

* Ici, c'est exactement l'inverse des résistances, car tous les condensateurs sont soumis à la même tension, qui est déterminante pour la formation du champ électrique.
* Cas d'application : Les condensateurs sont montés en parallèle pour obtenir une valeur de capacité correspondant à une série normalisée.

<note>
* Les condensateurs montés en parallèle agissent comme un seul condensateur de plus grande capacité
</note>

---

* Dans un circuit en parallèle, les capacités s'additionnent

[picture:822:e_parallelschaltung_kondensatoren:Montage en parallèle de 3 condensateurs]

$C_{\mathrm{ges}} = C_{1} + C_{2} + C_{3}$

---

[question:ED117]

---

[question:ED118]

---

## Circuits mixtes

--- style="font-size: 0.7em;"

### Variante 1 : Deux en parallèle et un en série

<left>
* On calcule d'abord le circuit en parallèle de $C_{2}$ et $C_{3}$

$C_{\mathrm{ges,p}} = C_{2} + C_{3}$

* Ensuite, on calcule le circuit en série de $C_{1}$ et $C_{\mathrm{ges,p}}$

$C_{\mathrm{ges}} = \frac{C_{1} \cdot C_{\mathrm{ges,p}}}{C_{1} + C_{\mathrm{ges,p}}}$
</left>
<right>
[picture:820:e_gemischt_variante_1:Montage mixte - Variante 1]
</right>

---

[question:ED123]

---

[question:ED124]

---

[question:ED122]

--- style="font-size: 0.7em;"

### Variante 2 : Deux en série et un en parallèle

<left>
* On calcule d'abord le circuit en série de $C_{1}$ et $C_{2}$

$C_{\mathrm{ges,r}} = \frac{C_{1} \cdot C_{2}}{C_{1} + C_{2}}$

* Ensuite, on calcule le circuit en parallèle de $C_{3}$ et $C_{\mathrm{ges,r}}$

$C_{\mathrm{ges}} = \frac{C_{3} \cdot C_{\mathrm{ges,r}}}{C_{3} + C_{\mathrm{ges,r}}}$
</left>
<right>
[picture:457:e_gemischt_variante_2:Montage mixte - Variante 2]
</right>

---

[question:ED121]
