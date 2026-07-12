Grâce à la faible dépense, le redresseur en pont est un circuit redresseur fréquemment utilisé. Pour cela, on a besoin d'un transformateur et de 4 diodes.

<latexonly>
Dans l'illustration [ref:a_brueckenlgeichrichter] est représenté un tel redresseur en pont.

<margin>
[picture:965:a_brueckenlgeichrichter:Redresseur en pont]
</margin>
</latexonly>

<webonly>
Dans l'applet adjacent est représenté un tel redresseur en pont. On peut suivre le courant de charge dans son évolution et constater que celui-ci circule toujours dans la même direction à travers la résistance de charge $R$.

<margin>
[include:applet_gleichrichter_2]
</margin>
</webonly>

<tip>
[picture:67:a_brueckenlgeichrichter_2:Disposition des diodes dans le redresseur en pont]
Dans le redresseur en pont, les diodes pointent avec leurs cathodes vers le pôle positif et les anodes vers le pôle négatif. On peut donc se souvenir : les "traits" des diodes se rencontrent à la sortie positive. Cette disposition ne doit pas être confondue avec un mélangeur en anneau de diodes, que nous apprendrons plus tard. 
</tip>

[question:AD305]

---

Si l'on installe un condensateur de charge $C_L$ et un filtre LC après le redresseur en pont (voir figure [ref:a_netzteil_Ucs]), on obtient une amplitude plus petite dans la tension continue de sortie pulsée. Ainsi, nous avons une alimentation conventionnelle. 

<margin>
[picture:66:a_netzteil_Ucs:Circuit redresseur avec filtrage]
</margin>

Même dans le redresseur en pont, le condensateur se charge à la tension de crête $\hat{U}$ de la tension secondaire $U_{\mathrm{sek}}$ du transformateur.

$\hat{U}=U_{\mathrm{eff}}\cdot\sqrt{2}$

De plus, nous devons tenir compte du fait que le transformateur présente un rapport de transformation $ü$. Avec cette connaissance, nous pouvons résoudre l'exercice suivant.

[question:AD306]

<indepth>
[photo:296: Brückengleichrichter Bauformen: Formes de construction des redresseurs en pont]
L'étiquetage des connexions doit être pris en compte.

1. Redresseur en pont haute intensité 26 MB 20 A ($\qty{200}{\volt}$, $\qty{20}{\ampere}$) dans un boîtier métallique pour montage direct sur un dissipateur thermique
2. B80 C 5000/3300 signifie : tension de service maximale $\qty{80}{\volt}$, charge capacitive maximale $\qty{2500}{\micro\farad}$ avec résistance de protection $R = \qty{1}{\ohm}$, courant de charge continu maximal : $\qty{5000}{\milli\ampere}$ avec dissipateur thermique, $\qty{3300}{\milli\ampere}$ sans dissipateur thermique
3. BY 225 Redresseur en pont - boîtier spécial
4. Forme ronde d'un redresseur en pont B 80 C 1000
5. B40 C 1500 - la séquence modifiée des connexions doit être prise en compte
6. FPU 4M ($\qty{1000}{\volt}$, $\qty{4}{\ampere}$)
7. séquence des connexions imprimée dans le plastique
</indepth>
