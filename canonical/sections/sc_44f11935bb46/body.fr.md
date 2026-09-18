Comme aucun circuit ne fonctionne de manière idéale, une tension continue parfaitement constante ne s'applique à la résistance de charge $R_L$ d'un redresseur, mais une tension pulsatoire. Elle résulte des demi-ondes sinusoïdales positives successives et de l'effet de lissage des condensateurs. Cette composante de tension alternative résiduelle est appelée **ondulation résiduelle**.

Sa fréquence est de $f=\qty{100}{\hertz}$, car la demi-onde négative est également réfléchie dans la zone positive, doublant ainsi la fréquence du réseau de $\qty{50}{\hertz}$. Si l'on injectait cette tension continue pulsatoire dans un amplificateur avec haut-parleur via un diviseur de tension, on pourrait entendre un bourdonnement à $\qty{100}{\hertz}$.


<webonly>
<margin>
[include:applet_brumm]
</margin>
</webonly>

[question:AD310]


Cette tension peut être visualisée à l'oscilloscope en n'affichant que la composante alternative (voir figure [ref:a_AC-Kopplung] : couplage AC de l'entrée).


<indepth>
[photo:306:a_AC-Kopplung:Couplage AC - DC de l'entrée de l'oscilloscope]
Avec la touche "GD", l'entrée de l'oscilloscope est mise à zéro volt.
En position non enfoncée de la touche AC/DC, un couplage capacitif de l'entrée de l'oscilloscope est activé et seule la composante alternative du signal d'entrée est affichée.
En position enfoncée de la touche AC/DC, un couplage galvanique de l'entrée de l'oscilloscope est activé et la composante continue d'une tension alternative est également affichée.
</indepth>


Dans la question suivante, il faut déterminer la fréquence ainsi que l'amplitude de l'ondulation résiduelle.

[question:AD309]