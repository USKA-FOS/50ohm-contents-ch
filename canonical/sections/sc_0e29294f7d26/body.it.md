% Il titolo del numero 14 è stato aperto (Il titolo è "Forme di antenna II". Tuttavia, non esiste un capitolo "Forme di antenna I")

Abbiamo già imparato a conoscere alcune forme di antenna. Ora vogliamo discutere più in dettaglio le proprietà delle diverse antenne. I dipoli alimentati al centro sono *antenne simmetriche*. Con il termine antenna simmetrica si intende un'antenna che, idealmente, durante il funzionamento presenta agli stessi poli (ad esempio, i punti di alimentazione di ogni ramo di un dipolo) la stessa tensione rispetto a terra, a meno del segno. Questo vale per i dipoli, inclusi il dipolo ripiegato e le antenne Yagi-Uda basate su di esso. Un'antenna Groundplane, invece, presenta al punto di connessione dei radiali idealmente il potenziale di terra (quindi una tensione pari a zero rispetto a terra) e quindi non rientra tra le antenne simmetriche.

<indepth>
Anche per i cavi utilizzati per la trasmissione del segnale, ad esempio la linea di alimentazione di un'antenna, si distingue tra *cavi simmetrici e asimmetrici*. Anche in questo caso la simmetria si riferisce alle tensioni elettriche ideali rispetto a terra. In un cavo coassiale, infatti, le correnti dovrebbero essere simmetriche, ma solo il conduttore interno presenta tensione rispetto a terra. I cavi coassiali appartengono quindi alle linee di alimentazione asimmetriche. Come impareremo in seguito, queste linee di alimentazione asimmetriche dovrebbero essere collegate a un'antenna simmetrica solo tramite un componente chiamato *simmetrizzatore* (Balun).
</indepth>

[question:EG213]

---

Una forma di antenna molto popolare è un filo lungo circa una lunghezza d’onda, disposto a cerchio, quadrato, triangolo o in una forma simile. Si parla quindi di cosiddette *antenne a loop a onda intera*. Molto popolare per la sua semplice struttura è la cosiddetta antenna Delta-Loop, che, come la lettera greca Delta (Δ) maiuscola, ha la forma di un triangolo.

<margin>
[picture:311:e_delta_loop:Esempio di antenna Delta-Loop]
</margin>

[question:EG101]

<indepth>
La *forma* esatta non è importante per le antenne a loop a onda intera, purché la lunghezza del filo corrisponda a circa una lunghezza d’onda. A seconda della forma, tuttavia, possono risultare resistenze di alimentazione diverse o guadagni dell’antenna leggermente migliori o peggiori.
</indepth>

---

Da distinguere dalle antenne a loop a onda intera sono le cosiddette *antenne magnetiche a loop* (Magnetic-Loops), che hanno dimensioni molto più piccole rispetto alla lunghezza d’onda e generano un campo magnetico vicino (cfr. figura [ref:e_mag_loop]).

<margin>
[picture:977:e_mag_loop:Esempio di antenna Magnetic-Loop]
</margin>

[question:EG105]

<indepth>
Sebbene tali antenne magnetiche a loop siano in linea di principio adatte anche per il funzionamento in trasmissione, è difficile ottenere un *rendimento* elevato. Nei sistemi di trasmissione con antenne magnetiche sono comuni rendimenti compresi tra $\qty{1}{\percent}$ e $\qty{10}{\percent}$. Tuttavia, queste Magnetic-Loops possono offrire vantaggi rispetto ad altre antenne: oltre alla struttura compatta, spesso interferiscono meno con oggetti conduttivi o attenuanti presenti nel campo vicino, ad esempio muri o tegole in caso di montaggio all’interno o sotto un tetto.
</indepth>

---

Le *antenne alimentate all’estremità* vengono alimentate da un’estremità. Di solito la loro lunghezza è pari a mezza lunghezza d’onda. Si parla quindi di dipolo a semionda alimentato all’estremità (in inglese: end fed half wave, EFHW). Tale antenna richiede una tensione notevolmente più alta rispetto alla corrente, che può essere generata da un adattatore appropriato, ad esempio un circuito di Fuchs. I dipoli a semionda alimentati all’estremità, adattati con un circuito di Fuchs, sono chiamati di conseguenza *antenne Fuchs*.

