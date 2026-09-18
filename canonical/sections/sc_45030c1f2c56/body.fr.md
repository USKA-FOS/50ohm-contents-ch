<margin>
[picture:1019:e_frequenzabhängiger_widerstand:Dépendance en fréquence des condensateurs et des bobines par rapport à une résistance classique]
[picture:1020:e_herleitung_tiefpass:Dérivation du circuit passe-bas à partir d'un diviseur de tension]
</margin>

Dans les chapitres sur les condensateurs et les bobines, nous avons déjà appris que ces deux composants possèdent une résistance dépendante de la fréquence. Le schéma [ref:e_frequenzabhängiger_widerstand] montre qualitativement que la résistance d'une résistance ohmique est indépendante de la fréquence, tandis que la résistance d'un condensateur diminue de manière hyperbolique avec l'augmentation de la fréquence et que la résistance d'une bobine augmente linéairement avec l'augmentation de la fréquence.

À partir de ces composants, on peut construire ce que l’on appelle des filtres de fréquence passifs, que nous allons examiner de plus près maintenant. Dans la première partie de ce chapitre, nous nous intéressons aux filtres simples, à savoir les filtres passe-haut et passe-bas. Ces filtres permettent de supprimer les plages de fréquences indésirables au-dessus ou en dessous d’une fréquence de coupure. Dans la deuxième partie, nous abordons ensuite des filtres plus complexes, comme par exemple les filtres passe-bande.

Nous commençons par dériver un passe-bas sous la forme d’un *circuit RC*. Le point de départ, à l’étape (1), est le circuit d’un diviseur de tension, tel qu’il est représenté dans la figure [ref:e_herleitung_tiefpass], que nous avons déjà étudié. Nous nous souvenons que pour un diviseur de tension, la relation suivante s’applique : 

$\frac{U_1}{U_2} = \frac{R_1}{R_2}$

Cela signifie par exemple : si la résistance $R_2$ est deux fois plus grande que la résistance $R_1$, alors la tension $U_2$ est également deux fois plus grande que la tension $U_1$.

À l’étape (2), nous remplaçons la résistance $R_2$ par le condensateur $C_1$. Ensuite, à l’étape (3), nous redessinons le circuit pour obtenir la représentation classique d’un passe-bas.

---

Nous retenons : un passe-bas n’est rien d’autre qu’un diviseur de tension. C’est pourquoi nous pouvons l’analyser de la même manière. Dans la figure [ref:e_wiederstaende_tiefpass], les courbes de résistance en fonction de la fréquence sont représentées à nouveau. Examinons d’abord les basses fréquences : dans ce cas, la résistance du condensateur est élevée, de sorte qu’une tension élevée apparaît en sortie. Lorsque la fréquence augmente, la résistance du condensateur diminue progressivement, et selon le principe du diviseur de tension, la tension de sortie diminue également.

C’est ainsi que l’on obtient la courbe de tension représentée dans la figure [ref:e_tiefpass_frequenzgang]. Cela explique l’idée centrale du passe-bas : les hautes fréquences sont fortement atténuées, tandis que les basses fréquences traversent le filtre presque sans atténuation. Un exemple d’application d’un passe-bas consiste à l’utiliser après des amplificateurs d’émission pour filtrer les harmoniques qui apparaissent en raison de distorsions.

<margin>
[picture:1021:e_wiederstaende_tiefpass:Comportement qualitatif des résistances dans le diviseur de tension du passe-bas]
[picture:1024:e_tiefpass_frequenzgang:Courbe qualitative de la tension $U_\text{A}$ en sortie du passe-bas]
</margin>

[question:ED208]
[question:ED201]

<indepth>
La *fréquence de coupure* ($f_\text{g}$) d'un passe-bas est la fréquence à laquelle le signal de sortie commence à être atténué de manière notable. Elle marque donc la transition entre la bande de fréquences transmise presque sans atténuation par le filtre et la zone où l'atténuation augmente de façon significative. Formellement, la fréquence de coupure est définie comme celle pour laquelle la puissance de sortie chute à la moitié de la puissance d'entrée ($\qty{-3}{\dB}$). Comme la puissance est proportionnelle au carré de la tension, cela correspond à une diminution de la tension de sortie à environ $\qty{70}{\percent}$ de sa valeur initiale ($\frac{1}{\sqrt{2}}$). En pratique, on identifie souvent la fréquence de coupure au point où la tension de sortie diminue notablement et où la réponse en fréquence commence à « plier ». En dessous de la fréquence de coupure, les basses fréquences sont transmises presque sans modification, tandis qu'au-dessus de cette fréquence, les fréquences plus élevées sont de plus en plus atténuées.
</indepth>
---
Pour un passe-haut, en revanche, ce sont les basses fréquences qui sont fortement atténuées, tandis que les hautes fréquences passent presque sans atténuation à travers ce filtre. Pour y parvenir, on échange le condensateur et la résistance comme illustré dans la figure [ref:e_wiederstaende_hochpass]. La réponse en fréquence d'un passe-haut est présentée qualitativement dans [ref:e_hochpass_frequenzgang]. Un exemple d'application d'un passe-haut est son utilisation dans un diplexeur d'antenne pour filtrer, par exemple, la bande HF avant un récepteur VHF, afin d'éviter les interférences causées par les opérations en HF.
<margin>
[picture:1025:e_wiederstaende_hochpass:Comportement qualitatif des résistances dans le diviseur de tension du passe-haut]
[picture:1022:e_hochpass_frequenzgang:Évolution qualitative de la tension $U_\text{A}$ en sortie du passe-haut]
</margin>
[question:ED211]
[question:ED202]
---
Les circuits RC simples présentent l'inconvénient d'avoir des flancs plutôt plats dans la zone de coupure. Dans un passe-bas RC, l'impédance minimale est déterminée par la résistance $R$. Cependant, cette résistance $R$ peut être remplacée par une bobine, dont le comportement en fréquence s'oppose à celui d'un condensateur. Il est donc naturel de combiner bobines et condensateurs pour créer des passe-haut et passe-bas.
Pour *les hautes fréquences, l'impédance de la bobine est élevée*, tandis que celle du condensateur est faible.
Pour *les basses fréquences, l'impédance de la bobine est faible*, tandis que celle du condensateur est élevée.
Selon le composant sur lequel la tension de sortie est mesurée, on obtient un passe-haut ou un passe-bas. En se souvenant que l'impédance de la bobine $X_\text{L}$ est également élevée à haute fréquence, il est facile d'identifier rapidement un circuit comme passe-haut ou passe-bas en observant sur quel composant la tension de sortie est mesurée.
<tip>
Pour les circuits combinant condensateur et bobine, voici une règle simple à retenir : si l'élément situé dans la branche supérieure du diviseur de tension forme un *H* droit – comme dans *H*autpass, il s'agit d'un passe-haut. Si, en revanche, c'est une résistance ou une bobine qui se trouve dans cette branche supérieure, il s'agit d'un passe-bas.
[picture:1023:e_hochpass_tipp:Astuce pour retenir]
</tip>
[question:ED209]
[question:ED212]
---
Dans les questions suivantes, il s'agit d'une application pratique de nos filtres. Bien sûr, plusieurs composants dépendant de la fréquence peuvent être utilisés dans un même circuit, ce qui permet d'obtenir une transition plus abrupte dans la zone de la fréquence de coupure. Le type de circuit utilisé dans les deux questions suivantes devrait maintenant être facile à identifier grâce à l'astuce donnée. 

[question:ED210]
[question:ED213] 

Un autre exemple pratique de l'enchaînement de bobines et de condensateurs en tant que filtre est le diplexeur, expliqué en marge. 

<indepth>
*Exemple pratique de diplexeur :* Les passe-haut et passe-bas passifs sont également utilisés dans les séparateurs de fréquences. Dans l'exemple ci-dessous, on peut voir un circuit pour un diplexeur dit pour $\qty{2}{\meter}$ et $\qty{70}{\centi\meter}$. Celui-ci peut être utilisé, par exemple, pour connecter un appareil radio $\qty{2}{\meter}$ et un appareil radio $\qty{70}{\centi\meter}$ à une antenne commune duplex. Inversement, on pourrait aussi utiliser des antennes séparées pour $\qty{2}{\meter}$ et $\qty{70}{\centi\meter}$ avec un appareil radio VHF duplex, par exemple pour utiliser un antenne omnidirectionnelle en direct sur $\qty{2}{\meter}$ et une antenne directionnelle pour le relais sur $\qty{70}{\centi\meter}$. 
En amont de la sortie $\qty{2}{\meter}$, on trouve un passe-bas, et en amont de la sortie $\qty{70}{\centi\meter}$, un passe-haut — chacun composé de 5 composants dépendant de la fréquence. 
[picture:939:e_circuit_diplexer:Schéma du diplexeur $\qty{2}{\meter}$/$\qty{70}{\centi\meter}$]
[photo:171:e_example_diplexer:Exemple de montage]
</indepth>

<indepth>
*Deux termes similaires, mais qui désignent des concepts différents :*
  
Un *diplexeur* sépare ou combine différentes plages de fréquences, comme décrit ci-dessus. 

Un *duplexeur* permet d'émettre et de recevoir simultanément sur la même antenne, même si l'émetteur et le récepteur fonctionnent sur des fréquences proches, comme par exemple dans le cas des relais FM. En Suisse, le [groupe UHF HB9UF](https://www.hb9uf.ch/) exploite, entre autres, de telles stations relais ou "répéteurs", comme on les appelle en anglais.

</indepth>

<indepth>
[photo:320:e_tiefpass_selbstbau:Filtre passe-bas auto-construit]
Les filtres mentionnés ci-dessus peuvent bien sûr être calculés et construits soi-même pour toutes les plages de fréquences. Le recueil de formules contient les formules nécessaires, mais il existe également de nombreuses propositions de construction et programmes de calcul. Les bobines requises peuvent souvent être facilement fabriquées soi-même. Pour cela, un petit stock de fil de cuivre émaillé de $\qty{0,8}{\milli\meter}$ suffit pour des bobines à air stables avec de petites valeurs d'inductance. Pour des valeurs d'inductance plus élevées, par exemple pour les bandes HF, on peut utiliser du fil de cuivre émaillé de $\qty{0,2}{\milli\meter}$ et des noyaux magnétiques avec des valeurs $A_\text{L}$ appropriées, afin de pouvoir fabriquer soi-même les valeurs correctes à tout moment. Les dimensions nécessaires, le nombre de spires, etc. peuvent généralement être facilement déterminés à l'aide du recueil de formules, des propositions de construction ou des programmes de calcul.
</indepth>  

---

Nous avons maintenant découvert des éléments RC et LC simples en tant que filtres passe-haut et passe-bas. Cependant, il est possible de réaliser d'autres types de filtres à partir de bobines et de condensateurs, qui vont au-delà des simples filtres passe-haut et passe-bas. Nous allons maintenant examiner de plus près ces éléments, à savoir les *circuits oscillants*.

<margin>
[image:1026:e_rp_schwingkreis:(a) Circuit oscillant série (b) Circuit oscillant parallèle]
</margin>

Dans les circuits oscillants, la bobine et le condensateur sont disposés – selon l'effet de filtrage souhaité – de manière à présenter une résistance particulièrement élevée ou particulièrement faible à une fréquence donnée. Cela permet d'atténuer ou de laisser passer sélectivement les fréquences supérieures ou inférieures à cette fréquence.

La disposition de la bobine et du condensateur peut se faire soit en série, soit en parallèle. On distingue ainsi les circuits oscillants série (a) et les circuits oscillants parallèle (b), comme illustré dans la figure [ref:e_rp_schwingkreis].

---

Si l'on branche une bobine et un condensateur en parallèle et qu'on applique par exemple une impulsion rectangulaire à cet ensemble, celui-ci entre en oscillation. Le condensateur chargé stocke alors de l'énergie dans son champ électrique, qui se décharge ensuite à travers la bobine. Le courant traversant la bobine génère un champ magnétique qui s'oppose au flux de courant. Une fois le champ magnétique établi, le condensateur se décharge complètement. L'énergie est alors stockée dans le champ magnétique de la bobine. Cependant, comme le condensateur ne peut plus se décharger ni maintenir le flux de courant, le champ magnétique ne peut être maintenu. Le champ magnétique de la bobine se décharge alors et génère une tension dans le sens inverse. Cette tension recharge le condensateur dans le sens inverse jusqu'à ce que le champ magnétique de la bobine soit dissipé et ne puisse plus s'opposer au champ électrique dans le condensateur. Le processus recommence ensuite.

<margin>
[include:applet_schwingkreis]
</margin>

---

C'est pourquoi on parle de circuit oscillant. La fréquence à laquelle ce circuit oscille est appelée *fréquence de résonance* ($f_0$). Elle est comparable à la fréquence de résonance d'un diapason mis en vibration par un choc. En cas de résonance, les impédances de la bobine $X_\text{L}$ et du condensateur $X_\text{C}$ sont de même valeur. Ces circuits oscillants peuvent être utilisés d'une part pour générer des oscillations, ce que nous examinerons plus en détail dans le chapitre sur les oscillateurs. D'autre part, ils peuvent également servir de filtres – et c'est précisément le sujet de ce chapitre.

<margin>
[image:1037:e_rsk_frequenzgang:Réponse en fréquence qualitative d'un circuit oscillant série]
</margin>

---

Dans un *circuit résonant série* ou *circuit oscillant en série* comme illustré à la figure [ref:e_rp_schwingkreis]a, la résistance totale est minimale à la résonance. La figure [ref:e_rsk_frequenzgang] montre la réponse en fréquence. Pour des fréquences supérieures à la fréquence de résonance, la résistance de la bobine augmente, ce qui fait également augmenter la résistance totale du circuit résonant série. Le même phénomène se produit pour des fréquences inférieures à la fréquence de résonance, mais ici c'est la résistance du condensateur qui devient élevée. Dans les circuits résonants série, la résistance est donc minimale à la fréquence de résonance. En raison de la connexion en série, c'est le composant ayant la résistance la plus élevée qui détermine l'impédance du circuit résonant pour les fréquences éloignées de la résonance.

<indepth>
La réponse en fréquence en valeur absolue d'un circuit résonant série composé d'une résistance, d'une bobine et d'un condensateur se calcule selon la formule suivante :
  
$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$
  
À la résonance, lorsque $X_\text{C} = X_\text{L}$, il ne reste que la résistance $R$. Dans le cas idéal, si la résistance $R=\qty{0}{\ohm}$, la résistance est même nulle. En substituant les valeurs de $X_\text{L}$ et $X_\text{C}$, on obtient :
  
$Z = \sqrt{R^2+\left(2\pi f \cdot L~-~\frac{1}{2\pi f \cdot C} \right)^2}$
  
Dans cette formule, on peut très bien observer la réponse en fréquence de la figure [ref:e_rsk_frequenzgang] : si l'on fait tendre la fréquence vers $\qty{0}{\hertz}$, la contribution de la bobine disparaît et seul le condensateur agit. Si l'on fait tendre la fréquence vers l'infini, seule la bobine agit et la contribution du condensateur disparaît.
  
On peut même calculer la fréquence de résonance. Si $X_\text{L} = X_\text{C}$, on peut résoudre la formule pour $f$ :
  
$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$
  
On obtient ainsi la formule :
  
$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$
  
La dérivation exacte des formules peut être consultée, par exemple, sur [Wikipedia](https://50ohm.de/schwk). Il convient de mentionner à ce stade que tous les réponses en fréquence sont représentés qualitativement et peuvent, en réalité, présenter des différences.
</indepth>

[question:ED205]

---

Si l'on associe un condensateur et une bobine pour former un *circuit résonant parallèle*, comme illustré dans la figure [ref:e_rp_schwingkreis]b, le comportement est exactement inverse : l'impédance *$Z$* est alors très élevée à la fréquence de résonance, cf. figure [ref:e_psk_frequenzgang]. Cependant, pour des fréquences supérieures à la fréquence de résonance, le condensateur présente une faible impédance, ce qui réduit l'impédance de ce circuit résonant. Pour des fréquences inférieures à la fréquence de résonance, c'est la bobine qui présente une faible impédance, réduisant également l'impédance du circuit résonant. 
Dans les circuits résonants parallèles, l'impédance est donc maximale à la fréquence de résonance. Pour des fréquences éloignées de la résonance, c'est le composant présentant la plus faible impédance qui détermine l'impédance du circuit résonant parallèle.

<margin>
[picture:1036:e_psk_frequenzgang:Réponse en fréquence qualitative d'un circuit résonant parallèle]
</margin>

[question:ED206] 
[question:ED207]

% TODO ////

Selon la manière dont les circuits résonants parallèles et séries sont intégrés dans le trajet du signal, il est possible d'atténuer ou de filtrer certaines plages de fréquences. Pour cela, nous allons à nouveau utiliser notre approche du diviseur de tension.

---

Commençons par les circuits pour les *circuits bouchons*. Il existe deux façons de les concevoir en tant que diviseurs de tension : premièrement, le *circuit bouchon* (cf. figure [ref:e_saugkreis]) et deuxièmement le *circuit bouchon* (cf. figure [ref:e_sperrkreis]). Les figures montrent respectivement la résistance dépendante de la fréquence ainsi que la tension de sortie. À l’aide de nos règles connues sur le diviseur de tension, ces relations peuvent être dérivées et comprises de manière tout à fait analogue aux circuits RC traités précédemment. Comme les circuits oscillants parallèles présentent une résistance élevée à la résonance, ils peuvent être utilisés efficacement en tant que circuit bouchon en série dans le trajet du signal. Ou bien on utilise la faible résistance de résonance d’un circuit oscillant série en parallèle avec le trajet du signal comme circuit bouchon. Cependant, il est fréquent que les deux soient combinés. Une application des circuits bouchons consiste par exemple à supprimer certaines plages de fréquences, par exemple lorsqu’un émetteur radio FM proche perturbe la réception.

[question:ED204]
[question:ED214]
[question:ED215]

<margin>
[picture:1038:e_saugkreis:Évolutions qualitatives de la fréquence d’un circuit bouchon]
[picture:1040:e_sperrkreis:Évolutions qualitatives de la fréquence d’un circuit bouchon]
</margin>

---

La deuxième catégorie de circuits que l’on peut concevoir à partir de circuits oscillants est celle des *passe-bande*. Ici aussi, il existe deux façons de les concevoir en tant que diviseurs de tension : premièrement le *circuit passe-bande* (cf. figure [ref:e_leitkreis]) et deuxièmement le *passe-bande* (cf. figure [ref:e_bandpass]). La dérivation s’effectue ici également selon le comportement d’un diviseur de tension. Pour un passe-bande, on place des circuits oscillants parallèles en parallèle avec le trajet du signal, car ceux-ci présentent une faible résistance pour les fréquences éloignées de la résonance et « court-circuitent » ainsi ces fréquences. Un circuit oscillant série en série dans le trajet du signal provoque une atténuation supplémentaire pour les fréquences éloignées de la résonance, tandis qu’il présente une faible résistance à la fréquence souhaitée.

[question:ED203]

<margin>
[picture:1039:e_leitkreis:Évolutions qualitatives de la fréquence d’un circuit passe-bande]
[picture:1041:e_bandpass:Évolutions qualitatives de la fréquence d’un passe-bande]
</margin>

Un exemple d’application évident des passe-bande est leur utilisation dans les récepteurs, où un pré-filtrage de certaines plages de fréquences est nécessaire. Dans ce cas, on utilise un filtre qui ne laisse passer qu’une plage de fréquences souhaitée, tandis que toutes les autres fréquences sont atténuées. De tels passe-bande se trouvent donc dans presque tous les récepteurs, souvent même séparément pour chaque bande HF individuelle. Conçus pour des puissances élevées, les passe-bande sont également utilisés en fonctionnement en émission, par exemple lors de concours ou de Fielddays, afin de minimiser les interférences mutuelles entre stations voisines.

Pour concevoir des passe-bande et des circuits bouchons, on peut donc utiliser aussi bien des circuits oscillants séries que parallèles. L’essentiel est de tenir compte du comportement des circuits oscillants respectifs en cas de résonance. Selon leur comportement, ils peuvent être placés en série ou en parallèle dans le trajet du signal, éventuellement combinés plusieurs fois entre eux.

Pour les filtres, seuls certains types de condensateurs adaptés peuvent être utilisés.
Les condensateurs électrolytiques ne conviennent pas aux circuits HF, car leur capacité dépend fortement de la fréquence et, en outre, ils présentent une résistance interne élevée aux fréquences élevées. Les condensateurs à film ne conviennent pas non plus, car en raison de leurs enroulements (inductance propre), leur capacité dépend fortement de la fréquence à partir de la bande HF et leur facteur de qualité est médiocre. 
En revanche, les condensateurs céramiques présentent de faibles pertes et leur capacité dépend peu de la fréquence et de la température. De plus, ils sont faciles à se procurer même pour des tensions élevées.
Les condensateurs à plaques avec l’air comme isolant conviennent également ; on les trouve surtout sous forme de condensateurs variables. Pour les hautes tensions, les condensateurs variables sont également utilisés dans les syntoniseurs d’antenne.

[question:ED216]
