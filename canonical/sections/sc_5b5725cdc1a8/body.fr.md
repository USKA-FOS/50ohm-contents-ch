Un convertisseur de tension est nécessaire chaque fois qu'une tension électrique doit être convertie en une autre tension. En radioamateurisme, cela peut par exemple consister à générer $\qty{5}{\volt}$ pour un microcontrôleur à partir d'une alimentation $\qty{13,8}{\volt}$, ou à alimenter un ordinateur portable avec $\qty{19}{\volt}$ à partir d'une batterie $\qty{12}{\volt}$. Ces circuits sont appelés convertisseurs DC/DC. Si la tension est augmentée, on parle de convertisseur élévateur (Step-UP), si elle est réduite, de convertisseur abaisseur (Step-DOWN).

Toute conversion de tension entraîne des pertes. C'est pourquoi la puissance fournie est toujours inférieure à la puissance absorbée. Le rapport entre la puissance de sortie et la puissance d'entrée est appelé rendement $\eta$ :

$ \eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} $

Pour répondre aux questions suivantes, il faut appliquer la formule de puissance $P = U \cdot I$ afin de calculer les puissances d'entrée et de sortie. Le rendement peut ensuite être déterminé.

[question:AB213]
[question:AB214]

<indepth>
[photo:300:StepUpWandler: Convertisseurs abaisseur (Buck) et élévateur (Boost). Ici réglé en convertisseur élévateur de $\qty{7,2}{\volt}$ à $\qty{24}{\volt}$]
Ce convertisseur Buck-Boost peut être réglé pour fournir une tension de sortie de $\qty{0,5}{\volt}$ à $\qty{25}{\volt}$. La puissance maximale est de $\qty{25}{\watt}$. Grâce à son rendement très élevé, les transistors de commutation fonctionnent sans dissipateur thermique. Le mode de fonctionnement abaisseur (Step Down = Buck Mode) ou élévateur (Step Up = Boost Mode) peut être activé à l'aide du petit interrupteur de droite.
</indepth>