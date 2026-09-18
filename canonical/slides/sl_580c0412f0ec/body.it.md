<left>
[picture:978:a_swr:Onda stazionaria]
</left>
<right>
* Il rapporto d’onda stazionaria (ROS) può spesso essere indicato direttamente in base alla resistenza di alimentazione di un’antenna
* In presenza di una pura resistenza attiva (senza componenti induttive o capacitive), il ROS si calcola dal rapporto tra la resistenza di carico e la resistenza caratteristica del cavo (in modo che ROS ≥ 1)
</right>

---

* Esempio: Un’antenna con $\qty{100}{\ohm}$ su un cavo da $\qty{50}{\ohm}$ porta a un ROS di $\num{2}$, mentre una con $\qty{10}{\ohm}$ porta a un ROS di $\num{5}$
* Per memoria: La resistenza di un dipolo ripiegato è di circa $\qty{300}{\ohm}$

---
[question:AG405]
---
#### Procedimento di soluzione
* dato: $Z = \qty{75}{\ohm}$
* dato: $R_2 \approx \qty{300}{\ohm}$ resistenza dipolo ripiegato
* cercato: $s$

<fragment>
$s = \frac{R_2}{Z} = \frac{\qty{300}{\ohm}}{\qty{75}{\ohm}} = 4$
</fragment>
---

### Influenza dell’attenuazione della linea sul rapporto d’onda stazionaria

* L’attenuazione della linea riduce sia la potenza incidente che quella riflessa
* Anche se al termine del cavo viene riflessa il $\qty{100}{\percent}$ dell’energia, al trasmettitore può essere misurato un ROS inferiore (migliore)
* Esempio: Se nella direzione di andata e di ritorno viene persa metà della potenza, rimane solo un quarto della potenza originale – questo corrisponde a un ROS misurato di $\num{3}$ ($
\qty{25}{\percent}$ di potenza riflessa)

---
[question:AG402]

[question:AG403]

---

### Effetto dell’attenuazione della linea sul ROS misurato

* Con un’attenuazione della linea di $\qty{5}{\dB}$ nella direzione di andata e di ritorno (in totale $\qty{10}{\dB}$), la potenza riflessa corrisponde solo a un decimo della potenza incidente
* Il ROS misurato può essere calcolato con la formula:

<fragment>
$s = \frac{\sqrt{P_\mathrm{i}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{i}}-\sqrt{P_\mathrm{r}}}$
</fragment>

---
[question:AG404]

#### Procedimento di soluzione
* dato: $P_i = \qty{10}{\watt}$
* dato: $a = \qty{5}{\dB}$
* cercato: $s$

<fragment>
Attenuazione totale del cavo per andata e ritorno: $\qty{10}{\dB}$
$P_r = \qty{-10}{\dB} \cdot P_i = \dfrac{\qty{10}{\watt}}{10} = \qty{1}{\watt}$
</fragment>
<fragment>
$s = \dfrac{\sqrt{P_\mathrm{i}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{i}}-\sqrt{P_\mathrm{r}}} = \dfrac{\sqrt{\qty{10}{\watt}}+\sqrt{\qty{1}{\watt}}}{\sqrt{\qty{10}{\watt}}-\sqrt{\qty{1}{\watt}}} = 1,92$
</fragment>