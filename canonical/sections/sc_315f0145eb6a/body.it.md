Il circuito a ponte è un arrangiamento di quattro resistenze, utilizzato tra l'altro per la misurazione precisa di resistenze. Un esempio pratico noto è il ponte di Wheatstone. Il circuito è composto da due partitori di tensione collegati in parallelo. Tra i punti medi dei due partitori si trova il cosiddetto ramo del ponte, in cui può essere misurata la tensione di ponte $U_\mathrm{AB}$.

<margin>
[picture:343:a_Brückenschaltung:Circuito a ponte tipico con 4 resistenze]
</margin>

Particolarmente interessante è il caso del ponte bilanciato. Questo si verifica quando i rapporti dei partitori di tensione su entrambi i lati sono uguali. In tal caso, i due punti medi possiedono lo stesso potenziale elettrico e non scorre corrente attraverso il ramo del ponte o lo strumento di misura collegato.

I singoli valori delle resistenze non devono necessariamente essere uguali. È fondamentale che il rapporto tra le resistenze su entrambi i lati sia identico.

Per lo stato bilanciato vale quindi:

$ U_\mathrm{AB} = \qty{0}{\volt} $

e di conseguenza:

$ \frac{R_1}{R_2} = \frac{R_3}{R_4} $

Il ponte di Wheatstone è quindi particolarmente adatto per determinare resistenze sconosciute o piccole variazioni di resistenza. Come funziona esattamente è descritto nell'approfondimento accanto.

<indepth>
Il caso speciale in cui i rapporti dei partitori di tensione nel circuito a ponte sono uguali a sinistra e a destra viene applicato per la misurazione di resistenze sconosciute. Charles Wheatstone (fisico britannico) riconobbe già nel 1833 l'importanza del circuito a ponte per la misurazione di resistenze sconosciute.

Nella misurazione, una resistenza di precisione regolabile viene modificata finché il sensibile strumento di misura nel ramo del ponte non indica più passaggio di corrente. A questo punto il ponte è bilanciato e si può determinare il valore della resistenza sconosciuta tramite la scala e il moltiplicatore.

Un esempio è visibile nell'immagine [ref:a_pontavi]. Qui è presente un moltiplicatore che può assumere valori di 0,1/1/10/100. Per la regolazione fine è presente la grande manopola.
[photo:286:a_pontavi:Circuito di misura delle resistenze secondo Wheatstone (Pontavi)]

L'immagine [ref:a_pontavi_schaltung] mostra lo schema elettrico semplificato di questo strumento di misura. Nel punto $X$ viene collegata la resistenza sconosciuta. Inizialmente, con il moltiplicatore si imposta l'ordine di grandezza stimato della resistenza sconosciuta. Poi, con la grande manopola, la resistenza di precisione viene modificata finché il ponte non è bilanciato. Lo strumento di misura indica quindi che non scorre più corrente nel ramo del ponte.

[picture:1076:a_pontavi_schaltung:Schema elettrico del circuito di misura delle resistenze (Pontavi)]
</indepth>

[question:AD111]

Poiché nella seguente esercitazione tutte le resistenze sono di uguale valore, anche i rapporti dei partitori di tensione devono essere uguali. Questo corrisponde al caso speciale descritto.

[question:AD112]

Nella domanda successiva il caso speciale non si verifica, poiché i rapporti dei partitori di tensione sono diversi. Sebbene siano presenti resistenze simili, sono disposte in modo invertito dall'alto verso il basso. L'esercizio può essere risolto con le conoscenze relative al partitore di tensione non caricato.

[question:AD113]

Sul lato sinistro troviamo il rapporto $\qty{1}{\kilo\ohm}$ a $\qty{10}{\kilo\ohm} = 1/10$.
Supponendo che lo strumento di misura sia molto altoohmico o scollegato, misuriamo con una tensione di servizio di $\qty{11}{\volt}$ sul lato sinistro sulla resistenza superiore ($R_1$) esattamente $\qty{1}{\volt}$ e sulla resistenza inferiore ($R_2$) $\qty{10}{\volt}$. Il potenziale nel punto di misura A è quindi di $\qty{10}{\volt}$ rispetto a massa.

Sul lato destro troviamo il rapporto $\qty{10}{\kilo\ohm}$ a $\qty{1}{\kilo\ohm} = 10/1$ e misuriamo quindi $\qty{10}{\volt}$ sulla resistenza superiore ($R_3$) e $\qty{1}{\volt}$ sulla resistenza inferiore ($R_4$). Il potenziale nel punto di misura B è quindi di $\qty{1}{\volt}$ rispetto a massa.

La differenza di potenziale tra A e B è quindi di $\qty{9}{\volt}$, con il punto di misura A positivo di $\qty{9}{\volt}$ rispetto al punto di misura B.