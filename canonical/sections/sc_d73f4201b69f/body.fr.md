L’alimentation à découpage a déjà été expliquée de manière introductive dans les classes N et E. Examinons maintenant plus en détail le schéma bloc simplifié.

<margin>
[picture:35:a_schaltnetzteil:Schéma de principe d’une alimentation à découpage]
</margin>

L’interrupteur électronique important dans le bloc E sert également à réguler la tension de sortie à une valeur constante.
Comme il n’existe pas d’états intermédiaires entre le transistor passant et bloqué, il doit exister une autre possibilité de régulation. Le transport d’énergie du côté entrée vers le côté charge peut être varié par le temps de conduction. Si l’interrupteur reste fermé plus longtemps, davantage d’énergie est transportée vers le côté charge et la tension de sortie augmente. Pour le constater, il est nécessaire de renvoyer la tension de sortie vers le bloc de commande de l’interrupteur électronique. Cette rétroaction est absente dans le schéma simplifié représenté. La régulation de la tension de sortie s’effectue donc par le biais d’un modulateur d’impulsions en largeur. Cela signifie que l’état passant de l’interrupteur est modifié, tandis que la fréquence de commutation reste constante.

---

[question:AD311]

Il est également important d’assurer une séparation galvanique entre les côtés entrée et sortie afin d’éviter que les potentiels de la tension secteur n’atteignent la sortie. Cette isolation est réalisée par le transformateur à noyau de ferrite.
Voir l’image [ref:a_innenansicht_eines_schaltnetzteils].

<margin>
[photo:264:a_innenansicht_eines_schaltnetzteils:Vue intérieure d’une alimentation à découpage]
</margin>

---

La variation du temps de commutation génère des signaux parasites supplémentaires qui doivent absolument être maintenus à distance du côté de la tension secteur afin qu’ils ne se propagent pas via le réseau électrique et ne perturbent pas d’autres appareils électroniques. Le réseau électrique agit également comme une antenne et peut donc rayonner des signaux parasites sous forme d’onde électromagnétique. Si l’interrupteur électronique fonctionne à une fréquence de commutation de $\qty{30}{\kilo\hertz}$, il en résulte un spectre de perturbations dans lequel un signal parasite apparaît tous les $\qty{30}{\kilo\hertz}$. L’image [ref:a_störspektrum] montre le spectre de perturbations d’une alimentation à découpage. Ce spectre a été capté directement au-dessus du boîtier de l’alimentation. À une distance de $\qty{1}{\meter}$, le spectre de perturbations est à peine mesurable.

[question:AD312]

Dans le cas d’alimentations à découpage insuffisamment antiparasitées, le spectre de perturbations perturbe la réception radio.

[question:AD313]

<margin>
[photo:277:a_störspektrum:Spectre de perturbations d’une alimentation à découpage]
</margin>

---

Pour empêcher que des perturbations n’atteignent le réseau électrique, une bobine d’arrêt de haute qualité doit être intégrée dans l’alimentation à découpage du côté de la connexion au réseau de $\qty{230}{\volt}$ en courant alternatif. La structure typique du filtre est visible dans l’image [ref:a-schaltnetzteilfilter].

<margin>
[picture:367:a-schaltnetzteilfilter:Filtre à l’entrée $\qty{230}{\volt}$ d’une alimentation à découpage]
</margin>

Voir également les filtres dans les images [ref:a_EMV_Filter1] et [ref:a_EMV_Filter2]
*À retenir :* Le conducteur de protection (PE) ne doit pas être connecté au conducteur L1 ou au conducteur N.
La bobine d’arrêt T ne doit pas avoir de fonction de transformateur pour la tension alternative du réseau.

[question:AD314]

<margin>
Filtre CEM = filtre antiparasite contre les perturbations conduites
[photo:242:a_EMV_Filter1: Filtre antiparasite pour une alimentation à découpage]
[photo:243:a_EMV_Filter2: Filtre directement à l’entrée de tension alternative $\qty{230}{\volt}$]
</margin>