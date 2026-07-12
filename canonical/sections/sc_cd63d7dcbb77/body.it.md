Nella classe E abbiamo già imparato a conoscere il decibel come strumento per descrivere rapporti e abbiamo visto che una variazione di potenza di $\qty{3}{\dB}$ corrisponde a un fattore di potenza di $\num{2}$. Nella raccolta di formule troviamo la tabella [ref:a_dezibel_leistungsfaktoren], che contiene altre corrispondenze importanti. 

<margin>
| c:dB | c:≈ Fattore di potenza |
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

La raccolta di formule fornisce la seguente formula per convertire un rapporto di potenza in $\unit{\dB}$, che abbiamo già incontrato nella classe E. Il rapporto $g$ di due potenze $P_1$ e $P_2$ in $\unit{\dB}$ è:

$g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$

Se si desidera determinare un fattore di rapporto da un valore in $\unit{\dB}$, la formula deve essere riorganizzata:

$\begin{align*} g &= 10 \cdot \log_{10}\left( x \right) \unit{\dB} & \quad\quad\quad &|: \qty{10}{\dB} \\ \frac{g}{\qty{10}{\dB}} &= \log_{10}\left( x \right) &~&| \quad 10^{x}\\ x &= 10^{\frac{g}{\qty{10}{\dB}}} &~&~\end{align*}$

Con queste due formule possiamo quindi facilmente convertire tra indicazioni in $\unit{\dB}$ e fattori di rapporto. Prova ora a calcolare le due seguenti domande:

---

[question:AA105]
[question:AA106]

<tip>
Nella classe E abbiamo già imparato il seguente trucco: Senza calcolatrice, i valori in decibel che terminano con "0" possono essere stimati: basta coprire l'ultima cifra zero, la cifra rimanente indica il numero di zeri del fattore di rapporto. Esempio: $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zeri} \rightarrow \text{fattore di rapporto}~1000$!

Anche al contrario si calcola facilmente: uno con 12 zeri ($\num{1000000000000}$) in $\unit{\dB}$ è semplicemente il numero di zeri, cioè 12, moltiplicato per 10. Si ottiene così un fattore di amplificazione di $\qty{120}{\dB}$.

Ma anche per i valori in $\unit{\dB}$ che non terminano con 0 si può determinare il fattore corrispondente tramite scomposizione:

* Si può scomporre $\qty{9}{\dB}$ in $\qty{6}{\dB} + \qty{3}{\dB}$, che corrisponde a una moltiplicazione di $4\cdot 2 = 8$.
* Quale fattore corrisponde a un rapporto di potenza di $\qty{17}{\dB}$? $\qty{17}{\dB} = \qty{20}{\dB} - \qty{3}{\dB}$, quindi il fattore 100 diviso per 2 è 50.
</tip>

Il decibel ($\unit{\dB}$) descrive fondamentalmente un rapporto adimensionale, ad esempio di potenze o tensioni. Pertanto, il $\unit{\dB}$ viene utilizzato principalmente per indicare amplificazioni e attenuazioni. In questi casi non è necessaria alcuna indicazione aggiuntiva, poiché viene indicato solo il rapporto tra due grandezze. I valori negativi in decibel indicano, tra l'altro, valori di rapporto inferiori a 1. Così $\qty{-3}{\dB}$ corrisponde a un valore di rapporto di $\frac{1}{2} = \num{0,5}$.

È anche possibile utilizzare i valori in decibel per indicare un livello assoluto. Tuttavia, per questo è necessario un valore di riferimento fisso $P_0$:

$p = 10\cdot \log_{10}\left(\frac{P}{P_0}\right)\unit{\dB}$

---

Questo valore di riferimento può essere, ad esempio, una potenza di $\qty{1}{\milli\watt}$. In questo caso, il valore in decibel riceve un'indicazione aggiuntiva appropriata: se il livello si riferisce a $\qty{1}{\milli\watt}$, si parla di $\unit{\dBm}$. In questo modo è chiaramente definito a quale valore di potenza assoluto si riferisce il livello in decibel.

