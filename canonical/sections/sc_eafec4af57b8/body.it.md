Nella [modulazione a spostamento di fase](#) (Phase-Shift Keying, PSK), i diversi simboli vengono rappresentati da diverse posizioni di fase di un segnale portante. L’[ampiezza](#) e la [frequenza](#) del portante rimangono invariate. Al passaggio da un simbolo a un altro, invece, può cambiare la posizione di fase.

La figura [ref:a_psk](#) mostra un segnale PSK nel dominio del tempo. Nei punti di transizione dei simboli si nota che l’[oscillazione](#) prosegue con una posizione di fase diversa.


<margin>
[picture:705:a_psk:Modulazione a spostamento di fase (Phase-Shift Keying)]
</margin>

---

La forma più semplice è la modulazione binaria a spostamento di fase (Binary Phase-Shift Keying, BPSK). In questo caso sono disponibili due posizioni di fase diverse e quindi due simboli possibili. Ad esempio, possono essere utilizzate le posizioni di fase $\qty{0}{\degree}$ e $\qty{180}{\degree}$ e associate ai valori di [bit](#) $0$ e $1$. La figura [ref:a_psk_mapping](#) mostra una possibile mappatura dei due valori di bit sui due simboli BPSK.


Poiché i due simboli differiscono solo per la loro posizione di fase e la loro ampiezza è uguale, i due punti nel diagramma di costellazione si trovano opposti su una circonferenza.


<margin>
[picture:1101:a_psk_mapping:BPSK nel diagramma di costellazione]
</margin>


<indepth>
Pignoleria: In realtà, la BPSK con gli angoli $\qty{0}{\degree}$ e $\qty{180}{\degree}$ può essere considerata anche come un metodo ASK in cui l’ampiezza del segnale portante viene commutata tra un valore negativo e uno positivo. Moltiplicare per $-1$ un segnale sinusoidale comporta uno spostamento di fase di $\qty{180}{\degree}$:


$-\sin(\omega t)=\sin(\omega t+\qty{180}{\degree})$


Questo è un caso speciale. Sarebbero possibili anche altri angoli di fase, ad esempio $\qty{90}{\degree}$ e $\qty{270}{\degree}$, le cui fasi dei simboli differirebbero anch’esse di $\qty{180}{\degree}$.
</indepth>

[question:AE401]


---

Utilizzando più posizioni di fase diverse, è possibile rappresentare un numero maggiore di simboli. In questo modo, diversi [bit](#) possono essere raggruppati in un singolo simbolo.


---

Nella modulazione quadrifase (Quadrature Phase-Shift Keying, QPSK), sono disponibili quattro posizioni di fase diverse e quindi quattro simboli possibili. Poiché esistono quattro combinazioni di bit possibili con due [bit](#), con ogni simbolo possono essere trasmessi due [bit](#).


Per confronto:

* BPSK: $\num{2}$ simboli → $\num{1}$ [bit](#) per simbolo
* QPSK: $\num{4}$ simboli → $\num{2}$ [bit](#) per simbolo
* 8-PSK: $\num{8}$ simboli → $\num{3}$ [bit](#) per simbolo

[question:AE402]


Analizziamo ora la QPSK nel diagramma di costellazione. I quattro simboli possibili hanno la stessa ampiezza, ma differiscono per la loro posizione di fase. Pertanto, tutti e quattro i punti del segnale si trovano su una circonferenza. La figura [ref:a_qpsk](#) mostra una possibile mappatura delle quattro combinazioni di bit $00$, $01$, $10$ e $11$ sui quattro simboli QPSK.


<margin>
[picture:1059:a_qpsk:Diagramma I/Q per una mappatura QPSK]
</margin>

---

In questo esempio vengono utilizzate le seguenti posizioni di fase:


* $11$ corrisponde a $\qty{45}{\degree}$
* $01$ corrisponde a $\qty{135}{\degree}$
* $00$ corrisponde a $\qty{225}{\degree}$
* $10$ corrisponde a $\qty{315}{\degree}$


<margin>
Il seguente applet illustra la modulazione digitale QPSK. In un sistema reale, il segnale è influenzato da rumore e altre interferenze. Pertanto, i punti del segnale ricevuto non si trovano esattamente nelle posizioni ideali, ma si discostano sia in ampiezza che in fase. L’applet simula questo effetto aggiungendo rumore. Le croci rappresentano i quattro simboli QPSK ideali. Ogni punto colorato è un valore ricevuto rumoroso. Il ricevitore lo associa al simbolo più vicino. Le aree colorate rappresentano le regioni decisionali del ricevitore. Finché un valore ricevuto rumoroso si trova nell’area del simbolo originariamente trasmesso, viene riconosciuto correttamente. Se un punto, a causa di un rumore elevato, supera un confine verso una regione adiacente, il ricevitore decide per il simbolo sbagliato. Tuttavia, questi errori possono essere corretti tramite la codifica di canale, un argomento che tratteremo in una sezione successiva.

[include:applet_qpsk]
</margin>

Le quattro posizioni di fase sono sfasate tra loro di $\qty{90}{\degree}$. Il ricevitore può determinare quale simbolo e quindi quale combinazione di bit è stata trasmessa in base alla posizione di fase rilevata.

L’assegnazione delle combinazioni di bit alle singole posizioni di fase non è univocamente definita. È fondamentale che a ogni simbolo venga assegnata una combinazione di bit univoca.


In pratica, la mappatura viene spesso scelta in modo che le combinazioni di bit dei punti di segnale adiacenti differiscano solo per un [bit](#). Tale assegnazione viene chiamata *codice di Gray*. Se a causa di rumore viene erroneamente riconosciuto un punto di segnale adiacente, ciò comporta spesso un singolo errore di [bit](#).


Il diagramma di costellazione evidenzia quindi una differenza fondamentale tra ASK e PSK: nell’ASK i simboli differiscono per la loro distanza dall’origine e si trovano generalmente solo sull’asse positivo I, mentre nella PSK differiscono per l’angolo. Nella PSK, quindi, i punti del segnale si trovano su una circonferenza se l’ampiezza è uguale.