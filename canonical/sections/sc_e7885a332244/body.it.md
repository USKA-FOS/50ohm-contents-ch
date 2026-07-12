Nella classe E abbiamo già imparato il partitore di tensione *senza carico*. Nella classe A ci occupiamo del partitore di tensione *con carico*, in cui la tensione d'uscita $U_2$ è caricata da una resistenza di carico $R_L$. Ciò significa che la resistenza di carico è in parallelo alla resistenza $R_2$, come si vede nello schema elettrico della figura [ref:a_spannungsteiler_belastet].

<margin>
[picture:199:a_spannungsteiler_belastet:belasteter Spannungsteiler]
</margin>

Con un partitore di tensione con carico, si deve tenere conto del fatto che la corrente totale aumenta se il carico viene aumentato, cioè se la resistenza di carico $R_L$ diventa a bassa impedenza. È meglio spiegare gli effetti del carico con un esempio concreto. Supponiamo che le resistenze $R_1$ e $R_2$ abbiano ciascuna un valore di $\qty{1}{\kilo\ohm}$ e che la tensione totale $U_B$ sia $\qty{12}{\volt}$.

Nel caso senza carico, la resistenza $R_\mathrm{L}=\infty$, quindi la resistenza non esiste e nessuna corrente può fluire attraverso di essa. La tensione si divide uniformemente tra le due resistenze $R_1$ e $R_2$, cioè si possono misurare $\qty{6}{\volt}$ su ciascuna resistenza. La resistenza totale è $R_{\mathrm{ges}}=\qty{2}{\kilo\ohm}$. La corrente totale è $I_1 = \frac{U_B}{R_{\mathrm{ges}}}=\qty{6}{\milli\ampere}$. Questa corrente scorre anche attraverso $R_2$. La potenza dissipata è uguale su entrambe le resistenze: $P_1 = P_2 = \qty{6}{\volt} \cdot \
\qty{6}{\milli\ampere} = \qty{36}{\milli\watt}$.

Nel caso con carico, la resistenza di carico dovrebbe ora essere anche $R_L = \qty{1}{\kilo\ohm}$. La connessione in parallelo di $R_2$ e $R_L$ produce una resistenza equivalente di $R_\mathrm{par}=\qty{500}{\ohm}$. La resistenza totale del partitore di tensione è ora solo $R_{\mathrm{ges}}=\qty{1,5}{\kilo\ohm}$. Ora un partitore di tensione con $\qty{1}{\kilo\ohm}$ contro $\qty{500}{\ohm}$ agisce e di conseguenza la tensione totale si divide. $\frac{2}{3}$ della tensione totale ($\qty{8}{\volt}$) può essere misurata su $R_1$ e $\frac{1}{3}$ della tensione totale ($\qty{4}{\volt}$) può essere misurata su $R_\mathrm{par}$. 

La corrente $I_1$ è ora $I_1 = \frac{\qty{8}{\volt}}{\qty{1}{\kilo\ohm}}= \frac{\qty{12}{\volt}}{\qty{1,5}{\kilo\ohm}} = \qty{8}{\milli\ampere}$. Questa corrente quindi aumenta. 

La potenza su $R_1$ è ora $P_1 = U_1 \cdot I_1 = \qty{8}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{64}{\milli\watt}$ rispetto a $\qty{36}{\milli\watt}$ nel caso senza carico. Su $R_\mathrm{par}$ la potenza è $P_\mathrm{par} = U_\mathrm{par} \cdot I_\mathrm{par} = \qty{4}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{32}{\milli\watt}$ rispetto a $\qty{36}{\milli\watt}$ nel caso senza carico, poiché la potenza si divide tra $R_2$ e $R_L$.

In sintesi: quando si carica un partitore di tensione con una resistenza, la corrente $I_1$ aumenta. Di conseguenza, $R_1$ si scalda e $R_2$ si scalda meno. Con queste conoscenze, possiamo risolvere facilmente la domanda successiva.

[question:AD115]

Nella domanda seguente dobbiamo combinare la nostra conoscenza del partitore di tensione e della connessione in parallelo delle resistenze. Per fare ciò, scomponiamo il compito in singoli passaggi: prima viene determinata la resistenza equivalente della connessione in parallelo di $R_2$ e $R_L$. Successivamente, il circuito può essere considerato come un semplice partitore di tensione e la tensione d'uscita $U_2$ può essere calcolata da esso.

[question:AD114]





