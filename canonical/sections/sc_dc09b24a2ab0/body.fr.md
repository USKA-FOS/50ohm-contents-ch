Dans la classe E, nous avons déjà appris à connaître les sources de tension. Avant d'examiner de plus près la source de courant et la résistance interne des sources de tension et de courant, intéressons-nous d'abord à la source de courant.

Tout comme la source de tension, une source de courant a pour fonction de fournir un courant aussi constant que possible. La figure [ref:a_isource_schematic] montre son schéma équivalent.

<margin>
[picture:1058:a_isource_schematic:Schéma équivalent de la source de courant $R_i$ haute impédance]
</margin>

<indepth>
Examen d'une source de courant constant à l'exemple d'un alimentation de laboratoire :

[photo:298:a_Strombegrenzung:Alimentation de laboratoire avec limitation de courant réglée à $\qty{500}{\milli\ampere}$]

Les alimentations de laboratoire sont équipées d'une limitation de courant, c'est-à-dire que si le courant de charge dépasse une intensité maximale, la tension aux bornes est réduite de manière à ce que le courant de charge reste constant. Cela correspond au fonctionnement d'une source de courant constant : en cas de court-circuit aux bornes de sortie, le courant maximal réglé circule.
</indepth>

Une source de courant constant idéale fournit un courant constant en continu, indépendamment de la charge connectée. En théorie, cela est possible avec une résistance interne infinie. En pratique, les sources de courant ont une résistance interne très élevée.

<margin>
[picture:1018:a_vsource_schematic:Schéma équivalent de la source de tension]
</margin>

---

La figure [ref:a_vsource_schematic] montre un schéma équivalent d'une source de tension. La résistance interne $R_i$ est en série avec la source de tension idéale et devrait idéalement être de $\qty{0}{\ohm}$. En pratique, les sources de tension ont une faible résistance interne.

[question:AB201]

Si une source de tension réelle est chargée par $R_L$, la tension aux bornes $U_k$ diminue. La raison en est la résistance interne $R_i$ de cette source de tension. Elle forme en quelque sorte un diviseur de tension. Comme la tension de la source $U_q$ en circuit ouvert, c'est-à-dire sans charge, est $U_q=U_L$, on l'appelle aussi tension à circuit ouvert.

Il n'est pas possible de mesurer la résistance interne avec un multimètre, mais on peut la calculer à l'aide de la loi d'Ohm (voir recueil de formules) :

$R_i = \frac{\Delta U}{\Delta I}$

Pour le calcul, deux cas de charge sont nécessaires :
1. Circuit ouvert sans charge : $I = \qty{0}{\ampere}$ et $U_L = U_q$
2. Charge avec $R_L$ : on mesure $I_L$ et $U_L$

À partir de la variation de tension ($\Delta U = U_q~-~U_L$) aux bornes et de la variation du courant de charge ($\Delta I = I_L~-~\qty{0}{\ampere}$), on peut calculer la résistance interne à l'aide de la formule ci-dessus.

$R_i = \frac{\Delta U}{\Delta I} = \frac{U_q - U_L}{I_L-\qty{0}{\ampere}} = \frac{U_q - U_L}{I_L}$

Avec ces connaissances, nous pouvons répondre aux questions d'examen suivantes :

[question:AB205]
[question:AB206]
[question:AB207]
[question:AB208]

Faisons le point :

* Les sources de tension doivent présenter une résistance interne très faible $R_i \ll R_L$, idéalement $\qty{0}{\ohm}$, afin que la tension de sortie reste inchangée en cas de charge. Si la tension aux bornes reste constante en cas de charge, on parle d'adaptation en tension.
* Les sources de courant doivent présenter une résistance interne très élevée $R_i \gg R_L$. Idéalement : $\qty{\infty}{\ohm}$, afin que le courant de charge reste constant en cas de variation de la résistance de charge, c'est pourquoi on parle aussi d'adaptation en courant.

[question:AB203]
[question:AB204]

---

Si une source de tension doit fournir la puissance maximale à une charge, on parle d'adaptation en puissance. Cela est également important pour un émetteur qui doit transmettre le plus de puissance possible à une antenne.

La transmission de puissance maximale est atteinte lorsque

$R_i = R_L$

c'est-à-dire lorsque la résistance interne et la résistance de charge sont de même valeur.

Dans ce cas, la tension de la source se répartit uniformément entre la résistance interne et la charge. La tension et le courant aux bornes de la charge donnent alors le produit maximal possible, et donc la puissance la plus élevée.

La figure [ref:a_Leistungsanpassung] montre la puissance normalisée à la charge en fonction du rapport $R_L/R_i$. Le maximum est atteint exactement lorsque $R_L/R_i = 1$, c'est-à-dire lorsque la résistance interne et la résistance de charge sont de même valeur. Cependant, le rendement en cas d'adaptation en puissance n'est que de $\qty{50}{\percent}$, car la même puissance est dissipée à la fois dans la charge et dans la résistance interne.

<margin>
[picture:1077:a_Leistungsanpassung:Adaptation en puissance optimale pour $R_i = R_L$, ici le quotient $\frac{R_L}{R_i}=1$ et donc la puissance maximale est émise à la charge. Le graphique est logarithmique.]
[picture:937:a_Leistungsanpassung:Puissance de sortie optimale pour une résistance de charge de $\qty{50}{\ohm}$ avec une résistance interne de $\qty{50}{\ohm}$. Le graphique n'est pas logarithmique.]
</margin>

<indepth>
Les sources de tension alternatives, par exemple les générateurs sinusoïdaux, possèdent également une résistance interne indiquée à la sortie.
[photo:292:Sinusgenerator 50 Ohm:Générateur sinusoïdal avec une résistance interne de 50 ohm]
</indepth>

% Peut-être à déplacer ailleurs ?
<indepth>
La valeur de $\qty{50}{\ohm}$, couramment utilisée en haute fréquence, est un compromis technique entre une transmission de puissance maximale et des pertes aussi faibles que possible dans les lignes.

Les câbles coaxiaux avec une impédance caractéristique d'environ $\qty{30}{\ohm}$ peuvent transmettre des puissances particulièrement élevées, car le courant est moins réparti dans le câble. En revanche, les câbles d'environ $\qty{77}{\ohm}$ présentent les pertes par atténuation les plus faibles et conviennent particulièrement bien à une transmission de signaux à faible perte.

La valeur largement répandue de $\qty{50}{\ohm}$ se situe entre ces deux optima et représente un bon compromis entre une transmission de puissance élevée, des pertes modérées et une construction de câble pratique. C'est pourquoi $\qty{50}{\ohm}$ s'est imposé comme norme dans la technique radio.

Si un émetteur, un câble et une antenne sont chacun adaptés à $\qty{50}{\ohm}$, la puissance est transmise de manière optimale et les réflexions sur la ligne sont minimisées.

[picture:1078:a_50ohm:50 ohm comme compromis entre transmission de puissance maximale et pertes minimales en haute fréquence]

Tu sais maintenant aussi pourquoi notre plateforme s'appelle 50ohm.de : nous voulons t'aider à réussir les questions d'examen et ainsi obtenir les meilleures performances à l'examen 🤓
</indepth>

[question:AG401]
[question:AB202]