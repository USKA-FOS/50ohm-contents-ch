Zunächst müssen wir aus den Werten von *L* und *C* die Resonanzfrequenz des Schwingkreises gemäß Thomsonscher Schwingkreisformel bestimmen, da die vorgenannten Gleichungen nur für den Resonanzfall gelten!

$f = \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}$

Mit eingesetzten Werten:

$\begin{split} f &= \frac{1}{2 \pi \cdot \sqrt{100 \cdot \qty{10^{-6}}{\henry} \cdot 0,01 \cdot 10^{-6}\text{ F}}} \\ &\approx \qty{159154,94}{\hertz} \approx 159,2 \cdot \qty{10^3}{\hertz}\\ &\approx \qty{159,2}{\kilo\hertz}\end{split}$
  
Damit kann der induktive Widerstand $X_\text{L}$ wie folgt berechnet werden (Formeln aus der Formelsammlung):

Kreisfrequenz: $\omega = 2 \pi \cdot f$

Induktiver Widerstand: $X_\text{L} = \omega \cdot L$

Mit eingesetzten Werten:
$\begin{split}X_\text{L} &= 2 \pi \cdot 159,2 \cdot \qty{10^3}{\hertz} \cdot 100 \cdot \qty{10^{-6}}{\henry}\\ &\approx \qty{100,03}{\ohm}\end{split}$
  
Die Güte errechnet sich damit unter Einbeziehung des ohmschen Widerstands $R_\text{S}$ zu:
  
$\begin{split}Q &= \frac{X_\text{L}}{R_\text{S}}\\\text{Mit eingesetzten Werten:}\\Q &= \frac{\qty{100,03}{\ohm}}{\qty{10}{\ohm}} \approx 10\end{split}$