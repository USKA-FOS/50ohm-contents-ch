Dans le cours HB3, nous avons déjà appris à connaître le *fading* (*QSB*) dans la section [sec:fading]. Cela sera approfondi un peu plus ici dans le cours HB9. Lorsqu'un signal radio atteint le récepteur par plus d'un chemin depuis l'émetteur, on parle de *propagation par trajets multiples*. Une cause importante est la réflexion du signal sur des surfaces (par exemple, bâtiments, topographie, avions) [ref:a_mehrwegeausbreitung_reflexion]. Sur les ondes courtes, s'ajoute le fait que le signal est souvent réfracté en plusieurs endroits dans l'ionosphère. Presque chaque liaison radio est affectée par la propagation par trajets multiples.

<margin>
[picture:1064:a_mehrwegeausbreitung_reflexion:Propagation par trajets multiples due à la réflexion. En raison du déphasage lors de la réflexion, le signal reçu peut être amplifié ou atténué]
</margin>

---

Le récepteur reçoit donc simultanément *plusieurs* signaux qui, en raison de trajets différents, arrivent avec des temps de propagation et donc des phases différents. Ces signaux sont additionnés dans le récepteur et cela s'appelle *interférence* dans le langage technique. Selon la différence de phase, le signal résultant peut être soit amplifié soit atténué – dans les cas extrêmes, jusqu'à une annulation complète.

<indepth>
L'interférence (du latin inter = "entre" et ferire, via l'ancien français s'entreferir = "se frapper mutuellement") désigne généralement la modification de l'amplitude qui se produit lors de la superposition de deux ondes ou plus, c'est-à-dire lors de leur addition.
</indepth>

[question:AH222]

<webmargin>
[include:applet_interferenz]
</webmargin>

Si l'un des milieux impliqués se déplace (par exemple, une opération radio depuis une voiture en mouvement, un avion comme réflecteur pour les signaux radio ou, fondamentalement, les zones de réfraction dans l'ionosphère, surtout pendant le crépuscule), alors le signal résultant dans le récepteur change également continuellement. Cela conduit constamment à du QSB et, selon le type de modulation, à des distorsions plus ou moins importantes et donc à une intelligibilité réduite.
