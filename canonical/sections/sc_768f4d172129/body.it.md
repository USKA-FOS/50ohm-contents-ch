%TODO Verificare i riferimenti di sezione. Forse ne servono due.
%TODO Correggere il refuso già presente in Mega. Sample.
%
Nella sezione [sec:iq_verfahren] abbiamo appreso la rappresentazione I/Q e il modulatore I/Q. In un sistema digitale, le due componenti I e Q vengono elaborate come due flussi di dati digitali separati. Questi possono essere generati, modificati e valutati tramite elaborazione digitale del segnale.

Sul lato ricevitore, il segnale di ingresso viene miscelato con due segnali della stessa frequenza, sfasati di $\qty{90}{\degree}$ l'uno rispetto all'altro. Ciò produce un segnale I e un segnale Q. Entrambi i segnali vengono poi digitalizzati ciascuno con un convertitore A/D e possono successivamente essere ulteriormente elaborati digitalmente. Sul lato trasmittente, il processo funziona al contrario: i flussi di dati digitali I e Q vengono convertiti in segnali analogici tramite due convertitori D/A e poi inviati a un modulatore I/Q.

Un flusso di dati digitale I/Q può rappresentare una banda di frequenza attorno a una determinata frequenza centrale. In questo caso, le frequenze al di sotto della frequenza centrale sono descritte da deviazioni di frequenza negative e le frequenze al di sopra da deviazioni di frequenza positive.

Ad esempio, se un segnale di ingresso viene miscelato con due segnali di $\qty{435}{\mega\hertz}$ ciascuno, sfasati di $\qty{90}{\degree}$ l'uno rispetto all'altro, il flusso di dati I/Q risultante rappresenta una banda di frequenza attorno alla frequenza centrale di $\qty{435}{\mega\hertz}$.

La dimensione di questa banda di frequenza dipende dalla frequenza di campionamento. Se sia I che Q vengono campionati a una frequenza di campionamento $f_\mathrm{S}$, idealmente può essere rappresentata una banda di frequenza di

$-\frac{f_\mathrm{S}}{2}\text{ a }+\frac{f_\mathrm{S}}{2}$

attorno alla frequenza centrale. La larghezza di banda complessivamente rappresentabile corrisponde quindi alla frequenza di campionamento $f_\mathrm{S}$.

Ad esempio, se I e Q vengono campionati ciascuno a $\qty{10}{\mega sample\per\second}$, il flusso di dati I/Q può rappresentare una banda di frequenza da $\qty{-5}{\mega\hertz}$ a $\qty{+5}{\mega\hertz}$ attorno alla frequenza centrale. Con una frequenza centrale di $\qty{435}{\mega\hertz}$, ciò corrisponde a una banda di frequenza da $\qty{430}{\mega\hertz}$ a $\qty{440}{\mega\hertz}$.

[question:AF634]
[question:AF635]
[question:AF636]
