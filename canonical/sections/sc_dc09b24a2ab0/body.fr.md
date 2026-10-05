Dans la section [sec:spannungsquelle], nous avons déjà fait connaissance avec les sources de tension. Nous allons d'abord nous intéresser à la source de courant, avant d'examiner plus en détail la résistance interne des sources de tension et de courant.

Tout comme pour la source de tension, une source de courant vise à fournir un courant aussi constant que possible. La figure [ref:a_isource_schematic] montre son schéma équivalent.

<margin>
[picture:1058:a_isource_schematic:Schéma équivalent d'une source de courant $R_i$ haute impédance]
</margin>

<indepth>
Examen d'une source de courant constant à l'exemple d'une alimentation de laboratoire :

[photo:298:a_Strombegrenzung:Alimentation de laboratoire avec limitation de courant réglée sur $\qty{500}{\milli\ampere}$]

Les alimentations de laboratoire sont équipées d'une limitation de courant, c'est-à-dire que si le courant de charge dépasse une intensité de courant maximale, la tension aux bornes est réduite de manière à maintenir le courant de charge constant. Cela correspond à la fonction d'une source de courant constant -- En cas de court-circuit aux bornes de sortie, le courant maximal réglé circule.
</indepth>

Une source de courant constant idéale fournit un courant continu constant, indépendamment de la charge connectée. En théorie, cela est possible avec une résistance interne infinie. En pratique, les sources de courant ont une résistance interne très élevée.

<margin>
[picture:1018:a_vsource_schematic:Schéma équivalent d'une source de tension]
</margin>

---

La figure [ref:a_vsource_schematic] montre un schéma équivalent d'une source de tension. La résistance interne $R_i$ est en série avec la source de tension idéale et devrait idéalement être de $\qty{0}{\ohm}$. En pratique, les sources de tension ont une faible résistance interne.

[question:AB201]

Lorsqu'une source de tension réelle est chargée avec $R_L$, la tension aux bornes $U_k$ diminue. La raison en est la résistance interne $R_i$ présente dans cette source de tension. Celle-ci forme en quelque sorte un diviseur de tension. Comme la tension de source $U_q$ à vide, c'est-à-dire sans charge, est $U_q=U_L$, on l'appelle également tension à circuit ouvert.

La résistance interne n'est pas mesurable avec un multimètre, mais on peut la déterminer par calcul via la loi d'Ohm (cf. recueil de formules) :

$R_i = \frac{\Delta U}{\Delta I}$

Pour le calcul, deux cas de charge sont nécessaires :
1. Circuit ouvert sans charge : $I = \qty{0}{\ampere}$ et $U_L = U_q$
2. Charge avec $R_L$ : Nous mesurons $I_L$ et $U_L$

À partir de la variation de tension ($\Delta U = U_q~-~U_L$) aux bornes et de la variation du courant de charge ($\Delta I = I_L~-~\qty{0}{\ampere}$), la résistance interne peut être calculée selon la formule ci-dessus.

$R_i = \frac{\Delta U}{\Delta I} = \frac{U_q - U_L}{I_L-\qty{0}{\ampere}} = \frac{U_q - U_L}{I_L}$

Avec ces connaissances, nous pouvons répondre aux questions d'examen suivantes :

[question:AB205]
[question:AB206]
[question:AB207]
[question:AB208]

Résumons :

* Les sources de tension doivent présenter une résistance interne très faible $R_i \ll R_L$, idéalement : $\qty{0}{\ohm}$, alors la tension de sortie reste inchangée sous charge. Si la tension aux bornes reste constante sous charge, on parle d'adaptation en tension.
* Les sources de courant doivent présenter une résistance interne très élevée $R_i \gg R_L$. Cas idéal : $\qty{\infty}{\ohm}$, alors le courant de charge reste constant lors d'un changement de la résistance de charge, c'est pourquoi on parle aussi d'adaptation en courant.

[question:AB203]
[question:AB204]

---

Lorsqu'une source de tension doit délivrer la puissance maximale à une charge, on parle d'adaptation en puissance. C'est par exemple également important pour un émetteur qui doit transmettre le plus de puissance possible à une antenne.

Le transfert de puissance maximal est atteint lorsque

$R_i = R_L$

est vérifié, c'est-à-dire lorsque la résistance interne et la résistance de charge sont égales.

Dans ce cas, la tension de source se répartit également entre la résistance interne et la charge. Il en résulte sur la charge le produit maximal de tension et de courant et donc la puissance la plus élevée possible.

La figure [ref:a_Leistungsanpassung] montre la puissance normalisée sur la charge en fonction du rapport $R_L/R_i$. Le maximum est atteint exactement à $R_L/R_i = 1$, c'est-à-dire lorsque la résistance interne et la résistance de charge sont égales. Cependant, le rendement lors de l'adaptation en puissance n'est que de $\qty{50}{\percent}$, car la même puissance est dissipée à la fois sur la charge et sur la résistance interne.

<margin>
[picture:1077:a_Leistungsanpassung:Adaptation de puissance optimale à $R_i = R_L$, ici le quotient $\frac{R_L}{R_i}=1$ et donc la puissance maximale est émise sur la charge. Le graphique est logarithmique.]
[picture:937:a_Leistungsanpassung:Puissance de sortie optimale à $\qty{50}{\ohm}$ de résistance de charge pour une résistance interne de $\qty{50}{\ohm}$. Le graphique n'est pas logarithmique.]
</margin>

<indepth>
Les sources de tension alternative, par exemple les générateurs sinusoïdaux, possèdent également une résistance interne, indiquée sur la prise de sortie.
[photo:292:Sinusgenerator 50 Ohm:Générateur sinusoïdal avec 50 ohm de résistance interne]
</indepth>

% À déplacer éventuellement ailleurs ?
<indepth>
La valeur couramment utilisée en haute fréquence de $\qty{50}{\ohm}$ est un compromis technique entre le transfert de puissance maximal et des pertes aussi faibles que possible dans les câbles.

Les câbles coaxiaux avec une impédance caractéristique d'environ $\qty{30}{\ohm}$ peuvent transmettre des puissances particulièrement élevées, car le courant dans le câble est réparti sur une intensité moindre. En revanche, les câbles d'environ $\qty{77}{\ohm}$ présentent les pertes par atténuation les plus faibles et sont particulièrement adaptés à une transmission de signal à faible perte.

La valeur aujourd'hui très répandue de $\qty{50}{\ohm}$ se situe entre ces deux optimums et représente un bon compromis entre un transfert de puissance élevé, des pertes modérées et une construction de câble pratique. C'est pourquoi les $\qty{50}{\ohm}$ se sont établis comme standard en technique radio.

Si un émetteur, un câble et une antenne sont chacun adaptés à $\qty{50}{\ohm}$, alors la puissance est transférée de manière optimale et les réflexions sur la ligne sont minimisées.

[picture:1078:a_50ohm:50 ohm comme compromis entre transfert de puissance maximal et pertes minimales en haute fréquence]

Maintenant tu sais aussi pourquoi notre plateforme s'appelle 50ohm.de : Nous voulons t'aider à maîtriser les questions d'examen et ainsi atteindre la puissance optimale lors de l'examen 🤓
</indepth>

[question:AG401]
[question:AB202]
