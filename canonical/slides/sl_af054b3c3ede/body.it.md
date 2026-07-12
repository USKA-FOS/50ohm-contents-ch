## Modulazione QAM e metodo I/Q

* Tecnica di modulazione digitale che utilizza due portanti della stessa frequenza.
* Una delle portanti è sfasata di $\qty{90}{\degree}$.
* Genera un segnale che varia in ampiezza e fase.

---

### Generazione della QAM

<left>
* Due portanti:
* Una viene modulata con il segnale I (In-Phase).
* L'altra, sfasata di $\qty{90}{\degree}$, con il segnale Q (Quadrature).
</left>
<right>
* Entrambe le portanti modulate vengono sovrapposte.
* Il segnale risultante varia in ampiezza e fase.
</right>

---

[include:applet_iq]

---

[question:AE404]

---

[question:AF632]

---

### Metodo I/Q – Lato trasmettitore

* Il flusso di dati digitale viene suddiviso in due parti: I e Q.
* Due convertitori D/A convertono i valori digitali I e Q in segnali analogici.
* Questi modulano le due portanti sfasate, che vengono poi combinate.

---

### Metodo I/Q – Lato ricevitore

* Il segnale ricevuto viene miscelato con una portante a $\qty{0}{\degree}$ per estrarre il segnale I.
* Contemporaneamente, avviene una miscelazione con una portante sfasata di $\qty{90}{\degree}$ per ottenere il segnale Q.
* Entrambi i segnali vengono convertiti A/D e formano così il flusso di dati digitale I/Q.

---

[question:AF633]

---

### Rappresentazione della banda di frequenza

* Il flusso di dati I/Q rappresenta la banda di frequenza attorno a una frequenza centrale.
* Esempio:
* Portante a $\qty{435}{\mega\hertz}$
* Frequenza di campionamento di $\num{10}$ milioni di campioni/s $\rightarrow$ Larghezza di banda = $\qty{10}{\mega\hertz}$ ($\pm\qty{5}{\mega\hertz}$ attorno alla frequenza centrale).
* Intervallo coperto: circa $\qty{430}{\mega\hertz}$ fino a $\qty{440}{\mega\hertz}$.

---

[question:AF634]

---

### Dipendenza della larghezza di banda dalla frequenza di campionamento

* La larghezza di banda coperta in $\unit{\hertz}$ corrisponde alla frequenza di campionamento in campioni al secondo.

---

[question:AF635]

---

[question:AF636]
