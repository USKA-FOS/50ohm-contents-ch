## Amplificateur de puissance HF

* Amplifient le signal HF issu des étages précédents
* Objectif : atteindre la puissance de sortie souhaitée
* Deux types : amplificateurs HF large bande et sélectifs

---
### Amplificateurs HF large bande

<left>
[picture:491:a_verstaerker_breitband_gegentaktverstaerker:Amplificateur push-pull large bande]
</left>
<right>
* Amplification uniforme sur une large bande de fréquences (par ex. $\qtyrange{1}{30}{\mega\hertz}$)
* Reconnaissables aux transformateurs de couplage large bande
* Pas de condensateurs en parallèle ou en série formant un circuit oscillant
</right>

---
[question:AF412]

---
### Amplificateurs HF sélectifs

<left>
[picture:778:a_verstaerker_selektiver_hf_verstaerker:Amplificateur HF sélectif]
</left>
<right>
* Gain maximal uniquement dans une bande étroite (par ex. une bande amateur)
* Conception à sélectivité fréquentielle
* Utilisation de circuits oscillants en série ou en parallèle dans le trajet du signal HF
</right>

---
[question:AF408]

---
# Amplificateurs multi-étages

<left>
[picture:764:a_verstaerker_zweistufiger_breitband_hf_verstaerker:Amplificateur HF large bande à deux étages]
</left>
<right>
* Les amplificateurs peuvent être conçus en plusieurs étages par enchaînement d'étages individuels
</right>

---
[question:AF413]

---
## Adaptation d'impédance entre les étages d'amplification

* Nécessaire pour un gain maximal, une distorsion minimale et un rendement optimal
* Empêche les réflexions et les non-linéarités

---
### Méthodes d'adaptation d'impédance

* Adaptation large bande par transformateur avec un rapport de transformation adapté
* Adaptation sélective en fréquence par circuit oscillant à prise intermédiaire

---

