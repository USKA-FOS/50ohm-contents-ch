Dans la classe E, nous avons déjà étudié le récepteur superhétérodyne. Dans cette classe, nous allons nous pencher sur le récepteur double superhétérodyne. Contrairement au superhétérodyne simple, le double superhétérodyne utilise deux fréquences intermédiaires, comme illustré dans le schéma bloc [ref:doppelsuper_blockschaltbild].

<margin>
[picture:810:doppelsuper_blockschaltbild:Schéma bloc d’un double superhétérodyne]
</margin>

L’utilisation d’une première FI élevée permet, comme décrit dans la section précédente, une bonne suppression de la fréquence image. Les deux fréquences de réception possibles sont ainsi très éloignées l’une de l’autre, et la suppression de la fréquence de réception indésirable (fréquence image) est facilement réalisable à l’aide de filtres d’entrée placés avant le premier mélangeur.

L’utilisation d’une deuxième FI basse permet, lors de la deuxième étape, d’obtenir une sélectivité élevée du récepteur, car pour les basses fréquences, il est techniquement très facile de réaliser des filtres à haute qualité et à flancs raides.

La première FI et la fréquence de réception maximale souhaitée doivent être, pour un récepteur ondes courtes, aussi éloignées que possible l’une de l’autre, selon le concept du récepteur, afin d’éviter une réception directe de la FI par l’antenne. La première FI devrait donc être égale au double de la fréquence de réception maximale.

<tip>
Une extension du concept de double superhétérodyne serait le triple superhétérodyne, dans lequel une troisième FI basse est générée. Cela peut être utile pour des procédés de démodulation spécifiques ou pour la réalisation de procédés de suppression des interférences (filtres Notch). Le calcul des fréquences intermédiaires et des fréquences de l’oscillateur s’effectue alors de manière similaire à celui du double superhétérodyne.
</tip>

[question:AF112]
[question:AF113]

Après le premier mélangeur, un filtre très étroit, accordé sur la première FI, peut être utilisé pour améliorer la robustesse aux signaux forts. Ce filtre est appelé *filtre de toit* (Roofing Filter). La bande passante du filtre de toit doit être au moins aussi grande que la bande passante maximale requise pour les modes de fonctionnement prévus.

[question:AF114]
[question:AF116]

Le double superhétérodyne se compose des blocs fonctionnels suivants :

1. Partie HF avec présélection
2. Premier mélangeur avec VFO pour la génération de la première FI. La fréquence du VFO peut être soit au-dessus, soit en dessous de la fréquence de réception souhaitée (décalée de la première FI)
3. Premier amplificateur FI avec filtre (filtre de toit)
4. Deuxième mélangeur avec oscillateur à quartz pour la génération de la deuxième FI. La fréquence de l’oscillateur à quartz peut être soit au-dessus, soit en dessous de la première FI (décalée de la deuxième FI)
5. Deuxième amplificateur FI avec filtre (filtre FI selon le type de modulation/mode de fonctionnement, généralement commutable)
6. Détecteur de produit ou démodulateur (selon le mode de fonctionnement), éventuellement avec BFO. Ce étage sert également à générer une tension de régulation pour le contrôle de la sensibilité d’entrée du récepteur (AGC)
7. Amplificateur BF avec sortie haut-parleur ou connexion casque

[question:AF209]
[question:AF117]
[question:AF210]

Pour calculer les fréquences d’oscillateur nécessaires en fonction d’une fréquence de réception souhaitée, il faut se rappeler que les fréquences d’oscillateur peuvent être soit au-dessus, soit en dessous de la fréquence d’entrée souhaitée du mélangeur. Il existe donc pour chaque étage de mélange deux solutions possibles.

1. Fréquence de l’oscillateur = fréquence d’entrée + fréquence de sortie
2. Fréquence de l’oscillateur = fréquence d’entrée - fréquence de sortie

Avec ces connaissances, on peut répondre aux questions suivantes.

[question:AF120]
[question:AF118]
[question:AF119]