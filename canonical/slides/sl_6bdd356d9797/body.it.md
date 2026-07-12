## Calcolo della potenza irradiata effettiva (ERP)

* Considerare solo l'energia che raggiunge effettivamente l'antenna – le perdite del cavo vengono sottratte
* L'ERP viene calcolata come prodotto della potenza fornita e del guadagno d'antenna (riferito a un dipolo a semionda)

---
[question:AG501]
---

### Note di calcolo per l'ERP

* Le perdite vengono sottratte dalla potenza di trasmissione prima che venga applicato il fattore di guadagno ($G_{Antenne}$)
* Il riferimento a un dipolo a semionda deve essere mantenuto nel calcolo

---
[question:AG502]
---

### ERP nel radioamatore – Esempio pratico

* Il piano di frequenza per la banda dei $\qty{630}{\meter}$ prevede un ERP massimo di $\qty{1}{\watt}$
* Un dipolo a semionda a $\qty{630}{\meter}$ avrebbe una lunghezza di $\qty{315}{\meter}$ – solitamente non realizzabile, quindi vengono utilizzate antenne accorciate
* Le antenne accorciate hanno un rendimento inferiore, ad esempio un guadagno d'antenna di $\qty{-20}{\dBd}$
* Rapporto di potenza: $\qty{-20}{\dB}$ corrisponde a un fattore di $\num{0,01}$; esempio: $\qty{50}{\watt} \cdot 0,01 = \qty{0,5}{\watt}$ ERP

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
[table:Pegel_Verhältnis:Leistungs- und Spannungsverhältnisse für wichtige Dämpfungs- und Verstärkungswerte]

---
[question:AG503]
---
#### Percorso di soluzione
* dato: $P_S = \qty{50}{\watt}$
* dato: $a \approx \qty{0}{\dB}$
* dato: $g_d = \qty{-20}{\dBd}$
* cercato: $P_{\textrm{ERP}}$

<fragment>
$\begin{split} P_{\textrm{ERP}} &= P_S \cdot 10^{\frac{g_d - a}{\qty{10}{\dB}}}\\ &= \qty{50}{\watt} \cdot 10^{\frac{\qty{-20}{\dBd} - \qty{0}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{50}{\watt} \cdot 10^{-2} = \qty{0,5}{\watt}\end{split}$
</fragment>
