Comme nous l'avons vu dans les sections précédentes, les transistors possèdent une courbe caractéristique qui représente la relation entre le signal d'entrée (tension base-émetteur ou grille-source) et le signal de sortie (courant de collecteur/drain). Sur cette courbe caractéristique, il existe différentes zones où le transistor présente un comportement linéaire ou non linéaire. Les zones où une variation de la grandeur de commande entraîne une variation proportionnelle de la grandeur de sortie sont dites linéaires. En représentation linéaire, ces zones se reconnaissent à une courbe droite, sans courbure. Les autres zones, où une variation de la grandeur de commande **ne** produit **pas** de variation proportionnelle de la grandeur de sortie, sont dites non linéaires.

<margin>
[picture:1085:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'entrée simplifiée d'un transistor avec différents points de fonctionnement]  
</margin>

La polarisation appliquée à la base ou à la grille détermine d'abord le point de fonctionnement de repos du transistor. Associée à l'amplitude du signal d'entrée, elle définit sur quelle partie de la courbe caractéristique le transistor est exploité et pendant quelle fraction d'une période du signal un courant circule. Cela donne lieu aux classes d'amplification A, A/B, B et C, qui présentent des propriétés différentes en termes de rendement, de linéarité, d'angle de conduction et de taux d'harmoniques. La figure [ref:a_kennlinien_transistor_arbeitspunkt] montre les points de fonctionnement de repos typiques des différentes classes d'amplification pour les modes A, B, A/B et C. Grâce à la conception du circuit amplificateur complet, leurs avantages et inconvénients respectifs peuvent être exploités ou partiellement compensés. Nous allons maintenant examiner les différentes classes d'amplification.

[question:AD416]

---

% Mode A de l'amplificateur :

En *mode A*, le point de fonctionnement est choisi de sorte que le transistor reste conducteur pendant toute la période du signal (angle de conduction $\qty{360}{\degree}$). Pour une exploitation maximale et symétrique, le point de fonctionnement de repos est souvent placé approximativement au milieu de la droite de charge, c'est-à-dire entre le blocage et la saturation, de sorte que le transistor fonctionne entièrement dans la zone linéaire. L'amplification du signal d'entrée (cf. [ref:a_eingangsspannung]) se fait alors autour du point de fonctionnement souhaité, qui définit le centre de la plage de travail. Le choix du point de fonctionnement détermine un courant de repos ($I_\mathrm{A}$) correspondant du transistor (cf. [ref:a_ausgangsstrom_a]). Ce courant circule même en l'absence de signal d'entrée. Le courant de repos influence considérablement l'efficacité d'un amplificateur, car il augmente sa puissance dissipée thermique et réduit ainsi son rendement. En mode A, on atteint généralement un rendement d'environ $\eta = \qty{40}{\percent}$, ce qui est une bonne valeur pour un amplificateur linéaire. Le taux d'harmoniques est très faible en mode A, car le transistor fonctionne entièrement dans la zone linéaire.

Tous les signaux dont l'information de modulation se trouve dans leur amplitude doivent généralement être amplifiés de manière linéaire pour transmettre l'information transmise sans distorsion (BLU, AM, etc.). Il existe toutefois des astuces de conception de circuit permettant de ne pas nécessairement recourir à un mode A linéaire. Les signaux dont l'information de modulation ne se trouve pas dans l'amplitude mais uniquement dans la fréquence peuvent également être amplifiés dans la zone non linéaire d'un amplificateur (FM, etc.) puis filtrés.

Résumé du mode A :

- Rendement d'environ $\qty{40}{\percent}$
- Taux d'harmoniques très faible
- Convient bien pour l'AM et la BLU
- Un courant de sortie circule sur toute la période (angle de conduction $\Theta =\qty{360}{\degree}$) du signal d'entrée

