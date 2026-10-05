Le misurazioni importanti per il radioamatore sui trasmettitori sono le misurazioni delle potenze di uscita dei trasmettitori o la misurazione delle tensioni RF nelle parti dei circuiti RF. Nella misurazione delle potenze di uscita del trasmettitore, il trasmettitore deve essere terminato con un'impedenza definita, che corrisponde all'impedenza di uscita del trasmettitore. Nell'ambito radioamatoriale, l'impedenza usuale (terminazione del trasmettitore) è $\qty{50}{\ohm}$. La terminazione può anche avvenire direttamente nel circuito di misura, il che tuttavia ha senso solo per piccole potenze.

La misurazione delle tensioni RF avviene mediante una sonda RF tramite raddrizzamento a diodo e successivo livellamento della tensione continua risultante con un condensatore posto a valle. La figura [ref:hf_messkopf_0] mostra il principio di una sonda RF con raddrizzamento semplice e livellamento della tensione continua. La tensione RF viene terminata correttamente in impedenza all'ingresso tramite una resistenza (o una combinazione di resistenze). Successivamente avviene il raddrizzamento tramite diodo, la cui tensione di uscita si calcola come valore di picco meno la tensione di soglia del diodo e viene tamponata nel condensatore a valle. La figura [ref:hf_messkopf_1] mostra una sonda RF autocostruita, la figura [ref:hf_messkopf_2] lo schema elettrico corrispondente.

<margin>
[picture:576:hf_messkopf_0:Principio di una sonda RF con raddrizzamento semplice e livellamento della tensione continua]
[photo:338:hf_messkopf_1:Sonda RF autocostruita di DL3JOP]
[photo:339:hf_messkopf_2:Schema elettrico sonda RF di DL3JOP]
</margin>

[question:AI608]

Per potenze RF più elevate deve essere inserito un attenuatore adeguatamente resistente, che assorbe la maggior parte della potenza di uscita del trasmettitore che deve essere misurata. L'attenuatore deve essere considerato nel calcolo della potenza.

[question:AI609]

---

Per una misurazione il più accurata possibile delle tensioni e potenze RF, il circuito di misura utilizzato deve prima essere calibrato. A tal fine vengono immessi segnali di riferimento noti e vengono determinate le deviazioni tra il valore reale e quello misurato. Da queste deviazioni si possono ricavare valori di correzione dipendenti dalla frequenza e dal livello e memorizzarli, ad esempio, in una tabella come in [ref:a_frequenzgang_messwerte].

In una misurazione successiva, il valore misurato visualizzato viene corretto con il corrispondente valore di correzione. Se i valori di misura sono indicati in $\unit{\dBm}$, ad esempio, la deviazione determinata durante la calibrazione per la frequenza corrispondente può essere aggiunta come valore di correzione in $\unit{\dB}$ al valore misurato.

<margin>
| c: Frequenza in MHz | c: Potenza di trasmissione $\qty{-40}{\dBm}$ | c: Potenza di trasmissione $\qty{-20}{\dBm}$ |
| 10   | $\qty{-40,24}{\dBm}$ | $\qty{-20}{\dBm}$    |
| 50   | $\qty{-40,24}{\dBm}$ | $\qty{-20}{\dBm}$    |
| 100  | $\qty{-40,26}{\dBm}$ | $\qty{-20,12}{\dBm}$ |
| 200  | $\qty{-40,26}{\dBm}$ | $\qty{-20,2}{\dBm}$  |
| 300  | $\qty{-40,51}{\dBm}$ | $\qty{-20,32}{\dBm}$ |
| 400  | $\qty{-40,46}{\dBm}$ | $\qty{-20,28}{\dBm}$ |
| 500  | $\qty{-40,84}{\dBm}$ | $\qty{-20,64}{\dBm}$ |
| 600  | $\qty{-40,7}{\dBm}$  | $\qty{-20,41}{\dBm}$ |
| 700  | $\qty{-40,7}{\dBm}$  | $\qty{-20,53}{\dBm}$ |
| 800  | $\qty{-40,8}{\dBm}$  | $\qty{-20,55}{\dBm}$ |
| 900  | $\qty{-40,37}{\dBm}$ | $\qty{-20,2}{\dBm}$  |
| 1000 | $\qty{-40,33}{\dBm}$ | $\qty{-20,09}{\dBm}$ |
| 1100 | $\qty{-40,12}{\dBm}$ | $\qty{-19,85}{\dBm}$ |
| 1200 | $\qty{-39,94}{\dBm}$ | $\qty{-19,62}{\dBm}$ |
| 1300 | $\qty{-39,69}{\dBm}$ | $\qty{-19,49}{\dBm}$ |
| 1400 | $\qty{-40,18}{\dBm}$ | $\qty{-19,79}{\dBm}$ |
| 1500 | $\qty{-40,13}{\dBm}$ | $\qty{-19,97}{\dBm}$ |
| 1600 | $\qty{-40,95}{\dBm}$ | $\qty{-20,62}{\dBm}$ |
| 1700 | $\qty{-41,55}{\dBm}$ | $\qty{-21,64}{\dBm}$ |
| 1800 | $\qty{-41,47}{\dBm}$ | $\qty{-20,92}{\dBm}$ |
| 1900 | $\qty{-43,1}{\dBm}$  | $\qty{-23,27}{\dBm}$ |
| 2000 | $\qty{-42,34}{\dBm}$ | $\qty{-21,89}{\dBm}$ |
[table:a_frequenzgang_messwerte:Livelli misurati in funzione della frequenza per la sonda RF di DL3JOP]
</margin>

