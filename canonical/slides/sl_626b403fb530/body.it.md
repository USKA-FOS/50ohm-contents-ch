## Funzione del convertitore A/D

* Converte i segnali di ingresso analogici in campioni digitali  
* Essenziale per la digitalizzazione e l'ulteriore elaborazione dei segnali

---

### Aliasing e Antialiasing

* Teorema di campionamento: per una ricostruzione priva di errori, la frequenza di campionamento deve essere $\gt 2 \cdot f_{\mathrm{max}}$
* I segnali al di sopra della frequenza massima elaborabile possono apparire come alias errati  
* I filtri antialiasing (filtri passa-basso o passa-banda) sopprimono le frequenze alte indesiderate  
* Proteggono il convertitore A/D da effetti di aliasing errati

---

[question:AF620]

---

### Generatore di clock (generatore di frequenza di campionamento)

* Genera il clock temporale esatto per il campionamento  
* Determina quante volte al secondo viene acquisito un campione  
* Può essere impostato in modo fisso o regolato tramite controllo (ad es. microcontrollore)

---

### Quantizzazione ed errori di quantizzazione

* Durante la conversione A/D, i valori di ampiezza analogici vengono mappati su livelli fissi  
* Ciò porta a una rappresentazione discreta in valore del segnale originariamente continuo  
* Gli errori di quantizzazione si verificano perché non tutti i valori intermedi possono essere acquisiti esattamente

---

[question:AF607]

---

## Risoluzione del convertitore A/D

* Numero di livelli possibili rappresentabili digitalmente  
* Viene indicato in bit (ad es. $\qty{8}{\bit} = \num{256}$ livelli, $\qty{16}{\bit} = \num{65536}$ livelli)
* Spesso metà dei valori viene utilizzata per l'intervallo positivo e l'altra metà per l'intervallo negativo

---

[question:AF608]

---

### Jitter: instabilità temporali

* Il jitter descrive piccole fluttuazioni casuali nei tempi di campionamento  
* Un generatore di frequenza di campionamento instabile porta a ulteriori effetti di rumore nel segnale digitale  
* È necessario un elevato sforzo tecnico per garantire un clock preciso

---

[question:AF621]
