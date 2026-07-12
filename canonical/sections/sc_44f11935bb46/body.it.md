Poiché nessun circuito funziona in modo ideale, ai capi della resistenza di carico $R_L$ di un raddrizzatore non è presente una tensione continua perfettamente costante, ma una tensione pulsante. Essa deriva dalle semionde sinusoidali positive successive e dall'effetto di livellamento dei condensatori. Questa componente di tensione alternata residua è chiamata ondulazione residua.
La sua frequenza è $f=\qty{100}{\hertz}$, poiché anche la semionda negativa viene specchiata nella zona positiva, raddoppiando così la frequenza di rete di $\qty{50}{\hertz}$. Se si immettesse questa tensione continua pulsante attraverso un partitore di tensione in un amplificatore con altoparlante, si potrebbe sentire un ronzio di $\qty{100}{\hertz}$.

<webonly>
<margin>
[include:applet_brumm]
</margin>
</webonly>

[question:AD310]

Questa tensione può essere osservata con un oscilloscopio, oscilloscopando solo la componente di tensione alternata (vedi figura [ref:a_AC-Kopplung]: accoppiamento AC dell'ingresso).

<indepth>
[photo:306:a_AC-Kopplung:Accoppiamento AC - DC dell'ingresso dell'oscilloscopio]
Premendo il tasto "GD" l'ingresso dell'oscilloscopio viene impostato su zero volt.
Se il tasto AC/DC non è premuto, avviene un accoppiamento capacitivo dell'ingresso dell'oscilloscopio e viene visualizzata solo la componente di tensione alternata del segnale di ingresso.
Se il tasto AC/DC è premuto, avviene un accoppiamento galvanico dell'ingresso dell'oscilloscopio e viene visualizzata anche la componente di tensione continua di una tensione alternata.
</indepth>

Nella domanda seguente è necessario determinare sia la frequenza che l'ampiezza dell'ondulazione residua. 

[question:AD309]