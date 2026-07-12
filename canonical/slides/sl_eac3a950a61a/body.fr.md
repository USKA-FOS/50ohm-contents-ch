--- style="font-size: 0.7em;"

## Caractéristique d'antenne et directivité

<left>
[picture:264:a_strahlungscharakteristik_dipol_richt:Caractéristique de rayonnement d'une antenne directionnelle par rapport à un dipôle]
* Le *rapport avant/arrière* décrit à quel point l'émission et la réception sont meilleures dans la direction principale du faisceau.
</left>
<right>
* Les antennes directionnelles émettent et reçoivent également dans la direction arrière – un effet indésirable.  
* Le gain d'antenne ne se réfère qu'à la direction principale du faisceau (par rapport à un dipôle ou à un radiateur isotrope).  
</right>

---

[question:AG214]

---

[question:AG213]

---

### Rapport avant/arrière en décibels

<left>
[picture:263:a_strahlungscharakteristik_richt:Caractéristique de rayonnement d'une antenne directionnelle]
</left>
<right>
* Le rapport avant/arrière est souvent exprimé en décibels.
</right>

---

[question:AG217]

---
#### Solution
* donné : $P_R = \qty{0,6}{\watt}$
* donné : $P_V = \qty{15}{\watt}$
* recherché : $\frac{avant}{arrière}$

<fragment>
$\begin{split}\frac{avant}{arrière} &= 10 \cdot \log_{10}{\left(\frac{P_V}{P_R}\right)} \unit{\dB}\\ &= 10 \cdot \log_{10}{\left(\frac{\qty{15}{\watt}}{\qty{0,6}{\watt}}\right)} \unit{\dB}\\ &= \qty{14}{\dB}\end{split}$
</fragment>

---

[question:AG215]

--- style="font-size: smaller;"
#### Solution
<left>
* donné : $g_D= \qty{10}{\dB}$
* donné : $\frac{avant}{arrière} = \qty{20}{\dB}$
</left>
<right>
* donné : $P_S = \qty{100}{\watt}$
* recherché : $P_R$
</right>

<left>
<fragment>
$\begin{split}P_V &= P_{ERP}\\ &= P_S \cdot 10^{\frac{g_d}{\qty{10}{\dB}}}\\ &= \qty{100}{\watt} \cdot 10^{\frac{\qty{10}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{1000}{\watt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}\qty{20}{\dB} &= 10 \cdot \log_{10}{\left(\frac{P_V}{P_R}\right)} \unit{\dB}\\ \Rightarrow \frac{P_V}{P_R} &= 10^{\frac{\qty{20}{\dB}}{\qty{10}{\dB}}}\\ &= 100\\ \Rightarrow P_R &= \frac{P_V}{100}\\ &= \frac{\qty{1000}{\watt}}{100}\\ &= \qty{10}{\watt}\end{split}$
</fragment>
</right>
---

[question:AG216]

--- style="font-size: smaller;"
#### Solution
<left>
* donné : $g_D= \qty{15}{\dB}$
* donné : $\frac{avant}{arrière} = \qty{25}{\dB}$
</left>
<right>
* donné : $P_S = \qty{6}{\watt}$
* recherché : $P_R$
</right>

<left>
<fragment>
$\begin{split}P_V &= P_{ERP}\\ &= P_S \cdot 10^{\frac{g_d}{\qty{10}{\dB}}}\\ &= \qty{6}{\watt} \cdot 10^{\frac{\qty{15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{189,7}{\watt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}\qty{25}{\dB} &= 10 \cdot \log_{10}{\left(\frac{P_V}{P_R}\right)} \unit{\dB}\\ \Rightarrow \frac{P_V}{P_R} &= 10^{\frac{\qty{25}{\dB}}{\qty{10}{\dB}}}\\ &= 316,2\\ \Rightarrow P_R &= \frac{P_V}{316,2}\\ &= \frac{\qty{189,7}{\watt}}{316,2}\\ &= \qty{0,6}{\watt}\end{split}$
</fragment>
</right>

---

[question:AG218]

--- style="font-size: smaller;"
#### Solution
<left>
* donné : $U_V = \qty{300}{\micro\volt\per\meter}$
* donné : $U_R = \qty{20}{\micro\volt\per\meter}$
</left>
<right>
* donné : $U_D = \qty{128}{\micro\volt\per\meter}$
* recherché : $g_D$, $\frac{avant}{arrière}$
</right>

<left>
<fragment>
$\begin{split}g_D &= 20 \cdot \log_{10}{\left(\frac{U_V}{U_D}\right)} \unit{\dB}\\ &= 20 \cdot \log_{10}{\left(\frac{\qty{300}{\micro\volt\per\meter}}{\qty{128}{\micro\volt\per\meter}}\right)}\\ &= \qty{7,4}{\dB}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}\frac{avant}{arrière} &= 20 \cdot \log_{10}{\left(\frac{U_V}{U_R}\right)} \unit{\dB}\\ &= 20 \cdot \log_{10}{\left(\frac{\qty{300}{\micro\volt\per\meter}}{\qty{20}{\micro\volt\per\meter}}\right)}\\ &= \qty{23,5}{\dB}\end{split}$
</fragment>
</right>
