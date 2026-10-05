Dans la section [sec:reihe_parallel_kondensator], nous avons déjà appris comment se comportent les condensateurs en série et en parallèle. La section précédente [sec:reihenschaltung_spule] a également traité du montage en série des bobines. Dans cette section, nous examinons maintenant le montage en parallèle des bobines et des condensateurs. Nous commençons cependant par réviser une fois de plus les relations fondamentales dans les montages en parallèle et en série des capacités.

Dans les circuits d'accord parallèles, les bobines et les condensateurs sont combinés. Une bobine réelle possède également une certaine capacité propre. Celle-ci apparaît par exemple à cause des spires de la bobine et des couplages de champ électrique qui en résultent entre les tours.

Pour un calcul aussi précis que possible de la fréquence de résonance, ces capacités "invisibles" doivent être prises en compte. Dans l'exercice suivant, les capacités des condensateurs et la capacité propre de la bobine peuvent être additionnées directement, car elles sont placées en parallèle.

Il est particulièrement important de faire attention aux différentes unités. Avant le calcul, toutes les valeurs doivent donc être converties dans la même unité, afin que les capacités puissent être additionnées correctement.

[question:AD103]

Dans l'exercice suivant, trois condensateurs sont montés en série. Dans la section [sec:reihe_parallel_kondensator], nous avons appris que pour des condensateurs en série, les inverses des capacités s'additionnent :

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

Ici aussi, les capacités doivent être converties dans la même unité avant le calcul, afin que les inverses puissent être additionnés correctement.

[question:AD101]

---

Dans les circuits à courant alternatif, outre les résistances ohmiques connues, des réactances apparaissent, comme nous les avons déjà rencontrées avec les condensateurs et les bobines. La résistance ohmique normale est appelée résistance active $R$. Les réactances sont désignées par $X$. Les deux types de résistance influencent simultanément le flux de courant dans le circuit.

Comme la résistance active et la réactance agissent différemment, elles ne peuvent pas simplement être additionnées. Au lieu de cela, elles sont combinées géométriquement. On peut se représenter cela comme un triangle rectangle, comme dans la figure [ref:a_dreieck] :

---

- La résistance active $R$ forme le côté horizontal.
- La réactance $X$ forme le côté vertical.
- La résistance totale qui en résulte est appelée impédance $|Z|$.

<margin>
[picture:1067:a_dreieck:Triangle rectangle pour illustrer le calcul de l'impédance $|Z|$ à partir de la résistance active $R$ et de la réactance $X$]
</margin>

L'impédance peut être calculée à l'aide du théorème de Pythagore (cf. recueil de formules) :

$ |Z| = \sqrt{R^2 + X^2} $

La lettre $Z$ est utilisée pour l'impédance. Pour les calculs de ce chapitre, il suffit cependant de considérer la valeur absolue $|Z|$ comme la résistance totale en courant alternatif du circuit.

<indepth>
Pour les personnes intéressées par les mathématiques : L'impédance $Z$ est une grandeur complexe qui contient la résistance active $R$ comme partie réelle et la réactance $X$ comme partie imaginaire :

$Z = R + jX$

La valeur absolue $|Z|$ correspond alors à la longueur du vecteur dans le plan complexe, qui résulte de la combinaison de $R$ et $X$.
</indepth>

Pour la question suivante, avant de pouvoir appliquer le théorème de Pythagore, la réactance $X_C$ du condensateur à $\qty{1}{\mega\hertz}$ doit être calculée. Pour cela, nous utilisons la formule de la réactance d'un condensateur.

[question:AD104]

La question suivante traite du calcul de l'impédance d'un montage en série d'une résistance et d'une bobine. Nous calculons d'abord $X_L$, puis nous appliquons à nouveau le théorème de Pythagore. Ici aussi, les puissances de dix doivent être prises en compte pour que le calcul puisse être effectué correctement.

[question:AD105]
