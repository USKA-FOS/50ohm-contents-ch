Nelle classi N ed E abbiamo imparato a conoscere il ROS e le relative formule per la potenza incidente e quella riflessa. In molti casi è possibile indicare semplicemente il rapporto d’onda stazionaria se si conosce la resistenza di carico di un’antenna. A patto che un’antenna (o un carico fittizio) non abbia un comportamento né induttivo né capacitivo, cioè rappresenti una pura resistenza attiva ($R_a$), il rapporto d’onda stazionaria si ricava dal rapporto tra la resistenza di carico e l’impedenza caratteristica della linea, scegliendo numeratore e denominatore in modo che il ROS risulti maggiore o uguale a uno.

La figura [ref:a_swr] mostra la distribuzione della tensione di un’onda stazionaria su una linea. In alcuni punti la tensione raggiunge un massimo $U_\mathrm{max}$, in altri un minimo $U_\mathrm{min}$. La distanza tra due massimi di tensione adiacenti o due minimi di tensione adiacenti è pari a $\frac{\lambda}{2}$. Dal rapporto tra la tensione massima e minima si può determinare anche il rapporto d’onda stazionaria:

In termini matematici, ciò significa:

$s = \frac{U_\mathrm{max}}{U_\mathrm{min}} = \begin{cases} \dfrac{R_a}{Z}, & \text{per } R_a > Z, \\[6pt] 1, & \text{per } R_a = Z, \\[6pt] \dfrac{Z}{R_a}, & \text{per } R_a < Z. \end{cases}$

<margin>
[picture:978:a_swr:Onda stazionaria]
</margin>

Un’antenna con una resistenza di carico di $\qty{100}{\ohm}$ provoca, se alimentata con un cavo da $\qty{50}{\ohm}$, un rapporto d’onda stazionaria di $\num{2}$, poiché la resistenza di carico è doppia. Un’antenna con una resistenza di carico di $\qty{10}{\ohm}$ avrebbe un rapporto d’onda stazionaria di $\num{5}$, poiché l’impedenza caratteristica della linea è cinque volte maggiore.

Per rispondere alle seguenti domande dobbiamo ricordare che la resistenza di un dipolo a semionda piegato è di circa $\qtyrange{240}{300}{\ohm}$.

[question:AG405]
[question:AI403]

Un effetto ingannevole è l’impatto dell’attenuazione della linea sul rapporto d’onda stazionaria. Maggiore è la perdita di una linea, minore (quindi "migliore") può risultare il rapporto d’onda stazionaria su quella linea. Questo accade perché una linea con perdite riduce sia la potenza incidente che quella riflessa. Anche se alla fine di una linea non è collegata alcuna antenna (a circuito aperto o in corto circuito) e lì il $\qty{100}{\percent}$ dell’energia viene riflesso, quindi il rapporto d’onda stazionaria è $\infty$, alla sua estremità opposta si può misurare un rapporto d’onda stazionaria notevolmente migliore. Se, ad esempio, nella direzione di andata si perde metà della potenza e nella direzione di ritorno si perde nuovamente metà, l’energia si riduce a un quarto ($\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$). Di conseguenza, un misuratore di ROS sul lato trasmettitore del cavo indica un rapporto d’onda stazionaria di $\num{3}$, che corrisponde al $\qty{25}{\percent}$ di potenza riflessa, anche se alla fine viene riflesso il $\qty{100}{\percent}$ — solo il $\qty{25}{\percent}$ arrivano effettivamente al misuratore di ROS.

[question:AG402]
[question:AG403]

Con un’attenuazione della linea di $\qty{5}{\dB}$ e una riflessione totale alla fine del cavo, ad esempio a causa di un’antenna scollegata, misuriamo addirittura un ROS sorprendentemente buono, anche se non è collegata alcuna antenna! Possiamo calcolarlo come segue:

$s = \frac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}}$

Quindi possiamo calcolare la domanda seguente, tenendo conto che l’onda riflessa misurata rappresenta solo un decimo dell’energia dell’onda incidente: $\qty{5}{\dB}$ di attenuazione in direzione di andata e $\qty{5}{\dB}$ in direzione di ritorno, per un’attenuazione totale di $\qty{10}{\dB}$. In questo caso, $P_\mathrm{r}$ è solo un decimo di $P_\mathrm{v}$.