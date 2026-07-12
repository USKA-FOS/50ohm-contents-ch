Les condensateurs sont utilisés dans de nombreuses applications en circuit en série, en circuit en parallèle ou même en technique de circuit mixte. Le circuit en parallèle est plus simple à comprendre, c'est pourquoi nous l'examinons en premier.

En connectant les condensateurs en parallèle, plus de plaques se font face et la surface des plaques augmente proportionnellement. En conséquence, la capacité dans le circuit global augmente également.

<margin>
[picture:822:e_3C-parallel: Circuit parallèle de 3 condensateurs]
</margin>

---

Dans un circuit parallèle de condensateurs de même taille, la capacité double, tandis que la tension de service reste la même. Bien sûr, on peut calculer la capacité totale. La formule se trouve dans le recueil de formules :

$C_{\mathrm{ges}} = C_{1} + C_{2} + C_{3} + \dots$

<tip>
La capacité totale dans un circuit en parallèle est toujours supérieure à la plus petite capacité individuelle.
</tip>

Dans la tâche suivante, une difficulté supplémentaire est à trouver, car les préfixes des valeurs de capacité sont différents. Il faut d'abord convertir toutes les valeurs en un préfixe commun. Les nombres ne doivent pas être trop grands et pas trop petits, c'est pourquoi il est recommandé de choisir le préfixe nano ($\unit{\nano}$). 

$\begin{split} \qty{0,1}{\micro\farad} &= \qty{100}{\nano\farad} \\ \qty{50000}{\pico\farad} &= \qty{50}{\nano\farad}\end{split}$

Il suffit maintenant d'additionner toutes les valeurs en $\unit{\nano\farad}$.

[question:ED117]

<margin>
[photo:262:a_Netzteil BEKO PA $7 \times \qty{10000}{\micro\farad}$ parallel: Circuit parallèle de $7 \times \qty{10000}{\micro\farad}$ dans une alimentation de l'étage final]
</margin>

La tâche suivante peut être utilisée comme test de compréhension.

[question:ED118]


---

Dans un circuit en série de condensateurs, comme le montre la figure [ref:e_3C-parallel], la tension de service augmente, mais la capacité diminue. Bien sûr, on peut à nouveau calculer la capacité totale. Celle-ci est très similaire au circuit en parallèle des résistances :

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

<margin>
[picture:823:e_3C-parallel:Circuit en série de 3 condensateurs] 
</margin>

<tip>
La capacité totale dans un circuit en série est toujours inférieure à la plus petite capacité individuelle.
</tip>

<tip>
Lors de la résolution des tâches, il est recommandé de procéder comme suit :
  
1. Dessinez le circuit
2. Écrivez les valeurs de capacité pour les composants.
3. Convertissez en préfixes identiques.
4. Simplifiez le circuit en regroupant les groupes de circuits de même type
5. Calculez étape par étape la capacité totale
</tip>

Si tous les condensateurs ont des valeurs de capacité identiques, alors on peut calculer facilement la capacité totale en divisant une capacité individuelle par 3. Dans la tâche suivante, on calcule $\qty{0,33}{\micro\farad} / 3 = \qty{0,11}{\micro\farad}$.

[question:ED119]

Dans le circuit en série de condensateurs de la tâche suivante, on trouve $\unit{\micro\farad}$ et $\unit{\nano\farad}$ comme préfixe. Il est très judicieux de convertir d'abord $\qty{200000}{\nano\farad}$ en $\qty{200}{\micro\farad}$. Dans un circuit en série, on peut maintenant appliquer la formule du recueil de formules.


$C_{\mathrm{ges}} =\frac{1}{\frac{1}{\qty{100}{\micro\farad}} + \frac{1}{\qty{50}{\micro\farad}} + \frac{1}{\qty{100}{\micro\farad}}}$

[question:ED120]

---
  
Dans la question suivante, 3 condensateurs sont combinés en circuit en série et en parallèle. 

[question:ED121]

Quelle partie du circuit peut être simplifiée en premier ? Exactement : le circuit en série.
Ce sous-groupe a une capacité totale de la moitié de $\qty{10}{\nano\farad}$, donc $\qty{5}{\nano\farad}$. Il est maintenant plus facile de continuer le calcul, car dans un circuit en parallèle, les valeurs de capacité sont additionnées. Félicitations pour le résultat de $\qty{10}{\nano\farad}$.

Les tâches suivantes sont similaires et faciles à résoudre.

[question:ED122]
[question:ED123]
[question:ED124]

%<margin>
%
%Aides à la solution:
%
%*ED 118:* Circuit en série de $\qty{22}{\nano\farad}$, $\qty{0,033}{\micro\farad} = \qty{33}{\nano\farad}$ et $\qty{15000}{\pico\farad} = \qty{15}{\nano\farad}$.
%$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{\qty{22}{\nano\farad}} + \frac{1}{\qty{33}{\nano\farad}} + \frac{1}{\qty{15}{\nano\farad}}$
%Il n'est pas nécessaire de calculer, car il n'y a qu'un résultat qui est inférieur à $\qty{15}{\nano\farard}$.
%*ED 120:* $\qty{50}{\micro\farad}$ 
%*ED 122:* $C_2 = \qty{1}{\micro\farad}$ et $C_3 = \qty{1}{\micro\farad}$ en circuit parallèle donne ensemble $\qty{2}{\micro\farad}$. Avec $C_1 = \qty{2}{\micro\farad}$ en série %résulte la moitié, donc $\qty{1}{\micro\farad}$.
% 
%*ED 123:* $C_2 = \qty{4}{\nano\farad}$ et $C_3 = \qty{4}{\nano\farad}$ en circuit parallèle donne ensemble $\qty{8}{\nano\farad}$. Avec $C_1 = \qty{8}{\nano\farad}$ en série %résulte la moitié, donc $\qty{4}{\nano\farad}$.
%  
%*ED 124:* $C_2 = \qty{100}{\nano\farad}$ et $C_3 = \qty{100000}{\pico\farad} = \qty{100}{\nano\farad}$ en circuit parallèle donne ensemble $\qty{200}{\nano\farad}$. Avec %$C_1 = \qty{200}{\nano\farad}$ en série résulte la moitié, donc $\qty{100}{\nano\farad}$.
%</margin>
