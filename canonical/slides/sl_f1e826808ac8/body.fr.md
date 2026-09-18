## Démodulation des signaux

* La démodulation convertit un signal HF modulé en un signal BF audible
* Selon le type de modulation utilisé, une méthode de démodulation adaptée est choisie
* Objectif : restaurer le signal BF d'origine

---
### Démodulation AM

<left>
[picture:141:demodulator_huellkurvendemodulator_am:Démodulateur à enveloppe pour la démodulation des signaux AM]
</left>
<right>
* Les signaux AM sont traités par un démodulateur à enveloppe
* Le signal HF est sélectionné via un circuit oscillant et redressé
* Le condensateur se charge $\rightarrow$ la résistance se décharge avec une constante de temps définie
</right>

---

[question:AD501]

---

<left>
[picture:607:demodulator_huellkurvendemodulator_am_2:Démodulateur à enveloppe avec signal d'entrée FI]

[picture:146:demodulator_huellkurvendemodulator_am_abbx:Signal démodulé au point X]
</left>
<right>
* Point X : affichage de la tension de crête redressée
* Légère baisse de la tension due à la décharge parallèle
* L'enveloppe correspond à la BF modulée, superposée à un signal en dents de scie
* Un filtrage ultérieur élimine la composante porteuse
</right>

---

[question:AD502]

--- style="font-size: smaller;"
### Démodulation FM

<left>
[picture:841:demodulator_flankendiskriminator:Circuit oscillant utilisé comme discriminateur de flanc]

[picture:149:demodulator_flankendiskriminator_schaltung:Discriminateur de flanc FM]
</left>
<right>
* Démodulation FM à l'aide d'un discriminateur de flanc
* Le signal issu de la fréquence intermédiaire (FI) est appliqué à un circuit oscillant
* Circuit oscillant : fréquence de résonance $f_\text{res}$ légèrement décalée par rapport à $f_\text{FI}$
* Les variations de fréquence sont converties en variations d'amplitude
* Un démodulateur AM en aval fournit le signal BF
</right>

---

[question:AD504]

---

#### Démodulation FM à l'aide d'une PLL

<left>
[picture:77:a_fm_demodulation_pll:Schéma bloc d'une démodulation FM par PLL]
</left>
<right>
* Une PLL utilise un oscillateur commandé en tension (VCO) qui suit le signal d'entrée
* La tension de régulation correspond à la modulation FM (BF modulée)
* Prélèvement du signal pour un traitement BF ultérieur
</right>

---

[question:AD505]

---
### Démodulation BLU

* Démodulation BLU à l'aide d'un détecteur de produit
* Un mélangeur en anneau mélange la fréquence intermédiaire (FI) avec un oscillateur à fréquence de battement (BFO)
* Le produit de mélange obtenu est le signal BF BLU souhaité
* Le BFO doit être précisément accordé sur la porteuse supprimée

---

[question:AD506]