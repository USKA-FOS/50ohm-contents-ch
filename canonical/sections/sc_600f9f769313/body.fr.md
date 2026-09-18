Dans les classes N et E, nous avons déjà appris à mesurer correctement le courant et la tension, ainsi que les propriétés des résistances internes des appareils de mesure. Si les appareils ne sont pas correctement intégrés dans le circuit, on obtient des indications erronées, voire absurdes, ou l'on risque d'endommager l'appareil de mesure dans le pire des cas. Dans la classe A, deux questions supplémentaires vérifient la mesure correcte du courant et de la tension, mais dans un contexte un peu plus complexe.

La première question porte sur la mesure de la puissance d'un amplificateur (Power Amplifier, PA). Nous connaissons déjà la relation $P = U \cdot I$ : la puissance peut être déterminée en mesurant la tension et le courant, puis en multipliant les deux valeurs. Dans la figure [ref:a_strom_spannung_messung], à gauche, l'alimentation électrique est connectée sous forme d'alimentation stabilisée, au centre se trouve la PA et à droite, un autre consommateur, l'émetteur (TRX), est branché. Si nous voulons maintenant déterminer la puissance de la PA, nous ne devons mesurer que le courant qui circule dans la PA.

<margin>
[picture:1003:a_strom_spannung_messung:Mesure de la puissance d'un amplificateur (PA)]
</margin>

[question:AI101]

Pour la question suivante, nous nous souvenons des règles de la classe E : les voltmètres sont toujours branchés en parallèle et les ampèremètres toujours en série. Grâce à cela, la question est très facile à résoudre.

[question:AI102]

---

Nous allons maintenant examiner deux caractéristiques souvent confondues lors des mesures :

- la résolution
- la précision de mesure (également appelée tolérance ou erreur)

La *résolution* désigne la plus petite variation de la grandeur mesurée que l'appareil peut encore afficher. Exemple : un multimètre avec une résolution de $\qty{0,1}{\volt}$ ne peut pas distinguer entre $\qty{10,5}{\volt}$ et $\qty{10,45}{\volt}$ si la différence est inférieure à la résolution. Un appareil avec une résolution de $\qty{0,01}{\volt}$ peut en revanche distinguer beaucoup plus finement. La résolution est généralement indiquée par le fabricant de l'appareil de mesure.

<tip>
Considérons d'abord la *résolution* à l'aide d'une horloge. Si l'horloge affiche les heures et les minutes, le temps peut être indiqué avec une précision d'une minute. Mais on ne peut pas savoir si c'est 13 h 3 min 10 s ou 13 h 3 min 59 s. *Une minute* est donc la *plus petite résolution* de l'horloge (une horloge avec une aiguille des secondes a une plus petite résolution d'une seconde).
</tip>

La *précision de mesure* (également appelée erreur de mesure ou tolérance) d'un appareil décrit dans quelle mesure la valeur affichée peut s'écarter au maximum de la valeur réelle, tant vers le haut que vers le bas, par exemple $\pm\qty{5}{\percent}$. Une règle empirique simple dit : plus la plage de mesure qu'un appareil doit couvrir est grande, plus la précision de la mesure est généralement faible.

La précision de mesure dépend notamment de la résistance interne de l'appareil de mesure, car celle-ci influence le résultat de la mesure.
Dans la classe E, nous avons appris : un ampèremètre a une résistance interne très faible (idéalement $\qty{0}{\ohm}$), tandis qu'un voltmètre a une résistance interne très élevée (idéalement $\qty{\infty}{\ohm}$). Dans la classe A, nous allons maintenant examiner en plus comment nos appareils de mesure captent avec précision la tension ou l'intensité du courant réellement présentes. La valeur mesurée affichée diffère généralement de la valeur réelle – et cela est dû aux résistances internes non parfaites des appareils de mesure, qui influencent la mesure.

---

Examinons le schéma équivalent d'un voltmètre réel dans la figure [ref:a_reale_spannungmessung] pour la question d'examen suivante. En plus de l'ampèremètre idéal, un voltmètre réel contient une résistance branchée en parallèle, par exemple de $\qty{10}{\mega\ohm}$. Si cette résistance était infinie, elle n'existerait pratiquement pas – et nous aurions un appareil de mesure idéal. Cela signifie cependant que lors d'une mesure de tension réelle, un faible courant circule à travers cette résistance, influençant notre résultat de mesure. Imaginons par exemple que nous voulons mesurer la tension aux bornes d'un diviseur de tension : en raison de la résistance interne de l'appareil de mesure, le diviseur de tension est légèrement chargé, de sorte que nous ne mesurons pas exactement la tension qu'afficherait un appareil de mesure idéal.

<margin>
[picture:1004:a_reale_spannungmessung:Schéma équivalent d'un voltmètre réel]
</margin>

---

Le principe est similaire pour l'ampèremètre. Un ampèremètre réel se compose de l'ampèremètre proprement dit et d'une petite résistance branchée en série, sur laquelle une faible tension chute toujours.

<margin>
[picture:1007:a_reale_strommessung:Schéma équivalent d'un ampèremètre réel]
</margin>

---

[question:AI104]

<tip>
Pour cette question, l'indication "Résolution minimale $\qty{100}{\micro\volt}$" n'est pas importante. Elle peut être résolue uniquement à l'aide de la loi d'Ohm.
</tip>

---

Comment se comportent alors les grandeurs calculées à partir des valeurs mesurées – par exemple la puissance dans notre exemple du début ($P = U \cdot I$) après une mesure de courant et de tension ? Les grandeurs mesurées individuelles comme le courant et la tension s'écartent de la valeur réelle en raison des erreurs de mesure, et ces écarts se répercutent dans le calcul.

Examinons un exemple concret : supposons que nous voulons déterminer la puissance en mesurant une tension continue et un courant continu. Les deux appareils de mesure affichent des valeurs qui sont chacune inférieures de cinq pour cent à la valeur réelle. On ne doit pas commettre l'erreur d'additionner simplement les écarts des grandeurs mesurées individuelles. Grâce à la formule de la puissance, il est clair que les erreurs se multiplient dans ce cas. Examinons cela en détail :

$U_\text{Mesuré}=0,95 \cdot U_\text{Vraie}$ et $I_\text{Mesuré}=0,95 \cdot I_\text{Vraie}$

Nous calculons la puissance avec notre formule connue :

$P_\text{Mesuré}=U_\text{Mesuré} \cdot I_\text{Mesuré}$

Nous insérons maintenant les valeurs réelles :

$P_\text{Mesuré} = 0,95 \cdot U_\text{Vraie} \cdot 0,95 \cdot I_\text{Vraie} = 0,9025 \cdot U_\text{Vraie} \cdot I_\text{Vraie}$

Cela signifie que la puissance mesurée est environ $\qty{9,75}{\percent}$ inférieure à la puissance réelle, car $1-0,9025 \equiv \qty{9,75}{\percent}$. Avec cette connaissance, la question d'examen suivante peut être résolue, les valeurs concrètes de courant et de tension ne sont pas pertinentes pour la solution.

[question:AI103]