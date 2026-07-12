Nella classe N abbiamo imparato: se un'antenna è perfettamente adattata alla linea di alimentazione (ad es. un cavo coassiale), il misuratore SWR indica il valore 1. Questo è il caso migliore possibile, poiché tutta la potenza di trasmissione viene assorbita dall'antenna e nessuna potenza viene riflessa al trasmettitore. Se, al contrario, non è collegata alcuna antenna o la linea di trasmissione è interrotta o in corto circuito, il valore SWR sale verso l'infinito ($\infty$). In questi casi, la potenza di trasmissione viene riflessa quasi completamente. Una tale riflessione completa può, nel peggiore dei casi, danneggiare lo stadio finale del trasmettitore. Nella classe E approfondiamo ora l'argomento e impariamo anche valori tra $\num{1}$ e $\infty$.

Il rapporto d’onda stazionaria (ROS), indicato con il simbolo di formula $s$, può essere calcolato dalla potenza in avanti $P_\text{V}$ e dalla potenza riflessa $P_\text{R}$. Troviamo la relazione corrispondente nella raccolta di formule:

$s = \frac{\sqrt{P_\text{V}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{V}}-\sqrt{P_\text{R}}}$

Se, ad esempio, il trasmettitore emette una potenza di $P_\text{V}=\qty{100}{\watt}$ e $P_\text{R}=\qty{25}{\watt}$ vengono riflessi dall'antenna verso il trasmettitore, si ottiene:

$s = \frac{\sqrt{100}+\sqrt{25}}{\sqrt{100}-\sqrt{25}} = \frac{10+5}{10-5} = \frac{15}{5} = 3$

Ciò significa che un ROS di $\num{3}$ corrisponde a una riflessione del $\frac{\qty{25}{\watt}}{\qty{100}{\watt}}=\qty{25}{\percent}$. Altre corrispondenze sono mostrate nella tabella [ref:e_swr_werte].

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
[table:e_swr_werte:Valori ROS in relazione alla potenza riflessa]
</margin>

---

<tip>
Per rispondere alle seguenti domande, è sufficiente sapere che un rapporto d’onda stazionaria di $\num{3}$ corrisponde a una riflessione del $\qty{25}{\percent}$ dell'energia, cioè l'onda riflessa trasporta un quarto dell'energia dell'onda in avanti. Di conseguenza, solo il $\qty{75}{\percent}$ dell'energia viene ceduto alla fine della linea, ad esempio a un'antenna o a una resistenza di perdita (quindi non riflesso). 
</tip>

[question:EG401]
[question:EG402]
[question:EG403]
