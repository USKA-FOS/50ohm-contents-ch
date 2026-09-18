## Mesures pour radioamateurs

* Mesures importantes : puissance de sortie et tensions HF
* La mesure de la **puissance de sortie de l'émetteur** nécessite une charge définie
* Impédance courante en radioamateurisme : $\qty{50}{\ohm}$
* Une mesure directe dans le circuit n'est judicieuse qu'en cas de faibles puissances

---
## Mesure de tension HF

* La tension HF est mesurée à l'aide d'une sonde HF
* Redressement par diode et lissage avec un condensateur en aval

---
### Sonde HF à redressement simple




<left>
[picture:576:a_messung_hf_tastkopf_leistungsmessung:Sonde pour la mesure de puissance HF via un diviseur de tension]
</left>
<right>
* Une diode en sortie fournit la tension de crête de la tension HF
* Moins la tension directe de la diode et, le cas échéant, la division de tension
</right>

---
[question:AI608]

---
### Sonde HF à double redressement

<left>
[picture:770:a_messung_hf_tastkopf_doppeldiode:Sonde HF avec deux diodes pour les deux alternances]
</left>
<right>
* Deux diodes pour améliorer la précision de mesure, notamment pour les faibles puissances
* Les deux alternances sont redressées
* Résultat : double tension de crête moins deux fois la tension directe des diodes
</right>

---
[question:AI605]

---
[question:AI604]

---
### Mesure de puissances HF élevées

* Nécessite un atténuateur robuste
* Absorbe une grande partie de la puissance
* L'atténuateur doit être pris en compte dans le calcul

---
[question:AI609]

<note>
Aucun calcul nécessaire, car il n'y a qu'une seule réponse avec atténuateur.
</note>

---
## Étalonnage des circuits de mesure

* Indispensable pour des mesures de puissance précises
* Des valeurs de correction doivent être établies

---
[question:AI612]

---
### Calcul d'une sonde HF

