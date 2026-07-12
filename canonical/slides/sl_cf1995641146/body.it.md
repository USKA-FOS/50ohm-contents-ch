## Distanza di sicurezza: Calcolo del campo lontano (senza attenuazione del cavo)

* Per gli impianti radioamatoriali fissi, la distanza di sicurezza viene determinata utilizzando la formula del campo lontano

<fragment>
$d=\dfrac{\sqrt{30\,\Omega\cdot P_A\cdot G_i}}{E}$
</fragment>

--- style="font-size: 0.7em;"
#### Informazioni aggiuntive sui metodi di modulazione nel calcolo della distanza di sicurezza

* Nell'indicazione di un impianto radioamatoriale fisso (ai sensi del § 9, BEMFV), deve essere inserito il fattore di conversione $\textrm{Faktor}_\textrm{FmodPers}$
* Questo fattore converte la potenza di picco indicata (PEP) nella potenza media utilizzata nella formula del campo lontano per il calcolo della distanza di sicurezza
* La maggior parte dei metodi di modulazione ha qui il fattore $\num{1}$
* ATV: Fattore $\num{0,38}$

<note>
DIN EN 50413, per il radioamatore solo ATV con $\num{0,38}$ e SATV con $\num{0,54}$ sono rilevanti
</note>

---

[question:AK106]

--- style="font-size: smaller;"
#### Percorso di soluzione
<left>
* dato: $E = \qty{28}{\volt\per\meter}$
* dato: $P_S = P_A = \qty{100}{\watt}$
</left>
<right>
* dato: $G_i = 1,64$
* cercato: $d$
</right>

<fragment>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{100}{\watt} \cdot 1,64}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{2,5}{\meter}\end{split}$
</fragment>

---
## Distanza di sicurezza: Considerazione dell'attenuazione del cavo
* Viene prima calcolata la potenza isotropa irradiata effettiva (EIRP)

<fragment>
$P_\text{EIRP} = P_S\cdot10^{\frac{g_d - a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}$
</fragment>

---

[question:AK108]

--- style="font-size: smaller;"
#### Percorso di soluzione
<left>
* dato: $E = \qty{28}{\volt\per\meter}$
* dato: $P_S = \qty{300}{\watt}$
* dato: $a = \qty{0,5}{\dB}$
</left>
<right>
* dato: $g_d = \qty{0}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{300}{\watt} \cdot 10^{\frac{\qty{0}{\dBd} - \qty{0,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{438,7}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{438,7}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{4,10}{\meter}\end{split}$
</right>
</fragment>

---

[question:AK109]

--- style="font-size: smaller;"
#### Percorso di soluzione
<left>
* dato: $E = \qty{28}{\volt\per\meter}$
* dato: $P_S = \qty{700}{\watt}$
* dato: $a = \qty{0,5}{\dB}$
</left>
<right>
* dato: $g_d = \qty{0}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{700}{\watt} \cdot 10^{\frac{\qty{0}{\dBd} - \qty{0,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1023,5}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1023,5}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{6,26}{\meter}\end{split}$
</right>
</fragment>

---

[question:AK110]

--- style="font-size: smaller;"
#### Percorso di soluzione
<left>
* dato: $E = \qty{28}{\volt\per\meter}$
* dato: $P_S = \qty{75}{\watt}$
* dato: $a = \qty{1,5}{\dB}$
</left>
<right>
* dato: $g_d = \qty{11,5}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{75}{\watt} \cdot 10^{\frac{\qty{11,5}{\dBd} - \qty{1,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1230,4}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1230,4}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{6,86}{\meter}\end{split}$
</right>
</fragment>

---

[question:AK111]

--- style="font-size: smaller;"
#### Percorso di soluzione
<left>
* dato: $E = \qty{28}{\volt\per\meter}$
* dato: $P_S = \qty{100}{\watt}$
* dato: $a = \qty{1,5}{\dB}$
</left>
<right>
* dato: $g_d = \qty{10,5}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{100}{\watt} \cdot 10^{\frac{\qty{10,5}{\dBd} - \qty{1,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1303,2}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1303,2}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{7,1}{\meter}\end{split}$
</right>
</fragment>

---

[question:AK112]

--- style="font-size: smaller;"
#### Percorso di soluzione
<left>
* dato: $E = \qty{61}{\volt\per\meter}$
* dato: $P_S = \qty{40}{\watt}$
* dato: $a = \qty{2}{\dB}$
</left>
<right>
* dato: $g_d = \qty{18}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{40}{\watt} \cdot 10^{\frac{\qty{18}{\dBd} - \qty{2}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{2612,5}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{2612,5}{\watt}}}{\qty{61}{\volt\per\meter}}\\ &\approx \qty{4,6}{\meter}\end{split}$
</right>
</fragment>
