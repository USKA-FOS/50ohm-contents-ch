Dans de nombreux domaines de la technique des hautes fréquences, les rapports de puissance jouent un rôle important, par exemple pour le gain d'une antenne ou d'un amplificateur, ou encore pour l'atténuation d'un câble. Jusqu'à présent, nous avons appris à connaître ces relations sous la forme de facteurs simples, par exemple : « L'antenne a un gain de facteur $2$. »

Ces rapports peuvent prendre des valeurs numériques très grandes ou très petites. Par exemple, un récepteur ondes courtes possède un facteur de gain total de $\num{1000000000000}$, soit un 1 suivi de douze zéros. Avec de tels nombres, les calculs deviennent rapidement peu maniables, et on commence inévitablement à compter les zéros.

Cependant, il existe un outil mathématique simplifiant ce « comptage des zéros » : les logarithmes. Grâce à eux, il est possible de transformer des multiplications en additions et des divisions en soustractions. Cela rend les calculs avec de grands nombres très simples.

---

Il est donc devenu courant d'exprimer les rapports de puissance sur une échelle logarithmique.
Le passage au logarithme est l'opération inverse de l'élévation à une puissance. En radioamateurisme, on utilise généralement le logarithme décimal ("logarithmes à base 10") :

---

a = \log_{10} (b), si b = 10^{a}

Le logarithme de 100 est égal à \log_{10}(100) = 2, car 10^2 = 100. Autrement dit : le nombre 100 possède deux zéros.

<warning>
Une calculatrice scientifique propose, en plus du logarithme décimal (étiqueté \lg ou \log), le logarithme naturel *$\ln$*, qui a pour base le nombre d’Euler *$e=\num{2,7182818}\dots$*. À ne pas confondre !
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

Le *Bel* ($\unit{\bel}$) est dérivé du logarithme décimal. Ce nom rend hommage à l'enseignant américain pour sourds et pionnier du téléphone, *Alexander Graham Bell*. Dans l'exemple ci-dessus, nous aurions aussi pu écrire :

$\log_{10}(b)=\qty{a}{\bel}$

En pratique, on utilise généralement le *décibel* (symbole $\unit{\dB}$), soit la dixième partie d'un Bel :

$10 \cdot \log_{10}(b) = \qty{a}{\dB}$

---

Le recueil de formules indique la formule suivante pour convertir un rapport de puissance :

$g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$

Où $P_1$ correspond à la puissance d'entrée et $P_2$ à la puissance de sortie. Supposons maintenant que nous avons un amplificateur qui amplifie la puissance d'entrée $P_1=\qty{50}{\watt}$ à $P_2=\qty{100}{\watt}$, soit le double. Selon notre formule, le facteur d'amplification en $\unit{\dB}$ est alors :

$g = 10\cdot \log_{10}\left(\frac{\qty{100}{\watt}}{\qty{50}{\watt}}\right)\unit{\dB} = 10\cdot \log_{10}\left(2\right)\unit{\dB} = 10\cdot \qty{0.301}{\dB} \approx \qty{3}{\dB}$

Pour HB3, il suffit dans un premier temps de connaître la valeur en décibels pour un facteur de puissance de 2. Le recueil de formules contient un tableau qui est également présenté dans le tableau [ref:e_dezibel_leistungsfaktoren]. On peut y lire qu'un facteur de puissance de 2 correspond à une valeur de $\qty{3}{\dB}$. Les calculs détaillés avec des valeurs en décibels ne sont abordés qu'au niveau de la classe A.

<tip>
Sans calculatrice, il est possible d'estimer des valeurs en décibels se terminant par "$0$" : il suffit de masquer le dernier zéro, le chiffre obtenu indique alors le nombre de zéros du facteur de rapport. Exemple : $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zéros} \rightarrow \text{facteur de rapport}~1000$ !
</tip>

<indepth>
D'autres valeurs en décibels peuvent être estimées sans calculatrice à l'aide du tableau suivant :

| c:dB | l:Facteur | c:dB | l:Facteur |
| -3 | 0,5 | +3 | 2 |
| -6 | 0,25 | +6 | 4 |
| -10 | 1/10 | +10 | 10 |
| -20 | 1/100 | +20 | 100 |
| -30 | 1/1000 | +30 | 1000 |
[table:n_db_leistungsangaben:Valeurs en décibels (puissance) fréquemment utilisées]
</indepth>

<tip>
En combinant les valeurs ci-dessus, il est possible d'estimer d'autres valeurs sans calculatrice.

| c:Facteur | c:dB | l:Calcul |
| ×8 | 9 | 3+3+3 |
| ×20 | 13 | 10+3 |
| ×1/8 | -9 | -3-3-3 |
| ×50 | 17 | 20-3 |
| ×3 | 5 | approximativement |
| ×1,25 | 1 | 10-9 |
| ×1,5 | 2 | approximativement |
[table:n_db_beispiele:Exemples de dB]
</tip>

[question:EA107]

Outre l'unité $\unit{dB}$, on rencontre fréquemment en pratique des indications comme $\unit{\dBi}$, $\unit{\dBm}$, $\unit{\dBW}$ ou $\unit{\dBu}$. Ces suffixes indiquent la grandeur de référence à laquelle se rapporte la valeur en décibels. En particulier pour les antennes, nous rencontrerons les indications $\unit{\dBi}$ et $\unit{\dBd}$ dans le chapitre [sec:antennengewinn]. Les autres grandeurs comme $\unit{\dBm}$ et $\unit{\dBW}$ ne seront abordées qu'au chapitre [sec:dezibel_2].