Nella sezione [sec:spule_1] abbiamo già trattato la bobina. In corrente continua, a regime, la bobina presenta una resistenza molto bassa. La bobina si comporta quindi come un pezzo di filo. Tuttavia, in corrente alternata, la bobina, simile a un condensatore, presenta un'impedenza $X_{\textrm{L}}$, cioè, nonostante il filo della bobina abbia solo una piccola resistenza ohmica (resistenza del conduttore), scorre una corrente che diminuisce all'aumentare della frequenza della tensione alternata:

$|X_{L}| = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$

Dalla formula si può vedere che l'impedenza aumenta con la frequenza crescente e diminuisce con la frequenza decrescente. A differenza del condensatore, l'impedenza di una bobina è positiva.

<indepth>
Perché la reattanza induttiva è positiva? Il motivo risiede nuovamente nel calcolo complesso della corrente alternata, che non è strettamente necessario per l'esame di radioamatore.

Per i lettori con conoscenze di numeri complessi, si noti tuttavia che la rappresentazione corretta della reattanza induttiva è in realtà

$X_L = j\omega L$

Dove $j$ rappresenta ancora l'unità immaginaria $\sqrt{-1}$.

Da ciò si evince che la reattanza induttiva non è solo positiva, ma anche complessa. Il segno positivo descrive la relazione di fase tra corrente e tensione sulla bobina, che esamineremo più in dettaglio in questo capitolo.
</indepth>

[question:AC202]

[question:AC203]

---

Con un analizzatore di rete vettoriale (VNA) è possibile rappresentare la variazione della reattanza induttiva $X_L$ in funzione della frequenza (cfr. figura [ref:a_XL_Verlauf]).

<margin>
[photo:265:a_XL_Verlauf:Variazione della reattanza induttiva $X_L$ di una bobina da $\qty{500}{\kilo\hertz}$ a $\qty{10}{\mega\hertz}$]
</margin>

Ora prova a rispondere alla seguente domanda utilizzando la formula sopra. Presta particolare attenzione alle unità o alle potenze di dieci per ottenere i risultati corretti.

[question:AC204]

---

Simile al condensatore, anche nella bobina si verifica uno sfasamento tra tensione e corrente. Questo è di $\qty{+90}{\degree}$, dove la corrente è in ritardo rispetto alla tensione, come mostrato nella figura [ref:a_Blindleistung_Spule]. La linea rossa nella figura [ref:a_XL_Verlauf] mostra la fase della reattanza induttiva $X_L$ a circa $\qty{+90}{\degree}$.

<tip>
Aiuto mnemonico: Con l'indutt*aaa*nza la corrente arriva t*aaa*rdi!
</tip>

[question:AC201]

Da ciò risulta una curva di potenza che oscilla simmetricamente attorno alla linea zero. Il valore medio di questa potenza è zero, cioè, proprio come nel condensatore, non viene assorbita potenza attiva. Invece, l'energia viene periodicamente immagazzinata nel campo magnetico della bobina e restituita alla sorgente.

Pertanto, per una bobina ideale senza perdite, si parla di potenza reattiva e di reattanza.

<margin>
[picture:944:a_Blindleistung_Spule:Il prodotto di $U \cdot I$ dà la curva di potenza verde]
</margin>

Se una bobina si riscalda in applicazioni ad alta frequenza, allora ha delle perdite che causano questo riscaldamento. Le perdite sono dovute alla resistenza ohmica del filo e inoltre agisce anche l'effetto pelle, che apparentemente riduce la sezione trasversale del filo. Anche qui, come nel condensatore, il fattore di qualità $Q$ o il fattore di perdita $\tan\delta$ vengono utilizzati per descrivere le perdite.

[question:AC209]

---

Ora abbiamo appreso la reattanza capacitiva $X_C$ del condensatore e la reattanza induttiva $X_L$ della bobina. Entrambe le grandezze dipendono dalla frequenza e insieme alla resistenza ohmica $R$ formano la cosiddetta *impedenza* $Z$ di un componente.

Le reattanze $X_L$ e $X_C$ agiscono in modo opposto e possono parzialmente o completamente annullarsi a vicenda. Tuttavia, per il calcolo delle reattanze con la resistenza ohmica non è possibile una semplice addizione algebrica, ma è necessaria un'addizione geometrica. Questa avviene utilizzando il teorema di Pitagora (cfr. figura [ref:a_impedanzdreieck]).

Il risultato è l'impedenza $Z$, che descrive la resistenza totale complessa di un componente. Il valore assoluto dell'impedenza $|Z|$ corrisponde alla cosiddetta impedenza:

