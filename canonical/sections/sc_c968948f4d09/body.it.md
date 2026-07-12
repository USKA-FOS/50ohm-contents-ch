<margin>
[picture:978:a_swr:Onda stazionaria]
</margin>
In molti casi, il rapporto d’onda stazionaria può essere semplicemente indicato se l’impedenza di alimentazione di un'antenna è nota. Purché un'antenna (o un carico fittizio) non sia né induttiva né capacitiva, cioè rappresenti una pura resistenza attiva, il rapporto d’onda stazionaria risulta dal rapporto tra la resistenza di carico e l’impedenza caratteristica della linea, dove numeratore e denominatore devono essere scelti in modo che il ROS sia maggiore o uguale a uno.

Un'antenna con un'impedenza di alimentazione di $\qty{100}{\ohm}$ provoca un rapporto d’onda stazionaria di $\num{2}$ se alimentata con un cavo da $\qty{50}{\ohm}$, poiché l'impedenza di alimentazione è doppia. Un'antenna con un'impedenza di alimentazione di $\qty{10}{\ohm}$ avrebbe un rapporto d’onda stazionaria di $\num{5}$, poiché l'impedenza caratteristica della linea è cinque volte maggiore.

Per rispondere alla seguente domanda, dobbiamo anche ricordare che la resistenza di un dipolo ripiegato è di poco inferiore a $\qty{300}{\ohm}$.

[question:AG405]

Un effetto ingannevole è l'impatto dell'attenuazione della linea sul rapporto d’onda stazionaria. Più una linea presenta perdite, minore (quindi "migliore") può essere il rapporto d’onda stazionaria su tale linea. Ciò è dovuto al fatto che una linea con perdite riduce sia la potenza in avanti che la potenza riflessa. Anche se alla fine di una linea non è collegata alcuna antenna (circuito aperto o corto circuito), e lì viene riflesso il $\qty{100}{\percent}$ dell'energia, quindi il rapporto d’onda stazionaria *lì* è $\infty$, si può misurare un rapporto d’onda stazionaria significativamente migliore all'altra estremità. Ad esempio, se la metà della potenza viene persa in direzione avanti e un'altra metà viene persa in direzione indietro, l'energia si riduce a un quarto ($\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$). Di conseguenza, un misuratore di onde stazionarie sul lato trasmettitore del cavo indica un rapporto d’onda stazionaria di $\num{3}$, che corrisponde al $\qty{25}{\percent}$ di potenza riflessa, sebbene alla fine vengano riflessi il $\qty{100}{\percent}$ – tuttavia, solo il $\qty{25}{\percent}$ arriva al misuratore di onde stazionarie.
[question:AG402]
[question:AG403]

Con un'attenuazione della linea di $\qty{5}{\dB}$ e una riflessione completa alla fine del cavo, ad esempio a causa di un'antenna scollegata, misuriamo persino un ROS sorprendentemente buono, sebbene nessuna antenna sia collegata! Possiamo calcolarlo come segue:

$s = \frac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}}$

Ciò consente di calcolare la seguente domanda, a condizione che si tenga presente che l'onda riflessa misurata costituisce solo un decimo dell'energia dell'onda in avanti: $\qty{5}{\dB}$ di attenuazione in direzione avanti e $\qty{5}{\dB}$ di attenuazione in direzione indietro, corrispondenti a $\qty{10}{\dB}$ di attenuazione totale. In questo caso, $P_\mathrm{r}$ è quindi solo un decimo di $P_\mathrm{v}$.

[question:AG404]
