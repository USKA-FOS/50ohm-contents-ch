Nelle trasmissioni digitali, le informazioni vengono trasmesse sotto forma di simboli. Un simbolo è uno stato di segnale distinguibile che viene trasmesso per un certo periodo di tempo. Questi stati di segnale possono differire, ad esempio, per ampiezza, frequenza o fase, oppure per combinazioni di queste proprietà. Nei paragrafi successivi vedremo come vengono generati tali simboli. A seconda del numero di simboli diversi che un metodo di trasmissione può utilizzare, un singolo simbolo può contenere uno o più bit di informazione.

Se sono disponibili solo due simboli diversi, con ogni simbolo può essere trasmesso esattamente un bit. Con quattro simboli possibili, possono già essere trasmessi due bit con un singolo simbolo, poiché due bit permettono di rappresentare quattro combinazioni diverse. Allo stesso modo, otto simboli diversi possono trasmettere tre bit e 16 simboli diversi possono trasmettere quattro bit contemporaneamente.

In generale, il numero $N$ di bit che possono essere trasmessi con un simbolo è dato dal numero $M=2^N$ di simboli possibili:

$N = \log_2(M)$

La *velocità di simbolo* indica quanti simboli vengono trasmessi al secondo. La sua unità di misura è il *baud*. Una velocità di simbolo di $\qty{1000}{\baud}$ significa quindi che vengono trasmessi $\num{1000}$ simboli al secondo.

La velocità di simbolo non è necessariamente identica alla velocità di trasmissione dei dati. Se con ogni simbolo vengono trasmessi più bit, la velocità di trasmissione dei dati risulta maggiore. Per la velocità di trasmissione dei dati $R_\mathrm{D}$ (con unità di misura $\unit{\bit\per\second}$) e la velocità di simbolo $R_\mathrm{S}$ vale:

$R_\mathrm{D} = R_\mathrm{S} \cdot N$

Ad esempio, se con una velocità di simbolo di $\qty{1200}{\baud}$ vengono trasmessi due bit per simbolo, la velocità di trasmissione dei dati risulta:

$R_\mathrm{D} = \qty{1200}{\baud} \cdot \qty{2}{\bit\per{Symbol}} = \qty{2400}{\bit\per\second}$

Il numero di simboli possibili e la velocità di simbolo sono quindi grandezze importanti per i metodi di trasmissione digitale. Nei paragrafi successivi vedremo come i singoli simboli possano essere rappresentati da diverse proprietà di un segnale.

[question:AA104]

---

Un esempio semplice di come diversi simboli possano essere rappresentati da diversi stati di segnale è la *modulazione a spostamento di frequenza* (*Frequency-Shift Keying*, FSK), già nota dalla classe E.

Nella FSK la frequenza del segnale trasmesso viene commutata tra diversi valori. La figura [ref:a_fsk] mostra una FSK binaria con due frequenze simboliche possibili nella rappresentazione temporale. Ad esempio, la frequenza più alta può rappresentare il simbolo $1$ e quella più bassa il simbolo $0$. Poiché sono disponibili due simboli diversi, con ogni simbolo può essere trasmesso un bit.

<margin>
[picture:703:a_fsk:FSK (Frequency-Shift Keying)]
</margin>

Un esempio è *RTTY*. In questo caso si commuta tra due frequenze simboliche, ad esempio tra $\qty{14072,43}{\kilo\hertz}$ e $\qty{14072,60}{\kilo\hertz}$. Con ogni simbolo può quindi essere trasmesso un bit, cioè $0$ o $1$.

[question:AE405]

La FSK non si limita però a due frequenze simboliche. Se ad esempio vengono utilizzate quattro frequenze diverse, sono disponibili quattro simboli diversi. A ogni simbolo può essere assegnata una delle quattro combinazioni di bit possibili: $00$, $01$, $10$ o $11$. In questo modo, con ogni simbolo possono essere trasmessi due bit.

Un esempio di questo metodo di trasmissione è *FT4*. In questo caso si commuta tra quattro frequenze simboliche, ad esempio $\qty{14081,20}{\kilo\hertz}$, $\qty{14081,40}{\kilo\hertz}$, $\qty{14081,61}{\kilo\hertz}$ e $\qty{14081,83}{\kilo\hertz}$.

[question:AE406]