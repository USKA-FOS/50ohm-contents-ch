Nella modulazione di fase, la fase di un'onda portante viene modificata in dipendenza dal segnale di modulazione. Ciò significa che lo sfasamento dell'onda portante varia direttamente in proporzione all'ampiezza del segnale di modulazione. Questa variazione di fase viene mantenuta nel corso del segnale e varia rispetto all'onda portante originale secondo uno schema specifico. Il risultato è un segnale sinusoidale la cui "posizione" (fase) si adatta continuamente, senza che l'ampiezza del segnale cambi.

La modulazione di fase può essere immaginata visivamente come lo spostamento della curva sinusoidale lungo l'asse temporale, dove ogni variazione di fase è controllata dal segnale di modulazione. Maggiore è l'ampiezza del segnale di modulazione, maggiore sarà lo spostamento della fase del segnale portante.

La modulazione di fase e la modulazione di frequenza appartengono entrambe al gruppo delle tecniche di modulazione angolare, poiché entrambe influenzano l'angolo dell'onda portante. La differenza sta nel fatto che nella modulazione di frequenza viene influenzata direttamente la frequenza e nella modulazione di fase la fase.

Ciò è particolarmente evidente con un segnale a onda quadra come segnale utile: nella modulazione di fase, ogni fronte del segnale a onda quadra provoca un salto di fase istantaneo del segnale portante, mentre nella modulazione di frequenza il fronte del segnale innesca solo un cambio di frequenza – la conseguente variazione di fase si accumula solo indirettamente nel tempo.

<margin>
[picture:907:a_phasenmodulation:Modulazione di fase con inversione di fase]
</margin>

<webonly>
<margin>
[include:applet_pm]
</margin>
</webonly>

<indepth>
Per gli interessati alla matematica: nella modulazione di fase, il segnale utile $m(t)$ ha un'influenza diretta sulla fase, ad esempio:

$\varphi(t) = m(t)$

Il segnale portante viene generato come un'oscillazione sinusoidale della forma

$s(t) = A_c \cos(2\pi f_c t + \varphi(t))$

dove $A_c$ è l'ampiezza, $f_c$ la frequenza portante e $\varphi(t)$ la fase modulata.

I due tipi di modulazione FM e PM sono strettamente correlati: la modulazione di fase di un segnale porta indirettamente a una variazione della frequenza e viceversa, la modulazione di frequenza crea una variazione di fase. Matematicamente, la relazione tra frequenza e fase può essere espressa dalla seguente relazione:

$f_i(t) = \frac{1}{2\pi} \cdot \frac{d\varphi(t)}{dt}$

Ciò significa che la frequenza è la derivata temporale della fase.

È quindi possibile realizzare la modulazione di frequenza tramite modulazione di fase integrando il segnale utile $m(t)$:

$\varphi(t) = 2\pi \int m(t) \, dt$

Il risultato viene quindi inserito nella funzione portante come $\varphi(t)$.
</indepth>

[question:AE313]