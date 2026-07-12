Finora conosciamo i diodi a semiconduttore solo nella loro funzione di raddrizzatori di una tensione alternata. Nei modulatori per la generazione di segnali AM e SSB, i diodi svolgono un nuovo ruolo: una tensione audio applicata ne aumenta o diminuisce la resistenza al ritmo della frequenza audio; maggiore è la tensione audio, maggiore è la corrente del diodo e minore è la resistenza risultante. In un modulatore di ampiezza, questa resistenza viene utilizzata per influenzare l'ampiezza di un segnale HF (proveniente da un oscillatore locale); la corrente HF attraverso il diodo è grande quando la resistenza del diodo è piccola e viceversa. Il segnale HF viene "modulato" nella sua ampiezza al ritmo del segnale audio! Nel caso più semplice, se si utilizza un solo diodo, lo spettro del segnale contiene una portante (alla frequenza HF originale) e due bande laterali di modulazione alla distanza della frequenza audio sopra e sotto la frequenza portante – un segnale con modulazione di ampiezza (AM).

Questo principio diventa chiaro nella seguente domanda: un diodo viene sollecitato contemporaneamente da un segnale audio e da un segnale HF e il segnale di uscita viene filtrato con un circuito oscillante LC.

[question:AD507]

Con un circuito di quattro diodi disposti ad anello, la portante può anche essere soppressa e rimangono solo le due bande laterali; per fare ciò, l'anello di diodi deve essere integrato in un circuito push-pull che sia bilanciato (o simmetrizzato) in modo tale che le correnti del segnale portante si annullino all'uscita. Nel capitolo "Mixer II" è già stato mostrato un circuito del genere come "miscelatore bilanciato" (inglese "balanced mixer"), anche se lì per convertire un segnale di ingresso HF in una posizione di frequenza intermedia.

Il modulatore bilanciato è il primo stadio di un modulatore a banda laterale singola - genera da un segnale dell'oscillatore locale e da un segnale audio (modulazione) un segnale a doppia banda laterale (DSB). Dietro segue un filtro passa-banda che lascia passare solo una delle due bande laterali, generando così un segnale SSB all'uscita.

Si pensi ai due stadi necessari del modulatore SSB.

[question:AE206]

[question:AF302]

---

Si riconosce un miscelatore bilanciato o modulatore bilanciato dall'anello di diodi. In questo circuito non c'è un'eccitazione push-pull completa, poiché viene utilizzato un solo trasformatore, tuttavia esiste l'equivalente di un presa centrale di un trasformatore nell'alimentazione del segnale dell'oscillatore al centro di un partitore di tensione (potenziometro).

[question:AF308]

<indepth>
Nel trasmettitore, il miscelatore bilanciato diventa un modulatore bilanciato scambiando gli ingressi: la modulazione a bassa frequenza viene accoppiata nel ramo a ponte del circuito push-pull tra la presa centrale di T2 e la massa. Il segnale dell'oscillatore locale viene immesso nell'anello di diodi tramite T1 e il segnale a doppia banda laterale viene estratto tramite T2. Senza una tensione di modulazione, le coppie di diodi D1, D2 e D3, D4 vengono commutate alternativamente formando partitori di tensione 1:1, in modo che i loro punti medi si trovino a potenziale di massa. In questo modo, le estremità superiore e inferiore dell'avvolgimento di T2 si trovano alternativamente a potenziale di massa, mentre l'altra estremità dell'avvolgimento rimane scollegata a causa dei diodi bloccati. Pertanto, non scorre corrente nell'avvolgimento e non si genera alcuna tensione sul lato di uscita – questo è ciò che costituisce la "soppressione della portante"!

Quando viene applicata una tensione di modulazione, scorre corrente aggiuntiva attraverso i diodi, in modo che il potenziale del punto medio dei partitori di tensione venga spostato – in questo modo la corrente può fluire nel trasformatore T2 e si genera un segnale di uscita. L'immagine mostra i profili di tensione che si verificano quando il segnale dell'oscillatore viene semplificato come funzione a onda quadra.
</indepth>

