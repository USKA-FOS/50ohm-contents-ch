Comme récepteur le plus simple, nous avons appris à connaître le récepteur à détection dans le chapitre précédent. Le récepteur à détection est un récepteur dit *à conversion directe*, que nous avons déjà étudié dans la classe N. Dans un récepteur à conversion directe, comme illustré dans la figure [ref:e_geradeausempfänger], le signal est simplement démodulé après réception et éventuellement amplification. Cependant, ce concept de récepteur présente l’inconvénient d’une faible sélectivité (pouvoir séparateur). Pour l’améliorer, on pourrait combiner plusieurs filtres dans le bloc de filtrage d’entrée (2) afin d’augmenter la sélectivité. Toutefois, il faudrait alors adapter tous ces filtres lors du changement de fréquence de réception, ce qui est très fastidieux. C’est pourquoi le *récepteur superhétérodyne* (cf. figure [ref:ueberlagerungsempfaenger_einfachsuper]) a été développé ; en langage technique, il est aussi appelé *Superheterodyne* ou *Superhet*.

<margin>
[picture:736:e_geradeausempfänger:Récepteur à conversion directe]
</margin>

<margin>
[picture:803:ueberlagerungsempfaenger_einfachsuper:Récepteur superhétérodyne avec amplificateurs]
</margin>

---

L’idée du récepteur superhétérodyne est aussi simple qu’ingénieuse. Au lieu d’utiliser des filtres accordables, on emploie un oscillateur variable (VFO) qui permet de transposer le signal reçu vers une fréquence fixe, appelée *fréquence intermédiaire* $f_z$ (souvent désignée par FI). Pour cette fréquence intermédiaire fixe, il est possible de réaliser des filtres très sélectifs et de haute qualité. La figure [ref:ueberlagerungsempfaenger_einfachsuper_filter] illustre ce principe.

<margin>
[picture:913:ueberlagerungsempfaenger_einfachsuper_filter:Récepteur superhétérodyne avec filtres]
</margin>

Le filtre d’entrée laisse d’abord passer uniquement la bande de fréquences souhaitée, par exemple la bande des ondes courtes. Ensuite, un mélangeur transpose le signal d’entrée, combiné à la fréquence du VFO, vers la fréquence intermédiaire constante, par exemple $\qty{455}{\kilo\hertz}$. Dans cet exemple concret, le VFO peut être réglé entre $\qty{3,455}{\mega\hertz}$ et $\qty{30,455}{\mega\hertz}$ pour pouvoir transposer toute la bande des ondes courtes. L’avantage décisif du récepteur superhétérodyne par rapport au récepteur à conversion directe réside précisément dans cette fréquence intermédiaire constante : le filtrage du signal peut être optimisé pour une fréquence fixe, ce qui permet d’atteindre une sélectivité, c’est-à-dire un pouvoir séparateur, très élevé.

---

Comme les filtres n’ont pas besoin d’être accordables, ils peuvent être optimisés de manière ciblée en termes de bande passante et de pente du front, par exemple en utilisant des filtres à quartz, céramiques ou numériques. Ainsi, pour la transmission vocale (SSB), on peut utiliser des filtres d’une bande passante d’environ $\qty{2,4}{\kilo\hertz}$, et pour la télégraphie (CW), des filtres étroits d’environ $\qty{300}{\hertz}$. Des filtres adaptés peuvent également être utilisés pour d’autres modes de transmission comme l’AM, la FM ou les modes numériques.

Grâce à ce concept, le récepteur superhétérodyne atteint une sélectivité nettement supérieure à celle du récepteur à conversion directe. Un autre avantage est que tous les modules suivants fonctionnent toujours avec la même fréquence intermédiaire et n’ont donc pas besoin d’être accordables, ce qui simplifie la structure et améliore la qualité de réception.

[question:EF102]

Les récepteurs superhétérodynes peuvent fonctionner avec une ou plusieurs fréquences intermédiaires. Dans le cas le plus simple, il s’agit d’un *récepteur à conversion directe*, où la fréquence intermédiaire est la fréquence BF souhaitée. À cette fin, la fréquence de l’oscillateur doit être très proche de la fréquence de réception.

[question:EF208]

Un récepteur superhétérodyne présente cependant aussi certains inconvénients, notamment l’apparition de fréquences images. Cette problématique, ainsi que des concepts de récepteurs avancés comme le superhétérodyne multiple avec plusieurs fréquences intermédiaires, seront abordés plus en détail dans la classe A.

<indepth>
L’inventeur du récepteur superhétérodyne ne peut pas être identifié de manière univoque. Cela s’explique notamment par le fait que son développement coïncide avec la période de la Première Guerre mondiale, durant laquelle toutes les parties belligérantes travaillaient intensivement à l’amélioration des techniques radio et de transmission sans fil. Plusieurs chercheurs ont étudié ce principe de fonctionnement de manière indépendante autour de l’année 1918, dont Edwin Armstrong aux États-Unis, Lucien Lévy en France ainsi que Walter Schottky en Allemagne.

Le terme *Heterodyn* ou *Superheterodyn* est une néologie. Il est composé du latin *super* (« au-dessus ») ainsi que des mots grecs *hetero* (« différent ») et *dynamis* (« force » ou « effet »). Ce nom décrit le principe de fonctionnement fondamental du récepteur superhétérodyne : le mélange de deux signaux de fréquences différentes pour générer une nouvelle fréquence.
</indepth>