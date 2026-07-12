In molti ambiti della tecnica ad alta frequenza, i rapporti di potenza giocano un ruolo importante, ad esempio nel guadagno di un'antenna o di un amplificatore, o nell'attenuazione di un cavo. Nella classe N, abbiamo appreso queste relazioni ancora sotto forma di semplici fattori, ad esempio: "L'antenna ha un guadagno di fattore $2$.

Questi rapporti possono assumere valori numerici molto grandi o molto piccoli. Ad esempio, un ricevitore per onde corte ha un fattore di amplificazione totale di $\num{1000000000000}$, cioè un uno seguito da dodici zeri. Con numeri del genere, il calcolo diventa rapidamente confuso e si inizia inevitabilmente a contare gli zeri.

Detto in modo semplificato, esiste tuttavia uno strumento matematico di ausilio per questo "conteggio degli zeri": i logaritmi. Con il loro aiuto, le moltiplicazioni possono essere trasformate in addizioni e le divisioni in sottrazioni. Ciò rende molto semplice il calcolo con numeri grandi.

---

Si è quindi consolidata l'abitudine di indicare i rapporti di potenza su una scala logaritmica.
Il logaritmo è l'operazione inversa dell'elevamento a potenza. Nell'radioamatore, utilizziamo di solito il logaritmo decimale ("logaritmo in base dieci") con base $10$:

---

$a =\log_{10} (b)$, se $b=10^{a}$

Il logaritmo di $100$ è $\log_{10}(100)=2$, poiché $10^2 = 100$. In altre parole: il numero $100$ ha due zeri.

<warning>
Una calcolatrice scientifico-tecnica offre, oltre al logaritmo decimale (etichetta $\lg$ o $\log$), anche il logaritmo naturale *$\ln$*, che ha come base il numero di Eulero *$e=\num{2,7182818}\dots$*. Non confondere!
</warning>	

<margin>
| c:dB | c:≈ Fattore di potenza |
| $0$ | $1$ |
| $1,5$ | $\sqrt{2} = 1,41$ |
| $2,15$ | $1,64$ |
| $3$ | $2$ |
| $5$ | $\sqrt{10} = 3,16$ |
| $6$ | $4$ |
| $10$ | $10$ |
| $20$ | $100$ |
[table:e_dezibel_leistungsfaktoren:Fattori di potenza importanti in $\unit{\dB}$]
</margin>

Dal logaritmo decimale deriva il *Bel* ($\unit{\bel}$). Il nome onora l'insegnante americano per sordi e pioniere del telefono, *Alexander Graham Bell*. Nell'esempio precedente, avremmo anche potuto scrivere:

$\log_{10}(b)=\qty{a}{\bel}$

Di solito, invece del Bel, si usa il *decibel* (simbolo dell'unità $\unit{\dB}$), cioè la decima parte di un Bel:

$10 \cdot \log_{10}(b) = \qty{a}{\dB}$

---

La raccolta di formule indica per la conversione di un rapporto di potenza la seguente formula:

$g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$

Dove $P_1$ corrisponde alla potenza d'ingresso e $P_2$ alla potenza d'uscita. Supponiamo ora di avere un amplificatore che amplifica la potenza d'ingresso $P_1=\qty{50}{\watt}$ a $P_2=\qty{100}{\watt}$, cioè la raddoppia. Secondo la nostra formula, il fattore di amplificazione in $\unit{\dB}$ risulta:

$g = 10\cdot \log_{10}\left(\frac{\qty{100}{\watt}}{\qty{50}{\watt}}\right)\unit{\dB} = 10\cdot \log_{10}\left(2\right)\unit{\dB} = 10\cdot \qty{0.301}{\dB} \approx \qty{3}{\dB} $

Per la classe E è inizialmente sufficiente conoscere il valore in decibel per il fattore di potenza $2$. La raccolta di formule contiene a tal proposito una tabella, che è riportata anche nella tabella [ref:e_dezibel_leistungsfaktoren]. Da essa si può leggere che un fattore di potenza di $2$ corrisponde a un valore in decibel di $\qty{3}{\dB}$. Il calcolo dettagliato con i valori in decibel verrà trattato solo nella classe A.

<tip>
Senza calcolatrice si possono stimare i valori in decibel che terminano con "$0$": basta coprire l'ultimo zero, la cifra indica quindi il numero di zeri del fattore di rapporto. Esempio: $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zeri} \rightarrow \text{fattore di rapporto}~1000$!
</tip>

[question:EA107]

Oltre all'unità $\unit{dB}$, nella pratica si incontrano spesso anche indicazioni come $\unit{\dBi}$, $\unit{\dBm}$, $\unit{\dBW}$ o $\unit{\dBu}$. Queste aggiunte indicano rispetto a quale grandezza di riferimento si riferisce il rispettivo valore in decibel. Nella classe E, in particolare per le antenne, incontreremo le indicazioni $\unit{\dBi}$ e $\unit{\dBd}$ nel capitolo sulle antenne. Le altre grandezze come $\unit{\dBm}$ e $\unit{\dBW}$ saranno necessarie solo per la classe A.