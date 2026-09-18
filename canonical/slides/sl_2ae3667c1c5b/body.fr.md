* La régulation automatique du gain (*AGC*) ajuste le signal BF de sortie en fonction des variations du signal HF d'entrée
* Utilisation par exemple en cas de fading
* Les variations de volume sonore sont réduites

---
## Fonctionnement

* Détection du niveau de réception à la sortie de la branche réceptrice
* Cela permet de réguler le gain HF
* Influence sur le volume sonore après la démodulation
* Possibilité d'ajuster le comportement de réponse (temps de montée, temps de descente)
<note>
* Ne pas confondre avec la régulation automatique de niveau (*ALC*) dans l'émetteur
</note>

---
## Modes AGC

<left>
* AGC Lent
* AGC Normal
* AGC Rapide
* AGC Désactivé
</left>
<right>
* BLU : AGC Lent ou Normal
* Morse : AGC Normal ou Rapide
* Modes numériques : AGC Rapide ou Désactivé
</right>
<note>
* Un comportement de réponse plus rapide permet d'éviter que des signaux forts n'écrasent des signaux faibles et que la régulation suive rapidement
</note>

---
[question:EF211]
---
[question:EF212]