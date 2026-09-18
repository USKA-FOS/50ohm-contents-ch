Analizziamo innanzitutto la struttura di un ricevitore. Nell’immagine [ref:aufbau_empfaenger_blockdiagramm] semplifichiamo lo schema non scendendo al livello dei singoli componenti, ma considerando blocchi che svolgono una specifica funzione. Questa rappresentazione è chiamata *diagramma a blocchi*. In elettrotecnica serve a visualizzare in modo semplificato dispositivi complessi. A tal fine, si omettono i dettagli non necessari per comprendere il funzionamento generale dell’apparecchio.

<margin>
[picture:736:aufbau_empfaenger_blockdiagramm:Diagramma a blocchi di un ricevitore semplice]
</margin>

<indepth>
Il ricevitore qui illustrato è detto *ricevitore a conversione diretta*. Il nome deriva dal fatto che il segnale ricevuto dall’antenna non subisce alcuna variazione di frequenza fino al demodulatore.
</indepth>

---

Esaminiamo ora in dettaglio i singoli blocchi del ricevitore, procedendo da sinistra a destra:

1. Antenna: l’antenna riceve una molteplicità di onde radio e le converte in oscillazioni elettriche.
2. Filtro passa-banda: per isolare il segnale desiderato, segue un filtro passa-banda. Questo lascia passare solo la banda di frequenza desiderata e blocca tutte le altre frequenze indesiderate.
3. Amplificatore AF: a seguire c’è un amplificatore che rafforza il segnale filtrato. Si tratta di un *amplificatore ad alta frequenza* (AF), poiché il segnale ha una frequenza elevata, ad esempio $\qty{144,3}{\mega\hertz}$.
4. Demodulatore: il segnale amplificato viene elaborato dal demodulatore. La demodulazione è l’inverso della modulazione. Mentre nella modulazione un segnale (ad esempio un segnale vocale) viene impresso su una portante ad alta frequenza, nella demodulazione avviene il contrario: dal segnale ad alta frequenza modulato si recupera il segnale originale. Si ottiene così, ad esempio, il segnale vocale che era stato pronunciato al microfono del trasmettitore. Si parla anche di *segnale a bassa frequenza* (segnale BF), poiché presenta frequenze relativamente basse, ad esempio sotto $\qty{20}{\kilo\hertz}$ per un segnale vocale.
5. Amplificatore BF: il segnale demodulato viene quindi amplificato. In questo caso si tratta di un *amplificatore BF* per rafforzare il segnale destinato all’altoparlante. Il simbolo dell’amplificatore BF è identico a quello dell’amplificatore ad alta frequenza.
6. Altoparlante: il segnale viene ora convertito da un’oscillazione elettrica in un’onda sonora dall’altoparlante, rendendolo nuovamente udibile.

<indepth>
Nel *filtro passa-banda*, le due onde barrate indicano che le frequenze al di sopra e al di sotto della banda desiderata vengono bloccate. L’onda centrale rappresenta la banda di frequenza che viene lasciata passare.
</indepth>

<indepth>
Il *demodulatore* è rappresentato dal simbolo del diodo, che è il componente principale di molti demodulatori. Il funzionamento del diodo verrà spiegato nel capitolo "Componenti e circuiti".
</indepth>

[question:NF201]

A seconda di come è strutturato un ricevitore, esso presenta caratteristiche diverse. Una caratteristica importante è la *sensibilità*. Con questo termine si indica la capacità del ricevitore di ricevere segnali deboli. Più un ricevitore è sensibile, più segnali deboli è in grado di ricevere.

[question:NF303]
