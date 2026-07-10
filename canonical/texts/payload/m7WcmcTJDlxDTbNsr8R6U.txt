## Genauigkeit von Frequenzen und Messbereichen

* Genauigkeitsangaben erfolgen in $\unit{\percent}$ (z.B. ${1 \cdot \num{10^{-2}}}$) oder in parts per million ($\qty{1}{\ppm} = {1 \cdot \num{10^{-6}}}$)
* Manchmal wird auch direkt in Exponentialschreibweise angegeben, z.B. ${1 \cdot \num{10^{-7}}}$
* Die angegebene Genauigkeit wird mit der Frequenz multipliziert, um die mögliche Abweichung von Messwerten oder Anzeigen zu berechnen

<note>
Hinweis bzgl. Umrechnung/Darstellung von 10er Potenzen:

$1 \cdot \num{10^{-2}} = \frac{1}{\num{10^2}}$
$1 \cdot \num{10^{-6}} = \frac{1}{\num{10^6}}$
usw.
</note>

---
[question:AA115]
---
#### Lösungsweg
* gegeben: $f = \qty{435}{\mega\hertz}$
* gesucht: $\qty{1}{\ppm}$ von $f$

<fragment>
$\qty{435}{\mega\hertz} \cdot \frac{1}{\num{10^6}} = \frac{435\cdot \qty{\cancel{10^6}}{\hertz}}{\cancel{\num{10^6}}} = \qty{435}{\hertz}$
</fragment>
---
[question:AA116]
---
#### Lösungsweg Teil 1
* gegeben: $f = \qty{14,200000}{\mega\hertz}$
* gegeben: $\textrm{Abw.} = \qty{10}{\ppm}$
* gesucht: $f_{\mathrm{min}}, f_{\mathrm{max}}$

<fragment>
$\begin{split}f_{\mathrm{min}} &= f\,-\,f \cdot \frac{10}{\num{10^6}}\\ &= \qty{14,2}{\mega\hertz}\,-\,\frac{14,2\cdot \qty{\cancel{10^6}}{\hertz}\cdot 10}{\cancel{\num{10^6}}}\\ &= \qty{14,2}{\mega\hertz}\,-\,\qty{142}{\hertz}\\ &= \qty{14,199858}{\mega\hertz}\end{split}$
</fragment>
---
#### Lösungsweg Teil 2
* gegeben: $f = 14,200.\qty{000}{\mega\hertz}$
* gegeben: $\textrm{Abw.} = \qty{10}{\ppm}$
* gesucht: $f_{\mathrm{min}}, f_{\mathrm{max}}$

<fragment>
$\begin{split}f_{\mathrm{max}} &= f\,+\,f \cdot \frac{10}{\num{10^6}}\\ &= \qty{14,2}{\mega\hertz}\,+\,\frac{14,2\cdot \qty{\cancel{10^6}}{\hertz}\cdot 10}{\cancel{10^6}}\\ &= \qty{14,2}{\mega\hertz}\,+\,\qty{142}{\hertz}\\ &= \qty{14,200142}{\mega\hertz}\end{split}$
</fragment>
---
[question:AI506]
---
#### Lösungsweg
* gegeben: $f = \qty{29}{\mega\hertz}$
* gegeben: $\textrm{Abw.} = \qty{0,01}{\percent}$
* gesucht: $\Delta f$

<fragment>
$\begin{split}\Delta f &= \qty{29}{\mega\hertz} \cdot \qty{0,01}{\percent}\\ &= 29\cdot \qty{\cancel{10^6}}{\hertz} \cdot 100\cdot \cancel{\num{10^{-6}}}\\ &= \qty{2900}{\hertz}\end{split}$
</fragment>
---
[question:AI507]
---
#### Lösungsweg
* gegeben: $f = \qty{14100}{\kilo\hertz}$
* gegeben: $\textrm{Abw.} = \pm\qty{0,00001}{\percent}$
* gesucht: $\Delta f$

<fragment>
$\begin{split}\Delta f &= \qty{14100}{\kilo\hertz} \cdot \qty{0,00001}{\percent}\\ &= 14,1\cdot \qty{\cancel{10^6}}{\hertz} \cdot 0,1\cdot \cancel{\num{10^{-6}}}\\ &= \qty{1,41}{\hertz}\end{split}$
</fragment>
---
[question:AI508]
---
#### Lösungsweg
* gegeben: $f = \qty{100}{\mega\hertz}$
* gegeben: $\textrm{Abw.} = \pm\qty{1}{\ppm}$
* gesucht: $\Delta f$

<fragment>
$\begin{split}\Delta f &= \qty{100}{\mega\hertz} \cdot \frac{1}{\num{10^6}}\\ &= \frac{100\cdot \qty{\cancel{10^6}}{\hertz}}{\cancel{10^6}}\\ &= \qty{100}{\hertz}\end{split}$
</fragment>
---
[question:AI509]
--- style="font-size: smaller;"
#### Lösungsweg
* gegeben: $f = \qty{145}{\mega\hertz}$
* gegeben: $\textrm{Abw.} = \qty{10}{\ppm}$
* gesucht: $f_{\mathrm{min}}, f_{\mathrm{max}}$

<fragment>
$\begin{split}\Delta f &= \qty{145}{\mega\hertz} \cdot \frac{10}{10^6}\\ &= \frac{145\cdot \qty{\cancel{10^6}}{\hertz} \cdot 10}{\cancel{10^6}}\\ &= \qty{1450}{\hertz}\end{split}$
</fragment>
<fragment>
<left>
$\begin{split}f_{\mathrm{min}} &= f\,-\,\Delta f\\ &= \qty{145}{\mega\hertz}\,-\,\qty{1450}{\hertz}\\ &= \qty{144,99855}{\mega\hertz}\end{split}$
</left>
<right>
$\begin{split}f_{\mathrm{max}} &= f\,+\,\Delta f\\ &= \qty{145}{\mega\hertz}\,+\,\qty{1450}{\hertz}\\ &= \qty{145,00145}{\mega\hertz}\end{split}$
</right>
</fragment>
---
[question:AI510]
---
#### Lösungsweg
* gegeben: $f = \qty{144,400}{\mega\hertz}$
* gegeben: $\textrm{Abw.} = \qty{1}{\ppm}$
* gegeben: $f_{B,\mathrm{max}} = \qty{2,7}{\kilo\hertz}$
* gesucht: $f_{B,\mathrm{max},\text{Abw}}$

<fragment>
<left>
$\begin{split}\Delta f &= \qty{144,4}{\mega\hertz} \cdot \frac{1}{\num{10^6}}\\ &= \frac{144,4\cdot \qty{\cancel{10^6}}{\hertz}}{\cancel{10^6}}\\ &= \qty{144,4}{\hertz}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}f_{B,\mathrm{max},\text{Abw}} &= f_{B,\mathrm{max}} + \Delta f\\ &= \qty{2,7}{\kilo\hertz} + \qty{144,4}{\hertz}\\ &= \qty{2,8444}{\kilo\hertz}\end{split}$
</right>
</fragment>
