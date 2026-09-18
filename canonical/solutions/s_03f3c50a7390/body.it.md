# Dati
* Frequenza del radiofaro: $f_\text{radiofaro} = \qty{144,4}{\mega\hertz}$
* Larghezza di banda SSB: $f_{B,max} = \qty{2,7}{\kilo\hertz}$
* Precisione: $\qty{1}{\ppm}$

# Considerazioni preliminari
La distanza ($f_\text{distanza}$) dalla frequenza del radiofaro ($f_\text{radiofaro}$) è data dalla somma della larghezza di banda SSB ($f_{B,max}$) e della distanza di sicurezza ($\Delta f$) dovuta all’imprecisione di $\qty{1}{\ppm}$. L’unità $\unit{ppm}$ sta per *parts per million*, quindi $\qty{1}{\ppm}$ significa $1$ su $10^6$. 

# Procedimento di soluzione
$\Delta f = \qty{144,4}{\mega\hertz} \cdot \frac{1}{10^6} = \frac{\qty{144,4 \cdot \cancel{10^6}}{\hertz}}{\cancel{10^6}} = \qty{144,4}{\hertz}= \qty{0,1444}{\kilo\hertz}$

$f_\text{distanza} = f_{B,max} + \Delta f = \qty{2,7}{\kilo\hertz} + \qty{0,1444}{\kilo\hertz} = \qty{2,8444}{\kilo\hertz}$