Contrairement au superhétérodyne simple, le double superhétérodyne utilise deux fréquences intermédiaires.

<margin>
[picture:810:doppelsuper_blockschaltbild:Schéma bloc d'un double superhétérodyne]
</margin>

Grâce à l'utilisation d'une première fréquence intermédiaire élevée, une bonne suppression de la fréquence image est possible. Les deux positions de réception possibles sont ainsi très éloignées l'une de l'autre et une suppression de la position de réception non souhaitée (fréquence image) est facilement réalisable par des filtres d'entrée avant le premier mélangeur. Grâce à l'utilisation d'une 2ème fréquence intermédiaire basse, une grande sélectivité du récepteur peut être obtenue lors de la 2ème étape, car des filtres à haute qualité et à flancs raides sont techniquement très réalisables pour les basses fréquences.
La première fréquence intermédiaire et la fréquence de réception la plus élevée souhaitée doivent, dans le cas d'un récepteur à ondes courtes, être également aussi éloignées que possible l'une de l'autre, selon le concept du récepteur, afin d'éviter une réception directe de la fréquence intermédiaire via l'antenne. La 1ère fréquence intermédiaire doit donc être égale au double de la fréquence de réception maximale.

<tip>
Une extension du concept du double superhétérodyne serait le triple superhétérodyne, dans lequel une 3ème fréquence intermédiaire basse est formée. Cela peut être utile pour des procédés de démodulation spéciaux ou pour la réalisation de procédés de suppression d'interférences (filtre coupe-bande). Le calcul des fréquences intermédiaires et des fréquences d'oscillateur s'effectue ici de manière correspondante à celui du double superhétérodyne.
</tip>

[question:AF112]
[question:AF113]

Après le premier mélangeur, un filtre très étroit, accordé sur la 1ère fréquence intermédiaire, peut être utilisé pour améliorer la résistance aux grands signaux. On appelle ce filtre *Roofing Filter*. La bande passante du filtre Roofing doit être au moins aussi grande que la plus grande bande passante nécessaire pour les modes de fonctionnement prévus.

[question:AF114]
[question:AF116]

Le double superhétérodyne se compose des blocs fonctionnels suivants :
1. Partie HF avec présélection
2. Premier mélangeur avec VFO pour la formation de la première fréquence intermédiaire. La fréquence du VFO peut être à la fois au-dessus et en dessous de la fréquence de réception souhaitée (décalée respectivement de la 1ère fréquence intermédiaire)
3. Premier amplificateur de fréquence intermédiaire avec filtre (Roofing-Filter)
4. Deuxième mélangeur avec CO (Oscillateur à quartz) pour la formation de la deuxième fréquence intermédiaire. La fréquence du CO peut être à la fois au-dessus et en dessous de la 1ère fréquence intermédiaire (décalée respectivement de la 2ème fréquence intermédiaire)
5. Deuxième amplificateur de fréquence intermédiaire avec filtre (filtre de fréquence intermédiaire selon le type de modulation/mode de fonctionnement, généralement commutable).
6. Détecteur de produit ou démodulateur (selon le mode de fonctionnement) éventuellement avec BFO. Ce niveau sert également à générer une tension de régulation pour le contrôle de la sensibilité d'entrée de la voie de réception (AGC)
7. Amplificateur de basse fréquence avec sortie haut-parleur ou connecteur de casque

[question:AF209]
[question:AF117]
[question:AF210]

Pour calculer les fréquences d'oscillateur nécessaires en fonction d'une fréquence de réception souhaitée, il faut se rappeler que les fréquences d'oscillateur peuvent être situées soit au-dessus soit en dessous de la fréquence d'entrée souhaitée du mélangeur. Il existe donc pour chaque étage de mélange deux possibilités de solution.
1. Fréquence d'oscillateur = Fréquence d'entrée + Fréquence de sortie
2. Fréquence d'oscillateur = Fréquence d'entrée - Fréquence de sortie

Avec cette connaissance, les questions suivantes peuvent être répondues.

[question:AF120]
[question:AF118]
[question:AF119]