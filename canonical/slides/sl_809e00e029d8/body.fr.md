## Convertisseur

* Les signaux d'une bande de fréquences sont transposés vers une autre bande de fréquences
* Par exemple, un signal de la bande $\qty{2}{\meter}$ est émis en réception sur la bande $\qty{70}{\centi\meter}$
* La conversion ne s'effectue que dans un seul sens
* En réalité, il s'agit d'un simple mélangeur

---
[question:EF504]

<note>
* Les TCXO et PLL seront abordés plus tard
* Mais le mélange peut déjà être calculé
</note>

---
[question:EF505]
---
## Transverter

* Le transverter permet une conversion dans les deux sens
* La transposition s'effectue également par mélange

---
[question:EF501]
---
[question:EF502]
---
[question:EF503]
<note>
* La méthode de résolution sera présentée sur la diapositive suivante
</note>
---
### Méthode de résolution

La fréquence de l'oscillateur est triplée : $\qty{38,666}{\mega\hertz} \cdot 3 = \qty{116}{\mega\hertz}$

<left>
*Voie TX*
* Les $\qtyrange{28}{30}{\mega\hertz}$ du TRX sont mélangées avec $\qty{116}{\mega\hertz}$
* Le signal peut être $\qtyrange{86}{88}{\mega\hertz}$ ou $\qtyrange{144}{146}{\mega\hertz}$
</left>
<right>
[picture:843:e_transverter_tx:Transverter en voie TX]
</right>

---

<left>
*Voie RX*
* Le signal de l'antenne est mélangé avec $\qty{116}{\mega\hertz}$ et produit $\qtyrange{28}{30}{\mega\hertz}$
* Le signal de l'antenne se situe donc notamment sur $\qtyrange{144}{146}{\mega\hertz}$
* $\rightarrow$ Seule la réponse avec $\qty{2}{\meter}$ et le transverter est correcte
</left>
<right>
[picture:842:e_transverter_rx:Transverter en voie RX]
</right>

---
## Stabilité de fréquence

* Les convertisseurs et transverters doivent être construits avec des oscillateurs stables en fréquence
* Si la fréquence dérive, la fréquence de sortie dérive également

---
<left>
* Graphique issu de la question précédente
* À partir de $\qty{10}{\mega\hertz}$, on obtient $\qty{2,256}{\giga\hertz}$, soit une multiplication par $\num{225,6}$
* Au lieu de $\qty{10}{\mega\hertz}$, l'oscillateur génère $\qty{10,01}{\mega\hertz}$ en raison d'une erreur
* $\qty{10,01}{\mega\hertz} \cdot 225,6 = \qty{2,258256}{\giga\hertz}$
* Mélangeur : $\qty{144}{\mega\hertz} + \qty{2,258256}{\giga\hertz} = \qty{2,402256}{\giga\hertz} \rightarrow \qty{2,256}{\mega\hertz}$ décalé
</left>
<right>
[picture:651:e_konverter_13cm:Convertisseur pour la bande $\qty{13}{\centi\meter}$]
</right>