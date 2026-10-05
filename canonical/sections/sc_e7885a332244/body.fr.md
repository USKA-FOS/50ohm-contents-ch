Dans la section [sec:spannungsteiler_1], nous avons déjà fait connaissance avec le *diviseur de tension* *non chargé*. Dans cette section, nous nous intéressons au *diviseur de tension* *chargé*, où la tension de sortie $U_2$ est chargée par une résistance de charge $R_\mathrm{L}$. Cela signifie que la résistance de charge est en parallèle avec la résistance $R_2$, comme on peut le voir dans le schéma de la figure [ref:a_spannungsteiler_belastet].

<margin>
[picture:199:a_spannungsteiler_belastet:Diviseur de tension chargé]
</margin>

Pour un diviseur de tension chargé, il faut tenir compte du fait que le courant total augmente lorsque la charge augmente, c'est-à-dire lorsque la résistance de charge $R_\mathrm{L}$ devient plus faible. Il est préférable d'expliquer les effets de la charge à l'aide d'un exemple concret. Supposons que les résistances $R_1$ et $R_2$ aient chacune une valeur de $\qty{1}{\kilo\ohm}$ et que la tension totale $U_\mathrm{B}$ soit de $\qty{12}{\volt}$.

Dans le cas non chargé, la résistance $R_\mathrm{L}=\infty$, c'est-à-dire que la résistance n'existe pas et qu'aucun courant ne peut la traverser. La tension se répartit uniformément sur les deux résistances $R_1$ et $R_2$, c'est-à-dire que l'on peut mesurer $\qty{6}{\volt}$ sur chaque résistance. La résistance totale est de $R_{\mathrm{ges}}=\qty{2}{\kilo\ohm}$. Le courant total est de $I_1 = \frac{U_\mathrm{B}}{R_{\mathrm{ges}}}=\qty{6}{\milli\ampere}$. Ce courant traverse également $R_2$. La puissance dissipée est la même sur les deux résistances : $P_1 = P_2 = \qty{6}{\volt} \cdot \qty{6}{\milli\ampere} = \qty{36}{\milli\watt}$.

Dans le cas chargé, supposons que la résistance de charge soit également $R_\mathrm{L} = \qty{1}{\kilo\ohm}$. Le montage en parallèle de $R_2$ et $R_\mathrm{L}$ donne une résistance équivalente de $R_\mathrm{par}=\qty{500}{\ohm}$. La résistance totale du diviseur de tension n'est maintenant plus que de $R_{\mathrm{ges}}=\qty{1,5}{\kilo\ohm}$. Maintenant, un diviseur de tension avec $\qty{1}{\kilo\ohm}$ et $\qty{500}{\ohm}$ agit, et la tension totale se répartit en conséquence. $\frac{2}{3}$ de la tension totale ($\qty{8}{\volt}$) peut être mesurée sur $R_1$ et $\frac{1}{3}$ de la tension totale ($\qty{4}{\volt}$) peut être mesurée sur $R_\mathrm{par}$.

Le courant $I_1$ est maintenant de $I_1 = \frac{\qty{8}{\volt}}{\qty{1}{\kilo\ohm}}= \frac{\qty{12}{\volt}}{\qty{1,5}{\kilo\ohm}} = \qty{8}{\milli\ampere}$. Ce courant augmente donc.

La puissance sur $R_1$ est maintenant de $P_1 = U_1 \cdot I_1 = \qty{8}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{64}{\milli\watt}$, contre $\qty{36}{\milli\watt}$ dans le cas non chargé. Sur $R_\mathrm{par}$, la puissance est de $P_\mathrm{par} = U_\mathrm{par} \cdot I_\mathrm{par} = \qty{4}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{32}{\milli\watt}$, contre $\qty{36}{\milli\watt}$ dans le cas non chargé. Comme les ${32}{\milli\watt}$ se répartissent entre $R_2$ et $R_\mathrm{L}$, la puissance sur $R_2$ dans le cas chargé est réduite à $P_2 = \qty{4}{\volt} \cdot \qty{4}{\milli\ampere} = \qty{16}{\milli\watt}$.

En résumé : Lorsqu'on charge un diviseur de tension avec une résistance, le courant $I_1$ augmente. En conséquence, $R_1$ devient plus chaud et $R_2$ moins chaud. Avec ces connaissances, nous pouvons facilement résoudre la question suivante.

[question:AD115]

Pour la question suivante, nous devons combiner nos connaissances sur le diviseur de tension et le montage en parallèle des résistances. Pour cela, nous décomposons la tâche en étapes individuelles : d'abord, on détermine la résistance équivalente du montage en parallèle de $R_2$ et $R_\mathrm{L}$. Ensuite, le circuit peut être considéré comme un simple diviseur de tension et la tension de sortie $U_2$ peut être calculée.

[question:AD114]
