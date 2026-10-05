Dans la section [sec:dezibel_1], nous avons déjà découvert le décibel comme outil pour décrire des rapports et vu qu'un changement de puissance de $\qty{3}{\dB}$ correspond à un facteur de puissance de $\num{2}$. Dans le recueil de formules, nous trouvons le tableau [ref:a_dezibel_leistungsfaktoren], qui contient d'autres correspondances importantes.

<margin>
| c:dB | c:≈ Facteur de puissance |
| $-20$ | $\num{0,01}$ |
| $-10$ | $\num{0,1}$ |
| $-6$ | $\num{0,25}$ |
| $-3$ | $\num{0,5}$ |
| $-1$ | $\num{0,79}$ |
| $0$ | $\num{1}$ |
| $1,5$ | $\sqrt{2} = \num{1,41}$ |
| $2,15$ | $\num{1,64}$ |
| $3$ | $\num{2}$ |
| $5$ | $\sqrt{10} = \num{3,16}$ |
| $6$ | $\num{4}$ |
| $10$ | $\num{10}$ |
| $20$ | $\num{100}$ |
[table:a_dezibel_leistungsfaktoren:Facteurs de puissance importants en $\unit{\dB}$]
</margin>

Le recueil de formules donne pour la conversion d'un rapport de puissance en $\unit{\dB}$ la formule suivante, que nous avons également apprise dans la classe E. Le rapport $g$ de deux puissances $P_1$ et $P_2$ en $\unit{\dB}$ est :

$g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$

[question:AD428]

Si l'on souhaite déterminer un facteur de rapport à partir d'une valeur en $\unit{\dB}$, la formule doit être réarrangée :

$\begin{align*} g &= 10 \cdot \log_{10}\left( x \right) \unit{\dB} & \quad\quad\quad &|: \qty{10}{\dB} \\ \frac{g}{\qty{10}{\dB}} &= \log_{10}\left( x \right) &~&| \quad 10^{x}\\ x &= 10^{\frac{g}{\qty{10}{\dB}}} &~&~\end{align*}$

Avec ces deux formules, nous pouvons donc facilement convertir entre les indications en $\unit{\dB}$ et les facteurs de rapport. Essayez maintenant de calculer les trois questions suivantes :

---

[question:AA105]
[question:AA106]
[question:AD426]

<tip>
Dans la section [sec:dezibel_1], nous avons déjà appris l'astuce suivante : sans calculatrice, on peut estimer les valeurs en décibels qui se terminent par "$0$" : il suffit de cacher le dernier zéro, le chiffre donne alors le nombre de zéros du facteur de rapport. Exemple : $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zéros} \rightarrow \text{facteur de rapport}~1000$ !

Cela peut aussi être facilement calculé dans l'autre sens : un avec $12$ zéros ($\num{1000000000000}$) en $\unit{\dB}$ est simplement le nombre de zéros, donc $12$, multiplié par $10$. Cela donne un facteur de gain de $\qty{120}{\dB}$.

Mais aussi pour les valeurs en $\unit{\dB}$ qui ne se terminent pas par $0$, on peut déterminer le facteur correspondant par décomposition :

* On peut décomposer $\qty{9}{\dB}$ en $\qty{6}{\dB} + \qty{3}{\dB}$, ce qui correspond à une multiplication de $4\cdot 2 = 8$.
  
* Quel facteur correspond à un rapport de puissance de $\qty{17}{\dB}$ ? $\qty{17}{\dB} = \qty{20}{\dB} - \qty{3}{\dB}$, donc facteur $100$ divisé par $2$ égal $50$.
</tip>

Le décibel ($\unit{\dB}$) décrit fondamentalement un rapport sans dimension, par exemple de puissances ou de tensions. C'est pourquoi $\unit{\dB}$ est principalement utilisé pour indiquer des gains et des atténuations. Dans ces cas, aucun suffixe supplémentaire n'est nécessaire, car seul le rapport de deux grandeurs est indiqué. Les valeurs négatives en décibels indiquent d'ailleurs des rapports inférieurs à $1$. Ainsi, $\qty{-3}{\dB}$ correspond à un rapport de $\frac{1}{2} = \num{0,5}$.

On peut aussi utiliser les valeurs en décibels pour indiquer un niveau absolu. Pour cela, cependant, une grandeur de référence fixe $P_0$ est requise :

$p = 10\cdot \log_{10}\left(\frac{P}{P_0}\right)\unit{\dB}$

---

