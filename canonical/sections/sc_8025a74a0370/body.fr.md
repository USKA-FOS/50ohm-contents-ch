Dans le recueil de formules, nous trouvons la formule suivante pour le calcul de la fréquence de coupure des circuits RC, par exemple des filtres passe-haut ou passe-bas :

$f_g = \frac{1}{2 \pi \cdot R \cdot C}$

Avec cette formule, nous pouvons résoudre une série de questions d'examen.

<indepth>
Pour les lecteurs intéressés par les mathématiques : la formule pour la fréquence de coupure d'un circuit RC peut également être dérivée en considérant les impédances complexes de la résistance et du condensateur. Nous considérons le filtre passe-bas RC comme un diviseur de tension dépendant de la fréquence.

[picture:175:a_rc_tiepass:Filtre passe-bas RC en tant que diviseur de tension dépendant de la fréquence]

Pour le rapport de la tension de sortie à la tension d'entrée, nous avons :

$\frac{|U_A|}{|U_E|} = \frac{|X_C|}{|R + X_C|}$

La réactance capacitive du condensateur est :

$X_C = \frac{1}{j\omega C}$

Nous obtenons donc :

$\frac{|U_A|}{|U_E|} = \frac{\left|\frac{1}{j\omega C}\right|}{\left|R + \frac{1}{j\omega C}\right|}$

Pour les amplitudes, nous avons :

$\frac{|U_A|}{|U_E|} = \frac{\frac{1}{\omega C}}{\sqrt{R^2 + \frac{1}{\omega^2 C^2}}}$

En multipliant le numérateur et le dénominateur par $\omega C$, l'expression se simplifie en :

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{1 + R^2\omega^2 C^2}}$

La fréquence de coupure est définie de telle sorte que la tension de sortie soit réduite au facteur $\frac{1}{\sqrt{2}} \approx 0{,}707$ de la valeur initiale. Cela correspond à environ $\qty{70}{\percent}$ de la tension de sortie ou à une atténuation de niveau de $\qty{3}{\dB}$.

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{2}}$

Il en résulte :

$\frac{1}{\sqrt{1 + R^2\omega^2 C^2}} = \frac{1}{\sqrt{2}}$

Par conséquent, nous devons avoir :

$R^2\omega^2 C^2 = 1$

et donc :

$\omega R C = 1$

Avec $\omega = 2\pi f$, nous obtenons :

$2\pi f_g R C = 1$

Il en résulte pour la fréquence de coupure :

$f_g = \frac{1}{2\pi R C}$
</indepth>

[question:AD201] 
[question:AD202] 
[question:AD203] 

---

La réponse en fréquence d'un circuit oscillant série composé d'une résistance, d'une bobine et d'un condensateur, comme représenté dans la figure [ref:a_serienschwingkreis], se calcule selon la formule suivante :
  
$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$

<margin>
[picture:181:a_serienschwingkreis:Circuit oscillant série]
</margin>

---

Si la réactance de la bobine est exactement égale à la réactance du condensateur, c'est-à-dire $X_\text{L} = X_\text{C}$, alors l'impédance est :

$Z=\sqrt{R^2+\left(0\right)^2}=\sqrt{R^2}=R$

Dans ce cas, il s'agit de la soi-disant *fréquence de résonance* $f_0$ du circuit oscillant, à laquelle l'impédance est déterminée uniquement par la résistance ohmique. À des fréquences supérieures et inférieures à la fréquence de résonance, l'impédance est supérieure à la résistance ohmique, car soit la bobine, soit le condensateur a une réactance plus élevée. La figure [ref:a_serienschwingkreis_frequenzgang] montre la réponse en fréquence d'un circuit oscillant série, où la fréquence de résonance est clairement visible. À des fréquences supérieures et inférieures à la fréquence de résonance, nous avons donc dans le circuit oscillant série une résistance totale (impédance) élevée. À haute fréquence, la bobine a une résistance élevée. À basse fréquence, le condensateur a une résistance élevée. 

