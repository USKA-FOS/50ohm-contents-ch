Le due diodi formano un raddrizzatore a *valore di picco* doppio. All'*uscita* vengono misurati $\qty{15,3}{\volt}$. Inoltre, devono essere considerate le tensioni di conduzione dei due diodi Schottky, ciascuna di $\qty{0,23}{\volt}$:

$U_\mathrm{SS} = \qty{15,3}{\volt} + 2 \cdot \qty{0,23}{\volt} = \qty{15,76}{\volt}$

Il *valore di picco* della tensione RF è quindi:

$\hat U = \frac{U_\mathrm{SS}}{2} = \frac{\qty{15,76}{\volt}}{2} = \qty{7,88}{\volt}$

Per il calcolo della potenza è necessario il valore efficace:

$U_\mathrm{eff} = \frac{\hat U}{\sqrt{2}} = \frac{\qty{7,88}{\volt}}{\sqrt{2}} \approx \qty{5,57}{\volt}$

Le *resistenze* da $\qty{56}{\ohm}$ e $\qty{470}{\ohm}$ sono in parallelo e formano approssimativamente un carico da $\qty{50}{\ohm}$:

$R = \qty{56}{\ohm} \parallel \qty{470}{\ohm} \approx \qty{50}{\ohm}$

Da ciò risulta la potenza RF:

$P = \frac{U_\mathrm{eff}^2}{R} = \frac{(\qty{5,57}{\volt})^2}{\qty{50}{\ohm}} \approx \qty{0,62}{\watt}$

La potenza RF è quindi di circa $\qty{600}{\milli\watt}$.