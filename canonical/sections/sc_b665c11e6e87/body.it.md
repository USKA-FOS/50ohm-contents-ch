Un vantaggio essenziale dell'elaborazione digitale dei segnali consiste nel fatto che le informazioni disponibili in forma digitale possono essere elaborate quasi arbitrariamente. Una sequenza di campioni di ingresso viene convertita in una sequenza di campioni di uscita mediante funzioni matematiche. Semplici filtri digitali, come passa-basso, passa-banda o passa-alto, possono essere implementati in due modi diversi: come filtri FIR e come filtri IIR. FIR sta per *Finite Impulse Response* e IIR per *Infinite Impulse Response*.

La caratteristica principale dei filtri FIR è, come indica già la denominazione "finite" (in tedesco: finito), che solo un numero limitato di campioni di ingresso viene utilizzato per il calcolo di un campione di uscita. I filtri IIR, invece, utilizzano anche campioni di uscita già calcolati, che vengono reimmessi nell'ingresso del calcolo. Attraverso questa retroazione, un singolo campione di ingresso può teoricamente influenzare i campioni di uscita successivi per un tempo illimitato.

I filtri digitali possono essere implementati sia in software su un DSP che in hardware programmabile su un FPGA. Inoltre, esistono i cosiddetti front-end a segnale misto, che realizzano varie funzioni di elaborazione del segnale, come ad esempio filtri di decimazione, insieme a convertitori AD/DA in un singolo chip, per eseguirle nel modo più efficiente dal punto di vista energetico e per alleggerire le fasi successive di elaborazione del segnale.

[question:AF631]

<indepth>
[picture:1133:a_fir:Filtro FIR]

La figura [ref:a_fir] mostra schematicamente la struttura di un filtro FIR. Un campione di ingresso viene scritto in una memoria di ingresso. Ad ogni ciclo, i valori memorizzati vengono spostati di una posizione di memoria come in un registro a scorrimento. I prelievi delle singole posizioni di memoria vengono moltiplicati per i corrispondenti coefficienti del filtro e successivamente sommati. Il risultato viene emesso come campione di uscita.

Supponendo che i quattro coefficienti del filtro abbiano ciascuno il valore $\frac{1}{4}$, gli ultimi quattro campioni di ingresso vengono moltiplicati ciascuno per $\frac{1}{4}$ e poi sommati. Il campione di uscita è quindi la media degli ultimi quattro campioni di ingresso. Un tale filtro è anche chiamato *media mobile*.

Una sequenza di ingresso $0,0,0,4,0,0,0,0$ porta quindi alla sequenza di uscita $0,0,0,1,1,1,1,0$.

Il filtro smorza quindi i cambiamenti rapidi, cioè le componenti ad alta frequenza del segnale di ingresso. I cambiamenti lenti, ovvero le basse frequenze, vengono in gran parte lasciati passare, mentre i cambiamenti rapidi, ovvero le componenti ad alta frequenza, vengono attenuati. Una media mobile agisce quindi come un filtro passa-basso digitale molto semplice.

Il filtro esegue un'operazione chiamata convoluzione, che è tra l'altro anche la base di molte reti neurali che alimentano l'intelligenza artificiale.
</indepth>

<indepth>
*FPGA*
indica un circuito integrato con il nome **F**ield **P**rogrammable **G**ate **A**rray. Si tratta di un componente hardware programmabile.
</indepth>
%TODO: FPGA è già apparso in precedenza -> spostare lì

