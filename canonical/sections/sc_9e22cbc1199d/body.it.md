Nella classe E abbiamo già trattato la bobina. In corrente continua, una bobina in stato stazionario presenta una resistenza molto bassa. La bobina si comporta quindi come un semplice filo. In corrente alternata, invece, la bobina – analogamente a un condensatore – mostra una impedenza $X_{\textrm{L}}$, vale a dire che, nonostante il filo della bobina abbia solo una resistenza ohmica molto bassa (resistenza del conduttore), scorre una corrente che diminuisce all’aumentare della frequenza della tensione alternata:

$|X_{L}| = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$

Dalla formula si deduce che la impedenza aumenta con l’aumentare della frequenza e diminuisce con la sua riduzione. A differenza del condensatore, la impedenza di una bobina è positiva.

<indepth>
Perché la reattanza induttiva è positiva? La ragione risiede ancora una volta nel calcolo complesso della corrente alternata, che non è strettamente necessario per l’esame di radioamatore.

Per i lettori con conoscenze di numeri complessi, si segnala che la rappresentazione corretta della reattanza induttiva è in realtà

$X_L = j\omega L$

dove $j$ rappresenta l’unità immaginaria $\sqrt{-1}$.

Da ciò risulta evidente che la reattanza induttiva non è solo positiva, ma anche complessa. Il segno positivo descrive la relazione di fase tra corrente e tensione ai capi della bobina, che approfondiremo in questo capitolo.
</indepth>

[question:AC202]

[question:AC203]

---

Con un analizzatore di rete vettoriale (VNA) è possibile rappresentare la variazione della reattanza induttiva $X_L$ in funzione della frequenza (cfr. figura [ref:a_XL_Verlauf]).

<margin>
[photo:265:a_XL_Verlauf:Variazione della reattanza induttiva $X_L$ di una bobina da $\qty{500}{\kilo\hertz}$ a $\qty{10}{\mega\hertz}$]
</margin>

Prova ora a rispondere alla seguente domanda utilizzando la formula sopra. Presta particolare attenzione alle unità di misura e alle potenze di dieci per ottenere i risultati corretti.

[question:AC204]

---

Analogamente al condensatore, anche la bobina presenta uno sfasamento tra tensione e corrente pari a $\qty{+90}{\degree}$, con la corrente che ritarda rispetto alla tensione, come mostrato nella figura [ref:a_Blindleistung_Spule]. La linea rossa nella figura [ref:a_XL_Verlauf] mostra la fase della reattanza induttiva $X_L$ a circa $\qty{+90}{\degree}$.

<tip>
Aiuto mnemonico: Con l’induttanza, la corrente arriva in ritardo!
</tip>

[question:AC201]

Ne consegue una curva di potenza che oscilla simmetricamente intorno alla linea dello zero. Il valore medio di questa potenza è nullo, il che significa che – proprio come nel caso del condensatore – non viene assorbita potenza attiva. Al contrario, l’energia viene immagazzinata periodicamente nel campo magnetico della bobina e poi restituita alla sorgente.

Si parla quindi, per una bobina ideale senza perdite, di potenza reattiva e di reattanza.

<margin>
[picture:944:a_Blindleistung_Spule:Il prodotto di $U \cdot I$ genera la curva di potenza verde]
</margin>

Se una bobina si riscalda in applicazioni ad alta frequenza, ciò indica la presenza di perdite che causano questo riscaldamento. Le perdite sono dovute alla resistenza ohmica del filo e, inoltre, anche l’effetto pelle riduce la sezione apparente del filo. Anche in questo caso, come per il condensatore, si ricorre al fattore di qualità $Q$ o al fattore di perdita $\tan\delta$ per descrivere le perdite.

[question:AC209]

---

Ora abbiamo trattato la reattanza capacitiva $X_C$ del condensatore e la reattanza induttiva $X_L$ della bobina. Entrambe le grandezze dipendono dalla frequenza e, insieme alla resistenza attiva $R$, formano la cosiddetta *impedenza* $Z$ di un componente.

Le reattanze $X_L$ e $X_C$ agiscono in modo opposto e possono annullarsi a vicenda, parzialmente o completamente. Tuttavia, per combinare le reattanze con la resistenza attiva non è possibile una semplice addizione algebrica, ma è necessaria una addizione geometrica. Questa avviene tramite il teorema di Pitagora (cfr. figura [ref:a_impedanzdreieck]).

Il risultato è l’impedenza $Z$, che descrive la resistenza totale complessa di un componente. Il valore assoluto dell’impedenza $|Z|$ corrisponde alla cosiddetta impedenza apparente:

