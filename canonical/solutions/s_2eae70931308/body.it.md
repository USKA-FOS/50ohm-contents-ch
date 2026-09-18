## Spiegazione

### Fonte per il calcolo della distanza di sicurezza

Il documento "Spiegazione delle procedure di valutazione secondo la BEMFV" dell’Agenzia federale delle reti (Bundesnetzagentur) del agosto 2013 fornisce chiarimenti.

Il paragrafo 1.2.2 (Esecuzione del calcolo del campo lontano) contiene la formula (5) per il calcolo della distanza di sicurezza, qui indicata con $r$:

$r = \sqrt(\frac{Z_0}{4 \cdot \pi}) \cdot \frac{\sqrt{P \cdot G_i}}{E_g} \cdot C$

Con $Z_0 = \qty{120\pi}{\Ohm}$, il primo fattore può essere semplificato in $\sqrt{\qty{30}{\Ohm}}$. Trascurando il fattore di perdita $C$, si ottiene la formula indicata nel quesito e negli strumenti ausiliari dell’Agenzia federale delle reti per il calcolo della distanza di sicurezza:

$d = \frac{\sqrt{\qty{30}{\Ohm} \cdot P_\mathrm{EIRP}}}{E}$

Il paragrafo 1.2.1 specifica che la formula sopra indicata per il calcolo della distanza di sicurezza è valida solo nel campo lontano di una sorgente di radiazioni.

Inoltre, in tale paragrafo viene fatta una distinzione tra il *campo reattivo vicino* e il *campo radiante vicino*.

### Campo reattivo vicino

Ci si trova nel campo reattivo vicino di un’antenna quando la distanza dall’antenna è

$d < \frac{\lambda}{2\pi}$

In questo caso vale:

"All’interno del campo reattivo vicino possono verificarsi localmente forti aumenti del campo elettrico e magnetico, che non possono essere determinati con il calcolo del campo lontano. Pertanto, in questa zona non è consentito utilizzare il calcolo del campo lontano."

### Campo radiante vicino

Ci si trova nel campo radiante vicino di un’antenna quando

* ci si trova al di fuori del campo reattivo vicino e
* la distanza dall’antenna è inferiore a $4 \lambda$.

In questo caso vale:

"Se la formula del campo lontano viene applicata nel campo radiante vicino, per la maggior parte delle forme di antenna si ottengono stime conservative, cioè i valori reali del campo sono inferiori a quelli calcolati. Tuttavia, ciò non vale per tutti i tipi di antenna: ad esempio, un’antenna magnetica nel campo vicino genera campi più intensi di quelli previsti dalla formula del campo lontano. In particolare, le antenne che sono geometricamente piccole rispetto alla lunghezza d’onda mostrano un tale comportamento."

### Calcoli del campo vicino

Il paragrafo 1.3 tratta la possibilità di calcolare il campo vicino tramite simulazione:

"Utilizzando metodi numerici, come quelli impiegati nei cosiddetti programmi di calcolo del campo vicino, è possibile calcolare con precisione, per qualsiasi punto dello spazio circostante un’antenna, i campi elettrici e magnetici in termini di valore assoluto e fase."

### Interpretazione

Dalle spiegazioni sul campo reattivo vicino, campo radiante vicino e sui calcoli del campo vicino si può giustificare la risposta fornita in precedenza.