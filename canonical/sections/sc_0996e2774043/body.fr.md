Lors du raccordement des antennes, nous souhaitons atteindre que seule l'antenne émette ou reçoive des signaux, et non la ligne d'alimentation elle-même, qui pourrait être installée dans la maison. Pour cela, des lignes blindées, par exemple des lignes coaxiales usuelles, conviennent, car celles-ci n'émettent ou ne reçoivent idéalement pas d'ondes électromagnétiques, mais conduisent le signal à travers le câble, isolé du monde extérieur (par exemple de l'électricité domestique).

<indepth>
Pour que le blindage d'un câble coaxial remplisse également la fonction souhaitée, une *condition* doit être remplie : le courant dans le conducteur intérieur doit être exactement opposé au courant dans le conducteur extérieur et les deux courants doivent avoir la même valeur. Dans ce cas, un champ n'est créé qu'entre les deux conducteurs, et l'environnement du câble n'est pas influencé. Le conducteur extérieur ne présente alors aucune tension haute fréquence par rapport à la terre.

Inversement, cela signifie également : si le conducteur extérieur présente une tension haute fréquence par rapport à la terre, alors les courants dans le conducteur intérieur ne sont pas symétriques et le câble coaxial émet.

Les courants dans le câble coaxial doivent donc être symétriques (même valeur mais signe opposé ou direction opposée) et les tensions par rapport à la terre doivent être *asymétriques* (seul le conducteur intérieur conduit une tension par rapport à la terre).
</indepth>

---

Cependant, si l'on connecte une antenne symétrique, par exemple un dipôle demi-onde, à un câble coaxial, il peut arriver que le câble coaxial émet malgré le blindage ! Cela est dû au fait que des courants haute fréquence peuvent circuler sur la surface du côté extérieur du conducteur extérieur métallique, accompagnés d'un champ électromagnétique autour de l'isolation extérieure (voir figure [ref:e_mantelwellen]). Nous désignons cet effet par *ondes de gaine*, qui peuvent perturber d'autres appareils dans la maison lors de l'émission, mais aussi entraîner des perturbations de réception, car le câble coaxial devient en quelque sorte une partie de l'antenne et les influences perturbatrices dans la maison peuvent alors être plus facilement captées par l'appareil radio. Les courants de gaine supplémentaires "manquent" alors sur l'un des deux bras du dipôle, ce qui entraîne en outre une déformation de la caractéristique directionnelle.

[question:EG405]
[question:EG406]

La figure [ref:e_mantelwellen] illustre comment une partie du courant, qui devrait normalement circuler dans le bras du dipôle, retourne sur le blindage coaxial.

<margin>
[picture:633:e_mantelwellen:Ondes de gaine]
</margin>

Les courants de gaine circulent en fait largement à la surface du conducteur extérieur. Cela est lié à ce que l'on appelle l'*effet de peau*, qui fait que les courants haute fréquence circulent largement à la surface des conducteurs métalliques. Dans ce sens, on peut aussi se représenter un câble coaxial comme un système à trois conducteurs :
  
1. Côté extérieur du conducteur intérieur
2. Côté intérieur du conducteur extérieur
3. Côté extérieur du conducteur extérieur
  
Le courant sur le côté extérieur du conducteur intérieur et le courant sur le côté intérieur du conducteur extérieur ont toujours la même valeur et sont opposés ($I_1$). Le courant sur le côté extérieur du conducteur extérieur ($I_3$) représente le courant de gaine.

[question:EG404]

---

Les ondes de gaine peuvent être évitées, par exemple, en utilisant un *symétriseur*, un balun, pour relier le câble coaxial et l'antenne.

<indepth>
Le mot *balun* est composé des mots anglais "balanced" et "unbalanced", car un côté symétrique (par exemple une antenne symétrique) doit être relié à un côté asymétrique (le câble coaxial, pour lequel idéalement seul le conducteur intérieur présente une tension par rapport à la terre).
</indepth>

[question:EG407]

---

Une autre forme de construction pour un balun consiste à enrouler un câble coaxial autour d'un noyau de ferrite. Cela représente une soi-disant *bobine à compensation de courant* et est également appelé *barrière d'ondes de gaine*. Pour les signaux en opposition de phase, elle a une faible impédance, car, lorsque le courant dans le conducteur intérieur est opposé à celui dans le conducteur extérieur, aucune interaction notable avec le matériau de ferrite ne se produit. Pour les ondes de gaine, cependant, la structure agit comme une bobine (à pertes).

<margin>
[photo:325:e_mantelwellendrossel:Barrière d'ondes de gaine]
</margin>

[question:EG408]