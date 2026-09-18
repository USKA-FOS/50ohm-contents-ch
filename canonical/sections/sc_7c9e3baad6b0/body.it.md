Abbiamo già incontrato il concetto di potenza come prodotto tra corrente e tensione ($P = U \cdot I$). Qui approfondiamo ulteriormente l'argomento occupandoci, tra l'altro, del riarrangiamento delle formule.

---

A questo scopo consideriamo il circuito mostrato nella figura [ref:e_leistung_r]. Essa illustra come in una resistenza la potenza elettrica venga convertita in calore. Supponendo noti i valori di $P$ e $R$, è possibile determinare la tensione $U$ utilizzando la formula della potenza ($P = U \cdot I$) e la legge di Ohm ($U = R \cdot I$).

<margin>
[picture:1013:e_leistung_r:La potenza viene dissipata come calore nella resistenza $R$]
</margin>

---

<tip>
Le formule derivate sono disponibili anche in modo chiaro nella [raccolta di formule dell'UFCOM](https://www.bakom.admin.ch/dam/de/sd-web/ooOLDCmCmEmX/formelsammlung.pdf).
</tip>

Innanzitutto, riordiniamo l'equazione della legge di Ohm per esprimere la corrente:

$\begin{align*} U &= R \cdot I &\quad\quad\quad &|~: R\\ \frac{U}{R} &= \frac{\cancel{R} \cdot I}{\cancel{R}}\\[1.5ex] I &= \frac{U}{R}.\end{align*}$

Sostituendo questa espressione di $I$ nella formula della potenza, otteniamo:

$\begin{split} P &= U \cdot \frac{U}{R}\\P&=\frac{U^2}{R}.\end{split}$

Riordiniamo questa equazione per $U^2$ moltiplicando entrambi i membri per $R$:

$\begin{align*} P &= \frac{U^2}{R} &\quad\quad\quad &|~\cdot R\\ U^2 &= P \cdot R.\end{align*}$

Ora vogliamo determinare la tensione $U$. A questo scopo applichiamo l'operazione inversa dell'elevamento al quadrato, cioè l'estrazione della radice quadrata. Otteniamo così:

$\begin{align*} U^2 &= P \cdot R &\quad\quad\quad &|~\sqrt{~~}\\ U &= \sqrt{P \cdot R}.\end{align*}$

In alcuni quesiti d'esame è importante saper riconoscere le giuste relazioni. Con l'aiuto della raccolta di formule è possibile derivare in qualsiasi momento la soluzione corretta.

[question:EB504]

Anche per la corrente $I$ è possibile derivare, sostituendo la legge di Ohm nella formula della potenza, la relazione tra corrente $I$, resistenza $R$ e potenza $P$.

Partiamo dalle due equazioni $P = U \cdot I$ e $U = R \cdot I$. Sostituendo la seconda equazione nella prima per $U$, otteniamo:

$\begin{split} P &= R \cdot I \cdot I\\ P &= I^2 \cdot R.\end{split}$

Riordiniamo per $I^2$ dividendo entrambi i membri per $R$:

$\begin{align*} P &= I^2 \cdot R &\quad\quad\quad &|~:~R\\ I^2 &= \frac{P}{R}.\end{align*}$

Nell'ultimo passaggio estraiamo la radice:

$\begin{align*} I^2 &= \frac{P}{R} &\quad\quad\quad &|~\sqrt{~~}\\ I &= \sqrt{\frac{P}{R}}\end{align*}$

[question:EB505]

Se si conoscono la potenza $P$ e la corrente $I$ o la tensione $U$, è sempre possibile calcolare la resistenza $R$.

Abbiamo già visto che:

$P=\frac{U^2}{R}$

Riordiniamo per $R$ moltiplicando entrambi i membri dell'equazione per $R$ e poi dividendo per $P$:

$R = \frac{U^2}{P}$

D'altra parte, $P = I^2 \cdot R$. Dividendo entrambi i membri per $I^2$, otteniamo l'espressione cercata:

$R = \frac{P}{I^2}$

[question:EB506]

Tutte le relazioni tra potenza, corrente e tensione presentate finora, valide per la tecnica in tensione continua, si applicano anche alla corrente alternata. Tuttavia, in questo caso devono essere utilizzati i valori efficaci di corrente e tensione. In un capitolo precedente [sec:spitze_effektiv_wert] abbiamo già imparato a calcolare il valore efficace partendo dal valore di picco:

$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}}\text{ ovvero }\hat{U} = U_\text{eff} \cdot \sqrt{2}$

