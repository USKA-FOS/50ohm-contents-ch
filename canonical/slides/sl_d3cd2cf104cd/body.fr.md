<left>
[picture:489:a_frequenzvervielfacher_schaltung:Exemple de circuit d'un multiplicateur de fréquence avec amplificateur de classe C sans polarisation de base]
</left>
<right>
* Le signal d'entrée est appliqué à un étage de distorsion non linéaire
* Par exemple, un amplificateur de classe C, grâce à un fonctionnement sans polarisation de base
* Le signal est fortement distordu
* Un filtre permet de sélectionner l'harmonique souhaitée
</right>
<note>
Les circuits amplificateurs seront abordés plus tard dans le chapitre.
</note>
---
<left>
[picture:489:a_frequenzvervielfacher_schaltung:Exemple de circuit d'un multiplicateur de fréquence avec amplificateur de classe C sans polarisation de base]
</left>
<right>
* Seuls les multiples entiers sont possibles
* En règle générale, on utilise la 2ᵉ ou la 3ᵉ harmonique
* Une multiplication de fréquence plus élevée s'effectue avec des étages montés en série
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
* Elles provoquent souvent des perturbations
* Tous les étages doivent être bien blindés

---
[question:AF313]
---
### Plusieurs étages de multiplicateur

* Les différentes fréquences entre les étages de multiplicateur peuvent causer des perturbations
* Suivre le chemin à travers les différents étages et calculer les fréquences individuelles
* L'ordre des étages est important pour déterminer les fréquences de perturbation

---
[question:AF314]
---
#### Méthode de résolution
* donné : $f_\text{Émetteur} = \qty{432}{\mega\hertz}$
* donné : $f_\text{Base} = \qty{12}{\mega\hertz}$
* donné : $f_\text{QRM} = \qty{144}{\mega\hertz}$
* recherché : Combinaison de multiplication

<fragment>
$n = \frac{f_\text{Émetteur}}{f_\text{QRM}} = \frac{\qty{432}{\mega\hertz}}{\qty{144}{\mega\hertz}} = 3$
</fragment>
<fragment>
Seule la combinaison $\textrm{Fréquence de base}\cdot 2\cdot 2\cdot 3\cdot 3$ est possible, car elle effectue en dernier une triplication de la fréquence.
</fragment>
---
Vérification :
$\begin{split}f_\text{Émetteur} &= f_\text{Base}\cdot 2\cdot 2\cdot 3\cdot 3\\ &= \qty{12}{\mega\hertz}\cdot 2\cdot 2\cdot 3\cdot 3\\ &= \qty{24}{\mega\hertz}\cdot 2\cdot 3\cdot 3\\ &= \qty{48}{\mega\hertz}\cdot 3\cdot 3\\ &= \bold{\qty{144}{\mega\hertz}}\cdot 3\\ &= \qty{432}{\mega\hertz}\end{split}$