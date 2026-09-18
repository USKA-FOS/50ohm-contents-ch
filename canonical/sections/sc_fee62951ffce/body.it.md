Nella classe E abbiamo già incontrato i convertitori e i transverter, utilizzati nel radioamatoriale per estendere con bande di frequenza aggiuntive i limiti dei dispositivi esistenti. Come mostrato nella figura [ref:a_konverter_2], per questo scopo sono necessari un oscillatore, un mixer e un filtro di banda.

[question:AF301]

Un problema che affronteremo ora in modo approfondito riguarda il fatto che le bande radioamatoriali hanno larghezze diverse. Ad esempio, la banda dei $\qty{70}{\centi\meter}$, da $\qtyrange{430}{440}{\mega\hertz}$ con una larghezza di $\qty{10}{\mega\hertz}$, è molto più ampia rispetto alla banda dei $\qty{10}{\meter}$, da $\qtyrange{28}{29,7}{\mega\hertz}$ con una larghezza di $\qty{1,7}{\mega\hertz}$. Di conseguenza, un convertitore che trasla la banda $\qtyrange{430}{440}{\mega\hertz}$ nella banda $\qtyrange{28}{30}{\mega\hertz}$ non può coprire l’intera larghezza di banda della banda dei $\qty{70}{\centi\meter}$.


<margin>
[picture:651:a_konverter_2:Up-Convertitore per QO-100]
</margin>

---

Per questo motivo, un convertitore potrebbe dover essere commutabile, come mostrato nella figura [ref:a_konverter], per poter coprire bande di frequenza più ampie. Se, ad esempio, si vuole traslare una banda da $\qtyrange{436}{440}{\mega\hertz}$, cioè con una larghezza di $\qty{4}{\mega\hertz}$, in una banda da $\qtyrange{28}{30}{\mega\hertz}$ con $\qty{2}{\mega\hertz}$ (ammettendo che la frequenza dell’oscillatore sia inferiore al segnale utile), sono necessarie due bande commutabili: la prima da $\qtyrange{436}{438}{\mega\hertz}$ e la seconda da $\qtyrange{438}{440}{\mega\hertz}$.


<margin>
[picture:85:a_konverter:Convertitore con commutazione della frequenza dell’oscillatore]
</margin>

Per la prima sottobanda da $\qtyrange{436}{438}{\mega\hertz}$, la frequenza dell’oscillatore può essere calcolata come:


$f_\mathrm{OSC} = \qty{436}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{408}{\mega\hertz}$


$f_\mathrm{OSC} = \qty{438}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{408}{\mega\hertz}$


Per entrambi i limiti di banda si ottiene ovviamente una frequenza dell’oscillatore di $\qty{408}{\mega\hertz}$.


Per la seconda sottobanda da $\qtyrange{438}{440}{\mega\hertz}$, la frequenza dell’oscillatore risulta:


$f_\mathrm{OSC} = \qty{440}{\mega\hertz} - \qty{30}{\meta\hertz} = \qty{438}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{410}{\mega\hertz}$.


Se questa frequenza dell’oscillatore viene generata tramite moltiplicazione di frequenza, occorre tenerne conto nella retrocalcolazione della frequenza necessaria per l’oscillatore al quarzo, dividendo per il fattore di moltiplicazione.


Se le frequenze dell’oscillatore di $\qty{408}{\mega\hertz}$ e $\qty{410}{\mega\hertz}$ vengono ottenute moltiplicando per nove la frequenza dell’oscillatore al quarzo, le due frequenze dell’oscillatore al quarzo risultano essere $f_\mathrm{Quarzo,1}=\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ e $f_\mathrm{Quarzo,2}=\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (arrotondate).


Con queste informazioni possiamo ora affrontare i seguenti esercizi.


[question:AF501]
[question:AF502]