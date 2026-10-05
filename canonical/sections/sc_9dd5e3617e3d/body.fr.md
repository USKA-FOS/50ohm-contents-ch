**EN TRAITEMENT**
**TODO: Insérer simulation : https://tinyurl.com/22m65xlw**


Comme déjà montré dans la section [sec:gleichrichter_1], une seule diode ne laisse passer que la demi-onde positive. Pour qu'une tension continue utilisable en résulte, au moins un condensateur supplémentaire est nécessaire, qui lisse la tension de sortie pulsante (voir le circuit [ref:a_einweggleichrichtung_c]).

<margin>
[picture:795:a_einweggleichrichtung_c:Redressement simple alternance avec condensateur]
</margin>

---

Pendant la demi-onde positive, la diode $D$ conduit et laisse le courant circuler. Pendant ce temps, le condensateur $C_L$ se charge jusqu'à la valeur de crête de la tension alternative. Au moment de la demi-onde négative, la diode $D$ bloque le courant et le condensateur $C_L$ se décharge à travers la résistance de charge $R_L$.

Ainsi, une tension continue légèrement pulsante $U_L$ s'établit aux bornes de la résistance de charge $R_L$ (cf. fig.[ref:a_Restwelligkeit]). Plus la capacité du condensateur est grande, plus la tension continue aux bornes de la résistance de charge est lissée de manière uniforme.

<margin>
[picture:75:a_Restwelligkeit:Ondulation de la tension de sortie continue $U_L$]
</margin>

Pour le dimensionnement de la diode et du condensateur, nous devons cependant savoir que les tensions du transformateur sont indiquées comme tensions efficaces $U_{\mathrm{eff}}$. Nous devons donc d'abord déterminer la tension de crête $\hat{U}$.

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}}$

Si, par exemple, la tension $U_a = \qty{15}{\volt}$ est indiquée sur un transformateur, nous calculons :

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}} = \sqrt{2} \cdot \qty{15}{\volt} = \qty{21,21}{\volt}$

Ainsi, sans charge, une tension de crête à vide d'environ $\qty{21}{\volt}$ s'établira.

[question:AD302]

Pour la question suivante, nous devons appliquer le rapport de transformation du transformateur pour déterminer notre tension de sortie. Nous substituons donc pour la tension d'entrée efficace $U_{\mathrm{eff}}$ un vingtième de la tension d'entrée du transformateur de $\qty{230}{\volt}$. À partir de la tension de crête, nous pouvons alors ajouter la moitié de la tension à nouveau pour prendre en compte la marge de sécurité.

[question:AD303]

Pour résoudre la tâche suivante, nous devons reconnaître que la valeur de crête de la demi-onde négative et la tension du condensateur s'additionnent et soumettent la diode à une tension inverse. C'est la tension la plus élevée qui peut apparaître aux bornes de la diode en polarisation inverse.

Nous calculons : $U_{\mathrm{sperr}} = 2 \cdot \hat{u}$
Il faut ensuite prendre en compte le rapport de transformation $5 : 1$ du transformateur secteur et la marge de sécurité de $\qty{20}{\percent}$.

[question:AD304]

%TODO Insérer simulation : https://tinyurl.com/22m65xlw
