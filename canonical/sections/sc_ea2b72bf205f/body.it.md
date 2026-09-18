Come già appreso nelle classi N ed E, nella modulazione di frequenza le informazioni del segnale modulante non sono contenute nell’ampiezza, ma solo nella variazione di frequenza del segnale portante. Pertanto, nel ricevitore è necessario valutare solo i passaggi per lo zero del segnale portante.

Le fluttuazioni di ampiezza vengono eliminate da un amplificatore limitatore. Per questo motivo, la modulazione di frequenza è intrinsecamente insensibile alle interferenze impulsive di ampiezza, che possono essere causate, ad esempio, da scintille di accensione, motori elettrici o simili. La FM è quindi adatta per l’utilizzo in veicoli a motore.

[question:AE302]

Nella classe A esamineremo ora come viene generata la modulazione di frequenza in un trasmettitore e come calcolare la larghezza di banda di un segnale FM.

---

La modulazione di frequenza può essere generata modificando la capacità del condensatore determinante la frequenza all’interno di un oscillatore (cfr. [ref:fm_modulation_schaltung]). Ad esempio, utilizzando un diodo a capacità variabile, che è in serie a un circuito oscillante o a un quarzo, è possibile generare la modulazione di frequenza. L’ampiezza della frequenza bassa (BF), generata ad esempio da un microfono collegato al diodo a capacità variabile, determina direttamente la variazione di frequenza dell’oscillatore.

[question:AE303]

<margin>
[picture:155:fm_modulation_schaltung:Circuito semplice per la modulazione di frequenza di un oscillatore con diodo a capacità variabile]
</margin>

La frequenza di modulazione influisce su quante volte la frequenza dell’oscillatore cambia.

[question:AE301]

Nella classe E abbiamo già imparato a conoscere la *deviazione di frequenza portante*. Essa indica di quanto il valore istantaneo della frequenza del segnale FM viene deviato rispetto alla frequenza portante dal segnale modulante. Maggiore è l’ampiezza del segnale modulante, maggiore è questa deviazione di frequenza.

Durante la demodulazione nel ricevitore FM, questa deviazione di frequenza viene convertita nuovamente in un’ampiezza corrispondente del segnale demodulato. Una maggiore deviazione di frequenza porta quindi, a parità di altre condizioni, a un’ampiezza maggiore del segnale BF demodulato.

Una maggiore deviazione di frequenza aumenta la larghezza di banda necessaria del segnale FM. Se vengono superati i valori previsti, il segnale trasmesso può estendersi ai canali adiacenti e causare interferenze con i canali adiacenti.

[question:AE305]
[question:AE306]
[question:AE307]
[question:AE304]

---

In realtà, la larghezza di banda occupata da un’emissione FM non è determinata solo dalla deviazione, ma anche dalla frequenza massima di modulazione (cfr. figura [ref:fm_modulation]). In prima approssimazione, per una deviazione ridotta e una frequenza di modulazione bassa, è possibile applicare la formula di Carson. Essa indica in quale larghezza di banda si trova il $\qty{99}{\percent}$ della potenza di trasmissione.

$BW\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$

<margin>
[picture:910:fm_modulation:Larghezza di banda della modulazione di frequenza]
</margin>

Utilizzando la formula di Carson, è possibile calcolare la larghezza di banda occupata da un’emissione FM nota la deviazione e la frequenza di modulazione. Riorganizzando opportunamente la formula, è possibile calcolare anche gli altri valori.

[question:AE309]
[question:AE308]
[question:AE311]
[question:AE312]
[question:AE310]
[question:AE314]
