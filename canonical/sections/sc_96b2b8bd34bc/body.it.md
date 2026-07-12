% TODO riformulare
% Idea DL9MJ: Esempio con immagine, un bit in I e uno in Q e come appare il segnale per 00, 01, 10, 11

La QAM può essere generata particolarmente facilmente utilizzando due portanti della stessa frequenza. Una delle due portanti deve essere sfasata di $\qty{90}{\degree}$. Entrambe le portanti vengono quindi modulate in ampiezza con un proprio segnale. Un segnale è chiamato I (per In-Phase Component) e l'altro segnale è chiamato Q (per Quadrature Phase Component). La portante sfasata viene modulata con il segnale Q. Successivamente, le due portanti modulate vengono sovrapposte, creando una portante che cambia sia in ampiezza che in fase.

<indepth>
[include:applet_iq]
</indepth>
  
%TODO IMMAGINE QAM4 QAM8 o più?

[question:AE404]
[question:AF632]

L'idea di base di elaborare un segnale in due parti separate trova ampia applicazione anche nell'elaborazione digitale dei segnali. Viene chiamata metodo I/Q dopo i due segnali parziali. Il metodo I/Q consente di generare qualsiasi segnale. A tale scopo, il flusso di dati da modulare è composto da una componente I e una componente Q. Due convertitori D/A convertono ciascuna delle due componenti in un segnale analogico I o Q. Con i segnali I e Q, le due portanti sfasate vengono nuovamente modulate. Nell'ultimo passaggio, queste vengono sovrapposte a una portante che viene trasmessa.

Analogamente, si procede sul lato ricevente. Il segnale di ingresso viene miscelato con una portante per ottenere il segnale I, che viene quindi convertito tramite un convertitore A/D nella componente I di un flusso di dati. Contemporaneamente, il segnale di ingresso viene miscelato anche con una portante sfasata di $\qty{90}{\degree}$ per ottenere il segnale Q, che a sua volta viene convertito tramite un convertitore A/D nella componente Q del flusso di dati.

[question:AF633]

Un tale flusso di dati digitale può sempre rappresentare una determinata banda di frequenza del segnale di ingresso, che si trova attorno a una frequenza centrale. Se, ad esempio, il segnale di ingresso viene miscelato con una portante da $\qty{435}{\mega\hertz}$ e una portante da $\qty{435}{\mega\hertz}$ sfasata di $\qty{90}{\degree}$, e i due segnali risultanti vengono digitalizzati tramite convertitori A/D, allora il flusso di dati I/Q risultante rappresenta la banda di frequenza attorno a $\qty{435}{\mega\hertz}$.

% TODO riferimento al teorema di campionamento?
La larghezza di banda coperta dipende dalla frequenza di campionamento della conversione A/D. La larghezza di banda in Hz corrisponde alla frequenza di campionamento in campioni al secondo. Se nel nostro esempio sia la componente I che la componente Q vengono campionate a 10 milioni di campioni al secondo, allora il flusso di dati I/Q risultante può coprire una banda di frequenza di $\qty{10}{\mega\hertz}$, cioè da $\qty{-5}{\mega\hertz}$ a $\qty{+5}{\mega\hertz}$ rispetto alla frequenza centrale. Il flusso di dati copre quindi le frequenze da $\qty{430}{\mega\hertz}$ a $\qty{440}{\mega\hertz}$.

[question:AF634]
[question:AF635]
[question:AF636]
