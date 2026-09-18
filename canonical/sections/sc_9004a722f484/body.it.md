Abbiamo già incontrato i diodi in diversi circuiti. Ora esaminiamo come la loro caratteristica non lineare possa essere utilizzata per modulare un segnale portante ad alta frequenza con un segnale utile a bassa frequenza.

Se un segnale HF e un segnale BF vengono applicati insieme a un diodo, come mostrato nella figura [ref:a_am_modulator], la tensione BF influisce sulla conduttività del diodo. Di conseguenza, il segnale HF viene trasmesso con intensità variabile a seconda del valore istantaneo della BF. La sua ampiezza, quindi, varia in sintonia con il segnale BF.

All’uscita si generano, oltre alla portante HF originale, due bande laterali sopra e sotto la frequenza portante. Un circuito oscillante sintonizzato sulla frequenza portante sopprime ulteriori componenti indesiderate. All’uscita si ottiene così un segnale modulato in ampiezza (AM).

<margin>
[picture:772:a_am_modulator:Modulatore AM semplice con diodo e circuito oscillante]
</margin>

<webonly>
La seguente simulazione mostra il funzionamento del modulatore AM; i valori sono stati scelti in modo che HF e BF siano ben distinguibili. La BF è a $\qty{500}{\hertz}$, l’HF a $\qty{10}{\kilo\hertz}$. L’ampiezza del segnale HF viene modificata in base alla BF. Il circuito oscillante è sintonizzato sulla frequenza portante e sopprime le componenti indesiderate. Se si rimuove il circuito oscillante, si osservano numerosi prodotti di mescolamento. È possibile anche modificare la frequenza BF a $\qty{1}{\kilo\hertz}$ per vedere come si spostano le bande laterali.

[include:applet_am_modulator]
</webonly>

<indepth>
Un segnale AM può essere descritto anche matematicamente. A tal fine, consideriamo inizialmente un segnale BF sinusoidale normalizzato

$m(t)=\cos(\omega t)$

con la pulsazione $\omega=2\pi f_\mathrm{m}$. Con la sua ampiezza $\hat U_\mathrm{m}$ e un componente continuo aggiuntivo $U_\mathrm{G}$, si ottiene

$U_\mathrm{m}(t)=U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)$

Questo segnale viene ora moltiplicato per il segnale portante ad alta frequenza

$U_\mathrm{T}(t)=\cos(\Omega t)$

con $\Omega=2\pi f_\mathrm{T}$. Per il segnale AM si ottiene quindi:

$U_\mathrm{AM}(t)=\left(U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)\right)\cdot\cos(\Omega t)$

Sviluppando l’espressione si ottiene:

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\hat U_\mathrm{m}\cdot\cos(\omega t)\cdot\cos(\Omega t)$

Utilizzando la relazione

$\cos(a)\cdot\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$

il secondo termine può essere ulteriormente scomposto:

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\frac{\hat U_\mathrm{m}}{2}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

Si possono così identificare immediatamente i tre componenti di un segnale AM: il primo termine descrive la *portante* alla frequenza $\Omega$. Gli altri due termini formano le *bande laterali superiore e inferiore* alle frequenze $\Omega+\omega$ e $\Omega-\omega$.

Il componente continuo $U_\mathrm{G}$ è responsabile del mantenimento della portante. Anche quando il segnale utile è momentaneamente nullo, viene comunque generato un segnale portante.

[picture:1127:a_am_modulation:Spettro di un segnale AM con portante e due bande laterali]

</indepth>

Questo principio è chiarito nella domanda seguente: un diodo viene alimentato contemporaneamente con un segnale BF e un segnale HF, e il segnale di uscita viene filtrato con un circuito LC oscillante.

[question:AD507]

---

Con quattro diodi disposti ad anello è possibile realizzare un modulatore in modo che la portante sia soppressa all’uscita. Un circuito di questo tipo è già stato presentato nel capitolo "Mixer II" come *miscelatore bilanciato*. In quel contesto veniva utilizzato per convertire un segnale HF in una frequenza intermedia. Nel trasmettitore utilizziamo lo stesso principio di base per generare un segnale modulato.

<margin>
[picture:759:a_balancemodulator:Modulatore bilanciato con anello di diodi]
</margin>

Un miscelatore bilanciato o modulatore bilanciato si riconosce tipicamente dall’anello di diodi, come mostrato nella figura [ref:a_balancemodulator]. L’anello di diodi viene pilotato dal segnale dell’oscillatore a frequenza $f_\mathrm{OSZ}$. A seconda della polarità del segnale dell’oscillatore, conducono alternativamente una delle due coppie di diodi opposte.

In questo modo, il segnale BF viene trasmesso all’uscita alternativamente con polarità uguale o invertita. In termini semplificati, il segnale BF viene quindi moltiplicato per il segnale dell’oscillatore.

Il vantaggio decisivo del circuito simmetrico è la *soppressione della portante*: le componenti del segnale dell’oscillatore si annullano idealmente tra loro all’uscita. Senza segnale BF, quindi, non si genera alcun segnale di uscita. Se invece viene applicato un segnale BF, si generano le bande laterali superiore e inferiore, mentre la portante rimane soppressa.

Il segnale di uscita viene definito come *segnale a doppia banda laterale con portante soppressa* (DSB).

[question:AE206]
[question:AF302]
[question:AF308]
[question:AD510]

<indepth>
La soppressione della portante di un modulatore bilanciato può essere descritta in modo semplificato con due rami simmetrici:

