<left>
[photo:268:a_I eilt vor:Phasenverschiebung am Kondensator zwischen Spannung und Strom]
</left>
<right>
* Phasenverschiebung di $\qty{90}{\degree}$
* La corrente precede la tensione
</right>
<note>
Ricorda: Condensatoooore, la corrente precede voooora!
</note>
---
[question:AC101]
---
### Potenza attiva
<left>
[picture:943:a_Blindleistung Kondensator:Das Produkt von $U \cdot I$ ergibt die grüne Leistungskurve]
</left>
<right>
* La curva di potenza verde è il prodotto di corrente e tensione
* La potenza oscilla simmetricamente attorno alla linea dello zero e si compensa
* *Potenza reattiva* su una *resistenza reattiva*
</right>
---
[question:AC111]
<note>
Nello stato stazionario, quasi nessuna corrente scorre più, motivo per cui anche la potenza è quasi 0W.
</note>
---
* La potenza attiva viene convertita solo in una resistenza ohmica (corrente e tensione in fase)
* La resistenza reattiva non assorbe energia attiva
* Pertanto non si scalda
* Un condensatore caldo ad alta frequenza ha una componente ohmica e dovrebbe essere sostituito

---
[question:AC103]

--- style="font-size: smaller;"
### Resistenza reattiva capacitiva $X_{\textrm{C}}$

Il condensatore viene collegato a una tensione alternata, caricato e scaricato continuamente $\rightarrow$ resistenza di corrente alternata / resistenza reattiva capacitiva

<fragment>
1. Se la frequenza della tensione alternata su un condensatore aumenta, scorre più corrente; ciò significa che la resistenza reattiva capacitiva è diminuita.
</fragment>
<fragment>
2. Se la capacità del condensatore aumenta, aumenta anche la corrente, cioè la resistenza reattiva diminuisce.
</fragment>

<fragment>
$X_{\textrm{C}} = \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}$
</fragment>

<note>
Un VNA misura la variazione della resistenza reattiva $X_C$ in funzione della frequenza
</note>
---
[question:AC102]
---
[question:AC104]
---
#### Percorso di soluzione
* dato: $C = \qty{10}{\pico\farad}$
* dato: $f = \qty{100}{\mega\hertz}$
* cercato: $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{10}{\pico\farad}}\\ &\approx \qty{159}{\ohm} \end{split}$
</fragment>

---
[question:AC105]
---
#### Percorso di soluzione
* dato: $C = \qty{50}{\pico\farad}$
* dato: $f = \qty{145}{\mega\hertz}$
* cercato: $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{145}{\mega\hertz} \cdot \qty{50}{\pico\farad}}\\ &\approx \qty{22}{\ohm} \end{split}$
</fragment>
---
[question:AC106]
---
#### Percorso di soluzione
* dato: $C = \qty{100}{\pico\farad}$
* dato: $f = \qty{100}{\mega\hertz}$
* cercato: $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{100}{\pico\farad}}\\ &\approx \qty{15,9}{\ohm} \end{split}$
</fragment>

---
[question:AC107]
---
#### Percorso di soluzione
* dato: $C = \qty{100}{\pico\farad}$
* dato: $f = \qty{435}{\mega\hertz}$
* cercato: $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{435}{\mega\hertz} \cdot \qty{100}{\pico\farad}}\\ &\approx \qty{3,7}{\ohm} \end{split}$
</fragment>

---
[question:AC108]
---
#### Percorso di soluzione
<left>
* dato: $U = \qty{16}{\volt}$
* dato: $I = \qty{32}{\milli\ampere}$
</left>
<right>
* dato: $f = \qty{50}{\hertz}$
* cercato: $C$
</right>

<fragment>
$X_{\textrm{C}} = \frac{U}{I} = \frac{\qty{16}{\volt}}{\qty{32}{\milli\ampere}} = \qty{500}{\ohm}$
</fragment>

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} \\ \Rightarrow C &= \frac{1}{\omega \cdot X_{\textrm{C}}} = \frac{1}{2\pi \cdot f \cdot X_{\textrm{C}}}\\ &= \frac{1}{2\pi \cdot \qty{50}{\hertz} \cdot \qty{500}{\ohm}}\\ &\approx \qty{6,37}{\micro\farad}\end{split}$
</fragment>

---
### Perdite del condensatore

<left>
[photo:260:a_Kondensator Ersatzschaltbild:Schema elettrico equivalente di un condensatore reale con una resistenza di perdita in serie (ESR).]
</left>
<right>
* Fattore di perdita<br/>$\tan(\delta) = \frac{R}{X_C}$
* Perdite nel materiale dielettrico e nei conduttori
</right>

---
[question:AC109]
---
[question:AC110]