---

La soppressione della portante ha a che fare con l'annullamento di un segnale indesiderato – per questo un circuito modulatore deve essere "bilanciato".

[question:AD510]

Proprio a questo bilanciamento appartiene una regolazione delle ampiezze (potenziometro) e delle fasi (trimmer C).

[question:AF309]

Un modulatore viene "simmetrizzato" o "bilanciato" per sopprimere la portante – le bande laterali di modulazione non vengono soppresse.

[question:AF304]

[question:AF303]

Dopo il modulatore bilanciato segue il secondo stadio di un modulatore SSB.

[question:AF305]

[question:AF306]

I quarzi determinano la frequenza della portante soppressa dal modulatore bilanciato. Si riconosce dalla frequenza del quarzo per la banda laterale inferiore (LSB): la portante si trova $\qty{1,5}{\kilo\hertz}$ sopra la frequenza centrale del filtro passa-banda da $\qty{9}{\mega\hertz}$. Con la frequenza audio massima di $\qty{3}{\kilo\hertz}$, la banda laterale inferiore si troverà quindi $\qty{1,5}{\kilo\hertz}$ sotto la frequenza centrale e la frequenza audio di $\qty{200}{\hertz}$ posizionerà la banda laterale a $\qty{1,3}{\kilo\hertz}$ sopra la frequenza centrale del filtro. Per la banda laterale superiore (USB) vale il contrario.

[question:AF307]

Il simbolo a croce o X nel blocco funzionale dietro l'amplificatore audio sta per la moltiplicazione matematica – modulatori, demodulatori e circuiti mixer vengono contrassegnati in questo modo perché la loro funzione può essere descritta matematicamente come la moltiplicazione di funzioni segnale.

Un modulatore per la modulazione di frequenza (FM) utilizza invece un altro tipo di diodo, il diodo capacità (riconoscibile nei circuiti dal piccolo simbolo di condensatore accanto al simbolo del diodo). Il diodo fa sempre parte di un circuito oscillante la cui frequenza di oscillazione è determinata da un circuito risonante che contiene il diodo capacità. Il diodo viene sollecitato con una tensione continua in direzione di blocco, in modo che si stabilisca una capacità fissa del diodo e quindi anche una frequenza dell'oscillatore. Il circuito diventa un modulatore di frequenza quando alla tensione continua viene sovrapposto un segnale audio – quindi l'oscillatore cambia la sua frequenza al ritmo del segnale audio.

Qui compare il diodo capacità – e il circuito a transistor accanto è un oscillatore con circuito oscillante LC.

[question:AD508]

Un diodo capacità funzionante in tensione inversa, che viene sollecitato da un lato con audio e dall'altro lato è parallelo al circuito oscillante di un circuito oscillatore, influenza la frequenza dell'oscillatore.

[question:AF310]

Con tensioni audio elevate si possono facilmente ottenere variazioni di frequenza dell'oscillatore molto maggiori (deviazione FM) di quelle ammesse. Pertanto, è necessaria una limitazione della "deviazione" tramite una regolazione e limitazione dell'ampiezza audio. Diodi collegati in antiparallelo limitano la tensione a circa la tensione di ginocchio del diodo.

[question:AD509]

Questo apparentemente non è un modulatore – c'è un solo segnale! Un condensatore elettrolitico all'uscita del diodo indica una tensione continua!

[question:AD503]

% TODO copiato da E qui... deve essere inserito.
<margin>
[picture:500:e_ssb_modulation:Schema a blocchi per la modulazione SSB con il metodo a filtro]
[picture:831:e_ssb_modulation_lsb:Frequenze con il metodo a filtro per LSB]
[picture:940:e_ssb_modulation_lsb:Spettro con il metodo a filtro per LSB]
[picture:832:e_ssb_modulation_usb:Frequenze con il metodo a filtro per USB]
[picture:941:e_ssb_modulation_usb:Spettro con il metodo a filtro per USB]
</margin>