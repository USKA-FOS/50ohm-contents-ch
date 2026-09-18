## Longueur d’antenne et facteur de vélocité

* La longueur d’antenne dépend du facteur de vélocité
* Dipôle demi-onde : moitié de la longueur d’onde $\times$ facteur de vélocité
* Radiateur quart d’onde : quart de la longueur d’onde $\times$ facteur de vélocité
* Valeur typique : $\num{0,95}$

---

[question:AG101]

---

#### Méthode de résolution
<left>
* donné : $f = \qty{14,2}{\mega\hertz}$
* donné : $k_v = 0,95$
</left>
<right>
* donné : dipôle demi-onde
* cherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \frac{1}{2} \cdot \frac{\lambda}{2}\\n&= \frac{1}{4} \cdot \frac{c}{f}\\n&\approx \frac{1}{4} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{14,2}{\mega\hertz}}\\n&\approx \frac{1}{4} \cdot \qty{21,13}{\meter}\\n&\approx \qty{5,28}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\n\Rightarrow l_G &= k_v \cdot l_E\\ &= 0,95 \cdot \qty{5,28}{\meter}\\n&\approx \qty{5,02}{\meter}\end{split}$
</fragment>
</right>

---

[question:AG102]

---

#### Méthode de résolution
<left>
* donné : $f = \qty{7,1}{\mega\hertz}$
* donné : $k_v = 0,95$
</left>
<right>
* donné : dipôle demi-onde
* cherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \frac{1}{2} \cdot \frac{\lambda}{2}\\n&= \frac{1}{4} \cdot \frac{c}{f}\\n&\approx \frac{1}{4} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{7,1}{\mega\hertz}}\\n&\approx \frac{1}{4} \cdot \qty{42,25}{\meter}\\n&\approx \qty{10,56}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\n\Rightarrow l_G &= k_v \cdot l_E\\ &= 0,95 \cdot \qty{10,56}{\meter}\\n&\approx \qty{10,04}{\meter}\end{split}$
</fragment>
</right>

---

[question:AG103]

---

#### Méthode de résolution
<left>
* donné : $l_G = \qty{20}{\meter}$
* donné : $k_v = 0,95$
</left>
<right>
* donné : dipôle
* cherché : $f$
</right>

<left>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\n\Rightarrow l_E &= \frac{l_G}{k_v}\\n&= \frac{\qty{20}{\meter}}{0,95}\\n&\approx \qty{21,05}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}l_E &= \frac{\lambda}{2}\\n&= \frac{1}{2} \cdot \frac{c}{f}\\n\Rightarrow f &= \frac{1}{2} \cdot \frac{c}{l_E}\\n&\approx \frac{1}{2} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{21,05}{\meter}}\\
&\approx \qty{7,125}{\mega\hertz}\end{split}$
</fragment>
</right>

---

[question:AG104]

---

#### Méthode de résolution
<left>
* donné : $f = \qty{7,1}{\mega\hertz}$
* donné : $k_v = 0,95$
</left>
<right>
* donné : groundplane quart d’onde
* cherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \frac{\lambda}{4}\\n&= \frac{1}{4} \cdot \frac{c}{f}\\n&\approx \frac{1}{4} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{7,1}{\mega\hertz}}\\n&\approx \frac{1}{4} \cdot \qty{42,25}{\meter}\\n&\approx \qty{10,56}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\n\Rightarrow l_G &= k_v \cdot l_E\\ &= 0,95 \cdot \qty{10,56}{\meter}\\n&\approx \qty{10,04}{\meter}\end{split}$
</fragment>
</right>

---

[question:AG105]

---

#### Méthode de résolution
<left>
* donné : $f = \qty{14,2}{\mega\hertz}$
* donné : $k_v = 0,97$
</left>
<right>
* donné : antenne verticale $\frac{5}{8}\lambda$
* cherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \frac{5}{8}\lambda\\ &= \frac{5}{8} \cdot \frac{c}{f}\\n&\approx \frac{5}{8} \cdot \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{14,2}{\mega\hertz}}\\n&\approx \frac{5}{8} \cdot \qty{21,13}{\meter}\\n&\approx \qty{13,20}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\n\Rightarrow l_G &= k_v \cdot l_E\\ &= 0,97 \cdot \qty{13,20}{\meter}\\n&\approx \qty{12,80}{\meter}\end{split}$
</fragment>
</right>

---

### Cause du facteur de vélocité

* Les conducteurs ne sont pas infiniment fins
* Capacité supplémentaire entre le conducteur et l’environnement
* Influence la longueur électrique effective de l’antenne

---

[question:AG202]

---

### Facteur d’allongement pour les antennes en boucle

* Différence avec le facteur de vélocité
* Conduit à un allongement apparent de l’antenne

<note>
Un facteur d’allongement n’implique <u>pas</u> que l’onde se propage à une vitesse *supérieure à celle de la lumière*. Il s’agit de la vitesse de phase, et non de la vitesse de groupe.
</note>

---

[question:AG118]

---

#### Méthode de résolution
<left>
* donné : $f = \qty{7,1}{\mega\hertz}$
* donné : $k_v = 1,02$
</left>
<right>
* donné : Delta-Loop
* cherché : $l_G$
</right>

<left>
<fragment>
$\begin{split}l_E &= \lambda\\ &= \frac{c}{f}\\n&= \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{7,1}{\mega\hertz}}\\n&\approx \qty{42,23}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\n\Rightarrow l_G &= k_v \cdot l_E\\ &= 1,02 \cdot \qty{42,23}{\meter}\\n&\approx \qty{43,10}{\meter}\end{split}$
</fragment>
</right>

---

### Facteur de vélocité pour les lignes bifilaires

* L’onde se propage entre les conducteurs
* L’effet de peau empêche une pénétration profonde dans le métal
* Facteur de vélocité proche de $1$ (comme en propagation en espace libre)


---

[question:AG313]

---

### Facteur de vélocité pour les câbles coaxiaux

* L’onde se propage dans le diélectrique entre les conducteurs
* Exemple pour le polyéthylène : $\epsilon_\mathrm{r} = 2,29$
* L’effet de peau empêche une pénétration profonde dans le métal
* La géométrie du câble a peu d’influence
* Calcul du facteur de vélocité :

<fragment>
$v_\mathrm{k} = \dfrac{1}{\sqrt{\epsilon_\mathrm{r}}}$
</fragment>

---

[question:AG315]

---

[question:AG316]

---
#### Méthode de résolution
* donné : $f = \qty{145}{\mega\hertz}$
* donné : $k_v = 0,66$
* cherché : $l_G$


<left>
<fragment>
$\begin{split}l_E &= \lambda\\ &= \frac{c}{f}\\n&\approx \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{145}{\mega\hertz}}\\n&\approx \qty{2,07}{\meter}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}k_v &= \frac{l_G}{l_E}\\n\Rightarrow l_G &= k_v \cdot l_E\\ &= 0,66 \cdot \qty{2,07}{\meter}\\n&\approx \qty{1,37}{\meter}\end{split}$
</fragment>
</right>