Nous avons déjà appris à connaître les trois grandeurs les plus importantes de l'électrotechnique, à savoir la tension électrique, le courant électrique et la résistance :
* Tout d'abord, nous avons appris que des charges électriques sont séparées dans des sources de tension, ce qui crée une tension électrique. Nous la désignons par la lettre $U$ et la mesurons en volts ($\unit{V}$).
* Ensuite, nous avons appris que la tension électrique fait circuler un courant électrique dans un circuit fermé, que nous désignons par la lettre $I$ et mesurons en ampères ($\unit{A}$).
* Et au début de ce chapitre, nous avons appris que les récepteurs dans un circuit exercent une résistance et freinent ainsi le flux de courant. Nous désignons la résistance par la lettre $R$ et la mesurons en ohms ($\unit{\ohm}$).

%<margin>
%[p-h-o-t-o:147:ohmsches_gesetz_comic:Représentation imagée des relations de la loi d'Ohm]
%</margin>

[question:NA203]

---

Mais comment ces trois grandeurs sont-elles liées ? Examinons un exemple dans l'illustration [ref:n_ohmsches_gesetz_stromkreis_mit_batterie]. Nous avons un circuit composé d'une batterie comme source de tension et d'une résistance. Nous connaissons la tension et nous pouvons mesurer le courant. La batterie a une tension de $\qty{10}{\volt}$, et un courant de $\qty{1}{\milli\ampere}$ circule.

<margin>
[picture:664:n_ohmsches_gesetz_stromkreis_mit_batterie:Circuit avec batterie]
</margin>

Si l'on remplace la batterie de $\qty{10}{\volt}$ dans cet exemple par une batterie de $\qty{20}{\volt}$, le courant passerait de $\qty{1}{\milli\ampere}$ à $\qty{2}{\milli\ampere}$. Si l'on double donc la tension, le courant double également. De même, le courant serait divisé par deux, soit $\qty{0,5}{\milli\ampere}$, si l'on divisait la tension par deux, à $\qty{5}{\volt}$.

Nous pouvons observer un schéma : dans notre exemple, la tension $U$ en volts est toujours 10 000 fois plus grande que le courant $I$ en ampères. Ou, exprimé mathématiquement :

$\dfrac{U}{I} = \dfrac{\qty{10}{\volt}}{\qty{0,001}{\ampere}} = \dfrac{\qty{20}{\volt}}{\qty{0,002}{\ampere}} = \dfrac{\qty{5}{\volt}}{\qty{0,0005}{\ampere}} = 10000 \frac{\unit{\volt}}{\unit{\ampere}}$

---

En termes techniques, on parle de proportionnalité : $I$ est proportionnel à $U$. En laissant de côté les unités, le *facteur de proportionnalité* dans notre exemple est de 10 000 : si l'on multiplie l'une des valeurs par 10 000, on obtient l'autre valeur.
%Dans ce cas, on peut aussi se représenter le phénomène à l'aide d'un circuit d'eau : si la pompe exerce une pression plus forte, davantage d'eau circule dans le circuit.

<indepth>
Le *facteur de proportionnalité* est le rapport numérique entre deux grandeurs proportionnelles.
</indepth>

Il reste cependant une question : d'où vient ce facteur de 10 000 ? La réponse est simple : il s'agit de notre résistance $R$ ! Et si l'on considère maintenant les unités, tout s'emboîte : l'ohm est en effet défini de telle sorte que $\qty{1}{\ohm}$ équivaut à $\qty{1}{\volt\per\ampere}$. Nous pouvons donc écrire $\qty{10000}{\volt\per\ampere}$ simplement $\qty{10000}{\ohm}$. Notre résistance est donc de $\qty{10000}{\ohm}$ ou, en abrégé, $\qty{10}{\kilo\ohm}$ :

$\qty{10000}{\volt\per\ampere} = \qty{10000}{\ohm}$

%La question suivante se pose : pourquoi le courant est-il exactement de $\qty{1}{\milli\ampere}$ lorsque la tension est de $\qty{10}{\volt}$ ? L'intensité du courant dépend de la valeur de la résistance. Si la résistance est grande, le courant sera faible ; si la résistance est faible, le courant sera élevé.

Nous avons appris que la valeur de la résistance peut être calculée à partir de la tension et du courant. Elle est le *rapport entre la tension et le courant*, ou, en d'autres termes : si l'on divise la tension par le courant, on obtient la valeur de la résistance.

---

Cette relation peut être représentée par la formule suivante, appelée *loi d'Ohm* :

$ R = \dfrac{U}{I} $

<person>
Le physicien allemand *Georg Simon Ohm* a découvert en 1826 la relation entre la tension électrique, le courant électrique et la résistance. En son honneur, la formule $ R = \frac{U}{I} $ est appelée loi d'Ohm.
</person>

[question:NB505]

Si l'on ne connaît que la résistance et la tension et que l'on souhaite calculer le courant correspondant, on peut utiliser la loi d'Ohm comme suit :

$ I = \dfrac{U}{R} $

Dans le cas où l'on ne connaît que la résistance et le courant et que l'on souhaite calculer la tension correspondante, il existe une autre variante de la formule :

$ U = R\cdot I $

[question:NB504]

Il n'est pas nécessaire de mémoriser ces formules. Elles figurent également dans le *recueil de formules* qui est mis à disposition comme outil d'aide lors de l'examen. Pour les calculs, une calculatrice peut être utilisée lors de l'examen.

[question:NB502]
[question:NB503]
[question:NB501]
