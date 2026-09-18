# Données
Niveau de sortie : $p_\text{sortie} = \qty{20}{\dBW}$

# Méthode de résolution
Nous utilisons la formule en $\unit{\dBW}$ du recueil de formules (niveaux, niveaux de puissance et niveaux de tension) :
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}$
et nous résolvons par rapport à $P$ :
$P = \qty{1}{\watt}\cdot 10^{\frac{p}{\qty{10}{\dBW}}}$
Avec $p_\text{sortie}$ issu de l’énoncé, la puissance de sortie s’élève à :
$P = \qty{1}{\watt}\cdot 10^{\frac{p_\text{sortie}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{\frac{\qty{20}{\dBW}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{2} = \qty{10^2}{\watt}$

# Abréviation
Quiconque a travaillé avec les logarithmes et le tableau des outils sait que $\qty{20}{\dB} \rightarrow 100$ correspond et que $\qty{20}{\dBW} \rightarrow \qty{100}{\watt} = \qty{10^2}{\watt}$.