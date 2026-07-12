Misurazioni importanti per il radioamatore sui trasmettitori sono le misurazioni delle potenze d’uscita sui trasmettitori o la misurazione delle tensioni HF in parti del circuito HF.

Quando si misurano le potenze d’uscita del trasmettitore, il trasmettitore deve essere terminato con un'impedenza definita che corrisponda all'impedenza di uscita del trasmettitore. Nel radioamatore, l'impedenza usuale (terminazione del trasmettitore) è di $\qty{50}{\ohm}$. La terminazione può avvenire anche direttamente nel circuito di misurazione, il che tuttavia ha senso solo con piccole potenze.

La misurazione delle tensioni HF avviene tramite una sonda HF attraverso la rettifica a diodo e la successiva livellatura della tensione continua risultante con un condensatore collegato a valle.

Nelle sonde HF con un solo diodo, la tensione di picco della tensione HF applicata, meno la tensione diretta del diodo utilizzato e di un eventuale partitore di tensione collegato a monte, è misurabile all'uscita di misurazione.

[question:AI608]

Per aumentare l'accuratezza della misurazione, in particolare con piccole potenze nell'intervallo VHF/UHF, si utilizza spesso una doppia rettifica tramite 2 diodi, in modo che entrambe le semionde della HF vengano raddrizzate (tensione di picco doppia) e, meno 2 volte la tensione diretta dei diodi utilizzati, siano disponibili come tensione di misurazione sommata all'uscita di misurazione.

[question:AI605]
[question:AI604]

Con potenze HF più elevate, è necessario collegare a monte un attenuatore adeguatamente dimensionato, che assorba gran parte della potenza d’uscita del trasmettitore da misurare. L'attenuatore deve essere considerato nel calcolo della potenza.

[question:AI609]

Per poter misurare con precisione le potenze e le tensioni HF con i circuiti sopra menzionati, questi devono essere calibrati per creare i rispettivi valori di correzione per le misurazioni.

[question:AI612]

Consideriamo ora il calcolo dei circuiti in dettaglio.
Una sonda HF con rettifica singola e livellatura successiva viene calcolata come segue:

Il segnale di ingresso HF viene terminato in modo impedente dal resistore presente (o combinazione di resistori singoli) all'ingresso. Nel circuito rappresentato, la tensione HF viene dimezzata dal partitore di tensione successivo (che è anch'esso efficace per quanto riguarda l'impedenza). Successivamente avviene la rettifica del valore di picco tramite diodo, la cui tensione di uscita si calcola come valore di picco meno la tensione diretta del diodo e viene tamponata nel condensatore collegato a valle.

Con $\qty{1}{\watt}$ di potenza d’ingresso in un sistema da $\qty{50}{\ohm}$, si ottiene una tensione d’ingresso di $\qty{7,07}{\volt}$ di tensione efficace e $\qty{10}{\volt}$ di tensione di picco.
Il partitore di tensione collegato a valle dimezza questa tensione a $\qty{5}{\volt}$ di tensione di picco, che dopo la rettifica tramite il diodo, meno la sua tensione diretta di $\qty{0,23}{\volt}$, è ancora di $\qty{4,77}{\volt}$. All'uscita del circuito vengono misurati circa $\qty{4,8}{\volt}$ arrotondati.

[question:AI610]

Viceversa, dalla tensione continua misurata si può calcolare la potenza applicata al circuito.

All'uscita del circuito vengono misurati $\qty{14,9}{\volt}$ di tensione di picco. A causa della tensione diretta del diodo, il valore di picco HF prima del diodo è di $\qty{15,6}{\volt}$. Considerando il partitore di tensione collegato a monte, ciò comporta una tensione di picco HF di $\qty{31,2}{\volt}$. Questo corrisponde a una potenza d’ingresso in un sistema da $\qty{50}{\ohm}$ di $\qty{9,73}{\watt}$ e quindi circa $\qty{9,7}{\watt}$.

[question:AI611]

Nelle sonde HF e nei misuratori di potenza con doppia rettifica di picco (2 diodi), il calcolo avviene come per la rettifica singola, ma è necessario considerare la tensione di picco doppia all'uscita e il doppio calo di tensione dovuto a 2 diodi.

[question:AI607]
[question:AI606]

Per indicare che un trasmettitore irradia potenza attraverso la sua antenna, si può utilizzare un indicatore di intensità di campo. In questo caso, la HF ricevuta viene fornita a un diodo tramite un'antenna di misurazione e raddrizzata dal diodo. Successivamente, la tensione raddrizzata viene fornita tramite induttanze HF a un condensatore che livella la tensione raddrizzata. L'indicazione avviene tramite un sensibile misuratore di corrente. Quanto maggiore è la deviazione dell'ago dello strumento di misurazione, tanto maggiore è l'intensità di campo HF misurata all'antenna. Per poter effettuare misurazioni precise, sia l'antenna di misurazione che il misuratore di campo devono essere calibrati.

[question:AI613]