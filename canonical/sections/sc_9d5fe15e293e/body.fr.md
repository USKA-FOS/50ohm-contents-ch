Dans les transmissions numériques, les informations sont transmises sous forme de symboles. Un symbole est un état de signal distinct qui est transmis pendant une durée déterminée. Ces états de signal peuvent différer par exemple par des amplitudes, des fréquences ou des phases différentes, ou par des combinaisons de ces propriétés. La manière dont ces symboles sont générés sera abordée dans les sections suivantes. Selon le nombre de symboles différents qu'une méthode de transmission peut utiliser, un seul symbole peut contenir un ou plusieurs bits d'information.

Si seulement deux symboles différents sont disponibles, un bit peut être transmis avec chaque symbole. Avec quatre symboles possibles, deux bits peuvent déjà être transmis avec un seul symbole, car deux bits permettent de représenter quatre combinaisons différentes. De même, huit symboles différents peuvent transmettre trois bits, et 16 symboles différents peuvent transmettre quatre bits simultanément.

En général, le nombre $N$ de bits transmis par un symbole est donné par le nombre $M=2^N$ de symboles possibles :

$N = \log_2(M)$

Le **débit de symboles** indique combien de symboles sont transmis par seconde. Son unité est le *baud*. Un débit de symboles de $\qty{1000}{\baud}$ signifie donc que 1000 symboles sont transmis par seconde.

Le débit de symboles n'est pas nécessairement identique au débit binaire. Si plusieurs bits sont transmis avec chaque symbole, le débit binaire est alors plus élevé. Pour le débit binaire $R_\mathrm{D}$ (avec l'unité $\unit{\bit\per\second}$) et le débit de symboles $R_\mathrm{S}$, on a :

$R_\mathrm{D} = R_\mathrm{S} \cdot N$

Par exemple, si un débit de symboles de $\qty{1200}{\baud}$ permet de transmettre deux bits avec chaque symbole, le débit binaire est alors :

$R_\mathrm{D} = \qty{1200}{\baud} \cdot \qty{2}{\bit\per{Symbol}} = \qty{2400}{\bit\per\second}$

Le nombre de symboles possibles et le débit de symboles sont donc des grandeurs importantes pour les méthodes de transmission numériques. La manière dont les différents symboles peuvent être représentés par différentes propriétés d'un signal sera abordée dans les sections suivantes.

[question:AA104]

---

Un exemple simple de la manière dont différents symboles peuvent être représentés par différents états de signal est la **modulation par déplacement de fréquence** (*Frequency-Shift Keying*, FSK), déjà connue de la classe E.

Dans le cas de la FSK, la fréquence du signal émis est commutée entre différentes valeurs. La figure [ref:a_fsk] montre une FSK binaire avec deux fréquences de symbole possibles dans une représentation temporelle. Par exemple, la fréquence plus élevée peut représenter le symbole $1$ et la fréquence plus basse le symbole $0$. Comme deux symboles différents sont disponibles, un bit peut être transmis avec chaque symbole.

<margin>
[picture:703:a_fsk:FSK (modulation par déplacement de fréquence)]
</margin>

Un exemple est le *RTTY*. Ici, on commute entre deux fréquences de symbole, par exemple entre $\qty{14072,43}{\kilo\hertz}$ et $\qty{14072,60}{\kilo\hertz}$. Un bit, c'est-à-dire $0$ ou $1$, peut ainsi être transmis avec chaque symbole.

[question:AE405]

La FSK n'est cependant pas limitée à deux fréquences de symbole. Si quatre fréquences différentes sont utilisées, quatre symboles différents sont disponibles. Chaque symbole peut alors être associé à l'une des quatre combinaisons de bits possibles : $00$, $01$, $10$ ou $11$. Deux bits peuvent ainsi être transmis avec chaque symbole.

Un exemple de ceci est la méthode de transmission *FT4*. Ici, on peut commuter entre quatre fréquences de symbole, par exemple $\qty{14081,20}{\kilo\hertz}$, $\qty{14081,40}{\kilo\hertz}$, $\qty{14081,61}{\kilo\hertz}$ et $\qty{14081,83}{\kilo\hertz}$.

[question:AE406]