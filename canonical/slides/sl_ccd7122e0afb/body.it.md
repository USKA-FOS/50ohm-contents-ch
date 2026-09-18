<left>
[photo:299:StepUpDownWandler: Convertitore Buck-Boost]
</left>
<right>
* Converte tensioni continue $\rightarrow$ convertitore DC/DC
* Ad esempio da $\qty{13,8}{\volt}$ a $\qty{5}{\volt}\rightarrow$ Step-DOWN (convertitore abbassatore)
* Ad esempio da $\qty{12}{\volt}$ a $\qty{19}{\volt}\rightarrow$ Step-UP (convertitore elevatore)
</right>
<note>
Il convertitore Buck-Boost nell'immagine può essere regolato in uscita da 0,5 V a 25 V. La potenza massima è di 25 W.
</note>
---
### Rendimento

* Si verificano perdite dovute ai componenti del circuito
* Rendimento $\eta$, solitamente espresso in $\%$

<fragment>
$\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$
</fragment>

---
[question:AB213]
---
#### Procedimento di soluzione
* dati: $U_{\textrm{in}} = \qty{12}{\volt}$
* dati: $U_{\textrm{out}} = \qty{5}{\volt}$
* dati: $I_{\textrm{in}} = \qty{2}{\ampere}$
* dati: $I_{\textrm{out}} = \qty{3}{\ampere}$
* richiesto: $\eta$

<fragment>
$\begin{split} \eta &= \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}}\\ &= \frac{\qty{5}{\volt} \cdot \qty{3}{\ampere}}{\qty{12}{\volt} \cdot \qty{2}{\ampere}} = \frac{\qty{15}{\watt}}{\qty{24}{\watt}} = \num{0,625} = \qty{62,5}{\percent} \end{split}$
</fragment>
---
[question:AB214]
---
* dati: $U_{\mathrm{in}} = \qty{5}{\volt}$
* dati: $U_{\mathrm{out}} = \qty{12}{\volt}$
* dati: $I_{\mathrm{in}} = \qty{3}{\ampere}$
* dati: $I_{\mathrm{out}} = \qty{1}{\ampere}$
* richiesto: $\eta$

<fragment>
$\begin{split} \eta &= \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}}\\ &= \frac{\qty{12}{\volt} \cdot \qty{1}{\ampere}}{\qty{5}{\volt} \cdot \qty{3}{\ampere}} = \frac{\qty{12}{\watt}}{\qty{15}{\watt}} = \num{0,8} = \qty{80}{\percent} \end{split}$
</fragment>
