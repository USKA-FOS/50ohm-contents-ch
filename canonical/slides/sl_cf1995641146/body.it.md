## Distanza di sicurezza: calcolo del campo lontano (senza attenuazione del cavo)

* Per gli impianti radioamatoriali fissi, la distanza di sicurezza viene determinata mediante la formula del campo lontano

<fragment>
$d=\dfrac{\sqrt{30\,\Omega\cdot P_A\cdot G_i}}{E}$
</fragment>

--- style="font-size: 0.7em;"
#### Informazioni aggiuntive sui metodi di modulazione nel calcolo della distanza di sicurezza

* Nella visualizzazione di un impianto radioamatoriale fisso (ai sensi del § 9, BEMFV) deve essere inserito il fattore di conversione $\textrm{Fattore}_\textrm{FmodPers}$
* Questo fattore converte la potenza di picco (PEP) indicata nella potenza media, che viene utilizzata nella formula del campo lontano per il calcolo della distanza di sicurezza
* La maggior parte dei metodi di modulazione ha un fattore pari a $\num{1}$
* ATV: fattore $\num{0,38}$

<note>
DIN EN 50413, rilevante per il radioamatore solo per ATV con $\num{0,38}$ e SATV con $\num{0,54}$
</note>

---

[question:AK106]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dati: $E = \qty{28}{\volt\per\metro}$
* dati: $P_S = P_A = \qty{100}{\watt}$
</left>
<right>
* dati: $G_i = 1,64$
* cercato: $d$
</right>

<fragment>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{100}{\watt} \cdot 1,64}}{\qty{28}{\volt\per\metro}}\\ &\approx \qty{2,5}{\metro}\end{split}$
</fragment>

---
## Distanza di sicurezza: considerazione dell'attenuazione del cavo
* Inizialmente viene calcolata la potenza isotropa irradiata efficace (EIRP)

<fragment>
$P_\text{EIRP} = P_S\cdot10^{\frac{g_d - a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}$
</fragment>

---

[question:AK108]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dati: $E = \qty{28}{\volt\per\metro}$
* dati: $P_S = \qty{300}{\watt}$
* dati: $a = \qty{0,5}{\dB}$
</left>
<right>
* dati: $g_d = \qty{0}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{300}{\watt} \cdot 10^{\frac{\qty{0}{\dBd} - \qty{0,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{438,7}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{438,7}{\watt}}}{\qty{28}{\volt\per\metro}}\\ &\approx \qty{4,10}{\metro}\end{split}$
</right>
</fragment>

---

[question:AK109]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dati: $E = \qty{28}{\volt\per\metro}$
* dati: $P_S = \qty{700}{\watt}$
* dati: $a = \qty{0,5}{\dB}$
</left>
<right>
* dati: $g_d = \qty{0}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{700}{\watt} \cdot 10^{\frac{\qty{0}{\dBd} - \qty{0,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1023,5}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1023,5}{\watt}}}{\qty{28}{\volt\per\metro}}\\ &\approx \qty{6,26}{\metro}\end{split}$
</right>
</fragment>

---

[question:AK110]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dati: $E = \qty{28}{\volt\per\metro}$
* dati: $P_S = \qty{75}{\watt}$
* dati: $a = \qty{1,5}{\dB}$
</left>
<right>
* dati: $g_d = \qty{11,5}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{75}{\watt} \cdot 10^{\frac{\qty{11,5}{\dBd} - \qty{1,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1230,4}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1230,4}{\watt}}}{\qty{28}{\volt\per\metro}}\\ &\approx \qty{6,86}{\metro}\end{split}$
</right>
</fragment>

---

[question:AK111]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dati: $E = \qty{28}{\volt\per\metro}$
* dati: $P_S = \qty{100}{\watt}$
* dati: $a = \qty{1,5}{\dB}$
</left>
<right>
* dati: $g_d = \qty{10,5}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{100}{\watt} \cdot 10^{\frac{\qty{10,5}{\dBd} - \qty{1,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1303,2}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1303,2}{\watt}}}{\qty{28}{\volt\per\metro}}\\ &\approx \qty{7,1}{\metro}\end{split}$
</right>
</fragment>

---

[question:AK112]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dati: $E = \qty{61}{\volt\per\metro}$
* dati: $P_S = \qty{40}{\watt}$
* dati: $a = \qty{2}{\dB}$
</left>
<right>
* dati: $g_d = \qty{18}{\dBd}$
* cercato: $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{40}{\watt} \cdot 10^{\frac{\qty{18}{\dBd} - \qty{2}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{2612,5}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{2612,5}{\watt}}}{\qty{61}{\volt\per\metro}}\\ &\approx \qty{4,6}{\metro}\end{split}$
</right>
</fragment>
