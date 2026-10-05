Dans le chapitre sur les circuits de base, nous avons déjà découvert différents amplificateurs à transistor. Dans l'émetteur, nous examinons maintenant en particulier les *amplificateurs de puissance*. Ils amplifient le signal HF généré dans les étapes précédentes jusqu'à la puissance de sortie souhaitée de l'émetteur.

Pour les amplificateurs de puissance HF, on peut fondamentalement distinguer deux types de conception :

1. Les *amplificateurs HF large bande* présentent un gain aussi uniforme que possible sur une bande de fréquences relativement large, par exemple sur une grande partie de la gamme des ondes courtes de $\qtyrange{1}{30}{\mega\hertz}$, cf. figure [ref:a_breitbandverstärker].
2. Les *amplificateurs HF sélectifs* sont, en revanche, accordés sur une bande de fréquences comparativement étroite, par exemple sur une seule bande radioamateur, cf. figure [ref:a_selektiver_verstaerker].

Les amplificateurs HF large bande sont souvent reconnaissables par les transformateurs de couplage large bande entre les différents étages amplificateurs. Ceux-ci, avec les condensateurs, ne forment pas de circuits oscillants accordés sur une fréquence spécifique. Le principe déjà connu de l'amplificateur push-pull se retrouve également dans de nombreux amplificateurs de puissance HF.

<margin>
[picture:491:a_breitbandverstärker:Amplificateur de puissance HF large bande avec montage push-pull]
</margin>

[question:AF412]

Les amplificateurs HF sélectifs sont quant à eux typiquement reconnaissables à leur conception sélective en fréquence, caractérisée par des circuits oscillants en série ou en parallèle dans le trajet du signal HF.

<margin>
[picture:778:a_selektiver_verstaerker:Amplificateur de puissance HF sélectif avec conception sélective en fréquence]
</margin>

[question:AF408]

---

Les amplificateurs des types mentionnés ci-dessus peuvent également être réalisés en plusieurs étages par la mise en cascade d'étages individuels.

[question:AF413]

Entre les étages amplificateurs d'un amplificateur de puissance et leurs entrées et sorties, il est nécessaire de réaliser une adaptation d'impédance. Ceci est nécessaire pour que l'impédance de sortie HF d'une étape précédente soit adaptée au mieux à l'impédance d'entrée HF de l'étape suivante pour un gain maximal, des distorsions minimales et un rendement optimal (évitement des réflexions et des non-linéarités).

L'adaptation d'impédance peut être réalisée soit en large bande par l'utilisation d'un transformateur avec un rapport de transformation approprié, soit de manière sélective en fréquence par un circuit oscillant à prise intermédiaire.

Pour l'adaptation sélective en fréquence, il existe deux possibilités fondamentales de la réaliser :
- par un diviseur de tension inductif (bobine avec prise intermédiaire et condensateur en parallèle)
- par un diviseur de tension capacitif (deux condensateurs en série avec une bobine en parallèle)

Ces bobines et condensateurs peuvent être disposés dans différentes configurations (circuit parallèle ou série) pour obtenir la transformation d'impédance souhaitée et éventuellement supprimer simultanément les harmoniques (filtre Pi).

[question:AF409]
[question:AF410]
[question:AF414]
[question:AF407]
[question:AF406]

---

La figure [ref:a_fet_verstaerker] montre un amplificateur ondes courtes avec des transistors à effet de champ LDMOS. LDMOS signifie *Laterally Diffused Metal-Oxide-Semiconductor* et désigne un transistor à effet de champ spécial pour les amplificateurs de puissance HF. Le circuit amplificateur proprement dit (partie supérieure) est très simple. C'est à nouveau un amplificateur push-pull avec deux FET qui fonctionnent en configuration push-pull. Les deux transistors sont commandés par un transformateur d'entrée commun. La sortie de l'amplificateur est prélevée par un autre transformateur. La partie inférieure du circuit est également moins complexe qu'on ne le pense : En gros, il s'agit simplement de générer la tension de polarisation (BIAS) pour les transistors via un diviseur de tension.

Il ne faut pas se laisser tromper par la propriété connue d'un transistor à effet de champ : En tension continue, la grille est pratiquement sans courant et possède donc une impédance d'entrée très élevée. Cependant, à haute fréquence, les capacités parasites du transistor jouent un rôle important, en particulier les capacités entre la grille et la source ainsi qu'entre la grille et le drain. Leur réactance capacitive diminue avec l'augmentation de la fréquence, de sorte qu'un courant HF peut circuler dans la grille. Pour les transistors de puissance HF, l'impédance d'entrée peut donc être nettement plus faible que ce à quoi on s'attendrait de l'analyse en courant continu d'un FET. Le transformateur d'entrée $T_1$ sert donc à adapter les $\qty{50}{\ohm}$ à l'impédance d'entrée faible des transistors.

<margin>
[picture:786:a_fet_verstaerker:Amplificateur ondes courtes avec transistors à effet de champ]
</margin>

