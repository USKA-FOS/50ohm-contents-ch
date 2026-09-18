Nella classe E abbiamo già imparato le basi del trasformatore. Esso è costituito da due bobine accoppiate magneticamente tramite un nucleo di ferro o ferrite. Per distinguerle, si parla di lato primario con numero di spire $N_P$ e lato secondario con numero di spire $N_S$.

Il principio del trasformatore si basa su un effetto fisico fondamentale: l'induzione elettromagnetica. Se il campo magnetico in una bobina cambia — come avviene quando si applica una tensione alternata — in una bobina adiacente, accoppiata magneticamente, viene indotta una tensione elettrica. Secondo la legge dell'induzione, questa tensione è diretta in modo da opporsi alla causa della sua formazione. Si parla quindi anche di *induzione contraria*.

[question:AC301]

Nella classe E abbiamo già imparato la formula del rapporto di trasformazione $ü$:

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Per le correnti vale invece la relazione inversa:

$ü = \frac{N_P}{N_S} = \frac{I_S}{I_P} = \frac{U_P}{U_S}$

Con questa formula, che si trova anche nella raccolta di formule, si può risolvere la domanda successiva:

[question:AC302]

---

Poiché i conduttori percorsi da corrente non devono riscaldarsi eccessivamente per evitare danni all'isolamento o addirittura la fusione del conduttore, non si può superare una determinata corrente massima in funzione della sezione del conduttore. Se si rapporta l'intensità di corrente alla sezione del conduttore in $\unit{\milli\meter\squared}$, si ottiene la cosiddetta densità di corrente $S$. Per i trasformatori, secondo le norme vigenti, non si dovrebbe superare una densità di corrente massima di circa $\qty{2,5}{\ampere\per\milli\meter\squared}$.

La formula di calcolo è la seguente (vedi raccolta di formule - voce: capacità di carico degli avvolgimenti):

$I = S \cdot A_\mathrm{Dr}$

<unit>
Densità di corrente $S = \frac{I}{A} $ in $\unit{\ampere\per\milli\meter\squared}$
</unit>

<indepth>
Secondo la VDE, per conduttori di rame liberamente posati, la corrente massima ammessa è fissata a $\qty{12}{\ampere}$ con una sezione di $\qty{0,75}{\milli\meter\squared}$. Nei fusibili, la densità di corrente può raggiungere fino a $\qty{3000}{\ampere\per\milli\meter\squared}$.
</indepth>

Prova ora a rispondere alla seguente domanda. Per farlo, ti serviranno la formula per la sezione di un conduttore e quella per la capacità di carico degli avvolgimenti. Assicurati di convertire correttamente le unità di misura.

[question:AC307]

---

Uno degli ambiti di applicazione più importanti dei trasformatori nella tecnica ad alta frequenza è l’**adattamento dell’impedenza**. In questo caso, i trasformatori vengono utilizzati come cosiddetti trasformatori di adattamento.

A differenza dei trasformatori di rete, il nucleo di questi trasformatori non è solitamente costituito da ferro massiccio, ma da polvere di ferro pressata o ferrite. Questi materiali sono più adatti alle alte frequenze e riducono le perdite.

<indepth>
Con *adattamento* si intende che l’impedenza di una sorgente (ad esempio un trasmettitore) viene adattata il più possibile all’impedenza del carico (ad esempio un’antenna). Solo con un buon adattamento la potenza può essere trasmessa in modo ottimale, senza che parte dell’energia venga riflessa.
</indepth>

Un trasformatore di adattamento ha quindi il compito di convertire un’impedenza data in un’altra, in modo che sorgente e carico si adattino il più possibile.

---

Nella raccolta di formule troviamo la formula del rapporto di trasformazione $ü$:

$ü = \sqrt{\frac{Z_p}{Z_s}} = \frac{N_p}{N_s} = \frac{U_p}{U_s}$

Se si elevano al quadrato entrambi i membri dell’equazione, si ottiene:

$ü^2 = \frac {Z_p}{Z_s} = \left(\frac{N_p}{N_s}\right)^2 = \left(\frac{U_p}{U_s}\right)^2$

Da ciò si deduce che il rapporto delle impedenze è il quadrato del rapporto delle tensioni e quindi anche il quadrato del rapporto delle spire. In altre parole, un determinato rapporto di spire porta a un rapporto di impedenze quadraticamente maggiore.

<indepth>
Derivazione della formula per la trasmissione dell’impedenza:
$ P_p = P_s$
$U_p \cdot I_p = U_s \cdot I_s$
Sostituire $U$ con la legge di Ohm: $U = I \cdot R$; $R$ viene sostituito da $Z$
$(I_p \cdot Z_p) \cdot I_p = (I_s \cdot Z_s) \cdot I_s$
Formare il rapporto di impedenza su un lato:
$ \frac{Z_p}{Z_s} = \frac{{I_s}^2}{{I_p}^2} = ü^2$
In alternativa, sostituire $I$ con la legge di Ohm:
$I = \frac{U}{R}$
$R$ viene sostituito da $Z$
$\frac{U_p}{Z_p} \cdot U_p  = \frac{U_s}{Z_s} \cdot U_s$
Formare il rapporto di impedenza su un lato:
$ \frac{Z_p}{Z_s} = \frac{{U_p}^2}{{U_s}^2} = ü^2$
</indepth>

---

Come esempio, consideriamo un’antenna alimentata in punta, che approfondiremo in un capitolo successivo. La sua impedenza di ingresso è di circa $\qty{2450}{\ohm}$ ed è quindi notevolmente elevata. Essa deve essere adattata a un trasmettitore con impedenza di carico di $\qty{50}{\ohm}$.

<margin>
[picture:260:a_endgespeiste_antenne:Antenne alimentata in punta con adattamento dell’impedenza tramite un trasformatore]
</margin>

Per la trasmissione dell’impedenza da $\qty{50}{\ohm}$ a $\qty{2450}{\ohm}$, il rapporto è $Z_p:Z_s = \qty{50}{\ohm}:\qty{2450}{\ohm} = 1:49$. Ciò significa che $ü^2 = 1:49$ e quindi $ü=\sqrt{1}:\sqrt{49}=1:7$. Questo significa che il lato primario deve avere solo un settimo delle spire del lato secondario per ottenere l’adattamento dell’impedenza, ad esempio $N_p=1$ e $N_s=7$. In pratica, di solito si utilizza un rapporto di spire di $2:14$ (cfr. figura [ref:a_unun]).

<margin>
[photo:332:a_unun:Esempio di un trasformatore Unun con rapporto di spire 2 a 14, in cui lato primario e secondario sono avvolti insieme bifilari (intrecciati)]
</margin>

La domanda seguente corrisponde essenzialmente all’esempio appena considerato. Per un dipolo alimentato in punta viene indicata un’impedenza di ingresso di circa $\qty{2,5}{\kilo\ohm}$. In pratica, tuttavia, questo valore oscilla tipicamente tra $\qty{2}{\kilo\ohm}$ e $\qty{3}{\kilo\ohm}$, a seconda dell’ambiente e della struttura. Con un rapporto di spire di circa $1:7$, in genere si ottiene comunque un adattamento sufficientemente buono a $\qty{50}{\ohm}$.

[question:AC306]

Prova ora a risolvere le seguenti domande in modo autonomo con le tue conoscenze.

[question:AC305]
[question:AC303]
[question:AC304]