Ad esempio, se si incontra l'indicazione "Il trasmettitore ha una potenza d'uscita di $\qty{20}{\dBm}$", questo valore può essere facilmente convertito in milliwatt. Un livello di $\qty{20}{\dB}$ corrisponde a un fattore di potenza di 100 (cioè due zeri). Questo fattore viene moltiplicato per il valore di riferimento di $\qty{1}{\milli\watt}$:

$ P = 100 \cdot \qty{1}{\milli\watt} = \qty{100}{\milli\watt}$

Nella tabella [ref:a_bezugsgroessen] sono elencati i principali valori di riferimento e le rispettive abbreviazioni in $\unit{\dB}$.

<margin>
| l: Abbreviazione            | X: Valore di riferimento          |
| $\unit{\dBm}$           | $\qty{1}{\milli\watt}$ | 
| $\unit{\dBW}$           | $\qty{1}{\watt}$       | 
| $\unit{\dBu}$           | $\qty{0,775}{\volt}$   | 
| $\unit{\dB\micro\volt}$ | $\qty{1}{\micro\volt}$ | 
[table:a_bezugsgroessen:Principali valori di riferimento dalla raccolta di formule]
</margin>

Le seguenti domande possono essere calcolate utilizzando la formula dalla raccolta di formule e la sua riorganizzazione all'inizio di questa lezione, se viene utilizzato il valore di riferimento corretto.

[question:AA109]
[question:AA110]
[question:AA107]
[question:AA108]

---

Perché fare tutto questo e indicare le potenze assolute in $\unit{\dBm}$ e $\unit{\dBW}$? Come già accennato nella classe E, l'uso dei decibel serve principalmente a semplificare i calcoli. Rappresentando amplificazioni e attenuazioni in decibel, intere catene di segnale possono essere stimate molto facilmente tramite addizione e sottrazione, senza dover ricorrere a complicate moltiplicazioni e divisioni.

La figura [ref:e_signalkette] mostra una tale catena di segnale con tre stadi di amplificazione. Il segnale di ingresso ha una potenza di $\qty{1}{\milli\watt}$, che corrisponde a $\qty{0}{\dBm}$. Attraverso i tre stadi di amplificazione, il segnale viene amplificato complessivamente a $\qty{60}{\dBm}$ (cioè $\num{1000000}\cdot \qty{1}{\milli\watt}$), che corrisponde a una potenza di $\qty{1000}{\watt}$.

La figura [ref:e_signalkette_2] mostra un altro esempio di catena di segnale in cui viene utilizzato anche un attenuatore con un'attenuazione di $\qty{20}{\dB}$, che corrisponde a un'amplificazione di $\qty{-20}{\dB}$. Il segnale di ingresso ha una potenza di $\qty{1}{\milli\watt}$, cioè $\qty{0}{\dBm}$. Attraverso il primo stadio di amplificazione, il segnale viene aumentato a $\qty{10}{\dBm}$. Successivamente, viene attenuato dall'attenuatore a $\qty{-10}{\dBm}$ e infine nuovamente amplificato dal secondo stadio di amplificazione a $\qty{0}{\dBm}$, che corrisponde nuovamente a $\qty{1}{\milli\watt}$.

<margin>
[picture:877:e_signalkette:Catena di segnale con tre amplificatori]
[picture:1053:e_signalkette_2:Catena di segnale con due amplificatori e un attenuatore]
</margin>

<indepth>
Perché è lecito sottrarre un'attenuazione di $\qty{3}{\dB}$ dal livello di $\qty{9}{\dBm}$? Entrambi i valori hanno unità di misura diverse! L'unità Bel ($\unit{\bel}$) o decibel ($\unit{\dB}$) è un'unità di misura ausiliaria (anche pseudounità).
In linea di principio, il valore numerico potrebbe anche essere scritto senza l'unità $\unit{\dB}$. Ma con l'indicazione $\unit{\dB}$ si chiarisce che si tratta di un rapporto logaritmico tra due grandezze. Senza questa unità, si dovrebbe descrivere verbalmente il significato del valore numerico.
</indepth>
  
