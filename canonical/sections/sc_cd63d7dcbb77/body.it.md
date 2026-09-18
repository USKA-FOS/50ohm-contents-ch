Nella classe E abbiamo già imparato a conoscere il decibel come strumento per descrivere i rapporti e abbiamo visto che una variazione di potenza di $\qty{3}{\dB}$ corrisponde a un fattore di potenza di $\num{2}$. Nella raccolta di formule troviamo la tabella [ref:a_dezibel_leistungsfaktoren], che contiene ulteriori corrispondenze importanti.

<margin>
| c:dB | c:≈ fattore di potenza |
| $-20$ | $\num{0,01}$ |
| $-10$ | $\num{0,1}$ |
| $-6$ | $\num{0,25}$ |
| $-3$ | $\num{0,5}$ |
| $-1$ | $\num{0,79}$ |
| $0$ | $\num{1}$ |
| $1,5$ | $\sqrt{2} = \num{1,41}$ |
| $2,15$ | $\num{1,64}$ |
| $3$ | $\num{2}$ |
| $5$ | $\sqrt{10} = \num{3,16}$ |
| $6$ | $\num{4}$ |
| $10$ | $\num{10}$ |
| $20$ | $\num{100}$ |
[table:a_dezibel_leistungsfaktoren:Fattori di potenza importanti in $\unit{\dB}$]
</margin>

La raccolta di formule fornisce la seguente formula per convertire un rapporto di potenza in $\unit{\dB}$, che abbiamo già imparato nella classe E. Il rapporto $g$ tra due potenze $P_1$ e $P_2$ in $\unit{\dB}$ è:

$g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$

[question:AD428]

Se si vuole determinare un fattore di rapporto partendo da un valore in $\unit{\dB}$, la formula deve essere modificata:

$\begin{align*} g &= 10 \cdot \log_{10}\left( x \right) \unit{\dB} & \quad\quad\quad &|: \qty{10}{\dB} \\ \frac{g}{\qty{10}{\dB}} &= \log_{10}\left( x \right) &~&| \quad 10^{x}\\ x &= 10^{\frac{g}{\qty{10}{\dB}}} &~&~\end{align*}$

Con queste due formule possiamo quindi convertire facilmente tra valori in $\unit{\dB}$ e fattori di rapporto. Prova ora a risolvere le seguenti tre domande:

---

[question:AA105]
[question:AA106]
[question:AD426]

<tip>
Nella classe E abbiamo già imparato il seguente trucco: senza calcolatrice, è possibile stimare i valori in decibel che terminano con uno "$0$": basta coprire l’ultimo zero, la cifra risultante indica il numero di zeri del fattore di rapporto. Esempio: $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zeri} \rightarrow \text{fattore di rapporto}~1000$!

Anche il calcolo inverso è semplice: uno con $12$ zeri ($\num{1000000000000}$) in $\unit{\dB}$ è semplicemente il numero di zeri, quindi $12$, moltiplicato per $10$. Ne risulta un fattore di guadagno di $\qty{120}{\dB}$.

Anche per valori in $\unit{\dB}$ che non terminano con uno $0$ si può determinare il fattore corrispondente scomponendo il valore:

* Si può scomporre $\qty{9}{\dB}$ in $\qty{6}{\dB} + \qty{3}{\dB}$, che corrisponde a una moltiplicazione di $4\cdot 2 = 8$.
* Quale fattore corrisponde a un rapporto di potenza di $\qty{17}{\dB}$? $\qty{17}{\dB} = \qty{20}{\dB} - \qty{3}{\dB}$, quindi fattore $100$ diviso $2$ uguale $50$.
</tip>

Il decibel ($\unit{\dB}$) descrive fondamentalmente un rapporto adimensionale, ad esempio di potenze o tensioni. Per questo motivo, $\unit{\dB}$ viene utilizzato principalmente per indicare guadagni e attenuazioni. In questi casi non è necessario alcun suffisso aggiuntivo, poiché viene indicato solo il rapporto tra due grandezze. I valori negativi in decibel indicano valori di rapporto inferiori a $1$. Quindi $\qty{-3}{\dB}$ corrisponde a un valore di rapporto di $\frac{1}{2} = \num{0,5}$.

Tuttavia, è anche possibile utilizzare i valori in decibel per indicare un livello assoluto. A tal fine, è necessaria una grandezza di riferimento fissa $P_0$:

$p = 10\cdot \log_{10}\left(\frac{P}{P_0}\right)\unit{\dB}$

---

Questa grandezza di riferimento può essere, ad esempio, una potenza di $\qty{1}{\milli\watt}$. In questo caso, il valore in decibel riceve un suffisso corrispondente: se il livello si riferisce a $\qty{1}{\milli\watt}$, si parla di $\unit{\dBm}$. In questo modo è chiaramente definito a quale valore di potenza assoluta si riferisce il livello in decibel.

