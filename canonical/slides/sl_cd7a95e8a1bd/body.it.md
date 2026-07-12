## Formula approssimata per l'intensità di campo
<left>
* Calcolo dell'intensità di campo elettrico
* A distanza da un irradiatore
* Dato la potenza e il guadagno
* Valido solo nello spazio libero <br/> ($d > \frac{\lambda}{2\pi}$)
</left>
<right>
$\begin{split} E &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{d}\\ &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{d} \end{split}$
</right>

---
## Formula approssimata per la distanza
<left>
* Data l'intensità di campo
* Riorganizzare per $d$
</left>
<right>
$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{E}\\ &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{E} \end{split}$
</right>

---
[question:EK108]
---
### Percorso di soluzione
<left>
* dato: $E = \qty{28}{\volt\per\meter}$
* dato: $g_d = \qty{7,5}{\dBd}$
* dato: $P_S = \qty{100}{\watt}$
</left>
<right>
* dato: $a_{\textrm{cavo}} = \qty{1,5}{\dB}$
* cercato: $P_{\textrm{EIRP}}$
* cercato: $d$
</right>

<left>
<fragment>
$\begin{split} P_{\textrm{EIRP}} &= P_S \cdot 10^{\frac{g_d - a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{100}{\watt} \cdot 10^{\frac{\qty{7,5}{\dBd} - \qty{1,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{100}{\watt} \cdot 6,5\\ &= \qty{650}{\watt} \end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{E}\\ &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{650}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{5}{\meter} \end{split}$
</fragment>
</right>

---
### Domanda bonus

La distanza calcolata di $\qty{5}{\meter}$ non rientra nel campo vicino per la banda dei $\qty{10}{\meter}$ della domanda?

<fragment>
$\begin{split} d &> \frac{\lambda}{2\pi}\\ \qty{5}{\meter} &> \frac{\qty{10}{\meter}}{2\pi}\\ \qty{5}{\meter} &\gtrapprox \qty{1,6}{\meter} \end{split}$
</fragment>

---
[question:EK106]
---
### Soluzione

* La distanza di sicurezza per la protezione delle persone è valida solo nello spazio libero
* $d > \frac{\lambda}{2\pi}$
* Banda dei $\qty{160}{\meter}$: $\qty{25,5}{\meter}$
* Banda degli $\qty{80}{\meter}$: $\qty{12,7}{\meter}$

---
[question:EK105]

<note>
Si trova nel campo vicino, come abbiamo calcolato in precedenza
</note>

