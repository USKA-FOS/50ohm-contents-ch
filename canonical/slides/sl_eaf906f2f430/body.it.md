## Modulazione a spostamento di fase (PSK)

* Metodo di modulazione digitale per la trasmissione dati
* I simboli vengono rappresentati da diverse posizioni di fase di una portante
* In una PSK ideale, l'ampiezza e la frequenza della portante rimangono invariate
* Al passaggio da un simbolo all'altro, la posizione di fase può cambiare

---

## PSK nella rappresentazione temporale

<left>
[picture:705:a_psk:Modulazione a spostamento di fase (Phase-Shift Keying)]
</left>
<right>
* L'ampiezza rimane costante
* Le informazioni sono codificate nella *posizione di fase*
* Al passaggio tra due simboli, la fase può cambiare bruscamente
* Se viene trasmesso nuovamente lo stesso simbolo, anche la posizione di fase rimane invariata
</right>

---

## Modulazione a spostamento di fase binaria (BPSK)

<left>
[picture:1101:a_psk_mapping:BPSK nel diagramma di costellazione]
</left>
<right>
* Due diverse posizioni di fase
* Due possibili simboli
* Consente di trasmettere $\num{1}$ bit per simbolo
* Esempio: $\qty{0}{\degree}$ → $0$ e $\qty{180}{\degree}$ → $1$
* I due punti del segnale si trovano opposti nel diagramma di costellazione
</right>

<note>
La forma più semplice di modulazione a spostamento di fase è la BPSK. I due possibili simboli hanno la stessa ampiezza, ma le loro fasi differiscono di 180 gradi.

Nota aggiuntiva: matematicamente, la BPSK può essere generata moltiplicando la portante per +1 o -1 a seconda del valore del bit. La moltiplicazione per -1 corrisponde a uno spostamento di fase di 180 gradi:

$-\sin(\omega t)=\sin(\omega t+\qty{180}{\degree})$

La scelta di 0 gradi e 180 gradi non è obbligatoria. Ad esempio, sarebbero possibili anche 90 gradi e 270 gradi.
</note>

---

[question:AE401]

---

## Più posizioni di fase – più simboli

* Con più posizioni di fase è possibile rappresentare più simboli diversi
* In questo modo, più bit possono essere raggruppati in un singolo simbolo

<fragment>
* *BPSK*: $\num{2}$ simboli → $\num{1}$ bit per simbolo
* *QPSK*: $\num{4}$ simboli → $\num{2}$ bit per simbolo
* *8-PSK*: $\num{8}$ simboli → $\num{3}$ bit per simbolo
</fragment>

---

[question:AE402]

---

## Modulazione a spostamento di fase in quadratura (QPSK)

* La QPSK utilizza quattro diverse posizioni di fase
* In questo modo sono disponibili quattro simboli diversi
* Due bit vengono raggruppati in un simbolo: $00$, $01$, $10$, $11$
* Ogni simbolo QPSK trasmette quindi $\num{2}$ bit

---

## QPSK nel diagramma di costellazione

<left>
[picture:1059:a_qpsk:Diagramma I/Q per una mappatura QPSK]
</left>
<right>
In questo esempio vale:

* $11$ → $\qty{45}{\degree}$
* $01$ → $\qty{135}{\degree}$
* $00$ → $\qty{225}{\degree}$
* $10$ → $\qty{315}{\degree}$

<fragment>
* Tutti i punti del segnale hanno la stessa ampiezza
* Le posizioni di fase sono sfalsate tra loro di $\qty{90}{\degree}$
* I quattro punti si trovano su una circonferenza
</fragment>
</right>

<note>
L'assegnazione delle combinazioni di bit alle singole posizioni di fase non è generalmente fissa. Tuttavia, trasmettitore e ricevitore devono utilizzare la stessa mappatura.

La mappatura utilizzata qui corrisponde anche alla rappresentazione nel testo didattico e nell'applet successivo.
</note>

---

## Codice di Gray nella QPSK

<left>
[picture:1059:a_qpsk_gray:Diagramma I/Q per una mappatura QPSK]
</left>
<right>
* I simboli adiacenti differiscono tra loro solo per *un bit*
* Un'assegnazione di questo tipo viene chiamata *codice di Gray*

<fragment>
Esempio:

$11 \leftrightarrow 01 \leftrightarrow 00 \leftrightarrow 10$
</fragment>

<fragment>
Se il rumore causa erroneamente il riconoscimento di un simbolo adiacente, ciò comporta spesso un singolo errore di bit.
</fragment>
</right>

<note>
La mappatura è stata scelta in modo che i punti adiacenti nel diagramma di costellazione differiscano solo per un bit.

Ad esempio, nel passaggio da 11 a 01 cambia solo il primo bit. Lo stesso vale per gli altri punti del segnale adiacenti, incluso 10 e 11.
</note>

---

<left>
[include:applet_qpsk]
</left>

<right>
### QPSK in presenza di rumore
* Il rumore altera ampiezza e fase del segnale ricevuto
* I valori ricevuti si disperdono intorno ai simboli QPSK ideali
* Il ricevitore decide per il simbolo più vicino
* Se viene superata una soglia di decisione, si verifica un errore di simbolo
</right>

<note>
L'applet mostra non solo i simboli QPSK ideali, ma anche la situazione al ricevitore.

Le croci contrassegnano i quattro punti ideali del segnale. I piccoli punti colorati rappresentano i valori ricevuti disturbati dal rumore. A causa del rumore e di altre interferenze, sia l'ampiezza che la fase del segnale ricevuto cambiano.

Le aree colorate sono le aree di decisione del ricevitore. Il ricevitore assegna un valore ricevuto al simbolo ideale più vicino.

Finché un punto disturbato si trova nell'area di decisione del simbolo originariamente trasmesso, il simbolo viene riconosciuto correttamente. Se il punto supera una soglia di decisione a causa di un rumore elevato, viene invece riconosciuto un altro simbolo.

Con "Trasmetti di nuovo", la stessa sequenza di bit viene trasmessa nuovamente con nuovo rumore. In questo modo è possibile osservare chiaramente che, nonostante i simboli trasmessi siano gli stessi, ogni volta si ottengono valori ricevuti diversi.

Con l'aumentare del rumore, aumenta la probabilità di errori di simbolo e quindi di bit. Attraverso una codifica di canale appropriata, molti di questi errori possono essere rilevati e corretti.
</note>

---

## ASK e PSK nel diagramma di costellazione

* Nell'*ASK* i simboli differiscono principalmente per la loro ampiezza
  * distanza diversa dall'origine
  * stessa posizione di fase
* Nella *PSK* i simboli differiscono per la loro posizione di fase
  * stessa distanza dall'origine
  * angolo diverso
* Nella PSK, quindi, i punti del segnale si trovano su una circonferenza poiché hanno la stessa ampiezza.