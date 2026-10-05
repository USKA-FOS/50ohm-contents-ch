Nella sezione [sec:reihe_parallel_kondensator] abbiamo già imparato come si comportano i condensatori in serie e in parallelo. Nella sezione precedente [sec:reihenschaltung_spule] è stata inoltre trattata la connessione in serie delle bobine. In questa sezione consideriamo ora il collegamento in parallelo di bobine e condensatori. Tuttavia, iniziamo ripetendo ancora una volta le relazioni fondamentali nei collegamenti in parallelo e in serie delle capacità.

Nei circuiti risonanti paralleli, bobine e condensatori vengono combinati tra loro. Anche una bobina reale possiede una certa capacità parassita. Questa si forma, ad esempio, attraverso gli avvolgimenti della bobina e gli accoppiamenti di campo elettrico tra le spire che ne derivano.

Per un calcolo il più possibile accurato della frequenza di risonanza, queste capacità "invisibili" devono essere prese in considerazione. Nel seguente esercizio, le capacità dei condensatori e la capacità parassita della bobina possono essere sommate direttamente, poiché sono collegate in parallelo tra loro.

Particolarmente importante è prestare attenzione alle diverse unità. Prima del calcolo, tutti i valori dovrebbero quindi essere convertiti nella stessa unità, in modo che le capacità possano essere sommate correttamente.

[question:AD103]

Nel seguente esercizio, tre condensatori sono collegati in serie. Nella sezione [sec:reihe_parallel_kondensator] abbiamo imparato che per i condensatori in serie si sommano i reciproci delle capacità:

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

Anche qui le capacità devono essere convertite nella stessa unità prima del calcolo, in modo che i reciproci possano essere sommati correttamente.

[question:AD101]

---

Nei circuiti a corrente alternata, oltre alle note resistenze ohmiche, compaiono anche reattanze, come abbiamo già imparato con condensatori e bobine. La normale resistenza ohmica è chiamata resistenza attiva $R$. Le reattanze sono indicate con $X$. Entrambi i tipi di resistenza influenzano simultaneamente il flusso di corrente nel circuito.

Poiché resistenza attiva e reattanza agiscono diversamente, non possono essere semplicemente sommate. Invece, vengono combinate geometricamente. Si può immaginare questo come un triangolo rettangolo come nella figura [ref:a_dreieck]:

---

- La resistenza attiva $R$ forma il lato orizzontale.
- La reattanza $X$ forma il lato verticale.
- La resistenza totale risultante è chiamata impedenza $|Z|$.

<margin>
[picture:1067:a_dreieck:Triangolo rettangolo per illustrare il calcolo dell'impedenza $|Z|$ dalla resistenza attiva $R$ e dalla reattanza $X$]
</margin>

L'impedenza può essere calcolata usando il teorema di Pitagora (cfr. raccolta di formule):

$ |Z| = \sqrt{R^2 + X^2} $

La lettera $Z$ è usata per la cosiddetta impedenza. Per i calcoli in questo capitolo, tuttavia, è sufficiente considerare il valore assoluto $|Z|$ come la resistenza totale a corrente alternata del circuito.

<indepth>
Per gli interessati alla matematica: L'impedenza $Z$ è una grandezza complessa, che contiene la resistenza attiva $R$ come parte reale e la reattanza $X$ come parte immaginaria:

$Z = R + jX$

Il valore assoluto $|Z|$ corrisponde quindi alla lunghezza del vettore nel piano complesso, che risulta dalla combinazione di $R$ e $X$.
</indepth>

Per la prossima domanda, prima di poter applicare il teorema di Pitagora, deve essere calcolata la reattanza $X_C$ del condensatore a $\qty{1}{\mega\hertz}$. Per questo usiamo la formula per la reattanza di un condensatore.

[question:AD104]

La prossima domanda riguarda il calcolo dell'impedenza di un collegamento in serie di una resistenza e una bobina. Prima calcoliamo $X_L$, poi applichiamo di nuovo il teorema di Pitagora. Anche qui devono essere considerate le potenze di dieci, in modo che il calcolo possa essere eseguito correttamente.

[question:AD105]
