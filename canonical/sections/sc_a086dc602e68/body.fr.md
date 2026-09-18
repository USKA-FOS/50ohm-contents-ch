De par son principe, un récepteur superhétérodyne génère, lors du processus de mélange (cf. illustration [ref:spiegelfrequenzen_mischen1]), avec la fréquence de l’oscillateur du récepteur, toujours deux fréquences de réception possibles :

$f_\text{ZF} = \left|f_\text{e} \pm f_\text{o}\right|$

Comme nous souhaitons, dans le récepteur superhétérodyne, descendre vers une fréquence intermédiaire (FI) plus basse, c’est en particulier la fréquence de différence qui nous intéresse :

$f_\text{ZF} = \left|f_\text{e} - f_\text{o}\right|$

La valeur absolue est ici déterminante : pour une fréquence d’oscillateur $f_\text{o}$ et une fréquence intermédiaire $f_\text{ZF}$ fixes, il existe deux fréquences de réception possibles qui produisent toutes deux la même FI. L’une d’elles est la fréquence de réception souhaitée, l’autre est appelée *fréquence image*.

<margin>
[picture:807:spiegelfrequenzen_mischen1:Processus de mélange avec fréquence de réception $f_\text{e}$, fréquence de l’oscillateur $f_\text{o}$ et la fréquence intermédiaire $f_\text{ZF}$]
</margin>

---

<margin>
[picture:806:spiegelfrequenzen_fe1_fe2:Fréquences de réception qui mènent toutes deux à la même $f_\text{ZF}$]
</margin>

Exemple : Supposons que notre oscillateur oscille, comme illustré dans l’image [ref:spiegelfrequenzen_fe1_fe2], à la fréquence $f_\text{o}=\qty{3,955}{\mega\hertz}$. La fréquence intermédiaire $f_\text{ZF}$ doit être de $\qty{0,455}{\mega\hertz}$. Grâce à la valeur absolue dans notre formule, il existe maintenant deux possibilités pour les fréquences de réception que l’on peut entendre, à savoir $f_\text{e1} = \qty{3,500}{\mega\hertz}$ et $f_\text{e2} = \qty{4,410}{\mega\hertz}$. Pour ces deux valeurs, la formule donne la fréquence intermédiaire $f_\text{ZF}$.

Si $f_\text{e1}$ est la fréquence de réception souhaitée, alors $f_\text{e2}$ est appelée la fréquence image de $f_\text{e1}$. Si $f_\text{e2}$ est la fréquence de réception souhaitée, alors $f_\text{e1}$ est la fréquence image de $f_\text{e2}$.

L’écart entre la fréquence de réception souhaitée et la fréquence image est toujours égal au double de la fréquence intermédiaire (FI), comme on peut le voir facilement dans l’illustration [ref:spiegelfrequenzen_fe1_fe2].

Si l’oscillateur oscille *au-dessus* de la fréquence de réception ($f_\mathrm{E} < f_\mathrm{OSZ}$), alors la fréquence image se trouve également à une distance du double de la FI *au-dessus* de la fréquence de réception ($f_\mathrm{S} = f_\mathrm{E} + 2\cdot f_\mathrm{ZF}$).

Si l’oscillateur se trouve en revanche *en dessous* de la fréquence de réception ($f_\mathrm{E} > f_\mathrm{OSZ}$), alors la fréquence image se trouve également à une distance du double de la FI *en dessous* de la fréquence de réception ($f_\mathrm{S} = f_\mathrm{E} - 2\cdot f_\mathrm{ZF}$). On trouve également cette relation dans le recueil de formules.

Essayez maintenant de résoudre les questions suivantes avec ces connaissances.

[question:AF106]
[question:AF201]
[question:AF202]
[question:AF203]
[question:AF107]
[question:AF108]

---
<margin>
[picture:808:spiegelfrequenzen_mischen2:Filtre passe-bande supplémentaire pour la suppression de la fréquence image]
</margin>

La fréquence image peut, en cas de suppression insuffisante, entraîner des interférences de réception, car les signaux sur la fréquence image sont également convertis vers la même fréquence intermédiaire et peuvent ainsi devenir audibles dans le récepteur. Pour éviter cela, la fréquence de réception souhaitée est, comme illustré dans l’image [ref:spiegelfrequenzen_mischen2], déjà sélectionnée avant le mélangeur à l’aide d’un filtre passe-bande. La fréquence image doit être fortement atténuée.

Pour une suppression efficace de la fréquence image, un écart aussi grand que possible entre la fréquence de réception souhaitée et la fréquence image est avantageux. Cet écart est d’autant plus grand que l’on choisit une fréquence intermédiaire plus élevée.

On peut également le constater à partir de l’illustration [ref:spiegelfrequenzen_fe1_fe2] : plus la FI est élevée, plus les deux fréquences de réception possibles $f_\text{e1}$ et $f_\text{e2}$ sont éloignées l’une de l’autre.

Plus cet écart de fréquence est grand, plus le filtre passe-bande en amont peut laisser passer facilement la fréquence de réception souhaitée et atténuer simultanément fortement la fréquence image. Si l’écart est très faible, le filtre devrait en revanche présenter des flancs beaucoup plus raides ou une sélectivité plus élevée. Les exigences en matière de présélection du récepteur seraient alors nettement plus élevées.

[question:AF109]
[question:AF110]
[question:AF111]
[question:AF204]