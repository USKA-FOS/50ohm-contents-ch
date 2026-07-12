## Transformation d'impédance dans le câble d'alimentation

* L'impédance de la ligne différente de la Résistance de charge entraîne, outre les ondes stationnaires, une transformation d'impédance
* La source de signal "voit" des résistances différentes aux extrémités du câble
* Les lignes $\lambda/4$ transforment les petites en grandes et les grandes en petites résistances actives
* Les lignes $\lambda/2$ n'effectuent aucune transformation d'impédance

---
[question:AG412]

---
[question:AG416]
---

### Alimentation des dipôles demi-onde et onde entière

<left>
[picture:312:a_impedanztransformation_speiseleitung:Dipôle demi-onde avec transformation d'impédance via le câble d'alimentation]
</left>
<right>
* Dipôle demi-onde : alimenté par le courant (faible impédance)
* Dipôle onde entière : alimenté par la tension (haute impédance)
</right>

---
[question:AG413]

---
[question:AG414]

---
[question:AG415]
---

### Calcul de l'impédance de la ligne
* Pour une transformation d'impédance ciblée, on a : $Z = \sqrt{Z_\mathrm{E} \cdot Z_\mathrm{A}}$
* L'impédance de la ligne résulte de la moyenne géométrique de la résistance d'alimentation et de charge

---
[question:AG417]
---
#### Solution
* donné : $Z_A = \qty{60}{\ohm}$
* donné : $Z_E = \qty{240}{\ohm}$
* recherché : $Z$

<fragment>
$\begin{split}Z &= \sqrt{Z_E \cdot Z_A}\\ &= \sqrt{\qty{240}{\ohm} \cdot \qty{60}{\ohm}}\\ &= \qty{120}{\ohm}\end{split}$ 
</fragment>
---
[question:AG418]
---
#### Solution
* donné : $Z_A = \qty{240}{\ohm}$
* donné : $Z_E = \qty{600}{\ohm}$
* recherché : $Z$

<fragment>
$\begin{split}Z &= \sqrt{Z_E \cdot Z_A}\\ &= \sqrt{\qty{600}{\ohm} \cdot \qty{240}{\ohm}}\\ &= \qty{380}{\ohm}\end{split}$ 
</fragment>
---

### Adaptation d'impédance avec des filtres Pi

<left>
[picture:425:a_impedanztransformation_pi_filter:Filtre Pi pour la transformation d'impédance]
</left>
<right>
* Les bobines et les condensateurs sont utilisés pour l'adaptation d'impédance
* Les filtres Pi agissent comme des passe-bas et transforment l'impédance
* Ils peuvent être utilisés comme accordeur d’antenne
</right>

<note>
Le nom "filtre Pi" provient de la disposition des composants, qui rappellent la lettre grecque $\pi$ et n'ont rien à voir avec le Nombre Pi.
</note>

---
[question:AG406]
