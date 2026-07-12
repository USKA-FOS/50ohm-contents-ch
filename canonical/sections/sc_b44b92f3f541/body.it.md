Diamo prima un'occhiata a come è strutturato un ricevitore. Nella figura [ref:aufbau_empfaenger_blockdiagramm], per semplificare, non entriamo nel dettaglio dei singoli componenti, ma consideriamo blocchi che hanno una funzione specifica. Questa rappresentazione è chiamata diagramma a blocchi. In elettrotecnica, serve a rappresentare dispositivi complessi in una visione d'insieme semplificata. Per fare ciò, si omettono i dettagli non necessari per la comprensione dell'intero dispositivo.

<margin>
[picture:736:aufbau_empfaenger_blockdiagramm:Diagramma a blocchi di un semplice ricevitore]
</margin>

<indepth>
Il ricevitore qui rappresentato è chiamato ricevitore a reazione diretta. Il nome deriva dal fatto che la frequenza del segnale captato dall'antenna non viene modificata fino al demodulatore.
</indepth>

---

Consideriamo i singoli blocchi del ricevitore in dettaglio, uno dopo l'altro da sinistra a destra:

1. Antenna: L'antenna capta una moltitudine di onde radio e le trasmette come oscillazioni elettriche.
2. Filtro passa-banda: Per filtrare il segnale desiderato, segue un filtro passa-banda. Questo lascia passare solo la banda di frequenza desiderata e blocca tutte le altre frequenze indesiderate.
3. Amplificatore HF: Successivamente, un amplificatore amplifica il segnale filtrato. Si tratta di un amplificatore ad alta frequenza (HF), poiché il segnale ha un'alta frequenza, ad esempio $\qty{144,3}{\mega\hertz}$.
4. Demodulatore: Il segnale amplificato viene ulteriormente elaborato dal demodulatore. La demodulazione è l'opposto della modulazione. Mentre nella modulazione un segnale (ad esempio un segnale vocale) viene modulato su una portante ad alta frequenza, nella demodulazione avviene il contrario: il segnale originale viene recuperato dalla portante ad alta frequenza modulata. Si ottiene quindi, ad esempio, di nuovo il segnale vocale che è stato parlato nel microfono al trasmettitore. Si parla anche di segnale a bassa frequenza, in breve segnale NF, poiché ha frequenze relativamente basse, nel caso di un segnale vocale, ad esempio, frequenze inferiori a $\qty{20}{\kilo\hertz}$.
5. Amplificatore NF: Il segnale demodulato viene quindi amplificato. Questa volta si tratta di un amplificatore a bassa frequenza (NF) per amplificare il segnale per l'altoparlante. Il simbolo per l'amplificatore NF è lo stesso di quello per l'amplificatore ad alta frequenza.
6. Altoparlante: Il segnale viene ora convertito dall'altoparlante da un'oscillazione elettrica a un'onda sonora e reso così nuovamente udibile.

<indepth>
Nel *filtro passa-banda*, le due onde barrate simboleggiano che le frequenze sopra e sotto la banda di frequenza desiderata vengono bloccate. L'onda centrale indica che la banda di frequenza desiderata viene lasciata passare.
</indepth>

<indepth>
Il *demodulatore* è rappresentato dal simbolo del circuito della diodo, che è il componente più importante di molti demodulatori. Il funzionamento di una diodo verrà spiegato più avanti nel capitolo "Componenti e circuiti".
</indepth>

[question:NF201]

A seconda di come è costruito esattamente un ricevitore, ha proprietà diverse. Una proprietà importante è la sensibilità. Questa indica la capacità del ricevitore di ricevere segnali deboli. Più un ricevitore è sensibile, più deboli segnali può ricevere.

[question:NF303]
