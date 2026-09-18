# Dati
Livello d’uscita: $p_\text{uscita} = \qty{20}{\dBW}$

# Procedimento
Utilizziamo la formula in $\unit{\dBW}$ dalla raccolta di formule (livelli, livelli di potenza e di tensione):
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}$
e risolviamo rispetto a $P$:
$P = \qty{1}{\watt}\cdot 10^{\frac{p}{\qty{10}{\dBW}}}$
Con $p_\text{uscita}$ dal testo del problema, si ottiene la potenza d’uscita:
$P = \qty{1}{\watt}\cdot 10^{\frac{p_\text{uscita}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{\frac{\qty{20}{\dBW}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{2} = \qty{10^2}{\watt}$

# Abbreviazione
Chi ha familiarità con i logaritmi e la tabella degli strumenti ausiliari sa che $\qty{20}{\dB} \rightarrow 100$ e quindi $\qty{20}{\dBW} \rightarrow \qty{100}{\watt} = \qty{10^2}{\watt}$.