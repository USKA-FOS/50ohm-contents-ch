Dans la classe E, nous avons déjà appris comment les condensateurs se comportent dans des montages en série et en parallèle. Dans le chapitre précédent, nous avons traité le montage en série de bobines. Dans ce chapitre, nous examinons maintenant le montage en parallèle de bobines et de condensateurs. Tout d’abord, nous révisons les relations fondamentales dans les montages en parallèle et en série de capacités.

Dans les circuits résonants parallèles, les bobines et les condensateurs sont combinés. Une bobine réelle possède également une certaine capacité propre. Celle-ci résulte par exemple des enroulements de la bobine et des couplages de champs électriques entre les spires qui en découlent.

Pour un calcul aussi précis que possible de la fréquence de résonance, ces capacités « invisibles » doivent être prises en compte. Dans l’exercice suivant, les capacités des condensateurs et la capacité propre de la bobine peuvent être additionnées directement, car elles sont en parallèle les unes par rapport aux autres.

Il est particulièrement important de faire attention aux différentes unités. Avant le calcul, toutes les valeurs doivent donc être converties dans la même unité afin que les capacités puissent être correctement additionnées.


[question:AD103]

Dans l’exercice suivant, trois condensateurs sont montés en série. Dans la classe E, nous avons appris que, pour des condensateurs en montage en série, les inverses des capacités s’additionnent :


$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$


Là aussi, les capacités doivent être converties dans la même unité avant le calcul afin que les inverses puissent être correctement additionnés.


[question:AD101]

---

Dans les circuits à courant alternatif, en plus des résistances ohmiques connues, il existe aussi des réactances, comme nous l’avons déjà vu pour les condensateurs et les bobines. La résistance ohmique normale est appelée résistance active $R$. Les réactances sont décrites par $X$. Ces deux types de résistance influencent simultanément le flux de courant dans le circuit.

Comme les résistances active et réactive agissent différemment, elles ne peuvent pas simplement être additionnées. Elles sont plutôt composées géométriquement. On peut s’imaginer cela comme un triangle rectangle, comme dans l’illustration [ref:a_dreieck] :


---

- La résistance active $R$ forme le côté horizontal.
- La réactance $X$ forme le côté vertical.
- La résistance totale qui en résulte est appelée impédance $|Z|$.

<margin>
[picture:1067:a_dreieck:Triangle rectangle illustrant le calcul de l’impédance $|Z|$ à partir de la résistance active $R$ et de la réactance $X$]
</margin>

L’impédance se calcule à l’aide du théorème de Pythagore (cf. recueil de formules) :


$ |Z| = \sqrt{R^2 + X^2} $


La lettre $Z$ est utilisée pour ce qu’on appelle l’impédance. Pour les calculs de ce chapitre, il suffit de considérer la valeur absolue $|Z|$ comme la résistance totale en courant alternatif du circuit.


<indepth>
Pour les personnes intéressées par les mathématiques : l’impédance $Z$ est une grandeur complexe qui contient la résistance active $R$ comme partie réelle et la réactance $X$ comme partie imaginaire :


$Z = R + jX$


La valeur absolue $|Z|$ correspond alors à la longueur du vecteur dans le plan complexe, qui résulte de la combinaison de $R$ et $X$.
</indepth>

Pour la question suivante, avant de pouvoir appliquer le théorème de Pythagore, il faut calculer la réactance $X_C$ du condensateur à $\qty{1}{\mega\hertz}$. Pour cela, nous utilisons la formule de la réactance d’un condensateur.


[question:AD104]


La question suivante porte sur le calcul de l’impédance d’un montage en série d’une résistance et d’une bobine. Nous calculons d’abord $X_L$, puis nous appliquons à nouveau le théorème de Pythagore. Ici aussi, il faut faire attention aux puissances de dix pour que le calcul soit correctement effectué.


[question:AD105]