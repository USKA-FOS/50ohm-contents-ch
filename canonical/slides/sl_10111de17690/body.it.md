## Situazione di partenza: ASK e PSK

* Con ASK e PSK è possibile utilizzare più simboli per trasmettere più bit per simbolo
* Con un numero molto elevato di simboli, gli stati del segnale possibili si trovano sempre più vicini tra loro
* Il ricevitore deve quindi essere in grado di riconoscere differenze sempre più piccole
* Il metodo diventa più suscettibile ai disturbi

<note>
Inizialmente potrebbe sembrare logico utilizzare semplicemente sempre più ampiezze o posizioni di fase. In questo modo è possibile trasmettere più bit per simbolo, ma allo stesso tempo diventa più difficile per il ricevitore distinguere in modo affidabile i singoli simboli.
</note>

---

## Modulazione di ampiezza in quadratura (QAM)

* Trucco: non viene modificato un *solo* parametro
* La QAM combina diversi valori di
  * ampiezza e
  * posizione di fase
* Un simbolo corrisponde a una specifica combinazione di ampiezza e fase

<fragment>
Con la stessa velocità di simbolo, è possibile trasmettere più bit al secondo.
</fragment>

<note>
Invece di dover distinguere molte ampiezze diverse, come nel caso dell'ASK, la QAM sfrutta due gradi di libertà contemporaneamente: ampiezza e fase.

In questo modo, con un numero relativamente piccolo di valori diversi, è possibile generare un numero maggiore di simboli diversi.
</note>

--- style="font-size: 0.7em;"
## Esempio: 8-QAM

[picture:702:a_8qam:Andamento del segnale di un segnale 8QAM, ogni simbolo con ampiezza ($\num{0,5}$ o $\num{1}$), posizione di fase e sequenza di bit a 3 cifre]

* $\num{8}$ simboli diversi
* Ogni simbolo possiede un'ampiezza e una posizione di fase specifiche
* $\num{8}$ simboli → $\num{3}$ bit per simbolo

<note>
La figura mostra un segnale 8-QAM nel dominio del tempo.

Ogni simbolo è associato a una sequenza di bit a tre cifre tramite la mappatura. Poiché esistono otto simboli diversi, con ogni simbolo possono essere trasmessi tre bit.
</note>

---
## Esempio: 16-QAM

<left>
[picture:1061:a_16qam:Diagramma I-Q per una mappatura 16-QAM]
</left>
<right>
* $\num{16}$ punti di segnale diversi
* Ogni punto corrisponde a una coppia di valori $(I,Q)$
* Da questi derivano diverse ampiezze e posizioni di fase
* $\num{16}$ simboli → $\num{4}$ bit per simbolo
</right>

<note>
Nel diagramma di costellazione si può riconoscere in modo particolare come la QAM generi molti simboli diversi.

Con la 16-QAM ci sono 16 punti di segnale possibili. A ogni punto viene associata una combinazione di quattro bit.

La posizione di un punto è descritta dai due valori I e Q. Da questi derivano, a loro volta, l'ampiezza e la posizione di fase del segnale risultante.
</note>

---
[question:AE403]

---
## Come viene generato un segnale QAM?

Dopo aver conosciuto il diagramma di costellazione, sorge la domanda:

<fragment>
**Come fa un trasmettitore a generare un punto desiderato nel diagramma?**
</fragment>

<fragment>
A questo scopo può essere utilizzato un *modulatore I/Q*.
</fragment>

---
## Modulatore I/Q

<left>
[picture:196:a_iq_modulator:Schema a blocchi di un modulatore I/Q]
</left>
<right>
* Due portanti con la stessa frequenza
* Sfasamento di $\qty{90}{\degree}$
* Una portante viene ponderata con il *segnale I*
* L'altra portante viene ponderata con il *segnale Q*
* Successivamente i due segnali vengono sommati
</right>

<note>
Un modulatore I/Q funziona con due portanti sinusoidali della stessa frequenza. Le due portanti sono sfasate di 90 gradi l'una rispetto all'altra.

La prima viene ponderata con il valore I e la seconda con il valore Q. Successivamente i due componenti del segnale vengono sommati.

A seconda della combinazione di I e Q, si ottiene un segnale con un'ampiezza e una posizione di fase specifiche.
</note>

---
## I e Q determinano ampiezza e fase

* Ogni punto nel diagramma di costellazione corrisponde a una coppia di valori $(I,Q)$
* Modificando I e Q si modificano
  * l'ampiezza e
  * la posizione di fase
  del segnale risultante

