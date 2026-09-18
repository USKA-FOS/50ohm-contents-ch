Dans le chapitre [sec:antennengewinn], nous avons déjà abordé le radiateur isotrope (cf. illustration [ref:e_Kugelstrahler]). Le radiateur isotrope n’est pas une antenne réelle, c’est un modèle physique d’un radiateur qui émet l’énergie uniformément dans toutes les directions de l’espace. 
La puissance isotrope rayonnée équivalente (EIRP) d’une antenne réelle se réfère au radiateur isotrope. En d’autres termes, la puissance rayonnée d’une antenne réelle est comparée à celle du radiateur isotrope. Pour la puissance émise, seule l’énergie effectivement reçue par l’antenne est pertinente. En raison des pertes dans les câbles, etc., la puissance de l’émetteur ne peut pas être entièrement transmise à l’antenne dans la réalité. Cette puissance perdue ne doit pas être prise en compte dans le calcul de la puissance rayonnée. Le gain d’antenne dans la direction privilégiée fait naturellement partie du calcul. En formule, cela s’exprime ainsi :
$P_\mathrm{EIRP} = (P_\mathrm{émetteur} - P_\mathrm{pertes}) \cdot G_\mathrm{antenne}$
où $G_\mathrm{antenne}$ représente le gain d’antenne. L’EIRP est donc le produit de la puissance effectivement fournie à l’antenne et de son gain dans une direction, rapporté au radiateur isotrope.
<margin>
[picture:751:e_Kugelstrahler:Radiateur isotrope au centre d’une sphère, produisant une puissance rayonnée identique en tous points de la surface de la sphère]
</margin>
<tip>
Avant l’examen, il est conseillé de bien se familiariser avec sa calculatrice. Les calculs et les formules des différentes questions doivent être répétés régulièrement afin de maîtriser parfaitement l’appareil et les étapes de calcul lors de l’examen.
</tip>
[question:EG501]
Pour la question suivante, il est impératif de prêter attention aux signes de calcul. Les pertes sont *soustrayues* de la puissance d'émission, puis multipliées par le facteur de gain ($G_\mathrm{Antenne}$). Comme il s'agit de calculer l'EIRP, la référence doit se faire par rapport au radiateur isotrope.[question:EG502]

---

Dans le chapitre sur les décibels [sec:dezibel_1], nous avons appris qu'il est judicieux de travailler avec des valeurs en dB, car cela simplifie considérablement de nombreux calculs. Les amplifications et les atténuations peuvent être simplement additionnées ou soustraites en décibels. La figure [ref:e_verstaerkung_daempfung] montre une installation radio avec plusieurs étages d'amplification et d'atténuation. Le gain global de cette installation s'obtient en additionnant les contributions individuelles : $\qty{-2}{\dB} + \qty{6}{\dB} - \qty{3}{\dB} + \qty{2}{\dB} = \qty{3}{\dB}$, ce qui correspond à un facteur de puissance de $\num{2}$. <margin>
[picture:439:e_verstaerkung_daempfung:Amplifications et atténuations dans une installation radio]
</margin>

---

Les questions suivantes nécessitent le calcul de l'EIRP. Pour cela, on peut soit utiliser directement une formule, soit résoudre les exercices – avec un peu d'entraînement – entièrement de tête. Dans la suite, nous présenterons donc généralement les deux méthodes.La formule permettant de calculer l'EIRP est issue du recueil de formules et s'exprime comme suit :$P_\mathrm{EIRP} = P_\mathrm{émetteur} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$<indepth>
On obtient la formule de $P_\mathrm{EIRP}$ en réarrangeant la formule de gain issue du recueil de formules :$g = 10 \cdot \log_{10}\left(\frac{P_2}{P_1}\right) \unit{\dB}$
  
Comme il faut également prendre en compte une atténuation $a$, celle-ci est soustraite du gain d'antenne. Pour $P_1$, nous utilisons la puissance de l'émetteur $P_\mathrm{Sender}$, car elle représente la puissance d'entrée, et pour $P_2$, la puissance EIRP $P_\mathrm{EIRP}$, car il s'agit de la puissance de sortie résultante.

