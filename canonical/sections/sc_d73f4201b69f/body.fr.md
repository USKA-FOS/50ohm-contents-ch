L'alimentation à découpage a déjà été expliquée de manière introductive dans la section [sec:schaltnetzteil_1]. Maintenant, nous examinons de plus près le schéma bloc simplifié [ref:a_schaltnetzteil].

<marge>
[image:35:a_schaltnetzteil:Schéma de principe d'une alimentation à découpage]
</marge>

L'interrupteur électronique important dans le bloc E sert également à réguler une tension de sortie constante.
Comme il n'y a pas d'états intermédiaires entre le transistor conducteur et bloqué, il doit exister une autre possibilité de régulation. Le transfert d'énergie du côté entrée vers le côté charge peut être varié par le temps de commutation. Si l'interrupteur est fermé plus longtemps, alors plus d'énergie est transférée vers le côté charge et la tension de sortie augmente. Pour le déterminer, un retour de la tension de sortie vers le bloc de commande de l'interrupteur électronique est nécessaire. Cette rétroaction manque dans le schéma simplifié représenté. La régulation de la tension de sortie se fait maintenant via le modulateur à largeur d'impulsion. Cela signifie que l'état conducteur de l'interrupteur est modifié, la fréquence de commutation restant constante.

---

[question:AD311]

La séparation galvanique des côtés entrée et sortie est également importante pour éloigner les potentiels de tension secteur de la sortie. Cette séparation du réseau se fait par le transformateur avec noyau en ferrite.
Voir la figure [ref:a_innenansicht_eines_schaltnetzteils].

<marge>
[photo:264:a_innenansicht_eines_schaltnetzteils:Vue intérieure d'une alimentation à découpage]
</marge>

---

La modification du temps de commutation provoque des signaux parasites supplémentaires, qui doivent absolument être éloignés du côté tension secteur pour qu'ils ne se propagent pas via le réseau électrique et ne perturbent pas d'autres appareils électroniques. Le réseau électrique agit également comme une antenne et peut donc rayonner des signaux parasites sous forme d'onde électromagnétique. Si l'interrupteur électronique fonctionne avec une fréquence de commutation de $\qty{30}{\kilo\hertz}$, alors un spectre de bruit apparaît, dans lequel un signal parasite apparaît tous les $\qty{30}{\kilo\hertz}$. La figure [ref:a_störspektrum] montre le spectre de bruit d'une alimentation à découpage. Le spectre de bruit a été reçu directement au-dessus du boîtier de l'alimentation à découpage. À $\qty{1}{\meter}$ de distance, le spectre de bruit est à peine mesurable.

[question:AD312]

Pour les alimentations à découpage insuffisamment antiparasitées, le spectre de bruit affecte la réception radio.

[question:AD313]

<marge>
[photo:277:a_störspektrum:Spectre de bruit d'une alimentation à découpage]
</marge>

---

Pour empêcher les perturbations de pénétrer dans le réseau électrique, un filtre passe-bas de haute qualité doit être intégré dans l'alimentation à découpage du côté de la connexion au réseau alternatif $\qty{230}{\volt}$. La structure typique du filtre est visible dans la figure [ref:a-schaltnetzteilfilter].

<marge>
[image:367:a-schaltnetzteilfilter:Filtre à l'entrée $\qty{230}{\volt}$ d'une alimentation à découpage]
</marge>

Comparez également les filtres dans les figures [ref:a_EMV_Filter1] et [ref:a_EMV_Filter2]
*À retenir :* Le conducteur PE ne doit pas être connecté au conducteur L1 ou au conducteur N.
La bobine d’arrêt T ne doit pas avoir de fonction de transformateur pour la tension alternative du réseau.

[question:AD314]


<marge>
Filtre CEM = filtre antiparasite contre les perturbations conduites
[photo:242:a_EMV_Filter1: Filtre antiparasite pour une alimentation à découpage]
[photo:243:a_EMV_Filter2: Filtre directement à l'entrée de tension AC $\qty{230}{\volt}$]
</marge>
