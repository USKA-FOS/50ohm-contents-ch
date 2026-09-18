## Calcolo della potenza irradiata effettiva (ERP)

* Considerare solo l'energia che effettivamente arriva all'antenna – sottrarre le perdite del cavo
* L'ERP viene calcolato come prodotto tra la potenza fornita e il guadagno d'antenna (riferito a un dipolo a semionda)

---
[question:AG501]
---

### Note per il calcolo dell'ERP

* Le perdite vengono sottratte dalla potenza di trasmissione prima di applicare il fattore di guadagno ($G_{antenna}$)
* Il riferimento a un dipolo a semionda deve essere rispettato nel calcolo

---
[question:AG502]
---

### ERP nel radioamatoriale – esempio pratico

* Il piano delle bande per la banda dei $\qty{630}{\m}$ prevede una potenza irradiata massima di $\qty{1}{\W}$
* Un dipolo a semionda avrebbe una lunghezza di $\qty{315}{\m}$ a $\qty{630}{\m}$ – solitamente non realizzabile, quindi si utilizzano antenne accorciate
* Le antenne accorciate hanno un rendimento inferiore, ad esempio un guadagno d'antenna di $\qty{-20}{\dBd}$
* Rapporto di potenza: $\qty{-20}{\dB}$ corrisponde a un fattore di $\num{0,01}$; esempio: $\qty{50}{\W} \cdot 0,01 = \qty{0,5}{\W}$ ERP

--- style="font-size: 0.7em;"

### Rapporti di potenza nella raccolta di formule

Questa tabella è inclusa nella raccolta di formule ed è disponibile durante l'esame.

| r:   | r: Rapporto di potenza | r: Rapporto di tensione |
| $\qty{-20}{\dB}$ | $\num{0,01}$ | $\num{0,1}$ |
| $\qty{-10}{\dB}$ | $\num{0,1}$ | $\num{0,32}$ |
| $\qty{-6}{\dB}$ | $\num{0,25}$ | $\num{0,5}$ |
| $\qty{-3}{\dB}$ | $\num{0,5}$ | $\num{0,71}$ |
| $\qty{-1}{\dB}$ | $\num{0,79}$ | $\num{0,89}$ |
| $\qty{0}{\dB}$ | $\num{1}$ | $\num{1}$ |
| $\qty{1}{\dB}$ | $\num{1,26}$ | $\num{1,12}$ |
| $\qty{3}{\dB}$ | $\num{2}$ | $\num{1,41}$ |
| $\qty{6}{\dB}$ | $\num{4}$ | $\num{2}$ |
| $\qty{10}{\dB}$ | $\num{10}$  | $\num{3,16}$ |
| $\qty{20}{\dB}$ | $\num{100}$ | $\num{10}$ |
[table:Pegel_Verhältnis:Rapporti di potenza e tensione per valori importanti di attenuazione e amplificazione]

---
[question:AG503]
---
#### Percorso di soluzione
* dato: $P_S = \qty{50}{\W}$
* dato: $a \approx \qty{0}{\dB}$
* dato: $g_d = \qty{-20}{\dBd}$
* cercato: $P_{\textrm{ERP}}$

<fragment>
$\begin{split} P_{\textrm{ERP}} &= P_S \cdot 10^{\frac{g_d - a}{\qty{10}{\dB}}}\\ &= \qty{50}{\W} \cdot 10^{\frac{\qty{-20}{\dBd} - \qty{0}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{50}{\W} \cdot 10^{-2} = \qty{0,5}{\W}\end{split}$
</fragment>
