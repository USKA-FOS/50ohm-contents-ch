Dans le cadre du traitement numérique des signaux, le *mapping* décrit l'étape où les données numériques sont converties en points de signal spécifiques (symboles) qui peuvent être envoyés via le système de transmission. Il s'agit d'un processus décisif dans la modulation, en particulier dans les modulations d'amplitude en quadrature (QAM) et les modulations de phase comme la QPSK (Quadrature Phase Shift Keying).

Pour visualiser les symboles, nous utilisons un *diagramme de constellation* comme dans la figure [ref:a_konstellation], qui représente les points de signal possibles dans un espace bidimensionnel. On désigne souvent les axes comme étant en phase (I) et en quadrature (Q). Chaque point du diagramme représente une amplitude et une phase spécifiques, qui sont associées à une combinaison particulière de bits, comme le montre la figure [ref:a_qpsk].

<margin>
[picture:1060:a_konstellation:Diagramme de constellation]
</margin>

---

Examinons d'abord la QPSK dans la figure [ref:a_qpsk] : dans la QPSK, deux bits sont regroupés en un symbole. Comme nous avons deux bits par symbole, il y a quatre combinaisons possibles ($\num{00}$, $\num{01}$, $\num{10}$, $\num{11}$). Chacune de ces combinaisons est associée à un point de signal spécifique, représenté par une phase particulière.

<margin>
[picture:1059:a_qpsk:Diagramme I-Q pour un mapping QPSK]
</margin>

---

Dans la QPSK, chaque symbole a sa propre phase. Les phases sont généralement définies par des incréments de $\qty{90}{\degree}$ et sont mappées aux quatre combinaisons de bits possibles, par exemple :

- $\num{11}$ correspond à $\qty{45}{\degree}$
- $\num{01}$ correspond à $\qty{135}{\degree}$
- $\num{00}$ correspond à $\qty{225}{\degree}$
- $\num{10}$ correspond à $\qty{315}{\degree}$

L'amplitude des signaux reste constante, et l'information est transmise exclusivement par la position de phase. C'est pourquoi les quatre points du diagramme de constellation pour la QPSK se trouvent sur un cercle. 

<indepth>
Il existe cependant d'autres possibilités pour associer les phases aux combinaisons de bits, à condition qu'elles soient univoques. Le mapping présenté ici n'est qu'un exemple. Dans cet exemple, les associations ont été choisies de manière à ce que peu de bits changent entre les symboles voisins. Cela présente l'avantage que, sous l'influence du bruit, peu d'erreurs de bit se produisent. Pour cela, on utilise le code de Gray, qui est utilisé dans la plupart des procédés de transmission numérique.
</indepth>

---

Chacun de ces points représente un symbole. Le récepteur peut déterminer, à partir de la position de phase, quelle combinaison de bits a été envoyée. Le diagramme de constellation dans la QPSK montre quatre points de signal à angle droit les uns par rapport aux autres, correspondant aux quatre phases utilisées. La grande séparation entre les phases individuelles permet un décodage fiable même dans des conditions bruitées.

Si l'on modifie non seulement la phase mais aussi l'amplitude, on parle alors d'une modulation d'amplitude en quadrature (QAM). Dans la QAM, à la fois l'amplitude et la phase sont variées pour transmettre plus de bits par symbole. Par exemple, dans le cas de la 16-QAM, chaque symbole peut représenter quatre bits, ce qui conduit à 16 points de signal possibles dans le diagramme de constellation. Un exemple de mapping 16-QAM est représenté dans la figure [ref:a_qam].

<margin>
[picture:1061:a_qam:Diagramme I-Q pour un mapping 16-QAM]
</margin>