<margin>
[picture:1086:a_eingangsspannung:Exemple de tension d'entrée HF $U_\mathrm{BE}$ d'un transistor]
[picture:1087:a_ausgangsstrom_a:Exemple de courant de sortie HF $I_\mathrm{C}$ d'un transistor en mode A]
</margin>

[question:AD419]

% Mode B de l'amplificateur :

Si le point de fonctionnement est choisi pour le *mode B*, le transistor se trouve idéalement juste au point de blocage. Sans signal d'entrée, le courant de repos est pratiquement nul. Avec une commande sinusoïdale, comme illustré à la figure [ref:a_eingangsspannung], le transistor ne commence à conduire qu'à partir d'une certaine tension d'entrée. Un seul transistor n'est donc actif que pendant une demi-onde, soit un angle de conduction de $\qty{180}{\degree}$.
Comme, au repos, il ne consomme pratiquement aucune puissance, le rendement théorique d'un amplificateur idéal en mode B peut atteindre environ $\qty{80}{\percent}$. Cependant, la forme du courant d'un seul transistor n'est plus sinusoïdale et contient donc un taux élevé d'harmoniques.

Pour réduire ou supprimer les harmoniques, il existe en pratique différentes solutions :

- Une possibilité consiste à utiliser un montage push-pull (amplificateur en contre-phase), avec deux transistors, comme illustré à la figure [ref:a_gegentakt]. Chaque transistor amplifie alors une demi-onde, de sorte que les deux demi-ondes sont recombinées en un signal sinusoïdal complet et que le taux d'harmoniques est considérablement réduit.
- En plus du montage push-pull, un circuit oscillant accordé peut être utilisé pour les amplificateurs HF à bande étroite. Le transistor ne fournit alors des impulsions de courant que pendant une demi-onde. Le circuit oscillant stocke de l'énergie et continue d'osciller entre les impulsions de courant, de sorte qu'un signal presque sinusoïdal est obtenu en sortie sur toute la période. Autrement dit : le circuit oscillant agit comme un filtre qui supprime les composantes harmoniques. Cette solution n'est toutefois adaptée qu'aux amplificateurs HF à bande étroite, car un circuit oscillant n'est résonant que dans une plage de fréquences étroite.

<margin>
[picture:1089:a_ausgangsstrom_b:Exemple de courant de sortie HF $I_\mathrm{C}$ d'un transistor en mode B]
[picture:1091:a_gegentakt:Montage push-pull avec deux transistors, chacun amplifiant une demi-onde]
</margin>

Résumé du mode B :
- Faible polarisation jusqu'au déclenchement du courant de collecteur
- Courant de repos quasi nul
- Rendement jusqu'à environ $\qty{80}{\percent}$
- Faible taux d'harmoniques avec montage push-pull ou circuit oscillant
- Angle de conduction de $\Theta = \qty{180}{\degree}$, c'est-à-dire qu'une seule demi-onde est amplifiée

[question:AD420]
[question:AD417]

---

% Mode A/B de l'amplificateur :

Une autre possibilité de réaliser un amplificateur est le mode A/B, dans lequel le point de fonctionnement se situe entre les modes A et B. Le courant de repos ($I_\mathrm{A/B}$) est alors supérieur à celui du mode B, mais bien inférieur à celui du mode A, comme illustré à la figure [ref:a_ausgangsstrom_ab]. Le rendement se situe entre $\qty{50}{\percent}$ et $\qty{80}{\percent}$, et le taux d'harmoniques est faible avec une conception de circuit appropriée.

Résumé du mode A/B de l'amplificateur :
- Polarisation plus élevée qu'en mode B, mais plus faible qu'en mode A
- Courant de repos supérieur à celui du mode B, mais bien inférieur à celui du mode A
- Rendement entre $\qty{50}{\percent}$ et $\qty{80}{\percent}$
- Faible taux d'harmoniques
- Angle de conduction : $\qty{180}{\degree} < \Theta < \qty{360}{\degree}$

En particulier dans les modes A/B ou B d'un amplificateur, il faut éviter la surmodulation, car celle-ci peut rapidement entraîner des distorsions du signal. Celles-ci se manifestent en BLU par des splatters sur les fréquences adjacentes.
[question:AD423]

<margin>
[picture:1088:a_ausgangsstrom_ab:Exemple de courant de sortie HF $I_\mathrm{C}$ d'un transistor en mode A/B]
</margin>

---

% Mode C de l'amplificateur :

Le *mode C* est fortement non linéaire, car le transistor ne conduit que pendant une petite partie de l'oscillation d'entrée (cf. figure [ref:a_ausgangsstrom_c]). L'angle de conduction est inférieur à $\qty{180}{\degree}$ et, sans signal d'entrée, le courant de repos est idéalement nul. Cela permet d'atteindre des rendements élevés, typiquement de l'ordre de $\qtyrange{80}{87}{\percent}$.

Comme le transistor ne génère que de brèves impulsions de courant, son signal de sortie contient de forts taux d'harmoniques. Un circuit oscillant accordé ou un filtre en aval sélectionne la fréquence de sortie souhaitée et supprime les harmoniques indésirables. Comme ces harmoniques peuvent encore présenter des puissances considérables à l'intérieur de l'amplificateur de puissance et du filtre, le circuit et ses câbles doivent être soigneusement conçus et blindés pour éviter toute émission de signaux indésirables.

Le mode C convient particulièrement aux signaux à enveloppe constante, par exemple pour la FM et la CW. Pour l'AM et la BLU, il est sans mesures supplémentaires inadapté, car l'information d'amplitude serait déformée par l'amplification non linéaire. C'est pourquoi les amplificateurs AM et BLU utilisent généralement les modes A, B ou A/B. Des procédés spéciaux, comme la modulation polaire, permettent toutefois de générer des signaux à modulation d'amplitude à l'aide d'amplificateurs non linéaires très efficaces. Nous aborderons ce sujet plus en détail dans une section ultérieure.

Résumé : mode C de l'amplificateur
- Sans polarisation
- Courant de repos nul
- Rendement d'environ $\qtyrange{80}{87}{\percent}$
- Génère le taux d'harmoniques le plus élevé de toutes les classes d'amplification
- Angle de conduction de $\Theta < \qty{180}{\degree}$, c'est-à-dire qu'une petite partie seulement de l'onde sinusoïdale est amplifiée

<margin>
[picture:1090:a_ausgangsstrom_c:Exemple de courant de sortie HF $I_\mathrm{C}$ d'un transistor en mode C]
</margin>

[question:AD418]
[question:AD425]
[question:AD421]
[question:AD422]
[question:AJ218]
[question:AF402]
[question:AF403]

Résumons les classes d'amplification apprises dans un tableau récapitulatif :

| l: Propriété | X: Mode A | X: Mode B | X: Mode A/B | X: Mode C |
| Courant de repos | $I_\mathrm{A}$ | 0 | $I_\mathrm{A/B}$ | 0 |
| Rendement | $\qty{40}{\percent}$ | jusqu'à $\qty{80}{\percent}$ | $\qtyrange{50}{80}{\percent}$ | $\qtyrange{80}{87}{\percent}$ |
| Angle de conduction | $\Theta = \qty{360}{\degree}$ | $\Theta = \qty{180}{\degree}$ | $\qty{180}{\degree} < \Theta < \qty{360}{\degree}$ | $\Theta < \qty{180}{\degree}$ |
| Mesures contre les harmoniques | Filtre | Montage push-pull ou filtre | Montage push-pull ou filtre | Filtre |

La puissance de sortie d'un amplificateur peut être calculée approximativement à partir du point de fonctionnement et donc de son rendement approximatif. Pour cela, on calcule d'abord la puissance continue à partir du produit de la tension et du courant fournis à l'amplificateur. On multiplie ensuite cette puissance par le facteur numérique du rendement, où $\qty{100}{\percent}$ correspond à un rendement de 1. Par exemple, un rendement de $\qty{40}{\percent}$ correspond alors à un facteur de 0,4. Essayez maintenant de résoudre les exercices suivants :

[question:AD424]

En plus des classes d'amplification classiques A, B, AB et C, il existe d'autres classes d'amplification très efficaces, comme les classes D, E et F. Dans les amplificateurs de classe D et E, le transistor est utilisé comme un interrupteur, de sorte que la puissance dissipée dans le transistor lui-même soit aussi faible que possible. Les amplificateurs de classe F utilisent en outre des réseaux accordés pour la fréquence fondamentale et certaines harmoniques afin de façonner favorablement les courbes de courant et de tension au niveau du transistor. De cette manière, des rendements très élevés peuvent être atteints. Cependant, ces amplificateurs nécessitent une conception de circuit minutieuse et ne sont souvent adaptés qu'à une plage de fréquences limitée dans le domaine HF. D'autres modes de fonctionnement, tels que la classe J ou la classe S, poursuivent des objectifs similaires, mais ne sont pas pertinents pour l'examen de radioamateur.