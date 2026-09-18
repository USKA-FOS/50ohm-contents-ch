La bande de fréquences de $\qtyrange{436}{440}{\mega\hertz}$ possède une bande passante de $\qty{4}{\mega\hertz}$. Comme le récepteur connecté ne traite que la plage de $\qtyrange{28}{30}{\mega\hertz}$, soit une bande passante de $\qty{2}{\mega\hertz}$, la plage de réception souhaitée doit être divisée en deux sous-plages :

* Sous-plage 1 : $\qtyrange{436}{438}{\mega\hertz}$
* Sous-plage 2 : $\qtyrange{438}{440}{\mega\hertz}$

Comme la fréquence de l’oscillateur doit être inférieure au signal utile, l’équation de mélange est :

$f_\mathrm{FI} = f_\mathrm{HF} - f_\mathrm{OSZ}$

Pour la première sous-plage de $\qtyrange{436}{438}{\mega\hertz}$, on obtient :

$f_\mathrm{OSZ} = \qty{436}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{408}{\mega\hertz}$

À la limite supérieure de la bande, on obtient également :

$f_\mathrm{OSZ} = \qty{438}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{408}{\mega\hertz}$

Pour la deuxième sous-plage de $\qtyrange{438}{440}{\mega\hertz}$, on obtient de même :

$f_\mathrm{OSZ} = \qty{438}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{410}{\mega\hertz}$

À la limite supérieure de la bande, on obtient également :

$f_\mathrm{OSZ} = \qty{440}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{410}{\mega\hertz}$

Les fréquences d’oscillateur requises sont donc de $\qty{408}{\mega\hertz}$ et $\qty{410}{\mega\hertz}$.

Comme ces fréquences sont générées par une multiplication par neuf de la fréquence de l’oscillateur à quartz, elles doivent être divisées par le facteur $\num{9}$ :

$f_\mathrm{Quartz,1} = \frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$

$f_\mathrm{Quartz,2} = \frac{\qty{410}{\mega\hertz}}{9} \approx \qty{45,556}{\mega\hertz}$

L’oscillateur à quartz doit donc pouvoir commuter entre $\qty{45,333}{\mega\hertz}$ et $\qty{45,556}{\mega\hertz}$.