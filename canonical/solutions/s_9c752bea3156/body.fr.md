Le décibel est une unité auxiliaire logarithmique permettant de représenter des niveaux ou des rapports. Pour calculer un niveau, une référence est nécessaire, celle-ci est indiquée après le $\unit{\dB}$. Des exemples de cette notation se trouvent dans le recueil de formules pour les niveaux de puissance et de tension :
$\qty{1}{\milli\watt} \rightarrow \unit{\dBm}$
$\qty{1}{\watt} \rightarrow \unit{\dBW}$
$\qty{0,775}{\volt} \rightarrow \unit{\dBu}$
L'unité auxiliaire $\unit{\dB\micro\volt\per\meter}$ signifie donc que la référence est de $\qty{1}{\micro\volt\per\meter}$.

Nous partons donc de la formule :
$e = 20 \cdot \log_{10} \left( \frac{E}{\qty{1}{\micro\volt\per\meter}}\right)\unit{\dB\micro\volt\per\meter}$
et nous résolvons pour $E$ :
$E = \qty{1}{\micro\volt\per\meter} \cdot 10^{\frac{e}{\qty{20}{\dB\micro\volt\per\meter}}}$
Avec la valeur de l'énoncé, nous obtenons :
$E = \qty{1}{\micro\volt\per\meter} \cdot 10^{\frac{\qty{120}{\dB\micro\volt\per\meter}}{\qty{20}{\dB\micro\volt\per\meter}}} = \qty{1}{\micro\volt\per\meter} \cdot 10^{6} = \qty{10^{-6}}{\volt\per\meter} \cdot 10^{6} = \qty{1}{\volt\per\meter}$