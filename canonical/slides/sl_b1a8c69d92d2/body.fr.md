## Échantillonnage : De l'analogique au numérique

* Les signaux analogiques sont convertis en valeurs numériques par échantillonnage
* L'échantillonnage se fait à intervalles de temps définis – seuls les états instantanés sont mesurés
* Les signaux analogiques sont continus dans le temps, car ils n'ont pas de plus petite résolution temporelle
* Les échantillons numériques sont discrets dans le temps, car un intervalle d'échantillonnage fixe existe

---

[include:quantisierung_und_sampling]

---

## Continuité de valeur vs. Discrétion de valeur

* Les signaux analogiques peuvent prendre n'importe quelle valeur de tension – ils sont continus en valeur
* Lors de la numérisation, il n'y a que des paliers limités (par exemple de $\num{-128}$ à $\num{+127}$) – les échantillons sont discrets en valeur
* Entre deux paliers de tension, le convertisseur A/N doit prendre une décision (quantification)

---

## Exemple pratique : Dimmer vs. Interrupteur à étages

* Un dimmer analogique permet des réglages de luminosité fins et progressifs
* Un interrupteur à étages (par exemple $\num{5}$ étages) ne permet que des valeurs de luminosité fixes – les étapes intermédiaires ne sont pas possibles
* Quantification : sélection de l'étage le plus proche pour représenter la valeur analogique

---

[question:AF601]

---

[question:AF603]

---

[question:AF602]

---

[question:AF604]