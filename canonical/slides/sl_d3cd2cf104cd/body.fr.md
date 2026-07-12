<left>
[picture:489:a_frequenzvervielfacher_schaltung:Exemple d'un circuit d'un multiplicateur de fréquence avec un amplificateur de classe C sans tension de polarisation de base]
</left>
<right>
* Le signal d'entrée est fourni à un étage de distorsion non linéaire
* Par exemple, un amplificateur de classe C, fonctionnant sans tension de polarisation de base
* Le signal est fortement distordu
* Un filtre est utilisé pour sélectionner l'harmonique souhaitée
</right>
<note>
Les circuits amplificateurs seront abordés plus tard dans le chapitre.
</note>
---
<left>
[picture:489:a_frequenzvervielfacher_schaltung:Exemple d'un circuit d'un multiplicateur de fréquence avec un amplificateur de classe C sans tension de polarisation de base]
</left>
<right>
* Seuls les multiples entiers sont possibles
* En règle générale, la 2ème ou la 3ème harmonique est utilisée
* Multiplication de fréquence plus élevée avec des étages connectés en série
</right>
<note>
</note>
---
[question:AF312]
---
[question:AF311]
---
### Blindage

* Des fréquences intermédiaires sont générées
* Celles-ci entraînent souvent des perturbations
* Tous les étages doivent être bien blindés

---
[question:AF313]
---
### Plusieurs étages de multiplication

* Les fréquences individuelles entre les étages de multiplication peuvent entraîner des perturbations
* Suivre les fréquences individuelles à travers les étages et calculer les fréquences individuelles
* L'ordre des étages est important pour déterminer les fréquences de perturbation

---
[question:AF314]
---
#### Méthode de solution
* donné : $f_\text{émetteur} = \qty{432}{\mega\hertz}$
* donné : $f_\text{base} = \qty{12}{\mega\hertz}$
* donné : $f_\text{QRM} = \qty{144}{\mega\hertz}$
* recherché : combinaison de multiplication

<fragment>
$n = \frac{f_\text{émetteur}}{f_\text{QRM}} = \frac{\qty{432}{\mega\hertz}}{\qty{144}{\mega\hertz}} = 3$
</fragment>
<fragment>
Seule la combinaison de $\textrm{Fréquence de base}\,\cdot 2\cdot 2\cdot 3\cdot 3$ est possible, car elle effectue une triple multiplication de la fréquence en dernier.
</fragment>
---
Vérification:
$\begin{split}f_\text{émetteur} &= f_\text{base}\cdot 2\cdot 2\cdot 3\cdot 3\\ &= \qty{12}{\mega\hertz}\cdot 2\cdot 2\cdot 3\cdot 3\\ &= \qty{24}{\mega\hertz}\cdot 2\cdot 3\cdot 3\\ &= \qty{48}{\mega\hertz}\cdot 3\cdot 3\\ &= \bold{\qty{144}{\mega\hertz}}\cdot 3\\ &= \qty{432}{\mega\hertz}\end{split}$
