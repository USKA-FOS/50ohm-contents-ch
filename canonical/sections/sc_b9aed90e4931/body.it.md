Perché esiste una rete a $\qty{230}{\volt}$ in tensione alternata? La tensione alternata offre un vantaggio decisivo rispetto alla tensione continua: può essere convertita in altri valori di tensione in modo semplice ed efficiente con l’ausilio di trasformatori, con perdite ridotte. Ciò consente un adattamento efficiente della tensione per la trasmissione e l’utilizzo.

Grazie all’autoinduzione nelle bobine, l’energia può essere trasmessa tra due bobine, come mostrato nella figura [ref:e_netztrafo], in caso di tensione alternata. Nasce così un nuovo componente, il *trasformatore* o *trasmettitore*, abbreviato in *Trafo*. Esso è costituito da due bobine accoppiate magneticamente tramite un nucleo di ferro o di ferrite. Per distinguerle, si parla di lato primario con numero di spire $N_P$ e di lato secondario con numero di spire $N_S$.

<margin>
[picture:1017:e_netztrafo:Schema del trasformatore]
</margin>

<margin>
[photo:239:e_Trafo con avvolgimenti separati:Trasformatore con avvolgimenti visibilmente separati]
</margin>

Un trasformatore serve per convertire una tensione alternata elevata, ad esempio $\qty{230}{\volt}$, in una tensione alternata più bassa, ad esempio $\qty{13,8}{\volt}$. Un trasformatore può trasmettere solo tensioni alternate. Se si applica erroneamente una tensione continua a un trasformatore, questo, a causa della bassa resistenza ohmica dell’avvolgimento primario, si comporta come un cortocircuito. Il trasformatore può surriscaldarsi notevolmente e, nel peggiore dei casi, bruciarsi.

---

Il rapporto di trasformazione di un trasformatore può essere espresso come segue:

$r = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Il rapporto tra il numero di spire corrisponde quindi al rapporto tra le tensioni. Riorganizzando questa equazione fondamentale, è possibile calcolare sia le tensioni $U$ che il numero di spire $N$ sul lato primario o secondario.

<indepth>
Queste relazioni valgono per il caso ideale di un trasformatore scarico, cioè per la cosiddetta condizione a vuoto. Il termine "a vuoto" significa che non è collegata alcuna utenza al lato secondario.
</indepth>

[question:EC401]

Eseguiamo il calcolo:

$\begin{align*}r = \frac{15}{1} = 15 &= \frac{\qty{230}{\volt}}{U_S} &\quad\quad\quad &|~\cdot~U_S\\[1.5ex]15 \cdot U_S &= \qty{230}{\volt} &\quad\quad\quad &|~:~15\\[1.5ex]U_S &= \frac{\qty{230}{\volt}}{15} = \qty{15,33}{\volt}\end{align*}$

[question:EC402]

Osserviamo innanzitutto che $N_P = 5\cdot N_S$ e che $U_P = \qty{230}{\volt}$ è dato. Si cerca nuovamente la tensione $U_S$.

$r = \frac{5\cdot N_S}{N_S} = \frac{\qty{230}{\volt}}{U_S}$

Le $N_S$ si semplificano, rimane solo:

$r = 5 = \frac{\qty{230}{\volt}}{U_S}$

Moltiplichiamo entrambi i lati per $U_S$ e dividiamo entrambi i lati per 5.

$U_S = \frac{\qty{230}{\volt}}{5}$

Nella domanda seguente si cerca il numero di spire secondarie.

[question:EC403]

Dati: $N_P=600$, $U_P=\qty{230}{\volt}$ e $U_S=\qty{11,5}{\volt}$. Si cerca il numero di spire secondarie $N_S$.

$\frac{600}{N_S} = \frac{\qty{230}{\volt}}{\qty{11,5}{\volt}}$

Questo si semplifica in:

$\frac{600}{N_S} = 20$

Moltiplichiamo entrambi i lati per $N_S$ e dividiamo entrambi i lati per 20.

$N_S = \frac{600}{20} = 30$

Il trasformatore seguente aumenta la tensione d’uscita $U_S$, pertanto il numero di spire secondarie deve essere maggiore di quello primario.

[question:EC404]

Dati: $N_P= 150$, $U_P=\qty{45}{\volt}$ e $U_S=\qty{180}{\volt}$. Si cerca $N_S$.

Inseriamo i valori:

$ \frac{150}{N_S} = \frac{\qty{45}{\volt}}{\qty{180}{\volt}}$

Questo si semplifica in:

$ \frac{150}{N_S} =0,25 $

Moltiplichiamo nuovamente entrambi i lati per $N_S$ e dividiamo entrambi i lati per 0,25.

$ N_S= \frac{150}{0,25} = 600$