$Z = \sqrt{R^2 + (X_L - X_C)^2}$ 

o, in forma semplificata (cfr. raccolta di formule – voce: impedenza apparente):

$Z = \sqrt{R^2 + X^2}$ 

Nell’alta frequenza, l’impedenza riveste un ruolo centrale, poiché determina il comportamento dei componenti nei circuiti e risulta fondamentale per l’adattamento di linee, antenne e amplificatori. Viene espressa in ohm ($\unit{\ohm}$) e descrive la resistenza totale di un componente in regime di corrente alternata. In un circuito in serie di reattanza e resistenza attiva, si ottiene un’impedenza apparente $Z$ che si verifica solo in funzionamento con tensione alternata e non può essere misurata con un ohmetro.

<margin>
[picture:1067:a_impedanzdreieck:Impedenza $Z$ come addizione geometrica di $R$ e $X$]
</margin>

<indepth>
L’impedenza $Z$ è una grandezza complessa che tiene conto sia della resistenza attiva $R$ che delle reattanze $X_L$ e $X_C$ ($Z = R + j\cdot X$).
</indepth>

[question:AA101]

<tip>
Una resistenza attiva di $\qty{100}{\ohm}$ e una reattanza di $\qty{100}{\ohm}$ in serie danno un’impedenza apparente (impedenza) di $\qty{141}{\ohm}$.
Il risultato si ottiene tramite l’addizione geometrica delle due resistenze tramite un triangolo rettangolo secondo il teorema di Pitagora $a^2 + b^2 = c^2$.
Per le resistenze ciò significa: $R^2 + X_L^2 = Z^2$
$Z = \sqrt{(\qty{100}{\ohm})^2 + (\qty{100}{\ohm})^2} = \qty{141}{\ohm}$
</tip>

---

Abbiamo già trattato l’induttanza di una bobina nella classe E. In linea generale, l’induttanza aumenta se si aumenta il numero di spire, si riduce la lunghezza della bobina, si aumenta la sezione trasversale della bobina e si utilizza un materiale con maggiore permeabilità magnetica come nucleo della bobina. Per aumentare l’induttanza senza aumentare drasticamente il numero di spire, la bobina viene avvolta su un nucleo toroidale in ferrite. Le induttanze di blocco con alta induttanza vengono utilizzate per ridurre le correnti ad alta frequenza.

<indepth>
[photo:270:a_Pulvereisenringkern:Esempio di nucleo toroidale in polvere di ferro]
[photo:271:a_Ferritringkern:Esempio di nucleo toroidale in ferrite]
</indepth>

[question:AC211]

Per le bobine toroidali, per semplificare il calcolo dell’induttanza, viene indicato un valore $A_\text{L}$ del materiale del nucleo.
Il calcolo dell’induttanza è quindi: $L = N^2 \cdot A_\text{L}$ (cfr. raccolta di formule – voce: induttanza di una bobina toroidale). Prova ora a rispondere alle seguenti domande con questa formula.

<attention>
La denominazione del valore $A_\text{L}$ è indicata in nanohenry per spira al quadrato.
</attention>

[question:AC205]
[question:AC206]
[question:AC207]
[question:AC208]

<indepth>
Se all’interno della bobina è presente un materiale magneticamente conduttivo (ad esempio ferro, ferrite), il campo magnetico viene amplificato. La densità di flusso magnetico $B$ efficace può essere calcolata con la formula (cfr. raccolta di formule – voce: densità di flusso magnetico)
$B = \mu_0 \cdot \mu_r \cdot H$
dove $\mu_0$ corrisponde alla permeabilità del vuoto $\qty{1,2566e-6}{\volt\second\per\ampere\meter}$ e $\mu_r$ rappresenta la permeabilità relativa del materiale del nucleo nella bobina. Per l’aria viene utilizzato il fattore $1$ (cfr. raccolta di formule – voce: permeabilità del vuoto; permeabilità relativa).
</indepth>

Per schermare un campo magnetico è necessario un materiale con buona conducibilità magnetica, ad esempio lamierino. La figura [ref:a_abschirmbecher] mostra un esempio di bobine con copertura schermante. I coperchi metallici di schermatura contengono bobine con un nucleo regolabile in ferrite, che può essere avvitato o svitato tramite l’apertura superiore con un cacciavite. In questo modo si modifica l’induttanza della bobina.

[question:AC210]

<margin>
[photo:333:a_abschirmbecher:Esempio di bobine con copertura schermante per la schermatura di campi magnetici]
</margin>