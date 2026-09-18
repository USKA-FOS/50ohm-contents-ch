Lors du raccordement d’antennes, nous souhaitons que seule l’antenne émette ou reçoive des signaux, et non la ligne d’alimentation elle-même, qui pourrait être installée dans la maison. Pour cela, des câbles blindés, par exemple des câbles coaxiaux, conviennent bien, car dans l’idéal, ils n’émettent ni ne reçoivent d’ondes électromagnétiques par eux-mêmes. Ils transmettent le signal de manière isolée de l’environnement extérieur (par exemple, de l’installation électrique de la maison) à travers le câble.

<indepth>
Pour que le blindage d’un câble coaxial remplisse correctement sa fonction, une *condition* doit être respectée : le courant dans le conducteur intérieur doit être exactement opposé au courant dans le conducteur extérieur, et les deux courants doivent avoir la même valeur absolue. Dans ce cas, un champ n’apparaît qu’entre les deux conducteurs, et l’environnement du câble n’est pas influencé. Le conducteur extérieur ne présente alors aucune tension haute fréquence par rapport à la terre.

Inversement, cela signifie aussi que si le conducteur extérieur présente une tension haute fréquence par rapport à la terre, les courants dans le conducteur intérieur ne sont pas symétriques et le câble coaxial émet.

Les courants dans le câble coaxial doivent donc être symétriques (même valeur absolue mais signe opposé ou direction opposée), et les tensions par rapport à la terre doivent être *asymétriques* (seul le conducteur intérieur présente une tension par rapport à la terre).
</indepth>

---

Cependant, si l’on raccorde une antenne symétrique, par exemple un dipôle demi-onde, à un câble coaxial, il peut arriver que le câble coaxial émette malgré son blindage ! Cela est dû au fait que des courants haute fréquence peuvent circuler sur la surface extérieure du conducteur extérieur métallique, accompagnés d’un champ électromagnétique autour de l’isolation externe (cf. illustration [ref:e_mantelwellen]). Cet effet est appelé *courants de gaine* : ils peuvent perturber d’autres appareils dans la maison lors de l’émission, et causer des perturbations de réception, car le câble coaxial devient en quelque sorte une partie de l’antenne. Les influences perturbatrices dans la maison sont alors plus facilement captées par l’appareil radio. Les courants de gaine supplémentaires « manquent » sur l’un des deux brins du dipôle, ce qui entraîne également une déformation du diagramme de rayonnement.

[question:EG405]
[question:EG406]

L’illustration [ref:e_mantelwellen] montre comment une partie du courant, qui devrait normalement circuler vers le brin du dipôle, revient sur le blindage du câble coaxial.

<margin>
[picture:633:e_mantelwellen:courants de gaine]
</margin>

Les courants de gaine circulent effectivement en grande partie à la surface du conducteur extérieur. Cela est lié à l’*effet de peau*, qui fait que les courants haute fréquence circulent principalement à la surface des conducteurs métalliques. On peut donc considérer un câble coaxial comme un système à trois conducteurs :
  
1. Face externe du conducteur intérieur
2. Face interne du conducteur extérieur
3. Face externe du conducteur extérieur
  
Le courant sur la face externe du conducteur intérieur et le courant sur la face interne du conducteur extérieur ont toujours la même valeur absolue et sont opposés ($I_1$). Le courant sur la face externe du conducteur extérieur ($I_3$) représente le courant de gaine.

[question:EG404]

---

Les courants de gaine peuvent être évités, par exemple, en utilisant un *symétriseur*, un balun, pour relier le câble coaxial à l’antenne.

<indepth>
Le terme *balun* est une contraction des mots anglais « balanced » et « unbalanced », car il s’agit de relier une partie symétrique (par exemple, une antenne symétrique) à une partie asymétrique (le câble coaxial, où idéalement seul le conducteur intérieur présente une tension par rapport à la terre).
</indepth>

[question:EG407]

---

Une autre forme de balun consiste à enrouler un câble coaxial autour d’un noyau de ferrite. Cela constitue une *self de mode commun*, également appelée *self de mode commun*. Pour les signaux en opposition de phase, elle présente une impédance faible, car si le courant circule en sens inverse dans le conducteur intérieur par rapport au conducteur extérieur, il n’y a pas d’interaction notable avec le matériau ferrite. En revanche, pour les courants de gaine, cette structure agit comme une bobine (avec pertes).

<margin>
[photo:325:e_mantelwellendrossel:self de mode commun]
</margin>

[question:EG408]