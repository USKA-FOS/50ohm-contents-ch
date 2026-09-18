Dans le recueil de formules, nous trouvons la formule suivante pour calculer la fréquence de coupure des circuits RC, par exemple des filtres passe-haut ou passe-bas :

$f_g = \frac{1}{2 \pi \cdot R \cdot C}$

Avec cette formule, nous pouvons résoudre une série de questions d’examen.

<indepth>
Pour les lecteurs intéressés par les mathématiques : la formule de la fréquence de coupure d’un circuit RC peut également être dérivée en considérant les impédances complexes de la résistance et du condensateur. Nous considérons le filtre passe-bas RC comme un diviseur de tension dépendant de la fréquence.

[picture:175:a_rc_tiepass:Filtre passe-bas RC comme diviseur de tension dépendant de la fréquence]

Pour le rapport entre la tension de sortie et la tension d’entrée, nous avons :

$\frac{|U_A|}{|U_E|} = \frac{|X_C|}{|R + X_C|}$

La réactance capacitive du condensateur s’exprime par :

$X_C = \frac{1}{j\omega C}$

Ce qui donne :

$\frac{|U_A|}{|U_E|} = \frac{\left|\frac{1}{j\omega C}\right|}{\left|R + \frac{1}{j\omega C}\right|}$

Pour les valeurs absolues, nous obtenons :

$\frac{|U_A|}{|U_E|} = \frac{\frac{1}{\omega C}}{\sqrt{R^2 + \frac{1}{\omega^2 C^2}}}$

En multipliant le numérateur et le dénominateur par $\omega C$, l’expression se simplifie en :

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{1 + R^2\omega^2 C^2}}$

La fréquence de coupure est définie comme la fréquence à laquelle la tension de sortie chute à un facteur de $\frac{1}{\sqrt{2}} \approx 0{,}707$ de sa valeur initiale. Cela correspond à environ $\qty{70}{\percent}$ de la tension de sortie ou à une chute de niveau de $\qty{3}{\dB}$.

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{2}}$

D’où il découle :

$\frac{1}{\sqrt{1 + R^2\omega^2 C^2}} = \frac{1}{\sqrt{2}}$

Par conséquent, il doit être satisfait que :

$R^2\omega^2 C^2 = 1$

et donc :

$\omega R C = 1$

Avec $\omega = 2\pi f$, nous obtenons :

$2\pi f_g R C = 1$

Ce qui donne pour la fréquence de coupure :

$f_g = \frac{1}{2\pi R C}$
</indepth>

[question:AD201]
[question:AD202]
[question:AD203]

---

L’impédance d’un circuit oscillant série composé d’une résistance, d’une bobine et d’un condensateur, comme illustré dans la figure [ref:a_serienschwingkreis], se calcule à l’aide de la formule suivante :

$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$

<margin>
[picture:181:a_serienschwingkreis:Circuit oscillant série]
</margin>

---

Lorsque la réactance de la bobine est exactement égale à la réactance du condensateur, c’est-à-dire $X_\text{L} = X_\text{C}$, l’impédance devient :

$Z=\sqrt{R^2+\left(0\right)^2}=\sqrt{R^2}=R$

Dans ce cas, il s’agit de la *fréquence de résonance* $f_0$ du circuit oscillant, où l’impédance n’est déterminée que par la résistance ohmique. Aux fréquences supérieures ou inférieures à la fréquence de résonance, l’impédance est supérieure à la résistance ohmique, car soit la bobine, soit le condensateur présente une réactance plus élevée. La figure [ref:a_serienschwingkreis_frequenzgang] montre la réponse en fréquence d’un circuit oscillant série, où la fréquence de résonance est clairement visible. Aux fréquences supérieures ou inférieures à la fréquence de résonance, le circuit oscillant série présente une impédance totale élevée (impédance). À haute fréquence, la bobine présente une résistance élevée. À basse fréquence, le condensateur présente une résistance élevée.

<margin>
[picture:1037:a_serienschwingkreis_frequenzgang:Réponse en fréquence d’un circuit oscillant série]
</margin>

[question:AD206]
[question:AD207]
[question:AD204]

Pour les circuits oscillants parallèles et séries, la relation suivante s’applique en cas de résonance, comme montré ci-dessus :

