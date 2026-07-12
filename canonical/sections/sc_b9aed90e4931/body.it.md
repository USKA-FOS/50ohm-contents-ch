Perché esiste una rete di tensione alternata da $\qty{230}{\volt}$? La tensione alternata offre un vantaggio decisivo rispetto alla corrente continua: può essere convertita in altri valori di tensione in modo semplice e con basse perdite utilizzando trasformatori. Ciò consente un adattamento efficiente della tensione per la trasmissione e l'utilizzo.

Grazie all'autoinduzione nelle bobine, l'energia può essere trasferita con tensione alternata tra due bobine, come mostrato nella figura [ref:e_netztrafo]. Si crea un nuovo componente, il *trasmettitore* o *trasformatore*, in breve *trafo*. È costituito da due bobine accoppiate magneticamente tramite un nucleo di ferro o ferrite. Affinché i lati possano essere distinti, si parla di lato primario con il numero di spire $N_P$ e lato secondario con il numero di spire $N_S$.

<margin>
[picture:1017:e_netztrafo:Schema elettrico trasformatore]
</margin>

<margin>
[photo:239:e_Trafo mit getrennten Wicklungen:Trafo con avvolgimenti visibilmente separati]
</margin>

Un trasformatore serve a convertire un'alta tensione alternata, ad esempio $\qty{230}{\volt}$, in una tensione alternata più bassa, ad esempio $\qty{13,8}{\volt}$. Un trasformatore può trasmettere solo tensioni alternate. Se si applica in modo errato una tensione continua a un trasformatore, questo si comporta a causa della bassa resistenza ohmica dell'avvolgimento primario come un cortocircuito. Il trasformatore può quindi surriscaldarsi notevolmente e, nel peggiore dei casi, bruciarsi.

---

Il rapporto di trasformazione di un trasformatore può essere indicato come segue:

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Il rapporto tra il numero di spire corrisponde quindi al rapporto tra le tensioni. Riorganizzando questa equazione fondamentale, è possibile calcolare sia le tensioni $U$ che il numero di spire $N$ sul lato primario o secondario.

<indepth>
Queste relazioni valgono per il caso ideale di un trasformatore non caricato, cioè per il cosiddetto caso a vuoto. Vuoto significa che nessun carico è collegato al lato secondario.
</indepth>

[question:EC401]

Calcoliamo:

$\begin{align*}ü = \frac{15}{1} = 15 &= \frac{\qty{230}{\volt}}{U_S} &\quad\quad\quad &|~\cdot~U_S\\[1.5ex]15 \cdot U_S &= \qty{230}{\volt} &\quad\quad\quad &|~:~15\\[1.5ex]U_S &= \frac{\qty{230}{\volt}}{15} = \qty{15,33}{\volt}\end{align*}$

[question:EC402]

Innanzitutto, stabiliamo che $N_P = 5\cdot N_S$ e che $U_P = \qty{230}{\volt}$ sono dati. Si cerca nuovamente la tensione $U_S$.

$ü = \frac{5\cdot N_S}{N_S} = \frac{\qty{230}{\volt}}{U_S}$ 

Le $N_S$ si semplificano, quindi rimane solo:

$ü = 5 = \frac{\qty{230}{\volt}}{U_S}$ 

Moltiplichiamo entrambi i lati per $U_S$ e dividiamo entrambi i lati per 5.

$U_S = \frac{\qty{230}{\volt}}{5}$ 

Nella domanda successiva viene cercato il numero di spire secondarie.

[question:EC403]

Dati $N_P=600$, $U_P=\qty{230}{\volt}$ e $U_S=\qty{11,5}{\volt}$. Si cerca $N_S$.

$\frac{600}{N_S} = \frac{\qty{230}{\volt}}{\qty{11,5}{\volt}}$ 

Questo si semplifica in:

$\frac{600}{N_S} = 20$ 

Moltiplichiamo entrambi i lati per $N_S$ e dividiamo entrambi i lati per $20$.

$N_S = \frac{600}{20} = 30$

Il seguente trasformatore aumenta la tensione di uscita $U_S$, quindi il numero di spire secondarie deve essere maggiore del numero di spire primarie.

[question:EC404]

Dati $N_P= 150$, $U_P=\qty{45}{\volt}$ e $U_S=\qty{180}{\volt}$. Si cerca $N_S$.

Inseriamo i valori:

$ \frac{150}{N_S} = \frac{\qty{45}{\volt}}{\qty{180}{\volt}}$

Questo si semplifica in

$ \frac{150}{N_S} =0,25 $

Moltiplichiamo nuovamente entrambi i lati per $N_S$ e dividiamo entrambi i lati per $0,25$.

$ N_S= \frac{150}{0,25} = 600$