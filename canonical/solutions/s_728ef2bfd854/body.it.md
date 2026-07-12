# Dati
Amplificazione: $g_\text{Verstärkung} = \qty{10}{\dezibel}$  
Potenza d'ingresso: $P = \qty{1}{\watt}$ (La potenza d'uscita del trasmettitore è la potenza d'ingresso dello stadio finale.)

# Percorso di soluzione
Calcoliamo il livello d'ingresso con la formula in $\unit{\dBW}$ dalla raccolta di formule (livello, livello di potenza e di tensione):
$ p_\text{Eingang} = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW} = \qty{0}{\dBW}$  
Il livello d'uscita si ottiene quindi per semplice addizione:
$ p_\text{Ausgang} = p_\text{Eingang} + g_\text{Verstärkung} = \qty{0}{\dBW} + \qty{10}{\dB} = \qty{10}{\dBW}$

# Abbreviazione
Il problema può essere risolto ancora più velocemente se si sa che $\log\left(1\right) = 0$ e quindi $\qty{1}{\watt} \rightarrow \qty{0}{\dBW}$. Pertanto, il livello d'uscita corrisponde esattamente all'amplificazione di $\qty{10}{\dBW}$.