Se, ad esempio, si incontra l’indicazione "Il trasmettitore ha una potenza d’uscita di $\qty{20}{\dBm}$", questo valore può essere facilmente convertito in milliwatt. Un livello di $\qty{20}{\dB}$ corrisponde a un fattore di potenza di $100$ (quindi due zeri). Questo fattore viene moltiplicato per la grandezza di riferimento di $\qty{1}{\milli\watt}$:

$ P = 100 \cdot \qty{1}{\milli\watt} = \qty{100}{\milli\watt}$

Nella tabella [ref:a_bezugsgroessen] sono elencate le principali grandezze di riferimento e le rispettive abbreviazioni in $\unit{\dB}$.

<margin>
| l: Abbreviazione          | X: Valore di riferimento |
| $\unit{\dBm}$             | $\qty{1}{\milli\watt}$ |
| $\unit{\dBW}$             | $\qty{1}{\watt}$       |
| $\unit{\dBu}$             | $\qty{0,775}{\volt}$   |
| $\unit{\dB\micro\volt}$ | $\qty{1}{\micro\volt}$ |
[table:a_bezugsgroessen:Principali grandezze di riferimento dalla raccolta di formule]
</margin>

Le seguenti domande possono essere risolte utilizzando la formula della raccolta di formule e la sua modifica iniziale di questa lezione, se si utilizza la grandezza di riferimento corretta.

[question:AA109]
[question:AA110]
[question:AA107]
[question:AA108]

---

Perché si fa tutto questo e si indicano le potenze assolute in $\unit{\dBm}$ e $\unit{\dBW}$? Come già accennato nella classe E, l’uso del decibel serve principalmente a semplificare i calcoli. Rappresentando i guadagni e le attenuazioni in decibel, è possibile stimare facilmente intere catene di segnale mediante addizione e sottrazione, senza dover ricorrere a complesse moltiplicazioni e divisioni.

La figura [ref:e_signalkette] mostra una tale catena di segnale con tre stadi amplificatori. Il segnale di ingresso ha una potenza di $\qty{1}{\milli\watt}$, che corrisponde a $\qty{0}{\dBm}$. Attraverso i tre stadi amplificatori, il segnale viene amplificato complessivamente a $\qty{60}{\dBm}$ (quindi $\num{1000000}\cdot \qty{1}{\milli\watt}$), che corrisponde a una potenza di $\qty{1000}{\watt}$.

La figura [ref:e_signalkette_2] mostra un altro esempio di una catena di segnale in cui è inserito un attenuatore con un’attenuazione di $\qty{20}{\dB}$, che corrisponde a un guadagno di $\qty{-20}{\dB}$. Il segnale di ingresso ha una potenza di $\qty{1}{\milli\watt}$, quindi $\qty{0}{\dBm}$. Attraverso il primo stadio amplificatore, il segnale viene aumentato a $\qty{10}{\dBm}$. Successivamente, viene attenuato dall’attenuatore a $\qty{-10}{\dBm}$ e infine amplificato dal secondo stadio amplificatore a $\qty{0}{\dBm}$, che corrisponde nuovamente a $\qty{1}{\milli\watt}$.

<margin>
[picture:877:e_signalkette:Catena di segnale con tre amplificatori]
[picture:1053:e_signalkette_2:Catena di segnale con due amplificatori e un attenuatore]
</margin>

<indepth>
Perché è consentito sottrarre un’attenuazione di $\qty{3}{\dB}$ dal livello $\qty{9}{\dBm}$? Entrambi i valori non hanno forse la stessa unità di misura? Nel caso del Bel ($\unit{\bel}$) o del decibel ($\unit{\dB}$) si tratta di un’unità di misura ausiliaria (detta anche pseudo-unità).
In linea di principio, il valore numerico potrebbe anche essere scritto senza l’unità $\unit{\dB}$. Tuttavia, con il suffisso $\unit{\dB}$ è chiaro che si tratta di un rapporto logaritmico tra due grandezze. Senza questa unità, bisognerebbe descrivere verbalmente il significato del valore numerico.
</indepth>

Per determinare il guadagno totale di un amplificatore di potenza a più stadi, è necessario calcolare la differenza tra la potenza d’uscita e quella d’ingresso mediante sottrazione con segno dei valori in dBm. Esempio: potenza d’ingresso $\qty{-5}{\dBm}$, potenza d’uscita $\qty{20}{\dBm}$ dà un guadagno totale di $\qty{25}{\dB}$ ($\qty{20}{\dBm} - (\qty{-5}{\dBm}) = \qty{25}{\dB}$)

