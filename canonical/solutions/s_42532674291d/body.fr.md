La diode Z stabilise la tension à la borne gauche de $R_2$ à

$U_Z=\qty{6,2}{\volt}$

Lorsque le curseur de $R_3$ est en butée 1, il est directement relié à la borne supérieure de $R_3$. Depuis ce point vers la masse, deux branches sont en parallèle :

$R_4=\qty{6,8}{\kilo\ohm}$

et

$R_3+R_6=\qty{220}{\ohm}+\qty{150}{\ohm}=\qty{370}{\ohm}$

La résistance équivalente vers la masse est donc :

$R_\mathrm{u}=R_4\parallel(R_3+R_6)$

$R_\mathrm{u}=\frac{\qty{6800}{\ohm}\cdot\qty{370}{\ohm}}{\qty{6800}{\ohm}+\qty{370}{\ohm}}\approx\qty{351}{\ohm}$

Il faut maintenant prendre en compte $R_2=\qty{270}{\ohm}$. $R_2$ et $R_\mathrm{u}$ forment un diviseur de tension à la tension stabilisée de $\qty{6,2}{\volt}$ :

$U_\mathrm{G}=\qty{6,2}{\volt}\cdot\frac{\qty{351}{\ohm}}{\qty{270}{\ohm}+\qty{351}{\ohm}}\approx\qty{3,5}{\volt}$

Les bornes de source des transistors étant reliées à la masse, la tension de grille correspond simultanément à la tension grille-source :

$U_\mathrm{GS}\approx\qty{3,5}{\volt}$

La tension grille-source est donc d’environ $\qty{3,5}{\volt}$.

À noter :

La résistance $R_5=\qty{51}{\ohm}$ n’influence pratiquement pas la tension continue à la grille, car un courant continu quasi nul circule dans la grille du transistor LDMOS. Pour le signal HF, $R_5$ est cependant important : il atténue, conjointement avec la capacité de grille, d’éventuelles oscillations haute fréquence et améliore ainsi la stabilité de l’amplificateur.

La résistance $R_4=\qty{6,8}{\kilo\ohm}$ garantit que la grille possède un potentiel défini par rapport à la masse même en cas de coupure du point de polarisation. Elle décharge également la capacité de grille et empêche ainsi que le transistor ne devienne conducteur de manière involontaire en raison d’une grille flottante. Comme $R_4$ est en parallèle avec la branche inférieure du diviseur de tension, il doit être pris en compte dans le calcul précis de la tension de grille.