<fragment>
In questo modo il modulatore I/Q può generare qualsiasi punto desiderato della mappatura.
</fragment>

<note>
Questa è la connessione diretta tra il diagramma di costellazione e il circuito reale:

Le coordinate di un punto del segnale sono esattamente i valori I e Q con cui viene pilotato il modulatore I/Q.

Il diagramma di costellazione non è quindi solo una rappresentazione del segnale. Descrive direttamente quali valori I e Q devono essere generati.
</note>

--- style="font-size: smaller;"

## Prova il modulatore I/Q

[include:applet_iq_169]

<note>
Con l'applet è possibile provare direttamente l'effetto dei due valori I e Q.

Modificando I e Q, il punto del segnale si sposta nel diagramma di costellazione. Allo stesso tempo si può osservare come cambino l'ampiezza e la posizione di fase del segnale risultante.

In questo modo si può comprendere come un modulatore I/Q possa generare i diversi punti di una mappatura QAM.
</note>

---

[question:AF632]

---

[question:AE404]

---

## I e Q dal software

* Un microcontrollore, un processore di segnale o un SDR calcola i valori per I e Q
* Per ogni simbolo viene determinata la coppia di valori corrispondente $(I,Q)$

<fragment>
Esempio 16-QAM:

* $\num{4}$ valori I possibili
* $\num{4}$ valori Q possibili
* $\num{4}\cdot\num{4}=\num{16}$ punti di segnale possibili
</fragment>

<note>
I valori I e Q non devono essere generati da un complicato circuito analogico.

In un sistema digitale, il software può semplicemente determinare per ogni simbolo da trasmettere i due valori numerici corrispondenti.

Con una 16-QAM, ad esempio, possono essere utilizzati quattro valori diversi per I e quattro per Q. Dalle combinazioni derivano in totale 16 punti di segnale.
</note>

---

## Dai valori numerici al segnale I/Q

* I e Q sono inizialmente disponibili come *valori numerici digitali*
* I convertitori DA generano da questi i segnali analogici I e Q
* Questi segnali pilotano il modulatore I/Q

<fragment>
La mappatura desiderata può quindi essere definita in gran parte tramite *software*.
</fragment>

<note>
Il software genera inizialmente valori numerici digitali per I e Q.

I convertitori DA li convertono poi in tensioni analogiche che possono essere fornite al modulatore I/Q.

In modo semplificato, il software deve quindi calcolare solo quale punto del diagramma di costellazione deve essere generato in un determinato momento.
</note>

---

## Software Defined Radio

* In una *Software Defined Radio (SDR)* gran parte dell'elaborazione del segnale viene eseguita tramite software
* Il software calcola i segnali I e Q necessari
* L'hardware ad alta frequenza può rimanere lo stesso per molti metodi di modulazione diversi

<fragment>
Il metodo di modulazione viene quindi determinato in gran parte tramite *software*.
</fragment>

---

## Non solo modulazione digitale

Un modulatore I/Q può anche elaborare segnali I e Q che variano in modo continuo.

<fragment>
In questo modo è possibile generare, ad esempio:

* AM
* FM
* PM
* SSB
* PSK
* QAM
</fragment>

<note>
Il principio I/Q non è affatto limitato alla QAM o ad altri metodi di modulazione digitale.

Il software può generare, invece di valori simbolici fissi, anche andamenti di I e Q che variano in modo continuo.

Con AM, ad esempio, viene modificato principalmente il valore assoluto del vettore del segnale. Con PM viene modificato il suo angolo.

Anche FM può essere generata tramite la fase: la fase viene modificata in modo continuo, dove la velocità della variazione di fase corrisponde alla frequenza istantanea.

Con segnali I e Q appropriati è inoltre possibile generare un segnale a banda laterale singola.
</note>

---

## Non solo modulazione digitale

* Lo stesso modulatore I/Q può generare molti metodi di modulazione diversi
* È sufficiente calcolare in modo diverso gli andamenti di *I* e *Q*
* L'hardware ad alta frequenza può rimanere in gran parte invariato

<fragment>
Il modulatore I/Q è quindi, per così dire, il
**"coltellino svizzero dei modulatori"**. 
</fragment>

<note>
Proprio questa caratteristica rende la tecnologia SDR moderna così flessibile.

Invece di dover utilizzare per AM, FM, SSB, PSK o QAM un circuito modulatore diverso, è possibile utilizzare la stessa hardware I/Q di base.

Il metodo desiderato viene generato calcolando tramite software altri segnali I e Q.
</note>
