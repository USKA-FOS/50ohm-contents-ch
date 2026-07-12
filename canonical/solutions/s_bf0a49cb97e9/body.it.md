Si cerca l'intervallo della resistenza di ingresso del circuito. La resistenza sinistra con $\qty{200}{\ohm}$ è sempre in serie al resto del circuito.

Dopo questa resistenza, il circuito si divide in due rami paralleli:

* un ramo con $\qty{100}{\ohm}$
* un ramo con $\qty{200}{\ohm} + R$

Consideriamo prima il valore più piccolo. Per fare ciò, impostiamo:

$ R = \qty{0}{\ohm} $

Quindi $\qty{100}{\ohm}$ è in parallelo a $\qty{200}{\ohm}$:

$ R_\mathrm{par} = \frac{\qty{100}{\ohm} \cdot \qty{200}{\ohm}}{\qty{100}{\ohm} + \qty{200}{\ohm}} \approx \qty{67}{\ohm} $

Con la resistenza collegata a monte, si ottiene:

$ R_\mathrm{min} = \qty{200}{\ohm} + \qty{67}{\ohm} = \qty{267}{\ohm} $

Ora consideriamo il valore più grande. Per fare ciò, impostiamo:

$ R = \qty{1}{\kilo\ohm} $

Quindi $\qty{100}{\ohm}$ è in parallelo a $\qty{200}{\ohm} + \qty{1}{\kilo\ohm}$, cioè in parallelo a $\qty{1200}{\ohm}$:

$ R_\mathrm{par} = \frac{\qty{100}{\ohm} \cdot \qty{1200}{\ohm}}{\qty{100}{\ohm} + \qty{1200}{\ohm}} \approx \qty{92}{\ohm} $

Con la resistenza collegata a monte, si ottiene:

$ R_\mathrm{max} = \qty{200}{\ohm} + \qty{92}{\ohm} = \qty{292}{\ohm} $

La resistenza di ingresso si trova quindi nell'intervallo da circa $\qtyrange{267}{292}{\ohm}$.