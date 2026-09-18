Spesso ci troviamo di fronte al problema che un valore di resistenza desiderato non è incluso nella cosiddetta "serie normalizzata delle resistenze". Potrebbe anche essere che una resistenza debba dissipare una grande potenza, che non è possibile con resistenze singole disponibili in commercio – per citare solo due esempi. Ora vedremo come ottenere altri valori di resistenza collegando resistenze in serie o in parallelo.

Dalla legge di Ohm possiamo derivare le regole per i collegamenti in serie e in parallelo delle resistenze:

$U=R \cdot I$

<margin>
[picture:819:e_spannungsteiler:Partitore di tensione]
</margin>

La figura [ref:e_spannungsteiler] mostra due resistenze $R_1$ e $R_2$ collegate in serie. Entrambe sono attraversate dalla stessa corrente *I*. Ai capi delle resistenze si generano le tensioni

$U_1 = R_1 \cdot I$ e  $U_2 = R_2 \cdot I$. 
La tensione totale $U_g$ è semplicemente la somma di queste due tensioni:

$U_g = U_1 + U_2 = R_{\mathrm{ges}} \cdot {I} = R_1 \cdot I + R_2 \cdot I$

Ora possiamo calcolare la resistenza che si osserva tra i morsetti esterni:
$R_{\mathrm{ges}} = \frac{U_g}{I} = R_1 + R_2$, poiché la corrente $I$ si semplifica in entrambi i membri dell'equazione.

Questo vale anche per più di due resistenze, come mostrato nella raccolta di formule:

$R_{\mathrm{ges}} = R_1 + R_2 + R_3 + R_4 + \dots$

---

Ma come si comportano due resistenze $R_1$ e $R_2$ collegate in parallelo, come mostrato nella figura [ref:e_parallelschaltung]?

Ora, ai capi di entrambe le resistenze è presente la stessa tensione $U$, che fa circolare le correnti

$I_1 = \frac{U}{R_1}$ e $I_2 = \frac{U}{R_2}$

<margin>
[picture:945:e_parallelschaltung:In questo circuito sono visibili tutte le tensioni e le correnti.]
</margin>

La corrente che circola nel circuito esterno è la somma di queste due correnti:

$I = I_1 + I_2 = \frac{U}{R_1} + \frac{U}{R_2}$

Cerchiamo nuovamente una resistenza totale $R_{\mathrm{ges}}$, per la quale deve valere: $I=\frac{U}{R_{\mathrm{ges}}}$ e di conseguenza:

$\dfrac{1}{R_{\mathrm{ges}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$

---

Il reciproco della resistenza totale è quindi la somma dei reciproci delle singole resistenze. Una conseguenza è che, collegando in parallelo una serie di resistenze uguali, si ottiene semplicemente il valore della singola resistenza diviso per il numero di resistenze.

Anche in questo caso possiamo calcolare la resistenza totale per un numero arbitrario di resistenze in parallelo (cfr. raccolta di formule):

$\dfrac{1}{R_{\mathrm{ges}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dfrac{1}{R_3} + \dfrac{1}{R_4} + \dots$

L'espressione per due resistenze in parallelo può essere riscritta, secondo le regole del calcolo frazionario, come:

$R_{\mathrm{ges}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$

<tip>
Nel collegamento in serie il valore della resistenza totale è sempre maggiore della resistenza singola più grande. Nel collegamento in parallelo, invece, la resistenza totale è sempre minore della resistenza singola più piccola.
</tip>

---

[question:ED104]
[question:ED105]
[question:ED106]

<tip>
Fare attenzione che le resistenze utilizzate nei calcoli abbiano sempre la stessa unità di misura. Consigliamo sempre di lavorare con l'unità fondamentale ($\unit{\ohm}$). Se colleghiamo in serie una resistenza da $\qty{1}{\kilo\ohm}$ e una da $\qty{10}{\ohm}$, allora calcoliamo $\qty{1000}{\ohm} + \qty{10}{\ohm} = \qty{1010}{\ohm}$.
</tip>

---

Alcuni esercizi includono reti di resistenze in cui sono presenti sia collegamenti in serie che in parallelo. In questi casi procediamo convertendo prima, ad esempio, il collegamento in parallelo in una resistenza equivalente, che poi combiniamo con la terza resistenza collegata in serie. Oppure viceversa, a seconda di ciò che risulta più opportuno in base allo schema del circuito.

<tip>
[picture:305:e_tipp_aufgabe:Esempio di circuito]

Un importante metodo di soluzione è la "tecnica dell'osservazione attenta" ... ad esempio, esiste un circuito che ha una resistenza $R_1$ in serie con due resistenze $R_2$ e $R_3$ collegate in parallelo. I valori sono $R_1 = \qty{1}{\kilo\ohm}$, $R_2 = \qty{2000}{\ohm}$ e $R_3 = \qty{2}{\kilo\ohm}$. Tuttavia, $\qty{2}{\kilo\ohm} = \qty{2000}{\ohm}$. Il collegamento in parallelo di $R_2$ e $R_3$ dà una resistenza pari alla metà: $\qty{1000}{\ohm} = \qty{1}{\kilo\ohm}$. La colleghiamo in serie con $R_1$ e otteniamo il risultato: $R_{\mathrm{ges}} = \qty{2}{\kilo\ohm}$.
</tip>

[question:ED111]
[question:ED110]
[question:ED112]
[question:ED113]
[question:ED108]
[question:ED109]

Per le considerazioni sulla potenza è meglio partire dalla nota espressione della potenza:

$P = U \cdot I$

Nel collegamento in serie di, ad esempio, tre resistenze uguali, la stessa corrente attraversa tutte le resistenze, ma ai capi di ogni singola resistenza cade solo un terzo della tensione esterna. Nel collegamento in parallelo, invece, la stessa tensione è presente ai capi di tutte le resistenze, ma la corrente si divide su tre percorsi. In entrambi i casi, il circuito sopporta quindi una potenza tripla rispetto a quella della singola resistenza.

[question:ED107]