[picture:765:a_anpassung_breitbandige_anpassung:Adaptation large bande entre deux étages au moyen d'un transformateur avec rapport de transformation adapté]

---
[question:AF414]

---

[picture:786:a_anpassung_mosfet:Adaptation large bande en entrée et en sortie sur des MOSFET basse impédance au moyen de transformateurs]

---
[question:AF417]

---

[picture:779:a_anpassung_induktiver_spannungsteiler:Adaptation sélective en fréquence avec une bobine comme diviseur de tension inductif]

---
[question:AF409]

---

[picture:780:a_anpassung_kapazitiver_spannungsteiler:Adaptation sélective en fréquence avec un condensateur comme diviseur de tension capacitif]

---
[question:AF410]

---

[picture:768:a_anpassung_eingang_schwingkreis:Circuit oscillant avec condensateurs variables pour l'adaptation de l'impédance d'entrée]

---
[question:AF407]

---

[picture:769:a_anpassung_ausgang_schwingkreis:Circuit oscillant avec condensateurs variables pour l'adaptation de l'impédance de sortie]

---
[question:AF406]

---
### Filtre en π pour l'adaptation d'impédance

* Adapte les impédances d'entrée et de sortie par le rapport des capacités
* La bobine définit, avec les condensateurs, la fréquence de conception
* Caractère passe-bas : suppression des harmoniques

---
[question:AF405]

---
### Circuit LC en aval d'un amplificateur de puissance HF

* Permet l'adaptation d'impédance et la suppression simultanée des harmoniques

---
[question:AF404]

---
## Rendement d'un amplificateur de puissance HF

* Rapport entre la puissance HF de sortie délivrée et la puissance d'alimentation en courant continu fournie

---
[question:AF401]

---
## Tension de polarisation dans les amplificateurs de puissance

<left>
[picture:786:a_verstaerker_bias_arbeitspunkt:Réglage du point de fonctionnement dans un amplificateur au moyen d'un potentiomètre]
</left>
<right>
* Réglage de la tension de service par diviseur de tension
* Réglage fin au moyen d'un potentiomètre ajustable
* Considération en courant continu : les condensateurs sont ignorés, les bobines sont considérées comme des courts-circuits
</right>

---
[question:AF420]

---
[question:AF423]

---
[question:AF424]

---
### Calcul de la tension de polarisation

* Application de la loi d'Ohm
* Prise en compte des montages en parallèle et en série de résistances
* Les connexions de grille des transistors sont capacitives et négligeables en considération en courant continu

---
[question:AF421]

--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $U_Z = \qty{6,2}{\volt}$
* donné : $R_2 = \qty{270}{\ohm}$
* donné : $R_3 = \qty{220}{\ohm}$
</left>
<right>
* donné : $R_4 = \qty{6,8}{\kilo\ohm}$
* donné : $R_6 = \qty{150}{\ohm}$
* recherché : $U_{GS}$
</right>

<left>
<fragment>
$\begin{split}R_E &= \frac{(R_3+R_6) \cdot R_4}{(R_3 + R_6) + R_4}\\ &= \frac{(\qty{220}{\ohm} + \qty{150}{\ohm}) \cdot \qty{6,8}{\kilo\ohm}}{\qty{220}{\ohm} + \qty{150}{\ohm} + \qty{6,8}{\kilo\ohm}}\\ &= \frac{\qty{2,516}{\mega\ohm}^2}{\qty{7170}{\ohm}}\\ &= \qty{351}{\ohm}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}\frac{U_Z}{U_{GS}} &= \frac{R_2 + R_E}{R_E}\\ \Rightarrow \frac{\qty{6,2}{\volt}}{U_{GS}} &= \frac{\qty{270}{\ohm}+\qty{351}{\ohm}}{\qty{351}{\ohm}}\\ &= 1,77\\ \Rightarrow U_{GS} &= \frac{\qty{6,2}{\volt}}{1,77}\\ &= \qty{3,50}{\volt}\end{split}$
</fragment>
</right>

---
## Découplage HF de la tension de service

* Empêche les rétroactions entre les étages d'amplification (par ex. tendance à l'oscillation)
* Réalisation par des inductances en série et des condensateurs de découplage
* Caractère passe-bas : la tension continue est maintenue, la HF est bloquée

---

[picture:781:a_entkopplung_drossel:Bobine d’arrêt pour le découplage de la HF de la tension de service]

---
[question:AF411]

---
[question:AF422]

---

[picture:786:a_entkopplung_abblock_kondensatoren:Condensateurs de découplage pour le découplage de la HF de la tension de service avec caractère passe-bas]

---
[question:AF419]

---
[question:AF418]

---
## Propriétés HF des condensateurs

* Les grandes capacités (par ex. condensateurs électrolytiques) ne sont utilisables qu'à basse fréquence
* Pour les applications HF, combinaison de différentes valeurs de capacité pour couvrir une large bande de fréquences

---
[question:AF415]

---
## Gain total d'un amplificateur de puissance

<left>
[picture:470:a_verstaerker_gesamtverstaerkung:Schéma bloc d'un amplificateur avec gain et perte par étage]
</left>
<right>
* Déterminé par la différence entre la puissance de sortie et la puissance d'entrée
* Calcul par soustraction algébrique des valeurs en dBm
</right>

---
[question:AF428]
---
#### Méthode de résolution

* donné : $P_1 = \qty{0,3}{\milli\watt}$ ou $\qty{-5}{\dBm}$
* donné : $P_2 = \qty{20}{\watt}$ ou $\qty{43}{\dBm}$
* recherché : $g$

<left>
<fragment>
$\begin{split}g &= P_2 - P_1\\ &= \qty{43}{\dBm} - (\qty{-5}{\dBm})\\ &= \qty{43}{\dBm} + \qty{5}{\dBm}\\ &= \qty{48}{\dB}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}g &= \qty{10 \cdot \log_{10}{\left(\frac{P_2}{P_1}\right)}}{\dB}\\ &= \qty{10 \cdot \log_{10}{\left(\frac{\qty{20}{\watt}}{\qty{0,3}{\milli\watt}}\right)}}{\dB} \\ &\approx \qty{48}{\dB}\end{split}$
</fragment>
</right>