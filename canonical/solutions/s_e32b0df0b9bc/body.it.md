Innanzitutto dobbiamo determinare la frequenza di risonanza del circuito risonante dai valori di *L* e *C* secondo la formula del circuito risonante di Thomson, poiché le equazioni sopra menzionate valgono solo per il caso di risonanza!

$f = \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}$

Con i valori inseriti:

$\begin{split} f &= \frac{1}{2 \pi \cdot \sqrt{100 \cdot \qty{10^{-6}}{\henry} \cdot 0,01 \cdot 10^{-6}\text{ F}}} \\ &\approx \qty{159154,94}{\hertz} \approx 159,2 \cdot \qty{10^3}{\hertz}\\ &\approx \qty{159,2}{\kilo\hertz}\end{split}$
  
Con questo si può calcolare la reattanza induttiva $X_\text{L}$ come segue (formule dalla raccolta di formule):

Pulsazione: $\omega = 2 \pi \cdot f$

Reattanza induttiva: $X_\text{L} = \omega \cdot L$

Con i valori inseriti:
$\begin{split}X_\text{L} &= 2 \pi \cdot 159,2 \cdot \qty{10^3}{\hertz} \cdot 100 \cdot \qty{10^{-6}}{\henry}\\ &\approx \qty{100,03}{\ohm}\end{split}$
  
Il fattore di qualità si calcola quindi tenendo conto della resistenza ohmica $R_\text{S}$:
  
$\begin{split}Q &= \frac{X_\text{L}}{R_\text{S}}\\\text{Con i valori inseriti:}\\Q &= \frac{\qty{100,03}{\ohm}}{\qty{10}{\ohm}} \approx 10\end{split}$