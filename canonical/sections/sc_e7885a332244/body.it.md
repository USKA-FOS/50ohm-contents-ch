Nella sezione [sec:spannungsteiler_1] abbiamo già conosciuto il *partitore di tensione* *non caricato*. In questa sezione ci occupiamo del *partitore di tensione* *caricato*, in cui la tensione d’uscita $U_2$ è caricata da una resistenza di carico $R_\mathrm{L}$. Ciò significa che la resistenza di carico è in parallelo alla resistenza $R_2$, come si vede nello schema circuitale della figura [ref:a_spannungsteiler_belastet].

<margin>
[picture:199:a_spannungsteiler_belastet:Partitore di tensione caricato]
</margin>

In un partitore di tensione caricato bisogna considerare che la corrente totale aumenta quando il carico aumenta, cioè quando la resistenza di carico $R_\mathrm{L}$ diventa più bassa. Spieghiamo meglio gli effetti del carico con un esempio concreto. Supponiamo che le resistenze $R_1$ e $R_2$ abbiano ciascuna un valore di $\qty{1}{\kilo\ohm}$ e che la tensione totale $U_\mathrm{B}$ sia di $\qty{12}{\volt}$.

Nel caso non caricato, la resistenza $R_\mathrm{L}=\infty$, cioè la resistenza non esiste e non può fluire corrente attraverso di essa. La tensione si divide equamente tra le due resistenze $R_1$ e $R_2$, cioè su ciascuna resistenza si possono misurare $\qty{6}{\volt}$. La resistenza totale è $R_{\mathrm{ges}}=\qty{2}{\kilo\ohm}$. La corrente totale è $I_1 = \frac{U_\mathrm{B}}{R_{\mathrm{ges}}}=\qty{6}{\milli\ampere}$. Questa corrente scorre anche attraverso $R_2$. La potenza dissipata è uguale su entrambe le resistenze: $P_1 = P_2 = \qty{6}{\volt} \cdot \qty{6}{\milli\ampere} = \qty{36}{\milli\watt}$.

Nel caso caricato, supponiamo che anche la resistenza di carico sia $R_\mathrm{L} = \qty{1}{\kilo\ohm}$. Il collegamento in parallelo di $R_2$ e $R_\mathrm{L}$ dà una resistenza equivalente di $R_\mathrm{par}=\qty{500}{\ohm}$. La resistenza totale del partitore di tensione ora è solo $R_{\mathrm{ges}}=\qty{1,5}{\kilo\ohm}$. Ora agisce un partitore di tensione con $\qty{1}{\kilo\ohm}$ e $\qty{500}{\ohm}$ e di conseguenza la tensione totale si divide. $\frac{2}{3}$ della tensione totale ($\qty{8}{\volt}) si può misurare su $R_1$ e $\frac{1}{3}$ della tensione totale ($\qty{4}{\volt}) si può misurare su $R_\mathrm{par}$.

La corrente $I_1$ ora è $I_1 = \frac{\qty{8}{\volt}}{\qty{1}{\kilo\ohm}}= \frac{\qty{12}{\volt}}{\qty{1,5}{\kilo\ohm}} = \qty{8}{\milli\ampere}$. Questa corrente quindi aumenta.

La potenza su $R_1$ ora è $P_1 = U_1 \cdot I_1 = \qty{8}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{64}{\milli\watt}$ rispetto ai $\qty{36}{\milli\watt}$ del caso non caricato. Su $R_\mathrm{par}$ la potenza è $P_\mathrm{par} = U_\mathrm{par} \cdot I_\mathrm{par} = \qty{4}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{32}{\milli\watt}$ rispetto ai $\qty{36}{\milli\watt}$ del caso non caricato. Poiché i ${32}{\milli\watt}$ si dividono tra $R_2$ e $R_\mathrm{L}$, la potenza su $R_2$ nel caso caricato si riduce a $P_2 = \qty{4}{\volt} \cdot \qty{4}{\milli\ampere} = \qty{16}{\milli\watt}$.

In sintesi: Caricando un partitore di tensione con una resistenza, la corrente $I_1$ aumenta. Di conseguenza, $R_1$ si scalda di più e $R_2$ si scalda meno. Con questa conoscenza possiamo risolvere facilmente la prossima domanda.

[question:AD115]

Nella domanda seguente dobbiamo combinare la nostra conoscenza sul partitore di tensione e sul collegamento in parallelo delle resistenze. Per farlo, scomponiamo il compito in singoli passi: prima si determina la resistenza equivalente del collegamento in parallelo di $R_2$ e $R_\mathrm{L}$. Successivamente, il circuito può essere considerato come un semplice partitore di tensione e da esso si può calcolare la tensione d’uscita $U_2$.

[question:AD114]
