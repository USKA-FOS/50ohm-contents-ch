Il fenomeno fisico che rende possibile i segnali radio è il campo elettromagnetico. La scoperta che questo campo possa propagarsi nel vuoto, senza un mezzo di supporto, fu una delle più significative del XIX secolo.

<margin>
Per lungo tempo la fisica ha creduto nell’esistenza di un "etere", presente ovunque e nel quale le onde elettromagnetiche si propagano come il suono nell’aria. Questa concezione era errata, ma il termine è rimasto nell’uso comune, ad esempio diciamo che siamo seduti al ricevitore e *ascoltiamo nell’etere*.
</margin>

---

Come suggerisce il nome stesso, il campo elettromagnetico è composto da due componenti: il campo elettrico e il campo magnetico. Se il campo elettrico e quello magnetico variano nel tempo, le due componenti del campo si presentano sempre insieme.

Iniziamo però con il campo elettrico statico, cioè non variabile nel tempo. Il campo elettrico viene generalmente indicato con la lettera $E$.

<margin>
[immagine:881:e_plattenkondensator: Un condensatore a piastre con tensione applicata e campo elettrico omogeneo]
</margin>

---

La figura [rif:e_plattenkondensator] mostra schematicamente un *condensatore a piastre* al quale è applicata una tensione $U$. Le piastre sono isolate tra loro e non circola corrente. La tensione provoca l’accumulo di cariche positive sulla piastra sinistra e negative su quella destra. Tra le due piastre si forma un campo elettrico statico $E$. Se supponiamo che l’estensione delle piastre in lunghezza e larghezza sia molto maggiore della distanza tra loro, l’intensità del campo è indipendente dalla posizione: parliamo quindi di un campo *omogeneo*. L’intensità del campo elettrico può essere calcolata semplicemente con la formula:

$E = \frac{U}{d}$

dove $d$ è la distanza tra le piastre.

<unit>
Dall’equazione $E = \frac{U}{d}$ deriva anche l’unità di misura dell’intensità del campo elettrico: $\unit{\volt\per\metro}$
</unit>

[domanda:EB101]
[domanda:EA103]

---

Per calcolare l’intensità del campo elettrico in un condensatore a piastre, dobbiamo conoscere la tensione applicata e la distanza tra le piastre. I condensatori a piastre sono spesso utilizzati nei dispositivi di adattamento delle antenne.

<danger>
In questi esercizi è fondamentale prestare attenzione all’unità di misura corretta!
</danger>

[domanda:EB102]

Qui possiamo semplicemente applicare la formula vista in precedenza:

$E = \frac{\qty{9}{\volt}}{\qty{0,6}{\centi\metro}} = \frac{\qty{9}{\volt}}{\qty{0,006}{\metro}} = \qty{1500}{\volt\per\metro}$

Un *condensatore avvolto* può essere immaginato come un condensatore a piastre con piastre molto larghe, arrotolate tra loro. Tra le piastre si trova però uno strato isolante, il *materiale dielettrico*. Esso aumenta la *capacità* del condensatore, cioè la sua capacità di immagazzinare cariche. Tuttavia, il materiale dielettrico non influisce sul calcolo dell’intensità del campo al suo interno.

[domanda:EB103]

Anche per questo esercizio utilizziamo la nostra formula:

$E = \frac{\qty{300}{\volt}}{\qty{0,15}{\milli\metro}} = \frac{\qty{300}{\volt}}{\qty{0,00015}{\metro}} = \qty{2000000}{\volt\per\metro} = \qty{2000}{\kilo\volt\per\metro}$

I materiali dielettrici possono sopportare solo un’intensità di campo elettrico limitata prima di perdere la loro capacità isolante. Il valore limite di intensità di campo al quale ciò avviene è detto *intensità di rottura*. Se conosciamo l’intensità di rottura e lo spessore del materiale dielettrico, possiamo calcolare la tensione massima che il condensatore può sopportare.

Se l’intensità di rottura è $E_d$ e lo spessore del materiale dielettrico è *d*, allora la tensione di rottura è:

$U_d =E_d \cdot d$

[domanda:EB104]

Qui calcoliamo con la formula vista in precedenza (attenzione alle unità di misura!):

$\begin{split} U_d &= \qty{400}{\kilo\volt\per\centi\metro} \cdot \qty{0,15}{\milli\metro} \\ &= \qty{40000000}{\volt\per\metro} \cdot \qty{0,00015}{\metro} \\ &= \qty{6000}{\volt} \\ &= \qty{6}{\kilo\volt} \end{split}$

---

Un’altra abilità importante è saper distinguere nelle schematizzazioni le linee del campo elettrico da quelle del campo magnetico, che verranno trattate in seguito.

Con una semplice regola pratica è piuttosto semplice: le linee del campo elettrico hanno un inizio e una fine, quelle del campo magnetico no! La direzione del campo elettrico va sempre dal potenziale più positivo a quello più negativo.

[domanda:EB105]

<margin>
[immagine:884:e_feldlinien_vertikalantenne: Linee di campo su un’antenna verticale]
</margin>