## Longueur de l'antenne et facteur de réduction

* La longueur de l'antenne dépend du facteur de réduction  
* Dipôle demi-onde : moitié de la longueur d'onde $\times$ facteur de réduction  
* Émetteur quart d'onde : quart de la longueur d'onde $\times$ facteur de réduction  
* Valeur typique : $\num{0,95}$  

---

[question:AG101]

---
#### Solution
<left>
* donné : $f = \qty{14,2}{\mega\hertz}$
* donné : $k_v = 0,95$
</left>
<right>
* donné : Dipôle $\frac{\lambda}{2}$
* recherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \frac{1}{2} \cdot \frac{\lambda}{2}\\ &= \frac{1}{4} \cdot \frac{c}{f}\\ &\approx \frac{1}{4} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{14,2}{\mega\hertz}}\\ &\approx \frac{1}{4} \cdot \qty{21,13}{\meter}\\ &\approx \qty{5,28}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\ \Rightarrow l_G &= k_v \cdot l_E\\ &= 0,95 \cdot \qty{5,28}{\meter}\\ &\approx \qty{5,02}{\meter}\end{split}$
</fragment>
</right>

---

[question:AG102]

---

#### Solution
<left>
* donné : $f = \qty{7,1}{\mega\hertz}$
* donné : $k_v = 0,95$
</left>
<right>
* donné : Dipôle $\frac{\lambda}{2}$
* recherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \frac{1}{2} \cdot \frac{\lambda}{2}\\ &= \frac{1}{4} \cdot \frac{c}{f}\\ &\approx \frac{1}{4} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{7,1}{\mega\hertz}}\\ &\approx \frac{1}{4} \cdot \qty{42,25}{\meter}\\ &\approx \qty{10,56}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\ \Rightarrow l_G &= k_v \cdot l_E\\ &= 0,95 \cdot \qty{10,56}{\meter}\\ &\approx \qty{10,04}{\meter}\end{split}$
</fragment>
</right>

---

[question:AG103]

---
#### Solution
<left>
* donné : $l_G = \qty{20}{\meter}$
* donné : $k_v = 0,95$
</left>
<right>
* donné : Dipôle
* recherché : $f$
</right>

<left>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\ \Rightarrow l_E &= \frac{l_G}{k_v}\\ &= \frac{\qty{20}{\meter}}{0,95}\\ &\approx \qty{21,05}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}l_E &= \frac{\lambda}{2}\\ &= \frac{1}{2} \cdot \frac{c}{f}\\ \Rightarrow f &= \frac{1}{2} \cdot \frac{c}{l_E}\\ &\approx \frac{1}{2} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{21,05}{\meter}}\\&\approx \qty{7,125}{\mega\hertz}\end{split}$
</fragment>
</right>

---

[question:AG104]

---

#### Solution
<left>
* donné : $f = \qty{7,1}{\mega\hertz}$
* donné : $k_v = 0,95$
</left>
<right>
* donné : Groundplane $\frac{\lambda}{4}$
* recherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \frac{\lambda}{4}\\ &= \frac{1}{4} \cdot \frac{c}{f}\\ &\approx \frac{1}{4} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{7,1}{\mega\hertz}}\\ &\approx \frac{1}{4} \cdot \qty{42,25}{\meter}\\ &\approx \qty{10,56}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\ \Rightarrow l_G &= k_v \cdot l_E\\ &= 0,95 \cdot \qty{10,56}{\meter}\\ &\approx \qty{10,04}{\meter}\end{split}$
</fragment>
</right>

---

[question:AG105]

---

#### Solution
<left>
* donné : $f = \qty{14,2}{\mega\hertz}$
* donné : $k_v = 0,97$
</left>
<right>
* donné : Antenne verticale $\frac{5}{8}\lambda$
* recherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \frac{5}{8}\lambda\\ &= \frac{5}{8} \cdot \frac{c}{f}\\ &\approx \frac{5}{8} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{14,2}{\mega\hertz}}\\ &\approx \frac{5}{8} \cdot \qty{21,13}{\meter}\\ &\approx \qty{13,20}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\ \Rightarrow l_G &= k_v \cdot l_E\\ &= 0,97 \cdot \qty{13,20}{\meter}\\ &\approx \qty{12,80}{\meter}\end{split}$
</fragment>
</right>

---

### Cause du facteur de réduction

* Les conducteurs ne sont pas infiniment fins  
* Capacité supplémentaire entre le conducteur et l'environnement  
* Influence la longueur électrique effective de l'antenne  

---

[question:AG202]

---

### Facteur d'allongement des antennes en boucle

* Différence par rapport au facteur de réduction  
* Conduit à un allongement apparent de l'antenne  

<note>
Un facteur d'allongement ne signifie <u>pas</u> que l'onde se propage à une vitesse *supérieure à la vitesse de la lumière*. Il s'agit de la vitesse de phase, et non de la vitesse de groupe.
</note>

---

[question:AG118]

---

#### Solution
<left>
* donné : $f = \qty{7,1}{\mega\hertz}$
* donné : $k_v = 1,02$
</left>
<right>
* donné : Delta-Loop
* recherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \lambda\\ &= \frac{c}{f}\\ &= \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{7,1}{\mega\hertz}}\\ &\approx \qty{42,23}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\ \Rightarrow l_G &= k_v \cdot l_E\\ &= 1,02 \cdot \qty{42,23}{\meter}\\ &\approx \qty{43,10}{\meter}\end{split}$
</fragment>
</right>

---

### Facteur de réduction des lignes parallèles

* L'onde se trouve entre les conducteurs  
* L'effet de peau empêche une pénétration profonde dans le métal  
* Facteur de réduction approximativement $1$ (comme la propagation en espace libre)  

---

[question:AG313]

---

### Facteur de réduction des câbles coaxiaux

* L'onde se trouve dans le diélectrique entre les conducteurs
* Exemple pour le polyéthylène : $\epsilon_\mathrm{r} = 2,29$  
* L'effet de peau empêche une pénétration profonde dans le métal  
* La géométrie du câble a peu d'influence  
* Calcul du facteur de réduction :  

<fragment>
$v_\mathrm{k} = \dfrac{1}{\sqrt{\epsilon_\mathrm{r}}}$
</fragment>

---

[question:AG315]

---

[question:AG316]

---
#### Solution
* donné : $f = \qty{145}{\mega\hertz}$
* donné : $k_v = 0,66$
* recherché : $l_G$

<left>
<fragment>
$\begin{split}l_E &= \lambda\\ &= \frac{c}{f}\\ &\approx \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{145}{\mega\hertz}}\\ &\approx \qty{2,07}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\ \Rightarrow l_G &= k_v \cdot l_E\\ &= 0,66 \cdot \qty{2,07}{\meter}\\ &\approx \qty{1,37}{\meter}\end{split}$
</fragment>
</right>