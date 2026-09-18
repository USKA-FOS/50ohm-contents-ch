Dans chaque appareil radio, il existe une ou plusieurs stabilisations de tension, car la tension d'entrée, surtout dans les appareils alimentés par batterie, peut varier et entraîner des changements de fréquence dans des modules sensibles, comme par exemple les oscillateurs.

Il existe trois types de stabilisation de tension :
1. *Circuit avec diode Z*
2. *Régulateurs de tension linéaires*
3. *Régulateurs de tension fixes* dans un circuit intégré

Le *circuit avec diode Z* (cf. illustration [ref:a_stab_z_diode]) représente un circuit très simple pour stabiliser la tension de sortie, car la diode Z peut maintenir la tension de sortie dans certaines limites.

La diode Z fonctionne toujours avec une résistance en série et en polarisation inverse ($-U_Z$). Les diodes Z avec une tension de claquage $U_Z$ à partir de $\qty{5}{\volt}$ présentent une courbe caractéristique très raide (cf. illustration [ref:a_z_diode_kennlinie]) et sont donc très adaptées à la stabilisation de tension. Le rendement de ce circuit est très faible, car il faut prendre en compte les pertes dans la résistance en série $R_V$ et dans la diode Z.

<margin>
[picture:323:a_stab_z_diode:Stabilisation de tension avec diode Z]
[picture:862:a_z_diode_kennlinie:Caractéristique d'une diode Z]
</margin>

La solution de l'exercice suivant est un peu plus complexe. On détermine d'abord la puissance de sortie à partir de la résistance de charge et du courant de charge. Ensuite, on calcule la puissance d'entrée absorbée à partir de la tension d'alimentation et de la somme du courant de charge et du courant de la diode Z. Le rendement s'obtient alors à partir du rapport entre la puissance fournie et la puissance absorbée.

[question:AD321]

---

Les *régulateurs de tension linéaires* stabilisent la tension de sortie en faisant fonctionner un transistor de puissance comme une résistance variable, qui forme, avec la résistance de charge, un diviseur de tension.

<margin>
[picture:1079:a_diskrete_pannungsstabilisierung:Stabilisation de tension réalisée de manière discrète]
</margin>

Dans l'exercice suivant, un stabilisateur de tension discret avec un transistor série est représenté. Une tension de référence de $\qty{5,6}{\volt}$ est générée à la base du transistor via une diode Z. Le potentiel d'émetteur est, dans l'état de fonctionnement d'un transistor au silicium, d'environ $\qty{0,6}{\volt}$ inférieur au potentiel de base. La tension de sortie régulée est donc d'environ $\qty{5}{\volt}$.

Le courant de charge traverse également le transistor, qui devient donc très chaud en cas de courant de charge élevé. Les transistors série se trouvent donc toujours sur un radiateur dans les stabilisateurs de tension régulés linéairement.

<margin>
[photo:246:a_Längstransistor 2N3055 sur radiateur:Le transistor série dans une alimentation régulée linéairement doit supporter de grandes puissances dissipées et est donc monté sur un radiateur.]
</margin>

[question:AD315]

La puissance dissipée $P_V$ s'obtient à partir de la différence entre $P_{\mathrm{in}}$ et $P_{\mathrm{out}}$. En utilisant la formule de puissance $P = U \cdot I$, on peut calculer la puissance dissipée.

[question:AD319]

Dans les régulateurs de tension linéaires, le rendement est souvent très faible pour des raisons systémiques. Il existe une question sur le rendement qui peut être résolue avec la formule connue $\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$.

[question:AD320]

---

En plus de la diode Z et du régulateur de tension linéaire, il existe également des *régulateurs de tension fixes* dans un circuit intégré. Les régulateurs de tension fixes fonctionnent comme les régulateurs linéaires avec transistor série et intègrent une source de référence de tension très précise ainsi qu'une régulation électronique optimale. Même si la tension d'entrée varie fortement (par exemple $\qty{\pm 2}{\volt}$), la variation de tension du côté de la charge n'est mesurable qu'à l'échelle des millivolts. Les condensateurs des deux côtés du régulateur de tension fixe doivent être choisis selon les spécifications du fabricant, sinon des oscillations indésirables peuvent apparaître dans le comportement de régulation du circuit.

<margin>
[picture:200:a_Festspannungsregler:Régulateur de tension fixe]
</margin>

---

Un régulateur de tension fixe maintient sa tension de sortie largement constante tant que la tension d'entrée est suffisamment supérieure à la tension de sortie. La tension de sortie reste donc presque inchangée, même si la tension d'entrée varie.

[question:AD316]
[question:AD317]

<tip>
Pour que le circuit de régulation interne fonctionne de manière optimale, la tension d'entrée des régulateurs de tension fixes standard (par exemple le type 7812 pour une tension fixe de $\qty{12}{\volt}$) doit être supérieure d'environ $\qty{3}{\volt}$ à la tension de sortie, soit au moins $\qty{15}{\volt}$. Il existe des régulateurs de tension fixes pour lesquels la tension d'entrée ne doit être supérieure que de $\qty{1}{\volt}$ à la tension de sortie. Ces régulateurs sont appelés régulateurs à faible chute de tension (Low-Drop).
</tip>

---

Pour résoudre l'exercice suivant, nous utilisons à nouveau la relation connue : la puissance dissipée $P_V$ du régulateur de tension fixe s'obtient à partir de la différence entre $P_{\mathrm{in}}$ et $P_{\mathrm{out}}$.

[question:AD318]

<tip>
La démarche commence par le calcul du courant de charge : $I_L$. Remarque : le courant dans le conducteur de masse du régulateur de tension fixe est négligeable et n'est donc pas pris en compte.
</tip>

<margin>
[photo:245:a_Festspannungsregler:Régulateurs de tension fixes pour $\qty{5}{\volt}$, $\qty{12}{\volt}$ et $\qty{9}{\volt}$ sur radiateur]
</margin>