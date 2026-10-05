Le rapport signal sur bruit (SNR) est défini comme le rapport du signal utile au signal de bruit (noise), comme illustré dans la figure [ref:a_snr]. Plus le SNR d'un signal reçu est élevé, plus le signal utile se distingue du bruit pour une bande passante donnée.

<margin>
[picture:1097:a_snr:Signal-to-Noise Ratio (SNR)]
</margin>

[question:AF227]

Le facteur de bruit est souvent spécifié pour les préamplificateurs HF. Il décrit la dégradation du SNR lors du passage d'un signal à travers ce composant. Le facteur de bruit est déterminé comme le rapport de la valeur SNR d'entrée à la valeur SNR de sortie. Le facteur de bruit est généralement exprimé en décibels ($\unit{\dB}$) par logarithmisation. Un facteur de bruit de $\num{2}$ en notation linéaire correspond à $\qty{3}{\dB}$ en représentation logarithmique.

[question:AF228]
[question:AF229]

<indepth>
Selon la norme DIN, le facteur de bruit exprimé en $\unit{\decibel}$ est appelé mesure de bruit. Malheureusement, il existe une autre définition de la mesure de bruit, ce qui rend cette désignation peu répandue.
</indepth>

<indepth>
Le *facteur de bruit* décrit la mesure dans laquelle un composant électronique ou un étage amplificateur dégrade le rapport signal / bruit d'un signal.

Un amplificateur est destiné à amplifier un signal faible. Cependant, l'amplificateur lui-même génère un bruit supplémentaire.

On compare donc

- le rapport signal / bruit à l'entrée avec le

- rapport signal / bruit à la sortie.

Le facteur de bruit $F$ est défini comme

$F = \frac{(S/N)_\mathrm{entrée}}{(S/N)_\mathrm{sortie}}$

Où :

- $S$ = puissance de signal
- $N$ = puissance du bruit
- $F$ = facteur de bruit en tant que grandeur sans dimension

*Facteur de bruit en décibels*

Le facteur de bruit (noise figure, NF) est très souvent exprimé logarithmiquement en décibels :

$NF = 10 \cdot \log_{10}(F)\;\mathrm{dB}$
</indepth>
