# Données
Puissance de sortie de l'émetteur : $p_\text{émetteur, sortie} = \qty{1}{\watt}$  
Gain : $g_\text{étage final} = \qty{10}{\dezibel}$  

# Démarche
Nous utilisons la formule en $\unit{\dBm}$ du <i>recueil de formules</i> (niveau, niveau de puissance et niveau de tension) :  
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$ 
et calculons ainsi le niveau d'entrée dans l'étage final :
$ p_\text{étage final, entrée} = 10 \cdot \log_{10}\left(\frac{p_\text{émetteur, sortie}}{\qty{1}{\milli\watt}}\right)\unit{\dBm}= 10 \cdot \log_{10}\left(\frac{\qty{1}{\watt}}{\qty{10^{-3}}{\watt}}\right)\unit{\dBm} \\ = 10 \cdot \log_{10}\left(10^{3}\right)\unit{\dBm}= 10 \cdot \qty{3}{\dBm}\\ = \qty{30}{\dBm}$ 
Le niveau de sortie s'obtient ensuite par simple addition :
$ p_\text{sortie} = p_\text{entrée} + g_\text{gain} = \qty{30}{\dBm} + \qty{10}{\dB} = \qty{40}{\dBm}$

# Raccourci
Quiconque a travaillé avec les logarithmes et le tableau des outils peut résoudre mentalement le problème.  
$\qty{1}{\watt}$ équivaut à $\qty{1000}{\milli\watt}$, soit $\qty{30}{\dBm}$, auquel s'ajoute le gain de $\qty{10}{\dezibel}$, ce qui donne $\qty{40}{\dBm}$. 