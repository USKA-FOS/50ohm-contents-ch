La bande de fréquences $\qtyrange{430}{434}{\mega\hertz}$ présente une bande passante de $\qty{4}{\mega\hertz}$. Comme le récepteur connecté ne traite que la plage $\qtyrange{28}{30}{\mega\hertz}$, avec une bande passante de $\qty{2}{\mega\hertz}$, la plage de réception souhaitée doit être divisée en deux sous-plages :

* Sous-plage 1 : $\qtyrange{430}{432}{\mega\hertz}$
* Sous-plage 2 : $\qtyrange{432}{434}{\mega\hertz}$

Comme la fréquence de l’oscillateur doit être inférieure au signal utile, l’équation de mélange est :

$f_\mathrm{FI} = f_\mathrm{HF} - f_\mathrm{OSZ}$

Pour la première sous-plage $\qtyrange{430}{432}{\mega\hertz}$, on obtient :

$f_\mathrm{OSZ} = \qty{430}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{402}{\mega\hertz}$

À la limite supérieure de la bande, on obtient également :

$f_\mathrm{OSZ} = \qty{432}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{402}{\mega\hertz}$

Pour la deuxième sous-plage $\qtyrange{432}{434}{\mega\hertz}$, on obtient de même :

$f_\mathrm{OSZ} = \qty{432}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{404}{\mega\hertz}$

À la limite supérieure de la bande, on obtient également :

$f_\mathrm{OSZ} = \qty{434}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{404}{\mega\hertz}$

Les fréquences d’oscillateur nécessaires sont donc $\qty{402}{\mega\hertz}$ et $\qty{404}{\mega\hertz}$.

Comme ces fréquences sont générées par une multiplication par neuf de la fréquence de l’oscillateur à quartz, elles doivent être divisées par le facteur $\num{9}$ :

$f_\mathrm{Quarz,1} = \frac{\qty{402}{\mega\hertz}}{9} \approx \qty{44,667}{\mega\hertz}$

$f_\mathrm{Quarz,2} = \frac{\qty{404}{\mega\hertz}}{9} \approx \qty{44,889}{\mega\hertz}$

L’oscillateur à quartz doit donc pouvoir commuter entre $\qty{44,667}{\mega\hertz}$ et $\qty{44,889}{\mega\hertz}$.