<left>
[picture:576:a_messung_messschaltung_beispiel_1:Exemple d'un circuit de mesure HF]
</left>
<right>
* Le signal d'entrée est terminé avec une impédance adaptée
* La tension est divisée par deux via un diviseur de tension
* Après redressement par diode, il reste la tension de crête moins la tension directe
</right>

---
[question:AI610]

--- style="font-size: smaller;"
#### Méthode de résolution

* donné : $P_E = \qty{1}{\watt}$
* donné : $U_F = \qty{0,23}{\volt}$
* donné : $R_V = \qty{110}{\ohm}$, $R_T = \qty{330}{\ohm}$
* recherché : $U_A$



<fragment>
$\begin{split}R &= \left(\frac{1}{R_T + R_T} + \frac{1}{R_V} + \frac{1}{R_V}\right)^{-1}\\ &= \left(\frac{1}{\qty{330}{\ohm} + \qty{330}{\ohm}} + \frac{1}{\qty{110}{\ohm}} + \frac{1}{\qty{110}{\ohm}}\right)^{-1}\\ &= \qty{50,77}{\ohm}\end{split}$
</fragment>

--- style="font-size: smaller;"
* donné : $P_E = \qty{1}{\watt}$
* donné : $U_F = \qty{0,23}{\volt}$
* calculé : $R = \qty{50,77}{\ohm}$
* recherché : $U_A$


<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ \Rightarrow U_{E,eff} &= \sqrt{P_E \cdot R}\\ &= \sqrt{\qty{1}{\watt} \cdot \qty{50,77}{\ohm}}\\ &= \qty{7,125}{\volt}\end{split}$
</fragment>

--- style="font-size: smaller;"
* donné : $U_F = \qty{0,23}{\volt}$
* calculé : $U_{E,eff} = \qty{7,125}{\volt}$
* recherché : $U_A$


<left>
<fragment>
$\begin{split}U_S &= U_{E,eff} \cdot \sqrt{2}\\ &= \qty{7,071}{\volt} \cdot 1,414\\ &= \qty{10,07}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_A &= \frac{U_S}{2}\,-\,U_F\\ &= \frac{\qty{10,07}{\volt}}{2}\,-\,\qty{0,23}{\volt}\\ &= \qty{5,035}{\volt}\,-\,\qty{0,23}{\volt}\\ &= \qty{4,805}{\volt} \approx \qty{4,8}{\volt}\end{split}$
</fragment>
</right>

---
### Calcul de la puissance d'entrée à partir de la tension continue mesurée


<left>
[picture:577:a_messung_messschaltung_beispiel_2:Exemple d'un circuit de mesure HF]
</left>
<right>
* La tension au niveau du diviseur de tension correspond à la tension de sortie plus la tension de la diode
* Calculer les valeurs efficaces
* Détermination de la puissance d'entrée via la résistance du circuit
</right>

---
[question:AI611]

--- style="font-size: smaller;"
#### Méthode de résolution
* donné : $U_A = \qty{14,9}{\volt}\text{ DC}$
* donné : $U_F = \qty{0,7}{\volt}$
* donné : $R_1 = \qty{54,1}{\ohm}$, $R_T = \qty{330}{\ohm}$
* recherché : $P_E$


<left>
<fragment>
$\begin{split}R &= \left(\frac{1}{R_T + R_T} + \frac{1}{R_1}\right)^{-1}\\ &= \left(\frac{1}{\qty{330}{\ohm} + \qty{330}{\ohm}} + \frac{1}{\qty{54,1}{\ohm}}\right)^{-1}\\ &= \qty{50}{\ohm}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_S &= \left(U_A + U_F\right) \cdot 2\\ &= \left(\qty{14,9}{\volt} + \qty{0,7}{\volt}\right) \cdot 2\\ &= \qty{31,2}{\volt}\end{split}$
</fragment>
</right>

--- style="font-size: smaller;"
<left>
* calculé : $R = \qty{50}{\ohm}$
* calculé : $U_S = \qty{31,2}{\volt}$
* recherché : $P_E$


<fragment>
$\begin{split}U_{E,eff}\\ &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{31,2}{\volt}}{1,414}\\ &= \qty{22,06}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ &= \frac{(\qty{22,06}{\volt})^2}{\qty{50}{\ohm}}\\ &\approx \qty{9,7}{\watt}\end{split}$
</fragment>
</right>

---
### Sonde HF à double redressement de crête

<left>
[picture:771:a_messung_hf_tastkopf_doppeldiode_2:Sonde HF à double redressement de crête]
</left>
<right>
* Calcul similaire à celui du redressement simple
* Prendre en compte la tension de crête double
* Tenir compte de la double tension directe des diodes
</right>

---
[question:AI607]

--- style="font-size: smaller;"
#### Méthode de résolution

* donné : $U_A = \qty{15,3}{\volt}\text{ DC}$
* donné : $U_F = \qty{0,23}{\volt}$
* donné : $R_{V1} = \qty{56}{\ohm}$, $R_{V2} = \qty{470}{\ohm}$
* recherché : $P_E$


<left>
<fragment>
$\begin{split}R &= \left(\frac{1}{R_{V1}} + \frac{1}{R_{V2}}\right)^{-1}\\ &= \left(\frac{1}{\qty{56}{\ohm}} + \frac{1}{\qty{470}{\ohm}}\right)^{-1}\\ &= \qty{50,04}{\ohm}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_S &= \frac{U_A}{2} + U_F\\ &= \frac{\qty{15,3}{\volt}}{2} + \qty{0,23}{\volt}\\ &= \qty{7,88}{\volt}\end{split}$
</fragment>
</right>

--- style="font-size: smaller;"
<left>
* calculé : $R = \qty{50,04}{\ohm}$
* calculé : $U_S = \qty{7,88}{\volt}$
* recherché : $P_E$


<fragment>
$\begin{split}U_{E,eff} &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{7,88}{\volt}}{1,414}\\ &= \qty{5,57}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ &= \frac{{\qty{5,57}{\volt}}^2}{\qty{50,04}{\ohm}}\\ &\approx \qty{600}{\milli\watt}\end{split}$
</fragment>
</right>

---
[question:AI606]

--- style="font-size: smaller;"
#### Méthode de résolution

* donné : $U_A = \qty{15,3}{\volt}\text{ DC}$
* donné : $U_F = \qty{0,23}{\volt}$
* donné : $R = \qty{50}{\ohm}$ issu du système de mesure
* recherché : $P_E$


<left>
<fragment>
$\begin{split}U_S &= \frac{U_A}{2} + U_F\\ &= \frac{\qty{15,3}{\volt}}{2} + \qty{0,23}{\volt}\\ &= \qty{7,88}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_{E,eff} &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{7,88}{\volt}}{1,414}\\ &= \qty{5,57}{\volt}\end{split}$
</fragment>
</right>

--- style="font-size: smaller;"
* calculé : $U_{E,eff} = \qty{5,57}{\volt}$
* donné : $R = \qty{50}{\ohm}$ issu du système de mesure
* recherché : $P_E$


<fragment>
$\begin{split}P_E &= \frac{(U_{E,eff} \cdot 10)^2}{R}\\ &= \frac{(\qty{5,57}{\volt} \cdot 10)^2}{\qty{50}{\ohm}}\\ &\approx \qty{60}{\watt}\end{split}$
</fragment>

---
### Indicateur d'intensité de champ pour la mesure de puissance

<left>
[picture:496:a_messung_feldstaerkeanzeiger:Indicateur d'intensité de champ]
</left>
<right>
* Mesure de la puissance HF via une antenne
* La HF reçue est redressée et tamponnée
* Affichage via un ampèremètre sensible
* Plus l'aiguille dévie, plus l'intensité de champ HF est élevée
* Des mesures précises nécessitent un étalonnage
</right>

---
[question:AI613]
