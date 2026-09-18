--- style="font-size: 0.7em;"

## Caratteristiche delle antenne e direttività

<left>
[picture:264:a_strahlungscharakteristik_dipol_richt:Caratteristica di radiazione di un'antenna direzionale rispetto a un dipolo]
* Il *rapporto avanti/indietro* descrive quanto è migliore la trasmissione e la ricezione nella direzione principale rispetto alle altre direzioni.
</left>
<right>
* Le antenne direzionali trasmettono e ricevono anche nella direzione opposta – un effetto indesiderato.
* Il guadagno d'antenna si riferisce solo alla direzione principale (rispetto a un dipolo o a un radiatore isotropico).
</right>

---

[question:AG214]

---

[question:AG213]

---

### Rapporto avanti/indietro in decibel

<left>
[picture:263:a_strahlungscharakteristik_richt:Caratteristica di radiazione di un'antenna direzionale]
</left>
<right>
* Il rapporto avanti/indietro viene spesso espresso in decibel.
</right>

---

[question:AG217]

---
#### Procedimento di soluzione
* dati: $P_R = \qty{0,6}{\watt}$
* dati: $P_V = \qty{15}{\watt}$
* richiesto: $\frac{Avanti}{Indietro}$

<fragment>
$\begin{split}\frac{Avanti}{Indietro} &= 10 \cdot \log_{10}{\left(\frac{P_V}{P_R}\right)} \unit{\dB}\\ &= 10 \cdot \log_{10}{\left(\frac{\qty{15}{\watt}}{\qty{0,6}{\watt}}\right)} \unit{\dB}\\ &= \qty{14}{\dB}\end{split}$
</fragment>

---

[question:AG215]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dati: $g_D= \qty{10}{\dB}$
* dati: $\frac{Avanti}{Indietro} = \qty{20}{\dB}$
</left>
<right>
* dati: $P_S = \qty{100}{\watt}$
* richiesto: $P_R$
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
#### Procedimento di soluzione
<left>
* dati: $g_D= \qty{15}{\dB}$
* dati: $\frac{Avanti}{Indietro} = \qty{25}{\dB}$
</left>
<right>
* dati: $P_S = \qty{6}{\watt}$
* richiesto: $P_R$
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
#### Procedimento di soluzione
<left>
* dati: $U_V = \qty{300}{\micro\volt\per\meter}$
* dati: $U_R = \qty{20}{\micro\volt\per\meter}$
</left>
<right>
* dati: $U_D = \qty{128}{\micro\volt\per\meter}$
* richiesto: $g_D$, $\frac{Avanti}{Indietro}$
</right>

<left>
<fragment>
$\begin{split}g_D &= 20 \cdot \log_{10}{\left(\frac{U_V}{U_D}\right)} \unit{\dB}\\ &= 20 \cdot \log_{10}{\left(\frac{\qty{300}{\micro\volt\per\meter}}{\qty{128}{\micro\volt\per\meter}}\right)}\\ &= \qty{7,4}{\dB}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}\frac{Avanti}{Indietro} &= 20 \cdot \log_{10}{\left(\frac{U_V}{U_R}\right)} \unit{\dB}\\ &= 20 \cdot \log_{10}{\left(\frac{\qty{300}{\micro\volt\per\meter}}{\qty{20}{\micro\volt\per\meter}}\right)}\\ &= \qty{23,5}{\dB}\end{split}$
</fragment>
</right>
