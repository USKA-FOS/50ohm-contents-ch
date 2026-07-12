Pour les signaux de courant alternatif sinusoïdaux, la puissance est calculée à partir des valeurs efficaces de courant et de tension. Il ne faut donc pas simplement utiliser la tension de crête à crête $U_\text{SS}$, ou la tension de crête $\hat{U}$ à la place.

<margin>
[picture:834:a_wechselstrom_leistung:Valeurs efficaces pour le calcul de la puissance]
</margin>

Ainsi, pour le calcul de la puissance
$P_\text{Wechselstrom} = U_\text{eff} \cdot I_\text{eff} = \dfrac{{U_\text{eff}}^2}{R} = I_\text{eff}^2 \cdot R$


Pour les signaux sinusoïdaux, on a toutefois également :

$U_\text{eff} = \dfrac {\hat{U}} {\sqrt{2}} = \dfrac {U_\text{SS}} {2 \cdot \sqrt{2}}$ 
$I_\text{eff} = \dfrac {\hat{I}} {\sqrt{2}} = \dfrac {I_\text{SS}} {2 \cdot \sqrt{2}}$ 

En conséquence, pour les signaux sinusoïdaux, les relations suivantes se présentent, pour lesquelles on peut également calculer avec les valeurs de crête et les valeurs de crête à crête :

$\begin{split} P_\text{Wechselstrom} &=  U_\text{eff} \cdot I_\text{eff} \\ &= \frac{\hat{U}\cdot\hat{I}}{\sqrt{2}\cdot\sqrt{2}} = \frac{\hat{U} \cdot \hat{I}}{2} \\ &= \frac{U_\text{eff}^2}{R} = \left(\frac{\hat{U}}{\sqrt{2}}\right)^2 \cdot \frac{1}{R} = \frac{\hat{U}^2}{2 \cdot R} \\ &= I_\text{eff}^2 \cdot R = \left(\frac{\hat{I}}{\sqrt{2}}\right)^2 \cdot R = \frac{\hat{I}^2\cdot R}{2} \end{split}$

La question suivante peut être résolue très facilement avec ces considérations ($I_\mathrm{max}$ n'est qu'une autre désignation pour $\hat{I}$) :

[question:AB301]

Dans le domaine du radioamateur, nous avons affaire à des tensions de fréquences différentes (par exemple, kilo- ou gigahertz) et de formes d'onde différentes (tension rectangulaire, tension sinusoïdale, tension continue). Celles-ci peuvent également être déformées et ne pas se présenter sous forme de, par exemple, tension sinusoïdale pure. Ces différentes tensions génèrent dans un circuit électrique des courants électriques différents. En principe, on aurait besoin de différents appareils pour mesurer cette gamme de courants électriques avec une précision de mesure raisonnable.

Dans le domaine du radioamateur, on utilise donc souvent un *thermoconvertisseur*.
On utilise ici le fait que le flux de courant chauffe le fil conducteur (cf. résistance des fils). Plus le courant est important, plus le fil devient chaud. Le réchauffement est donc proportionnel à l'intensité du courant. Le thermoconvertisseur mesure ce réchauffement et l'affiche comme intensité du courant. Il faut noter que nous obtenons avec cette méthode de mesure la *valeur efficace* de l'intensité du courant. L'avantage est maintenant que l'intensité du courant peut être déterminée presque *indépendamment* de la forme d'onde ou de la fréquence. Le thermoconvertisseur peut ainsi couvrir une grande gamme de signaux.

[question:AI105]