[question:EG104]
[question:EG103]

<margin>
[picture:310:e_fuchsantenne:Esempio di antenna Fuchs]
</margin>

<person>
Il circuito di Fuchs, o antenna Fuchs, prende il nome dal *Dr. Josef Fuchs* (nominativo radioamatoriale OE1JF, UO1JF ed EAAA), che lo brevettò anche nel 1927.
</person>

<indepth>
Anche un’antenna alimentata all’estremità necessita di un *contrappeso*, ad esempio sotto forma di un filo da $\lambda / 4$ o di un’altra forma di messa a terra RF. Tuttavia, le correnti che si verificano nei dipoli a semionda alimentati all’estremità al punto di alimentazione sono notevolmente inferiori, motivo per cui può essere sufficiente anche una messa a terra meno efficace, ad esempio un corto filo di appena un decimo o addirittura un ventesimo della lunghezza d’onda. A volte anche lo schermo della linea di alimentazione o altri elementi metallici (destinati ad altri scopi) fungono da messa a terra.

Non vanno confuse con i dipoli a semionda alimentati all’estremità le *antenne a filo lungo* alimentate all’estremità, la cui lunghezza supera notevolmente una lunghezza d’onda. La confusione deriva dal fatto che i dipoli a semionda alimentati all’estremità vengono spesso utilizzati anche su frequenze più elevate, diventando così di fatto un’antenna a filo lungo per tali frequenze.
</indepth>

---

La *direttività* di un’antenna può essere rappresentata in un cosiddetto diagramma di radiazione. In questo caso, per un piano, in ogni direzione viene tracciato il guadagno o l’intensità di campo o la potenza irradiata. Più il grafico si allontana dal punto centrale, maggiore è il guadagno o più elevata è l’intensità di campo e la potenza irradiata nel campo lontano. Se non viene utilizzata una scala angolare, spesso si rappresenta anche la disposizione meccanica dell’antenna nello stesso diagramma per chiarire quale direzione del diagramma corrisponde a quale direzione rispetto alla disposizione dell’antenna.

Un dipolo non irradia, come si potrebbe erroneamente pensare, nella direzione del filo, ma perpendicolarmente ad esso. Se si considera e si traccia un piano come diagramma di radiazione, si ottengono lobi corrispondenti (ad esempio a sinistra e a destra) accanto al dipolo (cfr. figura [ref:e_dipol_strahlungsdiagramm]). Un dipolo sospeso verticalmente irradia quindi, ad esempio, a sinistra e a destra e avanti e indietro. Poiché il diagramma di radiazione considera solo un piano, si vedono ad esempio solo un lobo per l’irradiazione a sinistra e un lobo per l’irradiazione a destra. A seconda della scala, questi lobi possono apparire circolari.

<margin>
[picture:1045:e_dipol_strahlungsdiagramm:Esempio di irradiazione del dipolo]
</margin>

<indepth>
Un *lobo circolare* nel profilo trasversale si ottiene con una scala lineare rispetto all’intensità di campo quando si considera un dipolo fortemente accorciato (dipolo hertziano). Un dipolo a semionda ha in realtà un guadagno leggermente superiore, corrispondente a un lobo leggermente più stretto. Tuttavia, nei quesiti d’esame si trova spesso una rappresentazione circolare che è solo approssimativa. Se la scala fosse lineare rispetto alla potenza irradiata nella rispettiva direzione, il lobo dovrebbe risultare ancora più stretto.
% TODO: ggf. Fragenbild korrigieren
</indepth>

[question:EG215]
[question:EG214]

---

Grazie alla caratteristica di irradiazione perpendicolare al dipolo, un dipolo a semionda montato verticalmente può consentire un’irradiazione piatta, che può essere desiderabile ad esempio nelle comunicazioni DX o nei contatti tramite onda diretta o onda di terra.

[question:EG219]