$g-a = 10 \cdot \log_{10}\left(\frac{P_\mathrm{EIRP}}{P_\mathrm{Sender}}\right) \unit{\dB} \quad\quad\quad | : \qty{10}{\dB}$
  
Nous divisons ensuite les deux côtés par $\qty{10}{\dB}$ :
  
$\frac{g-a}{\qty{10}{\dB}} = \log_{10}\left(\frac{P_\mathrm{EIRP}}{P_\mathrm{Sender}}\right) \quad\quad\quad | 10^x$
  
Ensuite, nous appliquons $10^x$ des deux côtés pour résoudre le logarithme :
  
$10^{\frac{g-a}{\qty{10}{\dB}}} = \frac{P_\mathrm{EIRP}}{P_\mathrm{Sender}} \quad\quad\quad | \cdot P_\mathrm{Sender}$
  
En multipliant par $P_\mathrm{Sender}$, on obtient la formule requise :
  
$P_\mathrm{EIRP} = P_\mathrm{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$
</indepth>

Dans cette formule, $g_i$ représente le gain d'antenne par rapport au radiateur isotrope, tandis que $a$ décrit l'atténuation due aux câbles et aux adaptateurs.

[question:EG503]

La première méthode de calcul utilise la formule mentionnée ci-dessus. Comme il n'y a pas de pertes de puissance, l'atténuation est $a=0$ et la formule se simplifie en : 

$P_\mathrm{EIRP} = P_\mathrm{émetteur} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 10^{\frac{\qty{26}{\dBi}}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 398 \approx \qty{100}{\watt}$

---

La deuxième méthode de calcul possible exploite le fait que l'on peut "décomposer" les valeurs en dB. Dans la question, le gain d'antenne est $g = \qty{26}{\dBi}$. Dans le recueil de formules, le tableau [ref:e_dezibel_leistungsfaktoren] présente un aperçu des facteurs de puissance pour des valeurs dB importantes. Pour $\qty{26}{\dB}$, il n'y a pas d'entrée directe. Cependant, comme les niveaux en décibels s'additionnent, on peut décomposer cette valeur de manière judicieuse :

$\qty{26}{\dBi} = \qty{20}{\dBi} + \qty{6}{\dB}$

<margin>
| c:dB | c:≈ facteur de puissance |
| $\num{0}$ | $\num{1}$ |
| $\num{1,5}$ | $\sqrt{2} = 1,41$ |
| $\num{2,15}$ | $\num{1,64}$ |
| $\num{3}$ | $\num{2}$ |
| $\num{5}$ | $\sqrt{10} = 3,16$ |
| $\num{6}$ | $\num{4}$ |
| $\num{10}$ | $\num{10}$ |
| $\num{20}$ | $\num{100}$ |
[table:e_dezibel_leistungsfaktoren:Facteurs de puissance importants en dB]
</margin>

<tip>
D'autres valeurs en décibels souvent utiles sont disponibles dans le chapitre [sec:dezibel_1].
</tip>

Pour $\qty{20}{\dB}$, le tableau indique un facteur de puissance de $\num{100}$, et pour $\qty{6}{\dB}$, un facteur de $\num{4}$. Ainsi, la puissance isotrope rayonnée équivalente se calcule très simplement :

$P_\mathrm{EIRP} = \qty{250}{\milli\watt} \cdot 100 \cdot 4 = \qty{100}{\watt}$

La bonne réponse est donc $\qty{100}{\watt}$ de puissance rayonnée (EIRP).

Pour la question suivante, nous pouvons procéder de la même manière que pour la question précédente.

[question:EG504]

---

Pour de nombreux radioamateurs, il est difficile de respecter la distance de sécurité nécessaire avec une puissance d'émission de, par exemple, $\qty{100}{\watt}$. Dans ces cas, le fonctionnement en QRP est une solution. Même avec un appareil non-QRP, il est possible de réduire la puissance de sortie à une certaine valeur, comme illustré dans la figure [ref:e_ausgangsleistung_ic].

<margin>
[photo:229:e_ausgangsleistung_ic:Sur de nombreux émetteurs-récepteurs, comme ici avec l'IC-705, il est possible de régler la puissance de sortie de manière continue ou par petits incréments.]
</margin>

[question:EG511]

L'antenne verticale indiquée dans cette question présente un gain de $g=\qty{5,15}{\dBi}$, les pertes de câble sont négligées, c'est-à-dire $a = 0$. Si l'antenne n'avait aucun gain ($\qty{0}{\dBi}$), la puissance d'émission devrait simplement être limitée à $\qty{10}{\watt}$ maximum. La puissance rayonnée serait alors de seulement $\qty{10}{\watt}$ EIRP. Cependant, comme un gain d'antenne de $\qty{5,15}{\dBi}$ est présent, la puissance d'émission doit être réduite en conséquence. La puissance d'émission doit être au moins $\qty{5,15}{\dB}$ inférieure à $\qty{10}{\watt}$.

Il existe également deux méthodes de calcul possibles pour cette question. Commençons par la méthode utilisant la formule connue. Cependant, dans cet exercice, ce n'est pas la puissance rayonnée $P_\mathrm{EIRP}$ qui est recherchée, mais la puissance d'émission $P_\mathrm{Sender}$. Il faut donc réarranger la formule en conséquence :

$P_\mathrm{EIRP} = P_\mathrm{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}} \quad\quad\quad | : 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

On obtient ainsi :

$ P_\mathrm{émetteur} = \frac{P_\mathrm{EIRP}}{10^{\frac{g_i-a}{\qty{10}{\dB}}}} $

On remplace les valeurs :

$ P_\mathrm{émetteur} = \frac{\qty{10}{\watt}}{10^{\frac{\qty{5,15}{\dBi}}{\qty{10}{\dB}}}} = \frac{\qty{10}{\watt}}{3,27} \approx \qty{3,05}{\watt} $

Le calcul avec une calculatrice donne $\qty{3,05}{\watt}$. Avec une **limitation** à $\qty{3}{\watt}$, on respecte la valeur limite de moins de $\qty{10}{\watt}$ EIRP.

La deuxième méthode de calcul passe à nouveau par la décomposition des valeurs en dB. En examinant la valeur $g=\qty{5,15}{\dBi}$, on remarque qu'il est possible de la décomposer en :

$\qty{5,15}{\dBi} = \qty{3}{\dBi} + \qty{2,15}{\dB}$

Dans le tableau [ref:e_dezibel_leistungsfaktoren], on trouve le facteur pour $\qty{2,15}{\dB}$ comme étant $\num{1,64}$. On obtient ainsi pour la **puissance d'émission** maximale :

$P_\mathrm{émetteur} = \frac{\qty{10}{\watt}}{2\cdot 1,64} = \frac{\qty{10}{\watt}}{3,28} \approx \qty{3}{\watt}$

Comme prévu, on obtient ici le même résultat. Avec $\qty{3}{\watt}$, on est du bon côté.

La question suivante pourrait également être résolue à l'aide du recueil de formules en remplaçant $a=\qty{1}{\dB}$, mais elle se calcule très simplement de tête.[question:EG505]

Comme décrit au tout début de cette section, la puissance rayonnée EIRP prend en compte le gain d'antenne ($\qty{11}{\dBi}$) et la puissance effectivement disponible à l'antenne. La puissance d'émission est atténuée de $\qty{1}{\dB}$ par le câble, et l'ensemble du système d'antenne présente un gain réel de $\qty{10}{\dBi}$. Dans notre tableau [ref:e_dezibel_leistungsfaktoren] du recueil de formules, le facteur $\num{10}$ est indiqué pour $\qty{10}{\dB}$. À partir d'une puissance d'émission de $\qty{100}{\watt}$, on obtient une puissance rayonnée de $\qty{1000}{\watt}$. Pour la question suivante, il faut veiller à ce qu'une antenne dipôle soit utilisée. Elle peut également être calculée très simplement de tête.[question:EG506]

Le gain d'une antenne dipôle par rapport au radiateur sphérique est de $\qty{2,15}{\dB}$. Cela correspond à un facteur de $\num{1,64}$. Cela est également indiqué dans le recueil de formules :$P_\mathrm{EIRP} = P_\mathrm{ERP} + \qty{2,15}{\dB}$ou, en tant que facteur :$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 1,64$où $P_\mathrm{ERP}$ représente la puissance rayonnée par rapport au dipôle.Le gain du dipôle est de $\qty{2,15}{\dBi}$, ce qui correspond exactement à l'atténuation du câble dans la question. Les deux s'annulent donc. L'antenne dipôle rayonne une puissance isotrope rayonnée équivalente (EIRP) de $\qty{75}{\watt}$.

Dans la question suivante, un dipôle est également proposé comme antenne.

[question:EG507]

On cherche la puissance isotrope rayonnée équivalente $P_\mathrm{EIRP}$. Il faut d'abord prendre en compte l'atténuation du câble. Une atténuation de $\qty{10}{\dB}$ correspond à un rapport de puissance de $\num{0,1}$. En utilisant ce facteur d'atténuation ainsi que le facteur de gain de l'antenne dipôle de $\num{1,64}$, on peut ensuite calculer la puissance rayonnée.

$P_\mathrm{EIRP} = \qty{100}{\watt} \cdot 0,1 \cdot 1,64 = \qty{16,4}{\watt}$

Pour la question suivante, on trouve également une formule directement applicable dans le recueil de formules. Comme nous avons une antenne directionnelle dont le gain est indiqué par rapport au dipôle (ERP), il faut ajouter $\qty{2,15}{\dB}$ pour le calcul de $P_\mathrm{EIRP}$ :

$P_\mathrm{EIRP} = P_\mathrm{émetteur} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}}$

