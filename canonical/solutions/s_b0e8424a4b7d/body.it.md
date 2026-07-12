# Dato
Livello di uscita: $p_\text{uscita} = \qty{20}{\dBW}$  

# Percorso di soluzione
Utilizziamo la formula in $\unit{\dBW}$ dalla raccolta di formule (Livello, Livello di potenza e di tensione):  
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}$ 
e risolviamo per P:
$P = \qty{1}{\watt}\cdot 10^{\frac{p}{\qty{10}{\dBW}}}$
Con $p_\text{uscita}$ dalla formulazione del problema, la potenza d'uscita risulta:
$P = \qty{1}{\watt}\cdot 10^{\frac{p_\text{uscita}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{\frac{\qty{20}{\dBW}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{2} = \qty{10^2}{\watt}$

# Abbreviazione
Chi ha lavorato un po' con i logaritmi e la tabella degli ausiliari sa che $\qty{20}{\dB} \rightarrow 100$ corrisponde e quindi $\qty{20}{\dBW} \rightarrow \qty{100}{\watt} = \qty{10^2}{\watt} $ corrisponde.
