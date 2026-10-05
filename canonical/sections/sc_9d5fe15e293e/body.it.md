Nelle trasmissioni digitali, le informazioni vengono trasmesse sotto forma di simboli. Un simbolo è uno stato di segnale distinguibile, trasmesso per un determinato periodo di tempo. Questi stati di segnale possono differire, ad esempio, per ampiezza, frequenza o fase, o per combinazioni di queste proprietà. Come tali simboli vengono generati lo esamineremo nelle sezioni seguenti. A seconda di quanti simboli diversi può utilizzare un metodo di trasmissione, un singolo simbolo può contenere uno o più bit di informazione.

Se sono disponibili solo due simboli diversi, ogni simbolo può trasmettere esattamente un bit. Con quattro simboli possibili, un simbolo può già trasmettere due bit, poiché con due bit si possono rappresentare quattro combinazioni diverse. Di conseguenza, otto simboli diversi possono trasmettere tre bit contemporaneamente e $\num{16}$ simboli diversi possono trasmettere quattro bit contemporaneamente.

In generale, il numero $N$ di bit trasmissibili con un simbolo deriva dal numero $M=2^N$ di simboli possibili:

$N = \log_2(M)$

La *velocità di simbolo* indica quanti simboli vengono trasmessi al secondo. La sua unità è il *Baud*. Una velocità di simbolo di $\qty{1000}{\baud}$ significa quindi che vengono trasmessi $\num{1000}$ simboli al secondo.

La velocità di simbolo non coincide necessariamente con la velocità di dati. Se ogni simbolo trasmette più bit, la velocità di dati è corrispondentemente maggiore. Per la velocità di dati $R_\mathrm{D}$ (con l'unità $\unit{\bit\per\second}$) e la velocità di simbolo $R_\mathrm{S}$ vale:

$R_\mathrm{D} = R_\mathrm{S} \cdot N$

Ad esempio, se con una velocità di simbolo di $\qty{1200}{\baud}$ ogni simbolo trasmette due bit, si ottiene una velocità di dati di:

$R_\mathrm{D} = \qty{1200}{\baud} \cdot \qty{2}{\bit\per{Symbol}} = \qty{2400}{\bit\per\second}$

Il numero di simboli possibili e la velocità di simbolo sono quindi grandezze importanti per i metodi di trasmissione digitale. Come i singoli simboli possano essere rappresentati da diverse proprietà di un segnale, lo esamineremo nelle sezioni seguenti.

[question:AA104]

---

Un semplice esempio di come simboli diversi possano essere rappresentati da diversi stati di segnale è la *modulazione a spostamento di frequenza* (*Frequency-Shift Keying*, FSK), già nota dalla sezione [sec:ask_fsk_afsk].

Nella FSK, la frequenza del segnale trasmesso viene commutata tra diversi valori. La figura [ref:a_fsk] mostra una FSK binaria con due frequenze simbolo possibili nella rappresentazione temporale. Ad esempio, la frequenza più alta può rappresentare il simbolo $1$ e la frequenza più bassa il simbolo $0$. Poiché sono disponibili due simboli diversi, ogni simbolo può trasmettere un bit.

<margin>
[picture:703:a_fsk:FSK (Frequency-Shift Keying)]
</margin>

Un esempio è *RTTY*. Qui si commuta tra due frequenze simbolo, ad esempio tra $\qty{14072,43}{\kilo\hertz}$ e $\qty{14072,60}{\kilo\hertz}$. Con ogni simbolo si può quindi trasmettere un bit, cioè $0$ o $1$.

[question:AE405]

La FSK, tuttavia, non è limitata a due frequenze simbolo. Se, ad esempio, vengono utilizzate quattro frequenze diverse, sono disponibili quattro simboli diversi. A ogni simbolo può quindi essere assegnata una delle quattro possibili combinazioni di bit $00$, $01$, $10$ o $11$. In questo modo, ogni simbolo può trasmettere due bit.

Un esempio di ciò è il metodo di trasmissione *FT4*. Qui si può commutare tra quattro frequenze simbolo, ad esempio $\qty{14081,20}{\kilo\hertz}$, $\qty{14081,40}{\kilo\hertz}$, $\qty{14081,61}{\kilo\hertz}$ e $\qty{14081,83}{\kilo\hertz}$.

[question:AE406]
