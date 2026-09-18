Questa sezione mostra come i segnali analogici vengano convertiti in valori digitali e, viceversa, come i valori digitali vengano riconvertiti in segnali analogici. A tale scopo vengono utilizzati i *convertitori A/D* (analogico-digitale) e *D/A* (digitale-analogico). La figura [ref:a_adc_dac] mostra gli schemi a blocchi di un convertitore A/D e di uno D/A.

<margin>
[picture:1130:a_adc_dac:Convertitori A/D e D/A]
</margin>

Un convertitore A/D campiona un segnale analogico di ingresso in determinati istanti di tempo e genera da esso valori numerici digitali che possono essere successivamente elaborati digitalmente da altre parti di un circuito.

Poiché un convertitore A/D opera con un numero limitato di valori digitali possibili, può rilevare l’ampiezza di un segnale analogico di ingresso solo in determinate fasi. Ci si ricorda in questo caso dell’esempio del dimmer e dell’interruttore a gradini utilizzato in precedenza. Se il valore effettivo si trova tra due fasi possibili, deve essere assegnato a una di esse. Ciò comporta un *errore di quantizzazione*.

[question:AF607]

---

Il numero di fasi possibili di un convertitore A/D viene definito come sua *risoluzione*. Essa viene spesso indicata in bit (unità: $\unit{\bit}$). Se, ad esempio, un convertitore può distinguere $\num{256}$ valori diversi, ha una risoluzione di $\qty{8}{\bit}$, poiché con $\qty{8}{\bit}$ è possibile rappresentare $\num{256}$ valori diversi. Un convertitore $\qty{16}{\bit}$ può già distinguere $\num{65536}$ valori diversi.

Per i segnali che possono assumere sia valori positivi che negativi, tipicamente una parte di questi valori viene utilizzata per la gamma positiva e una parte per quella negativa del segnale.

La figura [ref:a_adc_4bit] mostra un segnale sinusoidale che è stato digitalizzato da un convertitore A/D con una risoluzione di $\qty{4}{\bit}$ e poi riconvertito in un segnale analogico. La figura [ref:a_adc_12bit] mostra lo stesso segnale sinusoidale, che tuttavia è stato digitalizzato da un convertitore A/D con una risoluzione di $\qty{12}{\bit}$ e poi riconvertito in un segnale analogico. Si nota chiaramente che i $\qty{8}{\bit}$ aggiuntivi portano a una risoluzione molto più fine (migliore di un fattore 256), tanto che il segnale ricostruito si avvicina già molto al segnale sinusoidale originale.

<margin>
[picture:300:a_adc_4bit:Segnale sinusoidale digitalizzato da un convertitore A/D a 4 bit e successiva conversione D/A]
[picture:299:a_adc_12bit:Segnale sinusoidale digitalizzato da un convertitore A/D a 12 bit e successiva conversione D/A]
</margin>

[question:AF608]

Un’altra proprietà importante di un convertitore A/D è la precisione temporale del campionamento. I singoli campioni dovrebbero essere acquisiti il più possibile esattamente negli intervalli di tempo previsti. A tale scopo è necessario un generatore di clock di campionamento il più possibile stabile.

In pratica, tuttavia, i tempi di campionamento effettivi possono discostarsi leggermente dai tempi ideali. Queste fluttuazioni temporali vengono definite *jitter*. Il jitter può causare errori aggiuntivi e quindi rumore aggiuntivo nel segnale digitalizzato. Lo stesso meccanismo si verifica anche sul lato del convertitore D/A. Qui il jitter porta a rumore aggiuntivo nel segnale analogico.

[question:AF621]

---

Il *convertitore D/A* è l’opposto del convertitore A/D. Esso genera un segnale analogico a partire da un flusso di dati digitale o da campioni digitali.

Anche un convertitore D/A non può produrre valori di uscita arbitrariamente diversi. Come nel caso del convertitore A/D, esso ha una risoluzione specifica in bit e quindi solo un numero finito di valori di uscita possibili.

Un convertitore D/A può inoltre generare solo tensioni all’interno di un determinato intervallo di valori, ad esempio da $\qty{0}{\volt}$ a $\qty{1}{\volt}$ o da $\qty{-2}{\volt}$ a $\qty{2}{\volt}$.

In un convertitore D/A che opera in modo lineare, i valori di uscita possibili sono distribuiti uniformemente su questo intervallo di tensioni. Se, ad esempio, un convertitore D/A ha una risoluzione di $\qty{4}{\bit}$, sono disponibili

$\num{2^4}=\num{16}$

fasi possibili.

[question:AF609]

Se queste fasi vengono distribuite su un intervallo di tensioni da $\qty{0}{\volt}$ a $\qty{1}{\volt}$, tra le $\num{16}$ fasi ci sono in totale $\num{15}$ passi intermedi. La *passo* è quindi pari a

$\frac{\qty{1}{\volt}}{16-1}\approx\qty{67}{\milli\volt}.$

[question:AF611]
[question:AF610]

---

I convertitori A/D e D/A vengono utilizzati, ad esempio, nei ricevitori e nei transceiver SDR. I segnali analogici di ingresso vengono prima digitalizzati da un convertitore A/D e poi elaborati digitalmente. Se da essi deve essere generato nuovamente un segnale analogico, i valori digitali vengono riconvertiti in valori di tensione analogici tramite un convertitore D/A.

Può accadere che un segnale di ingresso utilizzi solo una piccola parte dell’intervallo di valori disponibile di un convertitore A/D. In questo caso vengono utilizzate solo una parte delle fasi digitali disponibili.

Viceversa, un segnale di ingresso può superare l’intervallo di valori massimo di un convertitore A/D. I valori superiori alla tensione di ingresso massima rilevabile non possono più essere rappresentati correttamente e vengono mappati solo con il valore massimo possibile. Questo effetto viene definito *clipping*. Nei grafici del segnale, le aree interessate appaiono quindi troncate.

Anche un convertitore D/A non può generare una tensione di uscita al di fuori del suo intervallo di valori previsto.

Maggiore è la risoluzione di un convertitore A/D o D/A, più fini possono essere rappresentati digitalmente valori di ampiezza diversi o riconvertiti in valori di tensione analogici. Con una risoluzione bassa, invece, sono disponibili solo poche fasi possibili, per cui le gradazioni risultano più evidenti.

[question:AF613]
[question:AF612]
[question:AF614]