## Convertitore

* I segnali su una banda di frequenza vengono convertiti in un'altra banda di frequenza
* Ad esempio, un segnale a $\qty{2}{\meter}$ viene trasmesso come segnale a $\qty{70}{\centi\meter}$ in ricezione
* Il segnale viene convertito solo in una direzione
* In sostanza si tratta di un semplice mixer

---
[question:EF504]

<note>
* TCXO e PLL verranno trattati in seguito
* Ma la miscelazione può essere calcolata
</note>

---
[question:EF505]
---
## Transverter

* Nel transverter la conversione avviene in entrambe le direzioni
* Anche in questo caso la conversione avviene tramite miscelazione

---
[question:EF501]
---
[question:EF502]
---
[question:EF503]
<note>
* La soluzione verrà illustrata nella diapositiva successiva
</note>
---
### Soluzione

La frequenza del generatore viene triplicata: $\qty{38,666}{\mega\hertz} \cdot 3 = \qty{116}{\mega\hertz}$

<left>
*Percorso TX*
* I $\qtyrange{28}{30}{\mega\hertz}$ del ricetrasmettitore vengono miscelati con $\qty{116}{\mega\hertz}$
* Il segnale può essere $\qtyrange{86}{88}{\mega\hertz}$ o $\qtyrange{144}{146}{\mega\hertz}$
</left>
<right>
[picture:843:e_transverter_tx:Transverter nel percorso TX]
</right>

---

<left>
*Percorso RX*
* Il segnale dell'antenna viene miscelato con $\qty{116}{\mega\hertz}$ e ne risultano $\qtyrange{28}{30}{\mega\hertz}$
* Il segnale dell'antenna si trova quindi, tra l'altro, a $\qtyrange{144}{146}{\mega\hertz}$
* $\rightarrow$ È corretta solo la risposta con $\qty{2}{\meter}$ e il transverter impostato correttamente
</left>
<right>
[picture:842:e_transverter_rx:Transverter nel percorso RX]
</right>

---
## Stabilità di frequenza

* I convertitori e i transverter dovrebbero essere costruiti con oscillatori a elevata stabilità di frequenza
* Se la frequenza devia, anche la frequenza di uscita devia

---
<left>
* Grafico dalla domanda precedente
* Da $\qty{10}{\mega\hertz}$ si ottengono $\qty{2,256}{\giga\hertz}$, quindi una moltiplicazione per $\num{225,6}$
* Invece di $\qty{10}{\mega\hertz}$, l'oscillatore genera $\qty{10,01}{\mega\hertz}$ a causa di un errore
* $\qty{10,01}{\mega\hertz} \cdot 225,6 = \qty{2,258256}{\giga\hertz}$
* Mixer: $\qty{144}{\mega\hertz} + \qty{2,258256}{\giga\hertz} = \qty{2,402256}{\giga\hertz} \rightarrow \qty{2,256}{\mega\hertz}$ sbagliato
</left>
<right>
[picture:651:e_konverter_13cm:Convertitore per la banda dei $\qty{13}{\centi\meter}$]
</right>