Cette grandeur de référence peut être par exemple une puissance de $\qty{1}{\milli\watt}$. Dans ce cas, la valeur en décibel reçoit un suffixe correspondant : si le niveau se réfère à $\qty{1}{\milli\watt}$, on parle de $\unit{\dBm}$. Ainsi, il est clairement défini à quelle valeur de puissance absolue le niveau en décibel se réfère.

Si l'on rencontre par exemple l'indication « L'émetteur a une puissance de sortie de $\qty{20}{\dBm}$ », cette valeur peut facilement être convertie en milliwatts. Un niveau de $\qty{20}{\dB}$ correspond à un facteur de puissance de $100$ (donc deux zéros). Ce facteur est multiplié par la grandeur de référence de $\qty{1}{\milli\watt}$ :

$ P = 100 \cdot \qty{1}{\milli\watt} = \qty{100}{\milli\watt}$

Le tableau [ref:a_bezugsgroessen] liste les grandeurs de référence les plus importantes et leurs abréviations en $\unit{\dB}$ respectives.

<margin>
| l: Abréviation            | X: Valeur de référence          |
| $\unit{\dBm}$           | $\qty{1}{\milli\watt}$ | 
| $\unit{\dBW}$           | $\qty{1}{\watt}$       | 
| $\unit{\dBu}$           | $\qty{0,775}{\volt}$   | 
| $\unit{\dB\micro\volt}$ | $\qty{1}{\micro\volt}$ | 
[table:a_bezugsgroessen:Grandeurs de référence importantes du recueil de formules]
</margin>

Les questions suivantes peuvent être calculées à l'aide de la formule du recueil de formules et de sa réorganisation du début de cette leçon, si la bonne grandeur de référence est utilisée.

[question:AA109]
[question:AA110]
[question:AA107]
[question:AA108]

---

Pourquoi fait-on tout cela et indique-t-on des puissances absolues en $\unit{\dBm}$ et $\unit{\dBW}$ ? Comme déjà évoqué dans la classe E, l'utilisation du décibel sert principalement à simplifier les calculs. En représentant les gains et atténuations en décibels, des chaînes de signal complètes peuvent être facilement estimées par addition et soustraction, sans recourir à des multiplications et divisions compliquées.

La figure [ref:e_signalkette] montre une telle chaîne de signal avec trois étages amplificateurs. Le signal d'entrée a une puissance de $\qty{1}{\milli\watt}$, ce qui correspond à $\qty{0}{\dBm}$. À travers les trois étages amplificateurs, le signal est globalement amplifié à $\qty{60}{\dBm}$ (donc $\num{1000000}\cdot \qty{1}{\milli\watt}$), ce qui correspond à une puissance de $\qty{1000}{\watt}$.

La figure [ref:e_signalkette_2] montre un autre exemple de chaîne de signal, où un atténuateur avec une atténuation de $\qty{20}{\dB}$ est utilisé en plus, ce qui correspond à un gain de $\qty{-20}{\dB}$. Le signal d'entrée a une puissance de $\qty{1}{\milli\watt}$, donc $\qty{0}{\dBm}$. À travers le premier étage amplificateur, le signal est élevé à $\qty{10}{\dBm}$. Ensuite, il est affaibli par l'atténuateur à $\qty{-10}{\dBm}$ et finalement amplifié à nouveau par le deuxième étage amplificateur à $\qty{0}{\dBm}$, ce qui correspond à nouveau à $\qty{1}{\milli\watt}$.

<margin>
[picture:877:e_signalkette:Chaîne de signal avec trois amplificateurs]
[picture:1053:e_signalkette_2:Chaîne de signal avec deux amplificateurs et un atténuateur]
</margin>

<indepth>
Pourquoi est-il permis de soustraire une atténuation de $\qty{3}{\dB}$ du niveau $\qty{9}{\dBm}$ ? Les deux valeurs ont pourtant des unités différentes ! L'unité bel ($\unit{\bel}$) ou décibel ($\unit{\dB}$) est une unité auxiliaire (aussi appelée pseudo-unité).
En principe, la valeur numérique pourrait aussi être écrite sans l'unité $\unit{\dB}$. Mais avec le suffixe $\unit{\dB}$, il est clair qu'il s'agit d'un rapport logarithmique de deux grandeurs. Sans cette unité, il faudrait décrire verbalement la signification de la valeur numérique.
</indepth>

Pour déterminer le gain total d'un amplificateur de puissance à plusieurs étages, la différence entre la puissance de sortie et la puissance d'entrée doit être effectuée par soustraction correcte des valeurs en dBm. Exemple : puissance d'entrée $\qty{-5}{\dBm}$, puissance de sortie $\qty{20}{\dBm}$ donne un gain total de $\qty{25}{\dB}$ ($\qty{20}{\dBm} - (\qty{-5}{\dBm}) = \qty{25}{\dB}$)

