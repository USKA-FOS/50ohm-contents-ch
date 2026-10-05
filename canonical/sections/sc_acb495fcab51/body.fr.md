La *MUF* (*maximum usable frequency*), c'est-à-dire la fréquence la plus élevée que l'ionosphère peut encore réfracter pour la distance entre l'émetteur et le récepteur, nous l'avons déjà rencontrée dans le cours HB3 dans la section [sec:muf_luf_1]. Il était clair que la MUF dépend de la densité des électrons libres dans la région de réfraction. Maintenant, dans le cours HB9, nous allons examiner ce sujet plus en détail, en particulier en ce qui concerne l'angle de rayonnement.

[question:AH206]
[question:AH207]

Comme nous le savons déjà, la portée des ondes spatiales dépend de l'angle de rayonnement. Plus l'onde arrive sur l'ionosphère de manière plate, plus la réfraction se produit facilement. Cette relation vaut également pour la MUF : la fréquence qui est encore réfractée, la *MUF*, est d'autant plus élevée que notre signal pénètre dans l'ionosphère de manière plus plate. La figure [ref:e_muf_winkel2] montre une simulation de la distance de saut pour un jour d'été en 2024 pour un signal de radioamateurisme autour de $\qty{7}{\mega\hertz}$. À $\qty{45}{\degree}$, la MUF ce jour-là était de $\qty{7,5}{\mega\hertz}$. Si l'on modifie l'angle de rayonnement, la MUF change également : si l'on rayonne plus verticalement (par exemple $\qty{60}{\degree}$), la MUF diminue et l'onde radio n'est plus réfractée. En revanche, si l'on rayonne plus à plat (par exemple $\qty{30}{\degree}$), la MUF augmente. Dans la suite, nous examinerons cette relation plus en détail.

<margin>
[picture:998:e_muf_winkel2:Distance de saut à 7 MHz en été 2024]
</margin>

%<wordorigin>
%L'abréviation *FOT* peut facilement être mémorisée ainsi : *F*réquence *O*ptimale de *T*rafic ou "Frequency %Optimum Traffic".
%La FOT est standardement à 85 % de la MUF (Maximum Usable Frequency).
%</wordorigin>
% Supprimé à nouveau, car redondant.

---

Les stations de mesure de l'ionosphère mesurent la fréquence critique dite $f_\text{c}$ (ou souvent aussi $f_\text{k}$, $f_\text{krit}$ ou $f_\text{oF2}$). C'est la fréquence la plus élevée à laquelle l'onde spatiale pénétrant verticalement dans l'ionosphère est encore réfléchie (cf. figure [ref:e_muf_winkel]). Lorsque nous rayonnons verticalement vers le haut, c'est-à-dire que notre signal pénètre dans l'ionosphère sous un angle de $\qty{90}{\degree}$, la MUF est la plus faible, car notre signal doit alors effectuer un "demi-tour" complet dans l'ionosphère, c'est-à-dire effectuer un virage à 180°. Cela signifie qu'à $\qty{90}{\degree}$, on a $f_\text{c} = MUF$.

<indepth>
Comme symbole, on utilise $f_o$ (petite lettre "O" en indice pour *ordinary wave*) suivie de la région ionosphérique pour laquelle cette fréquence est valable, par exemple $f_\text{oF2}$ pour la région F2. Cependant, $f_\text{c}$, $f_\text{k}$ ou $f_\text{krit}$ sont aussi souvent utilisés comme symboles.
</indepth>

<margin>
[picture:870:e_muf_winkel:Les angles pour le calcul de la MUF]
</margin>

<indepth>
La fréquence critique est donc la fréquence la plus élevée qui revient de l'ionosphère lorsqu'on rayonne verticalement vers le haut. Une règle empirique dit que la fréquence la plus élevée qui est encore réfléchie lors d'une incidence *plate* est environ le triple de la fréquence critique.
</indepth>

[question:AH204]
[question:AH205]

---

La figure [ref:e_muf_fof2] montre l'évolution temporelle de la MUF et de $f_\text{c}$ le 08.09.2025, mesurée avec l'ionosonde de Juliusruh. MUF $\qty{3000}{\kilo\meter}$ signifie dans ce cas qu'un rayonnement très plat est utilisé pour atteindre une distance de saut de $\qty{3000}{\kilo\meter}$.

<margin>
[picture:999:e_muf_fof2:MUF et $f_\text{c}$ le 08.09.2025]
</margin>

Pour d'autres angles de rayonnement, la MUF peut être approximativement déterminée à partir de $f_\text{c}$ à l'aide de la formule suivante du recueil de formules (valable pour $\alpha > \qty{40}{\degree}$) :

$MUF \approx \frac{f_\text{c}}{sin(\alpha)}$

où $\alpha$ désigne l'angle de rayonnement (cf. figure [ref:e_muf_winkel]). En examinant la formule de plus près, on constate que la MUF est toujours supérieure à la fréquence critique – et d'autant plus que l'antenne d'émission rayonne à plat ou que l'antenne de réception reçoit à plat.

[question:AH208]

---

Pour la planification commerciale des fréquences, où il est important qu'une liaison radio réussisse avec une forte probabilité, il existe également le terme *FOT* (*frequency of optimal transmission*, fréquence optimale d'émission), ou aussi $f_\text{opt}$. C'est la fréquence qui, sur un trajet de signal donné, permet statistiquement une liaison radio 90 % des jours ; elle se situe généralement 15 % en dessous de la moyenne mensuelle de la MUF. Dans le recueil de formules, nous trouvons cette relation sous la forme

$f_\text{OPT} = MUF \cdot 0,85$

Avec ces informations, nous pouvons maintenant résoudre l'exercice suivant ; une calculatrice est utile.

[question:AH209]

<indepth>
Pour les liaisons DX en radioamateurisme, la $f_\text{opt}$ ne joue aucun rôle, car on choisit généralement la bande de fréquences la plus élevée qui permet encore une liaison (c'est-à-dire la plus proche de la MUF), car c'est là que l'on peut s'attendre au bruit de fond le plus faible et donc au meilleur signal (rapport signal/bruit SNR le plus élevé).
</indepth>

Dans la classe E, nous avons déjà rencontré la LUF (Lowest Usable Frequency). Elle est déterminée par la couche D et désigne la fréquence utilisable la plus basse en dessous de laquelle l'atténuation est trop forte. La couche D *atténue* en effet notre signal radio et, par saut, ce signal doit encore traverser *deux* fois cette couche D. En même temps, cette atténuation est d'autant plus élevée que la fréquence est basse (la relation est quadratique : si l'on divise la fréquence par deux, l'atténuation est multipliée par quatre). Par conséquent, si l'on réduit continuellement la fréquence, on atteindra également un point où le signal réfracté n'est plus utilisable ; c'est la LUF.

[question:AH210]
[question:AH211]