% Nota:
% Una indicazione precisa al centesimo di decibel mi sembra un po' lontana dalla pratica. Difficilmente si può misurare con tale precisione. Questo può fornire un punto di discussione durante la lezione.

[question:AI612]

Consideriamo ora il calcolo dei circuiti in dettaglio. Nelle sonde RF con un solo diodo, all'uscita di misura è misurabile la tensione di picco della tensione RF applicata meno la tensione di soglia del diodo utilizzato e di un eventuale partitore di tensione posto a monte. Una sonda RF con raddrizzamento semplice e successivo livellamento viene calcolata come segue:

Il segnale di ingresso RF viene terminato correttamente in impedenza all'ingresso dalla resistenza presente (o combinazione di resistenze singole). Nel circuito rappresentato (cfr. figura [ref:hf_messkopf_0]) la tensione RF viene dimezzata dal successivo partitore di tensione (che è anch'esso efficace rispetto all'impedenza). Successivamente avviene il raddrizzamento del valore di picco tramite diodo, la cui tensione di uscita si calcola come valore di picco meno la tensione di soglia del diodo e viene tamponata nel condensatore a valle.

---

[question:AI610]

<tip>
In tutti i circuiti con sonde RF si può generalmente assumere che la resistenza di ingresso sia $\qty{50}{\ohm}$. Non è necessario ricalcolarlo, ma si può saltare questo passaggio per le domande d'esame.
</tip>

Viceversa, dalla tensione continua misurata si può calcolare la potenza fornita al circuito. Prova a vedere se riesci a trovare la soluzione!

[question:AI611]

Oltre alle sonde RF con un solo diodo, esistono circuiti con due diodi. Il loro vantaggio consiste nel fatto che vengono acquisiti sia il picco positivo che quello negativo del segnale RF. Di conseguenza, all'uscita è disponibile una tensione di misura approssimativamente doppia rispetto a un semplice raddrizzamento di picco. Questo è particolarmente utile quando si devono acquisire piccole tensioni RF con un voltmetro per tensione continua posto a valle.

[question:AI605]
[question:AI604]

Il picco positivo e quello negativo del segnale RF vengono acquisiti separatamente e immagazzinati in condensatori. Le due tensioni si sommano all'uscita. Idealmente, la tensione di uscita corrisponde quindi alla tensione picco-picco del segnale RF:

$U_\mathrm{A} \approx U_\mathrm{SS} = 2\hat U$

Nel circuito reale devono essere considerate anche le tensioni di soglia dei due diodi. Pertanto, approssimativamente vale:

$U_\mathrm{A} \approx 2\hat U - 2U_\mathrm{F}$

Se dalla tensione di uscita misurata si vuole risalire alla tensione RF, si ottiene:

$\hat{U} \approx \frac{U_\mathrm{A}+2U_\mathrm{F}}{2}$

Dal valore di picco si può poi calcolare il valore efficace e da esso, con resistenza nota, la potenza RF.

[question:AI607]
[question:AI606]

Per indicare che un trasmettitore irradia potenza attraverso la sua antenna, può essere utilizzato un indicatore di intensità di campo. In questo caso, l'RF ricevuta viene fornita al diodo tramite un'antenna di misura e raddrizzata dal diodo. Successivamente, la tensione raddrizzata viene fornita tramite induttanze RF a un condensatore, che tampona la tensione raddrizzata. La visualizzazione avviene tramite un amperometro sensibile. Più alto è il movimento dell'indicatore dello strumento di misura, maggiore è l'intensità di campo RF misurata all'antenna. Per effettuare misurazioni esatte, sia l'antenna di misura che il misuratore di intensità di campo devono essere calibrati.

[question:AI613]