[question:EB503]

Ciò significa che, con tutte le formule derivate in precedenza, possiamo ora risolvere anche esercizi relativi al mondo dell'alta frequenza, cioè della tensione alternata.

%%%%%

[question:EB507]

Il valore efficace della tensione è $U_\text{eff} = \qty{100}{\volt}$. La resistenza di terminazione è $\qty{50}{\ohm}$ (resistenza attiva pura). Si chiede di calcolare la potenza dissipata dal carico.

$P = \frac{U^2}{R} =\frac{(\qty{100}{\volt})^2}{\qty{50}{\ohm}} = \qty{200}{\watt}$

%%%%%

[question:EB508]

Anche se è nota la corrente, è possibile calcolare la potenza con la formula nota $P = I^2 \cdot R$. Sostituendo i valori:

$P = (\qty{2}{\ampere})^2 \cdot \qty{50}{\ohm} = \qty{200}{\watt}$

%%%%%

[question:EB509]

Per calcolare la potenza dissipata in una resistenza di $\qty{100}{\ohm}$ ai cui capi è presente una tensione di $\qty{10}{\volt}$, utilizziamo nuovamente:

$P = \frac{U^2}{R} = \frac{(\qty{10}{\volt})^2}{\qty{100}{\ohm}} = \qty{1}{\watt}$

%%%%%

[question:EB510]

La risposta a questo quesito richiede una certa riflessione. Sono indicati sia un valore massimo di tenuta in tensione ($\qty{700}{\volt}$) che una potenza massima ($\qty{1}{\watt}$). Ci si chiede quale dei due limiti venga raggiunto per primo all'aumentare della tensione.

Calcoliamo innanzitutto la tensione che deve essere applicata alla resistenza ($\qty{10}{\kilo\ohm}$) affinché venga raggiunta la potenza ammissibile. A questo scopo utilizziamo (derivazione già vista in precedenza):

$U = \sqrt{P \cdot R} = \sqrt{\qty{1}{\watt} \cdot \qty{10000}{\ohm}} = \qty{100}{\volt}$

Quindi la massima tensione continua è proprio $\qty{100}{\volt}$!

%%%%%

[question:EB511]

Il procedimento di calcolo è lo stesso del quesito precedente, ma con valori numerici diversi:

$U = \sqrt{P \cdot R} = \sqrt{\qty{6}{\watt} \cdot \qty{10^5}{\ohm}} \approx \qty{774,6}{\volt} \approx \qty{775}{\volt}$

%%%%%

[question:EB512]

Se sono noti il valore della resistenza e la capacità di carico massima e si chiede di determinare la corrente massima, utilizziamo la relazione:

$I = \sqrt{\frac{P}{R}} =  \sqrt{\frac{\qty{23}{\watt}}{\qty{120}{\ohm}}} \approx \qty{0,4378}{\ampere} \approx \qty{438}{\milli\ampere}$

[question:EB513]

In questo quesito viene utilizzato un oscilloscopio per misurare la tensione picco-picco ai capi del carico. Tale tensione è $U_\text{SS} = \qty{25}{\volt}$. Ciò significa che la tensione di picco è $\hat{U} = \qty{12,5}{\volt}$. Calcoliamo innanzitutto il valore efficace della tensione:

$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}} = \frac{\qty{12,5}{\volt}}{\sqrt{2}} \approx \qty{8,84}{\volt}$

La corrente efficace (legge di Ohm) è quindi:

$I_\text{eff} = \frac{U_\text{eff}}{R} = \frac{\qty{8,84}{\volt}}{\qty{1000}{\ohm}} \approx \qty{8,8}{\milli\ampere}$

Con questi valori sarebbe possibile calcolare anche la potenza efficace, ma la domanda non richiede questo passaggio.

---

[question:EB514]

La risposta a questo quesito può essere calcolata molto facilmente a mente. Qui vengono collegati in parallelo 11 resistori identici, come mostrato nella figura [ref:e_dummyload_11]. Ciò significa che la corrente che scorre in ciascun resistore è $1/11$ della corrente totale. Pertanto, anche la potenza dissipata da ogni singolo resistore è solo $1/11$ della potenza totale.

Quindi la potenza totale ammissibile è $11 \cdot \qty{5}{\watt} = \qty{55}{\watt}$.

<margin>
[picture:1014:e_dummyload_11:Carico fittizio composto da 11 resistori di uguale valore]
</margin>