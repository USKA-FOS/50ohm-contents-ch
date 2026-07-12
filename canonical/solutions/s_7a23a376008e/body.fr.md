# Données
Amplification : $g = \qty{16}{\dezibel}$  
Conduite d'entrée : $P_1 = \qty{1}{\watt}$

# Solution 1
Nous utilisons la formule du recueil de formules (niveau, amplification, puissance) :  
$ g = 10 \cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$  
et nous résolvons pour $P_2$:
$P_2 = P_1 \cdot 10^{\frac{g}{\qty{10}{\dB}}}$  
Avec les valeurs numériques de la question d'examen:
$P_2 = \qty{1}{\watt} \cdot 10^{\frac{\qty{16}{\dB}}{\qty{10}{\dB}}} = \qty{39.81}{\watt}$

# Solution 2
Nous utilisons le tableau du recueil de formules ainsi que la connaissance de la loi des logarithmes :  
Le logarithme d'un produit correspond à l'addition des 
logarithmes des facteurs:

$\log\left(a\right)+\log\left(b\right) = \log\left(a \cdot b\right)$

Avec les valeurs de l'énoncé et du tableau, nous obtenons pour le facteur d'amplification:

$\qty{16}{\dB} = \qty{6}{\dB} + \qty{10}{\dB} \rightarrow  4 \cdot 10 = 40$

Et donc:

$P_2 = \qty{1}{\watt} \cdot 40 = \qty{40}{\watt}$