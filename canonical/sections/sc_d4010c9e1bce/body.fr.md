Dans la classe E, nous avons déjà appris comment les condensateurs se comportent en série et en parallèle. Dans le chapitre précédent, le circuit série des bobines a également été traité. Dans ce chapitre, nous examinons maintenant le circuit parallèle des bobines et des condensateurs. Cependant, nous répétons d'abord les relations fondamentales des circuits série et parallèle des capacités.

Dans les circuits oscillants parallèles, les bobines et les condensateurs sont combinés. Une bobine réelle possède également une certaine capacité propre. Celle-ci est créée, par exemple, par les enroulements de la bobine et les couplages de champ électrique résultants entre les spires.

Pour un calcul aussi précis que possible de la fréquence de résonance, ces capacités "invisibles" doivent être prises en compte. Dans l'exercice suivant, les capacités des condensateurs et la capacité propre de la bobine peuvent être ajoutées directement, car elles sont en parallèle les unes des autres.

Il est particulièrement important de faire attention aux différentes unités. Avant le calcul, toutes les valeurs doivent donc être converties dans la même unité afin que les capacités puissent être additionnées correctement.

[question:AD103]

Dans l'exercice suivant, trois condensateurs sont connectés en série. Dans la classe E, nous avons appris que pour les condensateurs en série, les inverses des capacités s'additionnent:

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

Ici aussi, les capacités doivent être converties dans la même unité avant le calcul afin que les inverses puissent être additionnés correctement.

[question:AD101]

---

Dans les circuits en courant alternatif, des résistances ohmiques connues ainsi que des résistances réactives apparaissent, comme nous l'avons déjà appris avec les condensateurs et les bobines. La résistance ohmique normale est appelée résistance active $R$. Les résistances réactives sont décrites par $X$. Les deux types de résistances influencent simultanément le flux de courant dans le circuit.

Puisque la résistance active et la résistance réactive agissent différemment, elles ne peuvent pas être simplement additionnées. Au lieu de cela, elles sont combinées géométriquement. On peut se représenter cela comme un triangle rectangle comme dans la figure [ref:a_dreieck]:

---
- La résistance active $R$ forme le côté horizontal.
- La résistance réactive $X$ forme le côté vertical.
- La résistance totale résultante est appelée résistance apparente $|Z|$.

<margin>
[picture:1067:a_dreieck:Triangle rectangle pour illustrer le calcul de la résistance apparente $|Z|$ à partir de la résistance active $R$ et de la résistance réactive $X$]
</margin>

La résistance apparente peut être calculée avec le théorème de Pythagore (voir recueil de formules):

$ |Z| = \sqrt{R^2 + X^2} $

La lettre $Z$ est utilisée pour l'impédance. Pour les calculs de ce chapitre, il suffit cependant de considérer la valeur $|Z|$ comme la résistance totale en courant alternatif du circuit.

<indepth>
Pour les intéressés par les mathématiques: l'impédance $Z$ est une grandeur complexe qui contient la résistance active $R$ comme partie réelle et la résistance réactive $X$ comme partie imaginaire:

$Z = R + jX$

La valeur $|Z|$ correspond alors à la longueur du vecteur dans le plan complexe, qui résulte de la combinaison de $R$ et $X$.
</indepth>

Pour la question suivante, avant de pouvoir appliquer le théorème de Pythagore, la résistance réactive $X_C$ du condensateur doit être calculée à $\qty{1}{\mega\hertz}$. Pour cela, nous utilisons la formule pour la résistance réactive d'un condensateur.

[question:AD104]

La question suivante traite du calcul de la résistance apparente d'un circuit série composé d'une résistance et d'une bobine. Tout d'abord, nous calculons $X_L$, puis nous appliquons à nouveau le théorème de Pythagore. Ici aussi, les puissances de dix doivent être prises en compte pour que le calcul soit effectué correctement.

[question:AD105]
