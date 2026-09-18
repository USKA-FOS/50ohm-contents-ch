I circuiti integrati sono circuiti complessi realizzati su un substrato semiconduttore. Costituiscono quindi un ausilio essenziale per la costruzione di circuiti elettronici.

[question:AC601]

<margin>
[photo:334:a_ic:Trasmettitore in banda corta TinyWhisper della JKU Linz e JMU Würzburg realizzato come circuito integrato in tecnologia CMOS 130nm]
</margin>

Come classe speciale di circuiti integrati esistono i Monolithic Microwave Integrated Circuits (MMIC). Essi combinano sia componenti attivi che passivi sullo stesso substrato. Questi circuiti sono tipicamente progettati per un’impedenza di ingresso e di uscita di $\qty{50}{\ohm}$. Con essi è possibile ottenere un’elevata amplificazione a banda larga con pochi componenti.

[question:AC602]
[question:AC603]
[question:AC604]

---

Per risolvere gli esercizi d’esame è utile analizzare più in dettaglio il circuito mostrato in [ref:a_mmic].

I condensatori $C_1$ e $C_3$ fungono da condensatori di accoppiamento. Lasciano passare i segnali ad alta frequenza (HF), ma bloccano la tensione continua. In questo modo si evita che le tensioni continue vengano trasmesse tra le diverse sezioni del circuito e influenzino il punto di funzionamento.

La bobina d’arresto nel conduttore della tensione di servizio $U_\mathrm{CC}$ impedisce che i segnali ad alta frequenza defluiscano attraverso l’alimentazione elettrica. Per le alte frequenze, la bobina d’arresto presenta un’elevata impedenza e agisce quindi come un blocco. Il condensatore $C_2$ serve per il disaccoppiamento HF della tensione di alimentazione. Conduce le eventuali componenti HF verso massa e garantisce che la tensione di alimentazione rimanga stabile dal punto di vista HF. Insieme alla bobina d’arresto, forma un disaccoppiamento HF della tensione di servizio. Questo circuito lo impareremo a conoscere più avanti come "Bias-T".

Una particolarità di molti MMIC è che la tensione di alimentazione viene fornita tramite l’uscita. La resistenza $R_\text{BIAS}$ imposta il punto di funzionamento del MMIC.

<margin>
[picture:773:a_mmic:Circuito MMIC]
</margin>

A seconda del compito da svolgere, dal calo di tensione ai capi del MMIC si può determinare prima il calo di tensione sulla resistenza $R_\text{BIAS}$. Con il valore noto della resistenza, è quindi possibile calcolare la corrente che fluisce nel circuito. La stessa corrente attraversa anche il MMIC, consentendo ad esempio di determinare la potenza dissipata termicamente.

I seguenti esercizi possono quindi essere risolti in modo molto simile ai circuiti già noti con transistor bipolari.

[question:AF425]
[question:AF426]
[question:AF427]

% Un ausilio essenziale nella costruzione di circuiti elettronici
% è l’utilizzo di circuiti integrati.
% Un circuito integrato contiene in un involucro un circuito elettronico complesso,
% prodotto su un chip.

% "Informazioni aggiuntive" Applicazioni pratiche:
% Amplificatore operazionale: vedere sezione ...
% Amplificatore a bassa frequenza: vedere sezione ...
% Amplificatore a microonde MMIC: vedere sezione ...
% Circuito combinato mixer e oscillatore: vedere sezione ...
% Ricevitori completi: vedere sezione ...
% Circuiti digitali: vedere sezione ...
% Circuiti PLL: vedere sezione ...

% Con pochi componenti esterni è possibile realizzare, ad esempio, un amplificatore audio,
% un oscillatore con mixer o addirittura un ricevitore completo in banda corta.
% Immagine di un IC con sigla e schema a blocchi, ad esempio LM386
% Per frequenze a partire da circa 100 MHz si utilizzano i cosiddetti Monolithic Microwave Integrated Circuit (MMIC).
% Immagine MMIC MSA 0686 o ERA 3
% Si tratta di un amplificatore in grado di amplificare in modo ampio la banda di frequenza da 100 MHz a 2 GHz di 20 dB
% ed è adattato per un carico di 50 ohm sia in ingresso che in uscita.
% È sufficiente impostare la corrente per il punto di funzionamento secondo la scheda tecnica, in modo che il MMIC non venga sovraccaricato termicamente.
% A questo scopo, con una tensione di servizio data, è necessario calcolare una resistenza e il suo carico elettrico.

% Poiché il MMIC è un involucro per tecnologia SMD, è necessario realizzare anche il circuito di accoppiamento esterno in tecnologia SMD.
% La struttura complessiva dell’amplificatore risulterà quindi notevolmente più piccola rispetto alla tecnologia a componenti discreti.
% Immagine confronto tra circuito discreto e MMIC