Dans la modulation d'amplitude (AM) ainsi que dans le BLU, l'information à transmettre est transmise par une variation de l'amplitude de la porteuse haute fréquence. Dans le chapitre [sec:fm], nous avons déjà appris que dans la modulation de fréquence (FM), l'amplitude de la porteuse reste en revanche constante – l'information y est transmise par une variation de la fréquence instantanée de la porteuse.

La figure [ref:e_frequenzmodulation_t] montre l'évolution temporelle d'un signal FM à amplitude constante. Un signal FM peut donc être reconnu au fait que l'amplitude de la porteuse (idéalement) reste constante, tandis que sa fréquence instantanée varie en permanence en fonction du signal de modulation.

<margin>
[picture:906:e_frequenzmodulation_t:Évolution temporelle d'un signal FM]
</margin>

[question:EE301]

---

La figure [ref:e_frequenzmodulation_frequenzhub] montre à titre d'exemple un signal sinusoïdal BF qui provoque une déviation de fréquence correspondante (excursion de fréquence porteuse) d'une porteuse haute fréquence dans le spectre. Autrement dit, dans un signal FM, l'information de volume est transmise par la *déviation de la fréquence porteuse (excursion de fréquence porteuse)*. Un signal BF plus fort entraînerait une plus grande déviation de la fréquence porteuse et donc une bande passante plus large du signal FM.

<margin>
[picture:827:e_frequenzmodulation_frequenzhub:Déviation de la porteuse en modulation de fréquence]
</margin>

<indepth>
La bande passante occupée d'une émission FM est déterminée par l'excursion de fréquence porteuse et la fréquence de modulation maximale. En première approximation, pour une excursion de fréquence porteuse faible et une fréquence de modulation basse, on peut appliquer la *formule de Carson*. Elle indique dans quelle bande passante se trouve $\qty{99}{\percent}$ de la puissance d'émission.

$B\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$

Ce sujet est abordé plus en détail dans [sec:fm_3].
</indepth>

[question:EE306]
[question:EE304]

Pour respecter les exigences légales concernant la bande passante occupée d'un signal FM, le signal du microphone est d'abord limité en amplitude (par un amplificateur limiteur) dans les émetteurs FM, puis modulé sur la porteuse par FM. Dans ce cas, l'excursion de fréquence porteuse du modulateur, pour une excitation maximale du volume, est soit fixe, soit réglable au moyen d'un régulateur d'excursion.

[question:EE305]

Les signaux FM sont, du fait que l'information modulée n'est pas contenue dans l'amplitude mais uniquement dans la fréquence, relativement peu sensibles aux perturbations d'amplitude (par exemple, dues à la foudre, aux systèmes d'allumage, aux moteurs) par rapport à l'AM ou au BLU. Cela présente des avantages particuliers lors de l'utilisation dans des véhicules et dans des environnements perturbés en termes de sensibilité aux interférences.

[question:EE302]
[question:EE303]