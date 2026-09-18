# Données
Niveaux : $\qty{0}{\dBm}$, $\qty{3}{\dBm}$, $\qty{20}{\dBm}$

# Méthode de résolution
On utilise la formule du niveau en $\unit{\dBm}$ issue du recueil de formules (niveaux, niveaux de puissance et de tension) :
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$
et on résout pour $P$ :
$P = \qty{1}{\milli\watt}\cdot 10^{\frac{p}{\qty{10}{\dBm}}}$
On insère les valeurs de la question et on obtient :

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{0}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{0}= \qty{1}{\milli\watt}$

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{3}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{0,3}= \qty{1,995}{\milli\watt}$

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{20}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{2}= \qty{100}{\milli\watt}$

# Abréviation
Quiconque maîtrise les logarithmes et le tableau des outils peut rapidement arriver à la solution par élimination.
$\qty{0}{\dBm} \rightarrow \qty{1}{\milli\watt}$ (ce qui ne laisse que deux réponses possibles).
$\qty{3}{\dB}$ correspondent à un doublement. Ainsi, $\qty{3}{\dBm} \rightarrow  \qty{2}{\milli\watt}$ (ce qui ne laisse qu'une seule réponse possible).
