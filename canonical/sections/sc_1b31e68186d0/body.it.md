Nella sezione [sec:uebertrager_1] abbiamo già appreso le basi del trasformatore. È costituito da due bobine accoppiate magneticamente tramite un nucleo di ferro o ferrite. Per distinguere i lati, si parla di lato primario con il numero di spire $N_P$ e lato secondario con il numero di spire $N_S$.

Il principio del trasformatore si basa su un effetto fisico fondamentale: l'induzione elettromagnetica. Se il campo magnetico in una bobina cambia – come accade quando viene applicata una tensione alternata – viene indotta una tensione elettrica in una bobina adiacente accoppiata magneticamente. Secondo la legge di induzione, questa è diretta in modo da opporsi alla causa della sua formazione. Si parla quindi anche di *controinduzione*.

[question:AC301]

Nella sezione [sec:uebertrager_1] abbiamo già appreso la formula per il rapporto di trasformazione $r$:

$r = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Per le correnti vale corrispondentemente l'inverso:

$r = \frac{N_P}{N_S} = \frac{I_S}{I_P} = \frac{U_P}{U_S}$

Con questa formula, che si trova anche nella raccolta di formule, è possibile risolvere la prossima domanda:

[question:AC302]

---

Poiché i conduttori percorsi da corrente non devono surriscaldarsi eccessivamente, per evitare danni all'isolamento o addirittura l'incandescenza del conduttore, non deve essere superata una determinata corrente massima in dipendenza dalla sezione del conduttore. Mettendo in relazione l'intensità di corrente con la sezione del conduttore in $\unit{\milli\meter\squared}$, si ottiene la cosiddetta densità di corrente $S$. Per i trasformatori, secondo le norme pertinenti, non dovrebbe essere superata una densità di corrente massima di circa $\qty{2,5}{\ampere\per\milli\meter\squared}$.

La formula di calcolo è (vedi raccolta di formule - voce: capacità di carico degli avvolgimenti):

$I = S \cdot A_\mathrm{Dr}$

<unit>
Densità di corrente $S = \frac{I}{A} $ in  $\unit{\ampere\per\milli\meter\squared}$
</unit>

<law>
La norma per installazioni a bassa tensione SN 411000 (NIN) regola le installazioni elettriche in Svizzera fino a 1000 V AC o 1500 V DC e serve a proteggere persone, animali e beni. Si basa sull'ordinanza per installazioni a bassa tensione (NIV) e sulle norme internazionali IEC e Cenelec.

Per conduttori in rame posati liberamente, la corrente massima ammissibile è stabilita in:

- $\qty{6}{\ampere}$ per una sezione di $\qty{0,75}{\milli\meter\squared}$.

- $\qty{10}{\ampere}$ per una sezione di $\qty{1.00}{\milli\meter\squared}$.

temperatura ambiente max.: 30°C

Conduttori raggruppati sotto una guaina protettiva

Fonte: Conduttori in rame - Dimensionamento secondo NIN 2000
</law>

<attention>
Si sottolinea espressamente che una concessione radioamatoriale **non** autorizza a realizzare installazioni a bassa tensione.
</attention>

Prova ora a rispondere alla seguente domanda. Per farlo hai bisogno della formula per l'area della sezione di un conduttore e della formula per la capacità di carico degli avvolgimenti. Assicurati che le unità di misura siano convertite correttamente.

[question:AC307]

---

Uno dei campi di applicazione più importanti dei trasformatori nella tecnologia a radiofrequenza è l'**adattamento di impedenza**. Qui i trasformatori sono utilizzati come cosiddetti trasformatori di adattamento.

A differenza dei trasformatori di rete, il nucleo di tali trasformatori di solito non è di ferro massiccio, ma di polvere di ferro pressata o ferrite. Questi materiali sono più adatti per alte frequenze e riducono le perdite.

