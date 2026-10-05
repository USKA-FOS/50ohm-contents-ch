Nella sezione [sec:transverter_1] abbiamo già conosciuto convertitori e transverter, che in ambito radioamatoriale vengono utilizzati per accedere a ulteriori bande di frequenza con apparecchiature radio esistenti, che originariamente non coprono queste gamme. Come mostrato nella figura [ref:a_konverter_2], per questo sono necessari un oscillatore, un mixer e un filtro di banda.

[question:AF301]

Un problema che ora approfondiremo è che le bande radioamatoriali hanno larghezze diverse. Ad esempio, la banda dei $\qty{70}{\centi\meter}$ da $\qtyrange{430}{440}{\mega\hertz}$ con una larghezza di $\qty{10}{\mega\hertz}$ è significativamente più ampia della banda dei $\qty{10}{\meter}$ da $\qtyrange{28}{29,7}{\mega\hertz}$ con una larghezza di $\qty{1,7}{\mega\hertz}$. Di conseguenza, un convertitore che trasforma la banda di frequenza da $\qtyrange{430}{440}{\mega\hertz}$ nella banda di frequenza da $\qtyrange{28}{30}{\mega\hertz}$ non può coprire l'intera larghezza di banda della banda dei $\qty{70}{\centi\meter}$.

<margin>
[picture:651:a_konverter_2:Up-converter per QO-100]
</margin>

---

Pertanto, un convertitore potrebbe dover essere commutabile, come mostrato nella figura [ref:a_konverter], per poter mappare gamme di frequenza più ampie. Ad esempio, se si desidera convertire una banda di frequenza da $\qtyrange{436}{440}{\mega\hertz}$, cioè una larghezza di banda di $\qty{4}{\mega\hertz}$, in una banda di frequenza da $\qtyrange{28}{30}{\mega\hertz}$ con $\qty{2}{\mega\hertz}$ (assumendo che la frequenza dell’oscillatore si trovi al di sotto del segnale utile), sono necessarie due gamme di frequenza commutabili: la prima da $\qtyrange{436}{438}{\mega\hertz}$ e la seconda da $\qtyrange{438}{440}{\mega\hertz}$.

<margin>
[picture:85:a_konverter:Convertitore con commutazione della frequenza dell’oscillatore]
</margin>

Per la prima sottobanda da $\qtyrange{436}{438}{\mega\hertz}$ si può calcolare la seguente frequenza dell’oscillatore:

$f_\mathrm{OSZ} = \qty{436}{\mega\hertz}$ - $\qty{28}{\mega\hertz} = \qty{408}{\mega\hertz}$

$f_\mathrm{OSZ} = \qty{438}{\mega\hertz}$ - $\qty{30}{\mega\hertz} = \qty{408}{\mega\hertz}$

Per entrambi i limiti della banda si ottiene logicamente una frequenza dell’oscillatore di $\qty{408}{\mega\hertz}$.

Per la seconda sottobanda da $\qtyrange{438}{440}{\mega\hertz}$ si ottiene la seguente frequenza dell’oscillatore:

$f_\mathrm{OSZ} = \qty{440}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{438}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{410}{\mega\hertz}$.

Se questa frequenza dell’oscillatore viene generata mediante moltiplicazione di frequenza, nella riconversione alla frequenza richiesta dell'oscillatore al quarzo è necessario considerare la divisione.

Se i $\qty{408}{\mega\hertz}$ o $\qty{410}{\mega\hertz}$ calcolati sopra vengono ottenuti moltiplicando per nove la frequenza dell'oscillatore al quarzo, le due frequenze dell'oscillatore al quarzo risultano essere $f_\mathrm{Quarz,1}=\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ e $f_\mathrm{Quarz,2}=\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (ciascuna arrotondata).

Con questa conoscenza possiamo ora affrontare i seguenti esercizi.

[question:AF501]
[question:AF502]
