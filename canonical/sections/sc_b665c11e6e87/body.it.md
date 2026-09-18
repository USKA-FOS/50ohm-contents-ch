Un vantaggio fondamentale dell’elaborazione digitale dei segnali consiste nel fatto che le informazioni disponibili in formato digitale possono essere elaborate quasi arbitrariamente. Una sequenza di campioni di ingresso viene convertita in una sequenza di campioni di uscita mediante funzioni matematiche. Filtri digitali semplici, come passa-basso, passa-banda o passa-alto, possono essere realizzati in due modi diversi: come filtri FIR e come filtri IIR. FIR sta per *Finite Impulse Response* (risposta all’impulso finita) e IIR per *Infinite Impulse Response* (risposta all’impulso infinita).

La caratteristica principale dei filtri FIR, come suggerisce anche il termine "finite" (finito in tedesco), è che per il calcolo di un campione di uscita vengono utilizzati solo un numero limitato di campioni di ingresso. I filtri IIR, invece, utilizzano anche campioni di uscita già calcolati, che vengono reimmessi nell’elaborazione di ingresso. Grazie a questa retroazione, un singolo campione di ingresso può teoricamente influenzare in modo illimitato i campioni di uscita successivi.

I filtri digitali possono essere implementati sia in software su un DSP che in hardware programmabile su un FPGA. Inoltre, esistono i cosiddetti *Mixed Signal Frontends*, che integrano varie funzioni di elaborazione del segnale, come ad esempio filtri di decimazione, insieme a convertitori AD/DA in un unico chip, per eseguirle in modo il più possibile efficiente dal punto di vista energetico e alleggerire le fasi successive dell’elaborazione del segnale.

[question:AF631]

<indepth>
[picture:1133:a_fir:Filtro FIR]

La figura [ref:a_fir] mostra schematicamente la struttura di un filtro FIR. Un campione di ingresso viene scritto in una memoria di ingresso. Ad ogni ciclo di clock, i valori memorizzati vengono spostati di una posizione, come in un registro a scorrimento. Le prese dei singoli valori memorizzati vengono moltiplicate per i corrispondenti coefficienti del filtro e poi sommati. Il risultato viene emesso come campione di uscita.

Supponendo che i quattro coefficienti del filtro abbiano ciascuno il valore $\frac{1}{4}$, gli ultimi quattro campioni di ingresso vengono moltiplicati ciascuno per $\frac{1}{4}$ e poi sommati. Il campione di uscita è quindi la media dei ultimi quattro campioni di ingresso. Un tale filtro viene anche chiamato *media mobile*.

Una sequenza di ingresso $0,0,0,4,0,0,0,0$ porta quindi a una sequenza di uscita $0,0,0,1,1,1,1,0$.

Il filtro attenua quindi le variazioni rapide, cioè le componenti ad alta frequenza del segnale di ingresso. Le variazioni lente o le basse frequenze vengono invece lasciate passare in gran parte, mentre le variazioni rapide o le alte frequenze vengono attenuate. Una media mobile agisce quindi come un semplice filtro digitale passa-basso.

Il filtro esegue un’operazione di convoluzione, che tra l’altro è anche alla base di molte reti neurali che guidano l’intelligenza artificiale.