### Diodes à semi-conducteurs dans les modulateurs

* Connues jusqu’ici comme redresseurs
* La tension BF modifie la résistance de la diode
* Le signal BF commande le courant de la diode
* Le signal HF est modulé au rythme du signal BF
* La variante la plus simple produit une porteuse et deux bandes latérales

---
### Diode dans un modulateur d’amplitude
<left>
[picture:772:a_modulatoren_am_modulator:Modulateur AM]
</left>
<right>
* Une diode est soumise simultanément à un signal BF et à un signal HF
* Un circuit oscillant LC filtre le signal de sortie
</right>

---
[question:AD507]

---
### Mélangeur équilibré pour la suppression de la porteuse
* Quatre diodes disposées en anneau suppriment la porteuse
* Un circuit en opposition de phase annule les signaux de porteuse
* Seules les bandes latérales subsistent
* Déjà présenté dans le chapitre « Mélangeurs II » sous le nom de mélangeur équilibré

---
### Modulateur équilibré dans un modulateur BLU
* Le modulateur équilibré génère un signal à double bande latérale (DSB)
* Un filtre passe-bande ne laisse passer qu’une seule bande latérale
* Il en résulte un signal BLU
* Deux étages sont nécessaires
 
---
[question:AE206]

---
[question:AF302]

---
### Identification d’un mélangeur équilibré
<left>
[picture:759:a_modulatoren_dsb:Modulateur pour signaux AM avec porteuse supprimée]
</left>
<right>
* Un anneau de diodes caractérise le mélangeur équilibré
* Il n’y a pas d’excitation complète en opposition de phase
* Un transformateur fournit l’équivalent d’une prise médiane
</right>

---
[question:AF308]

<note>
* La modulation BF est injectée dans la branche de pont entre la prise médiane de T2 et la masse
* Le signal de l’oscillateur est injecté dans l’anneau de diodes via T1
* Le signal DSB est découplé via T2
* Sans modulation, les diviseurs de tension sont à la masse
* La porteuse est ainsi supprimée
* Avec modulation, le potentiel se décale et un courant circule dans T2
* Le signal de sortie est généré
</note>

---
### Suppression de la porteuse et équilibrage

* La suppression de la porteuse permet d’annuler les signaux indésirables
* Le circuit du modulateur doit être équilibré

---
[question:AD510]

---
### Réglage dans le modulateur

<left>
[picture:762:a_modulatoren_rc_traegerunterdrueckung:$R_1$ et $C_1$ pour le réglage de la suppression de la porteuse en valeur absolue et en phase]
</left>
<right>
* Les amplitudes sont ajustées avec des potentiomètres
* Les phases sont réglées avec des condensateurs ajustables
</right>

---
[question:AF309]

---
### Symétrisation dans le modulateur

* Le modulateur est symétrisé pour supprimer la porteuse
* Les bandes latérales de modulation sont conservées

---
[question:AF304]

---
[question:AF303]

---
### Deuxième étage du modulateur BLU

<left>
[picture:98:a_modulatoren_blockschaltbild_sender:Schéma bloc d’un émetteur]
</left>
<right>
* Un filtre passe-bande suit le modulateur équilibré
* Il permet de sélectionner la bande latérale souhaitée
</right>

---
[question:AF305]

---
### Fréquence du quartz et position de la bande latérale

<left>
[picture:500:a_modulatoren_quarzfilter:Filtre à quartz pour la sélection de la bande latérale]
</left>
<right>
* Les quartz déterminent la fréquence de la porteuse supprimée
* Pour le LSB, la porteuse se situe à $\qty{1,5}{\kilo\hertz}$ au-dessus de la fréquence centrale de $\qty{9}{\mega\hertz}$
* Avec une excursion BF maximale de $\qty{3}{\kilo\hertz}$, le LSB se trouve à $\qty{1,5}{\kilo\hertz}$ en dessous de la fréquence centrale
* Pour le USB, c’est l’inverse
</right>

---
[question:AF306]

---
[question:AF307]
---
#### Méthode de résolution
* donné : $f_Q = \qty{9}{\mega\hertz}$
* donné : $f_{LSB} = \qty{9,0015}{\mega\hertz}$
* recherché : $f_{USB}$

<fragment>
$\begin{split}f_{USB} &= f_Q - (f_{LSB} - f_Q)\\ &= \qty{9}{\mega\hertz} - (\qty{9,0015}{\mega\hertz} - \qty{9}{\mega\hertz})\\ &= \qty{9}{\mega\hertz} - \qty{0,0015}{\mega\hertz}\\ &=\qty{8,9985}{\mega\hertz}\end{split}$ 
</fragment>

---
### Diodes varicap dans les modulateurs FM

<left>
[picture:951:a_modulatoren_fm_modulator:Modulateur FM avec varicap]
</left>
<right>
* Les modulateurs FM utilisent des diodes varicap
* La diode fait partie d’un circuit oscillant
* La tension inverse fixe une capacité de diode déterminée
* Un signal BF modifie la fréquence de l’oscillateur au rythme du signal
</right>

---
[question:AD508]

---
### Influence de la diode varicap

<left>
[picture:158:a_modulatoren_fm_varicap:Varicap pour influencer la fréquence de l’oscillateur]
</left>
<right>
* La diode varicap influence la fréquence de l’oscillateur
* Elle est connectée en parallèle au circuit oscillant
</right>

---
[question:AF310]

---
### Limitation de l’excursion FM
* Des tensions BF élevées entraînent des variations de fréquence excessives
* Une limitation de l’excursion est nécessaire
* Des diodes montées en antiparallèle limitent la tension à la tension de coude

---
[question:AD509]

---
### Analyse d’un signal de diode
<left>
[picture:142:a_modulatoren_regelspannung:Montage avec une sortie pour une tension de régulation]
</left>
<right>
* Un signal unique ne permet pas d’identifier un modulateur
* Un condensateur électrolytique en sortie indique une tension continue
</right>

---
[question:AD503]
