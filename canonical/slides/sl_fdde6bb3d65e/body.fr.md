* Deux signaux HF puissants à l'entrée d'un récepteur → perturbations par intermodulation ou modulation croisée
* En cas d'*intermodulation*, l'étage du récepteur présente un comportement non linéaire → fréquences indésirables avec des interférences de superposition
* En cas de *modulation croisée*, le signal souhaité est influencé par un signal AM fort et adjacent → la modulation de l'émetteur adjacent est audible

---
[question:AF217]
---
[question:AF219]
---
[question:AF222]
---
[question:AF218]
---
### Circuit bouchon

<left>
[picture:434:a_inter_kreuzmodulation_saugkreis:Circuit bouchon devant un récepteur]
</left>
<right>
* Suppression du signal parasite avant le récepteur
* Le filtre est accordé sur la fréquence du signal parasite
* Le signal parasite est supprimé
</right>

---
[question:AF223]
---
### Robustesse aux forts signaux IP3

* Point d'interception d'ordre 3 (IP3)
* Mesure du point où les produits de mélange indésirables d'ordre 3 atteignent la valeur d'amplitude du signal d'entrée
* Plus l'IP3 d'un récepteur est élevé, plus de grands signaux peuvent être traités sans perturbation

---
[question:AF221]
---
### Atténuateur

* Atténuateur commutable à l'entrée du récepteur
* Les produits d'intermodulation et la modulation croisée sont réduits
* Le signal utile est réduit du facteur de l'atténuateur
* Les signaux parasites sont atténués de $\num{3}$ (ordre 3) en $\unit{dB}$
* Exemple : Atténuateur $\qty{10}{\dB}$ → signal utile $\qty{10}{\dB}$ → produits de mélange $\qty{30}{\dB}$

---
[question:AF220]
