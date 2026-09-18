Dans la classe N, nous avons déjà appris à connaître la *puissance rayonnée effective* (ERP). Contrairement à l'EIRP, elle ne se réfère pas à un radiateur isotrope, mais à un dipôle demi-onde. Pour le calcul, seule la puissance effectivement disponible au point d’alimentation de l’antenne est déterminante. Les pertes dans la ligne d’alimentation, par exemple dues à l’atténuation du câble, doivent donc être soustraites de la puissance de sortie de l’émetteur.

La puissance rayonnée effective résulte de la puissance fournie à l’antenne et du gain d’antenne dans la direction considérée :

$P_\mathrm{ERP}=P_\mathrm{Ant}\cdot G_\mathrm{d}$

Ici, $G_\mathrm{d}$ est le gain d’antenne rapporté à un dipôle demi-onde, exprimé comme facteur linéaire.

[question:AG501]

La puissance au point d’alimentation de l’antenne peut être déterminée à partir de la puissance de sortie de l’émetteur et de l’atténuation de la ligne d’alimentation. Pour cela, l’atténuation est convertie en un facteur d’atténuation linéaire $D$. Par exemple, pour une atténuation de $\qty{10}{\dB}$, ce facteur est de $\num{0,1}$, de sorte qu’un dixième seulement de la puissance de l’émetteur parvient à l’antenne :

$P_\mathrm{Ant}=D\cdot P_\mathrm{Émetteur}$

Ce n’est qu’ensuite que cette puissance effectivement fournie est multipliée par le gain d’antenne pour calculer l’ERP.

[question:AK104]

Pour la question suivante, il est impératif de prêter attention aux signes de calcul. Les pertes sont soustraites de la puissance d’émission, puis multipliées par le facteur de gain ($G_\mathrm{Antenne}$).
Comme il s’agit de calculer l’ERP, la référence doit se faire par rapport à un dipôle demi-onde.

[question:AG502]

Un indice pour la bonne solution de la question suivante est déjà donné dans l’[annexe 1 de l’AFUV](https://50ohm.de/a1). On y trouve comme puissance maximale pour la bande des $\qty{630}{\m}$ une ERP de $\qty{1}{\W}$. Un dipôle demi-onde pour cette fréquence aurait une longueur d’environ $\qty{315}{\m}$ et est donc à peine réalisable pour la plupart des radioamateurs. En pratique, on utilise donc souvent des antennes fortement raccourcies, dont le rendement est nettement inférieur à celui d’un dipôle demi-onde non raccourci. Un gain d’antenne de $\qty{-20}{\dBd}$ est donc tout à fait plausible. Comme le câble coaxial utilisé n’a qu’une faible longueur, son atténuation peut être négligée dans cette bande de fréquences. Essaie maintenant de résoudre la question suivante.

[question:AG503]