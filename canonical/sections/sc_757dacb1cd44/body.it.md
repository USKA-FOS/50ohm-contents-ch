Le velocità di trasmissione dati effettivamente raggiungibili in pratica differiscono notevolmente a seconda del metodo di trasmissione e delle condizioni radio. WLAN e 5G supportano, in condizioni ottimali, velocità di trasmissione dati fino a Gigabits al secondo. FT8, d'altra parte, può essere utilizzato anche in condizioni avverse, ma trasmette solo pochi bit al secondo.

La velocità di trasmissione dati raggiungibile dipende dalla larghezza di banda utilizzabile e dal rapporto segnale/rumore ($P_\text{S}/P_\text{N}$). Da queste due grandezze, utilizzando la legge di Shannon-Hartley, è possibile calcolare la velocità di trasmissione dati teoricamente massima raggiungibile per un canale di trasmissione:

$C=B \cdot \log_2 \left(1+{\dfrac{P_\text{S}}{P_\text{N}}}\right) \unit{\bit\per\second}$

[question:AE416]

---

Un valore facile da ricordare si ottiene con un rapporto segnale/rumore di $\qty{0}{\dB}$. Qui la larghezza di banda in $\unit{\hertz}$ corrisponde esattamente alla velocità di trasmissione dati massima raggiungibile in $\unit{\bit\per\second}$. Rapporti segnale/rumore peggiori consentono velocità di trasmissione dati inferiori, rapporti segnale/rumore migliori velocità di trasmissione dati superiori. Con questo aiuto mnemonico è possibile rispondere rapidamente alle relative domande d'esame anche senza lunghi calcoli.

<margin>
Se impostiamo $\frac{P_\text{S}}{P_\text{N}} = \qty{0}{\dB}$, cioè il fattore $\num{1}$, otteniamo:
  
$\begin{split} C&=B \cdot \log_2 \left(1+1\right) \unit{\bit\per\second}\\ C&=B \cdot \log_2 \left(2\right) \unit{\bit\per\second}\\C &= \qty{B}{\bit\per\second}\end{split}$
</margin>

---

Se si desidera trasmettere molti più bit al secondo di quanti ne siano disponibili in termini di larghezza di banda in $\unit{\hertz}$, il rapporto segnale/rumore richiesto aumenta notevolmente. Pertanto, tramite collegamenti a banda stretta sulle onde corte non è praticamente possibile ottenere elevate velocità di trasmissione dati. Così, Hamnet, come rete dati veloce, viene solitamente gestito nella gamma UHF superiore e SHF inferiore, dove sono disponibili larghezze di banda maggiori.

<indepth>
Qui viene considerata solo l'energia del rumore che rientra nella larghezza di banda utilizzata. Alcuni programmi per computer, tuttavia, utilizzano l'energia del rumore di un canale largo $\qty{2,4}{\kilo\hertz}$, anche se il segnale utile effettivo è molto più stretto; questa è tuttavia una grandezza diversa che non può essere inserita direttamente nella formula della legge di Shannon-Hartley.
</indepth>

Abbassando la velocità di trasmissione dati, invece, si possono sviluppare metodi che non solo richiedono una piccola larghezza di banda, ma funzionano anche con un rapporto segnale/rumore estremamente basso. Esempi di ciò sono i metodi di trasmissione digitale come WSPR o FT8, che scambiano solo pochi caratteri al secondo. In questo modo, anche in condizioni radio sfavorevoli, è possibile trasmettere almeno un breve messaggio.

[question:AE417]
[question:AE418]
[question:AE420]
[question:AE419]

Va notato che la legge di Shannon-Hartley determina solo un limite superiore per la velocità di trasmissione dati raggiungibile. Le velocità di trasmissione dati effettivamente raggiungibili sono sempre inferiori. Solo utilizzando buoni metodi di correzione degli errori, che impareremo in seguito, ci si può avvicinare a questo limite superiore.
