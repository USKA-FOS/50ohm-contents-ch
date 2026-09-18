Nella classe E abbiamo già imparato come si comportano i condensatori in un collegamento in serie e in parallelo. Nel capitolo precedente abbiamo trattato anche il collegamento in serie di bobine. In questo capitolo esaminiamo ora il collegamento in parallelo di bobine e condensatori. Prima di tutto, però, riassumiamo ancora una volta le relazioni fondamentali nei collegamenti in parallelo e in serie di capacità.

Nei circuiti risonanti paralleli, bobine e condensatori vengono combinati tra loro. Anche una bobina reale possiede una certa capacità propria. Questa si forma, ad esempio, a causa degli avvolgimenti della bobina e delle coppie elettriche esistenti tra le spire.

Per un calcolo il più possibile preciso della frequenza di risonanza, queste capacità "invisibili" devono essere prese in considerazione. Nel seguente esercizio le capacità dei condensatori e la capacità propria della bobina possono essere sommate direttamente poiché sono collegate in parallelo tra loro.

È particolarmente importante fare attenzione alle diverse unità di misura. Prima del calcolo, quindi, tutti i valori devono essere convertiti nella stessa unità affinché le capacità possano essere sommate correttamente.

[question:AD103]

Nel seguente esercizio tre condensatori sono collegati in serie. Nella classe E abbiamo imparato che, nei condensatori in collegamento in serie, si sommano i reciproci delle capacità:

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

Anche in questo caso, prima del calcolo, le capacità devono essere convertite nella stessa unità affinché i reciproci possano essere sommati correttamente.

[question:AD101]

---

Nei circuiti in corrente alternata, oltre alle note resistenze ohmiche, compaiono anche reattanze, come abbiamo già visto per i condensatori e le bobine. La normale resistenza ohmica viene chiamata resistenza attiva $R$. Le reattanze sono indicate con $X$. Entrambi i tipi di resistenza influenzano contemporaneamente il flusso di corrente nel circuito.

Poiché la resistenza attiva e la reattanza agiscono in modo diverso, non possono semplicemente essere sommate. Vengono invece composte geometricamente. Ci si può rappresentare questo concetto come un triangolo rettangolo, come mostrato nella figura [ref:a_dreieck]:

---

- La resistenza attiva $R$ forma il lato orizzontale.
- La reattanza $X$ forma il lato verticale.
- La resistenza totale risultante viene chiamata impedenza $|Z|$.

<margin>
[picture:1067:a_dreieck:Triangolo rettangolo per illustrare il calcolo dell'impedenza $|Z|$ a partire dalla resistenza attiva $R$ e dalla reattanza $X$]
</margin>

L'impedenza può essere calcolata con il teorema di Pitagora (cfr. raccolta di formule):

$ |Z| = \sqrt{R^2 + X^2} $

La lettera $Z$ viene utilizzata per la cosiddetta impedenza. Per i calcoli in questo capitolo, tuttavia, è sufficiente considerare il valore assoluto $|Z|$ come resistenza totale in corrente alternata del circuito.

<indepth>
Per chi è interessato alla matematica: l'impedenza $Z$ è una grandezza complessa che contiene la resistenza attiva $R$ come parte reale e la reattanza $X$ come parte immaginaria:

$Z = R + jX$

Il valore assoluto $|Z|$ corrisponde quindi alla lunghezza del vettore nel piano complesso, che si ottiene combinando $R$ e $X$.
</indepth>

Per la domanda successiva, prima di poter applicare il teorema di Pitagora, deve essere calcolata la reattanza $X_C$ del condensatore a $\qty{1}{\mega\hertz}$. A tale scopo utilizziamo la formula per la reattanza di un condensatore.

[question:AD104]

La domanda successiva riguarda il calcolo dell'impedenza di un circuito in serie composto da una resistenza e una bobina. Prima calcoliamo $X_L$, poi applichiamo nuovamente il teorema di Pitagora. Anche in questo caso è necessario fare attenzione alle potenze di dieci per poter eseguire correttamente il calcolo.

[question:AD105]
