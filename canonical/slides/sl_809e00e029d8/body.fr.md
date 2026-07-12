## Convertisseur

* Les signaux sur une bande de fréquences sont convertis en une autre bande de fréquences
* Par exemple, un signal de $\qty{2}{\meter}$ en réception est émis comme un signal de $\qty{70}{\centi\meter}$
* Le signal est converti dans une seule direction
* En fait, un mélangeur simple

---
[question:EF504]

<note>
* TCXO et PLL seront traités plus tard
* Mais le mélange peut être calculé
</note>

---
[question:EF505]
---
## Transverter

* Dans le cas du transverter, la conversion se fait dans les deux directions
* La conversion se fait également par mélange

---
[question:EF501]
---
[question:EF502]
---
[question:EF503]
<note>
* La solution sera donnée sur la diapositive suivante
</note>
---
### Solution

La fréquence du générateur est triplée: $\qty{38,666}{\mega\hertz} \cdot 3 = \qty{116}{\mega\hertz}$

<left>
* Chemin TX*
* Les $\qtyrange{28}{30}{\mega\hertz}$ du TRX sont mélangés avec $\qty{116}{\mega\hertz}$
* Le signal peut être $\qtyrange{86}{88}{\mega\hertz}$ ou $\qtyrange{144}{146}{\mega\hertz}$
</left>
<right>
[picture:843:e_transverter_tx:Transverter dans le chemin TX]
</right>

---

<left>
* Chemin RX*
* Le signal de l'antenne est mélangé avec $\qty{116}{\mega\hertz}$ et $\qtyrange{28}{30}{\mega\hertz}$ en sort
* Le signal de l'antenne est donc, entre autres, à $\qtyrange{144}{146}{\mega\hertz}$
* $\rightarrow$ Seule la réponse avec $\qty{2}{\meter}$ et le transverter est correcte
</left>
<right>
[picture:842:e_transverter_rx:Transverter dans le chemin RX]
</right>

---
## Stabilité de fréquence

* Les convertisseurs et les transverters doivent être construits avec des oscillateurs à fréquence stable
* Si la fréquence dévie, la fréquence de sortie est également déviée

---
<left>
* Graphique de la question précédente
* De $\qty{10}{\mega\hertz}$ on obtient $\qty{2,256}{\giga\hertz}$, soit $\num{225,6}$ fois la multiplication
* Au lieu de $\qty{10}{\mega\hertz}$, l'oscillateur produit $\qty{10,01}{\mega\hertz}$ en raison d'une erreur
* $\qty{10,01}{\mega\hertz} \cdot 225,6 = \qty{2,258256}{\giga\hertz}$
* Mélangeur: $\qty{144}{\mega\hertz} + \qty{2,258256}{\giga\hertz} = \qty{2,402256}{\giga\hertz} \rightarrow \qty{2,256}{\mega\hertz}$ à côté
</left>
<right>
[picture:651:e_konverter_13cm:Convertisseur pour la bande de $\qty{13}{\centi\meter}$]
</right>