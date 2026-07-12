Dans la classe N, nous avons déjà rencontré le radiateur isotrope (voir figure [ref:e_Kugelstrahler]). Le radiateur isotrope n'est pas une antenne réelle, c'est un modèle physique pour un radiateur qui émet de l'énergie uniformément dans toutes les directions de l'espace. 

La puissance isotrope rayonnée équivalente (EIRP) d'une antenne réelle se réfère au radiateur isotrope. En d'autres termes, la puissance rayonnée d'une antenne réelle est comparée à la puissance rayonnée du radiateur isotrope. Pour la puissance rayonnée, seule l'énergie qui arrive effectivement à l'antenne est pertinente. En raison de l'atténuation des câbles, etc., la puissance de l'émetteur ne peut pas être entièrement fournie à l'antenne dans le monde réel. Cette puissance perdue ne doit pas être prise en compte dans le calcul de la puissance de rayonnement. Le gain d'antenne dans la direction préférentielle fait bien sûr partie du calcul. En termes de formules, cela signifie:

$P_\text{EIRP} = (P_\text{Sender} - P_\text{Verluste}) \cdot G_\text{Antenne}$

Où $G$ représente le gain d'antenne. L'EIRP est donc le produit de la puissance fournie directement à l'antenne et de son gain dans une direction, par rapport au radiateur isotrope.

