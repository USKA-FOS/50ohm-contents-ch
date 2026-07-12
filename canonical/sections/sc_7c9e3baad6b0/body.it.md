Nella classe N abbiamo già appreso il concetto di potenza come prodotto di corrente e tensione ($P = U \cdot I$). Nella classe E approfondiamo ulteriormente questo argomento, occupandoci tra l'altro della manipolazione delle formule.

---

A tal fine, consideriamo il circuito nella figura [ref:e_leistung_r]. Essa mostra come la potenza elettrica venga convertita in calore su una resistenza. Supponendo che le grandezze $P$ e $R$ siano note, la tensione $U$ può essere determinata utilizzando la formula della potenza ($P = U \cdot I$) e la legge di Ohm ($U = R \cdot I$).

<margin>
[picture:1013:e_leistung_r:La potenza viene convertita in calore sulla resistenza $R$]
</margin>
  
---

<tip>
Le formule derivate si trovano anche in modo chiaro nella [raccolta di formule](https://50ohm.de/hm).
</tip>
  
Per prima cosa, riorganizziamo l'equazione della legge di Ohm per la corrente:

$\begin{align*} U &= R \cdot I &\quad\quad\quad &|~: R\\ \frac{U}{R} &= \frac{\cancel{R} \cdot I}{\cancel{R}}\\[1.5ex] I &= \frac{U}{R}.\end{align*}$

Sostituendo questa espressione per $I$ nella nostra formula della potenza, otteniamo:

$\begin{split} P &= U \cdot \frac{U}{R}\\P&=\frac{U^2}{R}.\end{split}$

Risolviamo questa equazione per $U^2$ moltiplicando entrambi i lati per R:

$\begin{align*} P &= \frac{U^2}{R} &\quad\quad\quad &|~\cdot R\\ U^2 &= P \cdot R.\end{align*}$

Ora vogliamo determinare la tensione $U$. Per fare ciò, applichiamo l'operazione inversa della quadratura, ovvero l'estrazione della radice quadrata. Otteniamo così:

$\begin{align*} U^2 &= P \cdot R &\quad\quad\quad &|~\sqrt{~~}\\ U &= \sqrt{P \cdot R}.\end{align*}$

In alcune domande d'esame è importante riconoscere le giuste relazioni. Utilizzando la raccolta di formule, è sempre possibile derivare la soluzione corretta.

[question:EB504]
  
Anche per la corrente $I$, sostituendo la legge di Ohm nella formula della potenza, è possibile derivare la relazione tra corrente $I$, resistenza $R$ e potenza $P$.

Partiamo dalle due equazioni $P = U \cdot I$ e $U = R \cdot I$. Sostituendo la seconda equazione nella prima per $U$, otteniamo:

$\begin{split} P &= R \cdot I \cdot I\\ P &= I^2 \cdot R.\end{split}$

Risolviamo per $I^2$ dividendo entrambi i lati per R:

$\begin{align*} P &= I^2 \cdot R &\quad\quad\quad &|~:~R\\ I^2 &= \frac{P}{R}.\end{align*}$

Nell'ultimo passaggio estraiamo quindi la radice quadrata:

$\begin{align*} I^2 &= \frac{P}{R} &\quad\quad\quad &|~\sqrt{~~}\\ I &= \sqrt{\frac{P}{R}}\end{align*}$

[question:EB505]

Se si conoscono la potenza $P$ e la corrente $I$ o la tensione $U$, è sempre possibile calcolare anche la resistenza $R$ da esse.

Conosciamo già:

$P=\frac{U^2}{R}$

Risolviamo per R moltiplicando entrambi i lati dell'equazione per R e poi dividendo per P:

$R = \frac{U^2}{P}$

D'altra parte, $P = I^2 \cdot R$. Dividiamo entrambi i lati per $I^2$ e otteniamo l'espressione cercata:

$R = \frac{P}{I^2}$

[question:EB506]

Tutte le relazioni della tecnica a corrente continua tra potenza, corrente e tensione presentate in precedenza valgono anche per la corrente alternata. Tuttavia, è necessario utilizzare i valori efficaci di corrente e tensione. In un capitolo precedente abbiamo già imparato come calcolare il valore efficace dal valore di picco:

$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}}\text{ o }\hat{U} = U_\text{eff} \cdot \sqrt{2}$

