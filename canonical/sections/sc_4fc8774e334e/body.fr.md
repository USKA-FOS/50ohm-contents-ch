Nous sommes souvent confrontés au problème qu'une valeur de résistance souhaitée n'est pas incluse dans la soi-disant "série de résistances normalisées". Il pourrait aussi être qu'une résistance doit convertir une grande puissance dissipée, ce qui n'est pas possible dans les résistances individuelles disponibles dans le commerce -- pour ne citer que deux exemples. Nous allons maintenant examiner comment nous pouvons obtenir d'autres valeurs de résistance en connectant des résistances en série ou en parallèle.

À partir de la loi d'Ohm, nous pouvons déduire les règles des circuits en série et en parallèle de résistances:

$U=R \cdot I$

<margin>
[picture:819:e_spannungsteiler:Diviseur de tension]
</margin>

La figure [ref:e_spannungsteiler] montre deux résistances $R_1$ et $R_2$, qui sont connectées l'une derrière l'autre. Elles sont traversées par le même courant *I*. Les tensions aux bornes des résistances sont alors

$U_1 = R_1 \cdot I$ et  $U_2 = R_2 \cdot I$. 
La tension totale $U_g$ est simplement la somme de ces deux tensions:

$U_g = U_1 + U_2 = R_{\mathrm{ges}} \cdot {I} = R_1 \cdot I + R_2 \cdot I$

Maintenant, nous pouvons calculer la résistance qui est visible entre les bornes extérieures:
$R_{\mathrm{ges}} = \frac{U_g}{I} = R_1 + R_2$, car le courant $I$ se simplifie des deux côtés de l'équation.

Tout cela fonctionne également avec plus de deux résistances, comme indiqué dans le recueil de formules:

$R_{\mathrm{ges}} = R_1 + R_2 + R_3 + R_4 + \dots$

---

Mais comment se comporte-t-il si nous connectons deux résistances $R_1$ et $R_2$ en parallèle comme le montre la figure [ref:e_parallelschaltung] ? 

Maintenant, la même tension $U$ est appliquée aux deux résistances, ce qui permet aux courants

$I_1 = \frac{U}{R_1}$ et $I_2 = \frac{U}{R_2}$

de circuler dans les résistances. 

<margin>
[picture:945:e_parallelschaltung:Dans ce circuit, toutes les tensions et tous les courants sont visibles.]
</margin>

Le courant circulant dans le circuit extérieur est la somme de ces deux courants:

$I = I_1 + I_2 = \frac{U}{R_1} + \frac{U}{R_2}$

Nous cherchons à nouveau une résistance totale $R_{\mathrm{ges}}$, pour laquelle doit s'appliquer: $I=\frac{U}{R_{\mathrm{ges}}}$ et par conséquent:

$\dfrac{1}{R_{\mathrm{ges}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$

---

L'inverse de la résistance totale est donc la somme des inverses des résistances individuelles. Une conséquence est que lors d'un circuit en parallèle d'une série de résistances égales, on divise simplement la valeur de la résistance individuelle par le nombre de résistances.

Nous pouvons également effectuer le calcul pour un nombre quelconque de résistances parallèles (voir recueil de formules):

$\dfrac{1}{R_{\mathrm{ges}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dfrac{1}{R_3} + \dfrac{1}{R_4} + \dots$

Nous pouvons également écrire l'expression pour deux résistances parallèles selon les règles de l'algèbre:

$R_{\mathrm{ges}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$

<tip>
Dans le cas d'un circuit en série, la valeur de la résistance totale est toujours supérieure à la plus grande résistance individuelle. Dans le cas d'un circuit en parallèle, la résistance totale est toujours inférieure à la plus petite résistance individuelle.
</tip>

---

[question:ED104]
[question:ED105]
[question:ED106]

<tip>
Il est important de veiller à ce que les résistances utilisées dans le calcul aient toujours les mêmes unités. Nous recommandons d'utiliser toujours, si possible, l'unité de base ($\unit{\ohm}$). Par exemple, si nous connectons une résistance de $\qty{1}{\kilo\ohm}$ et une résistance de $\qty{10}{\ohm}$ en série, nous calculons $\qty{1000}{\ohm} + \qty{10}{\ohm} = \qty{1010}{\ohm}$.
</tip>

---

Certaines des tâches contiennent des réseaux de résistances dans lesquels à la fois un circuit en série et un circuit en parallèle sont présents. Nous procédons de manière à transformer d'abord, par exemple, le circuit en parallèle en une résistance équivalente, que nous combinons ensuite avec la troisième résistance connectée en série. Ou inversement, selon ce qui s'offre à nous à l'aide du schéma de circuit.

<tip>
[picture:305:e_tipp_aufgabe:Circuit d'exemple]

Une méthode de résolution importante est la "méthode de l'observation attentive" ... il y a par exemple un circuit qui a une résistance $R_1$ en série avec deux résistances $R_2$ et $R_3$ connectées en parallèle. Les valeurs sont $R_1 = \qty{1}{\kilo\ohm}$, $R_2 = \qty{2000}{\ohm}$ et $R_3 = \qty{2}{\kilo\ohm}$. Or, $\qty{2}{\kilo\ohm} = \qty{2000}{\ohm}$. Le circuit en parallèle de $R_2$ et $R_3$ donne une résistance qui est moitié moins grande: $\qty{1000}{\ohm} = \qty{1}{\kilo\ohm}$. Nous le connectons en série avec $R_1$ et obtenons le résultat: $R_{\mathrm{ges}} = \qty{2}{\kilo\ohm}$.
</tip>

[question:ED111]
[question:ED110]
[question:ED112]
[question:ED113]
[question:ED108]
[question:ED109]

Dans le cas des considérations de puissance, il est préférable de partir de l'expression connue pour la puissance:

$P = U \cdot I$

Dans le cas d'un circuit en série de, par exemple, trois résistances égales, le même courant traverse toutes les résistances, mais seulement un tiers de la tension extérieure est appliqué à chaque résistance individuelle. Dans le cas d'un circuit en parallèle, la même tension est appliquée à toutes les résistances, mais le courant se divise en trois chemins. Dans les deux cas, le circuit supporte donc trois fois la puissance de la résistance individuelle.

[question:ED107]