[question:AF428]
  
De plus, nous avons déjà appris dans la classe E les suffixes $\unit{\dBd}$ et $\unit{\dBi}$, utilisés pour indiquer les gains d'antenne. Dans ce cas, la valeur en décibel ne se réfère pas à une puissance ou tension, mais à un radiateur de référence spécifique. Les plus courants sont $\unit{\dBi}$, référé au radiateur sphérique isotrope, et $\unit{\dBd}$, référé au dipôle demi-onde.

---

En plus des rapports de puissance, nous pouvons aussi utiliser le décibel pour indiquer des *rapports de tension* et des *niveaux de tension*. Pour cela, nous pouvons utiliser la formule $P = \frac{U^2}{R}$. Nous pouvons donc écrire :

$\begin{split}g &= 10 \cdot \log_{10}\left(\frac{P_1}{P_2}\right)\\ g &= 10 \cdot \log_{10}\left(\frac{\frac{U_1^2}{\cancel{R}}}{\frac{U_2^2}{\cancel{R}}}\right)\\ g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right) \end{split}$

<tip>
*Calcul avec les logarithmes :*
Quelques règles de calcul simples permettent de résoudre des problèmes de décibels sans calculatrice.

* Le logarithme d'un produit de deux nombres correspond à la somme des logarithmes : $\log_{10}(a\cdot b) = \log_{10}(a)+ \log_{10}(b)$
  
* Le logarithme d'une division de deux nombres correspond à la différence des logarithmes : $\log_{10}(a / b) = \log_{10}(a) - \log_{10}(b)$
  
* Le logarithme d'un nombre au carré : $\log_{10}(x^2)= 2 \cdot \log_{10}(x)$
  
* Le logarithme d'une racine : $\log_{10}(\sqrt{x})= \frac{1}{2} \cdot \log_{10}(x)$
</tip>

Mais le logarithme d'un nombre au carré est égal à deux fois le logarithme du nombre :

$\log_{10}(x^2)=2 \cdot \log_{10}(x)$

Il en découle :

$\begin{split} g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right)\\ g &= 10 \cdot 2 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \\ g &= 20 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \end{split}$

---

Par conséquent, nous calculons un rapport *$a$* de deux tensions $U_1$ et $U_2$ en multipliant le logarithme du rapport non pas par le facteur $10$, mais par le facteur $20$. Cette formule se trouve également dans le recueil de formules.

[question:AA111]
[question:AD427]

<attention>
Lors du calcul en décibels, toujours vérifier précisément s'il s'agit de rapports de puissance ou de tension !
</attention>

Pour déterminer des niveaux de tension, nous devons à nouveau d'abord fixer une tension de référence (cf. tableau [ref:a_bezugsgroessen]). Pour les signaux de réception, nous mesurons volontiers les tensions (très faibles) à l'entrée du récepteur en $\unit{\micro\volt}$. Le niveau de tension correspondant a alors l'unité $\unit{\dBuV}$. Exemple :

$\qty{10}{\micro\volt} \rightarrow 20 \cdot \log_{10}\left(\frac{\qty{10}{\micro\volt}}{\qty{1}{\micro\volt}}\right)=\qty{20}{\dBuV}$

---

Dans la question suivante, la valeur de référence est $\qty{1}{\micro\volt\per\meter}$. Essayez de résoudre l'exercice avec vos connaissances.

<attention>
Attention, ici $\unit{\dB(\micro\volt\per\meter)}$ est signifié et non $\unit{(\dB\micro\volt)/\meter}$ !
</attention>

[question:AA112]

<tip>
Avec les tensions aussi, on peut calculer beaucoup de choses mentalement à l'aide du tableau du recueil de formules :

| c:dB | c:≈ Rapport de tension |
| $-20$ | $\num{0,1}$ |
| $-10$ | $\num{0,32}$ |
| $-6$ | $\num{0,5}$ |
| $-3$ | $\num{0,71}$ |
| $-1$ | $\num{0,89}$ |
| $0$ | $\num{1}$ |
| $1$ | $\num{1,12}$ |
| $3$ | $\num{1,14}$ |
| $6$ | $2$ |
| $10$ | $3,16$ |
| $20$ | $10$ |
[table:a_spannungsverhaeltnisse:Rapports de tension importants en $\unit{\dB}$]

*Exemple :*

* Combien de $\unit{\dB}$ correspond à un rapport de tension de $4$ ? $4 = 2 \cdot 2 \rightarrow \qty{6}{\dB} + \qty{6}{\dB} = \qty{12}{\dB}$
</tip>