$Z = \sqrt{R^2 + (X_L - X_C)^2}$

o semplificato (cfr. raccolta di formule – parola chiave: impedenza):

$Z = \sqrt{R^2 + X^2}$

Nella tecnologia ad alta frequenza, l'impedenza gioca un ruolo centrale, poiché determina il comportamento dei componenti nei circuiti ed è decisiva in particolare per l'adattamento di linee, antenne e amplificatori. Viene indicata in ohm ($\unit{\ohm}$) e descrive la resistenza totale di un componente in funzionamento a corrente alternata. In un collegamento in serie di reattanza e resistenza attiva si ottiene un'impedenza $Z$, che si manifesta solo in funzionamento a tensione alternata e non può essere misurata con un ohmmetro.

<margin>
[picture:1067:a_impedanzdreieck:Impedanza $Z$ come addizione geometrica di $R$ e $X$]
</margin>

<indepth>
L'impedenza $Z$ è una grandezza complessa che tiene conto sia della resistenza ohmica $R$ che delle reattanze $X_L$ e $X_C$ ($Z = R + j\cdot X$).
</indepth>

[question:AA101]

<tip>
Una resistenza attiva di $\qty{100}{\ohm}$ e una reattanza di $\qty{100}{\ohm}$ in serie danno un'impedenza di $\qty{141}{\ohm}$.
Il risultato si ottiene dall'addizione geometrica delle due resistenze tramite un triangolo rettangolo secondo il teorema di Pitagora $a^2 + b^2 = c^2$.
Per le resistenze significa: $R^2 + X_L^2 = Z^2$
$Z = \sqrt{(\qty{100}{\ohm})^2 + (\qty{100}{\ohm})^2} = \qty{141}{\ohm}$
</tip>

---

L'induttanza di una bobina l'abbiamo già appresa nella classe E. Fondamentalmente, l'induttanza aumenta se il numero di spire viene aumentato, la lunghezza della bobina viene ridotta, l'area della sezione trasversale della bobina viene ingrandita e viene utilizzato un materiale magneticamente più conduttivo come nucleo della bobina. Per aumentare l'induttanza senza aumentare drasticamente il numero di spire, l'avvolgimento viene realizzato su un nucleo toroidale in ferrite. Bobine di strozzamento con alta induttanza vengono utilizzate per la riduzione di correnti ad alta frequenza.

<indepth>
[photo:270:a_Pulvereisenringkern:Esempio di un nucleo toroidale in polvere di ferro]
[photo:271:a_Ferritringkern:Esempio di un nucleo in ferrite]
</indepth>

[question:AC211]

Per le bobine su nucleo toroidale, per facilitare il calcolo dell'induttanza, viene indicato un cosiddetto valore $A_\text{L}$ del materiale del nucleo.
Il calcolo dell'induttanza è quindi:
$L = N^2 \cdot A_\text{L}$ (vedi raccolta di formule - parola chiave: Induttanza di una bobina toroidale). Ora prova a rispondere alle seguenti domande con questo.

<attention>
La denominazione del valore $A_\text{L}$ è data in nanohenry per spire al quadrato.
</attention>

[question:AC205]
[question:AC206]
[question:AC207]
[question:AC208]

<indepth>
Se all'interno della bobina si trova un materiale magneticamente conduttivo (ad es. ferro, ferrite) allora il campo magnetico viene rafforzato. La densità di flusso magnetico effettiva $B$ può essere calcolata con la formula (vedi raccolta di formule - parola chiave: Densità di flusso magnetico)
$B = \mu_0 \cdot \mu_r \cdot H$
Dove $\mu_0$ corrisponde alla permeabilità del vuoto $\qty{1,2566e-6}{\volt\second\per\ampere\meter}$ e $\mu_r$ sta per la permeabilità relativa del materiale del nucleo nella bobina. Per l'aria viene utilizzato il fattore $1$ (vedi raccolta di formule - parola chiave: Permeabilità del vuoto; permeabilità relativa).
</indepth>

Per schermare un campo magnetico è necessario un materiale magneticamente ben conduttivo, ad esempio la latta. La figura [ref:a_abschirmbecher] mostra un esempio di bobine con schermatura a coppa. Le coppe di schermatura metalliche contengono bobine con un nucleo in ferrite regolabile, che viene avvitato o svitato dall'alto attraverso l'apertura con un cacciavite. In questo modo cambia l'induttanza della bobina.

[question:AC210]

<margin>
[photo:333:a_abschirmbecher:Esempio di bobine con schermatura a coppa per la schermatura di campi magnetici]
</margin>