%Nel calcolo della potenza irradiata effettiva (ERP) va considerata solo l'energia che viene effettivamente immessa nell'antenna, cioè eventuali perdite del cavo possono essere sottratte prima di moltiplicare per il fattore di guadagno.

La potenza irradiata effettiva (ERP) di un'antenna si riferisce al dipolo a semionda. Per la potenza irradiata è rilevante solo l'energia che effettivamente arriva all'antenna. A causa dell'attenuazione del cavo, ecc., la potenza del trasmettitore non può essere completamente immessa nell'antenna nel mondo reale. Questa potenza persa non deve essere inclusa nel calcolo della potenza irradiata. Il guadagno d'antenna nella direzione preferita è naturalmente parte del calcolo. L'ERP è il prodotto della potenza immessa e del guadagno d'antenna.

[question:AG501]

Nella prossima domanda è assolutamente necessario prestare attenzione ai segni di calcolo. Le perdite vengono sottratte dalla potenza di trasmissione e poi moltiplicate per il fattore di guadagno ($G_{Antenna}$).
Dato che si deve calcolare l'ERP, è necessario fare riferimento a un dipolo a semionda.

[question:AG502]

---

Già il piano di frequenza per il servizio radioamatoriale fornisce un indizio per la soluzione corretta. Lì è specificata una potenza massima di $\qty{1}{\watt}$ ERP per la banda dei $\qty{630}{\meter}$.

Un dipolo a semionda avrebbe una lunghezza di $\qty{315}{\meter}$. Questo non è realizzabile per la maggior parte dei radioamatori. Inevitabilmente vengono utilizzate antenne fortemente accorciate. Purtroppo, le antenne accorciate hanno un rendimento inferiore rispetto a un dipolo a semionda di piena lunghezza. Un "guadagno d'antenna" di $\qty{-20}{\dBd}$ non è quindi sorprendente. Poiché il cavo coassiale è corto, la sua attenuazione in questa gamma di frequenza può essere trascurata.

Per risolvere la domanda AG503, si può fare riferimento alla tabella dei rapporti di potenza nella raccolta di formule. Lì, per $\qty{-20}{\dB}$ è indicato il fattore $\num{0,01}$.

$\qty{50}{\watt}\cdot 0,01 = \qty{0,5}{\watt}$

La soluzione corretta è $\qty{0,5}{\watt}$.

%Un trasmettitore per la banda dei $\qty{630}{\meter}$ con una potenza d'uscita di $\qty{50}{\watt}$ è collegato tramite un breve cavo coassiale a un'antenna con una perdita di $\qty{20}{\dBd}$. Quale ERP viene irradiata dall'antenna?

[question:AG503]

<tip>
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

</tip>
