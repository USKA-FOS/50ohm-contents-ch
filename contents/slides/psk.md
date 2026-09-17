* Digitales Modulationsverfahren zur Datenübertragung  
* Veränderung der Phase eines Trägersignals zur Repräsentation von Bitwerten  
* Weniger anfällig für Amplitudenrauschen $\rightarrow$ ermöglicht höhere Datenraten

---
## Prinzip der Phasenumtastung

<left>
[picture:705:psk:Phasenumtastung (Phase-shift Keying)]
</left>
<right>
<fragment>
*BPSK (Binary Phase Shift Keying)*
* Zwei Phasenwinkel: $\qty{0}{\degree}$ und $\qty{180}{\degree}$  
* Jeder Winkel repräsentiert einen Bitwert ($\num{0}$ oder $\num{1}$)
</fragment>
</right>

---
Höhere Varianten:  

* *QPSK (Quadrature PSK)*: Vier Phasen ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$, $\qty{270}{\degree}$) – $\qty{2}{\text{Bits pro Symbol}}$
* *8-PSK*: Acht Phasen – $\qty{3}{\text{Bits pro Symbol}}$


---

## PSK-Signale in der Zeitdarstellung

* Die Amplitude bleibt konstant; nur die Phase ändert sich  
* *BPSK*: Abrupter Sprung von positiver zu negativer Amplitude bei Bitwechsel  
* *QPSK*: Mehrere Phasenwinkel mit kleineren Übergängen, wodurch die Kurve geglättet erscheint

---

## Erkennung von PSK-Signalen

* *Im Zeitbereich*: Deutliche, abrupte Phasenwechsel  
* *Im Phasendiagramm (Constellation Diagram)*: Punkte auf einem Kreis, die die stabilen Phasenlagen anzeigen
* PSK bietet eine robuste digitale Kommunikation mit hoher Datenrate und guter Rauschfestigkeit

---

[question:AE401]
