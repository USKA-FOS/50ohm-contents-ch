Jusqu'à présent, nous avons considéré les champs électriques et magnétiques dans le cas où les champs ne varient pas dans le temps. En radioélectricité, de tels champs sont en fait peu intéressants, car nous nous intéressons aux tensions et aux courants qui varient dans le temps. De même, les champs électriques et magnétiques générés sont variables dans le temps. 

<margin>
[picture:885:e_vertikalantenne_em:Champ électrique et magnétique d'une antenne]
</margin>

Des effets supplémentaires se produisent. Dès 1831, Michael Faraday a découvert qu'un champ magnétique variable dans le temps dans un conducteur voisin produit une tension électrique. Cet effet, appelé *induction*, est utilisé par exemple dans le transformateur : un courant variable dans le temps (par exemple sinusoïdal) dans l'enroulement primaire produit un champ magnétique variable dans le temps, qui induit à son tour une tension dans l'enroulement secondaire.

Pour comprendre que la variation d'un champ électrique conduit à un champ magnétique, nous imaginons un condensateur à plaques dont les plaques forment un circuit avec une source de tension externe. Si nous changeons le champ électrique à l'intérieur du condensateur, des charges doivent être déplacées dans le circuit externe. Le déplacement des porteurs de charge implique un courant électrique. Ce courant électrique produit à son tour un champ magnétique autour du conducteur.

Bien que les modèles avec des conducteurs électriques soient intuitifs pour nous, il est important de noter que ces conducteurs ne sont pas nécessaires. Les champs magnétiques et électriques existent également en dehors des conducteurs, même dans le vide. Il en va de même ici : un champ magnétique variable dans le temps produit un champ électrique variable dans le temps. Ce champ variable dans le temps conduit à son tour à un champ magnétique variable dans le temps. *Les champs magnétiques variables dans le temps et les champs électriques variables dans le temps sont donc toujours couplés.* C'est pourquoi nous parlons également du *champ électromagnétique*. En résumé : une onde électromagnétique qui peut se propager librement dans l'espace repose sur l'interaction entre les champs magnétiques et électriques variables dans le temps.

[question:EB302]

Comme décrit ci-dessus, les tensions et les courants constants dans le temps ne peuvent pas générer de champ électromagnétique. Pour cela, nous avons besoin d'un courant variable dans le temps dans un conducteur.

[question:EB301]

<indepth>
Le champ magnétique et le champ électrique sont en fait décrits par des *vecteurs*, c'est-à-dire des grandeurs qui ont une direction dans l'espace. Mathématiquement, on peut montrer que dans le *champ lointain*, c'est-à-dire suffisamment loin de l'antenne, les vecteurs des deux champs doivent être perpendiculaires entre eux. La direction de propagation de l'onde électromagnétique (c'est-à-dire de notre signal radio ...) est à son tour perpendiculaire à la fois au champ électrique et au champ magnétique.
  
[picture:886:e_emfeld_ausbreitung:Propagation de l'onde électromagnétique]
  
Les relations décrites sont mathématiquement décrites par les *équations de Maxwell*, d'après James Clerk Maxwell, qui les a élaborées entre 1861 et 1864 à partir d'observations d'autres physiciens. Il en est arrivé à la conclusion que les champs magnétiques et électriques doivent être couplés :
  
1. $\vec{\nabla} \cdot \vec{E} =\frac{\rho}{\varepsilon_{0}}$
2. $\vec{\nabla} \cdot \vec{B} = 0$
3. $\vec{\nabla} \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$
4. $\vec{\nabla } \times \vec{B} =\mu_0 (\vec{j} +\varepsilon_0 \frac{\partial\vec{E}}{\partial t})$
  
L'équation (3) montre qu'un champ magnétique variable dans le temps produit un champ électrique. Ce champ électrique variable dans le temps contribue, selon l'équation (4), via le courant de déplacement, à la génération d'un champ magnétique. Ces relations vont bien au-delà de ce que l'on doit savoir en radioamateur.
  
L'existence du champ électromagnétique n'a été prouvée expérimentalement que plus de vingt ans plus tard (1886) par Heinrich Hertz.
</indepth>

Comme le montrent les figures et [ref:e_emfeld_ausbreitung], la composante du champ magnétique dans le champ lointain (loin de l'antenne) est toujours perpendiculaire à la composante du champ électrique.

[question:EB303]

Les composantes des champs magnétiques et électriques perpendiculaires dans le champ lointain déterminent également la direction de propagation $S$, comme le montre la figure [ref:e_vertikalantenne_em] : elle est à nouveau perpendiculaire aux deux. On peut se représenter cela comme si le champ magnétique et le champ électrique définissaient un plan sur lequel la direction de propagation est perpendiculaire.

[question:EB304]