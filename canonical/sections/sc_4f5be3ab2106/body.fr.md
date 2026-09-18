Dans le chapitre consacré aux circuits de base, nous avons déjà étudié divers amplificateurs à transistor. Dans l’émetteur, nous nous intéressons maintenant plus particulièrement aux *amplificateurs de puissance*. Ils amplifient le signal HF généré dans les étages précédents jusqu’à la puissance de sortie souhaitée de l’émetteur.

Pour les amplificateurs de puissance HF, on distingue généralement deux types d’exécution :

1. Les *amplificateurs HF large bande* offrent une amplification aussi uniforme que possible sur une large bande de fréquences, par exemple sur une grande partie de la bande HF de $\qtyrange{1}{30}{\mega\hertz}$, voir figure [ref:a_breitbandverstärker].
2. Les *amplificateurs HF sélectifs* sont en revanche accordés sur une bande de fréquences relativement étroite, par exemple sur une seule bande radioamateur, voir figure [ref:a_selektiver_verstaerker].

Les amplificateurs HF large bande se reconnaissent souvent à leurs transformateurs de couplage large bande entre les différents étages amplificateurs. Ceux-ci, associés à des condensateurs, ne forment pas de circuits oscillants accordés sur une fréquence déterminée. Le principe bien connu de l’amplificateur push-pull se retrouve également dans de nombreux amplificateurs de puissance HF.

<margin>
[picture:491:a_breitbandverstärker:Amplificateur de puissance HF large bande en montage push-pull]
</margin>

[question:AF412]

Les amplificateurs HF sélectifs se caractérisent quant à eux par leur conception sélective en fréquence, marquée par des circuits oscillants en série ou en parallèle dans le trajet du signal HF.

<margin>
[picture:778:a_selektiver_verstaerker:Amplificateur de puissance HF sélectif avec conception sélective en fréquence]
</margin>

[question:AF408]

---

Les amplificateurs des types mentionnés ci-dessus peuvent également être réalisés en plusieurs étages par enchaînement d’étages individuels.

[question:AF413]

Entre les étages amplificateurs d’un amplificateur de puissance et leurs entrées et sorties, il est nécessaire d’effectuer une adaptation d’impédance. Cela est indispensable pour adapter au mieux l’impédance de sortie HF d’un étage précédent à l’impédance d’entrée HF de l’étage suivant, afin d’obtenir un gain maximal, des distorsions minimales et un rendement optimal (éviter les réflexions et les non-linéarités).

L’adaptation d’impédance peut être réalisée soit en large bande au moyen d’un transformateur avec un rapport de transformation adapté, soit de manière sélective en fréquence par un circuit oscillant à prise intermédiaire.

Pour l’adaptation sélective en fréquence, il existe deux possibilités fondamentales de la réaliser :
- par un diviseur de tension inductif (bobine avec prise intermédiaire et condensateur en parallèle)
- par un diviseur de tension capacitif (deux condensateurs en série avec une bobine en parallèle)

Ces bobines et condensateurs peuvent être disposés dans différentes configurations (circuit parallèle ou série) pour obtenir la transformation d’impédance souhaitée et, le cas échéant, supprimer simultanément les harmoniques (filtre en π).

[question:AF409]
[question:AF410]
[question:AF414]
[question:AF407]
[question:AF406]

---

La figure [ref:a_fet_verstaerker] montre un amplificateur HF pour la bande HF avec des transistors à effet de champ LDMOS. LDMOS signifie *Laterally Diffused Metal-Oxide-Semiconductor* et désigne un transistor à effet de champ spécialement conçu pour les amplificateurs de puissance HF. Le circuit amplificateur proprement dit (partie supérieure) est très simple : il s’agit à nouveau d’un amplificateur push-pull avec deux transistors FET fonctionnant en configuration push-pull. Les deux transistors sont commandés par un transformateur d’entrée commun. La sortie de l’amplificateur est prélevée via un autre transformateur. La partie inférieure du circuit est moins complexe qu’il n’y paraît : dans l’ensemble, elle sert uniquement à générer, via un diviseur de tension, la tension de polarisation (BIAS) pour les transistors.

Il ne faut pas se laisser tromper par la propriété connue d’un transistor à effet de champ : en tension continue, la grille est pratiquement sans courant et présente donc une impédance d’entrée très élevée. À haute fréquence, en revanche, les capacités parasites du transistor jouent un rôle important, notamment les capacités entre grille et source ainsi qu’entre grille et drain. Leur réactance capacitive diminue avec l’augmentation de la fréquence, de sorte qu’un courant HF peut circuler à la grille. Dans le cas des transistors de puissance HF, l’impédance d’entrée peut donc être nettement plus faible que ce que l’on pourrait attendre d’une analyse en courant continu d’un FET. Le transformateur d’entrée $T_1$ sert donc à adapter les $\qty{50}{\ohm}$ à l’impédance d’entrée basse de ces transistors.

