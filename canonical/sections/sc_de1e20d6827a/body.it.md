Questa sezione mostra come i segnali analogici vengono convertiti in valori digitali e i valori digitali vengono riconvertiti in segnali analogici. A questo scopo vengono utilizzati *convertitori A/D* (convertitori analogico-digitali) e *convertitori D/A* (convertitori digitale-analogici). La figura [ref:a_adc_dac] mostra gli schemi a blocchi di un convertitore A/D e di un convertitore D/A.

<margin>
[picture:1130:a_adc_dac:Convertitore A/D e D/A]
</margin>

Un convertitore A/D campiona un segnale di ingresso analogico in determinati istanti di tempo e genera da esso valori numerici digitali, che possono successivamente essere elaborati digitalmente da altre parti di un circuito.

Poiché un convertitore A/D opera solo con un numero limitato di possibili valori digitali, può catturare l'ampiezza di un segnale di ingresso analogico solo in determinati livelli. Ricordiamo qui l'esempio utilizzato in precedenza nella sezione [sec:sampling_quantisierung] con il dimmer e l'interruttore a gradini. Se il valore effettivo si trova tra due livelli possibili, deve essere assegnato a uno di essi. Ciò genera un *errore di quantizzazione*.

[question:AF607]

---

Il numero di livelli possibili di un convertitore A/D è chiamato sua *risoluzione*. Viene spesso indicata in bit (unità: $\unit{\bit}$). Ad esempio, se un convertitore può distinguere $\num{256}$ valori diversi, ha una risoluzione di $\qty{8}{\bit}$, poiché con $\qty{8}{\bit}$ si possono rappresentare $\num{256}$ valori diversi. Un convertitore a $\qty{16}{\bit}$ può già distinguere $\num{65536}$ valori diversi.

Per segnali che possono assumere sia valori positivi che negativi, tipicamente una parte di questi valori viene utilizzata per l'intervallo positivo del segnale e una parte per l'intervallo negativo.

La figura [ref:a_adc_4bit] mostra un segnale sinusoidale digitalizzato da un convertitore A/D con una risoluzione di $\qty{4}{\bit}$ e successivamente riconvertito in un segnale analogico. La figura [ref:a_adc_12bit] mostra lo stesso segnale sinusoidale, ma digitalizzato da un convertitore A/D con una risoluzione di $\qty{12}{\bit}$ e successivamente riconvertito in un segnale analogico. Si può chiaramente vedere che i bit aggiuntivi di $\qty{8}{\bit}$ portano a una risoluzione molto più fine (migliore di un fattore 256), in modo che il segnale ricostruito si avvicini molto al segnale sinusoidale originale.

<margin>
[picture:300:a_adc_4bit:Segnale sinusoidale digitalizzato da un convertitore A/D a 4 bit e successiva conversione D/A]
[picture:299:a_adc_12bit:Segnale sinusoidale digitalizzato da un convertitore A/D a 12 bit e successiva conversione D/A]
</margin>

[question:AF608]

Un'altra importante proprietà di un convertitore A/D è l'accuratezza temporale del campionamento. I singoli campioni dovrebbero essere acquisiti il più possibile esattamente negli intervalli di tempo previsti. Per questo è necessario un generatore di clock di campionamento il più stabile possibile.

Nella pratica, tuttavia, gli istanti effettivi di campionamento possono discostarsi leggermente da quelli ideali. Queste fluttuazioni temporali sono chiamate *jitter*. Il jitter può portare a errori aggiuntivi e quindi a rumore aggiuntivo nel segnale digitalizzato. Lo stesso meccanismo si verifica sul lato del convertitore D/A. Lì, il jitter porta a rumore aggiuntivo nel segnale analogico.

[question:AF621]

---

La controparte del convertitore A/D è il *convertitore D/A*. Esso genera da un flusso di dati digitale o da campioni digitali nuovamente un segnale analogico.

Anche un convertitore D/A non può generare un numero arbitrario di valori di uscita diversi. Come nel convertitore A/D, ha una certa risoluzione in bit e quindi solo un numero finito di possibili valori di uscita.

Un convertitore D/A può inoltre generare solo tensioni entro un certo intervallo di valori, ad esempio da $\qty{0}{\volt}$ a $\qty{1}{\volt}$ o da $\qty{-2}{\volt}$ a $\qty{2}{\volt}$.

In un convertitore D/A che opera linearmente, i possibili valori di uscita sono distribuiti uniformemente su questo intervallo di tensione. Ad esempio, se un convertitore D/A ha una risoluzione di $\qty{4}{\bit}$, sono disponibili

$\num{2^4}=\num{16}$

livelli possibili.

[question:AF609]

Se questi sono distribuiti su un intervallo di tensione da $\qty{0}{\volt}$ a $\qty{1}{\volt}$, ci sono complessivamente $\num{15}$ passi intermedi tra i $\num{16}$ livelli. Il passo è quindi

$\frac{\qty{1}{\volt}}{16-1}\approx\qty{67}{\milli\volt}.$

[question:AF611]
[question:AF610]

---

I convertitori A/D e D/A sono utilizzati, ad esempio, nei ricevitori e transceiver SDR. I segnali di ingresso analogici vengono prima digitalizzati da un convertitore A/D e successivamente elaborati digitalmente. Se da questi deve essere generato nuovamente un segnale analogico, i valori digitali vengono riconvertiti in valori di tensione analogici mediante un convertitore D/A.

In questo contesto può accadere che un segnale di ingresso utilizzi solo una piccola parte dell'intervallo di valori disponibile di un convertitore A/D. In questo caso, viene utilizzata corrispondentemente solo una parte dei livelli digitali disponibili.

Viceversa, un segnale di ingresso può superare l'intervallo di valori massimo di un convertitore A/D. I valori al di sopra della tensione di ingresso massima acquisibile non possono più essere rappresentati correttamente e vengono mappati solo con il valore massimo possibile. Questo effetto è chiamato *clipping*. Nell'andamento del segnale, le aree interessate appaiono quindi troncate.

Anche un convertitore D/A non può generare una tensione di uscita al di fuori del suo intervallo di valori previsto.

Più alta è la risoluzione di un convertitore A/D o D/A, più finemente possono essere rappresentati digitalmente diversi valori di ampiezza o riconvertiti in valori di tensione analogici. Con una bassa risoluzione, invece, sono disponibili solo pochi livelli possibili, in modo che le gradazioni diventino più evidenti.

[question:AF613]
[question:AF612]
[question:AF614]
