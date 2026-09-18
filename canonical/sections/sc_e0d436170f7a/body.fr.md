Les condensateurs sont utilisés dans de nombreuses applications en montage en série, en montage en parallèle ou encore en technique de circuit mixte. Le montage en parallèle est plus simple à comprendre, c'est pourquoi nous l'examinons en premier.

En montage en parallèle, les plaques se font face en plus grand nombre, et la surface des plaques augmente proportionnellement. La capacité du circuit total augmente donc également.

<margin>
[picture:822:e_3C-parallel: Montage en parallèle de 3 condensateurs]
</margin>

---

Dans un montage en parallèle de condensateurs de même taille, la capacité double, tandis que la tenue en tension reste identique. Bien sûr, il est possible de calculer la capacité totale. La formule se trouve dans le recueil de formules :

$C_{\mathrm{ges}} = C_{1} + C_{2} + C_{3} + \dots$

<tip>
La capacité totale en montage en parallèle est toujours supérieure à la plus petite capacité individuelle.
</tip>

Dans l'exercice suivant, une difficulté supplémentaire se présente, car les préfixes des valeurs de capacité diffèrent. Il faut d'abord convertir toutes les valeurs vers un préfixe commun. Pour éviter des nombres trop grands ou trop petits, il est recommandé de choisir le préfixe nano ($\unit{\nano}$).

$\begin{split} \qty{0,1}{\micro\farad} &= \qty{100}{\nano\farad} \\ \qty{50000}{\pico\farad} &= \qty{50}{\nano\farad}\end{split}$

Il ne reste plus qu'à additionner toutes les valeurs en $\unit{\nano\farad}$.

[question:ED117]

<margin>
[photo:262:a_Netzteil BEKO PA $7 \times \qty{10000}{\micro\farad}$ parallel: Montage en parallèle de $7 \times \qty{10000}{\micro\farad}$ dans une alimentation de puissance]
</margin>

Un exercice de compréhension peut être utilisé pour le test suivant.

[question:ED118]

---

Dans un montage en série de condensateurs, comme illustré dans la figure [ref:e_3C-parallel], la tenue en tension augmente, mais la capacité diminue. Bien sûr, il est possible de calculer à nouveau la capacité totale. Celle-ci est très similaire au montage en parallèle de résistances :

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

<margin>
[picture:823:e_3C-parallel: Montage en série de 3 condensateurs]
</margin>

<tip>
La capacité totale en montage en série est toujours inférieure à la plus petite capacité individuelle.
</tip>

<tip>
Pour résoudre les exercices, la démarche suivante est recommandée :
  
1. Esquisser le circuit
2. Noter les valeurs de capacité des composants.
3. Convertir vers des préfixes identiques.
4. Simplifier le circuit en regroupant les éléments de même type
5. Calculer progressivement la capacité totale
</tip>

Si tous les condensateurs ont la même valeur de capacité, il est facile de calculer la capacité totale en divisant une capacité individuelle par 3. Dans l'exercice suivant, on calcule $\qty{0,33}{\micro\farad} / 3 = \qty{0,11}{\micro\farad}$.

[question:ED119]

Dans l'exercice sur le montage en série de condensateurs suivant, on trouve les préfixes $\unit{\micro\farad}$ et $\unit{\nano\farad}$. Il est judicieux de convertir d'abord $\qty{200000}{\nano\farad}$ en $\qty{200}{\micro\farad}$. Dans un montage en série, on peut maintenant appliquer la formule du recueil de formules.

$C_{\mathrm{ges}} =\frac{1}{\frac{1}{\qty{100}{\micro\farad}} + \frac{1}{\qty{200}{\micro\farad}} + \frac{1}{\qty{200}{\micro\farad}}}$

[question:ED120]

---

Dans la question suivante, 3 condensateurs sont combinés en montage en série et en parallèle.

[question:ED121]

Quel élément du circuit peut être simplifié en premier ? Exact : le montage en série.
Ce sous-groupe a une capacité totale égale à la moitié de $\qty{10}{\nano\farad}$, soit $\qty{5}{\nano\farad}$. Il est maintenant plus facile de poursuivre le calcul, car en montage en parallèle, les valeurs de capacité s'additionnent. Félicitations pour le résultat de $\qty{10}{\nano\farad}$.

Les autres exercices sont similaires et faciles à résoudre.

[question:ED122]
[question:ED123]
[question:ED124]

%<margin>
%
%Aides à la solution :
%
%*ED 118 :* Montage en série de $\qty{22}{\nano\farad}$, $\qty{0,033}{\micro\farad} = \qty{33}{\nano\farad}$ et $\qty{15000}{\pico\farad} = \qty{15}{\nano\farad}$.
%$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{\qty{22}{\nano\farad}} + \frac{1}{\qty{33}{\nano\farad}} + \frac{1}{\qty{15}{\nano\farad}}$
%En réalité, il n'est pas nécessaire de calculer, car il n'existe qu'un seul résultat inférieur à $\qty{15}{\nano\farad}$.
%*ED 120 :* $\qty{50}{\micro\farad}$
%*ED 122 :* $C_2 = \qty{1}{\micro\farad}$ et $C_3 = \qty{1}{\micro\farad}$ en montage en parallèle donnent ensemble $\qty{2}{\micro\farad}$. Avec $C_1 = \qty{2}{\micro\farad}$ en série, on obtient la moitié, soit $\qty{1}{\micro\farad}$.
%*ED 123 :* $C_2 = \qty{4}{\nano\farad}$ et $C_3 = \qty{4}{\nano\farad}$ en montage en parallèle donnent ensemble $\qty{8}{\nano\farad}$. Avec $C_1 = \qty{8}{\nano\farad}$ en série, on obtient la moitié, soit $\qty{4}{\nano\farad}$.
%*ED 124 :* $C_2 = \qty{100}{\nano\farad}$ et $C_3 = \qty{100000}{\pico\farad} = \qty{100}{\nano\farad}$ en montage en parallèle donnent ensemble $\qty{200}{\nano\farad}$. Avec $C_1 = \qty{200}{\nano\farad}$ en série, on obtient la moitié, soit $\qty{100}{\nano\farad}$.
%</margin>
