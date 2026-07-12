La dénomination du circuit de base d'un transistor bipolaire dépend de la connexion (base, collecteur ou émetteur) qui est commune au signal d'entrée et au signal de sortie.

Dans le cas du *circuit émetteur*, le signal d'entrée circule de la source à travers la base, l'*émetteur* et la masse pour revenir à la source. Le signal de sortie circule du collecteur à travers la charge (puits) et à travers la masse pour revenir dans l'*émetteur*.

[question:AD409]

%TODO: Insérer éventuellement un schéma avec les flux de courant.

Fonctionnement d'un amplificateur en circuit émetteur:

%TODO: Insérer une image du circuit émetteur avec un diviseur de tension et des condensateurs de couplage

Pour fonctionner comme un amplificateur de tension linéaire, le transistor dans le circuit émetteur nécessite un point de fonctionnement défini (BIAS), qui est généralement fixé par un diviseur de tension à la base.

[question:AD411]

La résistance de collecteur convertit le courant qui circule à travers la section collecteur-émetteur en une chute de tension, qui est prélevée au collecteur. Le courant de collecteur du transistor circule (ensemble avec la part normalement négligeable du courant de base) à travers l'émetteur à travers la résistance d'émetteur vers la masse. Le courant à travers la résistance d'émetteur provoque, par la chute de tension qui en résulte, une augmentation du potentiel d'émetteur (tension d'émetteur) et agit ainsi comme une contre-réaction pour la tension de base. De ce fait, le point de fonctionnement du transistor est en outre stabilisé, car les variations du courant de collecteur dues à la température sont ainsi régulées.

Afin de maintenir la contre-réaction pour l'amplification des signaux de tension alternative aussi faible que possible, la résistance d'émetteur est pontée de manière capacitive (par un condensateur).

[question:AD413]

Le couplage et le découplage des signaux à la base et au collecteur s'effectuent par l'intermédiaire de condensateurs de couplage. Ceux-ci ont pour tâche d'empêcher les composantes de tension continue d'atteindre l'étage amplificateur, ce qui entraînerait une modification du point de fonctionnement.

[question:AD412]

Le condensateur de blocage dans la tension de service (+) sert à évacuer les signaux HF et BF indésirables, afin d'éviter les effets de rétroaction sur l'étage et la tension d'alimentation.

Le déphasage entre le signal d'entrée et le signal de sortie est de $\qty{180}{\degree}$ dans le circuit émetteur, car lors d'une demi-onde positive dans la tension d'entrée, le courant de collecteur augmente et donc la chute de tension à la résistance de collecteur augmente. De ce fait, la tension au condensateur de sortie diminue. Il en résulte une demi-onde négative à la sortie de l'étage amplificateur.

[question:AD407]
[question:AD408]

Si un circuit émetteur, comme dans la question suivante, est exploité sans pré-réglage du point de fonctionnement par un diviseur de tension, le transistor est commandé uniquement par le signal d'entrée fourni. Ce n'est que lorsque celui-ci dépasse la valeur d'environ $\qty{0,6}{\volt}$ que la section base-émetteur du transistor devient conductrice. De ce fait, un courant de collecteur ne circule que dans les pics de tension, provoquant une chute de tension à la sortie. En tant que signal de sortie, la tension d'alimentation apparaît, qui chute aux moments où le transistor passe en zone conductrice. Cela explique le signal de sortie correspondant.

[question:AD406]

L'amplification de tension du circuit émetteur se situe, avec une conception appropriée, dans la plage de $100\dots 300$ et est donc élevée. Cependant, si le condensateur d'émetteur est retiré, le facteur d'amplification du circuit diminue considérablement. Il est finalement défini uniquement par le rapport entre la résistance de collecteur et la résistance d'émetteur.

[question:AD414]
[question:AD415]
[question:AD410]









