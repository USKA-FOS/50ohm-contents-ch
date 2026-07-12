* Procédé de modulation numérique pour la transmission de données 
* Modification de la phase d'un signal porteur pour représenter des valeurs binaires 
* Moins sensible au bruit d'amplitude $\rightarrow$ permet des débits de données plus élevés

---
## Principe de la modulation de phase

<left>
[picture:705:psk:Modulation de phase (Phase-shift Keying)]
</left>
<right>
<fragment>
*BPSK (Binary Phase Shift Keying)*
* Deux angles de phase : $\qty{0}{\degree}$ et $\qty{180}{\degree}$  
* Chaque angle représente une valeur binaire ($\num{0}$ ou $\num{1}$)
</fragment>
</right>

---
Variantes supérieures :  

* *QPSK (Quadrature PSK)*: Quatre phases ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$, $\qty{270}{\degree}$) – $\qty{2}{\text{Bits par symbole}}$
* *8-PSK*: Huit phases – $\qty{3}{\text{Bits par symbole}}$


---

## Signaux PSK dans la représentation temporelle

* L'amplitude reste constante ; seule la phase change  
* *BPSK* : Saut brutal de l'amplitude positive à l'amplitude négative lors du changement de bit  
* *QPSK* : Plusieurs angles de phase avec des transitions plus petites, ce qui rend la courbe plus lisse

---

## Détection des signaux PSK

* *Dans le domaine temporel* : Changements de phase nets et abrupts  
* *Dans le diagramme de phase (Constellation Diagram)* : Points sur un cercle indiquant les positions de phase stables
* PSK offre une communication numérique robuste avec un débit de données élevé et une bonne résistance au bruit

---

[question:AE401]
