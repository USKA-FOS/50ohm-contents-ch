Dans la classe E, nous avons déjà étudié le *diviseur de tension non chargé*. Dans la classe A, nous nous intéressons au *diviseur de tension chargé*, où la tension de sortie $U_2$ est soumise à une charge via une résistance de charge $R_\mathrm{L}$. Cela signifie que la résistance de charge est connectée en parallèle avec la résistance $R_2$, comme illustré dans le schéma de la figure [ref:a_spannungsteiler_belastet].

<margin>
[picture:199:a_spannungsteiler_belastet:Diviseur de tension chargé]
</margin>

Dans le cas d’un diviseur de tension chargé, il faut tenir compte du fait que le courant total augmente lorsque la charge est augmentée, c’est-à-dire lorsque la résistance de charge $R_\mathrm{L}$ devient plus faible. Les effets de la charge sont mieux expliqués à l’aide d’un exemple concret. Supposons que les résistances $R_1$ et $R_2$ valent chacune $\qty{1}{\kilo\ohm}$ et que la tension totale $U_\mathrm{B}$ soit de $\qty{12}{\volt}$.

Dans le cas non chargé, la résistance $R_\mathrm{L}$ vaut $\infty$, cette résistance n’existe donc pas et aucun courant ne peut la traverser. La tension se répartit uniformément entre les deux résistances $R_1$ et $R_2$, ce qui signifie que $\qty{6}{\volt}$ peuvent être mesurés aux bornes de chaque résistance. La résistance totale vaut $R_{\mathrm{ges}}=\qty{2}{\kilo\ohm}$. Le courant total est de $I_1 = \frac{U_\mathrm{B}}{R_{\mathrm{ges}}}=\qty{6}{\milli\ampere}$. Ce courant traverse également $R_2$. La puissance dissipée est identique aux deux résistances : $P_1 = P_2 = \qty{6}{\volt} \cdot \qty{6}{\milli\ampere} = \qty{36}{\milli\watt}$.

Dans le cas chargé, la résistance de charge est maintenant de $R_\mathrm{L} = \qty{1}{\kilo\ohm}$. Le montage en parallèle de $R_2$ et $R_\mathrm{L}$ donne une résistance équivalente de $R_\mathrm{par}=\qty{500}{\ohm}$. La résistance totale du diviseur de tension n’est plus que de $R_{\mathrm{ges}}=\qty{1,5}{\kilo\ohm}$. Il s’agit maintenant d’un diviseur de tension avec $\qty{1}{\kilo\ohm}$ en série avec $\qty{500}{\ohm}$, et la tension totale se répartit en conséquence. $\frac{2}{3}$ de la tension totale ($\qty{8}{\volt}$) peuvent être mesurés aux bornes de $R_1$, et $\frac{1}{3}$ de la tension totale ($\qty{4}{\volt}$) aux bornes de $R_\mathrm{par}$.

Le courant $I_1$ vaut maintenant $I_1 = \frac{\qty{8}{\volt}}{\qty{1}{\kilo\ohm}}= \frac{\qty{12}{\volt}}{\qty{1,5}{\kilo\ohm}} = \qty{8}{\milli\ampere}$. Ce courant augmente donc.

La puissance aux bornes de $R_1$ est maintenant de $P_1 = U_1 \cdot I_1 = \qty{8}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{64}{\milli\watt}$, contre $\qty{36}{\milli\watt}$ dans le cas non chargé. Aux bornes de $R_\mathrm{par}$, la puissance est de $P_\mathrm{par} = U_\mathrm{par} \cdot I_\mathrm{par} = \qty{4}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{32}{\milli\watt}$, contre $\qty{36}{\milli\watt}$ dans le cas non chargé. Comme les $\qty{32}{\milli\watt}$ se répartissent entre $R_2$ et $R_\mathrm{L}$, la puissance dissipée par $R_2$ dans le cas chargé se réduit à $P_2 = \qty{4}{\volt} \cdot \qty{4}{\milli\ampere} = \qty{16}{\milli\watt}$.

En résumé : lors de la charge d’un diviseur de tension avec une résistance, le courant $I_1$ augmente. Cela a pour effet d’échauffer davantage $R_1$ et moins $R_2$. Grâce à ces connaissances, nous pouvons facilement résoudre la question suivante.

[question:AD115]

Pour la question suivante, nous devons combiner nos connaissances sur le diviseur de tension et le montage en parallèle de résistances. Pour cela, nous décomposons la tâche en étapes individuelles : d’abord, nous déterminons la résistance équivalente du montage en parallèle de $R_2$ et $R_\mathrm{L}$. Ensuite, nous pouvons considérer le circuit comme un simple diviseur de tension et calculer à partir de là la tension de sortie $U_2$.

[question:AD114]