Dans les sections [sec:strommessung], [sec:spannungsmessung] et [sec:strom_spannung_messung_2], nous avons déjà appris comment mesurer correctement le courant et la tension, et quelles sont les propriétés des résistances internes des appareils de mesure. Si les appareils de mesure ne sont pas correctement intégrés dans le circuit, on obtient des indications fausses ou absurdes, ou, dans le pire des cas, on peut endommager l'appareil de mesure. Ici, dans le cours pour HB9, il y a deux questions supplémentaires qui testent la mesure correcte du courant et de la tension – mais dans un contexte un peu plus complexe.

La première question concerne la mesure de la puissance d'un amplificateur (Power Amplifier, PA). Nous connaissons déjà la relation $P = U \cdot I$ : la puissance peut être déterminée en mesurant la tension et le courant, puis en multipliant les deux valeurs. Dans la figure [ref:a_strom_spannung_messung], le bloc d’alimentation est connecté à gauche, l'amplificateur PA est au milieu, et un autre consommateur, l'émetteur (TRX), est connecté à droite. Si nous voulons maintenant déterminer la puissance de l'amplificateur PA, seul le courant qui circule dans l'amplificateur PA peut être mesuré.

<margin>
[picture:1003:a_strom_spannung_messung:Mesure de la puissance d'un amplificateur (PA)]
</margin>

[question:AI101]

Pour la question suivante, rappelons-nous les règles du cours HB3 : les voltmètres sont toujours connectés en parallèle et les ampèremètres toujours en série. Cela rend la question très facile à résoudre.

[question:AI102]

---

Dans ce qui suit, nous allons examiner deux caractéristiques lors de la mesure, souvent confondues :

- Résolution
- Précision de mesure (également appelée tolérance ou erreur)

La *résolution* désigne la plus petite variation de la grandeur mesurée qu'un appareil peut encore afficher. Exemple : un multimètre avec une résolution de $\qty{0,1}{\volt}$ ne peut pas distinguer entre $\qty{10,5}{\volt}$ et $\qty{10,45}{\volt}$ si la différence est inférieure à la résolution. Un appareil avec une résolution de $\qty{0,01}{\volt}$ peut en revanche distinguer beaucoup plus finement. La résolution est généralement indiquée par le fabricant de l'appareil de mesure.

<tip>
Examinons d'abord la *résolution* à l'aide d'une horloge. Si l'horloge possède une indication des heures et des minutes, le temps peut être donné à la minute près. Mais qu'il soit 13 heures 3 minutes et 10 secondes ou 13 heures 3 minutes et 59 secondes, cela ne peut pas être lu. *Une minute* est donc la *plus petite résolution* de l'horloge (de même, une horloge avec une trotteuse a une plus petite résolution d'une seconde).
</tip>

La *précision de mesure* (également appelée erreur de mesure ou tolérance) d'un appareil décrit à quel point la valeur affichée peut au maximum s'écarter de la valeur réelle – à la fois vers le haut et vers le bas, par exemple $\pm\qty{5}{\percent}$. Une règle empirique simple est : plus la plage de mesure qu'un appareil doit couvrir est grande, plus la précision de la mesure est généralement faible.

La précision de mesure dépend entre autres de la résistance interne de l'appareil de mesure, car celle-ci influence le résultat de la mesure.
Dans la classe E, nous avons appris : un ampèremètre a une résistance interne très faible (idéalement $\qty{0}{\ohm}$), un voltmètre en revanche a une résistance interne très élevée (idéalement $\qty{\infty}{\ohm}$). Dans la classe A, nous voulons maintenant examiner en plus comment nos appareils de mesure peuvent capturer avec précision la tension ou l'intensité du courant réellement présente. La valeur mesurée affichée diffère en effet généralement de la valeur réelle – et cela est dû aux résistances internes non parfaites des appareils de mesure, qui influencent la mesure.

---

Examinons le schéma équivalent d'un voltmètre réel dans la figure [ref:a_reale_spannungsmessung] pour la question d'examen suivante. Outre l'ampèremètre idéal, un voltmètre réel contient une résistance connectée en parallèle, par exemple de $\qty{10}{\mega\ohm}$. Si cette résistance était infiniment grande, elle n'existerait pratiquement pas – et nous aurions un appareil de mesure idéal. Cela signifie cependant que lors d'une mesure de tension réelle, un petit courant circule toujours à travers cette résistance, ce qui influence notre résultat de mesure. Imaginons par exemple que nous voulions mesurer la tension aux bornes d'un diviseur de tension : la résistance interne de l'appareil de mesure charge légèrement le diviseur de tension, de sorte que nous ne mesurons pas exactement la tension qu'un appareil de mesure idéal afficherait.

<margin>
[picture:1004:a_reale_spannungsmessung:Schéma équivalent d'un voltmètre réel]
</margin>

---

De même que pour le voltmètre, il en va de même pour l'ampèremètre. Un ampèremètre réel se compose de l'ampèremètre proprement dit et d'une petite résistance connectée en série, aux bornes de laquelle une petite tension chute toujours. Si cette résistance était nulle, elle n'existerait pratiquement pas – et nous aurions à nouveau l'appareil de mesure idéal.

<margin>
[picture:1007:a_reale_strommessung:Schéma équivalent d'un ampèremètre réel]
</margin>

---

[question:AI104]

<tip>
Pour cette question, l'indication "Plus petite résolution $\qty{100}{\micro\volt}$" n'est pas importante. Elle peut être résolue uniquement à l'aide de la loi d'Ohm.
</tip>

---

Comment se comportent les caractéristiques calculées à partir de valeurs mesurées – comme la puissance dans notre exemple du début ($P = U \cdot I$) après une mesure de courant et de tension ? Les grandeurs mesurées individuelles comme le courant et la tension s'écartent chacune de la valeur réelle en raison d'erreurs de mesure, et ces écarts se répercutent dans le calcul.

Examinons un exemple concret : supposons que nous voulions déterminer la puissance et mesurons pour cela une tension continue et un courant continu. Les deux appareils de mesure affichent des valeurs qui sont chacune inférieures de cinq pour cent. Il ne faut pas commettre l'erreur d'additionner simplement les écarts des grandeurs individuelles. La formule de puissance montre clairement que dans ce cas, les erreurs se multiplient. Examinons cela en détail :

$U_\text{Mesurée}=0,95 \cdot U_\text{Vraie}$ et $I_\text{Mesuré}=0,95 \cdot I_\text{Vrai}$

Nous calculons la puissance avec notre formule connue :

$P_\text{Mesurée}=U_\text{Mesurée} \cdot I_{Mesuré}$

Maintenant, substituons les vraies valeurs :

$P_\text{Mesurée} = 0,95 \cdot U_\text{Vraie} \cdot 0,95 \cdot I_\text{Vrai} = 0,9025 \cdot U_\text{Vraie} \cdot I_\text{Vrai}$

Cela signifie que la puissance mesurée est inférieure d'environ $\qty{9,75}{\percent}$ à la puissance réelle, car $1-0,9025 \equiv \qty{9,75}{\percent}$. Avec cette connaissance, la question d'examen suivante est résoluble, les valeurs concrètes du courant et de la tension ne sont pas pertinentes pour la solution.

[question:AI103]
