Nella modulazione di fase, la fase di un’onda portante viene modificata in funzione del segnale modulante. Ciò significa che lo sfasamento dell’onda portante varia in modo direttamente proporzionale all’ampiezza del segnale modulante. Questa variazione della fase permane lungo il segnale e si modifica rispetto all’onda portante originale secondo uno schema ben definito. Il risultato è un segnale sinusoidale il cui "spostamento" (fase) si adatta continuamente senza che l’ampiezza del segnale subisca variazioni.

La modulazione di fase può essere visualizzata come lo spostamento della sinusoide lungo l’asse temporale: ogni variazione della fase è controllata dal segnale modulante. Maggiore è l’ampiezza del segnale modulante, maggiore sarà lo spostamento di fase del segnale portante.

La modulazione di fase e quella di frequenza appartengono entrambe alla categoria delle tecniche di modulazione angolare, poiché entrambe influenzano l’angolo dell’onda portante. La differenza risiede nel fatto che nella modulazione di frequenza è la frequenza a essere influenzata direttamente, mentre nella modulazione di fase è la fase stessa a esserlo.

Questo aspetto emerge in modo particolare quando il segnale utile è un’onda quadra: nella modulazione di fase, ogni fronte dell’onda quadra provoca un immediato salto di fase del segnale portante, mentre nella modulazione di frequenza il fronte del segnale induce semplicemente un cambiamento di frequenza; la conseguente variazione di fase si accumula solo in modo indiretto e continuo nel tempo.

<margin>
[picture:907:a_phasenmodulation:Modulazione di fase con inversione di fase]
</margin>

<webonly>
<margin>
[include:applet_pm]
</margin>
</webonly>

<indepth>
Per gli interessati alla matematica: nel caso della modulazione di fase, il segnale utile $m(t)$ influisce direttamente sulla fase, ad esempio:

$\varphi(t) = m(t)$

Il segnale portante viene generato come oscillazione sinusoidale della forma

$s(t) = A_c \cos(2\pi f_c t + \varphi(t))$

dove $A_c$ è l’ampiezza, $f_c$ la frequenza portante e $\varphi(t)$ la fase modulata.

Le due tecniche di modulazione FM e PM sono strettamente correlate: la modulazione di fase di un segnale comporta indirettamente una variazione della frequenza, e viceversa la modulazione di frequenza genera una variazione della fase. Dal punto di vista matematico, il legame tra frequenza e fase può essere espresso dalla seguente relazione:

$f_i(t) = \frac{1}{2\pi} \cdot \frac{d\varphi(t)}{dt}$

Questo significa che la frequenza è la derivata temporale della fase.

Pertanto, è possibile realizzare la modulazione di frequenza tramite la modulazione di fase integrando il segnale utile $m(t)$:

$\varphi(t) = 2\pi \int m(t) \, dt$

Il risultato viene poi inserito come $\varphi(t)$ nella funzione portante.
</indepth>

[question:AE313]