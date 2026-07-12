Per calcolare le frequenze dell'oscillatore necessarie nei transverter, è necessario conoscere le frequenze di ingresso e uscita desiderate. È inoltre necessaria l'informazione se l'oscillatore debba trovarsi al di sotto o al di sopra del segnale utile.

<indepth>
Se la frequenza dell'oscillatore si trova al di sotto del segnale utile, la posizione della banda laterale di un segnale SSB (USB/LSB) viene mantenuta.
Se la frequenza dell'oscillatore si trova al di sopra del segnale utile, la posizione della banda laterale di un segnale SSB viene invertita (da USB diventa LSB e viceversa).
</indepth>

Esempio di calcolo:

Se la frequenza dell'oscillatore si trova al di sotto del segnale utile, la frequenza più alta del segnale utile corrisponde anche alla frequenza più alta del segnale di uscita del convertitore/transverter.

Ad esempio, se si desidera convertire una banda di frequenza da $\qtyrange{438}{440}{\mega\hertz}$ in una banda di frequenza da $\qtyrange{28}{30}{\mega\hertz}$ (supponendo che la frequenza dell'oscillatore si trovi al di sotto del segnale utile), è necessaria una frequenza dell'oscillatore di $\qty{440}{\mega\hertz} - \qty{30}{\mega\hertz}$ o $\qty{438}{\mega\hertz} - \qty{28}{\mega\hertz}$, che in entrambi i casi risulta $\qty{410}{\mega\hertz}$. Se questa frequenza dell'oscillatore viene generata tramite moltiplicazione di frequenza, è necessario tenerne conto dividendo per il fattore di moltiplicazione per risalire alla frequenza richiesta dell'oscillatore a quarzo.

Lo stesso vale per la banda di frequenza da $\qtyrange{436}{438}{\mega\hertz}$, se questa deve essere convertita nuovamente in una banda di frequenza da $\qtyrange{28}{30}{\mega\hertz}$ (sempre supponendo che la frequenza dell'oscillatore si trovi al di sotto del segnale utile).
In questo caso, il calcolo $\qty{438}{\mega\hertz}$ - $\qty{30}{\mega\hertz}$ o $\qty{436}{\mega\hertz}$ - $\qty{28}{\mega\hertz}$ dà come risultato una frequenza dell'oscillatore di $\qty{408}{\mega\hertz}$.

Se i valori di $\qty{408}{\mega\hertz}$ o $\qty{410}{\mega\hertz}$ calcolati sopra vengono ottenuti moltiplicando per nove la frequenza dell'oscillatore al quarzo, le due frequenze dell'oscillatore al quarzo risultano $\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ e $\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (arrotondati rispettivamente).

[question:AF501]
[question:AF502]

%TODO: La domanda 1472 secondo noi non appartiene qui, poiché si tratta di un trasmettitore e questa domanda non ha nulla a che fare con convertitori o transverter. Potrebbe essere necessario spostarla nel capitolo Trasmettitori e stadi di trasmissione.
[question:AF301]