Dans les classes N et E, nous avons déjà appris à mesurer correctement le courant et la tension et quelles sont les propriétés des résistances internes des appareils de mesure. Si les appareils de mesure ne sont pas correctement intégrés dans le circuit, on obtient des indications fausses ou absurdes ou, dans le pire des cas, on peut endommager l'appareil de mesure. Dans la classe A, il y a encore deux autres questions qui vérifient la mesure correcte du courant et de la tension - mais dans un contexte un peu plus complexe.

Dans la première question, il s'agit de la mesure de la puissance d'un amplificateur (Power Amplifier, PA). Nous connaissons déjà la relation $P = U \cdot I$ : la puissance peut être déterminée en mesurant la tension et le courant, puis en multipliant les deux valeurs. Dans la figure [ref:a_strom_spannung_messung], à gauche, l'alimentation électrique est connectée sous la forme d'une alimentation, au milieu se trouve la PA et à droite est connecté un autre consommateur, l'émetteur (TRX). Si nous voulons maintenant déterminer la puissance de la PA, seul le courant qui circule dans la PA doit être mesuré.

<margin>
[picture:1003:a_strom_spannung_messung:Mesure de la puissance d'un amplificateur (PA)]
</margin>

[question:AI101]

Pour la question suivante, nous nous souvenons des règles de la classe E, selon lesquelles les appareils de mesure de tension sont toujours branchés en parallèle et les appareils de mesure de courant toujours en série. La question est donc très facile à résoudre.

[question:AI102]

---

Ensuite, nous voulons examiner deux caractéristiques lors de la mesure, qui sont souvent confondues :

- Résolution
- Précision de mesure (également appelée tolérance ou erreur)

La *résolution* désigne le plus petit changement de la grandeur mesurée qu'un appareil peut encore afficher. Exemple : Un multimètre avec une résolution de $\qty{0,1}{\volt}$ ne peut pas distinguer entre $\qty{10,5}{\volt}$ et $\qty{10,45}{\volt}$ si la différence est inférieure à la résolution. Un appareil avec une résolution de $\qty{0,01}{\volt}$ peut en revanche distinguer beaucoup plus finement. La résolution est généralement indiquée par le fabricant de l'appareil de mesure.

<tip>
Examinons d'abord la *résolution* à l'aide d'une horloge. Si l'horloge a une indication des heures et des minutes, le temps peut être indiqué avec une précision d'une minute. Mais si l'heure est 13 heures 3 minutes et 10 secondes ou 13 heures 3 minutes et 59 secondes, cela ne peut pas être lu. *Une minute* est donc la *plus petite résolution* de l'horloge (correspondant à une horloge avec une aiguille des secondes, la plus petite résolution est d'une seconde).
</tip>

La *précision de mesure* (également appelée erreur de mesure ou tolérance) d'un appareil décrit à quel point la valeur affichée peut s'écarter au maximum de la valeur réelle - à la fois vers le haut et vers le bas, par exemple $\pm\qty{5}{\percent}$. Une règle simple est la suivante : plus le domaine de mesure qu'un appareil doit couvrir est grand, plus la précision de la mesure est généralement faible.

La précision de la mesure dépend, entre autres, de la résistance interne de l'appareil de mesure, car celle-ci influence le résultat de la mesure.
Dans la classe E, nous avons appris qu'un appareil de mesure de courant a une très faible résistance interne (idéalement $\qty{0}{\ohm}$), tandis qu'un appareil de mesure de tension a une très grande résistance interne (idéalement $\qty{\infty}{\ohm}$). Dans la classe A, nous voulons maintenant examiner en outre comment nos appareils de mesure peuvent capturer avec précision la tension ou l'intensité du courant réellement appliquée. La valeur mesurée affichée diffère en effet généralement de la valeur réelle - et cela est dû aux résistances internes non parfaites des appareils de mesure, qui influencent la mesure.

---

Examinons le schéma de remplacement d'un appareil de mesure de tension réel dans la figure [ref:a_reale_spannungsmessung] pour la question d'examen suivante. En plus de l'ampèremètre idéal, un appareil de mesure de tension réel contient une résistance branchée en parallèle, par exemple de $\qty{10}{\mega\ohm}$. Si cette résistance était infinie, elle n'existerait pratiquement pas - et nous aurions un appareil de mesure idéal. Cela signifie cependant que lors d'une mesure de tension réelle, un petit courant circule toujours à travers cette résistance, ce qui influence notre résultat de mesure. Imaginons par exemple que nous voulons mesurer la tension à un diviseur de tension : la résistance interne de l'appareil de mesure charge légèrement le diviseur de tension, de sorte que nous ne mesurons pas exactement la tension qu'un appareil de mesure idéal indiquerait.

<margin>
[picture:1004:a_reale_spannungsmessung:Schéma de remplacement d'un appareil de mesure de tension réel]
</margin>

---

Comme pour l'appareil de mesure de tension, il en va de même pour l'appareil de mesure de courant. Un appareil de mesure de courant réel se compose de l'ampèremètre proprement dit et d'une petite résistance qui est branchée en série et à laquelle une petite tension chute toujours. Si cette résistance était nulle, elle n'existerait pratiquement pas - et nous aurions à nouveau l'appareil de mesure idéal.

<margin>
[picture:1007:a_reale_strommessung:Schéma de remplacement d'un appareil de mesure de courant réel]
</margin>

---

[question:AI104]

<tip>
Dans cette question, l'indication "Résolution la plus petite $\qty{100}{\micro\volt}$" n'est pas importante. Elle peut être résolue à l'aide de la loi d'Ohm seule.
</tip>

---

Comment se comportent maintenant les caractéristiques qui sont calculées à partir des valeurs de mesure - par exemple la puissance dans notre exemple du début ($P = U \cdot I$) après une mesure de courant et de tension ? Les grandeurs de mesure individuelles telles que le courant et la tension s'écartent chacune de la valeur réelle en raison des erreurs de mesure, et ces écarts se répercutent en conséquence dans le calcul.

Examinons un exemple concret : Supposons que nous voulions déterminer la puissance et mesurer à cet effet une tension continue et un courant continu. Les deux appareils de mesure indiquent des valeurs qui sont chacune cinq pour cent trop faibles. On ne doit pas faire l'erreur d'additionner simplement les écarts des grandeurs de mesure individuelles. La formule de puissance montre clairement que les erreurs se multiplient dans ce cas. Examinons cela en détail :

$U_\text{Mesuré}=0,95 \cdot U_\text{Vrai}$ et $I_\text{Mesuré}=0,95 \cdot I_\text{Vrai}$

Nous calculons la puissance avec notre formule connue :

$P_\text{Mesuré}=U_\text{Mesuré} \cdot I_{Mesuré}$

Nous insérons maintenant les valeurs réelles : 

$P_\text{Mesuré} = 0,95 \cdot U_\text{Vrai} \cdot 0,95 \cdot I_\text{Vrai} = 0,9025 \cdot U_\text{Vrai} \cdot I_\text{Vrai}$

Cela signifie que la puissance mesurée est environ $\qty{9,75}{\percent}$ inférieure à la puissance réelle, car $1-0,9025 \equiv \qty{9,75}{\percent}$. Avec cette connaissance, la question d'examen suivante peut être résolue, les valeurs concrètes de courant et de tension ne sont pas pertinentes pour la solution.

[question:AI103]
