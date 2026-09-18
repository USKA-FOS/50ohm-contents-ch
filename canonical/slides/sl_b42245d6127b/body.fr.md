## Correction d'erreurs par anticipation (FEC)

* Si le **récepteur** détecte une erreur (par exemple à l'aide de bits de contrôle), il peut demander une nouvelle **transmission**
* Avec la correction d'erreurs par anticipation, on ajoute une redondance supplémentaire (par exemple, des bits de contrôle supplémentaires)
* Ainsi, non seulement l'erreur est détectée, mais aussi sa position exacte → le **bit** défectueux peut être corrigé
* En anglais, on parle de *Forward Error Correction* (FEC)

---

[question:AE413]

---

[question:AE414]

---

## Code de Hamming – Correction d'erreurs en détail

* Le code de Hamming utilise plusieurs *parity bits* pour non seulement détecter, mais aussi corriger les erreurs
* Objectif : localiser et corriger une erreur isolée sur un **bit**

---

<left>
[picture:683:hamming1:Transmission de 11 bits]
</left>
<right>
* Exemple : **transmission** d'un mot de données de 11 **bits**
* Objectif : détection et correction d'erreurs sur un **bit** défectueux
</right>

---

<left>
[picture:682:hamming2:Désignation alphabétique des positions de bits]
</left>
<right>
* Les positions des **bits** sont désignées par des lettres pour identifier les différentes zones
</right>

---

<left>
[picture:684:hamming3:Réorganisation avec bits supplémentaires]
</left>
<right>
* Organisation des bits de données avec des positions supplémentaires pour les *parity bits*
</right>

---

<left>
[picture:685:hamming4:Quatre parity bits dans le code de Hamming]
</left>
<right>
* Au lieu d'un seul bit de contrôle, quatre *parity bits* ($p_1$–$p_4$) sont utilisés
* Ceux-ci couvrent différentes zones des bits de données, à l'image d'une grille de mots croisés
</right>

---

<left>
[picture:686:hamming5:Attribution des zones de parité]
</left>
<right>
* Chaque *parity bit* protège une zone spécifique des bits de données
</right>

---

<left>
[picture:687:hamming6:Calcul des parity bits (parité paire)]
</left>
<right>
* Pour chaque zone, le *parity bit* est calculé selon la parité paire
* En cas d'erreur, les zones concernées sont identifiées et corrigées
</right>

---

<left>
[picture:687:hamming6:Calcul des parity bits (parité paire)]
</left>
<right>
* Grâce à la combinaison des zones de parité, l'emplacement du **bit** défectueux est déterminé
* Exemple : si un **bit** (par exemple le **bit** $k$) est modifié pendant la **transmission**, toutes les vérifications de parité associées échouent → l'erreur se situe donc au niveau du **bit** $k$
