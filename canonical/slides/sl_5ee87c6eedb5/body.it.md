## Lunghezza dell'antenna e fattore di riduzione

* La lunghezza dell'antenna dipende dal fattore di riduzione  
* Dipolo a semionda: Metà della lunghezza d'onda $\times$ Fattore di riduzione  
* Radiatore a quarto d'onda: Quarto della lunghezza d'onda $\times$ Fattore di riduzione  
* Valore tipico: $\num{0,95}$  

---

[question:AG101]

---
#### Percorso di soluzione
<left>
* dato: $f = \qty{14,2}{\mega\hertz}$
* dato: $k_v = 0,95$
</left>
<right>
* dato: dipolo $\frac{\lambda}{2}$
* cercato: $l_G$
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

#### Percorso di soluzione
<left>
* dato: $f = \qty{7,1}{\mega\hertz}$
* dato: $k_v = 0,95$
</left>
<right>
* dato: dipolo $\frac{\lambda}{2}$
* cercato: $l_G$
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
#### Percorso di soluzione
<left>
* dato: $l_G = \qty{20}{\meter}$
* dato: $k_v = 0,95$
</left>
<right>
* dato: dipolo
* cercato: $f$
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

#### Percorso di soluzione
<left>
* dato: $f = \qty{7,1}{\mega\hertz}$
* dato: $k_v = 0,95$
</left>
<right>
* dato: Groundplane a quarto d’onda
* cercato: $l_G$
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

#### Percorso di soluzione
<left>
* dato: $f = \qty{14,2}{\mega\hertz}$
* dato: $k_v = 0,97$
</left>
<right>
* dato: Antenna verticale 5/8λ
* cercato: $l_G$
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

### Causa del fattore di riduzione

* I conduttori non sono infinitamente sottili  
* Capacità aggiuntiva tra il conduttore e l'ambiente  
* Influenza la lunghezza elettrica effettiva dell'antenna  

---

[question:AG202]

---

### Fattore di allungamento nelle antenne a loop

* Differenza rispetto al fattore di riduzione  
* Porta a un allungamento apparente dell'antenna  

<note>
Un fattore di allungamento <u>non</u> significa che l'onda si propaghi a una velocità *superiore a quella della luce*. Si tratta della velocità di fase, non della velocità di gruppo.
</note>

---

[question:AG118]

---

#### Percorso di soluzione
<left>
* dato: $f = \qty{7,1}{\mega\hertz}$
* dato: $k_v = 1,02$
</left>
<right>
* dato: Delta-Loop
* cercato: $l_G$
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

### Fattore di riduzione nelle linee bifilari

* L'onda si trova tra i conduttori  
* L'effetto pelle impedisce una penetrazione profonda nel metallo  
* Fattore di riduzione approssimativamente $1$ (come la propagazione nello spazio libero)  

---

[question:AG313]

---

### Fattore di riduzione nei cavi coassiali comuni

* L'onda si trova nel materiale dielettrico tra i conduttori
* Esempio per polietilene: $\epsilon_\mathrm{r} = 2,29$  
* L'effetto pelle impedisce una penetrazione profonda nel metallo  
* La geometria del cavo ha poca influenza  
* Calcolo del fattore di riduzione:  

<fragment>
$v_\mathrm{k} = \dfrac{1}{\sqrt{\epsilon_\mathrm{r}}}$
</fragment>

---

[question:AG315]

---

[question:AG316]

---
#### Percorso di soluzione
* dato: $f = \qty{145}{\mega\hertz}$
* dato: $k_v = 0,66$
* cercato: $l_G$

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