$u_1(t)=\left(U_G+\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

$u_2(t)=\left(U_G-\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

All’uscita i due segnali vengono sottratti:

$u_\mathrm{out}(t)=u_1(t)-u_2(t)$

Si ottiene quindi:

$u_\mathrm{out}(t)=U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)-U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Le due componenti della portante $U_G\cos(\Omega t)$ si annullano a vicenda. Rimane:

$u_\mathrm{out}(t)=2\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Con $\cos(a)\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$ si ottiene:

$u_\mathrm{out}(t)=\hat U_\mathrm{m}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

Il segnale di uscita contiene quindi solo la banda laterale superiore e quella inferiore. La portante alla frequenza $\Omega$ è soppressa.
</indepth>

---

Affinché il segnale dell’oscillatore si annulli il più possibile all’uscita, il circuito deve essere simmetrico, cioè *bilanciato*. Anche piccole differenze di ampiezza o fase tra i due percorsi del segnale fanno sì che una parte della portante rimanga all’uscita. La simmetria dell’ampiezza può essere regolata, ad esempio, con un potenziometro. Per la regolazione della fase, in alcuni circuiti viene utilizzato un condensatore di taratura. L’obiettivo della regolazione è ottenere una soppressione della portante il più possibile elevata, mantenendo intatte le due bande laterali di modulazione.

<webonly>
Il seguente applet mostra la regolazione della portante. Se lo slider sulla destra viene spostato, la portante appare improvvisamente nello spettro.

[include:applet_dsp]
</webonly>

[question:AF309]

---

Il modulatore bilanciato costituisce il primo stadio di un modulatore SSB e genera un segnale DSB. Dietro il modulatore bilanciato, come secondo stadio, segue un filtro passa-banda a banda stretta, come mostrato nella figura [ref:a_ssb_modulation]. Esso lascia passare solo una delle due bande laterali e sopprime l’altra. All’uscita si ottiene così un segnale a banda laterale singola (SSB).

<margin>
[picture:500:a_ssb_modulation:Schema a blocchi per la modulazione SSB con il metodo del filtro]
</margin>

[question:AF306]
[question:AF304]
[question:AF303]
[question:AF305]

---

Una buona implementazione per un apparecchio radio in grado di generare sia USB che LSB consiste nel progettare il filtro passa-banda per una gamma di frequenze fissa. La scelta di quale banda laterale venga filtrata non dipende da una modifica del filtro, ma dalla frequenza dell’oscillatore nel modulatore bilanciato. A tal fine sono disponibili due oscillatori al quarzo diversi.

Ad esempio, per l’USB si seleziona la frequenza dell’oscillatore $\qty{8998,5}{\kilo\hertz}$. Attraverso la modulazione si generano due bande laterali. La banda laterale superiore viene spostata esattamente nella banda passante del filtro, mentre la banda laterale inferiore si trova al di fuori della banda passante e viene soppressa.

Per l’LSB si passa all’altra frequenza di quarzo di $\qty{9001,5}{\kilo\hertz}$. In questo modo l’intero spettro DSB viene spostato in modo che la banda laterale inferiore cada nella banda passante dello stesso filtro, mentre la banda laterale superiore viene soppressa.

Il trucco decisivo consiste quindi nel mantenere invariato il filtro e, invece, spostare la posizione del segnale DSB utilizzando frequenze dell’oscillatore diverse. Analogamente alla frequenza intermedia di un ricevitore, è possibile utilizzare un filtro fisso di alta qualità per diverse posizioni di frequenza.

[question:AF307]

<margin>
<latexonly>
[picture:831:a_ssb_modulation_lsb:Frequenze con il metodo del filtro per LSB]
[picture:940:a_ssb_modulation_lsb:Spettro con il metodo del filtro per LSB]
[picture:832:a_ssb_modulation_usb:Frequenze con il metodo del filtro per USB]
[picture:941:a_ssb_modulation_usb:Spettro con il metodo del filtro per USB]
</latexonly>
<webonly>
[include:applet_dsp_filter]
</webonly>
</margin>

---

Per generare un segnale modulato in frequenza (FM) può essere utilizzato un *diodo a capacità variabile*. Nei diagrammi di circuito è riconoscibile dal piccolo simbolo del condensatore accanto al diodo, come mostrato nella figura [ref:a_fm_modulator].

Un diodo a capacità variabile viene utilizzato in polarizzazione inversa. La sua capacità dipende dalla tensione inversa applicata. Se viene impiegato come parte del circuito oscillante che determina la frequenza di un oscillatore, una variazione di questa tensione modifica la frequenza di risonanza del circuito oscillante e, di conseguenza, la frequenza dell’oscillatore.

Per la modulazione di frequenza, al segnale BF alla tensione continua del diodo a capacità variabile viene sovrapposto il segnale BF. In questo modo la sua capacità varia in sintonia con il segnale BF e la frequenza dell’oscillatore viene spostata verso l’alto e verso il basso di conseguenza. In questo modo si ottiene un segnale modulato in frequenza.

<margin>
[picture:155:a_fm_modulator:Modulatore FM con diodo a capacità variabile]
</margin>

[question:AD508]
[question:AF310]

---

Con grandi tensioni BF è possibile ottenere facilmente deviazioni della frequenza dell’oscillatore ("deviazione" FM) molto più ampie di quelle consentite. Pertanto, è necessaria una *limitazione della deviazione* mediante la regolazione e la limitazione dell’ampiezza del segnale BF. Diodi collegati antiparallelamente limitano la tensione a circa la tensione di soglia del diodo. Un esempio è mostrato nelle figure [ref:a_fm_modulator_hub1] e [ref:a_fm_modulator_hub2].

<margin>
[picture:44:a_fm_modulator_hub1:Circuito per la limitazione della deviazione]
[picture:828:a_fm_modulator_hub2:Limitazione del segnale]
</margin>

[question:AD509]