Inoltre, nella classe E abbiamo già imparato le indicazioni aggiuntive $\unit{\dBd}$ e $\unit{\dBi}$, che vengono utilizzate nell'indicazione dei guadagni d'antenna. In questo caso, il valore in decibel non si riferisce a una potenza o tensione, ma a un particolare radiatore di riferimento. Comunemente si usano $\unit{\dBi}$, riferito al radiatore isotropo sferico, e $\unit{\dBd}$, riferito al dipolo a semionda.

---

Oltre ai rapporti di potenza, possiamo usare il decibel anche per indicare *rapporti di tensione* e *livelli di tensione*. Per fare ciò, possiamo usare la formula $P = \frac{U^2}{R}$. Quindi possiamo scrivere:

$\begin{split}g &= 10 \cdot \log_{10}\left(\frac{P_1}{P_2}\right)\\ &= 10 \cdot \log_{10}\left(\frac{\frac{U_1^2}{\cancel{R}}}{\frac{U_2^2}{\cancel{R}}}\right)\\ &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}ight)^2\right) \end{split}$

<tip>
*Calcoli con i logaritmi:*
Alcune semplici regole di calcolo consentono di risolvere problemi con i decibel senza calcolatrice.

* Il logaritmo del prodotto di due numeri è uguale alla somma dei logaritmi: $\log_{10}(a\cdot b) = \log_{10}(a)+ \log_{10}(b)$
* Il logaritmo di una divisione di due numeri è uguale alla differenza dei logaritmi: $\log_{10}(a / b) = \log_{10}(a) - \log_{10}(b)$
* Il logaritmo di un numero al quadrato: $\log_{10}(x^2)= 2 \cdot \log_{10}(x)$
* Il logaritmo di una radice: $\log_{10}(\sqrt{x})= \frac{1}{2} \cdot \log_{10}(x)$
</tip>

Il logaritmo di un numero al quadrato è uguale al doppio del logaritmo del numero:

$\log_{10}(x^2)=2 \cdot \log_{10}(x)$

Ne consegue:

$\begin{split} g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}ight)^2\right)\\ &= 10 \cdot 2 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \\ &= 20 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \end{split}$

---

Pertanto, calcoliamo un rapporto *$a$* di due tensioni $U_1$ e $U_2$ moltiplicando il logaritmo del rapporto non per il fattore 10, ma per il fattore 20. Troviamo anche questa formula nella raccolta di formule.

[question:AA111]

<attention>
Nel calcolo in decibel, prestare sempre attenzione se si tratta di rapporti di potenza o di tensione!
</attention>

Per determinare i livelli di tensione, dobbiamo prima stabilire una tensione di riferimento (cfr. tabella [ref:a_bezugsgroessen]). Nei segnali ricevuti, misuriamo volentieri le tensioni (molto piccole) all'ingresso del ricevitore in $\unit{\micro\volt}$. Il livello di tensione associato ha quindi l'unità $\unit{\dBuV}$. Esempio:

$\qty{10}{\micro\volt} \rightarrow 20 \cdot \log_{10}\left(\frac{\qty{10}{\micro\volt}}{\qty{1}{\micro\volt}}\right)=\qty{20}{\dBuV}$

---

Nella seguente domanda, il valore di riferimento è $\qty{1}{\micro\volt\per\meter}$. Prova a risolvere il problema con le tue conoscenze.

<attention>
Attenzione, qui si intende $\unit{\dB(\micro\volt\per\meter)}$ e non $\unit{(\dB\micro\volt)/\meter}$!
</attention>

[question:AA112]

<tip>
Anche con le tensioni si può calcolare molto a mente utilizzando la tabella dalla raccolta di formule:

| c:dB | c:≈ Rapporto di tensione |
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

* Quanti $\unit{\dB}$ corrisponde un rapporto di tensione di 4? $4 = 2 \cdot 2 \rightarrow \qty{6}{\dB} + \qty{6}{\dB} = \qty{12}{\dB}$
</tip>