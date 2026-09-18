Finora abbiamo conosciuto ASK e PSK. Per entrambi i metodi potrebbe sembrare inizialmente logico scegliere un numero di simboli il più possibile elevato, in modo da trasmettere il maggior numero di informazioni possibile per simbolo. Tuttavia, in tal caso il ricevitore deve essere in grado di distinguere tra molte ampiezze diverse. Il metodo diventa così più suscettibile ai disturbi.

Per mitigare questo problema, si può ricorrere a un trucco: invece di modificare un solo parametro (ad esempio l’ampiezza), per ogni simbolo vengono modificati due parametri, ovvero l’ampiezza e la fase. Un simbolo corrisponde quindi a una combinazione di un’ampiezza specifica con una fase specifica. In questo modo, nonostante un numero ridotto di ampiezze e fasi diverse, si ottiene comunque un numero maggiore di simboli. A parità di velocità di simbolo, è possibile trasmettere più bit al secondo. Questo metodo viene chiamato *modulazione di ampiezza in quadratura* (QAM).

La figura [ref:a_8qam] mostra un segnale 8-QAM nel dominio del tempo. Ogni simbolo possiede un’ampiezza, una fase e una sequenza di 3 bit definita dal mapping. Con ogni simbolo possono quindi essere trasmessi 3 bit. La figura [ref:a_16qam] mostra un mapping 16-QAM nel diagramma di costellazione. Ogni simbolo corrisponde a una combinazione di un’ampiezza e una fase specifiche. Con ogni simbolo possono quindi essere trasmessi 4 bit.

<margin>
[picture:702:a_8qam:Andamento temporale di un segnale 8QAM, ogni simbolo con ampiezza ($\num{0,5}$ o $\num{1}$), fase e sequenza di 3 bit]
[picture:1061:a_16qam:Diagramma I-Q per un mapping 16-QAM]
</margin>

[question:AE403]

---

Dopo aver appreso la rappresentazione I/Q, il diagramma di costellazione e la modulazione di ampiezza in quadratura, sorge la domanda su come un segnale del genere possa essere generato tecnicamente. A questo scopo si può utilizzare un cosiddetto *modulatore I/Q*.

Un modulatore I/Q funziona con due portanti della stessa frequenza, sfasate tra loro di $\qty{90}{\degree}$. La prima portante viene ponderata con il segnale I e la portante sfasata di $\qty{90}{\degree}$ con il segnale Q. La figura [ref:a_iq_modulator] mostra lo schema a blocchi di un modulatore I/Q.

Successivamente, le due portanti modulate vengono sommate. A seconda dei valori di I e Q, si ottiene un segnale con un’ampiezza e una fase specifiche. Se i valori di I e Q vengono modificati, possono cambiare sia l’ampiezza che la fase del segnale risultante.

<margin>
[picture:196:a_iq_modulator:Schema a blocchi di un modulatore I/Q]
</margin>

<webonly>
<indepth>
Tutto questo può essere descritto facilmente matematicamente. Per la somma di una portante coseno con un’altra portante coseno sfasata di $\qty{90}{\degree}$ vale la seguente relazione:

$ I(t)\cdot \cos\left(\omega t\right) + Q(t)\cdot \cos\left(\omega t + \qty{90}{\degree}\right)=A \cdot \cos\left(\omega t+\phi\right) $

Si ottiene quindi un nuovo segnale coseno con un’ampiezza di

$A=\sqrt{I(t)^2 + Q(t)^2}$ 

e uno sfasamento di 

$ \phi = \operatorname{atan2}\left(Q(t),I(t)\right)$

[include:applet_iq]
</indepth>
</webonly>

[question:AF632]
[question:AE404]

In un sistema digitale, i valori per I e Q possono essere generati molto facilmente tramite software. Ad esempio, un microcontrollore, un processore di segnale o un SDR assegna a ogni simbolo da trasmettere due valori numerici per I e Q. Un punto nel diagramma di costellazione corrisponde quindi direttamente a una coppia di valori $(I,Q)$.

In una 16-QAM, ad esempio, per I e Q potrebbero essere utilizzati quattro valori diversi ciascuno. Combinandoli, si ottengono i $\num{16}$ punti di segnale diversi. Il software deve semplicemente emettere, per ogni simbolo, i valori I e Q corrispondenti al punto di segnale desiderato.

I valori digitali iniziali per I e Q possono poi essere convertiti in tensioni analogiche tramite due convertitori DA e inviati al modulatore I/Q. In questo modo, tramite software è possibile generare praticamente qualsiasi punto desiderato nel diagramma di costellazione. I moderni *Software Defined Radios* (SDR) utilizzano esattamente questo principio: gran parte della modulazione non è più determinata da circuiti analogici fissi, ma dalla calcolazione dei segnali I e Q tramite software.

---

Un modulatore I/Q non è affatto limitato ai metodi di modulazione digitali come QPSK o QAM. Oltre a valori fissi per I e Q, il software può anche calcolare andamenti di segnale I e Q continuamente variabili. In questo modo è possibile generare anche metodi di modulazione analogici.

In una modulazione di ampiezza, ad esempio, viene modificata la lunghezza del vettore di segnale risultante. In una modulazione di fase viene modificato il suo angolo. Anche in una modulazione di frequenza la fase del vettore di segnale viene modificata continuamente, dove la velocità di questa variazione di fase determina la frequenza istantanea. Con due segnali I e Q generati in modo appropriato, è inoltre possibile generare un segnale a banda laterale singola (SSB).

Con lo stesso modulatore I/Q è quindi possibile generare tra l’altro AM, FM, PM, SSB, PSK e QAM. È sufficiente calcolare i segnali I e Q in modo diverso a seconda del metodo. 

Il modulatore I/Q è quindi, per così dire, il "coltellino svizzero dei modulatori". Questo è anche uno dei motivi principali della grande flessibilità della tecnologia SDR moderna: il metodo di modulazione utilizzato viene determinato in gran parte tramite software, mentre l’hardware ad alta frequenza può rimanere invariato.