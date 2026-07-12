Dans le cas de la modulation d'amplitude (AM) ainsi que de la modulation SSB, l'information à transmettre est transmise par une modification de l'amplitude de la porteuse haute fréquence. Nous avons déjà appris que dans le cas de la modulation de fréquence (FM), l'amplitude de la porteuse reste constante - l'information est ici transmise par une modification de la fréquence instantanée de la porteuse.

La figure [ref:e_frequenzmodulation_t] montre l'évolution temporelle d'un signal FM avec une amplitude constante. Un signal FM se caractérise donc par le fait que l'amplitude de la porteuse (idéalisée) reste constante, tandis que sa fréquence instantanée change en continu en fonction du signal de modulation.

<margin>
[picture:906:e_frequenzmodulation_t:Évolution temporelle d'un signal FM]
</margin>

[question:EE301]

---

La figure [ref:e_frequenzmodulation_frequenzhub] montre à titre d'exemple un signal sinusoïdal BF qui provoque une déviation de fréquence correspondante (excursion de fréquence) d'une porteuse haute fréquence dans le spectre. Cela signifie que dans un signal FM, l'information de volume est transmise par la *déviation de la fréquence porteuse (excursion de fréquence)*. Un signal BF plus fort entraînerait une plus grande déviation de la fréquence porteuse et donc une bande passante plus élevée du signal FM.

<margin>
[picture:827:e_frequenzmodulation_frequenzhub:Déviation de la porteuse lors de la modulation de fréquence]
</margin>

<indepth>
La bande passante occupée d'une émission FM est déterminée par l'excursion et la fréquence de modulation maximale. En première approximation, pour une faible excursion et une faible fréquence de modulation, la *formule de Carson* peut être appliquée. Elle indique dans quelle bande passante se trouvent $\qty{90}{\percent}$ de la puissance d'émission.

$B\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$
  
Ce sujet sera abordé plus en détail dans la classe A.
</indepth>

[question:EE306]
[question:EE304]

Pour respecter les prescriptions légales concernant la bande passante occupée d'un signal FM, le signal du microphone est d'abord limité en amplitude dans les émetteurs FM (par un amplificateur limiteur) et ensuite modulé sur la porteuse au moyen de la FM. Dans ce cas, l'excursion de fréquence du modulateur à pleine puissance est soit fixée, soit réglable au moyen d'un régulateur d'excursion.

[question:EE305]

Les signaux FM sont, du fait que l'information modulée n'est pas contenue dans l'amplitude, mais uniquement dans la fréquence, relativement insensibles aux perturbations d'amplitude (par exemple par des éclairs, des allumages, des moteurs) par rapport à l'AM ou au SSB. Cela présente des avantages, notamment en ce qui concerne la sensibilité aux perturbations, lors de l'utilisation dans les véhicules et dans des environnements perturbés.

[question:EE302]
[question:EE303]