[question:EG508]

---

En insérant les valeurs dans la formule, on peut résoudre rapidement la question. Mais il est aussi possible de le faire mentalement. Calculons le gain total du système et décomposons-le ensuite :

$\qty{-2}{\dB} + \qty{5}{\dB} + \qty{2,15}{\dB} = \qty{3}{\dB} + \qty{2,15}{\dB}$ 

Nous pouvons maintenant lire les facteurs dans le tableau :

$P_\mathrm{EIRP} = \qty{5}{\watt} \cdot 2 \cdot 1,64 = \qty{16,4}{\watt}$

On peut résoudre la question suivante de la même manière. Il faut simplement veiller à ce que le gain soit donné par rapport au dipôle.

[question:EG509]

Calculons à nouveau le gain total et décomposons-le :

$\qty{-1}{\dB} + \qty{11}{\dB} + \qty{2,15}{\dB} = \qty{10}{\dB} + \qty{2,15}{\dB}$ 

Nous pouvons maintenant lire les facteurs dans le tableau :

$P_\mathrm{EIRP} = \qty{0,6}{\watt} \cdot 10 \cdot 1,64 = \qty{9,8}{\watt}$

Dans la question suivante, une antenne avec un gain de $\qty{0}{\dB}$ par rapport au dipôle est indiquée. Cela signifie simplement que cette antenne est un dipôle.

[question:EG510]

On peut à nouveau utiliser la formule du [recueil de formules](#).

$P_\mathrm{EIRP} = P_\mathrm{émetteur} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{8,5}{\watt} \cdot 10^{\frac{\qty{0}{\dB}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{9,9}{\watt}$

On peut aussi l'estimer mentalement : si l'on calcule le gain total du système, celui-ci n'est que de $\qty{0,65}{\dB}$, soit moins de $\qty{1}{\dB}$. Selon notre tableau [ref:e_dezibel_leistungsfaktoren], $\qty{1}{\dB}$ correspond à un facteur de $\num{1,26}$. La valeur cible doit donc se situer entre $\qty{8,5}{\watt}$ et $\qty{10,71}{\watt}$. Seule la valeur de $\qty{9,9}{\watt}$ est donc possible.
