Nei dipoli a centro alimentato nello spazio libero, l'impedenza di alimentazione è di $\qty{73,1}{\ohm}$, quindi dell'ordine di $\qty{50}{\ohm}$ - ma non esattamente! Questo vale anche per un'altezza di montaggio pari o superiore a una lunghezza d'onda.

<margin>
[picture:788:e_fusspunktimpedanz_dipol:Impedenza di base di un dipolo in funzione dell'altezza di montaggio (Simulato con NECPP)]
</margin>

[question:EG207]

Con l'interazione con il terreno dovuta a una minore altezza di montaggio, l'impedenza di alimentazione di un dipolo a centro alimentato si muove nell'intervallo da $\qty{40}{\ohm}$ a $\qty{90}{\ohm}$, come mostrato nella figura [ref:e_fusspunktimpedanz_dipol]. 

[question:EG208]
[question:EG209]

Se si realizza un dipolo come dipolo ripiegato, la tensione applicata si raddoppia a causa delle sezioni dell'antenna collegate in serie ma parzialmente condotte in parallelo, e la corrente richiesta si dimezza. Ciò corrisponde a un quadruplicamento dell'impedenza di alimentazione. Pertanto, un dipolo ripiegato ha un'impedenza di base da $\qtyrange{240}{300}{\ohm}$.

[question:EG210]

---

In un'antenna Groundplane, invece, un'estremità del dipolo viene omessa e sostituita da una terra con la minor resistenza possibile. Qui si ottiene quindi una resistenza di alimentazione di $\frac{\qty{73,1}{\ohm}}{2} \approx \qty{37}{\ohm}$, che corrisponde alla metà della resistenza di alimentazione di un dipolo nello spazio libero. Nelle antenne Groundplane con radiali angolati verso il basso di $\qty{45}{\degree}$, si ottiene una resistenza di alimentazione di esattamente $\qty{50}{\ohm}$ a causa della radiazione aggiuntiva dei radiali, in modo che non sia necessario alcun ulteriore adattamento ai comuni cavi coassiali. Pertanto, l'impedenza di base di una Groundplane è compresa tra $\qtyrange{30}{50}{\ohm}$.

<indepth>
Con una messa a terra scadente o un'interazione con il terreno, una Groundplane può presentare una resistenza di alimentazione superiore a $\qty{37}{\ohm}$ anche con radiali disposti orizzontalmente (ad esempio, sulla Superficie terrestre). La resistenza aggiuntiva deriva quindi dalle perdite nel terreno.
</indepth>

[question:EG211]