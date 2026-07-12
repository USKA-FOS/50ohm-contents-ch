# Données
Amplification: $g_\text{Amplification} = \qty{10}{\dezibel}$  
Puissance d'entrée: $P = \qty{1}{\watt}$ (La puissance de sortie de l'émetteur est la puissance d'entrée de l'étage final.)

# Solution
Nous calculons le niveau d'entrée avec la formule $\unit{\dBW}$ du recueil de formules (niveau, niveaux de puissance et de tension):  
$ p_\text{Entrée} = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW} = \qty{0}{\dBW}$  
Le niveau de sortie est alors obtenu par simple addition:
$ p_\text{Sortie} = p_\text{Entrée} + g_\text{Amplification} = \qty{0}{\dBW} + \qty{10}{\dB} = \qty{10}{\dBW}$

# Abréviation
La tâche peut être résolue encore plus rapidement si l'on sait que $\log\left(1\right) = 0$ et donc que $\qty{1}{\watt} \rightarrow \qty{0}{\dBW}$. Ainsi, le niveau de sortie correspond exactement à l'amplification de $\qty{10}{\dBW}$.