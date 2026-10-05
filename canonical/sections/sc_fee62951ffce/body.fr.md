Dans la section [sec:transverter_1], nous avons déjà découvert les convertisseurs et transverters, qui sont utilisés en radioamateurisme pour étendre les bandes de fréquences accessibles avec des équipements existants, au-delà de leurs capacités d'origine. Comme illustré dans la figure [ref:a_konverter_2], cela nécessite un oscillateur, un mélangeur et un filtre de bande.  

[question:AF301]

Un problème que nous souhaitons approfondir ici est que les bandes radioamateurs ont des largeurs différentes. Par exemple, la bande des $\qty{70}{\centi\meter}$ de $\qtyrange{430}{440}{\mega\hertz}$, avec une largeur de $\qty{10}{\mega\hertz}$, est nettement plus large que la bande des $\qty{10}{\meter}$ de $\qtyrange{28}{29,7}{\mega\hertz}$, avec une largeur de $\qty{1,7}{\mega\hertz}$. En conséquence, un convertisseur qui transpose la bande de fréquences de $\qtyrange{430}{440}{\mega\hertz}$ vers la bande de $\qtyrange{28}{30}{\mega\hertz}$ ne peut pas couvrir toute la bande passante de la bande des $\qty{70}{\centi\meter}$.

<margin>
[picture:651:a_konverter_2:Convertisseur ascendant pour QO-100]
</margin>

---

C'est pourquoi un convertisseur doit parfois être commuté, comme illustré dans la figure [ref:a_konverter], pour pouvoir mapper des bandes de fréquences plus larges. Par exemple, pour convertir une bande de fréquences de $\qtyrange{436}{440}{\mega\hertz}$, soit une bande passante de $\qty{4}{\mega\hertz}$, vers une bande de $\qtyrange{28}{30}{\mega\hertz}$ avec $\qty{2}{\mega\hertz}$ (en supposant que la fréquence de l’oscillateur se situe en dessous du signal utile), deux plages de fréquences commutables sont nécessaires : la première de $\qtyrange{436}{438}{\mega\hertz}$ et la seconde de $\qtyrange{438}{440}{\mega\hertz}$. 

<margin>
[picture:85:a_konverter:Convertisseur avec commutation de la fréquence de l’oscillateur]
</margin>

Pour la première sous-plage de $\qtyrange{436}{438}{\mega\hertz}$, la fréquence de l’oscillateur peut être calculée comme suit : 

$f_\mathrm{OSZ} = \qty{436}{\mega\hertz}$ - $\qty{28}{\mega\hertz} = \qty{408}{\mega\hertz}$

$f_\mathrm{OSZ} = \qty{438}{\mega\hertz}$ - $\qty{30}{\mega\hertz} = \qty{408}{\mega\hertz}$

Logiquement, pour les deux limites de la bande, on obtient une fréquence de l’oscillateur de $\qty{408}{\mega\hertz}$.

Pour la seconde sous-plage de $\qtyrange{438}{440}{\mega\hertz}$, la fréquence de l’oscillateur est :

$f_\mathrm{OSZ} = \qty{440}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{438}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{410}{\mega\hertz}$.

Si cette fréquence de l’oscillateur est générée par multiplication de fréquence, il faut en tenir compte lors du calcul inverse de la fréquence requise de l’oscillateur à quartz en la divisant.

Si les $\qty{408}{\mega\hertz}$ ou $\qty{410}{\mega\hertz}$ calculés ci-dessus sont obtenus par multiplication par neuf de la fréquence de l’oscillateur à quartz, les deux fréquences de l’oscillateur à quartz sont : $f_\mathrm{Quarz,1}=\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ et $f_\mathrm{Quarz,2}=\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (arrondies respectivement).

Avec ces connaissances, nous pouvons maintenant traiter les exercices suivants.

[question:AF501]
[question:AF502]
