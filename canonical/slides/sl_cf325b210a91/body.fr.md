## Transformation d’impédance dans la ligne d’alimentation

* Une impédance caractéristique différente de la résistance de charge entraîne, en plus des ondes stationnaires, une transformation d’impédance
* La source de signal « voit » des résistances différentes aux extrémités du câble
* Les lignes de $\lambda/4$ transforment les petites résistances en grandes et les grandes en petites
* Les lignes de $\lambda/2$ ne provoquent aucune transformation d’impédance

---
[question:AG412]

---
[question:AG416]
---

### Alimentation des dipôles demi-onde et onde entière

<left>
[picture:312:a_impedanztransformation_speiseleitung:Dipôle demi-onde avec transformation d’impédance via la ligne d’alimentation]
</left>
<right>
* Dipôle demi-onde : alimentation par courant (faible impédance)
* Dipôle onde entière : alimentation par tension (impédance élevée)
</right>

---
[question:AG413]

---
[question:AG414]

---
[question:AG415]
---

### Calcul de l’impédance caractéristique
* Pour une transformation d’impédance ciblée, on a : $Z = \sqrt{Z_\mathrm{E} \cdot Z_\mathrm{A}}$
* L’impédance caractéristique est la moyenne géométrique entre l’impédance de la ligne et la résistance de charge

---
[question:AG417]
---
#### Méthode de résolution
* donné : $Z_A = \qty{60}{\ohm}$
* donné : $Z_E = \qty{240}{\ohm}$
* recherché : $Z$

<fragment>
$\begin{split}Z &= \sqrt{Z_E \cdot Z_A}\\ &= \sqrt{\qty{240}{\ohm} \cdot \qty{60}{\ohm}}\\ &= \qty{120}{\ohm}\end{split}$ 
</fragment>
---
[question:AG418]
---
#### Méthode de résolution
* donné : $Z_A = \qty{240}{\ohm}$
* donné : $Z_E = \qty{600}{\ohm}$
* recherché : $Z$

<fragment>
$\begin{split}Z &= \sqrt{Z_E \cdot Z_A}\\ &= \sqrt{\qty{600}{\ohm} \cdot \qty{240}{\ohm}}\\ &= \qty{380}{\ohm}\end{split}$ 
</fragment>
---

### Adaptation d’impédance avec des filtres en π

<left>
[picture:425:a_impedanztransformation_pi_filter:Filtre en π pour la transformation d’impédance]
</left>
<right>
* Des bobines et des condensateurs sont utilisés pour l’adaptation d’impédance
* Les filtres en π agissent comme des passe-bas et transforment l’impédance
* Ils peuvent être utilisés comme accordeurs d’antenne
</right>

<note>
Le nom « filtre en π » provient de l’agencement des composants, qui rappelle la lettre grecque $\pi$ et n’a rien à voir avec le nombre Pi.
</note>

---
[question:AG406]
