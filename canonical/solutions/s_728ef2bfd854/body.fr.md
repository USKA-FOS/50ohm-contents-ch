# Données
Gain : $g_\text{Verstärkung} = \qty{10}{\dezibel}$  
Puissance d’entrée : $P = \qty{1}{\watt}$ (La puissance de sortie de l’émetteur est la puissance d’entrée de l’étage final.)

# Méthode de résolution
Nous calculons le niveau d’entrée avec la formule en $\unit{\dBW}$ du *recueil de formules* (niveau, niveau de puissance et niveau de tension) :  
$ p_\text{entrée} = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW} = \qty{0}{\dBW}$  
Le niveau de sortie s’obtient ensuite par simple addition :
$ p_\text{sortie} = p_\text{entrée} + g_\text{Verstärkung} = \qty{0}{\dBW} + \qty{10}{\dB} = \qty{10}{\dBW}$

# Abréviation
On peut résoudre l’exercice encore plus rapidement si l’on sait que $\log\left(1\right) = 0$ et que $\qty{1}{\watt} \rightarrow \qty{0}{\dBW}$. Ainsi, le niveau de sortie correspond exactement au gain de $\qty{10}{\dBW}$. 