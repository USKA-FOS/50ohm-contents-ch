<margin>
[picture:807:spiegelfrequenzen_mischen1:Mélange avec la fréquence de réception $f_\text{e}$, la fréquence de l’oscillateur $f_\text{o}$ et la fréquence intermédiaire $f_\text{ZF}$]
</margin>

Par conception, lors d'un récepteur superhétérodyne, deux fréquences de réception possibles sont toujours générées par le processus de mélange (voir figure [ref:spiegelfrequenzen_mischen1]) avec la fréquence de l’oscillateur du récepteur :

$f_\text{ZF} = \left|f_\text{e} \pm f_\text{o}\right|$

---

<margin>
[picture:806:spiegelfrequenzen_fe1_fe2:Fréquences de réception qui mènent toutes deux à la même $f_\text{ZF}$]
</margin>

Supposons que notre oscillateur oscille, comme le montre la figure [ref:spiegelfrequenzen_fe1_fe2], à la fréquence $f_\text{o}=\qty{3,955}{\mega\hertz}$. La fréquence intermédiaire $f_\text{ZF}$ doit être de $\qty{0,455}{\mega\hertz}$. Grâce à la valeur absolue dans notre formule, il existe désormais deux possibilités de fréquences de réception que l'on peut entendre, à savoir $f_\text{e1} = \qty{3,500}{\mega\hertz}$ et $f_\text{e2} = \qty{4,410}{\mega\hertz}$. Pour les deux valeurs, la formule donne la fréquence intermédiaire $f_\text{ZF}$.

Si $f_\text{e1}$ est la fréquence de réception souhaitée, alors $f_\text{e2}$ est appelée la *fréquence image* de $f_\text{e1}$. Si $f_\text{e2}$ est la fréquence de réception souhaitée, alors $f_\text{e1}$ est appelée la *fréquence image* de $f_\text{e2}$.

La distance entre la fréquence de réception souhaitée et la fréquence image est toujours le double de la fréquence intermédiaire (ZF).
Si l'oscillateur oscille <u>au-dessus</u> de la fréquence de réception, la fréquence image se trouve également <u>au-dessus</u> de la fréquence de réception, de deux fois la ZF.
Si l'oscillateur se trouve <u>en dessous</u> de la fréquence de réception, la fréquence image se trouve également <u>en dessous</u> de la fréquence de réception, de deux fois la ZF.

---
<margin>
[picture:808:spiegelfrequenzen_mischen2:Filtre passe-bande supplémentaire pour la suppression de la fréquence image]
</margin>

La fréquence image peut, en cas de suppression insuffisante, entraîner des perturbations de la réception, car les signaux qui se trouvent sur la fréquence image sont alors également audibles dans le récepteur. Pour éviter cela, la fréquence de réception souhaitée est sélectionnée, comme le montre la figure [ref:spiegelfrequenzen_mischen2], par un filtre passe-bande et la *fréquence image* est ainsi supprimée au maximum.

Pour permettre une suppression aussi élevée que possible de la fréquence image, il est avantageux que la distance entre la fréquence de réception souhaitée et la fréquence image puisse être choisie aussi grande que possible par une ZF élevée. Avec une grande distance entre la fréquence de réception souhaitée et la fréquence image, un filtre passe-bande de haute qualité peut être réalisé plus facilement qu'avec une petite distance.

[question:AF201]
[question:AF202]
[question:AF203]
[question:AF204]
[question:AF106]
[question:AF107]
[question:AF108]
[question:AF109]
[question:AF110]
[question:AF111]