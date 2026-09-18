Il decibel è un'unità di misura ausiliaria logaritmica per la rappresentazione di livelli o rapporti. Per calcolare un livello è necessaria una riferimento, che viene indicato dopo il $\unit{\dB}$. Esempi di questa notazione si trovano nella raccolta di formule per livelli di potenza e di tensione:
$\qty{1}{\milli\watt}  \rightarrow  \unit{\dBm}$
$\qty{1}{\watt}  \rightarrow  \unit{\dBW} $
$\qty{0,775}{\volt}  \rightarrow  \unit{\dBu} $
L'unità di misura ausiliaria $\unit{\dB\micro\volt\per\meter}$ significa quindi che il riferimento è a $\qty{1}{\micro\volt\per\meter}$.

Partiamo quindi dalla formula:
$e = 20 \cdot \log_{10} \left( \frac{E}{\qty{1}{\micro\volt\per\meter}}\right)\unit{\dB\micro\volt\per\meter}$
e risolviamo rispetto a $E$:
$E = \qty{1}{\micro\volt\per\meter}\cdot 10^{\frac{e}{\qty{20}{\dB\micro\volt\per\meter}}}$
Con il valore fornito nel testo del problema otteniamo:
$E = \qty{1}{\micro\volt\per\meter}\cdot 10^{\frac{\qty{120}{\dB\micro\volt\per\meter}}{\qty{20}{\dB\micro\volt\per\meter}}} = \qty{1}{\micro\volt\per\meter}\cdot 10^{6} = \qty{10^{-6}}{\volt\per\meter}\cdot 10^{6} = \qty{1}{\volt\per\meter}$