<margin>
[picture:786:a_fet_verstaerker:Amplificateur HF pour la bande HF avec transistors à effet de champ]
</margin>

[question:AF417]

---

Comme mentionné plus haut, les éléments actifs d’un amplificateur de puissance nécessitent, en plus de la tension de service requise, un réglage en courant continu du point de fonctionnement (BIAS). Ce point de fonctionnement est généralement généré par des diviseurs de tension qui, à partir d’une tension auxiliaire stabilisée et à l’aide de potentiomètres de réglage pour un réglage optimal, produisent la tension de polarisation souhaitée sur les éléments.

<tip>
Lors de l’étude de la tension de polarisation et de ses effets sur les éléments du circuit, il convient de considérer le circuit uniquement en courant continu. Dans cette analyse, les condensateurs sont considérés comme des éléments ne transmettant que les tensions alternatives et sont donc ignorés. Les enroulements des transformateurs ainsi que les bobines sont considérés comme des courts-circuits en analyse en courant continu. En règle générale, il suffit pour ces tâches d’appliquer les connaissances de base des classes N et E concernant la loi d’Ohm et les diviseurs de tension !
</tip>

[question:AF420]

---

Le calcul de la tension de polarisation dans le circuit donné dans la question suivante se fait en appliquant la loi d’Ohm en tenant compte des montages en parallèle et en série de résistances. Il est important, lors de l’étude de la question, de considérer que les bornes de grille des transistors représentent des capacités et sont donc négligeables dans une analyse en courant continu.

[question:AF421]

<indepth>
La résistance $R_5=\qty{51}{\ohm}$ n’a pratiquement aucune influence sur la tension continue à la grille, car un courant continu quasi nul circule dans la grille du transistor LDMOS. Pour le signal HF, $R_5$ est cependant important : il atténue, avec la capacité de grille, d’éventuelles oscillations haute fréquence et améliore ainsi la stabilité de l’amplificateur.

La résistance $R_4=\qty{6,8}{\kilo\ohm}$ garantit que la grille possède un potentiel défini par rapport à la masse même en cas de rupture du réglage du point de fonctionnement. Elle décharge également la capacité de grille et empêche ainsi que le transistor ne devienne conducteur de manière involontaire en raison d’une grille flottante, par exemple si le potentiomètre $R_3$ est défectueux. Comme $R_4$ est en parallèle avec la branche inférieure du diviseur de tension, il doit être pris en compte pour le calcul précis de la tension de grille.
</indepth>

---

Le circuit de la figure [ref:a_fet_verstaerker_vhf] montre un amplificateur de puissance VHF avec des transistors à effet de champ. Ici aussi, les deux transistors fonctionnent en étage final push-pull, ce qui constitue la partie la plus simple du circuit. Les courtes lignes coaxiales servent de partie du réseau d’adaptation pour transformer la faible impédance des transistors LDMOS en une impédance adaptée au reste du circuit. Le reste du circuit sert à nouveau à générer la tension de polarisation pour les transistors, y compris une compensation en température. Les potentiomètres $R_1$ et $R_2$ forment chacun un diviseur de tension qui règle la tension de polarisation pour le transistor correspondant.

[question:AF424]
[question:AF423]

<margin>
[picture:783:a_fet_verstaerker_vhf:Amplificateur VHF avec transistors à effet de champ]
</margin>

---

Un filtre en π (voir figure [ref:a_pi_filter]) peut adapter les impédances à son entrée et à sa sortie par le rapport des deux condensateurs. La bobine du filtre en π définit, avec les deux condensateurs, la fréquence de conception du filtre. Le filtre en π supprime simultanément, grâce à son caractère de passe-bas, les harmoniques indésirables du signal d’émission.

<margin>
[picture:1100:a_pi_filter:Filtre en π]
</margin>

[question:AF405]

Une fonction similaire est assurée par un circuit LC placé après un amplificateur de puissance HF. Celui-ci sert également à l’adaptation d’impédance et à la suppression simultanée des harmoniques.

[question:AF404]

Dans les amplificateurs de puissance, il est important de découpler au mieux les différents étages du point de vue HF par rapport à la tension de service afin d’éviter les rétroactions sur les autres étages (tendance à l’oscillation, effets de modulation, etc.). Pour cela, les alimentations en tension de service des différents étages sont découplées les unes des autres par des inductances en série et des condensateurs de découplage vers la masse. Cette disposition constitue un passe-bas, car dans l’idéal, seule la tension de service continue souhaitée est transmise, tandis que les composantes HF sont bloquées.

[question:AF411]
[question:AF419]
[question:AF418]
[question:AF422]

Les propriétés HF des condensateurs réels dépendent de la fréquence. Les grandes capacités, comme les condensateurs électrolytiques, ne peuvent être utilisés qu’à basse fréquence et ne sont que partiellement efficaces dans la bande HF. Pour bloquer également les fréquences plus élevées, on utilise souvent une combinaison de différents types et valeurs de condensateurs qui, ensemble, peuvent bloquer une plus large bande de fréquences.

[question:AF415]