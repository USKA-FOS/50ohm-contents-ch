**GLI APPLET NON FUNZIONANO**

**applet_am_modulator e applet_dsp**

**Nel nostro generatore manca /assets/circuitjs/..    issue #54**

Abbiamo già conosciuto i diodi in vari circuiti. Ora esaminiamo come la loro caratteristica non lineare possa essere utilizzata per modulare un segnale portante ad alta frequenza con un segnale utile a bassa frequenza.

Se un segnale HF e un segnale BF vengono applicati insieme a un diodo, come mostrato nella figura [ref:a_am_modulator], la tensione BF influenza la conduttività del diodo. Di conseguenza, il segnale HF viene trasmesso in modo diverso a seconda del valore istantaneo della BF. La sua ampiezza cambia quindi in sincronia con il segnale BF.

All'uscita, oltre alla portante HF originale, si generano due bande laterali sopra e sotto la frequenza portante. Un circuito oscillante sintonizzato sulla frequenza portante sopprime ulteriori componenti di frequenza indesiderate. In uscita si ottiene così un segnale modulato in ampiezza (AM).

<margin>
[picture:772:a_am_modulator:Modulatore AM semplice con diodo e circuito oscillante]
</margin>

<webonly>
La seguente simulazione mostra il funzionamento del modulatore AM; i valori sono stati scelti in modo che l'HF e la BF siano ben riconoscibili. La BF è a $\qty{500}{\hertz}$, l'HF a $\qty{10}{\kilo\hertz}$. L'ampiezza del segnale HF viene modificata in sincronia con la BF. Il circuito oscillante è sintonizzato sulla frequenza portante e sopprime le componenti di frequenza indesiderate. Se si rimuove il circuito oscillante, si vede una moltitudine di prodotti di miscelazione. Si può anche cambiare la frequenza BF a $\qty{1}{\kilo\hertz}$ per vedere come si spostano le bande laterali.

[include:applet_am_modulator]

</webonly>

<indepth>
Un segnale AM può anche essere descritto matematicamente. Consideriamo prima un segnale BF sinusoidale normalizzato

$m(t)=\cos(\omega t)$

con la pulsazione $\omega=2\pi f_\mathrm{m}$. Con la sua ampiezza $\hat U_\mathrm{m}$ e una componente continua aggiuntiva $U_\mathrm{G}$ si ottiene

$U_\mathrm{m}(t)=U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)$

Questo segnale viene ora moltiplicato per il segnale portante ad alta frequenza

$U_\mathrm{T}(t)=\cos(\Omega t)$

con $\Omega=2\pi f_\mathrm{T}$. Per il segnale AM risulta quindi:

$U_\mathrm{AM}(t)=\left(U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)\right)\cdot\cos(\Omega t)$

Sviluppando si ottiene:

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\hat U_\mathrm{m}\cdot\cos(\omega t)\cdot\cos(\Omega t)$

Con la relazione

$\cos(a)\cdot\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$

il secondo termine può essere ulteriormente scomposto:

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\frac{\hat U_\mathrm{m}}{2}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

Si riconoscono così immediatamente i tre componenti di un segnale AM: il primo termine descrive la *portante* alla frequenza $\Omega$. Gli altri due termini formano la *banda laterale superiore e inferiore* alle frequenze $\Omega+\omega$ e $\Omega-\omega$.

La componente continua $U_\mathrm{G}$ è responsabile del fatto che la portante viene mantenuta. Anche quando il segnale utile è momentaneamente zero, viene comunque generato un segnale portante.

[picture:1127:a_am_modulation:Spettro di un segnale AM con portante e due bande laterali]

</indepth>

Questo principio è illustrato nella domanda seguente: un diodo viene alimentato contemporaneamente con un segnale BF e un segnale HF e il segnale di uscita viene filtrato con un circuito oscillante LC.

[question:AD507]

---

Con quattro diodi disposti ad anello è possibile costruire un modulatore in modo che la portante in uscita sia soppressa. Abbiamo già conosciuto un tale circuito nel capitolo "Miscelatore II" come *miscelatore bilanciato*. Lì veniva utilizzato per convertire un segnale HF in una frequenza intermedia. Nel trasmettitore utilizziamo ora lo stesso principio di base per generare un segnale modulato.

<margin>
[picture:759:a_balancemodulator:Modulatore bilanciato con anello di diodi]
</margin>

Un miscelatore bilanciato o modulatore bilanciato è tipicamente riconoscibile dall'anello di diodi, come mostrato nella figura [ref:a_balancemodulator]. L'anello di diodi è pilotato dal segnale dell'oscillatore $f_\mathrm{OSZ}$. A seconda della polarità del segnale dell'oscillatore, conduce una delle due coppie di diodi opposte.

Di conseguenza, il segnale BF viene trasmesso all'uscita alternativamente con la stessa polarità o con polarità invertita. In termini semplificati, il segnale BF viene quindi moltiplicato per il segnale dell'oscillatore.

Il vantaggio decisivo del circuito simmetrico è la *soppressione della portante*: le componenti del segnale dell'oscillatore si annullano idealmente a vicenda in uscita. Senza segnale BF, quindi, non viene generato alcun segnale di uscita. Se invece viene applicato un segnale BF, si generano la banda laterale superiore e quella inferiore, mentre la portante rimane soppressa.

Il segnale di uscita è chiamato *segnale a doppia banda laterale con portante soppressa* (DSB).

[question:AE206]
[question:AF302]
[question:AF308]
[question:AD510]

<indepth>
La soppressione della portante di un modulatore bilanciato può essere descritta in modo semplificato con due rami simmetrici:

