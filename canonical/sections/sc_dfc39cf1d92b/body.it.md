I segnali possono essere rappresentati in modi diversi. Finora abbiamo spesso considerato il *dominio del tempo*. In questo caso si rappresenta, ad esempio, come varia la tensione di un segnale nel tempo. Lo stesso segnale può tuttavia essere analizzato anche nel *dominio della frequenza*. In questo caso non viene più mostrata l’evoluzione temporale, ma da quali componenti di frequenza è composto il segnale e con quale intensità ciascuna di esse è presente. Questa rappresentazione è anche chiamata *spettro di frequenza*. La base di ciò risiede nel fatto che i segnali periodici possono essere descritti come sovrapposizione di oscillazioni sinusoidali di frequenza, ampiezza e fase diverse. Un segnale puramente sinusoidale, ad esempio, è composto da una singola frequenza e quindi appare nello spettro di frequenza solo a quella frequenza.

La *trasformata di Fourier* consente di passare dal dominio del tempo a quello della frequenza. Essa scompone matematicamente un segnale nei suoi singoli componenti di frequenza. Per i segnali discreti nel tempo e digitali si utilizza la *trasformata di Fourier discreta* (DFT). Il calcolo diretto di una DFT può risultare molto complesso in presenza di un elevato numero di campioni. Con la *Fast-Fourier-Transformation* (FFT) è disponibile un algoritmo molto più efficiente per il calcolo della DFT. Per questo motivo la FFT viene spesso impiegata nei software e nelle apparecchiature digitali, ad esempio per determinare lo spettro di frequenza di un segnale.

<indepth>
Le forme d’onda non sinusoidali sono composte da più componenti di frequenza. In particolare, cambiamenti bruschi e spigoli nel segnale temporale richiedono componenti ad alta frequenza aggiuntive. Con l’applet seguente è possibile analizzare come diverse oscillazioni sinusoidali si sovrappongano e diano origine a varie forme d’onda.

[include:fourier]
</indepth>

[question:AF630]

---

Il legame tra dominio del tempo e della frequenza risulta particolarmente evidente nei segnali con spigoli netti. Un segnale rettangolare ideale, ad esempio, può essere composto da una fondamentale e da diverse armoniche. Oltre alla frequenza fondamentale, compaiono i multipli dispari della frequenza fondamentale. Le loro ampiezze diminuiscono all’aumentare della frequenza.

Queste armoniche rivestono un’importanza anche per i trasmettitori. Se, ad esempio, un segnale rettangolare ideale venisse inviato direttamente a un’antenna, oltre alla frequenza fondamentale desiderata verrebbero irradiate anche le sue armoniche. Un filtro passa-basso può attenuare le componenti di frequenza indesiderate più elevate, in modo che all’antenna giunga principalmente l’oscillazione fondamentale desiderata.

Per alcune forme d’onda periodiche tipiche, lo spettro di frequenza può essere descritto in modo particolarmente semplice. In questo caso consideriamo forme d’onda ideali senza componente continua:

* Un *segnale sinusoidale* è composto da una singola frequenza. Nello spettro di frequenza appare quindi solo la frequenza fondamentale $f$.
* Un *segnale rettangolare* è composto dalla frequenza fondamentale e dai *multipli dispari* della frequenza fondamentale. Contiene quindi le frequenze $f$, $3\cdot f$, $5\cdot f$, $7\cdot f$ e così via. Le ampiezze delle armoniche diminuiscono all’aumentare della frequenza.
* Un *segnale a dente di sega* contiene sia i multipli pari che quelli dispari della frequenza fondamentale. Contiene quindi $f$, $2\cdot f$, $3\cdot f$, $4\cdot f$, $5\cdot f$ e così via. Anche in questo caso le ampiezze diminuiscono all’aumentare della frequenza.
* Un *segnale triangolare* contiene, come il segnale rettangolare, solo i multipli dispari della frequenza fondamentale, quindi $f$, $3\cdot f$, $5\cdot f$, $7\cdot f$ e così via. Tuttavia, le ampiezze delle componenti di frequenza più elevate diminuiscono molto più rapidamente che nel segnale rettangolare.

In questo modo è possibile distinguere le forme d’onda anche in base al loro spettro di frequenza. Un singolo componente spettrale indica un segnale sinusoidale. Se compaiono multipli dispari, nelle domande d’esame si tratta sempre di un segnale rettangolare.

[question:AB404]
[question:AB405]
[question:AB406]
[question:AB407]