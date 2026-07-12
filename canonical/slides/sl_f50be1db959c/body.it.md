## Mapping nell'elaborazione digitale dei segnali

* Converte i dati digitali in punti segnale specifici (simboli)  
* Cruciale per tecniche di modulazione come QAM e QPSK  
* Permette la trasmissione dei dati attraverso il sistema di comunicazione

---

## Fase 1: Conversione dei dati binari in simboli

* In QPSK, due bit vengono raggruppati in un simbolo  
* Ci sono 4 combinazioni possibili: $\num{00}$, $\num{01}$, $\num{10}$, $\num{11}$
* Ogni combinazione viene assegnata a un punto segnale specifico

---

## Fase 2: Assegnazione della fase

* A ogni simbolo viene assegnata una fase propria  
* Fasi tipiche a passi di $\qty{90}{\degree}$:
* $\num{00}$ corrisponde a $\qty{0}{\degree}$
* $\num{01}$ corrisponde a $\qty{90}{\degree}$
* $\num{10}$ corrisponde a $\qty{180}{\degree}$
* $\num{11}$ corrisponde a $\qty{270}{\degree}$

--- style="font-size: smaller;"
## Fase 3: Mapping sul diagramma di costellazione

<left>
[picture:697:a_8qam:Diagramma I-Q per un mapping 8QAM]
La rappresentazione è per un mapping 8QAM. QPSK nell'esempio corrisponde al cerchio esterno.
</left>
<right>
* Il diagramma di costellazione rappresenta i punti segnale in un diagramma quadrato  
* L'asse X (*I*n-phase) e l'asse Y (*Q*uadrature) mostrano le ampiezze dei componenti del segnale  
* Per QPSK, i quattro punti segnale si trovano alle estremità di un quadrato
</right>

---

## Rappresentazione dei simboli QPSK

* $\num{00}$ a $\qty{0}{\degree}$: punto sull'asse X positivo  
* $\num{01}$ a $\qty{90}{\degree}$: punto sull'asse Y positivo  
* $\num{10}$ a $\qty{180}{\degree}$: punto sull'asse X negativo  
* $\num{11}$ a $\qty{270}{\degree}$: punto sull'asse Y negativo

* La chiara separazione delle fasi facilita la distinzione dei simboli, anche in presenza di rumore
