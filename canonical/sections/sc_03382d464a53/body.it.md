Un circuito in serie composto da due resistenze viene spesso utilizzato come partitore di tensione. Inizialmente consideriamo il *partitore di tensione non caricato*, come compare anche nei seguenti esercizi. In un partitore di tensione non caricato, le tensioni sono proporzionali alle resistenze. Ciò significa, ad esempio, che su una resistenza di valore elevato cade una tensione maggiore, mentre su una resistenza di valore basso si misura una tensione corrispondentemente minore.

<margin>
[picture:819:E 63. Partitore di tensione:Partitore di tensione]
</margin>

<indepth>
Un importante partitore di tensione si trova, ad esempio, alla base di un transistor in un circuito amplificatore. 
Per questo motivo si parla di partitore di tensione di base. Lo approfondiremo nel capitolo sugli amplificatori.
</indepth>

Questa relazione può essere rappresentata con diverse formule, che troviamo nella raccolta di formule:

$\frac{U_{1}}{U_{2}} = \frac{R_{1}}{R_{2}}$

oppure

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

% TODO implementiere Attention in CSS!
<danger>
In un partitore di tensione caricato queste formule non valgono. A questo riguardo seguiranno domande nel capitolo [sec:spannungsteiler_2].
</danger>

Nelle seguenti domande il termine "partitore di tensione" non viene menzionato direttamente, ma dalla formulazione: "Come si divide la tensione ai due resistori collegati in serie ..." si dovrebbe riconoscere che si tratta di un partitore di tensione.

[question:ED101]

Non sono indicati valori concreti delle resistenze, quindi il risultato deve essere presentato come formula generale. 
Secondo il testo della domanda, $R_1$ è 5 volte maggiore di $R_2$, quindi su di esso si può misurare una tensione 5 volte maggiore, ovvero $R_1 = 5 \cdot R_2$

Questa relazione può essere espressa come formula.

$\frac{U_{1}}{U_{2}} = \frac{5 \cdot R_2}{R_2}$

Le $R_2$ si semplificano e si ottiene:

$\frac{U_{1}}{U_{2}} = \frac{5}{1}$

Dopo alcune trasformazioni otteniamo il risultato:

$U_{1} = U_{2} \cdot \frac{5}{1}$

$U_{1} = 5 \cdot U_{2}$

[question:ED102]

In questa domanda la relazione è inversa rispetto alla domanda ED 101. Secondo il testo della domanda, $R_1$ è 6 volte minore di $R_2$, quindi su di esso si misurerà una tensione 6 volte minore.

Questa relazione, espressa in una formula, è ora:

$\frac{U_{1}}{U_{2}} = \frac{1}{6}$
  
$U_{1} = U_{2} \cdot {\frac{1}{6}}$
  
$U_1 = \frac{U_2}{6}$

[question:ED103]

In questa domanda sono indicati valori concreti delle resistenze, che servono per determinare il rapporto del partitore di tensione. $R_1$ è in rapporto a $R_2$ come $\qty{10}{\kilo\ohm}$ a $\qty{20}{\kilo\ohm}$, quindi 1 a 2. $U_2$ deve quindi essere il doppio di $U_1$. Tuttavia, è indicata la tensione totale $U_g$. Questa è applicata a una resistenza totale di $\qty{30}{\kilo\ohm}$ e viene quindi suddivisa nel rapporto 30 a 20 (o 3 a 2) rispetto a $R_2$. Su $R_2$ si deve quindi poter misurare una tensione pari a 2/3 di $U_g$.

Naturalmente questo risultato può essere calcolato anche con la formula della raccolta di formule:

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

e poi risolta per $U_2$:

$U_{2} = \frac{R_{2}}{R_{1} + R_{2}} \cdot U_g$