Abbiamo già conosciuto alcune forme di antenne. Ora discuteremo più in dettaglio le proprietà delle diverse antenne. I dipoli alimentati al centro sono antenne *simmetriche*. Per antenna simmetrica si intende un'antenna che, in condizioni ideali, presenta in funzione ai due poli (ad esempio, i punti di alimentazione di ciascun braccio di un dipolo) la stessa tensione rispetto alla terra, a parte il segno. Questo è il caso dei dipoli, incluso il dipolo ripiegato e anche le antenne Yagi-Uda basate su di essi. Un'antenna Groundplane, invece, presenta idealmente un potenziale di terra nel punto di connessione dei radiali (quindi una tensione di zero rispetto alla terra) e non è quindi considerata un'antenna simmetrica.

<indepth>
Anche per i cavi di trasmissione del segnale, ad esempio la linea di alimentazione di un'antenna, si distingue tra cavi *simmetrici e asimmetrici*. Anche qui, la simmetria si riferisce alle tensioni elettriche rispetto alla terra che prevalgono in condizioni ideali. In un cavo coassiale, le correnti dovrebbero essere simmetriche, ma solo il conduttore interno dovrebbe portare tensione rispetto alla terra. I cavi coassiali appartengono quindi alle linee di alimentazione asimmetriche. Come impareremo più avanti, queste linee di alimentazione asimmetriche dovrebbero essere collegate a un'antenna simmetrica solo tramite un cosiddetto elemento di simmetria (balun).
</indepth>

[question:EG213]

---

Una popolare forma di costruzione di antenne è un filo lungo circa una lunghezza d'onda totale, a forma di cerchio, quadrato, triangolo o altra forma simile. Si parla quindi di cosiddette *antenne a loop a onda intera*. A causa della loro semplice struttura, la cosiddetta antenna Delta-Loop, che, come la grande Delta (Δ) dell'alfabeto greco, ha la forma di un triangolo, è molto popolare.

<margin>
[picture:311:e_delta_loop:Esempio di antenna Delta-Loop]
</margin>

[question:EG101]

<indepth>
La *forma* esatta non è importante per le antenne a loop a onda intera, purché la lunghezza del filo corrisponda circa a una lunghezza d'onda. A seconda della forma, tuttavia, possono risultare resistenze di alimentazione diverse o guadagni d'antenna leggermente migliori o peggiori.
</indepth>

---

Dalle antenne a loop a onda intera si distinguono le cosiddette *antenne ad anello magnetico* (Magnetic-Loops), che hanno dimensioni molto più piccole rispetto alla lunghezza d'onda e generano un campo magnetico vicino (cfr. figura [ref:e_mag_loop]).

<margin>
[picture:977:e_mag_loop:Esempio di antenna Magnetic-Loop]
</margin>

[question:EG105]

<indepth>
Sebbene tali antenne ad anello magnetico siano fondamentalmente adatte anche per la trasmissione, è difficile ottenere un alto *rendimento*. Rendimenti tra $\qty{1}{\percent}$ e $\qty{10}{\percent}$ sono comuni per le antenne magnetiche in trasmissione. Tuttavia, questi Magnetic-Loops possono offrire vantaggi rispetto ad altre antenne: oltre alla struttura compatta, spesso interferiscono meno con oggetti conduttivi o attenuanti vicini, ad esempio muri o tegole, se montati all'interno o sotto un tetto.
</indepth>

---

Le antenne alimentate da un'estremità vengono alimentate da un'estremità. Di solito la loro lunghezza è pari a mezza lunghezza d'onda. Si parla quindi anche di dipolo a semionda alimentato all'estremità (inglese: end fed half wave, EFHW). Un'antenna del genere richiede una tensione notevolmente più alta rispetto alla corrente, che può essere generata da un circuito di adattamento appropriato, ad esempio un circuito Fuchs. I dipoli a semionda alimentati all'estremità, adattati con un circuito Fuchs, sono quindi chiamati antenne Fuchs.

[question:EG104]
[question:EG103]

<margin>
[picture:310:e_fuchsantenne:Esempio di antenna Fuchs]
</margin>

<person>
Il circuito Fuchs o l'antenna Fuchs prende il nome dal *Dr. Josef Fuchs* (nominativi radioamatoriali OE1JF, UO1JF ed EAAA), che lo brevettò nel 1927.
</person>

<indepth>
Anche un'antenna alimentata all'estremità necessita di un *contrappeso*, ad esempio sotto forma di un filo $\lambda / 4$ o di un'altra forma di messa a terra HF. Tuttavia, le correnti che si verificano negli EFHW al punto di alimentazione sono significativamente inferiori, motivo per cui anche una messa a terra meno efficace può essere sufficiente, ad esempio un breve capo di filo di solo un decimo o addirittura un ventesimo della lunghezza d'onda. A volte, solo lo schermo della linea di alimentazione o altri elementi metallici (originariamente destinati ad altri scopi) fungono da messa a terra.

Da non confondere con i dipoli a semionda alimentati all'estremità sono le *antenne a filo lungo* alimentate all'estremità, la cui lunghezza è significativamente superiore a una lunghezza d'onda. La confusione deriva dal fatto che i dipoli a semionda alimentati all'estremità vengono spesso utilizzati anche a frequenze più elevate, il che li rende di fatto antenne a filo lungo per queste frequenze.
</indepth>

---

