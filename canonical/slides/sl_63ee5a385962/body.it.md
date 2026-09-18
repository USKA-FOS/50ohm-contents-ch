
* Considerare solo l'energia che arriva all'antenna
* Sottrarre le perdite $a$ dovute al cavo, ai connettori o ad altri componenti
* Moltiplicare solo successivamente per il fattore di guadagno
* Seguono diverse formule generali per ERP e EIRP

---
### ERP

Come noto dalla classe N:

$P_{\mathrm{ERP}} = (P_{\mathrm{Trasmettitore}} - P_{\mathrm{Perdite}}) \cdot G_{\mathrm{Antenna}}$

<fragment>
Nella calcolazione con $\unit{\dB}$ da utilizzare:

$P_{\mathrm{ERP}} = P_{\mathrm{Trasmettitore}} - a + g_d$
</fragment>

<fragment>
Dalla raccolta di formule con conversione da $\unit{\dB}$ a fattore di potenza:

$P_{\mathrm{ERP}} = P_{\mathrm{Trasmettitore}} \cdot 10^{\frac{g_d - a}{\qty{10}{\dB}}}$
</fragment>

---
### EIRP

Conversione ERP in EIRP:

$P_{\mathrm{EIRP}} = P_{\mathrm{ERP}} + \qty{2,15}{\dB}$

<fragment>
Dalla raccolta di formule con conversione da $\unit{\dB}$ a fattore di potenza:

$P_{\mathrm{EIRP}} = P_{\mathrm{Trasmettitore}} \cdot 10^{\frac{g_d - a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}$
</fragment>

<fragment>
Se il guadagno è indicato in $\unit{\dBi}$:

$P_{\mathrm{EIRP}} = P_{\mathrm{Trasmettitore}} \cdot 10^{\frac{g_i - a}{\qty{10}{\dB}}}$
</fragment>

---
[question:EG501]
---
[question:EG502]
---
## Impianto radioamatoriale fisso

Un impianto radioamatoriale fisso deve essere segnalato all'Agenzia federale delle reti (BNetzA) ai sensi del § 9 BEMFV se viene superata una potenza irradiata (EIRP) di $\qty{10}{\watt}$.
---
[question:EG503]
--- style="font-size: smaller;"
### Procedimento di soluzione

* dato: $P_{\mathrm{Trasmettitore}} = \qty{250}{\milli\watt}$
* dato: $g_i = \qty{26}{\dBi}$
* dato: $a = \qty{0}{\dB}$
* cercato: $P_{\mathrm{EIRP}}$

<fragment>
$\begin{split} P_{\mathrm{EIRP}} &= P_{\mathrm{Trasmettitore}} \cdot 10^{\frac{g_i - a}{\qty{10}{\dB}}}\\ &= \qty{250}{\milli\watt} \cdot 10^{\frac{\qty{26}{\dBi}}{\qty{10}{\dB}}}\\ &= \qty{250}{\milli\watt} \cdot 398\\ &\approx \qty{100}{\watt} \end{split}$
</fragment>

---
[question:EG504]

<note>
* Procedimento di soluzione identico al precedente
</note>
---
[question:EG511]
--- style="font-size: smaller;"
### Procedimento di soluzione

* dato: $P_{\mathrm{EIRP}} = \qty{10}{\watt}$
* dato: $g_i = \qty{5,15}{\dBi}$
* dato: $a = \qty{0}{\dB}$
* cercato: $P_{\mathrm{Trasmettitore}}$

<fragment>
$\begin{split} P_{\mathrm{EIRP}} &= P_{\mathrm{Trasmettitore}} \cdot 10^{\frac{g_i - a}{\qty{10}{\dB}}}\\ \Rightarrow P_{\mathrm{Trasmettitore}} &= \dfrac{P_{\mathrm{EIRP}}}{10^{\frac{g_i - a}{\qty{10}{\dB}}}}\\ &= \dfrac{\qty{10}{\watt}}{10^{\frac{\qty{5,15}{\dBi}}{\qty{10}{\dB}}}}\\ &\approx \frac{\qty{10}{\watt}}{3,27} \approx \qty{3}{\watt} \end{split}$
</fragment>

<note>
Esistono diversi modi per giungere alla soluzione. Ad esempio, è possibile calcolare direttamente con i logaritmi.
</note>
---
[question:EG505]

<note>
Guadagno: $\qty{10}{\dB}$, quindi anche fattore $\num{10}$
</note>
---
[question:EG507]

<note>
* Una perdita di $\qty{10}{\dB}$ corrisponde a un fattore $\num{10}$, quindi all'antenna arrivano $\qty{10}{\watt}$ di ERP
* Il fattore di conversione da ERP a EIRP è $\num{1,64}$
</note>
---
[question:EG506]

<note>
* Il guadagno del dipolo di $\qty{2,15}{\dBi}$ compensa esattamente le perdite del cavo
</note>
---

* Se il guadagno dell'antenna è riferito al dipolo, è necessario considerare anche il guadagno del dipolo stesso quando si chiede il valore di EIRP.

---
[question:EG508]
---
### Procedimento di soluzione

* dato: $P_{\mathrm{Trasmettitore}} = \qty{5}{\watt}$
* dato: $g_d = \qty{5}{\dBd}$
* dato: $a = \qty{2}{\dB}$
* cercato: $P_{\mathrm{EIRP}}$

<fragment>
$\begin{split} P_{\mathrm{EIRP}} &= P_{\mathrm{Trasmettitore}} \cdot 10^{\frac{g_d - a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{5}{\watt} \cdot 10^{\frac{\qty{5}{\dBd} - \qty{2}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{5}{\watt} \cdot 3,27\\ &\approx \qty{16,4}{\watt} \end{split}$
</fragment>

---
[question:EG509]

<note>
Procedimento di soluzione identico al precedente
</note>
---
[question:EG510]

<note>
Procedimento di soluzione identico al precedente
</note>