[question:AF428]

Inoltre, nella classe E abbiamo già imparato i suffissi $\unit{\dBd}$ e $\unit{\dBi}$, che vengono utilizzati per indicare i guadagni delle antenne. In questo caso, il valore in decibel non si riferisce a una potenza o a una tensione, ma a un particolare radiatore di riferimento. I riferimenti più comuni sono $\unit{\dBi}$, riferito al radiatore sferico isotropo, e $\unit{\dBd}$, riferito al dipolo a semionda.

---

Oltre ai rapporti di potenza, possiamo utilizzare il decibel anche per indicare i *rapporti di tensione* e i *livelli di tensione*. A tal fine, possiamo utilizzare la formula $P = \frac{U^2}{R}$. Quindi possiamo scrivere:

$\begin{split}g &= 10 \cdot \log_{10}\left(\frac{P_1}{P_2}\right)\\ g &= 10 \cdot \log_{10}\left(\frac{\frac{U_1^2}{\cancel{R}}}{\frac{U_2^2}{\cancel{R}}}\right)\\ g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right) \end{split}$

<tip>
*Calcoli con i logaritmi:*
Alcune semplici regole di calcolo consentono di risolvere esercizi con i decibel senza l’uso di una calcolatrice.

* Il logaritmo di un prodotto di due numeri corrisponde alla somma dei logaritmi: $\log_{10}(a\cdot b) = \log_{10}(a)+ \log_{10}(b)$
* Il logaritmo di una divisione di due numeri corrisponde alla differenza dei logaritmi: $\log_{10}(a / b) = \log_{10}(a) - \log_{10}(b)$
* Il logaritmo di un numero al quadrato: $\log_{10}(x^2)= 2 \cdot \log_{10}(x)$
* Il logaritmo di una radice: $\log_{10}(\sqrt{x})= \frac{1}{2} \cdot \log_{10}(x)$
</tip>

Il logaritmo di un numero al quadrato è uguale a due volte il logaritmo del numero:

$\log_{10}(x^2)=2 \cdot \log_{10}(x)$

Ne consegue che:

$\begin{split} g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right)\\ g &= 10 \cdot 2 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \\ g &= 20 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \end{split}$

---

Pertanto, calcoliamo un rapporto *$a$* tra due tensioni $U_1$ e $U_2$ moltiplicando il logaritmo del rapporto non con il fattore $10$, ma con il fattore $20$. Questa formula si trova anche nella raccolta di formule.

[question:AA111]
[question:AD427]

<attention>
Fare sempre attenzione a distinguere tra rapporti di potenza e rapporti di tensione quando si effettuano calcoli con i decibel!
</attention>

Per determinare i livelli di tensione, dobbiamo prima definire una tensione di riferimento (cfr. tabella [ref:a_bezugsgroessen]). Quando si misurano i segnali di ricezione, le (molto piccole) tensioni all’ingresso del ricevitore vengono spesso espresse in $\unit{\micro\volt}$. Il livello di tensione corrispondente ha quindi l’unità $\unit{\dBuV}$. Esempio:

$\qty{10}{\micro\volt} \rightarrow 20 \cdot \log_{10}\left(\frac{\qty{10}{\micro\volt}}{\qty{1}{\micro\volt}}\right)=\qty{20}{\dBuV}$

---

Nella seguente domanda, il valore di riferimento è $\qty{1}{\micro\volt\per\meter}$. Prova a risolvere l’esercizio con le tue conoscenze.

<attention>
Attenzione, qui si intende $\unit{\dB(\micro\volt\per\meter)}$ e non $\unit{(\dB\micro\volt)/\meter}$!
</attention>

[question:AA112]

<tip>
Anche per le tensioni si possono fare molti calcoli mentalmente utilizzando la tabella della raccolta di formule:

| c:dB | c:≈ rapporto di tensione |
| $-20$ | $\num{0,1}$ |
| $-10$ | $\num{0,32}$ |
| $-6$ | $\num{0,5}$ |
| $-3$ | $\num{0,71}$ |
| $-1$ | $\num{0,89}$ |
| $0$ | $\num{1}$ |
| $1$ | $\num{1,12}$ |
| $3$ | $\num{1,14}$ |
| $6$ | $2$ |
| $10$ | $3,16$ |
| $20$ | $10$ |
[table:a_spannungsverhaeltnisse:Rapporti di tensione importanti in $\unit{\dB}$]

*Esempio:*

* A quanti $\unit{\dB}$ corrisponde un rapporto di tensione di $4$? $4 = 2 \cdot 2 \rightarrow \qty{6}{\dB} + \qty{6}{\dB} = \qty{12}{\dB}$
</tip>