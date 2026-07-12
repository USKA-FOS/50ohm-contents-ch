Dans chaque appareil radio, il y a une ou plusieurs stabilisations de tension, car la tension d'entrée, surtout dans les appareils fonctionnant avec une batterie, peut varier et alors des composants sensibles, comme par exemple des oscillateurs, changeraient leur fréquence.

Il existe trois variantes de stabilisations de tension :
1. *Circuit avec diode Z* 
2. *Régulateurs de tension linéaires* 
3. *Régulateurs de tension fixe* dans un circuit intégré

Le *circuit avec diode Z* (voir figure [ref:a_stab_z_diode]) représente un circuit très simple pour stabiliser la tension de sortie, car la diode Z peut maintenir la tension de sortie stable dans certaines limites.

La diode Z est toujours utilisée avec une résistance en série et en sens inverse ($-U_Z$). Les diodes Z avec des tensions de claquage $U_Z$ à partir de $\qty{5}{\volt}$, présentent une courbe caractéristique très raide (voir figure [ref:a_z_diode_kennlinie]) et sont donc très adaptées à la stabilisation de tension. Le rendement du circuit est très faible, car les pertes dans la résistance en série $R_V$ et dans la diode Z doivent être prises en compte. 

<margin>
[picture:323:a_stab_z_diode:Stabilisation de tension avec diode Z]
[picture:862:a_z_diode_kennlinie:Caractéristique d'une diode Z]
</margin>

La solution de l'exercice suivant est un peu plus complexe. Tout d'abord, la puissance de sortie est déterminée à partir de la résistance de charge et du courant de charge. Ensuite, la puissance d'entrée est calculée à partir de la tension d'alimentation ainsi que de la somme du courant de charge et du courant de la diode Z. Le rendement résulte alors du rapport entre la puissance fournie et la puissance absorbée.

[question:AD321]

---

Les *régulateurs de tension linéaires* stabilisent la tension de sortie en faisant fonctionner un transistor de puissance comme une résistance variable et en formant avec la résistance de charge un diviseur de tension.

<margin>
[picture:1079:a_diskrete_pannungsstabilisierung:Stabilisation de tension construite de manière discrète]
</margin>

Dans la question suivante, une stabilisation de tension discrète avec un transistor en série est représentée. Une tension de référence de $\qty{5,6}{\volt}$ est générée à la base du transistor via une diode Z. Le potentiel de l'émetteur est, dans l'état de fonctionnement d'un transistor au silicium, d'environ $\qty{0,6}{\volt}$ inférieur au potentiel de la base. La tension de sortie régulée est alors d'environ $\qty{5}{\volt}$.

Le courant de charge traverse également le transistor et celui-ci devient très chaud en cas de courant de charge élevé. Les transistors en série appelés se trouvent donc toujours sur un dissipateur thermique dans les stabilisations de tension régulées linéairement. 

<margin>
[photo:246:a_Längstransistor 2N3055 sur dissipateur thermique:Le transistor en série dans une alimentation régulée linéairement doit supporter de grandes puissances dissipées et est donc monté sur un dissipateur thermique.]
</margin>

[question:AD315]

La puissance dissipée $P_V$ résulte de la différence de $P_{\mathrm{in}} - P_{\mathrm{out}}$. Avec la formule de puissance $P = U \cdot I$, la puissance dissipée peut être calculée.

[question:AD319]

Dans les régulateurs de tension linéaires, le rendement est souvent très faible pour des raisons systémiques. Il y a une question sur le rendement, qui peut être résolue avec la formule connue ci-dessus $\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$. 

[question:AD320]

---

Outre la diode Z et le régulateur de tension linéaire, il existe également des *régulateurs de tension fixe* dans un circuit intégré. Les régulateurs de tension fixe fonctionnent comme les régulateurs de tension linéaires avec transistor en série et comportent une source de référence de tension très précise ainsi qu'une régulation électronique optimale. Même si la tension d'entrée varie fortement (par exemple de $\qty{\pm 2}{\volt}$), la variation de tension du côté de la charge n'est mesurable que dans la plage des millivolts. Les condensateurs des deux côtés du régulateur de tension fixe doivent être choisis selon les spécifications du fabricant, sinon des oscillations indésirables peuvent se produire dans le comportement de régulation du circuit.

<margin>
[picture:200:a_Festspannungsregler:Régulateur de tension fixe]
</margin>

---

Un régulateur de tension fixe maintient sa tension de sortie largement constante, tant que la tension d'entrée est suffisamment supérieure à la tension de sortie. La tension de sortie reste donc presque inchangée, même si la tension d'entrée varie.

[question:AD316]
[question:AD317]

<tip>
Pour que le circuit de régulation interne fonctionne de manière optimale, la tension d'entrée doit être, pour les régulateurs de tension fixe standard (par exemple le type 7812 pour une tension fixe de $\qty{12}{\volt}$), d'environ $\qty{3}{\volt}$ supérieure à la tension de sortie, donc au moins $\qty{15}{\volt}$. Il existe des régulateurs de tension fixe pour lesquels la tension d'entrée ne doit être que $\qty{1}{\volt}$ supérieure à la tension de sortie. Ces régulateurs sont appelés régulateurs de tension à faible chute.
</tip>

---

Pour résoudre l'exercice suivant, nous utilisons à nouveau la relation connue : la puissance dissipée $P_V$ du régulateur de tension fixe résulte de la différence entre $P_{\mathrm{in}}$ et $P_{\mathrm{out}}$.

[question:AD318]

<tip>
Le processus de résolution commence par le calcul du courant de charge : $I_L$. Indication : le courant dans la ligne de masse du régulateur de tension fixe est négligeable et n'est donc pas pris en compte.
</tip>

<margin>
[photo:245:a_Festspannungsregler:Régulateur de tension fixe pour $\qty{5}{\volt}$, $\qty{12}{\volt}$ et $\qty{9}{\volt}$ sur dissipateur thermique]
</margin>