<indepth>
Per *adattamento* si intende che l'impedenza di una sorgente (ad esempio di un trasmettitore) sia adattata il più possibile all'impedenza del carico (ad esempio di un'antenna). Solo con un buon adattamento la potenza può essere trasmessa in modo ottimale, senza che parte dell'energia venga riflessa.
</indepth>

Un trasformatore di adattamento ha quindi il compito di trasformare una data impedenza in un'altra, in modo che sorgente e carico si adattino il meglio possibile.

---

Nella raccolta di formule troviamo la formula per il rapporto di trasformazione $r$:

$r = \sqrt{\frac{Z_p}{Z_s}} = \frac{N_p}{N_s} = \frac{U_p}{U_s}$

Elevando al quadrato entrambi i membri dell'equazione si ottiene:


$r^2 = \frac {Z_p}{Z_s} = \left(\frac{N_p}{N_s}\right)^2 = \left(\frac{U_p}{U_s}\right)^2$

Da ciò si riconosce che il rapporto di impedenza è il quadrato del rapporto di tensione e quindi anche il quadrato del rapporto del numero di spire. O, detto in altro modo, un determinato rapporto di spire porta a un rapporto di impedenza quadraticamente più alto.

<indepth>
Derivazione della formula per la trasformazione dell'impedenza:
$ P_p = P_s$
$U_p \cdot I_p = U_s \cdot I_s$
Sostituire $U$ con la legge di Ohm: $U = I \cdot R$;
$R$ viene sostituito da $Z$
$(I_p \cdot Z_p) \cdot I_p = (I_s \cdot Z_s) \cdot I_s$
Formare il rapporto di impedenza su un lato:
$ \frac{Z_p}{Z_s} = \frac{{I_s}^2}{{I_p}^2} = r^2$
In alternativa, sostituire $I$ con la legge di Ohm:
$I = \frac{U}{R}$
$R$ viene sostituito da $Z$
$\frac{U_p}{Z_p} \cdot U_p  = \frac{U_s}{Z_s} \cdot U_s$
Formare il rapporto di impedenza su un lato:
$ \frac{Z_p}{Z_s} = \frac{{U_p}^2}{{U_s}^2} = r^2$
</indepth>

---

Come esempio consideriamo un'antenna alimentata all'estremità, che esamineremo più in dettaglio in un capitolo successivo. La sua impedenza di ingresso è di circa $\qty{2450}{\ohm}$ ed è quindi chiaramente di valore alto. Deve essere adattata a un trasmettitore con un'impedenza di carico di $\qty{50}{\ohm}$.

<margin>
[picture:260:a_endgespeiste_antenne:Antenna alimentata all'estremità con adattamento di impedenza tramite un trasformatore]
</margin>

Per la trasformazione dell'impedenza da $\qty{50}{\ohm}$ a $\qty{2450}{\ohm}$, il rapporto è $Z_p:Z_s = \qty{50}{\ohm}:\qty{2450}{\ohm} = 1:49$. Ciò significa $r^2 = 1:49$ e quindi $r=\sqrt{1}:\sqrt{49}=1:7$. Ciò significa che il lato primario deve avere solo un settimo delle spire del lato secondario affinché l'adattamento di impedenza abbia successo, ad esempio $N_p=1$ e $N_s=7$. In pratica si usa solitamente un rapporto di spire di $2:14$ (cfr. figura [ref:a_unun]).

<margin>
[photo:332:a_unun:Esempio di un trasformatore Unun con un rapporto di spire di 2 a 14, in cui il lato primario e secondario sono avvolti insieme in modo bifilare (intrecciato)]
</margin>

Il seguente esercizio corrisponde essenzialmente all'esempio considerato in precedenza. Per un dipolo alimentato all'estremità, qui viene indicata un'impedenza di ingresso di circa $\qty{2,5}{\kilo\ohm}$. Nella pratica, tuttavia, questo valore varia, a seconda dell'ambiente e della struttura, tipicamente nell'intervallo da circa $\qty{2}{\kilo\ohm}$ a $\qty{3}{\kilo\ohm}$.
Con un rapporto di spire di circa $1:7$, si può comunque ottenere in genere un adattamento sufficientemente buono a $\qty{50}{\ohm}$.

[question:AC306]

Prova ora a risolvere autonomamente le seguenti domande con le tue conoscenze.

[question:AC305]
[question:AC303]
[question:AC304]
