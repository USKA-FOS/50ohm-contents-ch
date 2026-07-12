Nous, les humains, avons l'habitude d'utiliser les dix chiffres de $\num{0}$ à $\num{9}$. On parle d'un système décimal ou système décimal.

Pour les ordinateurs, il est plus simple de travailler avec seulement $\num{2}$ chiffres : le $\num{0}$ et le $\num{1}$. Cela correspond à deux états : Par exemple, éteint et allumé, "Transistor bloqué" et "Transistor conducteur" ou encore $\qty{0}{\volt}$ et $\qty{5}{\volt}$. Il en résulte un système de numération binaire ou un système dual.

[question:EA201]

Le comptage se fait dans tous les systèmes de numération de la même manière (voir tableau [ref:binaer_zahlensysteme]) : On commence à $\num{0}$ et on compte les chiffres. Lorsque le stock de chiffres est épuisé, on recommence à partir du début et on écrit un $\num{1}$ devant chaque nombre. C'est pourquoi, dans le système décimal, après le $\num{9}$ vient le $\num{10}$. Le chiffre le plus à droite a la valeur qu'il représente lui-même. On l'appelle la valeur de position $\num{1}$. 

---

Dans le système décimal, le deuxième chiffre de droite vaut dix fois plus que lui-même, a donc la valeur de position $\num{10}$. Chaque position plus à gauche vaut dix fois plus que celle qui est à droite. Par exemple, le nombre décimal $\num{5573}$ du tableau [ref:binaer_stellenwert_dezimal] signifie donc en réalité $5 \cdot 1000 + 5 \cdot 100 + 7 \cdot 10 + 3 \cdot 1$.

<margin>
|c: |c: |c: |c: |
|$\num{1000}$ | $\num{100}$ | $\num{10}$ | $\num{1}$ |
| $\num{5}$ | $\num{5}$ | $\num{7}$ | $\num{3}$ |
[table:binaer_stellenwert_dezimal:Valeurs de position du nombre décimal à quatre chiffres $\num{5573}$]

|r: Décimal | r: Dual |
| $\num{0}$ | $\num{0}$ |
| $\num{1}$ | $\num{1}$ |
| $\num{2}$ | $\num{10}$ |
| $\num{3}$ | $\num{11}$ |
| $\num{4}$ | $\num{100}$ |
| $\num{5}$ | $\num{101}$ |
| $\num{6}$ | $\num{110}$ |
| $\num{7}$ | $\num{111}$ |
| $\num{8}$ | $\num{1000}$ |
| $\num{9}$ | $\num{1001}$ |
| $\num{10}$ | $\num{1010}$ |
| $\num{11}$ | $\num{1011}$ |
| $\num{12}$ | $\num{1100}$ |
| $\num{13}$ | $\num{1101}$ |
| $\num{14}$ | $\num{1110}$ |
| $\num{15}$ | $\num{1111}$ |
[table:binaer_zahlensysteme:Nombres dans le système décimal et dans le système binaire]
</margin>

Dans le système binaire, il n'y a que deux chiffres, à savoir $\num{0}$ et $\num{1}$. Comme on peut le voir dans le tableau [ref:binar_stellenwert_dual], la première position à partir de la droite a la valeur de position $\num{1}$, la deuxième $\num{2}$, la troisième $\num{4}$, la quatrième $\num{8}$ et ainsi de suite. Les valeurs de position se doublent, au lieu de se décupler, parce qu'il n'y a que deux chiffres et non dix. Une position dans le système binaire s'appelle aussi bit ($\unit{\bit}$).

|c: |c: |c: |c: |c: |c: |c: |c: |
| $\num{128}$ | $\num{64}$ | $\num{32}$ | $\num{16}$ | $\num{8}$ | $\num{4}$ | $\num{2}$ | $\num{1}$ |
| $\num{1}$ | $\num{0}$ | $\num{0}$ | $\num{0}$ | $\num{1}$ | $\num{1}$ | $\num{1}$ | $\num{0}$ |
[table:binar_stellenwert_dual:Valeurs de position du nombre binaire à huit chiffres $\num{10001110}$]

Si l'on connaît les valeurs de position, la conversion des nombres binaires en nombres décimaux est simple. Prenons un exemple du tableau [ref:binar_stellenwert_dual]. Le nombre binaire $\num{10001110}$ doit être converti en un nombre décimal.

1. On écrit au-dessus de chaque chiffre du nombre binaire sa valeur de position.
2. On additionne toutes les valeurs de position sous lesquelles se trouve un $\num{1}$ : $128+8+4+2=142$

[question:EA206]
[question:EA207]
[question:EA208]

Sur le papier, on peut écrire des nombres binaires avec autant de bits que nécessaire. En technologie numérique, c'est différent. Le matériel ou le logiciel impose un certain nombre de chiffres, que l'on appelle aussi largeur. Par exemple, les microcontrôleurs ou les ordinateurs ont souvent des largeurs de $\num{8}$, $\num{16}$, $\num{32}$ ou $\qty{64}{\text{bits}}$. Dans la représentation, les nombres binaires sont souvent complétés par des zéros devant jusqu'à ce que cette largeur soit atteinte. Cela ne change rien à la valeur du nombre.

[question:EA205]

Une largeur fixe limite la plage de valeurs. Avec un bit, deux valeurs sont possibles ($\num{0}$ et $\num{1}$), avec deux bits déjà quatre ($\num{00}$, $\num{01}$, $\num{10}$ et $\num{11}$) et avec chaque bit supplémentaire respectivement le double. Avec $n$ bits, $2^n$ nombres différents peuvent être représentés.

[question:EA204]
[question:EA202]
[question:EA203]
