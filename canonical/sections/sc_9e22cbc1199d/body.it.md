Nella classe E abbiamo già trattato anche la bobina. Con corrente continua, la bobina ha una resistenza molto bassa nello stato stazionario. La bobina si comporta quindi come un pezzo di filo. Con corrente alternata, tuttavia, la bobina mostra, simile a un condensatore, una resistenza alla corrente alternata $X_{\textrm{L}}$, il che significa che, sebbene il filo della bobina abbia solo una resistenza ohmica molto bassa (resistenza del conduttore), scorre una corrente che tuttavia diminuisce con l'aumentare della frequenza della tensione alternata:

$|X_{L}| = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$

Dalla formula si può vedere che la resistenza alla corrente alternata aumenta con l'aumentare della frequenza e diminuisce con la diminuzione della frequenza. A differenza del condensatore, la resistenza alla corrente alternata di una bobina è positiva.

<indepth>
Perché la reattanza induttiva è positiva? Lo sfondo risiede nuovamente nel calcolo complesso della corrente alternata, che non è strettamente necessario per l'esame di radioamatore.

Per i lettori con conoscenze di numeri complessi, si noti tuttavia che la rappresentazione corretta della reattanza induttiva è in realtà

$X_L = j\omega L$

Dove $j$ sta nuovamente per l'unità immaginaria $\sqrt{-1}$.

Da ciò si evince che la reattanza induttiva non è solo positiva, ma anche complessa. Il segno positivo descrive la relazione di fase tra corrente e tensione sulla bobina, che esamineremo più in dettaglio in questo capitolo.
</indepth>

[question:AC201]

[question:AC203]

---

Con un analizzatore di rete vettoriale (VNA) è possibile rappresentare la variazione della reattanza induttiva $X_L$ in funzione della frequenza (cfr. figura [ref:a_XL_Verlauf]).

<margin>
[photo:265:a_XL_Verlauf:Variazione della reattanza induttiva $X_L$ di una bobina da $\qty{500}{\kilo\hertz}$ a $\qty{10}{\mega\hertz}$]
</margin>

Prova ora a rispondere alle seguenti domande utilizzando la formula sopra. Presta particolare attenzione alle unità e alle potenze di dieci, in modo da ottenere i risultati corretti.

[question:AC204]

---

Similmente al condensatore, anche nella bobina si verifica uno sfasamento tra tensione e corrente. Questo è di $\qty{+90}{\degree}$, con la corrente in ritardo rispetto alla tensione, come mostrato nella figura [ref:a_Blindleistung_Spule]. La linea rossa nella figura [ref:a_XL_Verlauf] mostra la relazione di fase della reattanza induttiva $X_L$ a circa $\qty{+90}{\degree}$.

<tip>
Aiuto mnemonico: Nell'induttanza la corrente arriva troppo tardi!
</tip>

[question:AC202]

Da ciò deriva una curva di potenza che oscilla simmetricamente attorno alla linea dello zero. Il valore medio di questa potenza è zero, il che significa che - proprio come con il condensatore - non viene assorbita potenza attiva. Invece, l'energia viene immagazzinata periodicamente nel campo magnetico della bobina e restituita alla sorgente.

Si parla quindi di potenza reattiva e reattanza per una bobina idealmente priva di perdite.

<margin>
[picture:944:a_Blindleistung_Spule:Il prodotto di $U \cdot I$ dà la curva di potenza verde]
</margin>

Se una bobina si riscalda nelle applicazioni ad alta frequenza, allora ha delle perdite che causano questo riscaldamento. Le perdite derivano dalla resistenza ohmica del filo e inoltre agisce anche l'effetto pelle, che riduce apparentemente la sezione del filo. Anche qui, come per il condensatore, il fattore di qualità $Q$ o il fattore di perdita $\tan\delta$ vengono utilizzati per descrivere le perdite.

[question:AC209]

---

Ora abbiamo conosciuto la reattanza capacitiva $X_C$ del condensatore e la reattanza induttiva $X_L$ della bobina. Entrambe le grandezze dipendono dalla frequenza e, insieme alla resistenza ohmica $R$, costituiscono la cosiddetta *impedenza* $Z$ di un componente.

Le reattanze $X_L$ e $X_C$ agiscono in modo opposto e possono annullarsi parzialmente o completamente a vicenda. Tuttavia, per il calcolo delle reattanze con la resistenza ohmica non è possibile una semplice addizione algebrica, ma è necessaria un'addizione geometrica. Questa avviene tramite il teorema di Pitagora (cfr. figura [ref:a_impedanzdreieck]).

