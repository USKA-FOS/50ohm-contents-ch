Les transistors ont une *courbe caractéristique*, qui représente la *relation entre le signal d'entrée (tension base-émetteur ou grille-source) et le signal de sortie (courant collecteur/drain)*. Dans ce cas, il existe dans la plage de la courbe caractéristique différentes sections dans lesquelles le transistor a une *caractéristique linéaire ou non linéaire*.
Les zones linéaires de la courbe caractéristique, dans lesquelles une modification de la grandeur de commande entraîne une modification proportionnelle de la grandeur de sortie, sont désignées comme linéaires.
D'autres zones de la courbe caractéristique, dans lesquelles une modification de la grandeur de commande n'entraîne **aucune** modification proportionnelle de la grandeur de sortie, sont désignées comme non linéaires.

<margin>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'un transistor avec points de fonctionnement]  
</margin>

Pour un fonctionnement optimal de l'amplificateur en termes de rendement et de pureté des harmoniques supérieures du signal amplifié, il est nécessaire de choisir un point de fonctionnement optimal de l'amplificateur sur sa courbe caractéristique.
Ce point de fonctionnement est défini par une tension continue auxiliaire appropriée (prétension) à la base ou à la grille.

L'amplification du signal d'entrée s'effectue ensuite autour du point de fonctionnement souhaité, qui définit le centre de la plage de fonctionnement.
Le choix du point de fonctionnement donne lieu à un courant de repos correspondant du transistor. Celui-ci circule également en l'absence de signal d'entrée. Le courant de repos influence de manière significative l'efficacité d'un amplificateur, car il augmente sa puissance dissipée thermique et réduit ainsi son rendement.

Tous les signaux dont l'information de modulation se trouve dans leur amplitude doivent être amplifiés de manière linéaire afin de transmettre l'information transmise sans distorsion (SSB, AM, etc.). Les signaux dont l'information de modulation ne se trouve pas dans l'amplitude mais seulement dans la fréquence peuvent également être amplifiés dans la zone non linéaire d'un amplificateur (FM, etc.) et ensuite filtrés.

Selon le mode de fonctionnement, on distingue différents points de fonctionnement et leur désignation sur la courbe caractéristique (voir figure [ref:a_kennlinien_transistor_arbeitspunkt] ) :

AP1 : fonctionnement en classe C de l'amplificateur
- sans prétension
- courant de repos nul
- rendement d'environ $\qtyrange{80}{87}{\percent}$
- taux élevé d'harmoniques supérieures

AP2 : fonctionnement en classe B de l'amplificateur
- Faible prétension jusqu'au début du courant collecteur
- courant de repos presque nul (faible)
- rendement jusqu'à $\qty{80}{\percent}$
- faible taux d'harmoniques supérieures

AP3 : fonctionnement en classe A/B de l'amplificateur
- prétension plus élevée que dans le fonctionnement en classe B, mais inférieure à celle du fonctionnement en classe A
- courant de repos plus élevé que dans le fonctionnement en classe B, mais nettement inférieur à celui du fonctionnement en classe A
- rendement compris entre $\qty{50}{\percent}$ et $\qty{80}{\percent}$
- faible taux d'harmoniques supérieures

AP4 : fonctionnement en classe A de l'amplificateur
- la prétension est choisie de telle sorte que le courant de repos atteint environ $\qty{50}{\percent}$ de la valeur maximale admissible
- rendement d'environ $\qty{40}{\percent}$
- très faible taux d'harmoniques supérieures

[question:AD416]
[question:AD419]
[question:AD420]
[question:AD421]

La puissance de sortie d'un amplificateur peut être calculée grossièrement par la connaissance du point de fonctionnement et donc de son rendement approximatif. Dans ce cas, on calcule d'abord la puissance en courant continu à partir du produit de la tension et du courant qui est fourni à l'amplificateur. Ensuite, on multiplie cette puissance par le facteur numérique du rendement, $\qty{100}{\percent}$ correspondant à un rendement de $1$. Par exemple, un rendement de $\qty{40}{\percent}$ correspond alors à un facteur de $0,4$.

[question:AD424]
[question:AD425]
[question:AD418]
[question:AD417]

Pour qu'un amplificateur puisse être utilisé pour le fonctionnement SSB (amplification linéaire), son point de fonctionnement doit se situer en classe A/AB ou B. En principe, le fonctionnement en classe A est possible en raison de la haute linéarité, mais il n'est pas efficace à des puissances plus élevées. Dans ce cas, on combine deux transistors dans un circuit dit push-pull, de sorte que chacun des deux transistors n'amplifie que respectivement une demi-onde (positive ou négative). Cela permet également un fonctionnement en classe AB ou B avec un rendement accru de l'amplificateur.
En classe C, le signal est toujours distordu. Par conséquent, un émetteur SSB ne peut pas fonctionner en classe C.
En particulier dans le cas du fonctionnement en classe AB ou B d'un amplificateur, il faut éviter la surcharge, car celle-ci entraîne rapidement des distorsions du signal. Celles-ci se manifestent dans le cas du SSB par des splatters sur des fréquences voisines.

[question:AD422]
[question:AJ218]
[question:AD423]

Les amplificateurs en classe C génèrent, en raison de leur point de fonctionnement fortement non linéaire, des taux élevés d'harmoniques supérieures, qui doivent être supprimés dans la suite du trajet du signal, par exemple par filtrage (passe-bas).
Étant donné que dans les amplificateurs de puissance en classe C, des harmoniques supérieures avec des amplitudes et des puissances élevées sont également présentes dans l'amplificateur ainsi que dans le filtre qui suit, l'amplificateur ainsi que le filtre doivent être exploités dans un boîtier métallique bien blindé, afin qu'ils ne provoquent pas de perturbations par les harmoniques supérieures.

[question:AF402]
[question:AF403]


