Come abbiamo già imparato nella sezione [sec:fm_2], nella modulazione di frequenza l'informazione del segnale modulante non si trova nell'ampiezza, ma solo nella variazione di frequenza del segnale portante. Pertanto, nel ricevitore devono essere valutati solo gli attraversamenti dello zero del segnale portante.

Le fluttuazioni di ampiezza vengono mascherate da un amplificatore limitatore. Per questo motivo, la modulazione di frequenza è intrinsecamente insensibile ai disturbi impulsivi dell'ampiezza, causati ad esempio da scintille d'accensione, motori elettrici o simili. La FM è quindi adatta per l'uso in veicoli a motore.

[question:AE302]

Ora vedremo come la modulazione di frequenza può essere generata in un trasmettitore e come può essere calcolata la larghezza di banda di un segnale FM.

---

La modulazione di frequenza può essere generata modificando la capacità del condensatore che determina la frequenza all'interno di un oscillatore (cfr. [ref:fm_modulation_schaltung]). Ad esempio, utilizzando un diodo a capacità variabile in serie a un circuito oscillante o a un cristallo di quarzo, si può generare modulazione di frequenza. L'ampiezza del segnale in bassa frequenza (BF), generato ad esempio da un microfono collegato al diodo a capacità variabile, determina direttamente la variazione di frequenza dell'oscillatore.

[question:AE303]

<margin>
[picture:155:fm_modulation_schaltung:Semplice circuito per la modulazione di frequenza di un oscillatore con diodo a capacità variabile]
</margin>

La frequenza di modulazione influenza la frequenza con cui cambia la frequenza dell'oscillatore.

[question:AE301]

Nella sezione [sec:fm_2] abbiamo già conosciuto la *deviazione di frequenza portante*. Essa indica di quanto la frequenza istantanea del segnale FM viene spostata rispetto alla frequenza portante dal segnale modulante. Maggiore è l'ampiezza del segnale modulante, maggiore è questa deviazione di frequenza.

Nella demodulazione nel ricevitore FM, questa deviazione di frequenza viene nuovamente convertita in una corrispondente ampiezza del segnale demodulato. Una deviazione di frequenza maggiore porta quindi, a parità di altre condizioni, a un'ampiezza maggiore del segnale BF demodulato.

Una deviazione di frequenza maggiore aumenta la larghezza di banda richiesta del segnale FM. Se i valori previsti vengono superati, il segnale emesso può estendersi nei canali adiacenti, causando così interferenze sul canale vicino.

[question:AE305]
[question:AE306]
[question:AE307]
[question:AE304]

---

In senso stretto, la larghezza di banda occupata da un'emissione FM non è determinata solo dalla deviazione, ma anche dalla massima frequenza di modulazione (cfr. figura [ref:fm_modulation]). In prima approssimazione, per deviazioni piccole e basse frequenze di modulazione, può essere applicata la formula di Carson. Essa indica in quale larghezza di banda si trova il $\qty{99}{\percent}$ della potenza di trasmissione.

$B\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$

<margin>
[picture:910:fm_modulation:Larghezza di banda modulazione di frequenza]
</margin>

Utilizzando la formula di Carson, con valori noti per la deviazione e la frequenza di modulazione, è possibile calcolare la larghezza di banda occupata da un'emissione FM. Riorganizzando opportunamente la formula, è possibile calcolare anche le altre grandezze.

[question:AE309]
[question:AE308]
[question:AE311]
[question:AE312]
[question:AE310]
[question:AE314]
