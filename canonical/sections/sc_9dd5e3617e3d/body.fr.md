Comme déjà montré au chapitre « Redresseur I » de la classe E, une seule diode ne laisse passer que la demi-onde positive. Pour obtenir une tension continue utilisable, il faut en outre au moins un condensateur qui lisse la tension de sortie pulsatoire (voir circuit [ref:a_einweggleichrichtung_c]).

<margin>
[picture:795:a_einweggleichrichtung_c:Redressement mono-alternance avec condensateur]
</margin>

---

Lors de la demi-onde positive, la diode $D$ conduit et laisse passer le courant. Pendant ce temps, le condensateur $C_L$ se charge à la valeur de crête de la tension alternative. Au moment de la demi-onde négative, la diode $D$ bloque le courant et le condensateur $C_L$ se décharge à travers la résistance de charge $R_L$.

Ainsi, une tension continue légèrement pulsatoire $U_L$ s'établit aux bornes de la résistance de charge $R_L$ (cf. fig. [ref:a_Restwelligkeit]). Plus la capacité du condensateur est grande, plus la tension continue aux bornes de la résistance de charge est lissée de manière uniforme.

<margin>
[picture:75:a_Restwelligkeit:Ondulation de la tension continue de sortie $U_L$]
</margin>

Pour dimensionner la diode et le condensateur, il faut savoir que les tensions du transformateur sont indiquées en tensions efficaces $U_{\mathrm{eff}}$. Il faut donc d'abord déterminer la tension de crête $\hat{U}$.

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}}$

Si une tension $U_a = \qty{15}{\volt}$ est indiquée sur un transformateur, nous calculons :

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}} = \sqrt{2} \cdot \qty{15}{\volt} = \qty{21,21}{\volt}$

Ainsi, en l'absence de charge, une tension de crête à vide d'environ $\qty{21}{\volt}$ s'établira.

[question:AD302]

Pour la question suivante, nous devons appliquer le rapport de transformation du transformateur pour déterminer notre tension de sortie. Nous utilisons donc pour la tension efficace d'entrée $U_{\mathrm{eff}}$ un vingtième de la tension d'entrée du transformateur de $\qty{230}{\volt}$. À partir de la tension de crête, nous pouvons ajouter à nouveau la moitié de la tension pour tenir compte de la marge de sécurité.

[question:AD303]

Pour résoudre la tâche suivante, nous devons reconnaître que la valeur de crête de la demi-onde négative et la tension du condensateur s'additionnent et sollicitent la diode en polarisation inverse. C'est la tension la plus élevée qui peut apparaître aux bornes de la diode en polarisation inverse.

Nous calculons : $U_{\mathrm{sperr}} = 2 \cdot \hat{u}$
Il faut ensuite tenir compte du rapport de transformation $5 : 1$ du transformateur secteur et de la marge de sécurité de $\qty{20}{\percent}$.

[question:AD304]

%TODO Intégrer simulation : https://tinyurl.com/22m65xlw