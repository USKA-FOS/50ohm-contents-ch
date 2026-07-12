Un oscilloscope est un appareil de mesure de tension qui peut visualiser l'évolution temporelle des tensions. Tout comme d'autres appareils de mesure de tension, les oscilloscopes ont une résistance interne élevée. On peut généralement mesurer deux tensions ou plus simultanément. L'appareil de l'Abbildung [ref:e_oszilloskop_digital] est par exemple réglé de manière à ce que deux signaux partagent l'écran.

<margin>
[photo:212:e_oszilloskop_digital:Oscilloscope avec de nombreuses fonctions supplémentaires]
</margin>

Examinons maintenant plus en détail l'affichage de l'oscilloscope dans l'Abbildung [ref:e_oszilloskop_bildschirmfoto_sinus]. Avec un oscilloscope, on peut par exemple déterminer les grandeurs caractéristiques d'une tension alternative sinusoïdale ($T$, $\hat{U}$, $U_\text{SS}$ et $U_\text{eff}$). En plus de la courbe du signal, une indication de temps et de tension est affichée - dans l'exemple $\qty{50,0}{\nano\second}$ et $\qty{500}{\milli\volt}$. Cela signifie qu'un carré dans la direction horizontale correspond à 50 nanosecondes et dans la direction verticale à 500 millivolts. Ces carrés sont souvent appelés divisions ou parties d'échelle, d'où l'écriture $\qty{500}{\milli\volt\per\oszidiv}$.

<margin>
[photo:214:e_oszilloskop_bildschirmfoto_sinus:une tension sinusoïdale, représentée sur un oscilloscope numérique]
</margin>

---

On peut se représenter cela comme un système de coordonnées et lire la durée de la période ($T$) et l'amplitude ($\hat{U}$). Dans l'exemple, une période est longue de 5 carrés ou parties d'échelle. Multipliée par $\qty{50,0}{\nano\second}$ par partie d'échelle, cela donne la durée de la période $\qty{250,0}{\nano\second}$. L'amplitude, c'est-à-dire la plus grande déviation par rapport à la position nulle, est de $\qty{1500}{\milli\volt}$ ou $\qty{1,5}{\volt}$, car elle est haute de 3 parties d'échelle et chaque partie correspond à $\qty{500}{\milli\volt}$. 

[question:EI301]

<tip>
Pour des mesures simples, de nombreux oscilloscopes numériques ont une touche AUTO. Si on l'appuie, plusieurs réglages sont effectués automatiquement et généralement une image fixe des signaux appliqués apparaît. L'affichage peut être déplacé horizontalement. Un bouton rotatif avec cette fonction est souvent étiqueté X-Position. Pour lire la durée de la période, on déplace un point marquant comme un passage par zéro sur une ligne verticale de la grille et on compte combien de parties d'échelle correspondent à une période.
</tip>
 
---

Dès que la durée de la période d'une oscillation est connue, on peut en déduire la fréquence. Dans la classe N, nous avons déjà connu la relation qualitative : la fréquence indique le nombre d'oscillations par seconde. Si la durée de la période est d'une seconde, la fréquence est de $\qty{1}{\hertz}$. Si nous réduisons la durée de la période à une demi-seconde, deux oscillations s'inscrivent dans une seconde - la fréquence est alors de $\qty{2}{\hertz}$.

Dans la classe E, nous considérons maintenant cette relation sous forme de formule :
  
$f=\dfrac{1}{T}$ ou $T=\dfrac{1}{f}$

La fréquence en Hertz est l'inverse de la durée de la période en secondes.

Le signal de l'Abbildung [ref:e_oszilloskop_bildschirmfoto_sinus] a donc la fréquence

$f = \dfrac{1}{\qty{250}{\nano\second}} = \qty{4}{\mega\hertz}$.
 
[question:EB408]
[question:EB409]
[question:EB411]
[question:EB410]
[question:EI302]

---

Parfois, les signaux sont déformés de manière involontaire. Cela se produit par exemple lorsqu'une tension d'entrée trop élevée est injectée dans un amplificateur. On dit alors que l'amplificateur est surmodulé et que son signal de sortie est distordu. De fortes distorsions comme dans l'Abbildung [ref:e_oszilloskop_verzerrt] peuvent être détectées avec un oscilloscope. Pour l'évaluation des signaux audio dans le radioamateur, cela suffit généralement.

<margin>
[photo:215:e_oszilloskop_verzerrt:signal d'entrée sinusoïdal (en haut) et signal de sortie distordu d'un amplificateur surmodulé]
</margin>

<indepth>
On ne peut pas bien évaluer avec un oscilloscope si un signal haute fréquence est exempt de distorsions qui affectent d'autres plages de fréquences. Pour cela, un analyseur de spectre est l'appareil de mesure approprié.
</indepth>

% EI304 Distorsions NF 
[question:EI304]