<margin>
[picture:1037:a_serienschwingkreis_frequenzgang:Réponse en fréquence d'un circuit oscillant série]
</margin>

[question:AD206]
[question:AD207] 
[question:AD204] 

Dans le cas des circuits oscillants parallèles et séries, il existe donc, comme montré ci-dessus, la relation suivante en cas de résonance :

$X_\text{C} = X_\text{L}$

Si nous insérons maintenant les formules pour les réactances de la bobine et du condensateur dans l'équation ci-dessus, nous obtenons :

$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$
  
Nous obtenons ainsi la formule : 
  
$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$

---

Cette formule s'appelle la formule de Thomson et s'applique aussi bien aux circuits oscillants parallèles qu'aux circuits oscillants séries. Dans le recueil de formules, nous la trouvons sous le thème "Circuits oscillants". Elle indique que la fréquence de résonance d'un circuit oscillant dépend uniquement de l'inductance de la bobine et de la capacité du condensateur. Les résistances ohmiques et les pertes n'ont aucune influence sur la fréquence de résonance. Avec la formule, nous pouvons calculer la fréquence de résonance des circuits oscillants. 

<indepth>
Les résistances ohmiques dans les circuits oscillants parallèles et séries influencent cependant le facteur de qualité ($Q$) et donc la bande passante ($B$) du circuit oscillant - nous y reviendrons plus en détail plus tard.
</indepth>


[question:AD208] 
[question:AD209]
[question:AD210] 

---

La fréquence de résonance des circuits oscillants parallèles est calculée exactement comme pour les circuits oscillants séries avec la formule de Thomson mentionnée précédemment. 

[question:AD211] 
[question:AD212] 

---

Pour modifier la fréquence de résonance des circuits oscillants, soit l'inductance de la bobine, soit la capacité du condensateur dans le circuit oscillant peut être modifiée.
Comme le montre la formule du circuit oscillant de Thomson, les grandeurs $L$ et $C$ se trouvent chacune sous le trait de fraction. Cela signifie qu'une augmentation de $L$ ou $C$ entraîne une réduction de la fréquence du circuit oscillant, car le dénominateur de la formule devient plus grand. En revanche, une diminution de $L$ et $C$ entraîne une augmentation de la fréquence de résonance du circuit oscillant.

<indepth>
La racine carrée n'a aucun effet sur cette relation, car la racine d'un nombre plus grand est également un nombre plus grand. La relation ici n'est cependant pas linéaire.
</indepth>

L'inductance d'une bobine peut être augmentée en augmentant le nombre de spires, en les rapprochant ou en introduisant un noyau de ferrite.
Inversement, l'inductance d'une bobine peut être réduite en réduisant le nombre de spires, en les éloignant ou en retirant un noyau de ferrite ou en introduisant un noyau de cuivre. La capacité des condensateurs peut être influencée en les échangeant ou en utilisant des condensateurs de réglage ou rotatifs.

Avec cette connaissance, nous pouvons maintenant répondre aux questions suivantes.

[question:AD213] 
[question:AD214] 
[question:AD215] 
[question:AD216] 
[question:AD217] 

Une combinaison de circuits oscillants parallèles et séries peut être utilisée comme filtre passe-bande si elle est disposée de manière appropriée. En cas de résonance, les circuits oscillants parallèles se comportent comme des résistances à haute impédance et le circuit oscillant série comme une résistance à basse impédance.

[question:AD205]

La bande passante des filtres et des passe-bandes est souvent indiquée en référence à une certaine valeur d'atténuation. L'atténuation décrit dans quelle mesure un signal est affaibli par rapport à la transmission maximale.

Habituellement, la *bande passante* d'un filtre est définie par le point dit $\qty{-3}{\dB}$.

Au point $\qty{-3}{\dB}$ :

- Seule la moitié de la puissance passe à travers le filtre
- La tension du signal est encore d'environ $0{,}7$ fois la valeur maximale

La bande passante résulte de la différence entre les fréquences de coupure supérieure et inférieure à $\qty{-3}{\dB}$:

$ B = f_\mathrm{o} - f_\mathrm{u} $

[question:AD220]

Où :

- $f_\mathrm{o}$: fréquence de coupure supérieure
- $f_\mathrm{u}$: fréquence de coupure inférieure

La bande passante $\qty{-3}{\dB}$ est utilisée pour décrire l'adéquation d'un filtre pour certains modes de fonctionnement :

- Filtre à bande étroite avec une bande passante d'environ $\qty{500}{\hertz}$ : adapté pour le CW (télégraphie)
- Filtre à bande plus large avec une bande passante d'environ $\qty{2,7}{\kilo\hertz}$ : adapté pour la transmission vocale SSB

[question:AD221] 
[question:AD222]

Pour la question suivante, il ne faut pas lire le point $\qty{-3}{\dB}$, mais la bande passante au point $\qty{-60}{\dB}$.

[question:AD219]

La qualité d'un circuit oscillant (en anglais, facteur Q) est déterminée par le rapport des réactances de la capacité et de l'inductance en cas de résonance à la résistance de perte ohmique. Si un circuit oscillant ne contenait aucune résistance de perte ohmique, son facteur Q serait infini. Les composants réels sont cependant toujours sujets à des pertes. Les inductances ont toujours une résistance de perte ohmique, les capacités ont des pertes diélectriques qui se manifestent également sous forme de résistance ohmique. Plus les résistances ohmiques dans un circuit oscillant sont grandes, plus son facteur Q est faible. Pour les filtres avec une qualité élevée et des flancs raides, on utilise souvent des filtres à quartz.

Pour le calcul du facteur Q, nous utilisons les formules correspondantes du recueil de formules selon qu'il s'agit d'un circuit oscillant parallèle ou série :

Pour le circuit oscillant série en cas de résonance ($X_\text{L} = X_\text{C}$) :

$Q = \frac{f_0}{B} = \frac{X_\text{L}}{R_\text{S}}$

Pour le circuit oscillant parallèle en cas de résonance ($X_\text{L} = X_\text{C}$) :

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD225]


