Dans la classe E, nous avons déjà abordé les convertisseurs et les transverters, qui sont utilisés en radioamateurisme pour exploiter, avec des émetteurs-récepteurs existants, des bandes de fréquences supplémentaires que ces appareils ne couvrent pas à l’origine. Comme le montre la figure [ref:a_konverter_2], cela nécessite un oscillateur, un mélangeur et un filtre de bande.

[question:AF301]

Un problème lié à cela, que nous allons approfondir, est que les bandes de radioamateurisme ont des largeurs différentes. Par exemple, la bande des $\qty{70}{\centi\meter}$, de $\qtyrange{430}{440}{\mega\hertz}$, avec une largeur de $\qty{10}{\mega\hertz}$, est bien plus large que la bande des $\qty{10}{\meter}$, de $\qtyrange{28}{29,7}{\mega\hertz}$, avec une largeur de $\qty{1,7}{\mega\hertz}$. Il en résulte qu’un convertisseur qui transpose la plage de fréquences de $\qtyrange{430}{440}{\mega\hertz}$ vers la plage de $\qtyrange{28}{30}{\mega\hertz}$ ne peut pas couvrir toute la bande passante de la bande des $\qty{70}{\centi\meter}$.

<margin>
[picture:651:a_konverter_2:Convertisseur monté pour QO-100]
</margin>

---

C’est pourquoi un convertisseur doit parfois être commutable, comme le montre la figure [ref:a_konverter], afin de pouvoir couvrir des bandes de fréquences plus larges. Si l’on souhaite transposer une plage de fréquences de $\qtyrange{436}{440}{\mega\hertz}$, soit une bande passante de $\qty{4}{\mega\hertz}$, vers une plage de $\qtyrange{28}{30}{\mega\hertz}$ avec $\qty{2}{\mega\hertz}$ (en supposant que la fréquence de l’oscillateur se situe en dessous du signal utile), il faut deux plages de fréquences commutables : la première de $\qtyrange{436}{438}{\mega\hertz}$ et la seconde de $\qtyrange{438}{440}{\mega\hertz}$.

<margin>
[picture:85:a_konverter:Convertisseur avec commutation de la fréquence de l’oscillateur]
</margin>

Pour la première plage partielle de $\qtyrange{436}{438}{\mega\hertz}$, on peut calculer la fréquence de l’oscillateur comme suit :

$f_\mathrm{OSC} = \qty{436}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{408}{\mega\hertz}$

$f_\mathrm{OSC} = \qty{438}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{408}{\mega\hertz}$

Pour les deux limites de bande, on obtient logiquement une fréquence d’oscillateur de $\qty{408}{\mega\hertz}$.

Pour la deuxième plage partielle de $\qtyrange{438}{440}{\mega\hertz}$, la fréquence de l’oscillateur est la suivante :

$f_\mathrm{OSC} = \qty{440}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{438}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{410}{\mega\hertz}$.

Si cette fréquence d’oscillateur est générée par multiplication de fréquence, il faut en tenir compte lors du calcul inverse pour déterminer la fréquence nécessaire de l’oscillateur à quartz.

Si les $\qty{408}{\mega\hertz}$ ou $\qty{410}{\mega\hertz}$ calculés précédemment sont obtenus par multiplication par neuf de la fréquence de l’oscillateur à quartz, les deux fréquences de l’oscillateur à quartz s’élèvent alors à $f_\mathrm{Quarz,1}=\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ et $f_\mathrm{Quarz,2}=\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (arrondies).

Avec ces informations, nous pouvons maintenant résoudre les exercices suivants.

[question:AF501]
[question:AF502]