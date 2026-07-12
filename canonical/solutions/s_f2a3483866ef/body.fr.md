# Données
Puissance de sortie de l'émetteur : $p_\text{émetteur, sortie} = \qty{1}{\watt}$  
Amplification : $g_\text{étage final} = \qty{10}{\dezibel}$  

# Solution
Nous utilisons la formule $\unit{\dBm}$ du recueil de formules (niveau, niveaux de puissance et de tension) :  
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$ 
et calculons ainsi le niveau d'entrée dans l'étage final :
$ p_\text{étage final, entrée} = 10 \cdot \log_{10}\left(\frac{p_\text{émetteur, sortie}}{\qty{1}{\milli\watt}}\right)\unit{\dBm}= 10 \cdot \log_{10}\left(\frac{\qty{1}{\watt}}{\qty{10^{-3}}{\watt}}\right)\unit{\dBm} \\ = 10 \cdot \log_{10}\left(10^{3}\right)\unit{\dBm}= 10 \cdot \qty{3}{\dBm}\\ = \qty{30}{\dBm}$ 
Le niveau de sortie résulte alors par simple addition à :
$ p_\text{sortie} = p_\text{entrée} + g_\text{amplification} = \qty{30}{\dBm} + \qty{10}{\dB} = \qty{40}{\dBm}$

# Abréviation
Celui qui a un peu travaillé avec les logarithmes et la table des outils auxiliaires peut calculer la solution de tête.  
$\qty{1}{\watt}$ correspondent à $\qty{1000}{\milli\watt}$ correspondent à $\qty{30}{\dBm}$ plus l'amplification de $\qty{10}{\dezibel}$ donnent $\qty{40}{\dBm}$.