Dans un récepteur, auquel deux signaux HF puissants sont appliqués à l'entrée, des perturbations peuvent être causées par l'intermodulation ou la modulation croisée.
Dans le cas de l'intermodulation, cet effet se manifeste par la création de fréquences indésirables supplémentaires en raison du comportement non linéaire de l'étage d'entrée du récepteur (fonctionnement dans la plage limite non linéaire), de manière similaire à celle d'un mélangeur. Celles-ci peuvent superposer les signaux de réception souhaités et les perturber.
Dans le cas de la modulation croisée, cet effet se manifeste par le fait que le signal de réception souhaité est influencé par la modulation d'un signal AM puissant et fréquentiellement voisin. Ainsi, la modulation de l'émetteur voisin devient audible dans le signal reçu et le perturbe.

[question:AF217]
[question:AF219]
[question:AF222]
[question:AF218]

Pour supprimer un signal indésirable puissant déjà avant l'entrée du récepteur, un circuit bouchon, qui est accordé sur la fréquence exacte du signal perturbateur, peut par exemple remédier à la situation avant l'entrée du récepteur.

[question:AF223]

La robustesse aux signaux forts d'un récepteur peut être décrite par le point d'interception de troisième ordre (IP3). Il s'agit d'une mesure du point où les produits de mélange indésirables de troisième ordre atteignent la valeur d'amplitude du signal d'entrée. Plus le IP3 d'un récepteur est élevé, plus celui-ci peut traiter des signaux importants sans perturbation.

%TODO: Plus d'informations sur IP3 éventuellement Astuce, graphique sur IP3

[question:AF221]

Pour réduire l'apparition de produits de mélange indésirables à l'entrée du récepteur par des signaux forts, un atténuateur commutable (Attenuator) peut être placé avant l'entrée du récepteur. Cela réduit les produits d'intermodulation ainsi que la modulation croisée dans le récepteur. Le signal utile n'est alors réduit que du facteur de l'atténuateur - les produits de mélange perturbateurs sont cependant atténués de $\num{3}$ (ordre 3) en $\unit{\dB}$ en raison des conditions mathématiques lors du processus de mélange. Par exemple, un atténuateur de $\qty{10}{\dB}$ réduit le signal utile seulement de $\qty{10}{\dB}$ tandis que les produits de mélange indésirables sont déjà atténués de $\qty{30}{\dB}$.

[question:AF220]