Abbiamo imparato: se un'antenna è perfettamente adattata alla linea di alimentazione (ad esempio un cavo coassiale), il rosmetro indica il valore 1. Questo è il caso migliore, poiché l'intera potenza di trasmissione viene assorbita dall'antenna e non viene riflessa alcuna potenza verso il trasmettitore. Se invece non è collegata alcuna antenna o la linea di trasmissione è interrotta o in corto circuito, il valore del ROS sale verso infinito ($\infty$). In questi casi, la potenza di trasmissione viene quasi completamente riflessa. Una riflessione totale di questo tipo può, nel caso peggiore, danneggiare lo stadio finale del trasmettitore. Approfondiamo ora l'argomento e prendiamo in considerazione anche valori compresi tra $\num{1}$ e $\infty$.


Il rapporto d’onda stazionaria (ROS), indicato con il simbolo $s$, può essere calcolato a partire dalla potenza incidente $P_\text{V}$ e dalla potenza riflessa $P_\text{R}$ con la seguente relazione:


$s = \frac{\sqrt{P_\text{V}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{V}}-\sqrt{P_\text{R}}}$


Se, ad esempio, il trasmettitore emette una potenza di $P_\text{V}=\qty{100}{\watt}$ e vengono riflessi verso il trasmettitore $P_\text{R}=\qty{25}{\watt}$ dall'antenna, si ottiene:


$s = \frac{\sqrt{100}+\sqrt{25}}{\sqrt{100}-\sqrt{25}} = \frac{10+5}{10-5} = \frac{15}{5} = 3$


Questo significa che un ROS di $\num{3}$ corrisponde a una riflessione di $\frac{\qty{25}{\watt}}{\qty{100}{\watt}}=\qty{25}{\percent}$.


Ulteriori corrispondenze sono illustrate nella tabella [ref:e_swr_werte].


<margin>
| l: ROS | l: Potenza riflessa |
| $\num{1}$ | $\qty{0}{\percent}$ |
| $\num{1,5}$ | $\qty{4}{\percent}$ |
| $\num{2}$ | $\qty{11,1}{\percent}$ |
| $\num{2,5}$ | $\qty{18,4}{\percent}$ |
| *$\num{3}$* | *$\qty{25}{\percent}$* |
| $\num{4}$ | $\qty{36}{\percent}$ |
| $\num{6}$ | $\qty{51}{\percent}$ |
| $\num{10}$ | $\qty{66,9}{\percent}$ |
| $\num{20}$ | $\qty{81,9}{\percent}$ |
| $\infty$ | $\qty{100}{\percent}$ |
[tabella:valori_ros:Valori del ROS in relazione alla potenza riflessa]
</margin>

---

<tip>
Per rispondere alle domande seguenti, è sufficiente sapere che un rapporto d’onda stazionaria di $\num{3}$ corrisponde a una riflessione del $\qty{25}{\percent}$ dell’energia, cioè l’onda riflessa trasmette un quarto dell’energia dell’onda incidente. Di conseguenza, solo $\qty{75}{\percent}$ dell’energia viene emessa alla fine della linea, ad esempio verso un'antenna o una resistenza di perdita (quindi non riflessa).
</tip>


[domanda:EG401]
[domanda:EG402]
[domanda:EG403]


<indepth>
Derivazione della formula del ROS utilizzata qui, basata sulla raccolta di formule dell’UFCOM.
È possibile utilizzare direttamente la formula sopra. Non è necessario comprendere la derivazione! 😉


1. Base di partenza (raccolta di formule dell’UFCOM)

La raccolta di formule dell’UFCOM definisce il rapporto d’onda stazionaria ($s$) e il coefficiente di riflessione ($|r|$) tramite le seguenti due equazioni:


$$s = \frac{1 + |r|}{1 - |r|}$$


$$|r| = \frac{\sqrt{P_\text{r}}}{\sqrt{P_\text{d}}}$$


---

2. Derivazione

Per semplificare la frazione per $s$ e sostituire $|r|$, si moltiplica mentalmente ogni termine al numeratore e al denominatore direttamente per $\sqrt{P_\text{d}}$. In questo modo, il denominatore di $|r|$ si semplifica immediatamente:


1. Da $1$ si ottiene:
   $$1 \cdot \sqrt{P_\text{d}} = \sqrt{P_\text{d}}$$
2. Da $|r|$ si ottiene:
   $$\frac{\sqrt{P_\text{r}}}{\sqrt{P_\text{d}}} \cdot \sqrt{P_\text{d}} = \sqrt{P_\text{r}}$$

Sostituendo questi termini direttamente nell’equazione del ROS, si ottiene immediatamente:


$$s = \frac{\sqrt{P_\text{d}} + \sqrt{P_\text{r}}}{\sqrt{P_\text{d}} - \sqrt{P_\text{r}}}$$


---

3. Adattamento alla notazione utilizzata qui

Sostituendo i nomi delle variabili ($s \rightarrow \text{ROS}$ e $P_\text{d} \rightarrow P_\text{v}$ per la potenza incidente), si ottiene esattamente la formula finale:


$$\text{ROS} = \frac{\sqrt{P_\text{v}} + \sqrt{P_\text{r}}}{\sqrt{P_\text{v}} - \sqrt{P_\text{r}}}$$
</indepth>