<margin>
[picture:751:e_Kugelstrahler:Radiateur isotrope au centre d'une sphère, qui produit la même puissance de rayonnement à tous les points de la surface de la sphère]
</margin>

<tip>
Avant l'examen, il est conseillé de bien se familiariser avec sa calculatrice de poche. Les calculs et les formules des différentes questions doivent toujours être pratiqués afin de maîtriser l'appareil et les étapes de calcul lors de l'examen.
</tip>

[question:EG501]

Dans la question suivante, il est absolument nécessaire de faire attention aux signes de calcul. Les pertes sont *soustraites* de la puissance d'émission et ensuite *multipliées* par le facteur de gain ($G_{Antenne}$). Comme l'EIRP doit être calculée, la référence au radiateur isotrope doit être effectuée.

[question:EG502]

---

Dans le chapitre sur les décibels, nous avons appris qu'il est utile de calculer avec des valeurs en dB, car de nombreux calculs s'en trouvent considérablement simplifiés. Les amplifications et les atténuations peuvent être simplement additionnées ou soustraites en décibels. La figure [ref:e_verstaerkung_daempfung] montre une installation radio avec plusieurs éléments d'amplification et d'atténuation. L'amplification totale de cette installation résulte de l'addition des contributions individuelles à $\qty{-2}{\dB} + \qty{6}{\dB} - \qty{3}{\dB} + \qty{2}{\dB} = \qty{3}{\dB}$, ce qui correspond à un facteur de puissance de $\num{2}$.

<margin>
[picture:439:e_verstaerkung_daempfung:Amplifications et atténuations dans une installation radio]
</margin>

---

Les questions suivantes nécessitent le calcul de l'EIRP. Pour cela, soit une formule peut être utilisée directement, soit les tâches peuvent être résolues – avec un peu de pratique – entièrement dans la tête. Par conséquent, nous souhaitons donc montrer les deux méthodes de procédure dans ce qui suit.

La formule pour calculer l'EIRP résulte du recueil de formules et est la suivante:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

<indepth>
On obtient la formule pour $P_\text{EIRP}$, en réarrangeant la formule de gain du recueil de formules de manière appropriée:
  
$g = 10 \cdot \log_{10}\left(\frac{P_2}{P_1}\right) \unit{\dB}$
  
Comme une atténuation $a$ doit également être prise en compte, celle-ci est soustraite du gain d'antenne. Pour $P_1$, nous utilisons la puissance d'émission $P_\text{Sender}$, car elle représente la puissance d'entrée, et pour $P_2$ nous utilisons $P_\text{EIRP}$, car il s'agit de la puissance de sortie résultante.

$g-a = 10 \cdot \log_{10}\left(\frac{P_\text{EIRP}}{P_\text{Sender}}\right) \unit{\dB} \quad\quad\quad | : \qty{10}{\dB}$
  
Nous divisons des deux côtés par $\qty{10}{\dB}$:
  
$\frac{g-a}{\qty{10}{\dB}} = \log_{10}\left(\frac{P_\text{EIRP}}{P_\text{Sender}}\right) \quad\quad\quad | 10^x$
  
Ensuite, nous appliquons $10^x$ des deux côtés pour résoudre le logarithme:
  
$10^{\frac{g-a}{\qty{10}{\dB}}} = \frac{P_\text{EIRP}}{P_\text{Sender}} \quad\quad\quad | \cdot P_\text{Sender}$
  
En multipliant par $P_\text{Sender}$, on obtient la formule nécessaire:
  
$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$
</indepth>

Où $g_i$ est le gain d'antenne par rapport au radiateur isotrope, tandis que $a$ décrit l'atténuation due aux câbles et aux appareils d'adaptation.

[question:EG503]

La première méthode de calcul utilise la formule mentionnée ci-dessus. Comme il n'y a pas de pertes de puissance, l'atténuation $a=0$ et la formule se simplifie en: 

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 10^{\frac{\qty{26}{dBi}}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 398 \approx \qty{100}{\watt}$

---

La deuxième méthode de calcul possible utilise le fait que les valeurs en dB peuvent être "décomposées". Dans la question, le gain d'antenne est de $g = \qty{26}{\dBi}$. Dans le recueil de formules, on trouve dans le tableau [ref:e_dezibel_leistungsfaktoren] un aperçu des facteurs de puissance pour des valeurs importantes en dB. Pour $\qty{26}{\dB}$, il n'y a pas d'entrée directe. Comme les niveaux en décibels peuvent s'additionner, on peut décomposer la valeur de manière significative:

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

Pour $\qty{20}{\dB}$, un facteur de puissance de $\num{100}$ est indiqué dans le tableau, et pour $\qty{6}{\dB}$, un facteur de $\num{4}$. Ainsi, la puissance isotrope rayonnée équivalente peut être calculée très simplement:

$P_\text{EIRP} = \qty{250}{\milli\watt} \cdot 100 \cdot 4 = \qty{100}{\watt}$

La bonne réponse est donc $\qty{100}{\watt}$ EIRP.

Pour la question suivante, nous pouvons procéder de la même manière que pour la question précédente. 

[question:EG504]

---

Pour de nombreux radioamateurs, il est difficile de respecter la distance de sécurité nécessaire pour une puissance d'émission de par exemple $\qty{100}{\watt}$. Le mode QRP est une solution dans ces cas. Si l'on reste en dessous de la limite de $\qty{10}{\watt}$ EIRP, l'affichage d'une installation fixe de radioamateur selon § 9 BEMFV peut être omis. Même avec un appareil non QRP, on peut réduire la puissance de sortie à une certaine valeur, comme le montre la figure [ref:e_ausgangsleistung_ic].

<margin>
[photo:229:e_ausgangsleistung_ic:Che de nombreux émetteurs-récepteurs, la puissance de sortie peut être ajustée en continu, ou comme ici sur l'IC-705, par petites étapes.]
</margin>

[question:EG511]

L'antenne verticale mentionnée dans cette question a un gain de $g=\qty{5,15}{\dBi}$, les pertes de câble sont négligées, c'est-à-dire $a = 0$. Si l'antenne n'avait pas de gain ($\qty{0}{\dBi}$), la puissance d'émission devrait simplement être limitée à un maximum de $\qty{10}{\watt}$. La puissance rayonnée serait alors seulement $\qty{10}{\watt}$ EIRP. Mais comme un gain d'antenne de $\qty{5,15}{\dBi}$ est présent, la puissance d'émission doit être réduite en conséquence. La puissance d'émission doit être au moins $\qty{5,15}{\dB}$ inférieure à $\qty{10}{\watt}$.

Il existe également deux méthodes de calcul possibles ici. Commençons par la méthode utilisant la formule connue. Dans cette tâche, cependant, ce n'est pas la puissance rayonnée $P_\text{EIRP}$ qui est recherchée, mais la puissance d'émission $P_\text{Sender}$. Par conséquent, nous devons reformuler la formule en conséquence:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}} \quad\quad\quad | : 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

Ainsi, nous obtenons:

$ P_\text{Sender} = \frac{P_\text{EIRP}}{10^{\frac{g_i-a}{\qty{10}{\dB}}}} $

Nous insérons les valeurs:

$ P_\text{Sender} = \frac{\qty{10}{\watt}}{10^{\frac{\qty{5,15}{\dBi}}{\qty{10}{\dB}}}} = \frac{\qty{10}{\watt}}{3,27} \approx \qty{3,05}{\watt} $

Le calcul avec la calculatrice donne $\qty{3,05}{\watt}$. Avec une limitation à $\qty{3}{\watt}$, on respecte la limite de moins de $\qty{10}{\watt}$ EIRP.

La deuxième méthode de calcul consiste à nouveau à décomposer les valeurs en dB. Si l'on examine la valeur $g=\qty{5,15}{\dBi}$, on reconnaît que l'on peut la décomposer en 

$\qty{5,15}{\dBi} = \qty{3}{\dBi} + \qty{2,15}{\dB}$

On peut la décomposer. Dans le tableau [ref:e_dezibel_leistungsfaktoren], on trouve le facteur pour $\qty{2,15}{\dB}$ comme $\num{1,64}$. Ainsi, pour la puissance d'émission maximale:

$P_\text{Sender} = \frac{\qty{10}{\watt}}{2\cdot 1,64} = \frac{\qty{10}{\watt}}{3,28} \approx \qty{3}{\watt}$

Comme on pouvait s'y attendre, nous arrivons ici au même résultat. Avec $\qty{3}{\watt}$, on est du bon côté.

La question suivante pourrait être résolue à nouveau avec le recueil de formules, en insérant $a=\qty{1}{\dB}$, mais cela se fait très simplement dans la tête. 

[question:EG505]

Comme décrit tout au début de la section, pour la puissance rayonnée EIRP, le gain d'antenne ($\qty{11}{\dBi}$) et la puissance qui arrive effectivement à l'antenne sont pris en compte. La puissance d'émission est atténuée par le câble de $\qty{1}{\dB}$, le système d'antenne complet a un gain réel de $\qty{10}{\dBi}$. Dans notre tableau [ref:e_dezibel_leistungsfaktoren] dans le recueil de formules, le facteur $\num{10}$ est indiqué pour $\qty{10}{\dB}$. La puissance d'émission de $\qty{100}{\watt}$ devient une puissance rayonnée de $\qty{1000}{\watt}$.

Pour la question suivante, il faut faire attention à ce qu'une antenne dipôle est utilisée. Celle-ci peut également être calculée très simplement dans la tête.

[question:EG506]

Le gain d'une antenne dipôle par rapport au radiateur sphérique est de $\qty{2,15}{\dB}$. Cela correspond au facteur de $\num{1,64}$. Cela se trouve également dans le recueil de formules:

$P_\text{EIRP} = P_\text{ERP} + \qty{2,15}{\dB}$

ou en facteur:

$P_\text{EIRP} = P_\text{ERP} \cdot 1,64$

où $P_\text{ERP}$ représente la puissance rayonnée par rapport au dipôle. 

Le gain du dipôle est de $\qty{2,15}{\dBi}$, ce qui correspond ici exactement à l'atténuation du câble dans la question. Ils s'annulent ainsi. L'antenne dipôle émet $\qty{75}{\watt}$ EIRP.

Dans la question suivante, une antenne dipôle est également spécifiée comme antenne. 

[question:EG507]

La puissance isotrope rayonnée équivalente $P_\text{EIRP}$ est recherchée. Tout d'abord, l'atténuation du câble doit être prise en compte. Une atténuation de $\qty{10}{\dB}$ correspond à un rapport de puissance de $\num{0,1}$. Avec ce facteur d'atténuation ainsi que le facteur de gain d'antenne du dipôle de $\num{1,64}$, la puissance rayonnée peut ensuite être calculée.

$P_\text{EIRP} = \qty{100}{\watt} \cdot 0,1 \cdot 1,64 = \qty{16,4}{\watt}$


Pour la question suivante, une formule directement applicable se trouve également dans le recueil de formules. Comme nous avons une antenne directionnelle dont le gain est indiqué par rapport au dipôle (ERP), $\qty{2,15}{\dB}$ doivent être ajoutés pour le calcul de $P_\text{EIRP}$:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}}$

