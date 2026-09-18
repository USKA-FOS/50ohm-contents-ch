Questo circuito funziona come raddrizzatore di tensione a doppia semionda o come rivelatore di picco-picco. Vengono rilevate la semionda positiva e quella negativa del segnale RF, in modo che all’uscita sia disponibile approssimativamente la tensione picco-picco meno le tensioni di conduzione dei due diodi.

$U_{\mathrm{SS}} = \qty{15,3}{\volt} + 2 \cdot \qty{0,23}{\volt} = \qty{15,76}{\volt}$

Da

$U_{\mathrm{SS}} = 2 \cdot \hat{U}$

ne consegue che il valore di picco della tensione RF alla presa intermedia da $\qty{5}{\ohm}$ sia:

$\hat{U} = \frac{U_{\mathrm{SS}}}{2} = \qty{7,88}{\volt}$

La tensione viene misurata su una presa intermedia da $\qty{5}{\ohm}$ di un carico fittizio complessivo da $\qty{50}{\ohm}$. Poiché attraverso l’intero carico fittizio circola la stessa corrente, le tensioni sono proporzionali alle resistenze. La tensione di picco RF sull’intero carico fittizio è quindi:

$\hat{U}_{\mathrm{trasmettitore}} = \frac{\qty{50}{\ohm}}{\qty{5}{\ohm}} \cdot \hat{U} = 10 \cdot \qty{7,88}{\volt} = \qty{78,8}{\volt}$

Con

$\hat{U} = U_{\mathrm{eff}} \cdot \sqrt{2}$

e

$P = \frac{U_{\mathrm{eff}}^2}{R}$

si ottiene:

$P = \frac{\hat{U}_{\mathrm{trasmettitore}}^2}{2R} = \frac{(\qty{78,8}{\volt})^2}{2 \cdot \qty{50}{\ohm}} \approx \qty{62}{\watt}$

La potenza RF del trasmettitore è quindi di circa $\qty{60}{\watt}$.