Un oscilloscope est un voltmètre qui permet de visualiser l’évolution temporelle des tensions. Comme les autres voltmètres, les oscilloscopes possèdent une résistance interne élevée. La plupart du temps, il est possible de mesurer simultanément deux tensions ou plus. L’appareil illustré dans la figure [ref:e_oszilloskop_digital] est par exemple réglé de manière à partager l’écran entre deux signaux.

<margin>
[photo:212:e_oszilloskop_digital: Oscilloscope doté de nombreuses fonctions supplémentaires]
</margin>

Examinons plus en détail l’affichage de l’oscilloscope dans la figure [ref:e_oszilloskop_bildschirmfoto_sinus]. Un oscilloscope permet par exemple de déterminer les grandeurs caractéristiques d’une tension alternative sinusoïdale ($T$, $\hat{U}$, $U_\text{SS}$ et $U_\text{eff}$). Outre l’évolution du signal, une indication de temps et de tension est superposée à l’écran – dans l’exemple, $\qty{50,0}{\nano\seconde}$ et $\qty{500}{\milli\volt}$. Cela signifie qu’un carré en direction horizontale correspond à 50 nanosecondes et qu’un carré en direction verticale correspond à 500 millivolts. Ces carrés sont souvent appelés divisions ou échelons de l’échelle, d’où la notation $\qty{500}{\milli\volt\per\oscidiv}$.

<margin>
[photo:214:e_oszilloskop_bildschirmfoto_sinus: Une tension sinusoïdale affichée sur un oscilloscope numérique]
</margin>

---

On peut se représenter cela comme un système de coordonnées et lire la durée d’une période ($T$) ainsi que l’amplitude ($\hat{U}$). Dans l’exemple, une période s’étend sur 5 carrés ou échelons. Multipliée par $\qty{50,0}{\nano\seconde}$ par échelon, cela donne une durée de période de $\qty{250,0}{\nano\seconde}$. L’amplitude, c’est-à-dire la plus grande déviation par rapport à la position nulle, est de $\qty{1500}{\milli\volt}$ ou $\qty{1,5}{\volt}$, car elle s’élève sur 3 échelons et chaque échelon correspond à $\qty{500}{\milli\volt}$.

[question:EI301]

<tip>
Pour des mesures simples, de nombreux oscilloscopes numériques disposent d’une touche AUTO. En appuyant dessus, certains réglages sont effectués automatiquement et une image stable des signaux appliqués apparaît généralement. L’affichage peut être déplacé horizontalement. Un bouton rotatif doté de cette fonction est souvent étiqueté « X-Position ». Pour lire la durée d’une période, on déplace un point marquant, comme un passage par zéro, sur une ligne verticale du quadrillage et on compte le nombre d’échelons correspondant à une période.
</tip>

---

Dès que la durée d’une période d’une oscillation est connue, il est possible d’en déduire la fréquence. Dans la classe N, nous avons déjà appris la relation qualitative : la fréquence indique le nombre d’oscillations par seconde. Si la durée d’une période est d’une seconde, la fréquence est de $\qty{1}{\hertz}$. Si l’on divise la durée de la période par deux, soit une demi-seconde, deux oscillations s’inscrivent en une seconde – la fréquence est alors de $\qty{2}{\hertz}$.

Dans la classe E, nous considérons maintenant cette relation sous forme de formule :

$f=\dfrac{1}{T}$ ou $T=\dfrac{1}{f}$

La fréquence en hertz est l’inverse de la durée de la période en secondes.

Le signal dans la figure [ref:e_oszilloskop_bildschirmfoto_sinus] a donc la fréquence

$f = \dfrac{1}{\qty{250}{\nano\seconde}} = \qty{4}{\mega\hertz}$.

[question:EB408]
[question:EB409]
[question:EB411]
[question:EB410]
[question:EI302]

---

Parfois, les signaux sont déformés de manière indésirable. Cela se produit par exemple lorsqu’une tension d’entrée trop élevée est appliquée à un amplificateur. On dit alors que l’amplificateur est surmodulé et que son signal de sortie est distordu. Des distorsions marquées comme dans la figure [ref:e_oszilloskop_verzerrt] peuvent être détectées à l’aide d’un oscilloscope. Pour évaluer les signaux audio en radioamateurisme, cela suffit généralement.

<margin>
[photo:215:e_oszilloskop_verzerrt: Signal d’entrée sinusoïdal (en haut) et signal de sortie distordu d’un amplificateur surmodulé]
</margin>

<indepth>
Un oscilloscope ne permet pas d’évaluer correctement si un signal haute fréquence est exempt de distorsions pouvant affecter d’autres bandes de fréquences. Pour cela, un analyseur de spectre est l’appareil de mesure approprié.
</indepth>

% EI304 Distorsions BF
[question:EI304]