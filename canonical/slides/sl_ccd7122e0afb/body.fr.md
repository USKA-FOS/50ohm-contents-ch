<left>
[photo:299:StepUpDownWandler: Convertisseur abaisseur (Buck) / élévateur (Boost)]
</left>
<right>
* Convertit les tensions continues → convertisseur DC/DC
* Par exemple, de $\qty{13,8}{\volt}$ à $\qty{5}{\volt}$ → abaisseur (Buck)
* Par exemple, de $\qty{12}{\volt}$ à $\qty{19}{\volt}$ → élévateur (Boost)
</right>
<note>
Le convertisseur Buck-Boost de l’image permet de régler la tension de sortie entre 0,5 V et 25 V. La puissance maximale est de 25 W.
</note>
---
### Rendement

* Des pertes surviennent en raison des composants du circuit
* Rendement $\eta$, généralement exprimé en $\%$

<fragment>
$\eta = \frac{P_{\mathrm{sortie}}}{P_{\mathrm{entrée}}}$
</fragment>

---
[question:AB213]
---
#### Méthode de résolution
* donné : $U_{\mathrm{entrée}} = \qty{12}{\volt}$
* donné : $U_{\mathrm{sortie}} = \qty{5}{\volt}$
* donné : $I_{\mathrm{entrée}} = \qty{2}{\ampere}$
* donné : $I_{\mathrm{sortie}} = \qty{3}{\ampere}$
* recherché : $\eta$

<fragment>
$\begin{split} \eta &= \frac{P_{\mathrm{sortie}}}{P_{\mathrm{entrée}}} = \frac{U_{\mathrm{sortie}} \cdot I_{\mathrm{sortie}}}{U_{\mathrm{entrée}} \cdot I_{\mathrm{entrée}}}\\ &= \frac{\qty{5}{\volt} \cdot \qty{3}{\ampere}}{\qty{12}{\volt} \cdot \qty{2}{\ampere}} = \frac{\qty{15}{\watt}}{\qty{24}{\watt}} = \num{0,625} = \qty{62,5}{\percent} \end{split}$
</fragment>
---
[question:AB214]
---
* donné : $U_{\mathrm{entrée}} = \qty{5}{\volt}$
* donné : $U_{\mathrm{sortie}} = \qty{12}{\volt}$
* donné : $I_{\mathrm{entrée}} = \qty{3}{\ampere}$
* donné : $I_{\mathrm{sortie}} = \qty{1}{\ampere}$
* recherché : $\eta$

<fragment>
$\begin{split} \eta &= \frac{P_{\mathrm{sortie}}}{P_{\mathrm{entrée}}} = \frac{U_{\mathrm{sortie}} \cdot I_{\mathrm{sortie}}}{U_{\mathrm{entrée}} \cdot I_{\mathrm{entrée}}}\\ &= \frac{\qty{12}{\volt} \cdot \qty{1}{\ampere}}{\qty{5}{\volt} \cdot \qty{3}{\ampere}} = \frac{\qty{12}{\watt}}{\qty{15}{\watt}} = \num{0,8} = \qty{80}{\percent} \end{split}$
</fragment>
