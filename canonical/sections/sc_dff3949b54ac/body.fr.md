Pour les signaux de courant alternatif sinusoïdaux, la puissance est calculée à partir des valeurs efficaces de la tension et de l'intensité du courant. Il n'est donc pas possible d'utiliser directement la tension de crête à crête $U_\text{SS}$ ou la tension de crête $\hat{U}$ à la place.

<margin>
[picture:834:a_wechselstrom_leistung:Valeurs efficaces pour le calcul de la puissance]
</margin>

La formule de calcul de la puissance s'écrit donc :
$P_\text{courant alternatif} = U_\text{eff} \cdot I_\text{eff} = \dfrac{{U_\text{eff}}^2}{R} = I_\text{eff}^2 \cdot R$


Pour les signaux sinusoïdaux, on a également les relations suivantes :

$U_\text{eff} = \dfrac {\hat{U}} {\sqrt{2}} = \dfrac {U_\text{SS}} {2 \cdot \sqrt{2}}$
$I_\text{eff} = \dfrac {\hat{I}} {\sqrt{2}} = \dfrac {I_\text{SS}} {2 \cdot \sqrt{2}}$

Les relations suivantes permettent de calculer la puissance en utilisant les valeurs de crête ou de crête à crête pour les signaux sinusoïdaux :

$\begin{split} P_\text{courant alternatif} &=  U_\text{eff} \cdot I_\text{eff} \\ &= \frac{\hat{U}\cdot\hat{I}}{\sqrt{2}\cdot\sqrt{2}} = \frac{\hat{U} \cdot \hat{I}}{2} \\ &= \frac{U_\text{eff}^2}{R} = \left(\frac{\hat{U}}{\sqrt{2}}\right)^2 \cdot \frac{1}{R} = \frac{\hat{U}^2}{2 \cdot R} \\ &= I_\text{eff}^2 \cdot R = \left(\frac{\hat{I}}{\sqrt{2}}\right)^2 \cdot R = \frac{\hat{I}^2\cdot R}{2} \end{split}$

La question suivante peut être résolue très facilement à l'aide de ces considérations ($I_\mathrm{max}$ n'est qu'une autre désignation pour $\hat{I}$) :

[question:AB301]

Dans le domaine de la radio amateur, on est confronté à des tensions de fréquences (par exemple kilohertz ou gigahertz) et de formes d'onde (tension rectangulaire, tension sinusoïdale, tension continue) différentes. Ces tensions peuvent également être déformées et ne pas se présenter, par exemple, sous la forme d'une tension sinusoïdale pure. Ces différentes tensions génèrent dans un circuit électrique des courants électriques différents. En principe, il faudrait donc différents appareils pour mesurer cette gamme de courants électriques avec une précision raisonnable.

C'est pourquoi, dans le domaine de la radio amateur, on utilise souvent un *convertisseur thermique*.
On exploite ici le fait que le passage du courant chauffe le fil conducteur (cf. résistance des fils). Plus le courant est élevé, plus le fil s'échauffe. L'échauffement est donc proportionnel à l'intensité du courant. Le convertisseur thermique mesure cet échauffement et l'affiche comme intensité du courant. Il est important de noter que cette méthode de mesure donne la *valeur efficace* de l'intensité du courant. L'avantage est que l'intensité du courant peut être déterminée presque *indépendamment* de la forme d'onde ou de la fréquence. Le convertisseur thermique peut ainsi couvrir une large gamme de signaux.

[question:AI105]