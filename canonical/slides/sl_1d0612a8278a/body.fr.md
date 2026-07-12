<left>
[picture:648:n_relaisfunkstellen_aufbau:Représentation schématique d'une station relais avec des utilisateurs]
</left>
<right>
* Permet une plus grande portée que lors d'une connexion directe
* Souvent situé à des endroits exposés, par exemple sur des sommets de montagnes, des gratte-ciel, (églises-) tours
* Ou dans des satellites
</right>

<note>
* On ne peut pas communiquer à travers la montagne
* Avec le relais, les deux radioamateurs peuvent établir une connexion
* Plus sur les satellites plus tard
</note>
---
## Définition de la station relais
une station radioamateur télécommandée (également dans des satellites), qui émet des émissions radioamateurs reçues, des parties de celles-ci ou d'autres signaux injectés ou stockés déclenchés à distance et sert ainsi à augmenter la portée des stations radioamateurs
---
<left>
* Aussi appelé brièvement : relais ou répéteur
* Émettre régulièrement leur indicatif
* L'indicatif commence généralement par DB0, DM0 ou DO0
</left>
<fragment>
<right>
* Les stations relais ne sont pas exploitées avec des indicatifs personnels.
* Les stations relais ne sont généralement pas occupées en permanence.
* Les stations relais n'ont pas besoin d'être exploitées à des endroits géographiquement exposés.
</right>
</fragment>

---
[question:NF118]
---
## Fonctionnement
<left>
* Reçoit sur la fréquence d'entrée le signal d'une station radioamateur
* Le diffuse simultanément sur la fréquence de sortie
* Afin que l'émetteur ne gêne pas, les fréquences sont généralement différentes
</left>
<right>
<fragment>
On appelle l'écart *déport de fréquence* ou brièvement *déport*

| r: Bande | r: Déport |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Déport de fréquence]
</fragment>
</right>

---
Exemple d'un relais de $\qty{70}{\centi\meter}$:
* Fréquence d'entrée: $\qty{431,275}{\mega\hertz}$
* Déport: $\qty{+7,600}{\mega\hertz}$
* Fréquence de sortie: $\qty{438,875}{\mega\hertz}$

---
[question:BE401]
---
[question:BE402]
---
[question:BE403]

--- indepth
## Fonctionnement en bande croisée
* Émet et reçoit simultanément sur deux bandes différentes, par exemple $\qty{2}{\meter}$ et $\qty{70}{\centi\meter}$
* Conversion du type d'émission également possible, par exemple SSB sur FM

---
## Digipeater
* Transmet des données au lieu de la parole
* Reçoit et émet des paquets de données
* L'émission peut ne se faire que par parties ou avec un décalage temporel
* Les paquets de données peuvent être répétés
* Les champs de données individuels peuvent être modifiés

<note>
* Pour le Packet Radio, qui était populaire dans les années 90 avant Internet
* Cela sera expliqué plus en détail plus tard
</note>
---
## Paramètres spéciaux
* Des paramètres supplémentaires peuvent être nécessaires pour la connexion au relais
* Ces informations sont disponibles dans les annuaires de répéteurs, sur les sites web ou auprès du responsable du relais
* Outre les répéteurs FM, il en existe pour la parole numérique comme DMR ou D-Star

<note>
Un exemple de paramètres supplémentaires est un sous-ton avec CTCSS
</note>

---
[question:NE309]
---
[question:NE308]
---
## Bande passante du canal
* L'espace nécessaire dans le spectre de fréquences
* Wide-FM: $\qty{25}{\kilo\hertz}$
* Narrow-FM: $\qty{12,5}{\kilo\hertz}$
* Les répéteurs préfèrent le Narrow-FM, sinon les signaux sont déformés et les fréquences voisines sont perturbées

---
[question:BE407]
---
## Fonctionnement sans perturbation
* En principe, tous les radioamateurs peuvent utiliser les stations radioamateurs télécommandées avec leur indicatif attribué
* L'exploitant peut exclure les radioamateurs pour assurer le fonctionnement sans perturbation
* L'autorité fédérale des réseaux (BNetzA) doit en être informée

---
[question:VD504]
---
## Fonctionnement radio sur les répéteurs
* Passages courts
* Les stations mobiles et portables sont souvent seulement temporairement dans la zone de réception
* Pause entre les passages pour l'enregistrement d'autres stations

---
[question:BE406]
---
[question:BE404]
---
## Double émission
* En cas d'entrée simultanée de la parole, l'émission est perturbée jusqu'à l'illisibilité
* Éviter le "doublage" par une remise correcte
* Commencer l'émission seulement lorsque la station précédente a terminé

---
[question:NE310]
---
[question:BE405]
---
## Puissance d'émission
* Selon l'annexe 1 de l'AFuV
* Pour les stations automatiques au-dessus de $\qty{30}{\mega\hertz}$ avec $\qty{50}{\watt}$ ERP

---
[question:VD503]
---
## Rapport
* L'intensité du signal reçu (S) est celle du relais
* On y renonce
* Se la lisibilité (R) est évaluée dans le rapport

---
[question:BE408]