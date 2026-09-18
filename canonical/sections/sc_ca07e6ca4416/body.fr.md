Une boucle à verrouillage de phase (PLL) peut par exemple synchroniser un oscillateur contrôlé en tension (VCO) variable et potentiellement instable avec un oscillateur de référence stable (G). Pour cela, elle compare les phases des deux signaux et régule le VCO de manière à obtenir une fréquence de sortie stable. Dans le radioamateurisme, les PLL sont principalement utilisées pour une génération de fréquence stable et précise dans les émetteurs et récepteurs, par exemple pour la sélection de canaux, la génération de fréquences de mélange et la synchronisation d’oscillateurs.

Une PLL est composée principalement des éléments suivants :

* *Comparateur de phase* : compare les phases des signaux du VCO et de l’oscillateur de référence.
* *Filtre passe-bas* : convertit les impulsions générées par le comparateur de phase en une tension continue.
* *VCO* : génère le signal de sortie dont la fréquence est contrôlée par la tension continue fournie par le filtre passe-bas.

[question:AD701]

Optionnellement, la PLL peut être complétée par un *diviseur de fréquence* pour synchroniser la fréquence du VCO sur des multiples de la fréquence de référence.

<margin>
[picture:45:a_oszillator_pll:Schéma d’une boucle à verrouillage de phase (PLL)]
</margin>

---

Le comparateur de phase mesure la différence de phase entre les signaux du VCO ($f_\mathrm{out}$) et de l’oscillateur de référence ($f_\mathrm{ref}$). En cas d’écart de phase, il émet des impulsions correspondant à l’erreur. Ces impulsions sont lissées par le filtre passe-bas et converties en une tension continue proportionnelle. La tension continue générée sert de signal de commande pour le VCO, qui régule sa fréquence de manière à réduire progressivement l’écart de phase jusqu’à zéro. Lorsque cet état est atteint, on dit que la PLL est « verrouillée » (locked), c’est-à-dire dans un *état stable*. Dans l’état stable de la PLL, les fréquences et les phases des deux signaux sont identiques. On a alors :

$f_\mathrm{ref}=\frac{f_\mathrm{out}}{n}$

La fréquence de sortie est stable et correspond essentiellement à la fréquence de référence ou à ses multiples (selon le rapport de division choisi du diviseur de fréquence).

Le principe de fonctionnement est illustré par un exemple simple dans la figure [ref:a_oszillator_pll] : l’oscillateur de référence fournit en point A une fréquence de $f_\mathrm{ref}=\qty{10}{\mega\hertz}$. La fréquence de sortie du VCO est divisée en point C par le diviseur de fréquence avec un rapport de division $n=100$. Lorsque la PLL est verrouillée, c’est-à-dire dans l’*état stable*, les fréquences aux points A et B sont égales. On obtient ainsi pour la fréquence de sortie :

$f_\mathrm{out}=n\cdot f_\mathrm{ref}=100\cdot\qty{10}{\mega\hertz}=\qty{1}{\giga\hertz}$

Le VCO génère donc une fréquence de $\qty{1}{\giga\hertz}$, qui est divisée par le diviseur de fréquence à $\qty{10}{\mega\hertz}$ et comparée à la fréquence de référence.

<indepth>
Une PLL peut être conçue de manière analogique, numérique ou hybride. Dans les appareils radio, on combine souvent des comparateurs de phase et des diviseurs de fréquence numériques avec un filtre de boucle analogique et un VCO.
</indepth>

[question:AD702]

La précision et la stabilité de la fréquence de sortie de la PLL dépendent en premier lieu de la qualité de l’oscillateur de référence, qui est généralement un oscillateur à quartz.

[question:AD705]

Pour régler une PLL sur différentes fréquences, cela peut être réalisé par le diviseur de fréquence. Cela permet de générer la fréquence de sortie comme un multiple entier de la fréquence de référence. Le plus petit intervalle de fréquence sélectionnable correspond alors à la fréquence de l’oscillateur de référence, car la division ne peut se faire que par pas entiers. Pour un appareil radio FM avec une grille de canaux de $\qty{12,5}{\kilo\hertz}$, on peut donc utiliser une fréquence de comparaison de $\qty{12,5}{\kilo\hertz}$. Si le rapport de division $n$ est augmenté ou diminué de un, la fréquence de sortie change alors de $\qty{12,5}{\kilo\hertz}$. De cette manière, la PLL peut être réglée sur les différents canaux radio.

[question:AD703]

Pour obtenir une fréquence de sortie donnée avec une fréquence de référence donnée, le facteur de division est choisi de manière à ce que la même fréquence soit présente aux entrées du comparateur de phase. Cela permet de calculer le rapport de division nécessaire pour la fréquence de sortie souhaitée.

[question:AD704]