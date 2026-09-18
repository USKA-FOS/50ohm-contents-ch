Nella classe E abbiamo già imparato a conoscere l'AGC (Automatic Gain Control). Con segnali di ingresso forti, l'AGC riduce il guadagno degli stadi amplificatori nel ramo ricevente e lo aumenta con segnali deboli. In questo modo l'ampiezza del segnale demodulato e quindi il volume del segnale BF vengono mantenuti costanti.

Senza AGC, i segnali forti sovraccaricherebbero l'audio e quelli deboli sarebbero udibili solo molto silenziosamente. Il volume dell'audio dovrebbe essere sempre regolato manualmente. L'AGC bilancia quindi la dinamica del segnale ricevuto e adatta la sensibilità del ramo ricevente in base ai segnali HF di ingresso.

[question:AF224]

<margin>
[picture:1055:e_agc:AGC nel ricevitore supereterodina]
</margin>

---

Affinché l'AGC possa adattare automaticamente il guadagno all'intensità del segnale ricevuto, necessita di informazioni sulla sua ampiezza. A tal fine, una parte del segnale IF può essere raddrizzata e poi livellata, come mostrato nella figura [ref:e_agc_regelspannung].

Il diodo raddrizza il segnale IF ad alta frequenza. Un circuito RC successivo sopprime le rapide componenti alternate, generando una tensione continua la cui entità dipende dall'ampiezza del segnale IF. Più forte è il segnale ricevuto, maggiore è il valore assoluto di questa tensione.

Questa *tensione di regolazione* viene reindirizzata agli stadi amplificatori HF o IF regolabili, dove viene utilizzata per controllarne il guadagno. In questo modo si crea un circuito di regolazione chiuso: un segnale ricevuto più forte porta a una regolazione più intensa e quindi a un guadagno inferiore.

<margin>
[picture:142:e_agc_regelspannung:Tensione di regolazione AGC]
</margin>

[question:AD503]
