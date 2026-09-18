In uno dei capitoli precedenti abbiamo imparato a conoscere la rappresentazione I/Q e il modulatore I/Q. In un sistema digitale, i due componenti I e Q vengono elaborati come due flussi di dati digitali separati. Questi possono essere generati, modificati ed elaborati tramite l'elaborazione digitale del segnale.

Lato ricevitore, il segnale di ingresso viene miscelato con due segnali della stessa frequenza, sfasati di $\qty{90}{\degree}$ l'uno rispetto all'altro. In questo modo si ottengono un segnale I e un segnale Q. Entrambi i segnali vengono poi digitalizzati tramite un convertitore analogico-digitale e possono essere ulteriormente elaborati in digitale. Lato trasmettitore, il processo funziona al contrario: i flussi di dati digitali I e Q vengono convertiti in segnali analogici tramite due convertitori D/A e quindi inviati a un modulatore I/Q.

Un flusso di dati I/Q digitale può rappresentare una banda di frequenza intorno a una frequenza centrale specifica. Le frequenze inferiori alla frequenza centrale sono descritte da deviazioni di frequenza negative, mentre quelle superiori da deviazioni di frequenza positive.

Se, ad esempio, un segnale di ingresso viene miscelato con due segnali sfasati di $\qty{90}{\degree}$ ciascuno a $\qty{435}{\mega\hertz}$, il flusso di dati I/Q risultante rappresenta una banda di frequenza intorno alla frequenza centrale di $\qty{435}{\mega\hertz}$.

La dimensione di questa banda di frequenza dipende dalla frequenza di campionamento. Se sia I che Q vengono campionati con una frequenza di campionamento $f_\mathrm{S}$, idealmente è possibile rappresentare una banda di frequenza da

$-\frac{f_\mathrm{S}}{2}\text{ a }+\frac{f_\mathrm{S}}{2}$

intorno alla frequenza centrale. La larghezza di banda totale rappresentabile corrisponde quindi alla frequenza di campionamento $f_\mathrm{S}$.

Se, ad esempio, I e Q vengono campionati ciascuno con $\qty{10}{\mega\sample\per\second}$, il flusso di dati I/Q può rappresentare una banda di frequenza da $\qty{-5}{\mega\hertz}$ a $\qty{+5}{\mega\hertz}$ intorno alla frequenza centrale. Con una frequenza centrale di $\qty{435}{\mega\hertz}$, ciò corrisponde a una banda di frequenza da $\qty{430}{\mega\hertz}$ a $\qty{440}{\mega\hertz}$.

[question:AF634]
[question:AF635]
[question:AF636]