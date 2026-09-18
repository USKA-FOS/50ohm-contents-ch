Un amplificateur prélève sur son alimentation électrique une puissance en courant continu et en convertit une partie en puissance de sortie haute fréquence (cf. illustration [ref:a_wirkungsgrad_verstaerker]). Une autre partie est dissipée principalement sous forme de chaleur dans le transistor et d’autres composants. Le courant de repos y contribue particulièrement, car il circule même en l’absence de signal d’entrée, comme nous l’examinerons plus en détail dans le chapitre suivant.

<margin>
[picture:1120:a_wirkungsgrad_verstaerker:Flux de puissance d’un amplificateur avec puissance en courant continu fournie, puissance de sortie HF et puissance dissipée]
</margin>

Le *rendement* $\eta$ indique quelle proportion de la puissance en courant continu fournie est disponible sous forme de puissance HF utilisable à la sortie de l’amplificateur :

$\eta = \frac{P_\mathrm{HF}}{P_\mathrm{DC}}$

Ici, $P_\mathrm{HF}$ est la puissance de sortie haute fréquence et $P_\mathrm{DC}$ la puissance en courant continu absorbée par l’alimentation électrique. Cette dernière peut être calculée à partir de la tension d’alimentation et du courant consommé :

$P_\mathrm{DC} = U_\mathrm{B} \cdot I_\mathrm{B}$

Le rendement est un rapport sans unité et peut atteindre au maximum la valeur $\num{1}$. Il est généralement exprimé en pourcentage :

$\eta_\mathrm{\%} = \eta \cdot \qty{100}{\percent}$

Le rendement d’un amplificateur de puissance HF est donc défini par le rapport entre la puissance HF de sortie fournie par l’amplificateur et la puissance en courant continu fournie par l’alimentation.

[question:AF401]

Un rendement élevé signifie qu’une faible partie de la puissance absorbée est perdue sous forme de chaleur. Avec un rendement faible, il faut évacuer une puissance dissipée plus importante à l’aide de dissipateurs thermiques ou d’autres mesures.

<tip>
Dans les questions d’examen suivantes, le rendement est considéré comme le rapport entre la puissance HF de sortie et la puissance en courant continu absorbée. Une éventuelle puissance HF d’entrée indiquée en plus n’est pas prise en compte dans ce calcul simplifié.
</tip>

[question:AD430]
[question:AD429]