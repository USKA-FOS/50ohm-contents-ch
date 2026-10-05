Nella sezione [sec:agc_1] abbiamo già conosciuto l'AGC (Automatic Gain Control). Con segnali di ingresso forti, l'AGC riduce il guadagno degli stadi amplificatori nel ramo del ricevitore e con segnali di ingresso deboli lo aumenta di conseguenza. In questo modo, l'ampiezza del segnale demodulato e quindi il volume del segnale BF vengono mantenuti costanti.

Senza un AGC, i segnali forti sovraccaricherebbero la BF e i segnali deboli sarebbero udibili nella BF solo molto silenziosamente. Il volume della BF dovrebbe essere sempre regolato manualmente. L'AGC compensa quindi la dinamica del segnale ricevuto e adatta dinamicamente la sensibilità del ramo del ricevitore in funzione dei segnali di ingresso RF.

[question:AF224]

<margin>
[picture:1055:e_agc:AGC nel ricevitore supereterodina]
</margin>

---

Affinché l'AGC possa adattare automaticamente il guadagno all'intensità del segnale ricevuto, ha bisogno di un'informazione sulla sua ampiezza. A questo scopo, una parte del segnale IF può essere raddrizzata e successivamente livellata, come mostrato nella figura [ref:e_agc_regelspannung].

Il diodo raddrizza il segnale IF ad alta frequenza. Un circuito RC successivo sopprime le componenti alternate rapide, in modo che si generi una tensione continua, la cui altezza dipende dall'ampiezza del segnale IF. Più forte è il segnale ricevuto, maggiore è il valore assoluto di questa tensione.

Questa *tensione di controllo* viene riportata agli stadi amplificatori RF o IF regolabili e lì utilizzata per controllare il loro guadagno. In questo modo si crea un anello di controllo chiuso: un segnale ricevuto più forte porta a un'azione di controllo più forte e quindi a un guadagno inferiore.

<margin>
[picture:142:e_agc_regelspannung:Tensione di controllo AGC]
</margin>

[question:AD503]
