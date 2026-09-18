In pratica, le velocità di trasmissione dati raggiungibili differiscono notevolmente a seconda del metodo di trasmissione e delle condizioni radio. WLAN e 5G supportano, in condizioni ottimali, velocità di trasmissione dati fino a gigabit al secondo. FT8, invece, può essere utilizzato anche in condizioni avverse, ma trasmette solo pochi bit al secondo.

La velocità di trasmissione dati raggiungibile dipende dalla larghezza di banda disponibile e dal rapporto segnale / rumore ($P_\text{S}/P_\text{N}$). Da queste due grandezze, con la legge di Shannon-Hartley, è possibile calcolare la velocità di trasmissione dati teoricamente massima per un canale di trasmissione:

$C=B \cdot \log_2 \left(1+{\dfrac{P_\text{S}}{P_\text{N}}}\right) \unit{\bit\per\second}$

[question:AE416]

---

Un valore facile da ricordare si ottiene con un rapporto segnale / rumore di $\qty{0}{\dB}$. In questo caso, la larghezza di banda in $\unit{\hertz}$ corrisponde esattamente alla velocità di trasmissione dati massima raggiungibile in $\unit{\bit\per\second}$. Rapporti segnale / rumore peggiori consentono velocità di trasmissione dati inferiori, mentre rapporti migliori permettono velocità superiori. Con questo aiuto mnemonico, è possibile rispondere rapidamente alle relative domande d'esame anche senza lunghi calcoli.

<margin>
Se sostituiamo $\frac{P_\text{S}}{P_\text{N}} = \qty{0}{\dB}$, quindi il fattore $\num{1}$, otteniamo:
  
$\begin{split} C&=B \cdot \log_2 \left(1+1\right) \unit{\bit\per\second}\\ C&=B \cdot \log_2 \left(2\right) \unit{\bit\per\second}\\C &= \qty{B}{\bit\per\second}\end{split}$
</margin>

---

Se si desidera trasmettere significativamente più bit al secondo di quanta larghezza di banda in $\unit{\hertz}$ sia disponibile, il rapporto segnale / rumore richiesto aumenta notevolmente. Quindi, tramite connessioni a banda stretta in onde corte, non è possibile ottenere velocità di trasmissione dati elevate. Ad esempio, il Hamnet, come rete dati veloce, viene generalmente utilizzato nella parte alta delle UHF e nella parte bassa delle SHF, dove sono disponibili larghezze di banda maggiori.

<indepth>
Qui viene considerata solo l'energia di rumore all'interno della larghezza di banda utilizzata. Alcuni programmi per computer, invece, utilizzano l'energia di rumore di un canale largo $\qty{2,4}{\kilo\hertz}$, anche se il segnale utile effettivo è molto più stretto; questa, tuttavia, è una grandezza diversa che non può essere inserita direttamente nella formula della legge di Shannon-Hartley.
</indepth>

Abbassando la velocità di trasmissione dati, invece, è possibile sviluppare metodi che non solo richiedono una larghezza di banda ridotta, ma funzionano anche con un rapporto segnale / rumore estremamente scarso. Esempi di ciò sono i metodi di trasmissione digitale come WSPR o FT8, che scambiano solo pochi caratteri per unità di tempo. In questo modo, anche in condizioni radio sfavorevoli, è possibile almeno trasmettere un breve messaggio.

[question:AE417]
[question:AE418]
[question:AE420]
[question:AE419]

Da notare che la legge di Shannon-Hartley determina solo un limite superiore per la velocità di trasmissione dati raggiungibile. Le velocità effettivamente raggiungibili sono sempre inferiori. Solo con buoni metodi di correzione degli errori, che impareremo più avanti, è possibile avvicinarsi a questo limite superiore.