<margin>
[photo:316:e_vertikaldipol:Dipolo verticale da $\frac{\lambda}{2}$]
</margin>

---

Un caso speciale di antenna verticale è rappresentato dall’antenna $\frac{5}{8}\lambda$ eccitata rispetto a terra (o alla carrozzeria di un veicolo) (cfr. figura [ref:e_fuenf_achtel]). Qui la lunghezza, pari a $\qty{0.625}{\lambda}$, è stata scelta per un motivo preciso. Il radiatore è quindi meccanicamente circa 2,5 volte più lungo di una normale antenna Groundplane da $\frac{\lambda}{4}$ ($\qty{0.25}{\lambda}$). La maggiore lunghezza del radiatore modifica favorevolmente il diagramma di radiazione verticale, come mostrato nella figura [ref:a_5_8_lambda_strahlung]: una maggiore quantità della potenza irradiata viene concentrata verso l’orizzonte, mentre meno potenza viene irradiata verso l’alto o verso il basso. Questo comporta, in genere, una maggiore portata nelle comunicazioni terrestri con la stessa potenza. Una lunghezza del radiatore di circa $\frac{5}{8} \lambda$ è ottimale per questo effetto: se il radiatore viene ulteriormente allungato, una maggiore quantità di potenza viene nuovamente persa verso l’alto e verso il basso.

[question:EG108]

<margin>
[picture:1134:a_5_8_lambda_strahlung:Modello di radiazione e distribuzione della corrente di antenne verticali con terra ideale]
[picture:650:e_fuenf_achtel:Antenna $5/8 \lambda$]
</margin>

---

Anche un’antenna Groundplane irradia perpendicolarmente al radiatore (non ai radiali). Poiché il diagramma di radiazione dell’antenna Groundplane viene spesso osservato dall’alto, si ottiene un radiatore omnidirezionale che presenta un guadagno quasi identico in tutte le direzioni (cfr. figura [ref:e_ground_plane_abstrahlung]). I radiali hanno solo un’influenza minima e possono "deformare" leggermente il diagramma di radiazione, corrispondente a un guadagno leggermente diverso in determinate direzioni.

<margin>
[picture:1046:e_ground_plane_abstrahlung:Irradiazione antenna Groundplane]
</margin>

[question:EG216]

<indepth>
Sebbene il diagramma di radiazione di un’antenna Groundplane con radiali sia leggermente *"deformato"*, questa deviazione è molto più piccola nella teoria rispetto a quanto spesso rappresentato. Pertanto, un’antenna Groundplane è in realtà un radiatore quasi ideale in piano.
</indepth>

---

Le *antenne direzionali* (ad esempio l’antenna Yagi-Uda) si distinguono per il fatto che il guadagno in una direzione è notevolmente più elevato che in altre direzioni, come mostrato nella figura [ref:e_richtantenne_abstrahlung].

[question:EG217]

<margin>
[picture:1047:e_richtantenne_abstrahlung:Irradiazione antenna direzionale]
</margin>

---

A frequenze più elevate, ad esempio nella gamma delle UHF o superiori, vengono utilizzati anche radiatori a tromba o antenne paraboliche (cfr. [ref:e_parabolantenne]). Allo stesso modo, su schede più piccole di dispositivi si trovano antenne a patch. Tutte queste forme di antenna sono inusuali per la gamma delle onde corte, poiché raggiungerebbero dimensioni poco maneggevoli. Pertanto, per le domande successive rimangono solo l’antenna a filo lungo, l’antenna Yagi-Uda, il dipolo, l’antenna Windom e l’antenna Delta-Loop.

[question:EG106]

<margin>
[picture:850:e_parabolantenne:Antenna parabolica]
</margin>

L’antenna a manicotto è costituita da un contenitore lungo $\lambda / 4$ che funge da simmetrizzatore o induttanza di modo comune. Con questa conoscenza è possibile rispondere alla domanda successiva, poiché sia un manicotto che una Yagi-Uda a croce, così come un riflettore parabolico, sarebbero troppo ingombranti nella banda degli 80 metri.

[question:EG107]