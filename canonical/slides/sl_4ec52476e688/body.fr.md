## En série

* Comme la tension est décisive pour la formation du champ électrique (et celle-ci se divise dans le circuit en série), le calcul de la capacité est exactement l'inverse de celui des résistances.
* Cas d'application : En cas de tensions élevées, plusieurs condensateurs sont connectés en série pour éviter le risque d'un claquage. Il est utile que la tension totale aux bornes des condensateurs se divise.

---

* Dans un circuit en série de condensateurs, la capacité totale est inférieure à la valeur du plus petit condensateur

[picture:823:e_reihenschaltung_kondensatoren:Reihenschaltung von 3 Kondensatoren]

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

* Ici, c'est exactement l'inverse des résistances, car tous les condensateurs ont la même tension, qui est décisive pour la formation du champ électrique.
* Cas d'application : Les condensateurs sont connectés en parallèle pour obtenir la valeur nécessaire à partir de la série normale.

<note>
* Les condensateurs connectés en parallèle agissent comme un grand condensateur
</note>

---

* Dans un circuit en parallèle, les capacités s'additionnent

[picture:822:e_parallelschaltung_kondensatoren:Parallelschaltung von 3 Kondensatoren]

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
* Ici, on calcule d'abord le circuit en parallèle de $C_{2}$ et $C_{3}$

$C_{\mathrm{ges,p}} = C_{2} + C_{3}$

* Ensuite, on calcule le circuit en série de $C_{1}$ et $C_{\mathrm{ges,p}}$

$C_{\mathrm{ges}} = \frac{C_{1} \cdot C_{\mathrm{ges,p}}}{C_{1} + C_{\mathrm{ges,p}}}$
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

### Variante 2 : Deux en série et un en parallèle

<left>
* Ici, on calcule d'abord le circuit en série de $C_{1}$ et $C_{2}$

$C_{\mathrm{ges,r}} = \frac{C_{1} \cdot C_{2}}{C_{1} + C_{2}}$

* Ensuite, on calcule le circuit en parallèle de $C_{3}$ et $C_{\mathrm{ges,r}}$

$C_{\mathrm{ges}} = \frac{C_{3} \cdot C_{\mathrm{ges,r}}}{C_{3} + C_{\mathrm{ges,r}}}$
</left>
<right>
[picture:457:e_gemischt_variante_2:Gemischte Schaltung - Variante 2]
</right>

---

[question:ED121]

