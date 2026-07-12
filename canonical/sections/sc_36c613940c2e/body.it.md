Gli oscillatori a frequenza variabile possono essere realizzati in vari modi. Un'opzione è il cosiddetto *oscillatore controllato in tensione VCO - Voltage controlled oscillator*.

[question:AD601]

---

Affinché la frequenza dell'oscillatore possa essere modificata, è possibile inserire nel suo circuito oscillante un diodo a capacità variabile, la cui capacità può essere influenzata da una tensione continua (cfr. figura [ref:a_vco_schaltung]). Una modifica di questa tensione continua porta quindi a una corrispondente modifica della frequenza dell'oscillatore. In questo modo, l'oscillatore diventa sintonizzabile tramite una tensione di controllo.

<margin>
[picture:752:a_vco_schaltung:Circuito VCO con diodo a capacità variabile]
</margin>

Il diodo a capacità variabile viene utilizzato in polarizzazione inversa. Maggiore è la tensione inversa del diodo, minore sarà la sua capacità, determinata dalla dimensione della zona di svuotamento (giunzione P-N). La zona di svuotamento aumenta all'aumentare della tensione di blocco applicata, riducendo la capacità e quindi aumentando la frequenza del circuito oscillante secondo la formula di Thomson per le oscillazioni.

Al contrario, la zona di svuotamento del diodo a capacità variabile diminuisce al diminuire della tensione di blocco applicata, aumentando la capacità e quindi diminuendo la frequenza del circuito oscillante. La tensione di blocco può essere generata, ad esempio, da un potenziometro o da un circuito di controllo.

%TODO: Possibile grafico sulla zona di svuotamento e sul comportamento nel diodo a capacità variabile.

[question:AD218] 

Per tutti i circuiti oscillanti, indipendentemente dalla loro implementazione, vale che i feedback indesiderati possono portare a instabilità di frequenza. Questo vale per i VCO così come per i VFO (ad es. con condensatori variabili) e altri oscillatori.

[question:AD611]