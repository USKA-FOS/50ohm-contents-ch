Un dipolo a semionda alimentato al centro e in risonanza, nello spazio libero, ha idealmente un'impedenza di alimentazione di circa $\qty{73,1}{\ohm}$, quindi approssimativamente $\qty{75}{\ohm}$. Questo valore è già dell'ordine di grandezza dei $\qty{50}{\ohm}$ desiderati, ma non corrisponde esattamente. Se un tale dipolo viene utilizzato direttamente con una linea di alimentazione da $\qty{50}{\ohm}$, si verifica quindi un leggero disadattamento. Per una trasmissione ottimale della potenza o per ottenere un ROS il più basso possibile, anche in un dipolo può essere utile un adattamento. Questo vale in generale anche per altezze di installazione di circa una lunghezza d'onda o più, dove l'impedenza di alimentazione effettiva può variare leggermente a seconda dello spessore del filo, dell'ambiente e dell'altezza di installazione, come vedremo subito.

<margin>
[picture:788:e_fusspunktimpedanz_dipol:Impedenza di piede di un dipolo in funzione dell'altezza di installazione (simulato con NECPP)]
</margin>

[question:EG207]

A causa dell'interazione con il suolo a causa di un'altezza di installazione ridotta, l'impedenza di alimentazione di un dipolo alimentato al centro varia tra $\qty{40}{\ohm}$ e $\qty{90}{\ohm}$, come mostrato nel grafico [ref:e_fusspunktimpedanz_dipol].


[question:EG208]
[question:EG209]


Se si realizza un dipolo come dipolo ripiegato, la tensione applicata si raddoppia a causa dei tratti di antenna collegati in serie ma parzialmente in parallelo, mentre la corrente necessaria si dimezza. Questo corrisponde a una quadruplicazione dell'impedenza di alimentazione. Pertanto, un dipolo ripiegato ha un'impedenza di piede di $\qtyrange{240}{300}{\ohm}$.


[question:EG210]

---

Nel caso di un'antenna Groundplane, invece, un'asta del dipolo viene omessa e sostituita da una terra con la resistenza più bassa possibile. Qui si ottiene quindi un'impedenza di alimentazione di $\frac{\qty{73,1}{\ohm}}{2} \approx \qty{37}{\ohm}$, che corrisponde alla metà dell'impedenza di alimentazione di un dipolo nello spazio libero. Con antenne Groundplane con radiali piegati di $\qty{45}{\degree}$ verso il basso, grazie alla radiazione aggiuntiva dei radiali, si ottiene un'impedenza di alimentazione esattamente di $\qty{50}{\ohm}$, per cui non è necessario alcun ulteriore adattamento ai comuni cavi coassiali. Pertanto, l'impedenza di piede di una Groundplane è compresa tra $\qtyrange{30}{50}{\ohm}$.


<indepth>
In caso di messa a terra scadente o di interazione con il suolo, per un'antenna Groundplane può risultare anche un'impedenza di alimentazione superiore a $\qty{37}{\ohm}$ con radiali posizionati orizzontalmente (ad esempio sulla superficie terrestre). La resistenza aggiuntiva deriva quindi dalle perdite del suolo.
</indepth>

[question:EG211]