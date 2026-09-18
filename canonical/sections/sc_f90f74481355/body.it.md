In ogni apparecchio radio sono presenti una o più stabilizzazioni della tensione, poiché la tensione d’ingresso, soprattutto nei dispositivi alimentati a batteria, può variare e causare cambiamenti di frequenza in moduli sensibili, come ad esempio gli oscillatori.

Esistono tre varianti di stabilizzazione della tensione:
1. *Circuito con diodo Zener*
2. *Regolatori lineari di tensione*
3. *Regolatori a tensione fissa* in un circuito integrato

Il *circuito con diodo Zener* (cfr. figura [ref:a_stab_z_diode]) rappresenta un circuito molto semplice per la stabilizzazione della tensione d’uscita, poiché il diodo Zener può mantenere la tensione d’uscita entro certi limiti.

Il diodo Zener viene sempre utilizzato con una resistenza in serie e in polarizzazione inversa ($-U_Z$). I diodi Zener con tensioni di breakdown $U_Z$ a partire da $\qty{5}{\volt}$ mostrano un andamento molto ripido della curva caratteristica (cfr. figura [ref:a_z_diode_kennlinie]) e sono quindi molto adatti alla stabilizzazione della tensione. Il rendimento del circuito è molto basso, poiché devono essere considerate le perdite nella resistenza in serie $R_V$ e nel diodo Zener.

<margin>
[picture:323:a_stab_z_diode:Stabilizzazione della tensione con diodo Zener]
[picture:862:a_z_diode_kennlinie:Curva caratteristica di un diodo Zener]
</margin>

La soluzione del seguente esercizio è un po’ più complessa. Innanzitutto, si determina la potenza d’uscita a partire dalla resistenza di carico e dalla corrente di carico. Successivamente, si calcola la potenza d’ingresso assorbita a partire dalla tensione di alimentazione e dalla somma tra la corrente di carico e la corrente del diodo Zener. Il rendimento si ottiene quindi dal rapporto tra la potenza erogata e quella assorbita.

[question:AD321]

---

I *regolatori lineari di tensione* stabilizzano la tensione d’uscita facendo funzionare un transistor di potenza come una resistenza variabile, che insieme alla resistenza di carico forma un partitore di tensione.

<margin>
[picture:1079:a_diskrete_pannungsstabilisierung:Stabilizzazione della tensione realizzata con componenti discreti]
</margin>

Nel seguente esercizio è rappresentata una stabilizzazione della tensione con transistor in serie. Una tensione di riferimento di $\qty{5,6}{\volt}$ viene generata tramite un diodo Zener alla base del transistor. Il potenziale dell’emettitore, in condizioni operative di un transistor al silicio, è circa $\qty{0,6}{\volt}$ inferiore a quello della base. La tensione d’uscita regolata risulta quindi pari a circa $\qty{5}{\volt}$.

La corrente di carico fluisce anche attraverso il transistor, che si riscalda notevolmente in caso di corrente di carico elevata. I cosiddetti *transistor in serie* si trovano quindi sempre su un dissipatore nei regolatori lineari di tensione.

<margin>
[photo:246:a_Längstransistor 2N3055 su dissipatore:Il transistor in serie in un alimentatore regolato linearmente deve dissipare grandi potenze e viene quindi montato su un dissipatore.]
</margin>

[question:AD315]

La potenza dissipata $P_V$ si ottiene dalla differenza tra $P_{\mathrm{in}}$ e $P_{\mathrm{out}}$. Utilizzando la formula della potenza $P = U \cdot I$, è possibile calcolare la potenza dissipata.

[question:AD319]

Nei regolatori lineari di tensione, il rendimento è spesso molto basso per principio di funzionamento. A questo proposito, esiste un esercizio sul rendimento che può essere risolto con la nota formula $\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$.

[question:AD320]

---

Oltre al diodo Zener e al regolatore lineare di tensione, esistono anche *regolatori a tensione fissa* in un circuito integrato. I regolatori a tensione fissa funzionano come i regolatori lineari con transistor in serie e includono una sorgente di riferimento di tensione molto precisa insieme a un regolatore elettronico ottimale. Anche se la tensione d’ingresso varia notevolmente (ad esempio $\qty{\pm 2}{\volt}$), sul lato del carico la variazione di tensione è misurabile solo nell’ordine dei millivolt. I condensatori su entrambi i lati del regolatore a tensione fissa devono essere scelti secondo le specifiche del produttore, altrimenti possono verificarsi oscillazioni indesiderate nel comportamento di regolazione del circuito.

<margin>
[picture:200:a_Festspannungsregler:Regolatore a tensione fissa]
</margin>

---

Un regolatore a tensione fissa mantiene la sua tensione d’uscita pressoché costante finché la tensione d’ingresso è sufficientemente superiore a quella d’uscita. La tensione d’uscita rimane quindi quasi invariata anche in caso di fluttuazioni della tensione d’ingresso.

[question:AD316]
[question:AD317]

<tip>
Affinché il circuito di regolazione interno funzioni in modo ottimale, la tensione d’ingresso nei regolatori a tensione fissa standard (ad esempio il tipo 7812 per una tensione fissa di $\qty{12}{\volt}$) deve essere superiore di circa $\qty{3}{\volt}$ rispetto a quella d’uscita, quindi almeno $\qty{15}{\volt}$. Esistono regolatori a tensione fissa in cui la tensione d’ingresso deve essere superiore di soli $\qty{1}{\volt}$ rispetto a quella d’uscita. Questi regolatori sono chiamati *Low-Drop-Spannungsregler*.
</tip>

---

Per risolvere il seguente esercizio utilizziamo nuovamente la relazione nota: la potenza dissipata $P_V$ del regolatore a tensione fissa si ottiene dalla differenza tra $P_{\mathrm{in}}$ e $P_{\mathrm{out}}$.

[question:AD318]

<tip>
Il procedimento di soluzione inizia con il calcolo della corrente di carico: $I_L$. Nota: la corrente nel conduttore di massa del regolatore a tensione fissa è trascurabile e pertanto non viene considerata.
</tip>

<margin>
[photo:245:a_Festspannungsregler:Regolatori a tensione fissa per $\qty{5}{\volt}$, $\qty{12}{\volt}$ e $\qty{9}{\volt}$ su dissipatore]
</margin>