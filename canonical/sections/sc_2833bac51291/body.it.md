I circuiti integrati sono circuiti complessi realizzati su un substrato semiconduttore. Rappresentano quindi un notevole aiuto per la costruzione di circuiti elettronici.

[question:AC601]

<margin>
[photo:334:a_ic:Trasmettitore onde corte TinyWhisper della JKU Linz e JMU Würzburg realizzato come circuito integrato in tecnologia CMOS da 130nm]
</margin>

Come classe speciale di circuiti integrati esistono i circuiti integrati monolitici a microonde (MMIC). Essi combinano elementi attivi e passivi sullo stesso substrato. Questi sono tipicamente progettati per un'impedenza di ingresso e uscita di $\qty{50}{\ohm}$. Con essi è possibile ottenere un'elevata amplificazione a banda larga con pochi componenti.

[question:AC602]
[question:AC603]
[question:AC604]

---

Per il calcolo dei problemi dell'esame, è utile esaminare più da vicino il circuito nella figura [ref:a_mmic].

I condensatori $C_1$ e $C_3$ fungono da condensatori di accoppiamento. Lasciano passare i segnali HF, ma bloccano la corrente continua. Ciò impedisce che le tensioni continue vengano trasmesse tra i singoli stadi del circuito e influenzino il punto di funzionamento.

La bobina nella linea di alimentazione $U_\mathrm{CC}$ impedisce che i segnali HF possano defluire attraverso l'alimentazione elettrica. Per le alte frequenze, la bobina ha un'alta resistenza e agisce quindi come un blocco. Il condensatore $C_2$ serve per il disaccoppiamento HF dell'alimentazione elettrica. Esso scarica le restanti componenti HF verso massa e garantisce che l'alimentazione elettrica rimanga stabile dal punto di vista HF. Insieme alla bobina, forma un disaccoppiamento HF dell'alimentazione elettrica. Impareremo a conoscere questo circuito più tardi come "Bias-T".

Una particolarità di molti MMIC è che la tensione di alimentazione viene fornita attraverso l'uscita. La resistenza $R_\text{BIAS}$ imposta il punto di funzionamento dell'MMIC.

<margin>
[picture:773:a_mmic:Circuito MMIC]
</margin>

A seconda del problema, dalla caduta di tensione attraverso l'MMIC si può prima determinare la caduta di tensione attraverso la resistenza $R_\text{BIAS}$. Con il valore di resistenza noto, è quindi possibile calcolare la corrente attraverso il circuito. La stessa corrente scorre anche attraverso l'MMIC, permettendo così, ad esempio, di determinare la potenza dissipata termica.

I seguenti problemi possono quindi essere risolti in modo molto simile ai circuiti già noti con transistor bipolari.

[question:AF425]
[question:AF426]
[question:AF427]

% Un notevole aiuto nella costruzione di circuiti elettronici 
% è l'uso di circuiti integrati.
% Un circuito integrato contiene in un unico alloggiamento un complesso circuito elettronico, 
% che è stato prodotto su un chip.

% "Informazioni aggiuntive" Applicazioni pratiche:
% Amplificatore operazionale: vedi sezione ...
% Amplificatore a bassa frequenza: vedi sezione ...
% Amplificatore a microonde MMIC: vedi sezione ...
% Circuito combinato mixer e oscillatore: vedi sezione ...
% Ricevitori completi: vedi sezione ...
% Circuiti digitali: vedi sezione ...
% Circuiti PLL: vedi sezione ...

% Con pochi componenti esterni, ad esempio, si può realizzare un amplificatore audio, un oscillatore con mixer o persino un ricevitore onde corte completo.
% Immagine di un IC con designazione del tipo e schema a blocchi, ad es. LM386
% Per frequenze da circa 100 MHz in su, vengono utilizzati i cosiddetti circuiti integrati monolitici a microonde (MMIC).
% Immagine MMIC MSA 0686 o ERA 3
% Si tratta di un amplificatore che può amplificare a banda larga la gamma di frequenza da 100 MHz a 2 GHz di 20 dB
% ed è adattato per un carico di 50 Ohm in ingresso e in uscita.
% È sufficiente impostare la corrente per il punto di funzionamento secondo la scheda tecnica, in modo che l'MMIC non venga sovraccaricato termicamente.
% Per fare ciò, con una tensione di servizio predefinita, è necessario calcolare una resistenza e il suo carico elettrico.

% Poiché l'MMIC ha un alloggiamento per la tecnologia SMD, è necessario eseguire anche il cablaggio esterno in tecnologia SMD.
% La struttura complessiva dell'amplificatore sarà quindi molto più piccola rispetto alla precedente tecnologia a circuiti discreti.
% Immagine confronto circuito discreto e MMIC



