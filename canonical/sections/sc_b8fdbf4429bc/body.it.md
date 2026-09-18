Anche nel radioamatoriale vengono utilizzati molti metodi di trasmissione digitale. Ne abbiamo già discussi uno molto semplice. Con la telegrafia Morse in Onda Continua (CW), una portante viene accesa e spenta a intervalli regolari. Ci sono quindi solo due livelli, $\qty{0}{\percent}$ e $\qty{100}{\percent}$ dell’ampiezza massima. La trasmissione avviene quindi in modo digitale.

La telegrafia Morse è il metodo di trasmissione più antico utilizzato nella radio. I primi trasmettitori radio non conoscevano altri metodi. L’unico modo per trasmettere informazioni era accendere e spegnere brevemente il trasmettitore con un tasto. All’ascolto, il ricevitore percepisce un tono che si accende e si spegne secondo un ritmo preciso.

Per trasmettere caratteri diversi, cioè lettere, cifre e segni di punteggiatura, si utilizza il codice Morse. Ogni carattere è rappresentato da una specifica sequenza di toni brevi e lunghi. Nelle tabelle [ref:n_morsetelegrafie_morsecode_buchstaben], [ref:n_morsetelegrafie_morsecode_ziffern_satzzeichen] e [ref:n_morsetelegrafie_morsecode_spezial] è riportata una parte del codice Morse. Un punto ([morse:e]) (pronunciato: "dit") corrisponde a un tono breve e una lineetta ([morse:t]) (pronunciata: "dah") a un tono lungo. La decodifica, cioè la traduzione dei toni in caratteri al ricevitore, avviene con le orecchie e il cervello – o, ai giorni nostri, anche con il computer.

**Il Morse è una manipolazione temporale di una portante. Le informazioni non derivano solo dai punti e dalle lineette, ma anche dalle pause esattamente definite.**

I rapporti temporali tra punto, lineetta e pause sono definiti come segue:

* Punto = 1 unità di tempo
* Lineetta = 3 unità di tempo
* Pausa tra gli elementi di un carattere = 1 unità di tempo
* Pausa tra due caratteri = 3 unità di tempo
* Pausa tra parole = 7 unità di tempo

La "velocità" viene espressa in parole al minuto [WPM] (Words Per Minute), dove il riferimento internazionale usuale è la parola PARIS.

<webmargin>
| c: | l: | c: | l: | c: | l: |
|  |  |  |  |  |  |
| A | [morse:a] | K | [morse:k] | U | [morse:u] |
| B | [morse:b] | L | [morse:l] | V | [morse:v] |
| C | [morse:c] | M | [morse:m] | W | [morse:w] |
| D | [morse:d] | N | [morse:n] | X | [morse:x] |
| E | [morse:e] | O | [morse:o] | Y | [morse:y] |
| F | [morse:f] | P | [morse:p] | Z | [morse:z] |
| G | [morse:g] | Q | [morse:q] | Ä | [morse:ä] |
| H | [morse:h] | R | [morse:r] | Ö | [morse:ö] |
| I | [morse:i] | S | [morse:s] | Ü | [morse:ü] |
| J | [morse:j] | T | [morse:t] |  |  |
[table:n_morsetelegrafie_morsecode_buchstaben:Codice Morse (lettere)]
</webmargin>

<webmargin>
| c: | l: | c: | l: | c: | l: |
|  |  |  |  |  |  | 
| 0 | [morse:0] | 5 | [morse:5] | / | [morse:/] |
| 1 | [morse:1] | 6 | [morse:6] | . | [morse:.] |
| 2 | [morse:2] | 7 | [morse:7] | , | [morse:,] |
| 3 | [morse:3] | 8 | [morse:8] | ? | [morse:?] |
| 4 | [morse:4] | 9 | [morse:9] | - | [morse:-] |
|  |  |  |  | @ | [morse:@] |
[table:n_morsetelegrafie_morsecode_ziffern_satzzeichen:Codice Morse (cifre e segni di punteggiatura)]
</webmargin>

% TODO ARK: Le prosigns bk, sk e irrung non funzionano ancora senza lo spazio intermedio. Il programma morse.py nel generatore deve essere sostituito con il programma morse.py indicato nell'issue xxx.

<webmargin>
| l: | l: |
|  |  |
| Interruzione (BK) | [morse:bk] |
| Separazione all’interno di un passaggio (BT,=) | [morse:=] |
| Fine del passaggio (AR)  | [morse:ar] |
| Fine della trasmissione (SK) | [morse:sk] |
| Errore, correzione | [morse:correction] |
[table:n_morsetelegrafie_morsecode_spezial:Codice Morse (caratteri speciali, selezione)]
</webmargin>

Per molto tempo, in tutto il mondo era obbligatorio che ogni radioamatore superasse un esame di Morse prima di poter trasmettere in onde corte. Dagli anni ’90, ogni paese può decidere autonomamente se richiedere un esame di Morse. Nella maggior parte dei paesi, inclusa la Svizzera, non è più richiesto alcun esame di Morse. Nonostante siano stati sviluppati metodi di trasmissione per la voce, le immagini e persino i video, la telegrafia Morse viene ancora praticata nel radioamatoriale. Ha un fascino particolare comunicare in tutto il mondo con mezzi estremamente semplici.

[question:VA304]

Nell’utilizzo operativo della telegrafia Morse, occorre tenere presente una particolarità: la scelta di una velocità adeguata. I segnali Morse possono essere trasmessi a velocità diverse. Tuttavia, è necessario molto esercizio per riuscire a ricevere anche segnali Morse trasmessi rapidamente. Pertanto, è importante non sovraccaricare la stazione corrispondente con una velocità troppo elevata. Una buona regola pratica è non trasmettere più velocemente della stazione con cui si comunica e non più velocemente di quanto si riesca a ricevere personalmente. In questo modo, tutti riescono a seguire la conversazione.

<indepth>
Non è un caso che le lettere più frequenti (n, t, i, ...) abbiano assegnati segnali Morse brevi e quelle meno frequenti (x, y, ...) segnali lunghi. Questo consente di risparmiare tempo nella trasmissione di un messaggio. Si parla anche di compressione dati alla sorgente.
</indepth>

[question:BE117]
[question:BE118]
