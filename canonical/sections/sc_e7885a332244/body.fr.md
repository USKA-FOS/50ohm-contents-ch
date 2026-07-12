Dans la classe E, nous avons déjà étudié le diviseur de tension *non chargé*. Dans la classe A, nous nous intéressons au diviseur de tension *chargé*, où la tension de sortie $U_2$ est chargée par une résistance de charge $R_L$. Cela signifie que la résistance de charge est en parallèle avec la résistance $R_2$, comme le montre le schéma de la figure [ref:a_spannungsteiler_belastet].

<margin>
[picture:199:a_spannungsteiler_belastet:diviseur de tension chargé]
</margin>

Dans le cas d'un diviseur de tension chargé, il faut tenir compte du fait que le courant total augmente lorsque la charge est augmentée, c'est-à-dire lorsque la résistance de charge $R_L$ devient plus faible. Nous expliquons le mieux les effets de la charge par un exemple concret. Supposons que les résistances $R_1$ et $R_2$ aient chacune une valeur de $\qty{1}{\kilo\ohm}$ et que la tension totale $U_B$ soit de $\qty{12}{\volt}$.

Dans le cas non chargé, la résistance $R_{\mathrm{L}}=\infty$, la résistance n'existe donc pas et aucun courant ne peut la traverser. La tension se répartit uniformément entre les deux résistances $R_1$ et $R_2$, c'est-à-dire que $\qty{6}{\volt}$ peuvent être mesurés à chaque résistance. La résistance totale est de $R_{\mathrm{ges}}=\qty{2}{\kilo\ohm}$. Le courant total est de $I_1 = \frac{U_B}{R_{\mathrm{ges}}}=\qty{6}{\milli\ampere}$. Ce courant traverse également $R_2$. La puissance dissipée est la même aux deux résistances : $P_1 = P_2 = \qty{6}{\volt} \cdot \qty{6}{\milli\ampere} = \qty{36}{\milli\watt}$.

Dans le cas chargé, la résistance de charge doit maintenant également être de $R_L = \qty{1}{\kilo\ohm}$. Le circuit en parallèle de $R_2$ et $R_L$ donne une résistance de remplacement de $R_{\mathrm{par}}=\qty{500}{\ohm}$. La résistance totale du diviseur de tension n'est maintenant plus que de $R_{\mathrm{ges}}=\qty{1,5}{\kilo\ohm}$. Maintenant, un diviseur de tension avec $\qty{1}{\kilo\ohm}$ à $\qty{500}{\ohm}$ est efficace et la tension totale se répartit en conséquence. $\frac{2}{3}$ de la tension totale ($\qty{8}{\volt}$) peut être mesurée à $R_1$ et $\frac{1}{3}$ de la tension totale ($\qty{4}{\volt}$) peut être mesurée à $R_{\mathrm{par}}$. 

Le courant $I_1$ est maintenant de $I_1 = \frac{\qty{8}{\volt}}{\qty{1}{\kilo\ohm}}= \frac{\qty{12}{\volt}}{\qty{1,5}{\kilo\ohm}} = \qty{8}{\milli\ampere}$. Ce courant augmente donc. 

La puissance à $R_1$ est maintenant de $P_1 = U_1 \cdot I_1 = \qty{8}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{64}{\milli\watt}$ contre $\qty{36}{\milli\watt}$ dans le cas non chargé. À $R_{\mathrm{par}}$, la puissance est de $P_{\mathrm{par}} = U_{\mathrm{par}} \cdot I_{\mathrm{par}} = \qty{4}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{32}{\milli\watt}$ contre $\qty{36}{\milli\watt}$ dans le cas non chargé, car la puissance se répartit entre $R_2$ et $R_L$.

En résumé : lorsque l'on charge un diviseur de tension avec une résistance, le courant $I_1$ augmente. Cela fait que $R_1$ devient plus chaud et $R_2$ moins chaud. Avec ces connaissances, nous pouvons facilement résoudre la question suivante.

[question:AD115]

Pour la question suivante, nous devons combiner nos connaissances sur le diviseur de tension et le circuit en parallèle des résistances. Pour ce faire, nous décomposons la tâche en étapes individuelles : d'abord, la résistance de remplacement du circuit en parallèle de $R_2$ et $R_L$ est déterminée. Ensuite, le circuit peut être considéré comme un simple diviseur de tension et la tension de sortie $U_2$ peut être calculée à partir de celui-ci.

[question:AD114]





