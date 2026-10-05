Dans la section [sec:reihe_parallel_widerstandsnetz_1], nous avons déjà analysé des réseaux de résistances. La plupart des exercices pouvaient encore être résolus assez facilement de tête. Ici, ce sujet est maintenant approfondi. Les exercices suivants nécessitent plusieurs étapes de calcul pour arriver à la solution. Pour cela, on décompose l'exercice en sous-parties individuelles, qui sont d'abord calculées puis combinées. De cette manière, on n'a pas besoin de formules compliquées et on arrive de manière fiable au bon résultat.

[question:AD106]
[question:AD107]
[question:AD108]

Dans le circuit de résistances suivant, une résistance variable (potentiomètre) est intégrée.
La valeur de la résistance peut être modifiée de $\qty{0}{\kilo\ohm}$ jusqu'à un maximum de $\qty{1}{\kilo\ohm}$.
Pour déterminer la plage de la résistance d'entrée, nous devons donc considérer deux cas limites : d'une part, lorsque le curseur du potentiomètre est à $\qty{0}{\ohm}$, et d'autre part, lorsqu'il est à $\qty{1}{\kilo\ohm}$. Donc, en quelque sorte, deux exercices en un.

---

[question:AD109]

<tip>
Le montage en parallèle de $\qty{100}{\ohm}$ avec $\qty{200}{\ohm}$ (curseur du potentiomètre à $\qty{0}{\ohm}$) ou de $\qty{100}{\ohm}$ avec $\qty{1,2}{\kilo\ohm}$ (curseur du potentiomètre à $\qty{1}{\kilo\ohm}$) donne toujours une valeur inférieure à $\qty{100}{\ohm}$. Si on ajoute encore $\qty{200}{\ohm}$, la résistance totale ne sera pas supérieure à $\qty{300}{\ohm}$.
Il n'y a qu'une seule solution qui satisfait cette condition.
</tip>

Nous examinons maintenant un circuit de résistances avec 4 résistances, souvent utilisé. Deux diviseurs de tension montés en parallèle donnent un circuit en pont. Les circuits en pont sont utilisés par exemple dans les ohmmètres selon le principe d'un pont de mesure de Wheatstone.

---

[question:AD110]

<tip>
Cet exercice peut aussi être facilement calculé de tête. Nous avons deux montages en parallèle avec des résistances identiques, qui sont montées en série. Pour des résistances de même valeur, les valeurs de résistance sont divisées par deux dans le montage en parallèle : $R_1 || R_2 = \qty{1100}{\ohm}$ ainsi que $R_3 || R_4 = \qty{110}{\ohm}$. Le résultat est alors simplement la somme des deux valeurs : $R_\mathrm{ges} = \qty{1100}{\ohm} + \qty{110}{\ohm} = \qty{1210}{\ohm}$.
</tip>