La direttività di un'antenna può essere rappresentata in un cosiddetto diagramma di radiazione. In questo caso, per un piano, il guadagno, l'intensità di campo o la potenza di radiazione vengono rappresentati in ogni direzione. Più il grafico si allontana dal centro, maggiore è il guadagno, o maggiore è l'intensità di campo e la potenza di radiazione nel campo lontano. Se non viene utilizzata una scala con angoli, spesso viene rappresentata anche la disposizione meccanica dell'antenna nello stesso diagramma, per chiarire quale direzione nel diagramma corrisponde a quale direzione rispetto alla disposizione dell'antenna.

Un dipolo non irradia nella direzione del filo, come si potrebbe erroneamente supporre, ma perpendicolarmente ad esso. Visto in un piano e rappresentato come diagramma di radiazione, si ottengono lobi corrispondenti (ad esempio, a sinistra e a destra) accanto al dipolo (cfr. figura [ref:e_dipol_strahlungsdiagramm]). Un dipolo sospeso verticalmente irradia quindi, ad esempio, a sinistra e a destra, nonché davanti e dietro. Poiché il diagramma di radiazione considera solo un piano, si vedono ad esempio solo un lobo per l'irradiazione a sinistra e un lobo per l'irradiazione a destra. A seconda della scala, questi lobi possono apparire circolari.

<margin>
[picture:1045:e_dipol_strahlungsdiagramm:Esempio di irradiazione del dipolo]
</margin>

<indepth>
Un *lobo circolare* in sezione trasversale si ottiene con una scala lineare rispetto all'intensità di campo, quando si considera un dipolo fortemente accorciato (dipolo di Hertz). Un dipolo a semionda ha in realtà un guadagno leggermente superiore, corrispondente a un lobo leggermente più stretto. Tuttavia, nelle domande d'esame troviamo una rappresentazione circolare che è solo approssimativamente corretta. Con una scala lineare rispetto alla potenza di radiazione nella rispettiva direzione, il lobo dovrebbe essere ancora più stretto.
% TODO: eventualmente correggere l'immagine delle domande
</indepth>

[question:EG215]
[question:EG214]

---

Grazie alla caratteristica di irradiazione perpendicolare al dipolo, un dipolo a semionda montato verticalmente può consentire un'irradiazione piatta, che può essere desiderata, ad esempio, nelle operazioni DX, ma anche nei contatti tramite onda diretta o onda di terra.

[question:EG219]

<margin>
[photo:316:e_vertikaldipol:Dipolo a $\frac{\lambda}{2}$ verticale]
</margin>

---

Un caso speciale di antenna verticale è l'antenna $5/8 \lambda$ eccitata rispetto alla terra (o alla carrozzeria di un veicolo) (cfr. figura [ref:e_fuenf_achtel]). Qui la lunghezza è scelta in modo tale da ottenere un guadagno ottimale.

[question:EG108]

<margin>
[picture:650:e_fuenf_achtel:Antenna $5/8 \lambda$]
</margin>

---

Anche un'antenna Groundplane irradia perpendicolarmente al radiatore (non ai radiali). Poiché il diagramma di radiazione considera spesso l'antenna Groundplane dall'alto, si ottiene quasi un'antenna omnidirezionale, che presenta quasi lo stesso guadagno in tutte le direzioni (cfr. figura [ref:e_ground_plane_abstrahlung]). I radiali hanno solo una piccola influenza e possono leggermente "deformare" il diagramma di radiazione, il che corrisponde a un guadagno leggermente diverso in determinate direzioni.

<margin>
[picture:1046:e_ground_plane_abstrahlung:Irradiazione antenna Groundplane]
</margin>

[question:EG216]

<indepth>
Anche se il diagramma di radiazione di un'antenna Groundplane con radiali è leggermente *"deformato"*, questa deviazione è in teoria molto più piccola di quanto spesso rappresentato. Pertanto, un'antenna Groundplane è effettivamente un'antenna omnidirezionale quasi ideale nel piano.
</indepth>

---

Le antenne direttive (ad esempio, l'antenna Yagi-Uda) si caratterizzano per il fatto che il guadagno in una direzione è significativamente maggiore che in altre direzioni, come mostrato nella figura [ref:e_richtantenne_abstrahlung].

[question:EG217]

<margin>
[picture:1047:e_richtantenne_abstrahlung:Irradiazione antenna direttiva]
</margin>

---

A frequenze più elevate, ad esempio nella gamma UHF o superiori, vengono utilizzati anche tromboni o antenne paraboliche (cfr. [ref:e_parabolantenne]). Anche le antenne patch si trovano su circuiti stampati di piccoli apparecchi. Tutte queste forme di antenne sono insolite per la gamma delle onde corte, poiché raggiungerebbero dimensioni ingombranti. Pertanto, per le seguenti domande rimangono solo antenne a filo lungo, antenne Yagi-Uda, antenne dipolo, antenne Windom, antenne Delta-Loop.

[question:EG106]

<margin>
[picture:850:e_parabolantenne:Antenna parabolica]
</margin>

L'antenna a trappola consiste in un trappola lunga $\lambda / 4$, che funge da elemento di simmetria o da blocco per le onde di corrente di modo comune. Con queste conoscenze è possibile rispondere alla seguente domanda, poiché sia una trappola che una Yagi-Uda a croce sarebbero ingombranti nella banda degli $\qty{80}{\meter}$, così come gli specchi parabolici.

[question:EG107]
