* *Classe A* : peut amplifier l'intégralité du signal
* *Classe B* : environ la moitié du signal est bien amplifiée
* *Classe A/B* : combinaison des classes A et B avec amplification d'un peu plus de la moitié du signal
* *Classe C* : moins de la moitié du signal est bien amplifiée

<fragment>
Les classes d'amplification sont déterminées par le choix du point de fonctionnement.
</fragment>

<note>
Les désignations par lettres proviennent d'une classification systématique précoce des amplificateurs à tubes et à transistors.
</note>
---
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'un transistor avec points de fonctionnement]
</left>
<right>
* La caractéristique du transistor montre la relation entre le signal d'entrée et le signal de sortie
* Tension base-émetteur ou tension grille-source et courant de collecteur ou courant de drain
* Dans les zones linéaires, la variation est proportionnelle
* D'autres zones sont non linéaires
</right>
---
### Point de fonctionnement

* Fonctionnement optimal grâce à un choix approprié du point de fonctionnement sur la caractéristique
* Le point de fonctionnement est déterminé par la polarisation de la base ou de la grille
* L'amplification agit alors autour du point de fonctionnement souhaité

---
### Courant de repos

* Le courant de repos résulte du choix du point de fonctionnement
* Il circule même sans signal d'entrée
* Influence l'efficacité d'un amplificateur
* Augmente la puissance dissipée thermique
* Réduit le rendement

--- style="font-size: smaller;"
### AP1
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'un transistor avec points de fonctionnement]  
</left>
<right>
* Fonctionnement en classe C de l'amplificateur
* Sans polarisation
* Courant de repos nul
* Rendement d'environ $\qtyrange{80}{87}{\percent}$
* Taux élevé d'harmoniques
</right>
--- style="font-size: smaller;"
### AP2
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'un transistor avec points de fonctionnement]  
</left>
<right>
* Fonctionnement en classe B de l'amplificateur
* Faible polarisation jusqu'à l'apparition du courant de collecteur
* Courant de repos presque nul (faible)
* Rendement jusqu'à $\qty{80}{\percent}$
* Faible taux d'harmoniques
</right>
--- style="font-size: smaller;"
### AP3
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'un transistor avec points de fonctionnement]  
</left>
<right>
* Fonctionnement en classe A/B de l'amplificateur
* Polarisation plus élevée qu'en classe B, mais inférieure à celle de la classe A
* Courant de repos supérieur à celui de la classe B, mais nettement inférieur à celui de la classe A
* Rendement entre $\qty{50}{\percent}$ et $\qty{80}{\percent}$
* Faible taux d'harmoniques
</right>
--- style="font-size: smaller;"
### AP4
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'un transistor avec points de fonctionnement]  
</left>
<right>
* Fonctionnement en classe A de l'amplificateur
* La polarisation est choisie de manière à ce que le courant de repos atteigne environ $\qty{50}{\percent}$ de la valeur maximale admissible
* Rendement d'environ $\qty{40}{\percent}$
* Taux d'harmoniques très faible
</right>
---
[question:AD416]
---
[question:AD419]
---
[question:AD420]
---
[question:AD421]
---
### Puissance de sortie

* Une fois le point de fonctionnement connu, le rendement est déterminé
* Calculer la puissance en courant continu
* La puissance de sortie est le produit de la puissance en courant continu et du rendement

---
[question:AD424]
---
#### Méthode de résolution
* donné : $U=\qty{50}{\volt}$
* donné : $I = \qty{2}{\ampere}$
* donné : $\eta_\text{A} \approx \qty{40}{\percent}$
* recherché : $P_\text{ab}$

<fragment>
$P_\text{zu} = U \cdot I = \qty{50}{\volt} \cdot \qty{2}{\ampere} = \qty{100}{\watt}$
</fragment>
<fragment>
$\eta_\text{A} = \frac{P_\text{ab}}{P_\text{zu}} \Rightarrow P_\text{ab} = \eta_\text{A} \cdot P_\text{zu} = 0,4 \cdot \qty{100}{\watt} = \qty{40}{\watt}$
</fragment>
---
[question:AD425]
---
#### Méthode de résolution
* donné : $U=\qty{50}{\volt}$
* donné : $I = \qty{2}{\ampere}$
* donné : $\eta_\text{C} \approx \qty{85}{\percent}$
* recherché : $P_\text{ab}$

<fragment>
$P_\text{zu} = U \cdot I = \qty{50}{\volt} \cdot \qty{2}{\ampere} = \qty{100}{\watt}$
</fragment>
<fragment>
$\eta_\text{C} = \frac{P_\text{ab}}{P_\text{zu}} \Rightarrow P_\text{ab} = \eta_\text{C} \cdot P_\text{zu} = 0,85 \cdot \qty{100}{\watt} = \qty{85}{\watt}$
</fragment>
---
[question:AD418]
---
[question:AD417]
---
### Fonctionnement BLU

* Une amplification linéaire est nécessaire
* Amplification en classe A, A/B ou B
* En cas de surmodulation, des distorsions du signal apparaissent $\rightarrow$ splatter sur les fréquences adjacentes

---
[question:AD422]
---
[question:AJ218]
---
[question:AD423]
---
### Classe C

* Le point de fonctionnement non linéaire génère des harmoniques
* Doivent être supprimées par filtrage
* Blindage par un boîtier métallique

---
[question:AF402]
---
[question:AF403]
