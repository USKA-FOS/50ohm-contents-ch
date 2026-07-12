<left>
[photo:299:StepUpDownWandler: Convertisseur élévateur-abaisseur]
</left>
<right>
* Convertit les tensions continues $\rightarrow$ Convertisseur DC/DC
* Par exemple, de $\qty{13,8}{\volt}$ à $\qty{5}{\volt}\rightarrow$ Step-DOWN (abaisseur)
* Par exemple, de $\qty{12}{\volt}$ à $\qty{19}{\volt}\rightarrow$ Step-UP (élévateur)
</right>
<note>
Le convertisseur Buck-Boost sur l'image peut être réglé de 0,5V à 25V en sortie. La puissance maximale est de 25W.
</note>
---
### Rendement

* Des pertes sont générées par les composants du circuit
* Rendement $\eta$, généralement exprimé en $\%$

<fragment>
$\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$
</fragment>

---
[question:AB213]
---
#### Solution
* Donné : $U_{\textrm{in}} = \qty{12}{\volt}$
* Donné : $U_{\textrm{out}} = \qty{5}{\volt}$
* Donné : $I_{\textrm{in}} = \qty{2}{\ampere}$
* Donné : $I_{\textrm{out}} = \qty{3}{\ampere}$
* Recherché : $\eta$

<fragment>
$\begin{split} \eta &= \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}}\\ &= \frac{\qty{5}{\volt} \cdot \qty{3}{\ampere}}{\qty{12}{\volt} \cdot \qty{2}{\ampere}} = \frac{\qty{15}{\watt}}{\qty{24}{\watt}} = \num{0,625} = \qty{62,5}{\percent} \end{split}$
</fragment>
---
[question:AB214]
---
* Donné : $U_{\mathrm{in}} = \qty{5}{\volt}$
* Donné : $U_{\mathrm{out}} = \qty{12}{\volt}$
* Donné : $I_{\mathrm{in}} = \qty{3}{\ampere}$
* Donné : $I_{\mathrm{out}} = \qty{1}{\ampere}$
* Recherché : $\eta$

<fragment>
$\begin{split} \eta &= \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}}\\ &= \frac{\qty{12}{\volt} \cdot \qty{1}{\ampere}}{\qty{5}{\volt} \cdot \qty{3}{\ampere}} = \frac{\qty{12}{\watt}}{\qty{15}{\watt}} = \num{0,8} = \qty{80}{\percent} \end{split}$
</fragment>
