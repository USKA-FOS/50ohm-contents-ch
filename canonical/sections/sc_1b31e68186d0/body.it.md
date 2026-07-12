Nella classe E abbiamo già appreso le basi del trasformatore. È costituito da due bobine accoppiate magneticamente tramite un nucleo di ferro o ferrite. Affinché i lati possano essere tenuti separati, si parla di lato primario con il numero di spire $N_P$ e lato secondario con il numero di spire $N_S$.

Il principio del trasformatore si basa su un effetto fisico fondamentale: l'induzione elettromagnetica. Se il campo magnetico in una bobina cambia – come accade quando si applica una tensione alternata – una tensione elettrica viene indotta in una bobina adiacente accoppiata magneticamente. Secondo la legge di induzione, questa è diretta in modo tale da opporsi alla causa della sua formazione. Si parla quindi anche di *controinduzione*.

[question:AC301]

Nella classe E abbiamo già appreso la formula per il rapporto di trasformazione $ü$:

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Per le correnti vale inversamente:

$ü = \frac{N_P}{N_S} = \frac{I_S}{I_P} = \frac{U_P}{U_S}$

Con questa formula, che si trova anche nella raccolta di formule, è possibile risolvere la domanda successiva:

[question:AC302]

---

Poiché i conduttori attraversati da corrente non devono surriscaldarsi eccessivamente per evitare danni all'isolamento o persino il surriscaldamento del conduttore, una determinata corrente massima non deve essere superata in funzione della sezione del conduttore. Se si mette in relazione la corrente con la sezione del conduttore in $\unit{\milli\meter\squared}$, si ottiene la cosiddetta densità della corrente $S$. Per i trasformatori, secondo le normative pertinenti, non si dovrebbe superare una densità della corrente di circa $\qty{2,5}{\ampere\per\milli\meter\squared}$.

La formula di calcolo è (vedi raccolta di formule - parola chiave: Capacità di carico degli avvolgimenti):

$I = S \cdot A_\mathrm{Dr}$

<unit>
Densità della corrente $S = \frac{I}{A} $ in  $\unit{\ampere\per\milli\meter\squared}$
</unit>

<indepth>
Secondo VDE, per conduttori in Rame liberamente posati, la corrente massima ammissibile è fissata a $\qty{12}{\ampere}$ con una superficie di sezione di $\qty{0,75}{\milli\meter\squared}$. Per i fusibili, la densità della corrente può raggiungere fino a $\qty{3000}{\ampere\per\milli\meter\squared}$.
</indepth>

Ora prova a rispondere alla seguente domanda. Per fare ciò, avrai bisogno della formula per la sezione di un conduttore e della formula per la capacità di carico degli avvolgimenti. Presta attenzione alla corretta conversione delle unità.

[question:AC307]

---

Uno dei campi di applicazione più importanti dei trasformatori nella tecnica ad alta frequenza è l'**adattamento di impedenza**. In questo caso, i trasformatori vengono utilizzati come cosiddetti trasformatori di adattamento.

A differenza dei trasformatori di rete, il nucleo di tali trasformatori di adattamento non è solitamente costituito da ferro massiccio, ma da polvere di ferro pressata o ferrite. Questi materiali sono più adatti per alte frequenze e riducono le perdite.

<indepth>
Per *adattamento* si intende che l'impedenza di una sorgente (ad esempio, un trasmettitore) viene adattata il più precisamente possibile all'impedenza del carico (ad esempio, un'antenna). Solo con un buon adattamento la potenza può essere trasmessa in modo ottimale, senza che una parte dell'energia venga riflessa.
</indepth>

Un trasformatore di adattamento ha quindi il compito di convertire un'impedenza data in un'altra, in modo che sorgente e carico si adattino al meglio l'uno all'altro.

---

Nella raccolta di formule troviamo la formula per il rapporto di trasformazione $ü$:

$ü = \sqrt{\frac{Z_p}{Z_s}} = \frac{N_p}{N_s} = \frac{U_p}{U_s}$

Elevando al quadrato i lati dell'equazione si ottiene:


$ü^2 = \frac {Z_p}{Z_s} = \left(\frac{N_p}{N_s}\right)^2 = \left(\frac{U_p}{U_s}\right)^2$

Da ciò si evince che il rapporto di impedenza è il quadrato del rapporto di tensione e quindi anche il quadrato del rapporto del numero di spire. O, detto altrimenti, un determinato rapporto di spire porta a un rapporto di impedenza quadraticamente più elevato.

<indepth>
Derivazione della formula per la trasmissione di impedenza:
$ P_p = P_s$
$U_p \cdot I_p = U_s \cdot I_s$
Sostituire la legge di Ohm per $U$: $U = I \cdot R$;
$R$ viene sostituito con $Z$
$(I_p \cdot Z_p) \cdot I_p = (I_s \cdot Z_s) \cdot I_s$
Formare il rapporto di impedenza su un lato:
$ \frac{Z_p}{Z_s} = \frac{{I_s}^2}{{I_p}^2} = ü^2$
Alternativamente, sostituire la legge di Ohm per $I$:
$I = \frac{U}{R}$
$R$ viene sostituito con $Z$
$\frac{U_p}{Z_p} \cdot U_p  = \frac{U_s}{Z_s} \cdot U_s$
Formare il rapporto di impedenza su un lato:
$ \frac{Z_p}{Z_s} = \frac{{U_p}^2}{{U_s}^2} = ü^2$
</indepth>

---

Come esempio, consideriamo un'antenna alimentata all'estremità, che esamineremo più in dettaglio in un capitolo successivo. La sua impedenza di ingresso è di circa $\qty{2450}{\ohm}$ ed è quindi significativamente ad alta impedenza. Deve essere adattata a un trasmettitore con un'impedenza di carico di $\qty{50}{\ohm}$.

<margin>
[picture:260:a_endgespeiste_antenne:Antenna alimentata all'estremità con adattamento di impedenza tramite un trasformatore]
</margin>

Per la trasmissione di impedenza da $\qty{50}{\ohm}$ a $\qty{2450}{\ohm}$, il rapporto $Z_p:Z_s = \qty{50}{\ohm}:\qty{2450}{\ohm} = 1:49$. Ciò significa $ü^2 = 1:49$ e quindi $ü=\sqrt{1}:\sqrt{49}=1:7$. Ciò significa che il lato primario deve avere solo un settimo delle spire del lato secondario affinché l'adattamento di impedenza abbia successo, ad esempio $N_p=1$ e $N_s=7$. In pratica, viene solitamente utilizzato un rapporto di spire di $2:14$ (cfr. figura [ref:a_unun]).

<margin>
[photo:332:a_unun:Esempio di trasformatore Unun con un rapporto di spire da 2 a 14, dove il lato primario e secondario sono avvolti insieme bifilarmente (ritorti)]
</margin>

Il seguente compito corrisponde essenzialmente all'esempio precedentemente considerato. Per un dipolo alimentato all'estremità, qui viene fornita un'impedenza di ingresso di circa $\qty{2,5}{\kilo\ohm}$. In pratica, tuttavia, questo valore varia tipicamente nell'intervallo da circa $\qty{2}{\kilo\ohm}$ a $\qty{3}{\kilo\ohm}$, a seconda dell'ambiente e della struttura. 
Con un rapporto di spire di circa $1:7$, è comunque possibile ottenere un adattamento sufficientemente buono a $\qty{50}{\ohm}$.

[question:AC306]

Ora prova a risolvere autonomamente le seguenti domande con le tue conoscenze.

[question:AC305]
[question:AC303]
[question:AC304]
