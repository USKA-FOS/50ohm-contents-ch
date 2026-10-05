Dans les transmissions numériques, les informations sont transmises sous forme de symboles. Un symbole est un état de signal distinctif qui est transmis pendant une durée déterminée. Ces états de signal peuvent différer, par exemple, par des amplitudes, des fréquences ou des phases différentes, ou par des combinaisons de ces propriétés. Nous examinerons comment de tels symboles sont générés dans les sections suivantes. Selon le nombre de symboles différents qu'une méthode de transmission peut utiliser, un symbole individuel peut contenir un ou plusieurs bits d'information.

Si seulement deux symboles différents sont disponibles, chaque symbole peut transmettre exactement un bit. Avec quatre symboles possibles, deux bits peuvent déjà être transmis avec un symbole, car deux bits permettent de représenter quatre combinaisons différentes. De même, huit symboles différents peuvent transmettre trois bits simultanément, et $\num{16}$ symboles différents peuvent transmettre quatre bits.

En général, le nombre $N$ de bits transmissibles avec un symbole est dérivé du nombre $M=2^N$ de symboles possibles :

$N = \log_2(M)$

Le *débit de symboles* indique combien de symboles sont transmis par seconde. Son unité est le *baud*. Un débit de symboles de $\qty{1000}{\baud}$ signifie donc que $\num{1000}$ symboles sont transmis par seconde.

Le débit de symboles n'est pas nécessairement identique au débit de données. Si plusieurs bits sont transmis avec chaque symbole, le débit de données est d'autant plus élevé. Pour le débit de données $R_\mathrm{D}$ (avec l'unité $\unit{\bit\per\second}$) et le débit de symboles $R_\mathrm{S}$, on a :

$R_\mathrm{D} = R_\mathrm{S} \cdot N$

Par exemple, si à un débit de symboles de $\qty{1200}{\baud}$, deux bits sont transmis avec chaque symbole, le débit de données est :

$R_\mathrm{D} = \qty{1200}{\baud} \cdot \qty{2}{\bit\per{Symbole}} = \qty{2400}{\bit\per\second}$

Le nombre de symboles possibles et le débit de symboles sont donc des grandeurs importantes pour les méthodes de transmission numérique. Nous examinerons dans les sections suivantes comment les symboles individuels peuvent être représentés par différentes propriétés d'un signal.

[question:AA104]

---

Un exemple simple de la manière dont différents symboles peuvent être représentés par différents états de signal est la *modulation par déplacement de fréquence* (*Frequency-Shift Keying*, FSK), déjà connue dans la section [sec:ask_fsk_afsk].

Avec la FSK, la fréquence du signal émis est commutée entre différentes valeurs. La figure [ref:a_fsk] montre une FSK binaire avec deux fréquences de symbole possibles dans la représentation temporelle. Par exemple, la fréquence plus élevée peut représenter le symbole $1$ et la fréquence plus basse le symbole $0$. Comme deux symboles différents sont disponibles, chaque symbole peut transmettre un bit.

<margin>
[picture:703:a_fsk:FSK (Frequency-Shift Keying)]
</margin>

Un exemple est le *RTTY*. Ici, la commutation se fait entre deux fréquences de symbole, par exemple entre $\qty{14072,43}{\kilo\hertz}$ et $\qty{14072,60}{\kilo\hertz}$. Ainsi, chaque symbole peut transmettre un bit, c'est-à-dire $0$ ou $1$.

[question:AE405]

Cependant, la FSK n'est pas limitée à deux fréquences de symbole. Si, par exemple, quatre fréquences différentes sont utilisées, quatre symboles différents sont disponibles. Chaque symbole peut alors être associé à l'une des quatre combinaisons de bits possibles $00$, $01$, $10$ ou $11$. Ainsi, chaque symbole peut transmettre deux bits.

Un exemple de cela est la méthode de transmission *FT4*. Ici, la commutation peut se faire entre quatre fréquences de symbole, par exemple $\qty{14081,20}{\kilo\hertz}$, $\qty{14081,40}{\kilo\hertz}$, $\qty{14081,61}{\kilo\hertz}$ et $\qty{14081,83}{\kilo\hertz}$.

[question:AE406]
