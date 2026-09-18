## Precisione delle frequenze e degli intervalli di misura

* Le indicazioni di precisione vengono fornite in $\unit{\percent}$ (ad esempio ${1 \cdot \num{10^{-2}}}$) o in parti per milione ($\qty{1}{\ppm} = {1 \cdot \num{10^{-6}}}$)
* A volte viene indicato direttamente in notazione esponenziale, ad esempio ${1 \cdot \num{10^{-7}}}$
* La precisione indicata viene moltiplicata per la frequenza per calcolare la possibile deviazione dei valori di misura o delle indicazioni

<note>
Nota sulla conversione/rappresentazione delle potenze del 10:

$1 \cdot \num{10^{-2}} = \frac{1}{\num{10^2}}$
$1 \cdot \num{10^{-6}} = \frac{1}{\num{10^6}}$
 ecc.
</note>

---
[question:AA115]
---
#### Procedimento
* dati: $f = \qty{435}{\mega\hertz}$
* richiesto: $\qty{1}{\ppm}$ di $f$

<fragment>
$\qty{435}{\mega\hertz} \cdot \frac{1}{\num{10^6}} = \frac{435\cdot \qty{\cancel{10^6}}{\hertz}}{\cancel{\num{10^6}}} = \qty{435}{\hertz}$
</fragment>
---
[question:AA116]
---
#### Procedimento parte 1
* dati: $f = \qty{14,200000}{\mega\hertz}$
* dati: $\textrm{Dev.} = \qty{10}{\ppm}$
* richiesto: $f_{\mathrm{min}}, f_{\mathrm{max}}$

<fragment>
$\begin{split}f_{\mathrm{min}} &= f\,-\,f \cdot \frac{10}{\num{10^6}}\\ &= \qty{14,2}{\mega\hertz}\,-\,\frac{14,2\cdot \qty{\cancel{10^6}}{\hertz}\cdot 10}{\cancel{\num{10^6}}}\\ &= \qty{14,2}{\mega\hertz}\,-\,\qty{142}{\hertz}\\ &= \qty{14,199858}{\mega\hertz}\end{split}$
</fragment>
---
#### Procedimento parte 2
* dati: $f = 14,200.\qty{000}{\mega\hertz}$
* dati: $\textrm{Dev.} = \qty{10}{\ppm}$
* richiesto: $f_{\mathrm{min}}, f_{\mathrm{max}}$

<fragment>
$\begin{split}f_{\mathrm{max}} &= f\,+\,f \cdot \frac{10}{\num{10^6}}\\ &= \qty{14,2}{\mega\hertz}\,+\,\frac{14,2\cdot \qty{\cancel{10^6}}{\hertz}\cdot 10}{\cancel{10^6}}\\ &= \qty{14,2}{\mega\hertz}\,+\,\qty{142}{\hertz}\\ &= \qty{14,200142}{\mega\hertz}\end{split}$
</fragment>
---
[question:AI506]
---
#### Procedimento
* dati: $f = \qty{29}{\mega\hertz}$
* dati: $\textrm{Dev.} = \qty{0,01}{\percent}$
* richiesto: $\Delta f$

<fragment>
$\begin{split}\Delta f &= \qty{29}{\mega\hertz} \cdot \qty{0,01}{\percent}\\ &= 29\cdot \qty{\cancel{10^6}}{\hertz} \cdot 100\cdot \cancel{\num{10^{-6}}}\\ &= \qty{2900}{\hertz}\end{split}$
</fragment>
---
[question:AI507]
---
#### Procedimento
* dati: $f = \qty{14100}{\kilo\hertz}$
* dati: $\textrm{Dev.} = \pm\qty{0,00001}{\percent}$
* richiesto: $\Delta f$

<fragment>
$\begin{split}\Delta f &= \qty{14100}{\kilo\hertz} \cdot \qty{0,00001}{\percent}\\ &= 14,1\cdot \qty{\cancel{10^6}}{\hertz} \cdot 0,1\cdot \cancel{\num{10^{-6}}}\\ &= \qty{1,41}{\hertz}\end{split}$
</fragment>
---
[question:AI508]
---
#### Procedimento
* dati: $f = \qty{100}{\mega\hertz}$
* dati: $\textrm{Dev.} = \pm\qty{1}{\ppm}$
* richiesto: $\Delta f$

<fragment>
$\begin{split}\Delta f &= \qty{100}{\mega\hertz} \cdot \frac{1}{\num{10^6}}\\ &= \frac{100\cdot \qty{\cancel{10^6}}{\hertz}}{\cancel{10^6}}\\ &= \qty{100}{\hertz}\end{split}$
</fragment>
---
[question:AI509]
--- style="font-size: smaller;"
#### Procedimento
* dati: $f = \qty{145}{\mega\hertz}$
* dati: $\textrm{Dev.} = \qty{10}{\ppm}$
* richiesto: $f_{\mathrm{min}}, f_{\mathrm{max}}$

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
#### Procedimento
* dati: $f = \qty{144,400}{\mega\hertz}$
* dati: $\textrm{Dev.} = \qty{1}{\ppm}$
* dati: $f_{B,\mathrm{max}} = \qty{2,7}{\kilo\hertz}$
* richiesto: $f_{B,\mathrm{max},\text{Dev}}$

<fragment>
<left>
$\begin{split}\Delta f &= \qty{144,4}{\mega\hertz} \cdot \frac{1}{\num{10^6}}\\ &= \frac{144,4\cdot \qty{\cancel{10^6}}{\hertz}}{\cancel{10^6}}\\ &= \qty{144,4}{\hertz}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}f_{B,\mathrm{max},\text{Dev}} &= f_{B,\mathrm{max}} + \Delta f\\ &= \qty{2,7}{\kilo\hertz} + \qty{144,4}{\hertz}\\ &= \qty{2,8444}{\kilo\hertz}\end{split}$
</right>
</fragment>
