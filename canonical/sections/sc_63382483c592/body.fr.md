Pour réduire la bande passante maximale d’un signal BLU émis et utiliser efficacement le spectre de fréquences disponible, la bande passante maximale du signal BF d’un signal BLU ne doit pas dépasser $\qty{2,7}{\kilo\hertz}$. Cela permet un espacement minimal de $\qty{3}{\kilo\hertz}$ entre les signaux BLU, pour un fonctionnement sans interférences.

[question:AE208]
[question:AE209]

Si un signal BLU est surmodulé dans le modulateur de l’émetteur, cela génère des distorsions qui entraînent des émissions parasites. Ces émissions parasites sont communément appelées « splatter » et peuvent perturber les émissions voisines, car la bande passante du signal émis dépasse alors les $\qty{2,7}{\kilo\hertz}$ requis.
[question:AE205]

La voix de chaque personne possède un spectre de fréquences individuel. Pour une intelligibilité optimale des émissions BLU, les fréquences vocales élevées doivent être renforcées et les fréquences basses atténuées. Un égaliseur intégré à l’amplificateur du microphone de l’émetteur permet d’ajuster individuellement la réponse en fréquence du signal de modulation. Cela permet d’adapter de manière optimale la réponse en fréquence du microphone à l’opérateur.
[question:AE213]

---

Pour évaluer la qualité et la linéarité de la forme de l’enveloppe de modulation d’un émetteur BLU, un signal à deux tons peut être utilisé pour moduler l’émetteur BLU. Dans ce cas, l’émetteur BLU est modulé par un signal BF composé de deux fréquences BF superposées. Ces fréquences BF ne doivent pas être dans un rapport entier l’une par rapport à l’autre. La superposition de ces deux fréquences génère, dans le signal HF émis, des maxima et des minima (passages par zéro) du signal HF. Pour la modulation, on peut par exemple utiliser un ton de $\qty{700}{\hertz}$ et un ton de $\qty{1200}{\hertz}$. Cela produit, lors de la mesure du signal HF à l’aide d’un oscillogramme (sur une résistance de charge), une battement HF de $\qty{500}{\hertz}$, qui devrait idéalement être sinusoïdal. Le signal à deux tons permet également de mesurer la puissance d’enveloppe (PEP) d’un émetteur BLU en visualisant la forme d’onde sur l’oscilloscope.

[question:AI304]

<margin>
[picture:1092:a_ssb_zweiton:Signal à deux tons pour évaluer la forme de l’enveloppe de modulation d’un émetteur BLU]
</margin>

L’illustration [ref:a_ssb_zweiton] montre en 1. un signal à un seul ton, c’est-à-dire un simple ton BF sinusoïdal. Les illustrations 2. et 3. montrent comment ce signal à un seul ton est transposé en HF en AM ou en BLU. Le signal BLU en 3. se compose d’un seul composant HF à amplitude constante et apparaît donc comme une porteuse HF non modulée sur une fréquence décalée par rapport à la porteuse supprimée. Un tel signal à un seul ton ne permet cependant qu’une évaluation limitée de la qualité et de la linéarité d’un émetteur BLU ; en particulier, aucun produit d’intermodulation significatif entre plusieurs signaux utiles n’apparaît.

En 4., un signal utile à deux tons composé de la superposition de deux tons sinusoïdaux de $\qty{700}{\hertz}$ et $\qty{1200}{\hertz}$ est représenté. Les illustrations 5. et 6. montrent comment ce signal à deux tons est transposé en HF en AM ou en BLU. Dans le cas du signal BLU à deux tons en 6., deux composants HF apparaissent, espacés de $\qty{500}{\hertz}$. Leur superposition génère une oscillation périodique de l’enveloppe HF avec une fréquence de battement de $\qty{500}{\hertz}$. Cette enveloppe permet de mesurer la puissance crête de l’enveloppe (PEP) et sert également à évaluer la linéarité de l’émetteur, car les non-linéarités entraînent des produits d’intermodulation supplémentaires dans le spectre.

[question:AE207]

Pour les exercices suivants, la puissance de sortie de l’émetteur doit être déterminée en tant que puissance crête de l’enveloppe (PEP). La PEP décrit la puissance effective que l’émetteur délivre pendant le pic de l’enveloppe de modulation. Elle ne se réfère donc pas à la puissance moyenne sur l’ensemble de la modulation, mais à la valeur de puissance au maximum de l’enveloppe, comme illustré dans la figure [ref:a_pep_hüllkurve]. La tension de crête permettant de calculer la puissance efficace peut être lue sur l’oscillogramme. Il faut alors tenir compte du rapport de la sonde de mesure.

<margin>
[picture:875:a_pep_hüllkurve:Courbe d’enveloppe de modulation pour le calcul de la puissance]
</margin>

% Sonde 1:1 PEP
[question:AI305]

% Sonde 10:1 PEP
[question:AI306]