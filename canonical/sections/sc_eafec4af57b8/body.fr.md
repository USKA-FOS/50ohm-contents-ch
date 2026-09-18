Dans la modulation par déplacement de phase (Phase-Shift Keying, PSK), les différents symboles sont représentés par des décalages de phase distincts d'une porteuse. L'amplitude et la fréquence de la porteuse restent inchangées. En revanche, lors du passage d'un symbole à l'autre, la phase peut varier.

L'illustration [ref:a_psk] montre un signal PSK dans le domaine temporel. Aux limites des symboles, on observe que l'oscillation se poursuit avec une autre phase.

<margin>
[picture:705:a_psk:Modulation par déplacement de phase (Phase-Shift Keying)]
</margin>

---

La forme la plus simple est la modulation par déplacement de phase binaire (Binary Phase-Shift Keying, BPSK). Elle utilise deux décalages de phase distincts et donc deux symboles possibles. Par exemple, les décalages de phase à $\qty{0}{\degree}$ et $\qty{180}{\degree}$ peuvent être associés aux valeurs de bits $0$ et $1$. L'illustration [ref:a_psk_mapping] montre une association possible des deux valeurs de bits aux deux symboles BPSK.

Comme les deux symboles ne diffèrent que par leur phase et que leur amplitude est identique, les deux points du diagramme de constellation sont situés en opposition sur un cercle.

<margin>
[picture:1101:a_psk_mapping:BPSK dans un diagramme de constellation]
</margin>

<indepth>
Précision : techniquement, la BPSK avec les angles $\qty{0}{\degree}$ et $\qty{180}{\degree}$ peut aussi être considérée comme une modulation ASK où l'amplitude du signal porteur est commutée entre une valeur négative et une valeur positive. La multiplication par $-1$ d'un signal sinusoïdal équivaut à un décalage de phase de $\qty{180}{\degree}$ :

$-\sin(\omega t)=\sin(\omega t+\qty{180}{\degree})$

Il s'agit d'un cas particulier. D'autres angles de phase, comme $\qty{90}{\degree}$ et $\qty{270}{\degree}$, seraient également possibles, leurs deux phases de symbole étant séparées de $\qty{180}{\degree}$.
</indepth>

[question:AE401]

---

Avec plus de deux décalages de phase distincts, il est possible de représenter davantage de symboles. Cela permet de regrouper plusieurs bits en un seul symbole.

---

Dans la modulation par déplacement de phase en quadrature (Quadrature Phase-Shift Keying, QPSK), quatre décalages de phase distincts sont utilisés, offrant ainsi quatre symboles possibles. Comme il existe quatre combinaisons de bits possibles à partir de deux bits, chaque symbole permet de transmettre deux bits.

Pour comparaison :

* BPSK : $\num{2}$ symboles → $\num{1}$ bit par symbole
* QPSK : $\num{4}$ symboles → $\num{2}$ bits par symbole
* 8-PSK : $\num{8}$ symboles → $\num{3}$ bits par symbole

[question:AE402]

Examinons maintenant la QPSK dans un diagramme de constellation. Les quatre symboles possibles ont la même amplitude, mais diffèrent par leur phase. C'est pourquoi les quatre points du signal se trouvent sur un cercle. L'illustration [ref:a_qpsk] montre une association possible des quatre combinaisons de bits $00$, $01$, $10$ et $11$ aux quatre symboles QPSK.

<margin>
[picture:1059:a_qpsk:Diagramme I/Q pour une association QPSK]
</margin>

---

Dans cet exemple, les décalages de phase suivants sont utilisés :

* $11$ correspond à $\qty{45}{\degree}$
* $01$ correspond à $\qty{135}{\degree}$
* $00$ correspond à $\qty{225}{\degree}$
* $10$ correspond à $\qty{315}{\degree}$

<margin>
L'applet suivant illustre la modulation numérique QPSK. Dans un système réel, le signal est affecté par le bruit et d'autres perturbations. Les points du signal reçu ne se trouvent donc pas exactement sur les positions idéales, mais s'écartent à la fois en amplitude et en phase. L'applet simule cela en ajoutant du bruit. Les croix marquent les quatre symboles QPSK idéaux. Chaque point coloré représente une valeur de réception bruitée. Le récepteur l'attribue au symbole le plus proche. Les zones colorées en arrière-plan sont les zones de décision du récepteur. Tant qu'une valeur de réception bruitée reste dans la zone du symbole initialement émis, elle est correctement reconnue. Si un point dépasse une limite vers une zone voisine en raison d'un bruit important, le récepteur choisit le mauvais symbole. Cependant, ces erreurs peuvent être corrigées par un codage de canal. Nous aborderons ce sujet dans une section ultérieure.

[include:applet_qpsk]
</margin>

Les quatre décalages de phase sont chacun décalés de $\qty{90}{\degree}$ les uns par rapport aux autres. Le récepteur peut déterminer le symbole, et donc la combinaison de bits transmise, en fonction de la phase détectée.

L'attribution des combinaisons de bits aux différents décalages de phase n'est pas définie de manière unique. L'essentiel est d'abord que chaque symbole soit associé à une combinaison de bits unique.

En pratique, l'attribution est souvent choisie de manière à ce que les combinaisons de bits de symboles voisins ne diffèrent que par un seul bit. Une telle attribution est appelée *code de Gray*. Si un point de signal voisin est détecté par erreur en raison du bruit, cela ne conduit souvent qu'à une seule erreur de bit.

Le diagramme de constellation met ainsi en évidence une différence essentielle entre l'ASK et la PSK : dans l'ASK, les symboles diffèrent par leur distance par rapport à l'origine et se trouvent généralement uniquement sur l'axe I positif, tandis que dans la PSK, ils diffèrent par leur angle. Avec la PSK, les points du signal se trouvent donc sur un cercle si l'amplitude est identique.