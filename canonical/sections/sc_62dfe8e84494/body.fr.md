Le troisième composant passif en radioélectricité – après la résistance et le condensateur – est la *bobine*. Différents types de bobines et leurs symboles de circuit sont illustrés dans les figures [ref:e_spulen] et [ref:e_schaltsymbole_spulen]. Comme nous l'avons déjà appris dans le chapitre sur le champ magnétique, une bobine génère un champ magnétique dès qu'un courant électrique la traverse. La forme de construction la plus simple d'une bobine est la *bobine cylindrique* droite, comme illustré dans la figure [ref:e_spule_Aufbau].


<margin>
[photo:207:e_spulen:Différentes formes de construction de bobines]
[picture:942:e_schaltsymbole_spulen:Symboles de circuit pour différents types de bobines]
[picture:948:e_spule_Aufbau:Structure d'une bobine]
</margin>

---

Une bobine cylindrique possède une *inductance* $L$, qui se calcule selon la formule suivante :


$L = \frac{\mu_0 \cdot \mu_r \cdot N^2 \cdot A_S}{l}$


En examinant la structure d'une bobine, on identifie donc les grandeurs suivantes :
1. $\mu_0$ est la *perméabilité du vide*, une constante naturelle dont la valeur est $\qty{1,2566e-6}{\henry\per\meter}$. Cette valeur peut toujours être consultée dans le recueil de formules.
2. $\mu_r$ est une constante de matériau, car le noyau de la bobine peut être constitué d'un matériau spécial qui peut amplifier les champs magnétiques.
3. Le nombre $N$ de *spires de bobine* en fil de cuivre émaillé ou en fil de cuivre argenté.
4. $A_S$ représente la surface de la section transversale du noyau de la bobine.
5. La longueur $l$ de la bobine.

[question:EA102]


<indepth>
La lettre $L$ a été choisie en l'honneur du professeur Emil Lenz (1804–1864) de Saint-Pétersbourg, qui a formulé la règle de Lenz qui porte son nom.
</indepth>


<unit>
Une bobine possède une inductance $L$ avec pour unité $\qty{1}{\volt\second\per\ampere}$, généralement exprimée en *henry* ($\unit{\henry}$). Cette unité porte le nom du physicien américain *Joseph Henry* (1797–1878). Une inductance de $\qty{1}{\henry}$ existe lorsque la variation d'un courant de $\qty{1}{\ampere}$ en une seconde produit une tension d'auto-induction de $\qty{1}{\volt}$. En pratique, les valeurs d'inductance sont généralement bien inférieures et sont typiquement exprimées en $\unit{\milli\henry}$, $\unit{\micro\henry}$ ou $\unit{\nano\henry}$.
</unit>

---

À l'aide de cette formule et des relations qualitatives suivantes, on peut déjà résoudre un certain nombre de questions d'examen :


1. L'inductance augmente de manière quadratique avec le nombre de spires. Si le nombre de spires est doublé, l'inductance quadruple.
2. Si la bobine est comprimée, l'inductance $L$ augmente.
3. Si la surface de la section transversale est agrandie, l'inductance $L$ augmente.
4. Si le champ magnétique dans la bobine est amplifié par un matériau approprié à conduction magnétique (par exemple, le fer), l'inductance $L$ augmente.

[question:EC305]


Si l'on comprime la bobine, $l$ diminue. Par conséquent, l'inductance $L$ augmente.


[question:EC306]


Si la longueur $l$ de la bobine est doublée, l'inductance $L$ doit être divisée par deux.


[question:EC307]


Si le nombre de spires $N$ est doublé, l'inductance $L$ est multipliée par quatre.


Si le nombre de spires est réduit, l'inductance diminue, mais même avec une demi-spire ou un quart de spire, et même avec un simple fil droit, une faible inductance parasite subsiste.


[question:EC304]


---

On qualifie de *ferromagnétique* une certaine classe de matériaux qui, à l'échelle atomique, contiennent de petits aimants élémentaires s'alignant sous l'influence d'un champ magnétique externe et augmentant ainsi fortement la *densité de flux magnétique* (que nous n'aborderons pas ici). Parmi les éléments chimiques purs, seuls le fer, le cobalt et le nickel sont ferromagnétiques.


<indepth>
$\mu_r$, aussi appelée *perméabilité relative*, est très élevée pour les matériaux ferromagnétiques (par exemple, pour le fer, elle se situe dans la plage de $300\dots\num{10000}$).
</indepth>


[question:EB204]


Si l'on introduit un matériau ferromagnétique comme le fer dans la bobine, le champ magnétique est amplifié et l'inductance augmente. 


Si l'on introduit dans une bobine cylindrique un noyau en un métal conducteur (non ferromagnétique) comme l'*aluminium* ou le *cuivre*, l'inductance de la bobine diminue au contraire. Cela est dû au fait que le champ magnétique à haute fréquence de la bobine induit des courants, appelés courants de Foucault, dans les noyaux. Ces courants secondaires génèrent à leur tour des champs magnétiques qui s'opposent au champ magnétique de la bobine. C'est pourquoi l'inductance diminue. Le champ magnétique à l'intérieur du noyau est alors réduit.


Dans la question suivante, la réponse considérée comme correcte est que le champ magnétique ne peut pas pénétrer dans le noyau, réduisant ainsi la section du champ. Cependant, ce n'est pas exactement ce qui se passe physiquement. Il suffit simplement de retenir la "bonne" réponse.


[question:EB205]


---

Examinons d'abord, comme pour le condensateur, le comportement en courant continu de la bobine : la bobine est connectée à une source de *tension continue* via une *résistance en série*, comme illustré dans la figure [ref:e_spule_einschalten]. Au moment de la mise sous tension, l'augmentation du courant est d'abord retardée, de sorte que le courant n'augmente pas de manière abrupte, mais progressivement jusqu'à sa valeur maximale.


La cause en est la règle de Lenz : lors de l'augmentation du courant, la bobine génère une tension d'auto-induction qui s'oppose à la variation du courant – et donc à sa cause. Cela limite l'augmentation du courant. Comme aucun courant ne circule initialement, presque toute la tension appliquée chute d'abord aux bornes de la bobine. Au fur et à mesure que le courant augmente, cette tension d'induction diminue, tandis que le courant continue d'augmenter.


Une fois l'état stationnaire atteint, la bobine se comporte approximativement comme un simple fil sous courant continu. La tension à ses bornes est alors pratiquement nulle. L'évolution temporelle de la tension aux bornes de la bobine est illustrée dans la figure [ref:e_spule_einschalten_spannung].


<margin>
[picture:1016:e_spule_einschalten:Circuit électrique pour l'étude d'une bobine]
</margin>
<margin>
[picture:186:e_spule_einschalten_spannung:Évolution de la tension lors de la mise sous tension]
</margin>

[question:EC301]


---

Au moment de la coupure, la tension d'auto-induction cherche à maintenir le flux de courant. La bobine se comporte alors comme un générateur dont la tension d'induction apparaît avec une polarité opposée à celle précédente. La bobine se comporte donc exactement à l'inverse du condensateur. Ces phénomènes peuvent être bien observés à l'aide d'un oscilloscope, comme illustré dans la figure [ref:e_Spulenstrom].


<margin>
[photo:257:e_Spulenstrom:Comportement à la mise sous tension et à la coupure de la tension et du courant de la bobine]
</margin>

C'est pourquoi les bobines peuvent également être utilisées pour introduire un *retard*. Dans la question suivante, le courant à travers la lampe 2 augmente plus lentement que celui à travers la lampe 1, car une bobine est connectée en série, dont la tension d'auto-induction ne permet qu'une augmentation lente du courant de mise sous tension.


[question:EC302]


Tout comme le condensateur, une bobine se comporte différemment selon qu'elle est connectée à une *tension continue* ou à une *tension alternative*. En radioélectricité, c'est surtout le comportement en tension alternative qui est important. C'est pourquoi nous examinons maintenant le comportement en courant alternatif.


La bobine présente, tout comme le condensateur, une *impédance* $X_{\textrm{L}}$ : bien que le fil de la bobine ne possède qu'une très faible résistance ohmique (résistance du conducteur), un courant circule, mais il diminue avec l'augmentation de la *fréquence* de la *tension alternative* :


$X_{L} = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$


D'après la formule, on peut voir que l'*impédance* augmente avec la fréquence croissante et diminue avec la fréquence décroissante.


[question:EC303]