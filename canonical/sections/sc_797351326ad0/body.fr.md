Nous avons appris dans le chapitre précédent le récepteur détecteur comme le récepteur le plus simple. Le récepteur détecteur est un récepteur dit direct, que nous avons également appris dans la classe N. Dans le récepteur direct, comme le montre la figure [ref:e_geradeausempfänger], le signal est simplement démodulé après la réception et éventuellement l'amplification. Cependant, ce concept de récepteur a l'inconvénient d'une mauvaise sélectivité (sélectivité). Pour améliorer cela, on pourrait combiner le bloc de filtrage d'entrée (2) avec plusieurs filtres pour augmenter la sélectivité. Cependant, lors du changement de la fréquence de réception, tous ces filtres devraient être ajustés, ce qui est très fastidieux. C'est pourquoi le *récepteur superhétérodyne* (voir figure [ref:ueberlagerungsempfaenger_einfachsuper]) a été développé, qui est également appelé *superhétérodyne* ou *superhet* dans la langue technique.

<margin>
[picture:736:e_geradeausempfänger:Récepteur direct]
</margin>

<margin>
[picture:803:ueberlagerungsempfaenger_einfachsuper:Récepteur superhétérodyne avec amplificateurs]
</margin>

---

L'idée du récepteur superhétérodyne est aussi simple que géniale. Au lieu de filtres accordables, un oscillateur variable (VFO) est utilisé, à l'aide duquel le signal reçu est d'abord converti en une fréquence fixe, appelée fréquence intermédiaire $f_z$ (souvent également appelée ZF). Pour cette fréquence intermédiaire fixe, des filtres très sélectifs et de haute qualité peuvent être réalisés. La figure [ref:ueberlagerungsempfaenger_einfachsuper_filter] illustre ce principe.

<margin>
[picture:913:ueberlagerungsempfaenger_einfachsuper_filter:Récepteur superhétérodyne avec filtres]
</margin>

Le filtre d'entrée laisse d'abord passer seulement la bande de fréquences souhaitée, par exemple la bande des ondes courtes. Ensuite, un mélangeur convertit le signal d'entrée avec la fréquence du VFO en une fréquence intermédiaire constante, par exemple à $\qty{455}{\kilo\hertz}$. Dans l'exemple concret, le VFO peut être réglé entre $\qty{3,455}{\mega\hertz}$ et $\qty{30,455}{\mega\hertz}$ pour pouvoir convertir toute la bande des ondes courtes. L'avantage décisif du récepteur superhétérodyne par rapport au récepteur direct réside précisément dans cette fréquence intermédiaire constante : le filtrage du signal peut être optimisé pour une fréquence fixe, ce qui permet d'obtenir une très haute sélectivité, c'est-à-dire une sélectivité.

---

Comme les filtres n'ont pas besoin d'être accordables, ils peuvent être optimisés en termes de bande passante et de raideur de flanc, par exemple en utilisant des filtres à quartz, céramiques ou numériques. Ainsi, des filtres avec une bande passante d'environ $\qty{2,4}{\kilo\hertz}$ pour la transmission vocale (SSB) et des filtres à bande étroite d'environ $\qty{300}{\hertz}$ pour la télégraphie (CW) peuvent être utilisés. Des filtres adaptés peuvent également être utilisés pour d'autres procédés de transmission tels que l'AM, la FM ou les modes numériques.

Grâce à ce concept, le récepteur superhétérodyne atteint une sélectivité nettement supérieure à celle du récepteur direct. Un autre avantage réside dans le fait que tous les groupes de construction suivants fonctionnent toujours avec la même fréquence intermédiaire et ne doivent donc pas non plus être réalisés de manière accordable, ce qui simplifie la structure et améliore la qualité de réception.

[question:EF102]

Les récepteurs superhétérodynes peuvent fonctionner avec une ou plusieurs fréquences intermédiaires. Dans le cas le plus simple, il s'agit d'un récepteur à superhétérodyne directe, dans lequel la fréquence intermédiaire est la fréquence NF souhaitée. À cette fin, la fréquence de l'oscillateur doit être très proche de la fréquence de réception.

[question:EF208]

Un récepteur superhétérodyne présente cependant certains inconvénients, notamment l'apparition de fréquences dites images. Cette problématique ainsi que des concepts de récepteurs plus avancés tels que le superhétérodyne multiple avec plusieurs fréquences intermédiaires seront traités plus en détail dans la classe A.

<indepth>
L'inventeur du récepteur superhétérodyne ne peut pas être nommé de manière univoque. Cela est dû, entre autres, au fait que son développement remonte à l'époque de la Première Guerre mondiale, période pendant laquelle toutes les parties belligérantes travaillaient intensivement à l'amélioration des techniques radio et radiophoniques. Vers l'année 1918, plusieurs chercheurs se sont intéressés indépendamment les uns des autres à ce principe de fonctionnement, parmi lesquels Edwin Armstrong aux États-Unis, Lucien Lévy en France et Walter Schottky en Allemagne.

Le terme hétérodyne ou superhétérodyne est un néologisme. Il est composé du latin super ("sur") ainsi que des mots grecs hetero ("différent") et dynamis ("force" ou "effet"). Le nom décrit le principe de fonctionnement fondamental du récepteur superhétérodyne : le mélange de deux signaux de fréquences différentes pour générer une nouvelle fréquence.
</indepth>