$X_\text{C} = X_\text{L}$

Si nous substituons les formules des réactances de la bobine et du condensateur dans l’équation ci-dessus, nous obtenons :

$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$

Ce qui donne la formule :

$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$

---

Cette formule est appelée formule d’oscillation de Thomson et s’applique aussi bien aux circuits oscillants parallèles que séries. Dans le recueil de formules, elle se trouve dans la section « Circuits oscillants ». Elle indique que la fréquence de résonance d’un circuit oscillant dépend uniquement de l’inductance de la bobine et de la capacité du condensateur. Les résistances ohmiques et les pertes n’ont pas d’influence sur la fréquence de résonance. Avec cette formule, nous pouvons calculer la fréquence de résonance des circuits oscillants.

<indepth>
Les résistances ohmiques dans les circuits oscillants parallèles et séries influencent cependant le facteur de qualité ($Q$) et donc la bande passante ($B$) du circuit oscillant – nous y reviendrons plus en détail ultérieurement.
</indepth>

[question:AD208]
[question:AD209]
[question:AD210]

---

La fréquence de résonance des circuits oscillants parallèles se calcule de la même manière que pour les circuits oscillants séries, à l’aide de la formule d’oscillation de Thomson mentionnée précédemment.

[question:AD211]
[question:AD212]

---

Pour modifier la fréquence de résonance des circuits oscillants, il est possible de faire varier soit l’inductance de la bobine, soit la capacité du condensateur dans le circuit oscillant.
Comme le montre la formule d’oscillation de Thomson, les grandeurs $L$ et $C$ se trouvent chacune au dénominateur. Ainsi, une augmentation de $L$ ou $C$ entraîne une réduction de la fréquence du circuit oscillant, car le dénominateur de la formule devient plus grand. À l’inverse, une diminution de $L$ et $C$ entraîne une augmentation de la fréquence de résonance du circuit oscillant.

<indepth>
La racine carrée n’a pas d’influence sur cette relation, car la racine d’un nombre plus grand est également un nombre plus grand. Cependant, la relation n’est pas linéaire.
</indepth>

L’inductance d’une bobine peut être augmentée en augmentant le nombre de spires, en resserrant les spires ou en insérant un noyau en ferrite.
À l’inverse, l’inductance d’une bobine peut être réduite en diminuant le nombre de spires, en écartant les spires, en retirant un noyau en ferrite ou en insérant un noyau en cuivre. La capacité des condensateurs peut être modifiée en remplaçant le condensateur ou en utilisant des condensateurs variables ou ajustables.

Avec ces connaissances, nous pouvons maintenant répondre aux questions suivantes.

[question:AD213]
[question:AD214]
[question:AD215]
[question:AD216]
[question:AD217]

Une combinaison de circuits oscillants parallèles et séries, disposés de manière appropriée, peut être utilisée comme filtre passe-bande. En cas de résonance, les circuits oscillants parallèles se comportent comme des résistances de forte impédance, tandis que le circuit oscillant série se comporte comme une résistance de faible impédance.

[question:AD205]

La bande passante des filtres et des filtres passe-bande est souvent indiquée par rapport à une valeur d’atténuation spécifique. L’atténuation décrit dans quelle mesure un signal est affaibli par rapport au passage maximal.

En général, la *bande passante* d’un filtre est définie par le point à $\qty{-3}{\dB}$.

Au point à $\qty{-3}{\dB}$, nous avons :

- Seule la moitié de la puissance traverse le filtre
- La tension de signal atteint environ $0{,}7$ fois la valeur maximale

La bande passante résulte de la différence entre la fréquence de coupure supérieure et inférieure au point à $\qty{-3}{\dB}$ :

$ B = f_\mathrm{o} - f_\mathrm{u} $

[question:AD220]

Où :

- $f_\mathrm{o}$ : fréquence de coupure supérieure
- $f_\mathrm{u}$ : fréquence de coupure inférieure

La bande passante à $\qty{-3}{\dB}$ est utilisée pour décrire l’adéquation d’un filtre à certains modes de fonctionnement :

- Filtre à bande étroite d’environ $\qty{500}{\hertz}$ de bande passante : adapté pour la CW (télégraphie)
- Filtre plus large d’environ $\qty{2,7}{\kilo\hertz}$ de bande passante : adapté pour la transmission vocale en BLU

