<margin>
[picture:1019:e_frequenzabhängiger_widerstand:Fréquence dépendante de la résistance des condensateurs et des bobines en comparaison avec une résistance classique]
[picture:1020:e_herleitung_tiefpass:Déduction du circuit passe-bas à partir d'un diviseur de tension]
</margin>

Dans les chapitres consacrés aux condensateurs et aux bobines, nous avons déjà appris que ces deux composants possèdent une résistance dépendante de la fréquence. La figure [ref:e_frequenzabhängiger_widerstand] montre qualitativement que la résistance d'une résistance ohmique est indépendante de la fréquence, tandis que la résistance d'un condensateur diminue hyperboliquement avec l'augmentation de la fréquence et que la résistance d'une bobine augmente linéairement avec l'augmentation de la fréquence.

À partir de ces composants, on peut construire des filtres de fréquence passifs appelés, que nous allons examiner de plus près. Dans la première partie de ce chapitre, nous nous occupons de filtres simples, à savoir les passe-haut et les passe-bas. Avec ces filtres, on peut supprimer les plages de fréquences indésirables au-dessus ou en dessous d'une fréquence de coupure. Dans la deuxième partie, nous nous consacrons ensuite à des filtres plus complexes, comme par exemple les passe-bande.

Nous commençons par la dérivation d'un filtre passe-bas en tant que ce qu'on appelle un *élément RC*. Le point de départ est l'étape (1) du circuit d'un diviseur de tension, comme le montre la figure [ref:e_herleitung_tiefpass] et que nous avons déjà rencontré. Nous nous souvenons que pour un diviseur de tension, ce qui suit s'applique :$\frac{U_1}{U_2} = \frac{R_1}{R_2}$Cela signifie par exemple : si la résistance $R_2$ est deux fois plus grande que la résistance $R_1$, alors la tension $U_2$ est également deux fois plus grande que la tension $U_1$.À l'étape (2), nous remplaçons la résistance $R_2$ par le condensateur $C_1$. Ensuite, nous dessinons le circuit à l'étape (3) encore un peu, de sorte que nous obtenons la représentation habituelle d'un filtre passe-bas.---

Nous retenons : un filtre passe-bas n'est au départ rien d'autre qu'un diviseur de tension. C'est pourquoi nous pouvons le considérer de la même manière par la suite. Dans la figure [ref:e_wiederstaende_tiefpass], les variations de résistance en fonction de la fréquence sont encore représentées. Examinons d'abord les fréquences basses : dans ce cas, la résistance du condensateur est grande, de sorte qu'une tension élevée est appliquée à la sortie. Si la fréquence augmente, la résistance du condensateur devient de plus en plus petite, et selon le principe du diviseur de tension, la tension de sortie diminue également.De cette manière, on obtient la courbe de tension, comme le montre la figure [ref:e_tiefpass_frequenzgang]. Ainsi, l'idée centrale du filtre passe-bas est également expliquée : les hautes fréquences sont fortement atténuées, tandis que les basses fréquences traversent le filtre largement sans obstacle. Un exemple d'application d'un filtre passe-bas est son utilisation derrière les amplificateurs d'émission pour filtrer les harmoniques supérieures qui apparaissent par les distorsions.<margin>
[picture:1021:e_wiederstaende_tiefpass:Comportement qualitatif de la résistance dans le diviseur de tension passe-bas]
[picture:1024:e_tiefpass_frequenzgang:Courbe de tension qualitative $U_\text{A}$ au filtre passe-bas]
</margin>

[question:ED208]
[question:ED201]

<indepth>
La *fréquence de coupure* ($f_\text{g}$) d'un filtre passe-bas est la fréquence à laquelle le signal de sortie commence à être notablement affaibli. Elle marque donc la transition entre la bande de fréquences qui est largement transmise par le filtre sans obstacle et la zone dans laquelle l'atténuation augmente considérablement. Formellement, la fréquence de coupure est définie de telle sorte que, à cette fréquence, la puissance de sortie est réduite de moitié par rapport à la puissance d'entrée ($\qty{-3}{\dB}$). Comme la puissance est proportionnelle au carré de la tension, cela correspond à une diminution de la tension de sortie à environ $\qty{70}{\percent}$ de sa valeur initiale ($\frac{1}{\sqrt{2}}$). En pratique, on reconnaît donc souvent la fréquence de coupure au point où la tension de sortie devient nettement plus petite et où la courbe de réponse en fréquence commence à « s'infléchir ». En dessous de la fréquence de coupure, les basses fréquences sont transmises presque sans changement, au-dessus de la fréquence de coupure, les fréquences plus élevées sont de plus en plus atténuées.
</indepth>

---

Dans le cas d'un filtre passe-haut, en revanche, les basses fréquences sont fortement atténuées, tandis que les hautes fréquences traversent ce filtre à peine atténuées. Cela est réalisé en échangeant le condensateur et la résistance comme le montre la figure [ref:e_wiederstaende_hochpass]. La réponse en fréquence d'un filtre passe-haut est qualitativement représentée dans [ref:e_hochpass_frequenzgang]. Un exemple d'application d'un filtre passe-haut est son utilisation dans un filtre de séparation d'antenne, par exemple pour filtrer la bande des ondes courtes devant un récepteur FM afin d'éviter les perturbations dues à l'exploitation des ondes courtes.<margin>
[picture:1025:e_wiederstaende_hochpass:Comportement qualitatif de la résistance dans le diviseur de tension passe-haut]
[picture:1022:e_hochpass_frequenzgang:Courbe de tension qualitative $U_\text{A}$ au filtre passe-haut]
</margin>

[question:ED211]
[question:ED202]

---

Les simples éléments RC présentent l'inconvénient que leurs flancs dans la zone limite sont plutôt plats. La plus petite impédance d'un filtre passe-bas RC est déterminée par la résistance $R$. La résistance $R$ peut cependant être remplacée par une bobine qui se comporte de manière opposée à un condensateur en termes de comportement en fréquence. Il est donc logique de combiner des bobines et des condensateurs pour des filtres passe-haut et passe-bas. 
À *hautes fréquences, la résistance de la bobine est élevée*, tandis que la résistance du condensateur est faible.
À *basses fréquences, la résistance de la bobine est faible*, tandis que la résistance du condensateur est élevée. 
Selon que la tension de sortie est mesurée via quel composant, on obtient un filtre passe-haut ou un filtre passe-bas. Si l'on se souvient que la résistance de la bobine $X_\text{L}$ est également élevée à haute fréquence, un circuit peut être rapidement identifié comme un filtre passe-haut ou passe-bas, si l'on regarde sur quel composant la tension de sortie est mesurée.<tip>
Même pour les circuits avec condensateur et bobine, la règle suivante s'applique : s'il s'agit d'une *H* droite dans la branche supérieure du diviseur de tension - comme dans *H*ochpass, alors il s'agit d'un filtre passe-haut. Si, en revanche, il y a une résistance ou une bobine dans la branche supérieure, il s'agit d'un filtre passe-bas.
[picture:1023:e_hochpass_tipp:Astuce pour se souvenir]
</tip>

[question:ED209]
[question:ED212]

---

Dans les questions suivantes, il s'agit d'une application pratique de nos filtres. Bien sûr, plusieurs composants dépendant de la fréquence peuvent également être utilisés dans un circuit, de sorte que la transition dans la zone de la fréquence de coupure devient à flancs raides. Quelle est la configuration utilisée dans les deux questions suivantes, vous devriez maintenant la reconnaître facilement avec le conseil mentionné.[question:ED210]
[question:ED213] 

Un autre exemple pratique d'une combinaison de bobines et de condensateurs en tant que filtres est le diplexeur expliqué en marge.<indepth>
*Exemple pratique du diplexeur :* Les filtres passe-haut et passe-bas passifs sont également utilisés dans les séparateurs de fréquence. Dans l'exemple ci-dessous, un circuit pour un diplexeur pour $\qty{2}{\meter}$ et $\qty{70}{\centi\meter}$ est représenté. Celui-ci peut être utilisé, par exemple, pour utiliser un appareil radio $\qty{2}{\meter}$ et un appareil radio $\qty{70}{\centi\meter}$ sur une antenne commune Duoband. Inversement, on pourrait également utiliser des antennes séparées pour $\qty{2}{\meter}$ et $\qty{70}{\centi\meter}$ sur un appareil Duoband UHF, par exemple pour utiliser un radiateur omnidirectionnel pour le trafic direct $\qty{2}{\meter}$ et une antenne directionnelle pour le trafic relais $\qty{70}{\centi\meter}$. 
Un filtre passe-bas est placé devant la sortie $\qty{2}{\meter}$, un filtre passe-haut devant la sortie $\qty{70}{\centi\meter}$ - chacun combiné à 5 composants dépendant de la fréquence. 
[picture:939:e_circuit_diplexer:Schéma du diplexeur $\qty{2}{\meter}$-/$\qty{70}{\centi\meter}$]
[photo:171:e_example_diplexer:Exemple de construction]
</indepth>

<indepth>
[photo:320:e_tiefpass_selbstbau:Filtre passe-bas fait maison]
Les filtres mentionnés ci-dessus peuvent bien sûr être calculés et construits pour toutes les bandes de fréquences. Dans le recueil de formules, on trouve les formules nécessaires, mais il existe également de nombreuses propositions de construction et programmes de calcul. Les bobines nécessaires peuvent souvent être fabriquées facilement. Pour les petites valeurs d'inductance, un petit stock de fil de cuivre émaillé de $\qty{0,8}{\milli\meter}$ suffit pour des bobines d'air stables. Pour les grandes valeurs d'inductance, par exemple pour les bandes de fréquences courtes, on peut utiliser du fil de cuivre émaillé de $\qty{0,2}{\milli\meter}$ et du matériau de noyau avec des valeurs $A_\text{L}$ correspondantes, afin de pouvoir fabriquer soi-même les valeurs appropriées à tout moment. Les tailles, les enroulements, etc. nécessaires sont généralement faciles à obtenir grâce au recueil de formules, aux propositions de construction ou aux programmes de calcul.
</indepth>  

---

Nous avons maintenant appris les éléments RC et LC simples en tant que filtres passe-haut et passe-bas. Cependant, à partir de condensateurs et de bobines, on peut encore réaliser d'autres types de filtres qui vont au-delà des simples passe-haut et passe-bas. C'est ce que nous allons examiner de plus près dans la deuxième partie, à savoir les soi-disant *circuits oscillants*.

<margin>
[picture:1026:e_rp_schwingkreis:(a) Circuit oscillant en série (b) Circuit oscillant en parallèle]
</margin>

Dans les circuits oscillants, la bobine et le condensateur sont disposés – selon l'effet de filtrage souhaité – de telle sorte qu'une résistance particulièrement élevée ou particulièrement faible se produit à une certaine fréquence. Ainsi, les fréquences au-dessus ou en dessous de cette fréquence sont atténuées ou transmises de manière ciblée.

La disposition de la bobine et du condensateur peut se faire soit en série, soit en parallèle. On distingue donc les circuits oscillants en série (a) et les circuits oscillants en parallèle (b), comme représenté dans la figure [ref:e_rp_schwingkreis]. 

---

Si l'on connecte la bobine et le condensateur en parallèle et que l'on applique, par exemple, une impulsion rectangulaire à cet arrangement, celui-ci entre en oscillation. Le condensateur chargé a maintenant de l'énergie stockée dans le champ électrique, qui se décharge cependant à travers la bobine. Le flux de courant à travers la bobine crée un champ magnétique qui s'oppose d'abord au flux de courant. Dès que le champ magnétique est établi, le condensateur se décharge complètement. L'énergie est maintenant stockée dans le champ magnétique de la bobine. Comme le condensateur ne peut plus se décharger et ne peut plus maintenir le flux de courant, le champ magnétique ne peut pas être maintenu. Le champ magnétique de la bobine se décharge et génère une tension dans la direction opposée. Cette tension charge maintenant le condensateur dans la direction opposée, jusqu'à ce que le champ magnétique dans la bobine soit dissipé et ne puisse plus s'opposer au champ électrique dans le condensateur. Le processus recommence ensuite. 

<margin>
[include:applet_schwingkreis]
</margin>

---

C'est pourquoi on parle de circuit oscillant. La fréquence à laquelle ce circuit oscillant oscille est appelée fréquence de résonance ($f_0$). Elle est comparable à la fréquence de résonance d'un diapason qui est mis en oscillation par un coup. En cas de résonance, les résistances de la bobine $X_\text{L}$ et du condensateur $X_\text{C}$ sont égales. De tels circuits oscillants peuvent être utilisés d'une part pour la génération d'oscillations, ce que nous examinerons plus en détail dans le chapitre sur les oscillateurs. D'autre part, ils peuvent également être utilisés comme filtres – et c'est précisément le sujet de ce chapitre.

<margin>
[picture:1037:e_rsk_frequenzgang:Réponse en fréquence qualitative d'un circuit oscillant en série]
</margin>

---

Dans un *circuit oscillant en série* ou *circuit oscillant en série* comme dans la figure [ref:e_rp_schwingkreis]a, la résistance totale est la plus faible en cas de résonance. La figure [ref:e_rsk_frequenzgang] montre la réponse en fréquence. À des fréquences supérieures à la fréquence de résonance, la résistance de la bobine augmente, de sorte que la résistance totale du circuit oscillant en série augmente également. Il en va de même pour les fréquences inférieures à la fréquence de résonance, mais ici, c'est la résistance du condensateur qui est grande. Dans les circuits oscillants en série, la résistance est donc la plus faible à la fréquence de résonance. Dans le cas d'un circuit oscillant en série, c'est le composant ayant la plus grande résistance qui détermine l'impédance du circuit oscillant à des fréquences éloignées de la fréquence de résonance.

<indepth>
La réponse en fréquence d'un circuit oscillant en série composé d'une résistance, d'une bobine et d'un condensateur se calcule selon la formule suivante:
  
$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$
  
En cas de résonance, lorsque $X_\text{C}$ = $X_\text{L}$, il ne reste que la résistance $R$. Dans le cas idéal, lorsque la résistance $R=\qty{0}{\ohm}$, la résistance est même nulle. Si nous insérons les valeurs pour $X_\text{L}$ et $X_\text{C}$, nous obtenons:
  
$Z = \sqrt{R^2+\left(2\pi f \cdot L~-~\frac{1}{2\pi f \cdot C} \right)^2}$
  
Dans la formule, on peut très bien voir la réponse en fréquence de la figure [ref:e_rsk_frequenzgang] : si l'on fait tendre la fréquence vers $\qty{0}{\hertz}$, alors la partie de la bobine disparaît et seul le condensateur agit. Si l'on fait tendre la fréquence vers l'infini, alors seule la bobine agit et la partie du condensateur disparaît.
  
On peut même calculer la fréquence de résonance. Si $X_\text{L} = X_\text{C}$ est valable, on peut résoudre la formule pour $f$:
  
$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$
  
On obtient ainsi la formule : 
  
$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$
  
La dérivation exacte des formules peut être lue, par exemple, sur [Wikipedia](https://50ohm.de/schwk). Il doit être mentionné à ce stade que toutes les réponses en fréquence sont tracées qualitativement et peuvent éventuellement avoir un aspect différent dans la réalité.
</indepth>

[question:ED205]

---

Si l'on combine le condensateur et la bobine en un *circuit oscillant en parallèle*, comme dans la figure [ref:e_rp_schwingkreis]b, il en va tout autrement : la résistance *$Z$* est très élevée à la fréquence de résonance, cf. figure [ref:e_psk_frequenzgang]. À des fréquences supérieures à la fréquence de résonance, le condensateur a cependant une faible résistance, de sorte que la résistance de ce circuit oscillant diminue. À des fréquences inférieures à la fréquence de résonance, la bobine a en revanche une faible résistance, de sorte que la résistance du circuit oscillant diminue également à des fréquences plus faibles. 
Dans les circuits oscillants en parallèle, la résistance est donc la plus élevée à la fréquence de résonance. À des fréquences éloignées de la fréquence de résonance, c'est le composant ayant la plus faible résistance qui détermine l'impédance du circuit oscillant en parallèle. 

<margin>
[picture:1036:e_psk_frequenzgang:Réponse en fréquence qualitative d'un circuit oscillant en parallèle]
</margin>

[question:ED206] 
[question:ED207]

% TODO ////

Selon la manière dont les circuits oscillants en parallèle et en série sont utilisés dans le chemin du signal, il est désormais possible d'atténuer ou de filtrer des plages de fréquences. Pour ce faire, nous voulons à nouveau utiliser notre approche de diviseur de tension.

---

Commençons par les circuits pour les *filtres coupe-bande*. Il existe deux possibilités de les construire comme diviseurs de tension : d'une part le *circuit bouchon* (voir figure [ref:e_saugkreis]) et d'autre part le *circuit bouchon* (voir figure [ref:e_sperrkreis]). Dans les figures, la résistance dépendante de la fréquence ainsi que la tension de sortie sont représentées. À l'aide de nos règles connues sur le diviseur de tension, ces relations peuvent être dérivées et comprises de manière tout à fait analogue aux éléments RC traités précédemment. Parce que les circuits oscillants parallèles ont une résistance élevée à la résonance, ceux-ci peuvent être utilisés efficacement comme circuit bouchon en série dans le chemin du signal. Ou bien, on utilise la faible résistance de résonance d'un circuit oscillant en série en parallèle avec le chemin du signal comme circuit bouchon. Souvent, cependant, les deux sont utilisés en combinaison. Une application pour les filtres coupe-bande est, par exemple, la suppression de certaines plages de bandes, par exemple lorsqu'un émetteur radio FM proche perturbe la réception.

[question:ED204]
[question:ED214] 
[question:ED215]

<margin>
[picture:1038:e_saugkreis:Comportements qualitatifs en fréquence d'un circuit bouchon]
[picture:1040:e_sperrkreis:Comportements qualitatifs en fréquence d'un circuit bouchon]
</margin>

---

La deuxième catégorie de circuits que l'on peut développer à partir de circuits oscillants sont les *passe-bandes*. Ici, il existe également deux possibilités de les construire comme diviseurs de tension : d'une part le *circuit bouchon* (voir figure [ref:e_leitkreis]) et d'autre part le *passe-bande* (voir figure [ref:e_bandpass]). Ici aussi, la dérivation se fait comme d'habitude par le comportement d'un diviseur de tension. Pour un passe-bande, on place des circuits oscillants parallèles en parallèle avec le chemin du signal, car ceux-ci ont une faible résistance pour les fréquences éloignées de la résonance et les "court-circuitent" en quelque sorte. Un circuit oscillant en série dans le chemin du signal assure une atténuation supplémentaire en dehors de la résonance, tandis que celui-ci a une faible résistance à la fréquence souhaitée.

[question:ED203]

<margin>
[picture:1039:e_leitkreis:Comportements qualitatifs en fréquence d'un circuit bouchon]
[picture:1041:e_bandpass:Comportements qualitatifs en fréquence d'un passe-bande]
</margin>

Un exemple d'application évident pour les passe-bandes est leur utilisation dans les récepteurs, où un préfiltre de certaines bandes de fréquences est nécessaire. Dans ce cas, un filtre est utilisé qui ne laisse passer qu'une bande de fréquences souhaitée, tandis que toutes les autres fréquences sont atténuées. De tels passe-bandes se trouvent donc dans presque tous les récepteurs, souvent même séparément pour chaque bande d'ondes courtes individuelle. Conçus pour des puissances suffisamment élevées, les passe-bandes sont également utilisés en mode émission, par exemple lors de contests communs ou de fielddays, afin de minimiser les perturbations mutuelles entre les stations voisines.

Pour construire des passe-bandes et des filtres coupe-bande, on peut donc utiliser à la fois des circuits oscillants en série et en parallèle. Il est décisif de noter comment les circuits oscillants respectifs se comportent en cas de résonance. En fonction de leur comportement, ceux-ci peuvent être placés en série dans le chemin du signal ou en parallèle avec celui-ci - éventuellement même combinés plusieurs fois entre eux. 

Dans les filtres, seuls certains types de condensateurs appropriés peuvent être utilisés.
Les condensateurs électrolytiques ne conviennent pas, par exemple, pour les circuits HF, car leur capacité est d'une part fortement dépendante de la fréquence, d'autre part parce qu'ils ont une résistance interne élevée à haute fréquence. Les condensateurs à film ne conviennent pas, car ceux-ci, en raison de leurs enroulements (inductance propre), sont particulièrement dépendants de la fréquence à partir de la bande des ondes courtes et ont une mauvaise qualité. 
Les condensateurs céramiques ont en revanche peu de pertes et la capacité n'est que peu dépendante de la fréquence et de la température. De plus, ceux-ci sont également faciles à obtenir pour de grandes tensions.
Les condensateurs appropriés sont également ceux à plaques et à air comme isolant, que l'on rencontre le plus souvent sous forme de condensateurs rotatifs. Pour les hautes tensions, les condensateurs rotatifs sont également utilisés dans les accordeurs d'antenne.

[question:ED216]