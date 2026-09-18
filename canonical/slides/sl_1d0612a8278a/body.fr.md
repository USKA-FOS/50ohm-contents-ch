<left>
[image:648:n_relaisfunkstellen_aufbau:Représentation schématique d’une station relais avec utilisateurs]
</left>
<right>
* Permet une portée plus grande qu’un contact direct
* Généralement installée à des emplacements exposés, par exemple des sommets de montagne, des gratte-ciels, des clochers (d’église)
* Ou encore à bord de satellites
</right>

<note>
* La montagne ne permet pas de transmettre directement
* Grâce au relais, les deux radioamateurs peuvent établir une liaison
* Les satellites seront abordés plus tard
</note>

---

## Définition d’une station relais
station radioamateur télécommandée (y compris les satellites), qui émet à distance les émissions radioamateurs reçues, des parties de celles-ci ou d’autres signaux injectés ou mémorisés, et qui sert ainsi à augmenter la portée des stations radioamateurs


---

<left>
* Surnommée aussi relais ou répéteur
* Émet régulièrement son indicatif d’appel
* L’indicatif commence généralement par DB0, DM0 ou DO0
</left>
<fragment>
<right>
* Les stations relais ne sont pas exploitées avec des indicatifs personnels.
* Les stations relais ne sont généralement pas occupées en permanence.
* Les stations relais ne sont pas obligatoirement installées à des emplacements géographiquement exposés.
</right>
</fragment>

---

[question:VD118]
---

## Fonctionnement
<left>
* Reçoit sur la fréquence d’entrée le signal d’une station radioamateur
* Le retransmet simultanément sur la fréquence de sortie
* Pour éviter les interférences, les fréquences sont généralement différentes
</left>
<right>
<fragment>
L’écart entre ces fréquences est appelé *décalage* ou *écart*


| r: Bande | r: Décalage |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Décalage des fréquences]
</fragment>
</right>

---
Exemple d’un relais $\qty{70}{\centi\meter}$ :
* Fréquence d’entrée : $\qty{431,275}{\mega\hertz}$
* Décalage : $\qty{+7,600}{\mega\hertz}$
* Fréquence de sortie : $\qty{438,875}{\mega\hertz}$

---

[question:BE401]
---

[question:BE402]
---

[question:BE403]
---

## Fonctionnement en crossband
* Émet et reçoit simultanément sur deux bandes différentes, par exemple $\qty{2}{\meter}$ et $\qty{70}{\centi\meter}$
* Conversion du mode d’émission possible, par exemple BLU vers FM

---

## Digipeater
* Achemine des données au lieu de la voix
* Reçoit et émet des paquets de données
* L’émission peut se faire par parties ou avec un décalage temporel
* Les paquets de données peuvent être répétés
* Certains champs de données peuvent être modifiés

<note>
* Utilisé pour le Packet Radio, populaire dans les années 1990 avant l’ère d’Internet
* Abordé plus en détail ultérieurement
</note>

---

[question:NF118]
---

## Paramètres particuliers
* Des réglages supplémentaires peuvent être nécessaires pour établir la liaison avec le relais
* Ces informations sont disponibles dans les annuaires de répéteurs, sur des sites web ou auprès du responsable du relais
* En plus des répéteurs FM, il existe des répéteurs pour les modes numériques comme le DMR ou le D-Star

<note>
Un exemple de réglage supplémentaire est un sous-ton avec CTCSS
</note>

---

[question:NE309]
---

[question:NE308]
---

## Largeur de canal
* L’espace nécessaire dans le spectre de fréquences
* FM large : $\qty{25}{\kilo\hertz}$
* FM étroite : $\qty{12,5}{\kilo\hertz}$
* Les répéteurs privilégient la FM étroite, car sinon les signaux sont déformés et les fréquences voisines sont perturbées

---

[question:BE407]
---

## Exploitation sans interférences
* En principe, tout radioamateur peut utiliser les stations radioamateurs télécommandées avec son indicatif attribué
* L’exploitant peut exclure des radioamateurs pour garantir un fonctionnement sans interférences
* La BNetzA doit en être informée

---

[question:VD504]
---

## Exploitation radio sur les répéteurs
* Échanges courts
* Les stations mobiles ou portables sont souvent à portée de réception pendant une courte durée
* Pause entre les échanges pour permettre aux autres stations de se signaler

---

[question:BE406]
---

[question:BE404]
---

## Double appel
* Si deux stations émettent simultanément, l’émission est brouillée au point de devenir inaudible
* Éviter le "double appel" en assurant une bonne transition
* Ne commencer l’émission qu’une fois la station précédente terminée

---

[question:NE310]
---

[question:BE405]
---

## Puissance d’émission
* Selon l’annexe 1 de l’AFuV
* Pour les stations automatiques au-dessus de $\qty{30}{\mega\hertz}$ : $\qty{50}{\watt}$ de puissance rayonnée apparente (ERP)

---

[question:VD503]
---

## Rapport
* L’intensité du signal (S) reçue est celle du relais
* Elle n’est pas prise en compte
* Seul le niveau de lisibilité (R) est évalué dans le rapport