$u_1(t)=\left(U_G+\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

$u_2(t)=\left(U_G-\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

In uscita, i due segnali vengono sottratti l'uno dall'altro:

$u_\mathrm{out}(t)=u_1(t)-u_2(t)$

Risulta quindi:

$u_\mathrm{out}(t)=U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)-U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Le due componenti portanti $U_G\cos(\Omega t)$ si annullano. Rimane:

$u_\mathrm{out}(t)=2\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Con $\cos(a)\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$ segue:

$u_\mathrm{out}(t)=\hat U_\mathrm{m}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

Il segnale di uscita contiene quindi solo la banda laterale superiore e quella inferiore. La portante a $\Omega$ è soppressa.
</indepth>

---

Affinché il segnale dell'oscillatore si annulli il più completamente possibile in uscita, il circuito deve essere simmetrico, cioè *bilanciato*. Anche piccole differenze in ampiezza o fase tra i due percorsi del segnale fanno sì che una parte residua della portante rimanga in uscita. La simmetria di ampiezza può essere ad esempio compensata con un potenziometro. Per la compensazione di fase, in alcuni circuiti viene utilizzato anche un condensatore di regolazione. L'obiettivo della regolazione è una soppressione della portante il più alta possibile, mantenendo le due bande laterali di modulazione.

<webonly>
Il seguente applet mostra la regolazione della portante. Quando il cursore sul lato destro viene spostato, la portante appare improvvisamente nello spettro.

[include:applet_dsp]
</webonly>

[question:AF309]

---

Il modulatore bilanciato costituisce il primo stadio di un modulatore SSB e genera un segnale DSB. Dopo il modulatore bilanciato segue come secondo stadio un filtro passa-banda a banda stretta, come nella figura [ref:a_ssb_modulation]. Esso lascia passare solo una delle due bande laterali e sopprime l'altra. In uscita si ottiene così un segnale a banda laterale unica (SSB).

<margin>
[picture:500:a_ssb_modulation:Schema a blocchi per la modulazione SSB con il metodo a filtro]
</margin>

[question:AF306]
[question:AF304]
[question:AF303]
[question:AF305]

---

Una buona implementazione per un apparecchio radio che debba generare sia USB che LSB consiste nel progettare il filtro passa-banda in modo fisso per una determinata banda di frequenza. Il fatto che venga filtrata la banda laterale superiore o inferiore non è determinato da una modifica del filtro, ma dalla frequenza dell'oscillatore nel modulatore bilanciato. A questo scopo sono disponibili due oscillatori a quarzo diversi.

Se ad esempio per USB viene scelta la frequenza dell'oscillatore $\qty{8998,5}{\kilo\hertz}$, la modulazione genera due bande laterali. La banda laterale superiore viene spostata esattamente nella banda passante del filtro costante, mentre la banda laterale inferiore si trova al di fuori della banda passante e viene soppressa.

Per LSB si passa all'altra frequenza del quarzo di $\qty{9001,5}{\kilo\hertz}$. In questo modo l'intero spettro DSB si sposta in modo che ora la banda laterale inferiore cada nella banda passante dello stesso filtro e la banda laterale superiore venga soppressa.

Il trucco decisivo consiste quindi nel lasciare il filtro invariato e invece spostare la posizione del segnale DSB utilizzando diverse frequenze dell'oscillatore. Similmente alla frequenza intermedia di un ricevitore, è così possibile utilizzare un filtro di alta qualità, sintonizzato in modo fisso, per diverse posizioni di frequenza.

[question:AF307]

<margin>
<latexonly>
[picture:831:a_ssb_modulation_lsb:Frequenze con il metodo a filtro per LSB]
[picture:940:a_ssb_modulation_lsb:Spettro con il metodo a filtro per LSB]
[picture:832:a_ssb_modulation_usb:Frequenze con il metodo a filtro per USB]
[picture:941:a_ssb_modulation_usb:Spettro con il metodo a filtro per USB]
</latexonly>
<webonly>
[include:applet_dsp_filter]
</webonly>
</margin>

---

Per la generazione di un segnale modulato in frequenza (FM) può essere utilizzato un *diodo a capacità variabile*. Nei diagrammi circuitali è riconoscibile dal piccolo simbolo del condensatore accanto al diodo, come nella figura [ref:a_fm_modulator].

Un diodo a capacità variabile viene polarizzato in polarizzazione inversa. La sua capacità dipende dalla tensione inversa applicata. Se viene utilizzato come parte del circuito oscillante che determina la frequenza di un oscillatore, una variazione di questa tensione modifica la frequenza di risonanza del circuito oscillante e quindi la frequenza dell'oscillatore.

Per la modulazione di frequenza, al segnale BF viene sovrapposta la tensione continua sul diodo a capacità variabile. Di conseguenza, la sua capacità cambia in sincronia con il segnale BF e la frequenza dell'oscillatore viene spostata verso l'alto e verso il basso. In questo modo si genera un segnale modulato in frequenza.

<margin>
[picture:155:a_fm_modulator:Modulatore FM con diodo a capacità variabile]
</margin>

[question:AD508]
[question:AF310]

---

Con grandi tensioni BF si possono facilmente causare variazioni di frequenza dell'oscillatore ("deviazione" FM) molto maggiori di quelle consentite. Pertanto, è necessaria una limitazione della "deviazione" mediante una regolazione e limitazione dell'ampiezza della BF. Diodi collegati in antiparallelo limitano la tensione a circa la tensione di ginocchio del diodo. Un esempio è mostrato nelle figure [ref:a_fm_modulator_hub1] e [ref:a_fm_modulator_hub2].

<margin>
[picture:44:a_fm_modulator_hub1:Circuito per la limitazione della deviazione]
[picture:828:a_fm_modulator_hub2:Limitazione del segnale]
</margin>

[question:AD509]
