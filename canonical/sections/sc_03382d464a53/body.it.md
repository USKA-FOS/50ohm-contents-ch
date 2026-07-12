Una serie di due resistenze viene spesso utilizzata come partitore di tensione. Nella classe E, consideriamo prima il *partitore di tensione non caricato*, come si trova anche nei seguenti esercizi. In un partitore di tensione non caricato, le tensioni sono proporzionali alle resistenze. Ciò significa, ad esempio, che una tensione maggiore cade su una resistenza ad alta impedenza, mentre una tensione corrispondentemente minore può essere misurata su una resistenza a bassa impedenza.

<margin>
[picture:819:E 63. Spannungsteiler:Partitore di tensione]
</margin>

<indepth>
Un importante partitore di tensione si trova, ad esempio, alla base di un transistor in un circuito amplificatore. 
Per questo motivo si parla di partitore di tensione di base. Lo esamineremo più da vicino nel capitolo amplificatore.
</indepth>

Questa relazione può essere rappresentata in varie formule, che troviamo nella raccolta di formule:

$\frac{U_{1}}{U_{2}} = \frac{R_{1}}{R_{2}}$

o

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

% TODO implementiere Attention in CSS!
<danger>
Queste formule non valgono per un partitore di tensione caricato. Le domande al riguardo seguiranno nella classe A.
</danger>

Nelle seguenti domande, il termine partitore di tensione non viene menzionato direttamente, ma dalla scelta delle parole: "Come si divide la tensione su due resistenze collegate in serie..." si dovrebbe riconoscere che si tratta di un partitore di tensione.

[question:ED101]

Non sono specificati valori di resistenza concreti, pertanto il risultato deve essere presentato come una formula generale. 
Secondo la domanda, R1 è 5 volte più grande di R2, quindi deve essere possibile misurare una tensione 5 volte maggiore su di esso, ovvero R1 = 5 * R2

Questa relazione può essere espressa come una formula.

$\frac{U_{1}}{U_{2}} = \frac{5 \cdot R_2}{R_2}$

Gli R2 si semplificano e si ottiene:

$\frac{U_{1}}{U_{2}} = \frac{5}{1}$

Dopo un po' di riorganizzazione otteniamo il risultato:

$U_{1} = U_{2} \cdot \frac{5}{1}$

$U_{1} = 5 \cdot U_{2}$

[question:ED102]

In questa domanda vale la relazione inversa rispetto alla domanda ED 101. Secondo la domanda, R1 è 6 volte più piccolo di R2, quindi deve essere possibile misurare una tensione 6 volte più piccola su di esso. 

Questa relazione espressa in una formula ora è:

$\frac{U_{1}}{U_{2}} = \frac{1}{6}$
  
$U_{1} = U_{2} \cdot {\frac{1}{6}}$
  
$U_1 = \frac{U_2}{6}$

[question:ED103]

In questa domanda sono specificati valori di resistenza concreti che servono a determinare il rapporto del partitore di tensione. R1 sta a R2 come 10 kOhm sta a 20 kOhm, quindi 1 a 2. Pertanto, U2 deve essere il doppio di U1. Tuttavia, viene fornita la tensione totale Ug. Questa viene suddivisa su una resistenza totale di 30 kOhm e quindi suddivisa nel rapporto 30 a 20 (o 3 a 2) rispetto a R2. Pertanto, su R2 deve essere possibile misurare una tensione pari a 2/3 di Ug.

Naturalmente, questo risultato può anche essere calcolato con la formula della raccolta di formule:

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

e quindi riorganizzata per U2:

$U_{2} = \frac{R_{2}}{R_{1} + R_{2}} \cdot U_g$