[question:AF417]

---

Comme indiqué ci-dessus, les éléments actifs d'un amplificateur de puissance nécessitent, outre la tension de service requise, un réglage du point de fonctionnement en tension continue (BIAS). Ce point de fonctionnement est généralement généré par des diviseurs de tension qui, à partir d'une tension auxiliaire stabilisée, en utilisant des potentiomètres de réglage pour un réglage optimal, produisent la tension de polarisation souhaitée sur les éléments.

<tip>
Lors de l'examen de la tension de polarisation et de ses effets sur les éléments du circuit, le circuit ne doit être considéré qu'en tension continue. Ici, les condensateurs, en tant qu'éléments ne pouvant transmettre que des tensions alternatives, sont ignorés. Les enroulements des transformateurs ainsi que les bobines sont considérés comme des courts-circuits dans l'analyse en tension continue. En principe, pour ces exercices, il suffit d'appliquer les connaissances de base des sections [sec:ohmsches_gesetz] Loi d'Ohm, [sec:spannungsteiler_1] et [sec:spannungsteiler_2] !
</tip>

[question:AF420]

---

Le calcul de la tension de polarisation pour un circuit donné dans la question suivante s'effectue en appliquant la loi d'Ohm en tenant compte des montages en parallèle et en série des résistances. Il est important, lors de l'examen de la question, de noter que les connexions de grille des transistors représentent des capacités et sont donc négligeables dans l'analyse en tension continue.

[question:AF421]

<indepth>
La résistance $R_5=\qty{51}{\ohm}$ n'influence pratiquement pas la tension continue sur la grille, car pratiquement aucun courant continu ne circule dans la grille du transistor LDMOS. Cependant, pour le signal HF, $R_5$ est important : Avec la capacité de grille, il amortit d'éventuelles oscillations haute fréquence et améliore ainsi la stabilité de l'amplificateur.

La résistance $R_4=\qty{6,8}{\kilo\ohm}$ assure que la grille ait un potentiel défini par rapport à la masse même en cas d'interruption du réglage du point de fonctionnement. Elle décharge également la capacité de grille et empêche ainsi le transistor de devenir conducteur involontairement à cause d'une grille flottante, par exemple si le potentiomètre $R_3$ est défectueux. Comme $R_4$ est en parallèle avec la branche inférieure du diviseur de tension, il doit être pris en compte dans le calcul précis de la tension de grille.
</indepth>

---

Le circuit de la figure [ref:a_fet_verstaerker_vhf] montre un amplificateur de puissance VHF avec des transistors à effet de champ. Ici aussi, les deux transistors fonctionnent comme un étage final push-pull, ce qui est la partie simple du circuit. Les courts câbles coaxiaux servent de partie du réseau d'adaptation pour transformer la faible impédance des transistors LDMOS en une impédance adaptée au reste du circuit. Le reste du circuit est à nouveau la génération de la tension de polarisation pour les transistors, y compris une compensation de température. Les potentiomètres $R_1$ et $R_2$ forment chacun un diviseur de tension qui règle la tension de polarisation pour le transistor respectif.

[question:AF424]
[question:AF423]

<margin>
[picture:783:a_fet_verstaerker_vhf:Amplificateur VHF avec transistors à effet de champ]
</margin>


---

Un filtre Pi (cf. figure [ref:a_pi_filter]) peut adapter les impédances à son entrée et sa sortie par le rapport des deux capacités. La bobine du filtre Pi définit, avec les deux capacités, la fréquence de conception du filtre. Le filtre Pi supprime simultanément, par son caractère passe-bas, les harmoniques indésirables du signal d'émission.

<margin>
[picture:1100:a_pi_filter:Filtre Pi]
</margin>

[question:AF405]

Un circuit LC derrière un amplificateur de puissance HF a une fonction similaire. Il sert également à l'adaptation d'impédance et à la suppression simultanée des harmoniques.

[question:AF404]

Pour les amplificateurs de puissance, il est important de découpler au mieux les différentes étages HF de la tension de service pour éviter des rétroactions sur d'autres étages (tendance à l'oscillation, effets de modulation, etc.). Pour cela, les alimentations en tension de service des différentes étages sont découplées les unes des autres par des inductances montées en série et des condensateurs de découplage vers la masse. Cet agencement constitue un passe-bas, car idéalement, seule la tension de service continue souhaitée est transmise, tandis que les composantes HF sont bloquées.

[question:AF411]
[question:AF419]
[question:AF418]
[question:AF422]

Les propriétés HF des condensateurs réels dépendent de la fréquence. Les grandes capacités comme les condensateurs électrolytiques ne peuvent être utilisées qu'à basse fréquence et ne sont que partiellement efficaces dans la gamme HF. Pour découpler également les fréquences plus élevées avec des condensateurs, on utilise souvent une combinaison de différents types de condensateurs et de valeurs de capacité, qui ensemble peuvent découpler une plus large bande de fréquences.

[question:AF415]
