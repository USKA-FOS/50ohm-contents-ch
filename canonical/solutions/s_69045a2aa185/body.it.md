La banda di frequenza da $\qtyrange{436}{440}{\mega\hertz}$ ha una larghezza di banda di $\qty{4}{\mega\hertz}$. Poiché il ricevitore collegato elabora solo la gamma da $\qtyrange{28}{30}{\mega\hertz}$, con una larghezza di banda di $\qty{2}{\mega\hertz}$, la banda di ricezione desiderata deve essere suddivisa in due sottobande:


* Sottobanda 1: $\qtyrange{436}{438}{\mega\hertz}$
* Sottobanda 2: $\qtyrange{438}{440}{\mega\hertz}$


Poiché la frequenza dell’oscillatore deve essere inferiore al segnale utile, per la miscelazione vale:


$f_\mathrm{IF} = f_\mathrm{HF} - f_\mathrm{OSZ}$


Per la prima sottobanda $\qtyrange{436}{438}{\mega\hertz}$ si ottiene:


$f_\mathrm{OSZ} = \qty{436}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{408}{\mega\hertz}$


Anche al limite superiore della banda si ottiene:


$f_\mathrm{OSZ} = \qty{438}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{408}{\mega\hertz}$


Per la seconda sottobanda $\qtyrange{438}{440}{\mega\hertz}$ si ottiene di conseguenza:


$f_\mathrm{OSZ} = \qty{438}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{410}{\mega\hertz}$


Anche al limite superiore della banda si ottiene:


$f_\mathrm{OSZ} = \qty{440}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{410}{\mega\hertz}$


Le frequenze dell’oscillatore necessarie sono quindi $\qty{408}{\mega\hertz}$ e $\qty{410}{\mega\hertz}$.


Poiché queste frequenze vengono generate moltiplicando per nove la frequenza dell’oscillatore a quarzo, devono essere divise per il fattore $\num{9}$:


$f_\mathrm{Quarzo,1} = \frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$


$f_\mathrm{Quarzo,2} = \frac{\qty{410}{\mega\hertz}}{9} \approx \qty{45,556}{\mega\hertz}$


L’oscillatore a quarzo deve quindi essere commutabile tra $\qty{45,333}{\mega\hertz}$ e $\qty{45,556}{\mega\hertz}$.