[question:EG508]

---

En insérant dans la formule, on peut résoudre la question rapidement. Mais cela fonctionne aussi ici dans la tête. Calculons le gain total du système et décomposons-le à nouveau de manière appropriée:

$\qty{-2}{\dB} + \qty{5}{\dB} + \qty{2,15}{\dB} = \qty{3}{\dB} + \qty{2,15}{\dB}$ 

Maintenant, nous pouvons lire les facteurs à nouveau dans le tableau:

$P_\text{EIRP} = \qty{5}{\watt} \cdot 2 \cdot 1,64 = \qty{16,4}{\watt}$

La question suivante peut également être résolue de la même manière. Il faut seulement faire attention au fait que le gain est donné par rapport au dipôle. 

[question:EG509]

Nous calculons à nouveau le gain total et le décomposons:

$\qty{-1}{\dB} + \qty{11}{\dB} + \qty{2,15}{\dB} = \qty{10}{\dB} + \qty{2,15}{\dB}$ 

Nous pouvons maintenant lire à nouveau les facteurs dans le tableau :

$P_\text{EIRP} = \qty{0,6}{\watt} \cdot 10 \cdot 1,64 = \qty{9,8}{\watt}$

Dans la question suivante, une antenne avec un gain de $\qty{0}{\dB}$ par rapport au dipôle est indiquée. Cela ne signifie rien d'autre que le fait qu'il s'agit d'une antenne dipôle.

[question:EG510]

Ici, la formule du recueil de formules peut être utilisée à nouveau :

$P_\text{EIRP} = P_\text{émetteur} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{8,5}{\watt} \cdot 10^{\frac{\qty{0}{\dB}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{9,9}{\watt}$

On peut aussi l'estimer de tête : si l'on calcule à nouveau le gain total du système, celui-ci n'est que de $\qty{0,65}{\dB}$, donc pas même $\qty{1}{\dB}$. $\qty{1}{\dB}$ correspond, selon notre tableau [ref:e_dezibel_leistungsfaktoren], à un facteur de $\num{1,26}$. La valeur cible doit donc se situer entre $\qty{8,5}{\watt}$ et $\qty{10,71}{\watt}$. Seules les $\qty{9,9}{\watt}$ sont donc en question.