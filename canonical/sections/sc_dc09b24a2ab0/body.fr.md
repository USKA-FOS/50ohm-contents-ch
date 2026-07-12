Dans la classe E, nous avons déjà appris à connaître les sources de tension. Tout d'abord, nous voulons nous occuper de la source de courant, avant d'examiner plus en détail la résistance interne des sources de tension et de courant.

De même que pour la source de tension, une source de courant veille à ce qu'elle fournisse un courant aussi constant que possible. La figure [ref:a_vsource_schematic] montre son schéma équivalent.

<margin>
[picture:1058:a_vsource_schematic:Schéma équivalent de la source de courant $R_i$ haute impédance]
</margin>

<indepth>
Examen d'une source de courant constant à l'exemple d'un appareil de laboratoire:

[photo:298:a_Strombegrenzung:Appareil de laboratoire avec une limitation de courant réglée à $\qty{500}{\milli\ampere}$]

Dans les appareils de laboratoire, une limitation de courant est intégrée, c'est-à-dire que si le courant de charge dépasse une intensité de courant maximale, la tension aux bornes est réduite de telle sorte que le courant de charge reste constant. Cela correspond à la fonction d'une source de courant constant -- En cas de court-circuit aux bornes de sortie, le courant maximal réglé circule.
</indepth>

Une source de courant constant idéale fournit un courant continu constant, indépendamment de la charge connectée. En théorie, cela est possible avec une résistance interne infinie. En pratique, les sources de courant ont une résistance interne très élevée.

<margin>
[picture:1018:a_vsource_schematic:Schéma équivalent de la source de tension]
</margin>

---

La figure [ref:a_vsource_schematic] montre un schéma équivalent d'une source de tension. La résistance interne $R_i$ est en série avec la source de tension idéale et devrait, dans l'idéal, être de $\qty{0}{\ohm}$. En pratique, les sources de tension ont une faible résistance interne.

[question:AB201]

Lorsqu'une source de tension réelle est chargée avec $R_L$, la tension aux bornes $U_k$ diminue. La raison en est la résistance interne $R_i$ de cette source de tension. Celle-ci crée un diviseur de tension. Comme la tension de la source $U_q$ est, en l'absence de charge, donc sans charge $U_q=U_L$, on l'appelle aussi tension à circuit ouvert.

Avec un multimètre, la résistance interne n'est pas mesurable, mais on peut la déterminer par le calcul selon la loi d'Ohm (voir recueil de formules):

$R_i = \frac{\Delta U}{\Delta I}$

Pour le calcul, deux cas de charge sont nécessaires:
1. Circuit ouvert sans charge: $I = \qty{0}{\ampere}$ et $U_L = U_q$
2. Charge avec $R_L$: Nous mesurons $I_L$ et $U_L$

À partir de la variation de tension ($\Delta U = U_q~-~U_L$) aux bornes et de la variation de courant de charge ($\Delta I = I_L~-~\qty{0}{\ampere}$), la résistance interne peut être calculée selon la formule ci-dessus.

$R_i = \frac{\Delta U}{\Delta I} = \frac{U_q - U_L}{I_L-\qty{0}{\ampere}} = \frac{U_q - U_L}{I_L}$

Avec cette connaissance, nous pouvons répondre aux questions d'examen suivantes:

[question:AB205]
[question:AB206]
[question:AB207]
[question:AB208]

Nous résumons:

* Les sources de tension doivent présenter une résistance interne très faible $R_i \ll R_L$, dans l'idéal: $\qty{0}{\ohm}$, alors la tension de sortie reste inchangée en cas de charge. Si la tension aux bornes reste constante en cas de charge, on parle d'adaptation de tension.
* Les sources de courant doivent présenter une résistance interne très élevée $R_i \gg R_L$. Cas idéal: $\qty{\infty}{\ohm}$, alors le courant de charge reste constant en cas de modification de la résistance de charge, c'est pourquoi on parle également d'adaptation de courant.

[question:AB203]
[question:AB204]

---

Si une source de tension doit fournir la puissance maximale à une charge, on parle d'adaptation de puissance. Cela est également important, par exemple, pour un émetteur qui doit transmettre autant de puissance que possible à une antenne.

La transmission de puissance maximale est obtenue lorsque

$R_i = R_L$

git, c'est-à-dire lorsque la résistance interne et la résistance de charge sont égales.

Dans ce cas, la tension de la source se répartit uniformément sur la résistance interne et la charge. Cela donne ainsi à la charge le produit maximal de tension et de courant et donc la puissance maximale possible.

La figure [ref:a_Leistungsanpassung] montre la puissance normalisée à la charge en fonction du rapport $R_L/R_i$. Le maximum est atteint exactement lorsque $R_L/R_i = 1$, c'est-à-dire lorsque la résistance interne et la résistance de charge sont égales. Cependant, le rendement lors de l'adaptation de puissance n'est que de $\qty{50}{\percent}$, car la même puissance est dissipée à la fois à la charge et à la résistance interne.

<margin>
[picture:1077:a_Leistungsanpassung:Adaptation de puissance optimale lorsque $R_i = R_L$, ici le quotient $\frac{R_L}{R_i}=1$ et donc la puissance maximale est fournie à la charge. Le graphique est logarithmique.]
[picture:937:a_Leistungsanpassung:Puissance de sortie optimale pour une résistance de charge de $\qty{50}{\ohm}$ avec une résistance interne de $\qty{50}{\ohm}$. Le graphique n'est pas logarithmique.]
</margin>

<indepth>
Les sources de tension alternative, par exemple les générateurs de sinus, possèdent également une résistance interne, qui est indiquée sur la prise de sortie.
[photo:292:Sinusgenerator 50 Ohm:Générateur de sinus avec une résistance interne de 50 ohms]
</indepth>

% GGF doit être déplacé ailleurs ? 
<indepth>
La valeur fréquemment utilisée dans la technique des hautes fréquences de $\qty{50}{\ohm}$ est un compromis technique entre la transmission de puissance maximale et les pertes minimales dans les lignes.

Les lignes coaxiales avec une impédance de ligne d'environ $\qty{30}{\ohm}$ peuvent transmettre des puissances particulièrement élevées, car le courant dans le câble est moins réparti. Les câbles d'environ $\qty{77}{\ohm}$ possèdent en revanche les pertes d'atténuation les plus faibles et conviennent particulièrement bien à une transmission de signal à faible perte.

La valeur aujourd'hui largement répandue de $\qty{50}{\ohm}$ se situe entre les deux optima et représente un bon compromis entre une transmission de puissance élevée, des pertes modérées et une construction de câble pratique. C'est pourquoi $\qty{50}{\ohm}$ se sont imposés comme standard dans la technique radio.

Lorsque l'émetteur, le câble et l'antenne sont chacun adaptés à $\qty{50}{\ohm}$, la puissance est transmise de manière optimale et les réflexions sur la ligne sont minimisées.

[picture:1078:a_50ohm:50 ohms comme compromis entre la transmission de puissance maximale et les pertes minimales dans la technique des hautes fréquences]

Maintenant, tu sais aussi pourquoi notre plateforme s'appelle 50ohm.de : Nous voulons t'aider à maîtriser les questions d'examen et ainsi atteindre la performance optimale à l'examen 🤓
</indepth>

[question:AG401]
[question:AB202]