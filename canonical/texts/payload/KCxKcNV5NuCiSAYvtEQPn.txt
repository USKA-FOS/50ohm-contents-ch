<left>
[photo:299:StepUpDownWandler: Abwärts- (Buck) Aufwärts- (Boost) Wandler]
</left>
<right>
* Wandelt Gleichspannungen um $\rightarrow$ DC/DC-Wandler
* z.B. von $\qty{13,8}{\volt}$ auf $\qty{5}{\volt}\rightarrow$ Step-DOWN (Tiefsetzsteller)
* z.B. von $\qty{12}{\volt}$ auf $\qty{19}{\volt}\rightarrow$ Step-UP (Hochsetzsteller)
</right>
<note>
Der Buck-Boost Converter im Bild kann von 0,5V bis 25V am Ausgang eingestellt werden. Die maximale Leistung beträgt 25W.
</note>
---
### Wirkungsgrad

* Es entstehen Verluste durch die Bauteile in der Schaltung
* Wirkungsgrad $\eta$, meistens in $\%$ angegeben

<fragment>
$\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$
</fragment>

---
[question:AB213]
---
#### Lösungsweg
* gegeben: $U_{\textrm{in}} = \qty{12}{\volt}$
* gegeben: $U_{\textrm{out}} = \qty{5}{\volt}$
* gegeben: $I_{\textrm{in}} = \qty{2}{\ampere}$
* gegeben: $I_{\textrm{out}} = \qty{3}{\ampere}$
* gesucht: $\eta$

<fragment>
$\begin{split} \eta &= \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}}\\ &= \frac{\qty{5}{\volt} \cdot \qty{3}{\ampere}}{\qty{12}{\volt} \cdot \qty{2}{\ampere}} = \frac{\qty{15}{\watt}}{\qty{24}{\watt}} = \num{0,625} = \qty{62,5}{\percent} \end{split}$
</fragment>
---
[question:AB214]
---
* gegeben: $U_{\mathrm{in}} = \qty{5}{\volt}$
* gegeben: $U_{\mathrm{out}} = \qty{12}{\volt}$
* gegeben: $I_{\mathrm{in}} = \qty{3}{\ampere}$
* gegeben: $I_{\mathrm{out}} = \qty{1}{\ampere}$
* gesucht: $\eta$

<fragment>
$\begin{split} \eta &= \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}}\\ &= \frac{\qty{12}{\volt} \cdot \qty{1}{\ampere}}{\qty{5}{\volt} \cdot \qty{3}{\ampere}} = \frac{\qty{12}{\watt}}{\qty{15}{\watt}} = \num{0,8} = \qty{80}{\percent} \end{split}$
</fragment>
