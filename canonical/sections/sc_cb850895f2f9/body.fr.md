Dans les sections [sec:ueberlagerungsempfaenger_einfachsuper_1] et [sec:ueberlagerungsempfaenger_einfachsuper_2], nous avons déjà fait connaissance avec le récepteur superhétérodyne. Dans cette classe, nous allons maintenant nous intéresser au récepteur double superhétérodyne. Contrairement au superhétérodyne simple, le double superhétérodyne utilise 2 fréquences intermédiaires, comme le montre la figure [ref:doppelsuper_blockschaltbild].

<margin>
[picture:810:doppelsuper_blockschaltbild:Schéma bloc d'un double superhétérodyne]
</margin>

L'utilisation d'une première FI élevée permet, comme décrit dans la section précédente, une bonne suppression de la fréquence image. Les deux fréquences de réception possibles sont ainsi très éloignées l'une de l'autre et la suppression de la fréquence de réception indésirable (fréquence image) est facilement réalisable par des filtres d'entrée avant le premier mélangeur.

L'utilisation d'une deuxième FI basse permet, dans une deuxième étape, d'atteindre une haute sélectivité du récepteur, car pour les basses fréquences, des filtres à facteur de qualité élevé et à flancs raides sont techniquement très bien réalisables.

Pour un récepteur ondes courtes, la première FI et la fréquence de réception maximale souhaitée doivent également, selon le concept du récepteur, être aussi éloignées que possible l'une de l'autre pour éviter une réception directe de la FI par l'antenne. La première FI devrait donc être le double de la fréquence de réception maximale.

<tip>
Une extension du concept du double superhétérodyne serait le triple superhétérodyne, où une troisième FI basse est formée. Cela peut être utile pour des procédures de démodulation spéciales ou pour la mise en œuvre de procédures de suppression d'interférences (filtre coupe-bande). Le calcul des fréquences intermédiaires et des fréquences de l’oscillateur se fait ici en conséquence de celui du double superhétérodyne.
</tip>

[question:AF112]
[question:AF113]

Après le premier mélangeur, un filtre très étroit, accordé sur la première FI, peut être utilisé pour améliorer la robustesse aux signaux forts. On appelle ce filtre *Roofing Filter*. La bande passante du filtre roofing doit ici être au moins aussi grande que la plus grande bande passante requise par les modes de fonctionnement prévus.

[question:AF114]
[question:AF116]

Le double superhétérodyne se compose des blocs fonctionnels suivants :

1. Partie HF avec présélection
2. Premier mélangeur avec VFO pour former la première FI. Ici, la fréquence du VFO peut être soit au-dessus, soit en dessous de la fréquence de réception souhaitée (décalée dans chaque cas de la première FI)
3. Premier amplificateur FI avec filtre (filtre roofing)
4. Deuxième mélangeur avec CO (oscillateur à quartz) pour former la deuxième FI. Ici, la fréquence du CO peut être soit au-dessus, soit en dessous de la première FI (décalée dans chaque cas de la deuxième FI)
5. Deuxième amplificateur FI avec filtre (filtre FI selon le type de modulation/mode de fonctionnement, généralement commutable).
6. Détecteur de produit ou démodulateur (selon le mode de fonctionnement) éventuellement avec BFO. Cette étape sert également à la génération d'une tension de commande pour le contrôle de la sensibilité d'entrée de la branche de réception (AGC)
7. Amplificateur BF avec sortie haut-parleur ou prise casque

[question:AF209]
[question:AF117]
[question:AF210]

Pour calculer les fréquences de l’oscillateur nécessaires en fonction d'une fréquence de réception souhaitée, il faut se représenter que les fréquences de l’oscillateur peuvent être respectivement au-dessus ou en dessous de la fréquence d'entrée souhaitée du mélangeur. Par conséquent, pour chaque étage de mélangeur, il existe deux possibilités de solution.

1. Fréquence de l’oscillateur = Fréquence d'entrée + Fréquence de sortie
2. Fréquence de l’oscillateur = Fréquence d'entrée - Fréquence de sortie

Avec ces connaissances, les questions suivantes peuvent être résolues.

[question:AF120]
[question:AF118]
[question:AF119]
