De nombreux procédés de modulation numérique utilisent plus de deux symboles. Au lieu de seulement deux amplitudes (petite et grande), la modulation d'amplitude fonctionne également avec quatre amplitudes différentes ou plus, par exemple $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$, $\qty{100}{\percent}$ du maximum. Ainsi, deux bits ou plus peuvent être combinés en un symbole et transmis simultanément.

[picture:701:4ask:Modulation d'amplitude à quatre niveaux (Quaternary Amplitude-shift Keying)]

Ce principe peut également être appliqué à la modulation de fréquence et de phase. Une modulation de phase simple (Binary Phase-Shift Keying, BPSK) n'utilise que deux positions de phase différentes et ne peut donc envoyer qu'un bit à la fois. La modulation de phase en quadrature (Quadrature Phase-Shift Keying, QPSK), en revanche, utilise déjà quatre positions de phase différentes ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ et $\qty{270}{\degree}$). La QPSK transmet ainsi deux bits à chaque étape.

[question:AE402]

Dans les procédés tels que la QPSK, plus d'un bit est transmis par symbole, nous devons donc faire attention aux unités. Alors que nous parlons de débit de données en $\unit{\bit\per\second}$ en ce qui concerne le flux de données, le taux de succession de symboles différents est noté en symboles par seconde avec l'unité Baud.

[question:AA104]

Si seulement deux symboles sont utilisés et donc chaque bit est envoyé individuellement, le débit de symboles en Baud ($\unit{\baud}$) correspond au débit de données en bits par seconde ($\unit{\bit\per\second}$). Cependant, si plus de symboles sont utilisés et donc plusieurs bits sont transmis simultanément, le débit de données est plus élevé que le débit de symboles. Pour la relation, il est valable que le débit de données en $\unit{\bit\per\second}$ est égal au débit de symboles en $\unit{\baud}$ multiplié par le nombre de bits transmis par symbole :

$C=R_\mathrm{S}\cdot n$

$C$ Débit de transmission de données en $\unit{\bit\per\second}$

$R_\mathrm{S}$ Débit de symboles en $\unit{\baud}$

$n$ Taille du symbole en $\unit{\bit\per\text{Symbol}}$

[question:AE405]
[question:AE406]
