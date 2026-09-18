Nelle trasmissioni digitali, i bit da trasmettere devono essere associati ai possibili simboli. Questa associazione viene chiamata *mappatura* (*mapping*). Il componente che esegue questa operazione è detto *mapper*. Il simbolo di un mapper è mostrato nella figura [ref:a_mapper]. Il mapper riceve un flusso di bit digitale e associa le combinazioni di bit ai simboli corrispondenti in un diagramma di costellazione.


<margin>
[picture:1102:a_mapper:Schema a blocchi di un mapper]
</margin>

---


Per comprendere il principio della mappatura, consideriamo inizialmente l'*Ampiezza-Shift Keying* (ASK) binaria, già nota dalla classe E. La figura [ref:a_ask] mostra un ASK binario nel dominio del tempo. In questo caso, l'ampiezza del segnale portante viene commutata tra due valori. Ad esempio, un'ampiezza elevata può rappresentare il bit $1$, mentre un'ampiezza ridotta il bit $0$.


<margin>
[picture:700:a_ask:ASK (Ampiezza-Shift Keying) nel dominio del tempo]
</margin>

---


I due simboli possibili possono essere rappresentati anche nel diagramma di costellazione introdotto in precedenza. Poiché in questo esempio cambia solo l'ampiezza mentre la fase rimane costante, entrambi i punti del segnale si trovano sull'asse I. La diversa distanza dall'origine corrisponde alle due ampiezze differenti. Tramite la mappatura, a ciascuno dei due punti del segnale viene ora associato un valore di bit.


<margin>
[picture:1128:a_ask_mapping:ASK (Ampiezza-Shift Keying) nel diagramma di costellazione]
</margin>

---


Un'Ampiezza-Shift Keying non è limitata a due ampiezze possibili. Se, ad esempio, vengono utilizzate quattro ampiezze diverse, sono disponibili quattro simboli diversi. Poiché con due bit si possono formare quattro combinazioni diverse, a ogni simbolo può essere associata una delle combinazioni $00$, $01$, $10$ o $11$.


La figura [ref:a_4_ask] mostra una *4-ASK* con quattro ampiezze diverse nel dominio del tempo. Ad esempio, possono essere utilizzate il $\qty{25}{\percento}$, il $\qty{50}{\percento}$, il $\qty{75}{\percento}$ e il $\qty{100}{\percento}$ dell'ampiezza massima. Ogni simbolo consente così di trasmettere due bit.


<margin>
[picture:701:a_4_ask:4-ASK (Quaternary Amplitude-Shift Keying)]
</margin>


Anche nel diagramma di costellazione sono ora presenti quattro punti del segnale possibili. Poiché in questo esempio cambia solo l'ampiezza, tutti e quattro i punti si trovano sull'asse I. A ogni punto è associata una specifica combinazione di bit.


<margin>
[picture:1129:a_4_ask_mapping:4-ASK (Quaternary Amplitude-Shift Keying) nel diagramma di costellazione]
</margin>