Il risultato è l'impedenza $Z$, che descrive la resistenza totale complessa di un componente. Il modulo dell'impedenza $|Z|$ corrisponde alla cosiddetta impedenza caratteristica:

$Z = \sqrt{R^2 + (X_L - X_C)^2}$ 

o semplificato (cfr. raccolta di formule – parola chiave: impedenza caratteristica):

$Z = \sqrt{R^2 + X^2}$ 

Nella tecnica ad alta frequenza, l'impedenza gioca un ruolo centrale, poiché determina il comportamento dei componenti nei circuiti ed è particolarmente cruciale per l'adattamento di linee, antenne e amplificatori. Viene indicata in Ohm ($\unit{\ohm}$) e descrive la resistenza totale di un componente in funzionamento a corrente alternata. In una connessione in serie di reattanza e resistenza attiva si ottiene un'impedenza caratteristica $Z$, che si verifica solo durante il funzionamento a tensione alternata e non può essere misurata con un ohmmetro.

<margin>
[picture:1067:a_impedanzdreieck:Impedenza $Z$ come addizione geometrica di $R$ e $X$]
</margin>

<indepth>
L'impedenza $Z$ è una grandezza complessa che tiene conto sia della resistenza ohmica $R$ che delle reattanze $X_L$ e $X_C$ ($Z = R + j\cdot X$).
</indepth>

[question:AA101]

<tip>
Resistenza attiva $\qty{100}{\ohm}$ e reattanza $\qty{100}{\ohm}$ in serie danno un'impedenza caratteristica (impedenza) di $\qty{141}{\ohm}$.
Il risultato deriva dall'addizione geometrica delle due resistenze tramite un triangolo rettangolo secondo il teorema di Pitagora $a^2 + b^2 = c^2$.
Per le resistenze ciò significa: $R^2 + X_L^2 = Z^2$
$Z = \sqrt{(\qty{100}{\ohm})^2 + (\qty{100}{\ohm})^2} = \qty{141}{\ohm}$
</tip>

---

Abbiamo già conosciuto l'induttanza di una bobina nella classe E. Fondamentalmente, l'induttanza aumenta all'aumentare del numero di spire, al diminuire della lunghezza della bobina, all'aumentare dell'area della sezione trasversale della bobina e all'utilizzo di un materiale più conduttivo magneticamente come nucleo della bobina. Per aumentare l'induttanza senza aumentare drasticamente il numero di spire, l'avvolgimento viene avvolto su un nucleo ad anello di ferrite. Le bobine di reattanza con alta induttanza vengono utilizzate per ridurre le correnti ad alta frequenza.

<indepth>
[photo:270:a_Pulvereisenringkern:Esempio di nucleo ad anello di ferro in polvere]
[photo:271:a_Ferritringkern:Esempio di nucleo di ferrite]
</indepth>

[question:AC211]

Nelle bobine toroidali, per facilitare il calcolo dell'induttanza, viene fornito un cosiddetto valore $A_\text{L}$ del materiale del nucleo.
Il calcolo dell'induttanza è quindi:
$L = N^2 \cdot A_\text{L}$ (vedi raccolta di formule - parola chiave: Induttanza di una bobina toroidale). Prova ora a rispondere alle seguenti domande con questo.

<attention>
La denominazione del valore $A_\text{L}$ è indicata in nanohenry per spire al quadrato.
</attention>


[question:AC205]
[question:AC206]
[question:AC207]
[question:AC208]

<indepth>
Se all'interno della bobina è presente un materiale conduttivo magneticamente (ad es. ferro, ferrite), il campo magnetico viene rinforzato. La densità di flusso magnetico $B$ effettiva può essere calcolata con la formula (vedi raccolta di formule - parola chiave: Densità di flusso magnetico)
$B = \mu_0 \cdot \mu_r \cdot H$
Dove $\mu_0$ corrisponde alla costante del campo magnetico $\qty{1,2566e-6}{\volt\second\per\ampere\meter}$ e $\mu_r$ sta per la permeabilità relativa del materiale del nucleo nella bobina. Per l'aria viene utilizzato il fattore $1$ (vedi raccolta di formule - parola chiave: Costante del campo magnetico; permeabilità relativa).
</indepth>

Per schermare un campo magnetico è necessario un materiale magneticamente ben conduttivo, ad esempio banda stagnata. La figura [ref:a_abschirmbecher] mostra un esempio di bobine con schermo. Gli schermi metallici contengono bobine con un nucleo di ferrite regolabile, che viene avvitato dentro o fuori dall'alto con un cacciavite. Ciò modifica l'induttanza della bobina.

[question:AC210]

<margin>
[photo:333:a_abschirmbecher:Esempio di bobine con schermo per la schermatura di campi magnetici]
</margin>