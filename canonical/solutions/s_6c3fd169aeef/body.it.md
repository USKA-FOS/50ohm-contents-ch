## Spiegazione

Una resistenza di scarica ad alta impedenza serve per scaricare in modo controllato i condensatori dell'alimentatore. Essa limita la corrente di scarica e riduce così il rischio di formazione di archi elettrici, danni ai componenti e pericoli elettrici.

### Perché una resistenza ad alta impedenza?

Durante la scarica di un condensatore, la corrente fluisce attraverso la resistenza di scarica $R$. Essa viene dimensionata in modo che:

* la corrente iniziale rimanga limitata:

    $I_0 = \frac{U_0}{R}$

* non si verifichino picchi di corrente pericolosamente elevati,
* non si formino archi elettrici,
* i componenti e le piste dei circuiti stampati siano protetti da sovraccarichi,
* la scarica avvenga comunque in un tempo ragionevole.

Una resistenza a bassa impedenza o un cortocircuito provocherebbero invece:

* correnti iniziali molto elevate,
* possibili danni al condensatore e alle piste dei circuiti,
* picchi di corrente e tensione incontrollati,
* un aumento del rischio di incendio e di lesioni


### Perché la potenza della resistenza deve essere sufficiente?

L'energia immagazzinata nel condensatore è:

$E = \frac{1}{2} \cdot C \cdot {U_0}^2$

Questa energia viene completamente convertita in calore nella resistenza durante la scarica.

La potenza dissipata iniziale è:

$P_0 = \frac{{U_0}^2}{R}$

Per $R = \qty{100}{\kilo\ohm}$ e $U_0 = \qty{400}{\volt}$ si ottiene quindi una potenza di $P_0 = \qty{1,6}{\watt}$.

Pertanto, la resistenza deve:

* avere una potenza nominale sufficiente,
* essere in grado di sopportare sovraccarichi per brevi periodi (funzionamento a impulsi),
* essere dimensionata termicamente in modo sicuro per evitare il surriscaldamento.