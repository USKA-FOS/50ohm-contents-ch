* Metodo di modulazione digitale per la trasmissione dati  
* Variazione della fase di un segnale portante per rappresentare valori di bit  
* Meno suscettibile al rumore di ampiezza $\rightarrow$ consente velocità di trasmissione dati più elevate

---
## Principio del Phase Shift Keying

<left>
[picture:705:psk:Phase-shift Keying]
</left>
<right>
<fragment>
*BPSK (Binary Phase Shift Keying)*
* Due angoli di fase: $\qty{0}{\degree}$ e $\qty{180}{\degree}$  
* Ogni angolo rappresenta un valore di bit ($\num{0}$ o $\num{1}$)
</fragment>
</right>

---
Varianti superiori:  

* *QPSK (Quadrature PSK)*: Quattro fasi ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$, $\qty{270}{\degree}$) – $\qty{2}{\text{Bit per simbolo}}$
* *8-PSK*: Otto fasi – $\qty{3}{\text{Bit per simbolo}}$


---

## Segnali PSK nella rappresentazione temporale

* L'ampiezza rimane costante; cambia solo la fase  
* *BPSK*: Salto brusco da ampiezza positiva a negativa al cambio di bit  
* *QPSK*: Diversi angoli di fase con transizioni più piccole, che rendono la curva più liscia

---

## Riconoscimento dei segnali PSK

* *Nel dominio del tempo*: Cambi di fase chiari e bruschi  
* *Nel diagramma di fase (Constellation Diagram)*: Punti su un cerchio che indicano le posizioni di fase stabili
* PSK offre una comunicazione digitale robusta con alta velocità di trasmissione dati e buona resistenza al rumore

---

[question:AE401]