---

Conformément à l'exemple de calcul ci-dessus, nous pouvons maintenant calculer le facteur de qualité du circuit oscillant parallèle. La fréquence de résonance est calculée comme dans l'exemple précédent. Il est cependant à noter que pour le calcul de $Q$, la formule pour le circuit oscillant parallèle doit être utilisée :

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD226]

La bande passante des circuits oscillants parallèles et séries peut désormais être calculée également simplement à partir de la fréquence de résonance du circuit oscillant et de son facteur de qualité comme suit (formule à cet effet dans le recueil de formules) :

$Q = \frac{f_0}{B}$

En réarrangeant la formule, nous obtenons la bande passante $B$ :

$B = \frac{f_0}{Q}$

La formule mentionnée ci-dessus s'applique à la fois au circuit oscillant série et au circuit oscillant parallèle !

[question:AD224]

En conséquence, la question suivante peut désormais être calculée étape par étape avec les connaissances décrites précédemment.
[question:AD223]

---

Pour la transmission de signaux entre les étages de circuit ainsi que dans les filtres des émetteurs et des récepteurs, on utilise souvent des circuits oscillants couplés. Dans ce cas, deux circuits oscillants sont couplés de manière inductive ou capacitive. La figure [ref:a_gekoppelte_schwingkreise] montre un couplage inductif. Ce couplage peut, selon l'application 

- *faible* (d),
- *sous-critique* (c),
- *critique* (b) ou 
- *sur-critique* (a)

trouver. Le degré de couplage détermine l'influence mutuelle et donc la bande passante et la courbe de passage de l'ensemble du dispositif.

<margin>
[picture:184:a_gekoppelte_schwingkreise:Couplage de circuits oscillants]
</margin>

En cas de couplage faible et sous-critique, il y a peu d'influence mutuelle ; En revanche, l'atténuation de passage de l'ensemble est relativement élevée et la bande passante relativement faible.

En cas de couplage critique, les deux circuits oscillants s'influencent juste assez pour qu'une courbe de passage plate avec une faible atténuation soit créée dans la plage de passage et qu'elle soit complètement plane (plateau) dans la plage de passage souhaitée. La bande passante de l'ensemble est plus grande que dans le cas d'un couplage faible et sous-critique. C'est aussi un bon moyen de reconnaître un couplage critique.

En cas de couplage sur-critique, l'influence mutuelle des deux circuits oscillants est très forte, ce qui entraîne un changement important des deux fréquences de résonance et donc une grande bande passante. Cela déforme fortement la courbe de passage dans la plage de passage et forme deux points de résonance à gauche et à droite de la fréquence centrale. La courbe de passage présente un "creux". C'est aussi un bon moyen de reconnaître le couplage sur-critique.

[question:AD227] 
[question:AD228] 
[question:AD229] 