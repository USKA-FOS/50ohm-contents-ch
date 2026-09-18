# Soluzione tramite metodo di esclusione
È utile riconoscere che si tratta del demodulatore ad inviluppo illustrato nel capitolo "Demodulator". 
Sul lato sinistro del circuito si nota che il segnale IF è presente all'ingresso del circuito. 
$\rightarrow$ Pertanto, la risposta "L'uscita per il segnale IF" è da escludere.

Il terminale $\text{X}$ si trova dopo un filtro passa-basso RC, realizzato con un condensatore elettrolitico (riconoscibile dal piccolo segno "+"). I condensatori elettrolitici hanno una capacità relativamente elevata. Per la relazione tra frequenza di taglio ($f_\text{g}$) e capacità ($C$), consideriamo la formula (filtro, filtro passa-basso RC) dalla raccolta di formule:

$f_\text{g} = \frac{1}{2\cdot\pi\cdot R \cdot C}$

Una capacità ($C$) elevata genera un denominatore grande e quindi una frequenza di taglio ($f_\text{g}$) bassa per il filtro passa-basso RC. 
$\rightarrow$ Pertanto, sono da escludere le risposte "L'uscita per il segnale BF" e "L'uscita per il segnale dell'oscillatore".

Al terminale $\text{X}$ è presente una tensione a bassa frequenza, utilizzabile per la regolazione.