[question:AD221]
[question:AD222]

Dans la question suivante, il ne faut pas lire la bande passante au point à $\qty{-3}{\dB}$, mais au point à $\qty{-60}{\dB}$.

[question:AD219]

Le facteur de qualité d’un circuit oscillant (appelé Q en anglais) est déterminé par le rapport entre les réactances de la capacité et de l’inductance en cas de résonance et la résistance de perte ohmique. Si un circuit oscillant ne contenait aucune résistance de perte ohmique, son facteur Q serait infini. Cependant, les composants réels présentent toujours des pertes. Les inductances ont toujours une résistance de perte ohmique, les condensateurs ont des pertes diélectriques qui se traduisent également par une résistance ohmique. Plus les résistances ohmiques dans un circuit oscillant sont élevées, plus son facteur Q est faible. Pour les filtres à haute qualité et à flancs raides, on utilise souvent des filtres à quartz.

Pour calculer le facteur Q, nous utilisons les formules correspondantes du recueil de formules, selon qu’il s’agit d’un circuit oscillant série ou parallèle :

Pour le circuit oscillant série, en cas de résonance ($X_\text{L} = X_\text{C}$) :

$Q = \frac{f_0}{B} = \frac{X_\text{L}}{R_\text{S}}$

Pour le circuit oscillant parallèle, en cas de résonance ($X_\text{L} = X_\text{C}$) :

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD225]

---

D’après l’exemple de calcul ci-dessus, nous pouvons maintenant également calculer le facteur de qualité du circuit oscillant parallèle. La fréquence de résonance est calculée comme dans l’exemple précédent. Il faut cependant noter que pour le calcul de $Q$, il faut utiliser la formule du circuit oscillant parallèle :

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD226]

La bande passante des circuits oscillants parallèles et séries peut également être calculée simplement à partir de la fréquence de résonance du circuit oscillant et de son facteur de qualité à l’aide de la formule suivante (disponible dans le recueil de formules) :

$Q = \frac{f_0}{B}$

En réarrangeant la formule, nous obtenons la bande passante $B$ :

$B = \frac{f_0}{Q}$

La formule ci-dessus s’applique aussi bien au circuit oscillant série qu’au circuit oscillant parallèle !

[question:AD224]

Grâce aux connaissances décrites précédemment, nous pouvons maintenant calculer étape par étape la question suivante.
[question:AD223]

---

Pour transmettre des signaux entre des étages de circuit ainsi que dans les filtres des émetteurs et récepteurs, on utilise souvent des circuits oscillants couplés. Dans ce cas, deux circuits oscillants sont couplés de manière inductive ou capacitive. La figure [ref:a_gekoppelte_schwingkreise] montre un couplage inductif. Selon l’application, ce couplage peut être :

- *faible* (d),
- *sous-critique* (c),
- *critique* (b) ou
- *sur-critique* (a)

Le degré de couplage détermine l’influence mutuelle et donc la bande passante et la courbe de réponse du dispositif.

<margin>
[picture:184:a_gekoppelte_schwingkreise:Circuits oscillants couplés]
</margin>

En cas de couplage faible ou sous-critique, il y a peu d’influence mutuelle ; en revanche, l’atténuation d’insertion du dispositif est relativement élevée et la bande passante est relativement faible.

En cas de couplage critique, les deux circuits oscillants s’influencent mutuellement de telle sorte qu’une courbe de réponse plate avec une faible atténuation est obtenue dans la bande passante, et celle-ci est parfaitement plane dans la bande passante souhaitée (plateau). La bande passante du dispositif est alors plus grande qu’en cas de couplage faible ou sous-critique. C’est ainsi qu’un couplage critique peut être reconnu.

En cas de couplage sur-critique, l’influence mutuelle des deux circuits oscillants est très forte, ce qui entraîne une forte modification des deux fréquences de résonance et donc une grande bande passante. La courbe de réponse est alors fortement déformée dans la bande passante et deux points de résonance apparaissent à gauche et à droite de la fréquence centrale. La courbe de réponse présente une « encoche ». C’est ainsi qu’un couplage sur-critique peut être reconnu.

[question:AD227]
[question:AD228]
[question:AD229]