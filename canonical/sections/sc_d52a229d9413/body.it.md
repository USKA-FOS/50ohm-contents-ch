Nei metodi di trasmissione digitale, i bit da trasmettere devono essere assegnati ai vari simboli possibili. Questa assegnazione è chiamata *mapping*. Il blocco funzionale che esegue questa assegnazione è chiamato *mapper*. Il simbolo a blocchi di un mapper è mostrato nella figura [ref:a_mapper]. Il mapper riceve un flusso di bit digitale e assegna le combinazioni di bit contenute ai corrispondenti simboli in un diagramma di costellazione.

<margin>
[picture:1102:a_mapper:Schema a blocchi di un mapper]
</margin>

---

Per conoscere il principio del mapping, consideriamo prima la *modulazione a spostamento di ampiezza* (*Amplitude-Shift Keying*, ASK), già nota dalla sezione [sec:ask_fsk_afsk]. La figura [ref:a_ask] mostra un ASK binario nella rappresentazione temporale. Qui l'ampiezza del segnale portante viene commutata tra due valori. Ad esempio, un'ampiezza grande può rappresentare il bit $1$ e un'ampiezza piccola il bit $0$.

<margin>
[picture:700:a_ask:ASK (Amplitude-Shift Keying) nell'andamento temporale]
</margin>

---

I due simboli possibili possono anche essere rappresentati nel diagramma di costellazione precedentemente appreso. Poiché in questo esempio cambia solo l'ampiezza e la fase rimane la stessa, entrambi i punti del segnale si trovano sull'asse I. La diversa distanza dall'origine corrisponde alle due diverse ampiezze. A ciascuno dei due punti del segnale viene ora assegnato un valore di bit tramite il mapping.

<margin>
[picture:1128:a_ask_mapping:ASK (Amplitude-Shift Keying) nel diagramma di costellazione]
</margin>

---

Una *modulazione a spostamento di ampiezza* non è limitata a due ampiezze possibili. Se, ad esempio, vengono utilizzate quattro diverse ampiezze, sono disponibili quattro simboli diversi. Poiché con due bit si possono formare quattro diverse combinazioni di bit, a ciascun simbolo può essere assegnata una delle combinazioni $00$, $01$, $10$ o $11$.

La figura [ref:a_4_ask] mostra una tale *4-ASK* con quattro diverse ampiezze nella rappresentazione temporale. Ad esempio, possono essere utilizzati $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$ e $\qty{100}{\percent}$ dell'ampiezza massima. Con ogni simbolo possono quindi essere trasmessi due bit.

<margin>
[picture:701:a_4_ask:Modulazione a spostamento di ampiezza quaternaria (Quaternary Amplitude-Shift Keying)]
</margin>

Anche nel diagramma di costellazione ci sono ora quattro possibili punti del segnale. Poiché cambia ancora solo l'ampiezza, in questo esempio tutti e quattro i punti giacciono sull'asse I. A ciascun punto è assegnata una specifica combinazione di bit.

<margin>
[picture:1129:a_4_ask_mapping:Modulazione a spostamento di ampiezza quaternaria (Quaternary Amplitude-Shift Keying) nel diagramma di costellazione]
</margin>
