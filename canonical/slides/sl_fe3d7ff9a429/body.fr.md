---
## Charge utile dans la plage HF

<left>
[picture:47:a_dummy_load:Charge utile composée de plusieurs chaînes de résistances]
</left>
<right>
* Souvent composée de plusieurs résistances partielles pour une meilleure dissipation thermique et une capacité de charge
* Les résistances peuvent être connectées en parallèle, en série ou combinées
</right>
---

* Des valeurs de résistance identiques assurent une répartition uniforme de la puissance dissipée
* Le calcul est effectué selon la loi d'Ohm et les règles des circuits en série et en parallèle

---
[question:AI601]

--- style="font-size: smaller;"
#### Solution
<left>
* donné : $R = \qty{150}{\ohm}$
* donné : $R_S = 4\cdot \qty{150}{\ohm} = \qty{600}{\ohm}$
</left>
<right>
* donné : $R_{ges} = \qty{50}{\ohm}$
* donné : $P_R = \qty{1}{\watt}$
* recherché : $n$ résistances, $P$
</right>

<fragment>
Lignes avec 4 résistances chacune :
$\frac{1}{R_{ges}} = n_S \cdot \frac{1}{R_S} \Rightarrow n_S = \frac{R_S}{R_{ges}} = \frac{\qty{600}{\ohm}}{\qty{50}{\ohm}} = 12$
$n = 4 \cdot n_S = 4 \cdot 12 = 48$ 
</fragment>
<fragment>
$P = n \cdot P_R = 48 \cdot \qty{1}{\watt} = \qty{48}{\watt}$
</fragment>

---
### Charge utile avec sortie de mesure

* Peut être utilisée pour la mesure indirecte de la puissance de sortie d'un émetteur
* Le redresseur de valeur de crête convertit la tension HF en tension continue

---
[question:AI602]

---
### Mesure de la puissance de sortie HF via un diviseur de tension

* La charge utile avec prise intermédiaire permet une détermination approximative de la puissance
* La tension partielle HF est calculée via le rapport du diviseur de tension
* Mesure possible avec une sonde HF et un multimètre

---
[question:AI603]

