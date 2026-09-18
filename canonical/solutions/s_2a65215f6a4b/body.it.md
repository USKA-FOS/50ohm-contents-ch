La banda di frequenza da $\qtyrange{430}{434}{\mega\hertz}$ ha una larghezza di banda di $\qty{4}{\mega\hertz}$. Poiché il ricevitore collegato elabora solo la gamma da $\qtyrange{28}{30}{\mega\hertz}$, con una larghezza di banda di $\qty{2}{\mega\hertz}$, la banda di ricezione desiderata deve essere suddivisa in due sottobande:

* Sottobanda 1: $\qtyrange{430}{432}{\mega\hertz}$
* Sottobanda 2: $\qtyrange{432}{434}{\mega\hertz}$

Poiché la frequenza dell’oscillatore deve essere inferiore al segnale utile, per la miscelazione vale:

$f_\mathrm{IF} = f_\mathrm{HF} - f_\mathrm{OSZ}$

Per la prima sottobanda da $\qtyrange{430}{432}{\mega\hertz}$ si ottiene:

$f_\mathrm{OSZ} = \qty{430}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{402}{\mega\hertz}$

Anche al limite superiore della banda otteniamo:

$f_\mathrm{OSZ} = \qty{432}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{402}{\mega\hertz}$

Per la seconda sottobanda da $\qtyrange{432}{434}{\mega\hertz}$ si ottiene di conseguenza:

$f_\mathrm{OSZ} = \qty{432}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{404}{\mega\hertz}$

Anche al limite superiore della banda otteniamo:

$f_\mathrm{OSZ} = \qty{434}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{404}{\mega\hertz}$

Le frequenze dell’oscillatore necessarie sono quindi $\qty{402}{\mega\hertz}$ e $\qty{404}{\mega\hertz}$.

Poiché queste frequenze vengono generate moltiplicando per nove la frequenza dell’oscillatore a quarzo, devono essere divise per il fattore $\num{9}$:

$f_\mathrm{Quarz,1} = \frac{\qty{402}{\mega\hertz}}{9} \approx \qty{44,667}{\mega\hertz}$

$f_\mathrm{Quarz,2} = \frac{\qty{404}{\mega\hertz}}{9} \approx \qty{44,889}{\mega\hertz}$

L’oscillatore a quarzo deve quindi essere commutabile tra $\qty{44,667}{\mega\hertz}$ e $\qty{44,889}{\mega\hertz}$. 