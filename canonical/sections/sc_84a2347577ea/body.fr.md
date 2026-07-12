À de nombreux endroits de la technique des hautes fréquences, les rapports de puissance jouent un rôle important, par exemple dans le gain d'une antenne ou d'un amplificateur, ou dans l'atténuation d'un câble. Dans la classe N, nous avons déjà connu ces relations sous forme de facteurs simples, par exemple : « L'antenne a un gain de facteur $2$ ».

Ces rapports peuvent prendre des valeurs numériques très grandes ou très petites. Par exemple, un récepteur à ondes courtes possède un facteur d'amplification total de $\num{1000000000000}$, soit un un suivi de douze zéros. Avec de tels nombres, le calcul devient rapidement peu clair, et on commence inévitablement à compter les zéros.

Cependant, il existe un moyen mathématique pour ce « comptage des zéros » : les logarithmes. Avec leur aide, les multiplications peuvent également être transformées en additions et les divisions en soustractions. Cela rend le calcul avec de grands nombres très simple.

---

Il est donc devenu courant d'indiquer les rapports de puissance sur une échelle logarithmique.
La logarithmation est l'opération inverse de la puissance. En radioamateur, nous utilisons généralement le logarithme décimal ("logarithmes décimaux") de base $10$ :

---

$a =\log_{10} (b)$, si $b=10^{a}$

Le logarithme de $100$ est $\log_{10}(100)=2$, car $10^2 = 100$. En d'autres termes : le nombre $100$ possède deux zéros.

<warning>
Un calculateur de poche technique-scientifique offre, outre le logarithme décimal (libellé $\lg$ ou $\log$), également le logarithme naturel *$\ln$* qui a pour base la constante d'Euler *$e=\num{2,7182818}\dots$*. Ne pas confondre !
</warning>	

<margin>
| c:dB | c:≈ Facteur de puissance |
| $0$ | $1$ |
| $1,5$ | $\sqrt{2} = 1,41$ |
| $2,15$ | $1,64$ |
| $3$ | $2$ |
| $5$ | $\sqrt{10} = 3,16$ |
| $6$ | $4$ |
| $10$ | $10$ |
| $20$ | $100$ |
[table:e_dezibel_leistungsfaktoren:Facteurs de puissance importants en $\unit{\dB}$]
</margin>

Le *Bel* ($\unit{\bel}$) est dérivé du logarithme décimal. Le nom rend hommage à l'enseignant américain pour sourds et pionnier du téléphone, *Alexander Graham Bell*. Dans l'exemple ci-dessus, nous aurions également pu écrire :

$\log_{10}(b)=\qty{a}{\bel}$

En règle générale, on utilise non pas le Bel, mais le *décibel* (symbole d'unité $\unit{\dB}$), c'est-à-dire le dixième d'un Bel :

$10 \cdot \log_{10}(b) = \qty{a}{\dB}$

---

Le recueil de formules donne pour la conversion d'un rapport de puissance la formule suivante :

$g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$

Où $P_1$ correspond à la puissance d'entrée et $P_2$ à la puissance de sortie. Supposons maintenant que nous avons un amplificateur qui amplifie la puissance d'entrée $P_1=\qty{50}{\watt}$ à $P_2=\qty{100}{\watt}$, donc la double. Selon notre formule, nous obtenons alors le facteur d'amplification suivant en $\unit{\dB}$ :

$g = 10\cdot \log_{10}\left(\frac{\qty{100}{\watt}}{\qty{50}{\watt}}\right)\unit{\dB} = 10\cdot \log_{10}\left(2\right)\unit{\dB} = 10\cdot \qty{0.301}{\dB} \approx \qty{3}{\dB} $

Pour la classe E, il suffit initialement de connaître la valeur en décibels pour le facteur de puissance $2$. Le recueil de formules contient à ce sujet un tableau qui est également représenté dans le tableau [ref:e_dezibel_leistungsfaktoren]. On peut y lire qu'un facteur de puissance de $2$ correspond à une valeur en décibels de $\qty{3}{\dB}$. Le calcul détaillé avec les valeurs en décibels n'est traité qu'en classe A.

<tip>
Sans calculatrice de poche, on peut estimer les valeurs en décibels qui se terminent par "$0$" : il suffit de retenir le dernier zéro, le chiffre indique alors le nombre de zéros du facteur de rapport. Exemple : $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zéros} \rightarrow \text{Facteur de rapport}~1000$ !
</tip>

[question:EA107]

Outre l'unité $\unit{dB}$, on rencontre fréquemment dans la pratique des indications telles que $\unit{\dBi}$, $\unit{\dBm}$, $\unit{\dBW}$ ou $\unit{\dBu}$. Ces compléments indiquent la grandeur de référence à laquelle se réfère la valeur en décibels respective. En classe E, nous rencontrerons particulièrement dans le chapitre sur les antennes les indications $\unit{\dBi}$ et $\unit{\dBd}$. Les autres grandeurs telles que $\unit{\dBm}$ et $\unit{\dBW}$ ne seront nécessaires que pour la classe A.