Dans la classe E, nous avons déjà fait connaissance avec l’*analyseur de réseau vectoriel* (VNA) (cf. figure [ref:a_vna_swr]). Dans la classe A, nous allons examiner son fonctionnement de manière plus détaillée.

Pour une mesure, le VNA génère d’abord un signal HF avec une fréquence de départ définie et l’applique à l’objet mesuré, par exemple une antenne ou un circuit oscillant. Il mesure ensuite le signal renvoyé ou réfléchi par l’objet mesuré. L’amplitude ainsi que la phase de ce signal sont enregistrées. Pour réduire l’influence des perturbations, plusieurs mesures peuvent être effectuées et moyennées pour un point de fréquence donné.

Après la mesure, la fréquence est augmentée d’un pas défini et le processus est répété. De cette manière, le VNA parcourt pas à pas l’ensemble de la plage allant de la fréquence de départ à la fréquence d’arrêt. Ce processus est appelé *balayage en fréquence*, ou autrefois parfois *wobulation*.

À partir des valeurs mesurées pour les différents points de fréquence, le VNA peut déterminer et représenter graphiquement différentes grandeurs en fonction de la fréquence. Parmi celles-ci figurent par exemple l’impédance de l’objet mesuré et le rapport d’ondes stationnaires (ROS). On peut ainsi immédiatement identifier à quelles fréquences une antenne est bien adaptée ou présente une résonance.

<margin>
[photo:323:a_vna_swr:Mesure du ROS d’une antenne filaire alimentée en bout. Le ROS est presque égal à $1$ à $\qty{14}{\mega\hertz}$]
[picture:526:a_vna_swr_2:Évolution possible du ROS d’une antenne.]
</margin>

[question:AI201]
[question:AI202]
[question:AI203]

---

Une forme d’affichage possible du VNA consiste à décomposer l’impédance en composante active et réactive (résistance active $R$ et réactance $X$). La résistance active est souvent indiquée en $\unit{\ohm}$ et la réactance, parfois, en $j\unit{\ohm}$. Les affichages des différents appareils ne sont pas uniformes. Le $j$ provient d’une notation utilisée en électrotechnique, où il représente l’unité imaginaire ($i$) des mathématiques. Une réactance positive correspond à un comportement inductif, tandis qu’une réactance négative correspond à un comportement capacitif.

<indepth>
*Les nombres imaginaires* sont un outil très répandu en électrotechnique et en mathématiques. Pour résoudre des équations comme $x^2 = -1$, on a imaginé un nombre dit imaginaire ($i$) qui, multiplié par lui-même, donne un nombre négatif : $i^2 = -1$. Aucune nombre réel ne satisfait une telle équation, car un nombre négatif multiplié par un nombre négatif donne un nombre positif. C’est pourquoi on qualifie $i$ d’« imaginaire ». Ce nombre « inventé » multiplié par lui-même donne un nombre négatif, à savoir $-1$. Si l’on additionne des nombres réels (par exemple $54$) avec un nombre imaginaire (par exemple $-12i$), on obtient un nombre complexe : $54 - 12i$. Un nombre complexe peut par exemple servir à décrire une composante active et une composante réactive d’une résistance. On peut également convertir un nombre complexe en une amplitude et une phase. Au lieu de la lettre $i$, on utilise la lettre $j$ en électrotechnique pour éviter toute confusion avec le symbole $i$ (pour les courants).
</indepth>

[question:AI204]
[question:AI205]
[question:AI206]

---

De nombreux VNA offrent la possibilité de représenter graphiquement l’évolution du ROS en fonction de la fréquence. Si la fréquence de résonance d’une antenne est trop basse, on sait qu’il faut la raccourcir. Si elle est trop élevée, il faut l’allonger.

[question:AI207]
[question:AI208]