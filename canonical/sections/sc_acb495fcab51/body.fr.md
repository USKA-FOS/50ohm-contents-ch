La *MUF* (*maximum usable frequency*), c'est-à-dire la fréquence la plus élevée que l'ionosphère peut encore réfléchir pour la distance entre l'émetteur et le récepteur, nous l'avons déjà rencontrée dans la classe E. Il est apparu que la MUF dépend de la densité des électrons libres dans la région de réfraction. Dans la classe A, nous allons examiner ce sujet plus en détail, en particulier en ce qui concerne l'angle d'émission.

[question:AH206]
[question:AH207]

Comme nous le savons déjà, la portée des ondes spatiales dépend de l'angle d'émission. Plus l'onde frappe l'ionosphère de manière plate, plus la réfraction est facile. Cette relation s'applique également à la MUF : la fréquence encore réfléchie, la *MUF*, est d'autant plus élevée que notre signal pénètre dans l'ionosphère de manière plus plate. La figure [ref:e_muf_winkel2] montre une simulation de la distance de saut pour un jour d'été en 2024 pour un signal radioamateur autour de $\qty{7}{\mega\hertz}$. À $\qty{45}{\degree}$, la MUF ce jour-là était de $\qty{7,5}{\mega\hertz}$. Si l'on modifie l'angle d'émission, la MUF change également : si l'on émet de manière plus raide (par exemple $\qty{60}{\degree}$), la MUF diminue et l'onde radio n'est plus réfractée. Si, en revanche, on émet de manière plus plate (par exemple $\qty{30}{\degree}$), la MUF augmente. Nous allons examiner ce lien plus en détail ci-dessous.

<margin>
[picture:998:e_muf_winkel2:Distance de saut à 7 MHz en été 2024]
</margin>

---

Les stations de mesure de l'ionosphère mesurent ce que l'on appelle la fréquence critique $f_\text{c}$ (ou souvent aussi $f_\text{k}$, $f_\text{krit}$ ou $f_\text{oF2}$). Il s'agit de la fréquence la plus élevée pour laquelle l'onde spatiale entrant verticalement dans l'ionosphère est encore réfléchie (voir figure [ref:e_muf_winkel]). Si nous émettons verticalement vers le haut, notre signal pénètre donc dans l'ionosphère sous un angle de $\qty{90}{\degree}$, la MUF est la plus faible, car notre signal doit alors effectuer un virage à 180° dans l'ionosphère. Cela signifie que pour $\qty{90}{\degree}$, on a $f_\text{c} = MUF$. 

<indepth>
Comme symbole de formule, on utilise $f_o$ (petite lettre en indice "O" pour *onde ordinaire*) suivie de la région ionosphérique pour laquelle cette fréquence s'applique, par exemple $f_\text{oF2}$ pour la région F2. Cependant, on utilise souvent aussi $f_\text{c}$, $f_\text{k}$ ou $f_\text{krit}$ comme symbole de formule.
</indepth>

<margin>
[picture:870:e_muf_winkel:Les angles pour le calcul de la MUF]
</margin>

<indepth>
La fréquence critique est donc la fréquence la plus élevée qui revient de l'ionosphère lorsque l'on émet verticalement vers le haut. Une règle empirique veut que la fréquence la plus élevée qui soit encore renvoyée en cas d'irradiation *plate* soit environ le triple de la fréquence critique.
</indepth>

[question:AH204]
[question:AH205]

---

La figure [ref:e_muf_fof2] montre l'évolution temporelle de la MUF et de $f_\text{c}$ le 08.09.2025, mesurée avec l'ionosonde de Juliusruh. MUF $\qty{3000}{\kilo\meter}$ signifie dans ce cas que l'on émet très platement pour atteindre une distance de saut de $\qty{3000}{\kilo\meter}$.

<margin>
[picture:999:e_muf_fof2:MUF et $f_\text{c}$ le 08.09.2025]
</margin>

Pour d'autres angles d'émission, la MUF peut être déterminée approximativement à partir de $f_\text{c}$ à l'aide de la formule suivante du recueil de formules (valable pour $\alpha > \qty{40}{\degree}$) :

$MUF \approx \frac{f_\text{c}}{sin(\alpha)}$

où $\alpha$ désigne l'angle d'émission (voir figure [ref:e_muf_winkel]). Si l'on examine la formule de plus près, on constate que la MUF est toujours supérieure à la fréquence critique – et d'autant plus que l'antenne d'émission émet plus platement ou que l'antenne de réception reçoit.

[question:AH208]

---

Pour la planification commerciale des fréquences, où il est important qu'une liaison radio réussisse avec une probabilité élevée, il existe en outre le terme de *FOT* (*frequency of optimal transmission*, fréquence d'émission optimale), ou encore $f_\text{opt}$. Il s'agit de la fréquence qui permet statistiquement une liaison radio sur un certain trajet de signal 90% des jours ; elle se situe généralement 15% en dessous de la moyenne mensuelle de la MUF. Dans le recueil de formules, nous trouvons cette relation sous la forme 

$f_\text{OPT} = MUF \cdot 0,85$

Avec ces informations, nous pouvons maintenant résoudre l'exercice suivant ; un calculateur de poche est utile à cet effet.

[question:AH209]

<indepth>
Pour les liaisons DX en radioamateur, la $f_\text{opt}$ n'a pas d'importance, car on choisit généralement la bande de fréquences la plus élevée qui permet encore une liaison (donc la plus proche de la MUF), car c'est là que l'on peut s'attendre au bruit de fond le plus faible et donc au meilleur signal (rapport signal/bruit SNR le plus élevé).
</indepth>

Dans la classe E, nous avons déjà rencontré la LUF (Lowest Usable Frequency). Elle est déterminée par la région D et désigne la fréquence utilisable la plus basse, en dessous de laquelle l'atténuation est trop forte. La région D *atténue* en effet notre signal radio et ce signal doit également traverser cette région D *deux* fois par saut. Simultanément, cette atténuation est d'autant plus grande que la fréquence est faible (la relation est quadratique : si l'on divise la fréquence par deux, l'atténuation est multipliée par quatre). C'est pourquoi, si l'on réduit la fréquence en continu, on finira également par atteindre le point où le signal réfléchi n'est plus utilisable ; il s'agit de la LUF.

[question:AH210]
[question:AH211]
