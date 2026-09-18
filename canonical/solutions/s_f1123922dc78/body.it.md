Con un’antenna artificiale da $\qty{50}{\ohm}$, il ROS all’ingresso della linea è circa $\num{1}$. Sappiamo quindi innanzitutto che la linea di antenna stessa è in ordine.

Con l’antenna collegata, invece, si misura un ROS di $\num{3}$. Per il ROS vale la formula con la tensione dell’onda incidente $U_\mathrm{V}$ e quella dell’onda riflessa $U_\mathrm{R}$:


$s=\frac{U_\mathrm{V}+U_\mathrm{R}}{U_\mathrm{V}-U_\mathrm{R}}.$


Con $s=\num{3}$ ne consegue che la tensione dell’onda riflessa è la metà di quella dell’onda incidente:


$\frac{U_\mathrm{R}}{U_\mathrm{V}}=\frac{3-1}{3+1}=\num{0,5}.$


Poiché la potenza è proporzionale al quadrato della tensione, la potenza riflessa all’ingresso della linea è quindi


$\num{0,5}^2=\num{0,25}$

della potenza incidente. Dei $\qty{10}{\watt}$ immessi, quindi, all’ingresso della linea arrivano circa

$\qty{10}{\watt}\cdot\num{0,25}=\qty{2,5}{\watt}$

come potenza riflessa.

La linea presenta su ogni percorso un’attenuazione di $\qty{3}{\decibel}$. Dei $\qty{10}{\watt}$ immessi, quindi, all’antenna arrivano solo circa $\qty{5}{\watt}$. Sul percorso di ritorno, la potenza riflessa viene dimezzata.


Affinché all’ingresso della linea arrivino ancora $\qty{2,5}{\watt}$ di potenza riflessa, all’antenna devono essere stati riflessi circa $\qty{5}{\watt}$. Questo corrisponde praticamente a tutta la potenza ivi ricevuta.


L’antenna, quindi, non assorbe quasi nessuna potenza di HF ed è difettosa.