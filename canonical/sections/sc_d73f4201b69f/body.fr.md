Le bloc d'alimentation à découpage a été expliqué de manière introductive dans les classes N et E. Nous allons maintenant examiner plus en détail le schéma bloc simplifié.

<margin>
[picture:35:a_schaltnetzteil:Schéma bloc d'un bloc d'alimentation à découpage]
</margin>

L'interrupteur électronique important dans le bloc E sert également à réguler une tension de sortie constante.
Comme il n'y a pas d'états entre le transistor conducteur et bloqué, il doit y avoir une autre possibilité de régulation. Le transport d'énergie du côté entrée vers le côté charge peut être varié par le temps de commutation. Si l'interrupteur est fermé plus longtemps, plus d'énergie est transportée vers le côté charge et la tension de sortie augmente. Pour déterminer cela, un retour d'information de la tension de sortie vers le bloc de commande de l'interrupteur électronique est nécessaire. Ce retour est absent dans le schéma de circuit simplifié représenté. La régulation de la tension de sortie se fait maintenant via le modulateur de largeur d'impulsion dit. Cela signifie que l'état conducteur de l'interrupteur est modifié, la fréquence de commutation restant constante. 

---

[question:AD311]

Il est également important d'assurer la séparation galvanique des côtés entrée et sortie afin d'éloigner les potentiels de la tension du réseau de la sortie. Cette séparation du réseau est réalisée par le transformateur à noyau de ferrite. 
Voir l'illustration [ref:a_innenansicht_eines_schaltnetzteils]. 

<margin>
[photo:264:a_innenansicht_eines_schaltnetzteils:Vue intérieure d'un bloc d'alimentation à découpage]
</margin>

---

La modification du temps de commutation entraîne des signaux parasites supplémentaires qui doivent absolument être éloignés du côté de la tension du réseau afin qu'ils ne se propagent pas dans le réseau électrique et n'interfèrent pas avec d'autres appareils électroniques. Le réseau électrique agit également comme une antenne et peut donc émettre des signaux parasites sous forme d'onde électromagnétique. Si l'interrupteur électronique est exploité à une fréquence de commutation de $\qty{30}{\kilo\hertz}$, un spectre de perturbations se produit dans lequel un signal de perturbation apparaît tous les $\qty{30}{\kilo\hertz}$. L'illustration [ref:a_störspektrum] montre le spectre de perturbations d'un bloc d'alimentation à découpage. Le spectre de perturbations a été reçu directement au-dessus du boîtier du bloc d'alimentation à découpage. À une distance de $\qty{1}{\meter}$, le spectre de perturbations est à peine mesurable.

[question:AD312]

Dans le cas des blocs d'alimentation à découpage insuffisamment filtrés, le spectre de perturbations affecte la réception radio.

[question:AD313]

<margin>
[photo:277:a_störspektrum:Spectre de perturbations d'un bloc d'alimentation à découpage]
</margin>

---

Pour empêcher les perturbations de pénétrer dans le réseau électrique, un filtre passe-bas de haute qualité doit être intégré dans le bloc d'alimentation à découpage du côté de la connexion au réseau de tension alternative de $\qty{230}{\volt}$. La structure typique du filtre est visible dans l'illustration [ref:a-schaltnetzteilfilter].

<margin>
[picture:367:a-schaltnetzteilfilter:Filtre sur l'entrée $\qty{230}{\volt}$ d'un bloc d'alimentation à découpage]
</margin>

Comparez également les filtres dans l'illustration [ref:a_EMV_Filter1] et [ref:a_EMV_Filter2]
*Remarque :* Le conducteur PE ne doit pas être connecté au conducteur L1 ou au conducteur N.
La bobine de choc T ne doit pas avoir de fonction de transformateur pour la tension alternative du réseau.

[question:AD314]


<margin>
Filtre CEM = Filtre anti-parasites contre les perturbations conduites par les lignes
[photo:242:a_EMV_Filter1: Filtre anti-parasites pour un bloc d'alimentation à découpage]
[photo:243:a_EMV_Filter2: Filtre directement sur l'entrée de tension alternative de $\qty{230}{\volt}$]
</margin>