## Lunghezza dell'antenna e fattore di velocità

* La lunghezza dell'antenna dipende dal fattore di velocità
* Dipolo a semionda: metà della lunghezza d’onda $\times$ fattore di velocità
* Radiatore a quarto d’onda: un quarto della lunghezza d’onda $\times$ fattore di velocità
* Valore tipico: $\num{0,95}$

---

[question:AG101]

---
#### Procedimento di soluzione
<left>
* dati: $f = \qty{14,2}{\mega\hertz}$
* dati: $k_v = 0,95$
</left>
<right>
* dati: dipolo a semionda $\frac{\lambda}{2}$
* richiesto: $l_G$
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
#### Procedimento di soluzione
<left>
* dati: $f = \qty{7,1}{\mega\hertz}$
* dati: $k_v = 0,95$
</left>
<right>
* dati: dipolo a semionda $\frac{\lambda}{2}$
* richiesto: $l_G$
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
#### Procedimento di soluzione
<left>
* dati: $l_G = \qty{20}{\meter}$
* dati: $k_v = 0,95$
</left>
<right>
* dati: dipolo
* richiesto: $f$
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
#### Procedimento di soluzione
<left>
* dati: $f = \qty{7,1}{\mega\hertz}$
* dati: $k_v = 0,95$
</left>
<right>
* dati: antenna groundplane a $\frac{\lambda}{4}$
* richiesto: $l_G$
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
#### Procedimento di soluzione
<left>
* dati: $f = \qty{14,2}{\mega\hertz}$
* dati: $k_v = 0,97$
</left>
<right>
* dati: antenna verticale $\frac{5}{8}\lambda$
* richiesto: $l_G$
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

### Causa del fattore di velocità

* I conduttori non sono infinitamente sottili
* Capacità aggiuntiva tra conduttore e ambiente circostante
* Influenza la lunghezza elettrica effettiva dell'antenna

---

[question:AG202]

---

### Fattore di allungamento nelle antenne a loop

* Differenza rispetto al fattore di velocità
* Porta a un apparente allungamento dell'antenna

<note>
Un fattore di allungamento <u>non</u> significa che l'onda si propaga a una velocità *superiore a quella della luce*. Si tratta della velocità di fase, non della velocità di gruppo.
</note>

---

[question:AG118]

---

#### Procedimento di soluzione
<left>
* dati: $f = \qty{7,1}{\mega\hertz}$
* dati: $k_v = 1,02$
</left>
<right>
* dati: antenna Delta-Loop
* richiesto: $l_G$
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

### Fattore di velocità nelle linee a due fili paralleli

* L'onda si propaga tra i conduttori
* L'effetto pelle impedisce la penetrazione profonda nel metallo
* Fattore di velocità prossimo a $1$ (come nella propagazione nello spazio libero)

---

[question:AG313]

---

### Fattore di velocità nei cavi coassiali

* L'onda si propaga nel materiale dielettrico tra i conduttori
* Esempio per polietilene: $\epsilon_\mathrm{r} = 2,29$
* L'effetto pelle impedisce la penetrazione profonda nel metallo
* La geometria del cavo ha scarsa influenza
* Calcolo del fattore di velocità:

<fragment>
$v_\mathrm{k} = \dfrac{1}{\sqrt{\epsilon_\mathrm{r}}}$
</fragment>

---

[question:AG315]

---

[question:AG316]

---
#### Procedimento di soluzione
* dati: $f = \qty{145}{\mega\hertz}$
* dati: $k_v = 0,66$
* richiesto: $l_G$

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