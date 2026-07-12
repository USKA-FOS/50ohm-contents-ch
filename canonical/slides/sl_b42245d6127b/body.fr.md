## Correction d'erreur directe (FEC)

* Si le récepteur détecte une erreur (par exemple au moyen de bits de contrôle), il peut demander une nouvelle transmission 
* Dans le cas de la correction d'erreur directe, une redondance supplémentaire (par exemple des bits de contrôle supplémentaires) est ajoutée 
* Ainsi, non seulement on détecte qu'une erreur est présente, mais on sait aussi à quel endroit $\rightarrow$ le bit erroné peut être corrigé
* En anglais, on parle de Forward Error Correction (FEC)

---

[question:AE413]

---

[question:AE414]

---

## Code de Hamming – Correction d'erreur en détail

* Le code de Hamming utilise plusieurs bits de parité pour non seulement détecter les erreurs, mais aussi les corriger 
* Objectif : localiser et corriger une erreur de bit unique

---

<left>
[picture:683:hamming1:Transmission de 11 bits]
</left>
<right>
* Exemple : transmission d'un mot de données de 11 bits 
* Objectif : détection et correction d'erreur en cas d'erreur de bit
</right>

---

<left>
[picture:682:hamming2:Désignation alphabétique des positions des bits]
</left>
<right>
* Les positions des bits sont désignées par des lettres alphabétiques pour identifier les différentes zones
</right>

---

<left>
[picture:684:hamming3:Réorganisation avec des bits supplémentaires]
</left>
<right>
* Disposition des bits de données avec des positions de bits supplémentaires pour les bits de parité
</right>

---

<left>
[picture:685:hamming4:Quatre bits de parité dans le code de Hamming]
</left>
<right>
* Au lieu d'un seul bit de contrôle, quatre bits de parité ($p_1$–$p_4$) sont utilisés 
* Ceux-ci couvrent différentes zones des bits de données – de manière similaire à un mot croisé
</right>

---

<left>
[picture:686:hamming5:Attribution des zones de parité]
</left>
<right>
* Chaque bit de parité sécurise une certaine zone des données
</right>

---

<left>
[picture:687:hamming6:Calcul des bits de parité (Parité paire)]
</left>
<right>
* Pour chaque zone, le bit de parité est calculé au moyen d'une parité paire 
* Si une erreur se produit, les zones erronées peuvent être identifiées et corrigées
</right>

---

<left>
[picture:687:hamming6:Calcul des bits de parité (Parité paire)]
</left>
<right>
* Grâce à la combinaison des zones de parité, l'emplacement du bit erroné peut être déterminé 
* Exemple : Si un certain bit (par exemple le bit $k$) est modifié pendant la transmission, toutes les vérifications de parité associées échouent – l'erreur se situe donc au niveau du bit $k$
</right>