[question:EB503]

Ciò significa che con tutte le formule precedentemente derivate possiamo ora calcolare anche i seguenti problemi dal mondo dell'alta frequenza, cioè della tensione alternata.

%%%%%

[question:EB507]

Il valore efficace qui è $U_\text{eff} = \qty{100}{\volt}$. La resistenza di terminazione è $\qty{50}{\ohm}$ (resistenza pura attiva). Si cerca la potenza sul carico.

$P = \frac{U^2}{R} =\frac{(\qty{100}{\volt})^2}{\qty{50}{\ohm}} = \qty{200}{\watt}$

%%%%%

[question:EB508]

Anche se la corrente è nota, si può calcolare con la formula nota $P = I^2 \cdot R$. Inseriamo i valori:
  
$P = (\qty{2}{\ampere})^2 \cdot \qty{50}{\ohm} = \qty{200}{\watt}$

%%%%%

[question:EB509]

Per calcolare la potenza che viene dissipata in una resistenza da $\qty{100}{\ohm}$ su cui cade una tensione di $\qty{10}{\volt}$, utilizziamo di nuovo:

$P = \frac{U^2}{R} = \frac{(\qty{10}{\volt})^2}{\qty{100}{\ohm}} = \qty{1}{\watt} $

%%%%%

[question:EB510]

La risposta a questa domanda richiede una certa riflessione. Sono specificati sia una resistenza di picco alla tensione ($\qty{700}{\volt}$) che una potenza massima ($\qty{1}{\watt}$). Ci si chiede solo quale limite venga raggiunto per primo se aumentiamo la tensione.

Calcoliamo innanzitutto la tensione che deve essere presente sulla resistenza ($\qty{10}{\kilo\ohm}$) affinché venga raggiunta la potenza ammissibile. A tal fine, calcoliamo (derivazione sopra):

$U = \sqrt{P \cdot R} = \sqrt{\qty{1}{\watt} \cdot \qty{10000}{\ohm}} = \qty{100}{\volt}$

Questa è quindi la massima tensione continua cercata!

%%%%%

[question:EB511]

Qui il percorso di calcolo è lo stesso del problema precedente, cambiano solo i valori numerici:

$U = \sqrt{P \cdot R} = \sqrt{\qty{6}{\watt} \cdot \qty{10^5}{\ohm}} \approx \qty{774,6}{\volt} \approx \qty{775}{\volt}$

%%%%%

[question:EB512]

Quando sono dati il valore della resistenza e la capacità di carico massima e viene richiesta la corrente massima, utilizziamo la relazione:

$I = \sqrt{\frac{P}{R}} =  \sqrt{\frac{\qty{23}{\watt}}{\qty{120}{\ohm}}} \approx \qty{0,4378}{\ampere} \approx \qty{438}{\milli\ampere}$

[question:EB513]

In questa domanda viene utilizzato un oscilloscopio per misurare la tensione picco-picco sul carico. Questa tensione è $U_\text{SS} = \qty{25}{\volt}$. Ciò significa che la tensione di picco è $\hat{U} = \qty{12,5}{\volt}$. Calcoliamo innanzitutto il valore efficace della tensione:

$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}} = \frac{\qty{12,5}{\volt}}{\sqrt{2}} \approx \qty{8,84}{\volt}$

Quindi la corrente efficace (Legge di Ohm):

$I_\text{eff} = \frac{U_\text{eff}}{R} = \frac{\qty{8,84}{\volt}}{\qty{1000}{\ohm}} \approx \qty{8,8}{\milli\ampere}$

Con ciò si potrebbe anche calcolare la potenza efficace, ma la domanda non va così oltre.

---

[question:EB514]

La risposta a questa domanda può essere calcolata molto bene a mente. Qui vengono collegati in parallelo 11 resistori identici, come mostrato nella figura [ref:e_dummyload_11]. Ciò significa che la corrente attraverso ogni singolo resistore è 1/11 della corrente totale. Pertanto, anche la potenza su ogni resistore è solo 1/11 della potenza totale.

Quindi la potenza totale ammissibile è $11 \cdot \qty{5}{\watt} =\qty{55}{\watt}$.

<margin>
[picture:1014:e_dummyload_11:Dummy load composta da 11 resistori di uguali dimensioni]
</margin>