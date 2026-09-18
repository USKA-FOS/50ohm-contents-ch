Nous sommes souvent confrontés au problème suivant : une valeur de résistance souhaitée n'est pas disponible dans la série normalisée des résistances. Il se peut aussi qu'une résistance doive dissiper une puissance dissipée importante, ce qui n'est pas possible avec des résistances unitaires standard — pour ne citer que deux exemples. Nous allons maintenant examiner comment obtenir d'autres valeurs de résistance en associant des résistances en série ou en parallèle.

À partir de la loi d'Ohm, nous pouvons déduire les règles des montages en série et en parallèle de résistances :

$U=R \cdot I$

<margin>
[picture:819:e_spannungsteiler:Diviseur de tension]
</margin>

La figure [ref:e_spannungsteiler] montre deux résistances $R_1$ et $R_2$ montées l'une derrière l'autre. Elles sont parcourues par le même courant *I*. Aux bornes des résistances, les tensions suivantes s'établissent :

$U_1 = R_1 \cdot I$ et $U_2 = R_2 \cdot I$. 
La tension totale $U_g$ est simplement la somme de ces deux tensions :

$U_g = U_1 + U_2 = R_{\mathrm{ges}} \cdot {I} = R_1 \cdot I + R_2 \cdot I$

Nous pouvons maintenant calculer la résistance vue entre les bornes extérieures :
$R_{\mathrm{ges}} = \frac{U_g}{I} = R_1 + R_2$, car le courant $I$ s'annule des deux côtés de l'équation.

Ce principe s'applique également à plus de deux résistances, comme illustré dans le recueil de formules :

$R_{\mathrm{ges}} = R_1 + R_2 + R_3 + R_4 + \dots$

---

Mais que se passe-t-il si nous montons deux résistances $R_1$ et $R_2$ en parallèle, comme montré dans la figure [ref:e_parallelschaltung] ?

Dans ce cas, la même tension $U$ est appliquée aux deux résistances, ce qui fait circuler les courants suivants dans les résistances :

$I_1 = \frac{U}{R_1}$ et $I_2 = \frac{U}{R_2}$

<margin>
[picture:945:e_parallelschaltung:Dans ce circuit, toutes les tensions et tous les courants sont visibles.]
</margin>

Le courant circulant dans le circuit extérieur est la somme de ces deux courants :

$I = I_1 + I_2 = \frac{U}{R_1} + \frac{U}{R_2}$

Nous cherchons à nouveau une résistance totale $R_{\mathrm{ges}}$, pour laquelle nous devons avoir : $I=\frac{U}{R_{\mathrm{ges}}}$ et donc :

$\dfrac{1}{R_{\mathrm{ges}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$

---

L'inverse de la résistance totale est donc la somme des inverses des résistances individuelles. Une conséquence est que, dans un montage en parallèle de résistances identiques, on peut simplement diviser la valeur de la résistance individuelle par le nombre de résistances.

Nous pouvons également effectuer le calcul pour un nombre quelconque de résistances en parallèle (voir recueil de formules) :

$\dfrac{1}{R_{\mathrm{ges}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dfrac{1}{R_3} + \dfrac{1}{R_4} + \dots$

L'expression pour deux résistances en parallèle peut également s'écrire, selon les règles du calcul des fractions :

$R_{\mathrm{ges}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$

<tip>
Dans un montage en série, la valeur de la résistance totale est toujours supérieure à la plus grande résistance individuelle. Dans un montage en parallèle, la résistance totale est toujours inférieure à la plus petite résistance individuelle.
</tip>

---

[question:ED104]
[question:ED105]
[question:ED106]

<tip>
Veillez à ce que les résistances utilisées dans les calculs aient toujours les mêmes unités. Nous recommandons d'utiliser systématiquement l'unité de base ($\unit{\ohm}$). Par exemple, si nous montons en série une résistance de $\qty{1}{\kilo\ohm}$ et une résistance de $\qty{10}{\ohm}$, nous calculons $\qty{1000}{\ohm} + \qty{10}{\ohm} = \qty{1010}{\ohm}$.
</tip>

---

Certains exercices comportent des réseaux de résistances dans lesquels des montages en série et en parallèle coexistent. Dans ce cas, nous commençons par convertir, par exemple, le montage en parallèle en une résistance équivalente, que nous combinons ensuite avec la troisième résistance montée en série. Ou inversement, selon ce qui est le plus pratique d'après le schéma du circuit.

<tip>
[picture:305:e_tipp_aufgabe:Exemple de circuit]

Une méthode de résolution importante est la « méthode de l'œil vif » ... par exemple, un circuit comprenant une résistance $R_1$ en série avec deux résistances $R_2$ et $R_3$ montées en parallèle. Les valeurs sont $R_1 = \qty{1}{\kilo\ohm}$, $R_2 = \qty{2000}{\ohm}$ et $R_3 = \qty{2}{\kilo\ohm}$. Or, $\qty{2}{\kilo\ohm} = \qty{2000}{\ohm}$. Le montage en parallèle de $R_2$ et $R_3$ donne une résistance deux fois plus petite : $\qty{1000}{\ohm} = \qty{1}{\kilo\ohm}$. Nous l'associons en série avec $R_1$ et obtenons le résultat : $R_{\mathrm{ges}} = \qty{2}{\kilo\ohm}$.
</tip>

[question:ED111]
[question:ED110]
[question:ED112]
[question:ED113]
[question:ED108]
[question:ED109]

Pour les considérations de puissance, il est préférable de partir de l'expression connue de la puissance :

$P = U \cdot I$

Dans un montage en série de trois résistances identiques, le même courant circule dans toutes les résistances, mais seule un tiers de la tension extérieure est appliquée à chaque résistance individuelle. Dans un montage en parallèle, la même tension est appliquée à toutes les résistances, mais le courant se divise en trois branches. Dans les deux cas, le circuit supporte donc une puissance triple de celle de la résistance individuelle.

[question:ED107]
