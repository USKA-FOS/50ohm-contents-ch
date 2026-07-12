Nella classe E abbiamo già appreso come si comportano i condensatori in serie e in parallelo. Nel capitolo precedente è stata inoltre trattata la connessione in serie di bobine. In questo capitolo esamineremo ora la connessione in parallelo di bobine e condensatori. Innanzitutto, tuttavia, ripetiamo ancora una volta le relazioni fondamentali per le connessioni in parallelo e in serie delle capacità.

Nei circuiti oscillanti paralleli, bobine e condensatori vengono combinati. Una bobina reale possiede anche una certa capacità parassita. Questa si forma, ad esempio, a causa degli avvolgimenti della bobina e delle conseguenti accoppiamenti di campo elettrico tra le spire.

Per un calcolo il più preciso possibile della frequenza di risonanza, queste capacità "invisibili" devono essere prese in considerazione. Nel seguente esercizio, le capacità dei condensatori e la capacità parassita della bobina possono essere sommate direttamente, poiché sono collegate in parallelo.

È particolarmente importante prestare attenzione alle diverse unità. Prima del calcolo, tutti i valori devono quindi essere convertiti nella stessa unità, in modo che le capacità possano essere sommate correttamente.

[question:AD103]

Nel seguente esercizio, tre condensatori sono collegati in serie. Nella classe E abbiamo imparato che, per i condensatori in serie, si sommano i reciproci delle capacità:

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

Anche qui, le capacità devono essere convertite nella stessa unità prima del calcolo, in modo che i reciproci possano essere sommati correttamente.

[question:AD101]

---

Nei circuiti a corrente alternata, oltre alle resistenze ohmiche note, compaiono anche reattanze, come quelle che abbiamo già incontrato nei condensatori e nelle bobine. La normale resistenza ohmica è chiamata resistenza attiva $R$. Le reattanze sono descritte con $X$. Entrambi i tipi di resistenza influenzano contemporaneamente il flusso di corrente nel circuito.

Dato che la resistenza attiva e la reattanza agiscono in modo diverso, non possono essere semplicemente sommate. Vengono invece combinate geometricamente. Si può immaginare come un triangolo rettangolo, come mostrato nella figura [ref:a_dreieck]:

---

- La resistenza attiva $R$ forma il lato orizzontale.
- La reattanza $X$ forma il lato verticale.
- La resistenza totale risultante è chiamata impedenza $|Z|$.

<margin>
[picture:1067:a_dreieck:Triangolo rettangolo per illustrare il calcolo dell’impedenza $|Z|$ dalla resistenza attiva $R$ e dalla reattanza $X$]
</margin>

L’impedenza può essere calcolata con il teorema di Pitagora (cfr. raccolta di formule):

$ |Z| = \sqrt{R^2 + X^2} $

La lettera $Z$ viene utilizzata per la cosiddetta impedenza. Per i calcoli in questo capitolo, tuttavia, è sufficiente considerare il modulo $|Z|$ come la resistenza totale alla corrente alternata del circuito.

<indepth>
Per gli interessati alla matematica: l’impedenza $Z$ è una grandezza complessa che contiene la resistenza attiva $R$ come parte reale e la reattanza $X$ come parte immaginaria:

$Z = R + jX$

Il modulo $|Z|$ corrisponde quindi alla lunghezza del vettore nel piano complesso, che si forma combinando $R$ e $X$.
</indepth>

Per la prossima domanda, prima di poter applicare il teorema di Pitagora, è necessario calcolare la reattanza capacitiva $X_C$ del condensatore a $\qty{1}{\mega\hertz}$. Per fare ciò, utilizziamo la formula per la reattanza capacitiva di un condensatore.

[question:AD104]

La prossima domanda riguarda il calcolo dell’impedenza di una connessione in serie di una resistenza e di una bobina. Per prima cosa calcoliamo $X_L$, poi applichiamo nuovamente il teorema di Pitagora. Anche qui è necessario prestare attenzione alle potenze di dieci per poter eseguire correttamente il calcolo.

[question:AD105]
