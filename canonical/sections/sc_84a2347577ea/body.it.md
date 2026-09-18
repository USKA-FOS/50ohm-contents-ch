In molti ambiti della tecnica delle alte frequenze, i rapporti di potenza giocano un ruolo importante, ad esempio nel guadagno di un'antenna o di un amplificatore, oppure nell'attenuazione di un cavo. Finora abbiamo conosciuto questi rapporti sotto forma di semplici fattori, ad esempio: "L'antenna ha un guadagno di fattore $2$".

Questi rapporti possono assumere valori numerici molto grandi o molto piccoli. Ad esempio, un ricevitore per onde corte possiede un fattore di amplificazione totale di $\num{1000000000000}$, cioè un uno seguito da dodici zeri. Lavorare con numeri del genere diventa rapidamente complicato e si finisce inevitabilmente per contare gli zeri.

In realtà, esiste però uno strumento matematico che semplifica questo "contare gli zeri": i logaritmi. Essi permettono di trasformare le moltiplicazioni in addizioni e le divisioni in sottrazioni, rendendo molto più semplice il calcolo con numeri grandi.

---

Per questo motivo, è consuetudine esprimere i rapporti di potenza su una scala logaritmica.
Il logaritmo è l'operazione inversa dell'elevamento a potenza. Nel radioamatoriale si utilizza di norma il logaritmo decimale ("logaritmo in base 10"):

---

a = \log_{10} (b), se b=10^{a}

Il logaritmo di $100$ è $\log_{10}(100)=2$, poiché $10^2 = 100$. In altre parole: il numero $100$ ha due zeri.

<warning>
Una calcolatrice scientifica offre, oltre al logaritmo decimale (etichettato come $\lg$ o $\log$), anche il logaritmo naturale *$\ln$*, che ha come base il numero di Eulero *$e=\num{2,7182818}\dots$*. Non confonderli!
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

Dal logaritmo decimale deriva il *Bel* ($\unit{\bel}$), così chiamato in onore dell'insegnante statunitense di sordomuti e pioniere del telefono, *Alexander Graham Bell*. Nell'esempio precedente avremmo potuto scrivere anche:

$\log_{10}(b)=\qty{a}{\bel}$

Di norma, però, si utilizza il *decibel* (simbolo $\unit{\dB}$), cioè la decima parte di un Bel:

$10 \cdot \log_{10}(b) = \qty{a}{\dB}$

---

La raccolta di formule fornisce la seguente formula per convertire un rapporto di potenza:

g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}

Dove $P_1$ corrisponde alla potenza d’ingresso e $P_2$ alla potenza d’uscita. Supponiamo ora di avere un amplificatore che porta la potenza d’ingresso $P_1=\qty{50}{\watt}$ a $P_2=\qty{100}{\watt}$, cioè la raddoppia. Applicando la formula otteniamo il seguente fattore di amplificazione in $\unit{\dB}$:

g = 10\cdot \log_{10}\left(\frac{\qty{100}{\watt}}{\qty{50}{\watt}}\right)\unit{\dB} = 10\cdot \log_{10}\left(2\right)\unit{\dB} = 10\cdot \qty{0.301}{\dB} \approx \qty{3}{\dB}

Per HB3 è sufficiente conoscere inizialmente il valore in decibel per il fattore di potenza $2$. La raccolta di formule contiene una tabella che è anche rappresentata nella Tabella [ref:e_dezibel_leistungsfaktoren]. Da essa si può dedurre che un fattore di potenza di $2$ corrisponde a un valore di $\qty{3}{\dB}$. Il calcolo dettagliato con i valori in decibel viene affrontato solo nella classe A.

<tip>
Senza calcolatrice, è possibile stimare i valori in decibel che terminano con "$0$": basta coprire l'ultimo zero, la cifra risultante indica il numero di zeri del fattore di rapporto. Esempio: $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zeri} \rightarrow \text{fattore di rapporto}~1000$!
</tip>

<indepth>
Alcuni altri valori in decibel possono essere stimati senza calcolatrice grazie alla seguente tabella:

| c:dB | l:Fattore | c:dB | l:Fattore |
| -3 | 0.5 | +3 | 2 |
| -6 | 0.25 | +6 | 4 |
| -10 | 1/10 | +10 | 10 |
| -20 | 1/100 | +20 | 100 |
| -30 | 1/1000 | +30 | 1000 |
[table:n_db_leistungsangaben:Valori in decibel (potenza) frequentemente utilizzati]
</indepth>

<tip>
Combinando i valori sopra riportati, è possibile stimare ulteriori valori senza calcolatrice.

| c:Fattore | c:dB | l:Derivazione |
| ×8 | 9 | 3+3+3 |
| ×20 | 13 | 10+3 |
| ×1/8 | -9 | -3-3-3 |
| ×50 | 17 | 20-3 |
| ×3 | 5 | approssimativamente |
| ×1.25 | 1 | 10-9 |
| ×1.5 | 2 | approssimativamente |
[table:n_db_beispiele:Esempi di dB]
</tip>

[question:EA107]

Oltre all’unità $\unit{dB}$, nella pratica si incontrano spesso anche indicazioni come $\unit{\dBi}$, $\unit{\dBm}$, $\unit{\dBW}$ o $\unit{\dBu}$. Questi suffissi indicano a quale grandezza di riferimento si riferisce il rispettivo valore in decibel. In particolare per le antenne, incontreremo le indicazioni $\unit{\dBi}$ e $\unit{\dBd}$ nel capitolo [sec:antennengewinn]. Le altre grandezze come $\unit{\dBm}$ e $\unit{\dBW}$ verranno trattate solo nel capitolo [sec:dezibel_2].