# Données
Niveau : $\qty{0}{\dBm}$, $\qty{3}{\dBm}$, $\qty{20}{\dBm}$  

# Solution
Nous utilisons la formule $\unit{\dBm}$ du recueil de formules (niveau, niveau de puissance et de tension) :  
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$ 
et nous résolvons pour $P$:
$P = \qty{1}{\milli\watt}\cdot 10^{\frac{p}{\qty{10}{\dBm}}}$
Nous insérons les valeurs de la question et obtenons :  

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{0}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{0}= \qty{1}{\milli\watt}$

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{3}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{0,3}= \qty{1,995}{\milli\watt}$

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{20}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{2}= \qty{100}{\milli\watt}$

# Abréviation
Celui qui a un peu travaillé avec les logarithmes et la table des outils auxiliaires peut rapidement arriver à la solution correcte par le procédé d'élimination.  
$\qty{0}{\dBm} \rightarrow \qty{1}{\milli\watt}$ (il ne reste donc que deux réponses possibles).  
$\qty{3}{\dB}$ correspondent à un doublement. Donc $\qty{3}{\dBm} \rightarrow  \qty{2}{\milli\watt}$ (il ne reste donc qu'une seule réponse). 
