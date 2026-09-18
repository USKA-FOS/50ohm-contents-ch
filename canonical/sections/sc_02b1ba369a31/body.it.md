Le misure importanti per il radioamatore sui trasmettitori riguardano le misurazioni delle potenze di uscita dei trasmettitori o la misurazione delle tensioni HF in parti di circuiti HF. Quando si misura la potenza di uscita del trasmettitore, il trasmettitore deve essere chiuso su un’impedenza definita, che corrisponda all’impedenza di uscita del trasmettitore. Nel radioamatoriale, l’impedenza usuale (chiusura del trasmettitore) è di $\qty{50}{\ohm}$. La chiusura può essere realizzata anche direttamente nel circuito di misura, il che è tuttavia sensato solo per potenze ridotte.

La misurazione delle tensioni HF avviene tramite una sonda HF mediante raddrizzamento a diodo e successiva livellazione della tensione continua generata con un condensatore collegato a valle. La figura [ref:hf_messkopf_0] mostra il principio di una sonda HF con raddrizzamento semplice e livellazione della tensione continua. La tensione HF viene chiusa su un’impedenza corretta tramite una resistenza (o una combinazione di resistenze) all’ingresso. Successivamente avviene il raddrizzamento tramite diodo, la cui tensione di uscita si calcola come valore di picco meno la tensione diretta del diodo e viene immagazzinata nel condensatore collegato a valle. La figura [ref:hf_messkopf_1] mostra una sonda HF autocostruita, mentre la figura [ref:hf_messkopf_2] ne presenta lo schema elettrico.

<margin>
[picture:576:hf_messkopf_0:Principio di una sonda HF con raddrizzamento semplice e livellazione della tensione continua]
[photo:338:hf_messkopf_1:Sonda HF autocostruita di DL3JOP]
[photo:339:hf_messkopf_2:Schema elettrico della sonda HF di DL3JOP]
</margin>

[question:AI608]

Per potenze HF più elevate, è necessario collegare a monte un attenuatore adeguatamente dimensionato, che assorba gran parte della potenza di uscita del trasmettitore da misurare. L’attenuatore deve essere considerato nel calcolo della potenza.

[question:AI609]

---

Per ottenere una misurazione il più possibile precisa di tensioni e potenze HF, il circuito di misura utilizzato deve essere prima calibrato. A tal fine, vengono iniettati segnali di riferimento noti e vengono determinate le deviazioni tra il valore reale e quello misurato. Da queste deviazioni è possibile ricavare valori di correzione dipendenti da frequenza e livello, che possono essere memorizzati, ad esempio, in una tabella come quella in [ref:a_frequenzgang_messwerte].

Durante una successiva misurazione, il valore misurato viene corretto con il corrispondente valore di correzione. Se i valori di misura sono espressi in $\unit{\dBm}$, ad esempio, la deviazione determinata durante la calibrazione per la frequenza corrispondente può essere aggiunta come valore di correzione in $\unit{\dB}$ al valore misurato.

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
[table:a_frequenzgang_messwerte:Livelli misurati in funzione della frequenza per la sonda HF di DL3JOP]
</margin>

[question:AI612]

Analizziamo ora nel dettaglio il calcolo dei circuiti. Nei puntali HF con un solo diodo, all’uscita della misura è possibile rilevare la tensione di picco del segnale HF applicato meno la tensione diretta del diodo utilizzato e, se presente, di un partitore di tensione collegato a monte. Un puntale HF con raddrizzamento semplice e successiva livellazione viene calcolato come segue:

Il segnale di ingresso HF viene chiuso su un’impedenza corretta tramite la resistenza (o combinazione di resistenze) presente all’ingresso. Nel circuito rappresentato (cfr. figura [ref:hf_messkopf_0]), la tensione HF viene dimezzata dal partitore di tensione successivo (che agisce anche sull’impedenza). Successivamente avviene il raddrizzamento del valore di picco tramite diodo, la cui tensione di uscita si calcola come valore di picco meno la tensione diretta del diodo e viene immagazzinata nel condensatore collegato a valle.

---

[question:AI610]

<tip>
In tutti i circuiti con puntali HF si può assumere in modo generalizzato che la resistenza di ingresso sia $\qty{50}{\ohm}$. Non è necessario rifare il calcolo, ma questo passaggio può essere saltato per le domande d’esame.
</tip>

Viceversa, dalla tensione continua misurata è possibile calcolare la potenza fornita al circuito. Prova a trovare tu stesso la soluzione!

[question:AI611]

Oltre ai puntali HF con un solo diodo, esistono circuiti con due diodi. Il loro vantaggio consiste nel fatto che sia la semionda positiva che quella negativa del segnale HF vengono rilevate. Di conseguenza, all’uscita è disponibile una tensione di misura circa doppia rispetto a quella ottenuta con un semplice raddrizzamento del valore di picco. Questo è particolarmente utile quando si devono rilevare piccole tensioni HF con un amperometro in corrente continua collegato a valle.

[question:AI605]
[question:AI604]

La semionda positiva e quella negativa del segnale HF vengono rilevate separatamente e immagazzinate nei condensatori. Le due tensioni si sommano all’uscita. Idealmente, la tensione di uscita corrisponde quindi alla tensione picco-picco del segnale HF:

$U_\mathrm{A} \approx U_\mathrm{SS} = 2\hat U$

Nei circuiti reali, tuttavia, devono essere considerate anche le tensioni dirette dei due diodi. In prima approssimazione vale quindi:

$U_\mathrm{A} \approx 2\hat U - 2U_\mathrm{F}$

Se si vuole risalire dalla tensione di uscita misurata alla tensione HF, si ottiene:

$\hat{U} \approx \frac{U_\mathrm{A}+2U_\mathrm{F}}{2}$

Dal valore di picco è quindi possibile calcolare il valore efficace e, con una resistenza nota, la potenza HF.

[question:AI607]
[question:AI606]

Per indicare che un trasmettitore irradia potenza tramite la sua antenna, può essere utilizzato un misuratore di intensità di campo. In questo caso, tramite un’antenna di misura, la HF ricevuta viene inviata al diodo e raddrizzata. Successivamente, la tensione raddrizzata viene inviata tramite induttanze HF a un condensatore, che immagazzina la tensione raddrizzata. La visualizzazione avviene tramite un amperometro sensibile. Maggiore è la deviazione dell’indice dello strumento, maggiore è l’intensità di campo HF misurata all’antenna. Per poter effettuare misurazioni precise, sia l’antenna di misura che il misuratore di intensità di campo devono essere calibrati.

[question:AI613]