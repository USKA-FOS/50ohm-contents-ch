# Données
Niveau de sortie : $p_\text{sortie} = \qty{20}{\dBW}$  

# Solution
Nous utilisons la formule $\unit{\dBW}$ du recueil de formules (niveau, niveau de puissance et de tension)  
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}$ 
et nous résolvons pour $P$:
$P = \qty{1}{\watt}\cdot 10^{\frac{p}{\qty{10}{\dBW}}}$
Avec $p_\text{sortie}$ de l'énoncé, la puissance de sortie est:
$P = \qty{1}{\watt}\cdot 10^{\frac{p_\text{sortie}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{\frac{\qty{20}{\dBW}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{2} = \qty{10^2}{\watt}$

# Abréviation
Celui qui a un peu travaillé avec les logarithmes et la table des outils auxiliaires sait que $\qty{20}{\dB} \rightarrow 100$ et donc que $\qty{20}{\dBW} \rightarrow \qty{100}{\watt} = \qty{10^2}{\watt}$ correspondent.