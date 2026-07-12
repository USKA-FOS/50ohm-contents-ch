En radioamateur, nous avons souvent affaire à des nombres très grands et très petits. L'unité de la fréquence – le hertz (\unit{\hertz}) – ainsi que les préfixes typiques pour les grands nombres comme *Kilo* (\unit{\kilo}), *Mega* (\unit{\mega}) et *Giga* (\unit{\giga}) nous sont déjà familiers.

Il existe également des préfixes pour les petits nombres. Par exemple, *Milli*, abrégé en \unit{\milli}. Un millimètre correspond à un millième de mètre, soit \qty{0,001}{\meter}. Les préfixes les plus utilisés pour les grands et les petits nombres sont présentés dans le tableau [ref:e_einheitenvorzeichen].

<margin>
| c: Préfixe | c: Abréviation | l: Valeur |
| Pico | \unit{\pico} | $10^{-12} = 0,000000000001$ |
| Nano | \unit{\nano} | $10^{-9} = 0,000000001$ |
| Micro | \unit{\micro} | $10^{-6} = 0,000001$ |
| Milli | \unit{\milli} | $10^{-3} = 0,001$ |
| |  | $10^{0} = 1$ |
| Kilo | \unit{\kilo} | $10^{3} = 1000$ |
| Mega | \unit{\mega} | $10^{6} = 1000000$ |
| Giga | \unit{\giga} | $10^{9} = 1000000000$ |
[table:e_einheitenvorzeichen:Préfixes d'unités pour les puissances de dix]
</margin>

Outre les unités hertz et mètre, que nous avons déjà rencontrées, il existe de nombreuses autres unités physiques que nous aborderons au cours de ce cours. Parmi celles-ci, on trouve par exemple la tension électrique, mesurée en volts (\unit{\volt}), le courant électrique en ampères (\unit{\ampere}), la puissance en watts (\unit{\watt}), la résistance électrique en ohms (\unit{\ohm}) et bien d'autres.

Pour comprendre les concepts suivants, il n'est pas encore nécessaire de connaître ces unités en détail. Il est important de comprendre d'abord la signification et l'application des préfixes d'unités.

Malheureusement, ces préfixes d'unités ne peuvent pas être entrés directement dans tous les calculatrices de poche. On utilise à cet effet les puissances de dix.

---

Examinons d'abord l'exemple du préfixe Kilo, qui représente 1000 : au lieu de 1000, on peut écrire 10 \cdot 10 \cdot 10. Pour cela, il existe l'abréviation $10^3$ (prononcé "10 puissance 3" ou "3ème puissance de 10"). Les indications \qty{1500}{\hertz}, \qty{1,5}{\kilo\hertz} et \qty{1,5e3}{\hertz} représentent la même valeur.

<tip>
On peut aussi s'en souvenir autrement : on multiplie le nombre par 10 autant de fois que l'indique l'exposant. Pour les nombres sans virgule, on ajoute simplement autant de zéros que l'indique l'exposant.
</tip>

Pour un million, il ne faut pas multiplier trois, mais six exemplaires du nombre 10. Le préfixe Mega correspond donc à la valeur $10^6$. L'écriture \qty{28e6}{\hertz} signifie donc la même chose que \qty{28}{\mega\hertz}.

Pour les petits nombres, cela fonctionne de manière similaire. Un millième est \frac{1}{10} \cdot \frac{1}{10} \cdot \frac{1}{10}. On écrit cela comme $10^{-3}$ ("dix puissance moins trois"). La valeur \qty{3,5e-3}{\volt} n'est donc rien d'autre que \qty{3,5}{\milli\volt} et \qty{22e-6}{\volt} signifie \qty{22}{\micro\volt}. Les puissances de dix les plus importantes sont à nouveau présentées dans le tableau [ref:e_einheitenvorzeichen].

---

Les calculatrices scientifiques techniques disposent généralement d'une touche pour les puissances, généralement désignée par $x^y$. Certains modèles offrent en outre une possibilité d'entrée simplifiée pour les puissances de dix : une touche avec l'inscription *Exp*, *E* ou \cdot 10^x. Celle-ci signifie "fois dix puissance …" et facilite grandement l'entrée de nombres très grands ou très petits.

Exemple : Pour entrer la valeur \num{3,5e6}, on appuie sur : 3.5 → Exp → 6

<tip>
Consultez de préférence le manuel d'utilisation de votre calculatrice pour trouver la combinaison exacte de touches.
</tip>

L'affichage de valeurs particulièrement grandes ou petites dépend de l'appareil. Certains les écrivent comme des puissances de dix ordinaires, d'autres avec *Exp* ou *E* pour *fois 10 puissance*. Souvent, la touche *S/D* permet de basculer entre différentes représentations. Dans l'écriture des puissances de dix, des touches comme *ENG*, *<ENG* ou *ENG>* déplacent la virgule ou ajoutent des zéros à la fin et adaptent l'exposant de manière à ce que la valeur ne change pas. Consultez de préférence ici le manuel d'utilisation de votre calculatrice.

---

La figure [ref:e_taschenrechner] montre trois représentations du même nombre dans une application de calculatrice. Les trois boutons pour la manipulation des puissances de dix ont été mis en évidence en rouge.

<margin>
[photo:172:e_taschenrechner:Différentes représentations du nombre 0,007 dans une application de calculatrice]
</margin>

Dans ce qui suit, vous trouverez plusieurs questions d'examen que vous pouvez résoudre à l'aide de votre calculatrice. Entrez à cet effet le nombre respectif selon l'énoncé de la question – faites attention éventuellement aux préfixes d'unité et utilisez le mode exponentiel. Avec la touche ENG, vous pouvez laisser la conversion s'effectuer automatiquement.

Avec un peu de pratique, les exercices peuvent bien sûr aussi être résolus de tête. Les unités peuvent être négligées dans ces exemples, car il s'agit ici en premier lieu de la représentation correcte en écriture exponentielle ou du préfixe d'unité approprié. Dans les calculs futurs, il sera de plus en plus important de sélectionner ou de convertir un résultat avec un certain préfixe d'unité.

%EA110
[question:EA110]
%EA109
[question:EA109]
%EA108
[question:EA108]
%EA116
[question:EA116]
%EA114
[question:EA114]
[question:EA111]
[question:EA112]
[question:EA115]
[question:EA113]