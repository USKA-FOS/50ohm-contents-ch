<left>
[photo:268:a_I eilt vor:Sfasamento di fase al condensatore tra tensione e corrente]
</left>
<right>
* Sfasamento di fase di $\qty{90}{\degree}$
* La corrente precede la tensione
</right>
<note>
Da ricordare: Condensatoooore, la corrente precede!
</note>
---
[question:AC101]
---
### Potenza attiva
<left>
[picture:943:a_Blindleistung Kondensator:Il prodotto di $U \cdot I$ genera la curva di potenza verde]
</left>
<right>
* La curva di potenza verde è il prodotto di corrente e tensione
* La potenza oscilla simmetricamente intorno alla linea zero e si annulla
* *Potenza reattiva* su una *reattanza*
</right>
---
[question:AC111]
<note>
In stato stazionario non scorre quasi più corrente, motivo per cui anche la potenza è quasi nulla (0 W).
</note>
---
* La potenza attiva viene dissipata solo in una resistenza ohmica (corrente e tensione in fase)
* La reattanza non assorbe energia attiva
* Per questo motivo non si scalda
* Un condensatore caldo in alta frequenza presenta una componente ohmica e dovrebbe essere sostituito

---
[question:AC103]

--- style="font-size: smaller;"
### Reattanza capacitiva $X_{\textrm{C}}$

Il condensatore collegato a tensione alternata viene caricato e scaricato continuamente $\rightarrow$ resistenza alternata / reattanza capacitiva

<fragment>
1. Se la frequenza della tensione alternata su un condensatore aumenta, scorre più corrente; ciò significa che la reattanza capacitiva diventa più piccola.
</fragment>
<fragment>
2. Se la capacità del condensatore aumenta, aumenta anche la corrente, cioè la reattanza diventa più piccola.
</fragment>

<fragment>
$X_{\textrm{C}} = \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}$
</fragment>

<note>
Un VNA misura la variazione della reattanza $X_C$ in funzione della frequenza
</note>
---
[question:AC102]
---
[question:AC104]
---
#### Procedimento di soluzione
* dati: $C = \qty{10}{\pico\farad}$
* dati: $f = \qty{100}{\mega\hertz}$
* richiesto: $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{10}{\pico\farad}}\\ &\approx \qty{159}{\ohm} \end{split}$
</fragment>

---
[question:AC105]
---
#### Procedimento di soluzione
* dati: $C = \qty{50}{\pico\farad}$
* dati: $f = \qty{145}{\mega\hertz}$
* richiesto: $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{145}{\mega\hertz} \cdot \qty{50}{\pico\farad}}\\ &\approx \qty{22}{\ohm} \end{split}$
</fragment>
---
[question:AC106]
---
#### Procedimento di soluzione
* dati: $C = \qty{100}{\pico\farad}$
* dati: $f = \qty{100}{\mega\hertz}$
* richiesto: $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{100}{\pico\farad}}\\ &\approx \qty{15,9}{\ohm} \end{split}$
</fragment>

---
[question:AC107]
---
#### Procedimento di soluzione
* dati: $C = \qty{100}{\pico\farad}$
* dati: $f = \qty{435}{\mega\hertz}$
* richiesto: $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{435}{\mega\hertz} \cdot \qty{100}{\pico\farad}}\\ &\approx \qty{3,7}{\ohm} \end{split}$
</fragment>

---
[question:AC108]
---
#### Procedimento di soluzione
<left>
* dati: $U = \qty{16}{\volt}$
* dati: $I = \qty{32}{\milli\ampere}$
</left>
<right>
* dati: $f = \qty{50}{\hertz}$
* richiesto: $C$
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
[photo:260:a_Kondensator Ersatzschaltbild:Circuito equivalente di un condensatore reale con una resistenza di perdita serie (ESR).]
</left>
<right>
* Fattore di perdita<br/>$\tan(\delta) = \frac{R}{X_C}$
* Perdite nel materiale dielettrico e nei conduttori di alimentazione
</right>

---
[question:AC109]
---
[question:AC110]
