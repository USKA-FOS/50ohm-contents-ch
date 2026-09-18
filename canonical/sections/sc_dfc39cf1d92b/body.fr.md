Les signaux peuvent être représentés de différentes manières. Jusqu’à présent, nous avons souvent considéré le *domaine temporel*. Dans ce cas, on représente par exemple comment la tension d’un signal évolue dans le temps. Le même signal peut cependant aussi être analysé dans le *domaine fréquentiel*. Ici, ce n’est plus l’évolution temporelle qui est représentée, mais les composantes fréquentielles qui constituent le signal et leur amplitude respective. Cette représentation est aussi appelée *spectre de fréquences*. Elle repose sur le fait que les signaux périodiques peuvent être décrits comme une superposition de sinusoïdes de fréquences, amplitudes et phases différentes.

Un signal sinusoïdal pur ne contient par exemple qu’une seule fréquence et apparaît donc dans le spectre de fréquences uniquement à cette fréquence.


La *transformée de Fourier* permet de passer du domaine temporel au domaine fréquentiel. Elle décompose mathématiquement un signal en ses différentes composantes fréquentielles. Pour les signaux discrets dans le temps et numérisés, on utilise la *transformée de Fourier discrète* (TFD). Le calcul direct d’une TFD peut devenir très complexe avec un grand nombre d’échantillons. La *transformée de Fourier rapide* (TFR) est un algorithme bien plus efficace pour calculer la TFD. C’est pourquoi la TFR est souvent utilisée dans les logiciels et les matériels numériques, par exemple pour déterminer le spectre de fréquences d’un signal.


<indepth>
Les formes d’onde non sinusoïdales sont composées de plusieurs composantes fréquentielles. En particulier, les variations brutales et les fronts raides dans l’évolution temporelle du signal nécessitent des composantes haute fréquence supplémentaires. Avec l’applet suivant, on peut étudier comment différentes sinusoïdes se superposent pour former diverses formes d’onde.


[include:fourier]
</indepth>

[question:AF630]

---

Le lien entre domaine temporel et domaine fréquentiel est particulièrement visible avec les signaux présentant des fronts raides. Un signal rectangulaire idéal peut par exemple être reconstitué à partir d’une fondamentale et de plusieurs harmoniques. Outre la fréquence fondamentale, apparaissent les multiples impairs de cette fréquence fondamentale. Leurs amplitudes diminuent à mesure que la fréquence augmente.

Ces harmoniques jouent aussi un rôle important pour les émetteurs. Si l’on appliquait directement un signal rectangulaire idéal à une antenne, non seulement la fréquence fondamentale souhaitée serait rayonnée, mais aussi ses harmoniques. Un *filtre passe-bas* permet de supprimer les composantes fréquentielles indésirables de plus haute fréquence, de sorte que seule la fondamentale souhaitée parvienne à l’antenne.

Pour certaines formes d’onde périodiques typiques, le spectre de fréquences peut être décrit de manière particulièrement simple. Nous considérons ici des formes d’onde idéalisées sans composante continue :


* Un *signal sinusoïdal* ne contient qu’une seule fréquence. Dans le spectre de fréquences, seule la fréquence fondamentale $f$ apparaît donc.
* Un *signal rectangulaire* est composé de la fréquence fondamentale et des *multiples impairs* de cette fréquence fondamentale. Il contient donc les fréquences $f$, $3\cdot f$, $5\cdot f$, $7\cdot f$ etc. Les amplitudes des harmoniques diminuent à mesure que la fréquence augmente.
* Un *signal en dents de scie* contient aussi bien les multiples pairs qu’impairs de la fréquence fondamentale. Il contient donc $f$, $2\cdot f$, $3\cdot f$, $4\cdot f$, $5\cdot f$ etc. Ici aussi, les amplitudes diminuent à mesure que la fréquence augmente.
* Un *signal triangulaire* ne contient, comme le signal rectangulaire, que les multiples impairs de la fréquence fondamentale, donc $f$, $3\cdot f$, $5\cdot f$, $7\cdot f$ etc. Cependant, les amplitudes des composantes fréquentielles plus élevées diminuent bien plus rapidement que pour le signal rectangulaire.

Ainsi, les formes d’onde peuvent aussi être distinguées par leur spectre de fréquences. Une seule composante spectrale indique un signal sinusoïdal. Si des multiples impairs apparaissent, il s’agit dans les questions d’examen toujours d’un signal rectangulaire.

[question:AB404]
[question:AB405]
[question:AB406]
[question:AB407]