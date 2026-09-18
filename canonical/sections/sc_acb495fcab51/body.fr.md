La *MUF* (*maximum usable frequency*, fréquence maximale utilisable), c'est-à-dire la fréquence la plus élevée que l'ionosphère peut encore *réfléchir* pour la distance entre l'émetteur et le récepteur, a déjà été abordée dans la classe E. À ce moment-là, il a été démontré que la MUF dépend de la densité des électrons libres dans la région de *réfraction*. Dans la classe A, nous allons maintenant examiner ce sujet plus en détail, en particulier sous l'angle de l'*angle de rayonnement*.

[question:AH206]
[question:AH207]

Comme nous le savons déjà, la portée des *ondes spatiales* dépend de l'*angle de rayonnement*. Plus l'onde arrive *platement* sur l'ionosphère, plus la *réfraction* est facile. Cette relation s'applique également à la MUF : plus notre signal pénètre *platement* dans l'ionosphère, plus la fréquence qui est encore *réfléchie* (la MUF) est élevée. L'illustration [ref:e_muf_winkel2] montre une simulation de la distance de saut pour un jour d'été en 2024 pour un signal de radioamateur autour de $\qty{7}{\mega\hertz}$. À $\qty{45}{\degree}$, la MUF était de $\qty{7,5}{\mega\hertz}$ ce jour-là. Si l'on modifie l'*angle de rayonnement*, la MUF change également : si l'on émet plus verticalement (par exemple $\qty{60}{\degree}$), la MUF diminue et l'onde radio n'est plus *réfléchie*. En revanche, si l'on émet plus *platement* (par exemple $\qty{30}{\degree}$), la MUF augmente. Nous allons examiner cette relation plus en détail ci-dessous.

<margin>
[picture:998:e_muf_winkel2:Distance de saut à 7 MHz en été 2024]
</margin>

---

Les stations de mesure de l'ionosphère mesurent la *fréquence critique* $f_\text{c}$ (ou souvent aussi $f_\text{k}$, $f_\text{krit}$ ou $f_\text{oF2}$). Il s'agit de la fréquence la plus élevée à laquelle l'*onde spatiale* entrant verticalement dans l'ionosphère est encore *réfléchie* (cf. illustration [ref:e_muf_winkel]). Si nous émettons verticalement vers le haut, c'est-à-dire si notre signal pénètre dans l'ionosphère sous un angle de $\qty{90}{\degree}$, la MUF est alors la plus faible, car notre signal doit alors effectuer un virage complet de 180° dans l'ionosphère. Cela signifie qu'à $\qty{90}{\degree}$, on a $f_\text{c} = MUF$.

<indepth>
Pour désigner cette fréquence, on utilise le symbole $f_o$ (lettre minuscule "o" en indice pour *onde ordinaire*), suivie de la région ionosphérique concernée, par exemple $f_\text{oF2}$ pour la région F2. Cependant, on utilise aussi souvent $f_\text{c}$, $f_\text{k}$ ou $f_\text{krit}$ comme symbole.
</indepth>

<margin>
[picture:870:e_muf_winkel:Les angles pour le calcul de la MUF]
</margin>

<indepth>
La fréquence critique est donc la fréquence la plus élevée qui revient de l'ionosphère lorsque l'on émet verticalement vers le haut. Une règle empirique indique que la fréquence la plus élevée qui est encore renvoyée en cas d'incidence *plate* est environ le triple de la fréquence critique.
</indepth>

[question:AH204]
[question:AH205]

---

L'illustration [ref:e_muf_fof2] montre l'évolution temporelle de la MUF et de $f_\text{c}$ le 08.09.2025, mesurée avec l'ionosonde de Juliusruh. Une MUF de $\qty{3000}{\kilo\mètre}$ signifie dans ce cas qu'un rayonnement très *plat* est émis pour atteindre une distance de saut de $\qty{3000}{\kilo\mètre}$.

<margin>
[picture:999:e_muf_fof2:MUF et $f_\text{c}$ le 08.09.2025]
</margin>

Pour d'autres angles de rayonnement, la MUF peut être déterminée approximativement à partir de $f_\text{c}$ à l'aide de la formule suivante (valable pour $\alpha > \qty{40}{\degree}$) issue du *recueil de formules* :

$MUF \approx \frac{f_\text{c}}{sin(\alpha)}$

où $\alpha$ désigne l'*angle de rayonnement* (cf. illustration [ref:e_muf_winkel]). En examinant la formule de plus près, on constate que la MUF est toujours supérieure à la fréquence critique – et ce d'autant plus que l'antenne d'émission ou de réception émet ou reçoit plus *platement*.

[question:AH208]

---

Pour la planification des fréquences commerciales, où l'objectif est d'assurer une *liaison radio* avec une probabilité élevée de succès, il existe également le concept de *FOT* (*frequency of optimal transmission*, fréquence optimale d'émission), ou encore $f_\text{opt}$. Il s'agit de la fréquence qui, sur un trajet de signal donné, permet une *liaison radio* avec une probabilité de 90 % sur 90 % des jours ; elle se situe généralement 15 % en dessous de la moyenne mensuelle de la MUF. Dans le *recueil de formules*, cette relation est donnée par

$f_\text{OPT} = MUF \cdot 0,85$

Avec ces informations, nous pouvons maintenant résoudre l'exercice suivant ; une calculatrice peut être utile.

[question:AH209]

<indepth>
Pour les liaisons DX en radioamateurisme, la $f_\text{opt}$ ne joue aucun rôle, car on choisit généralement la bande de fréquences la plus élevée qui permet encore une liaison (donc la plus proche de la MUF), car c'est là que l'on peut s'attendre au bruit le plus faible et donc au meilleur signal (rapport signal/bruit SNR le plus élevé).
</indepth>

Dans la classe E, nous avons déjà abordé la LUF (*Lowest Usable Frequency*). Elle est déterminée par la couche D et désigne la fréquence minimale utilisable, en dessous de laquelle l'*atténuation* est trop forte. La couche D *atténue* en effet notre signal radio, et à chaque saut, ce signal doit traverser cette couche D *deux fois*. En même temps, cette *atténuation* est d'autant plus élevée que la fréquence est basse (la relation est quadratique : si l'on divise la fréquence par deux, l'atténuation est multipliée par quatre). Par conséquent, si l'on continue à réduire la fréquence, on finit par atteindre un point où le signal *réfléchi* n'est plus utilisable ; c'est la LUF.

[question:AH210]
[question:AH211]