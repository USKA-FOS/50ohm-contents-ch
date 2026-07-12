Come abbiamo appreso in precedenza, gli apparecchi radioamatoriali e le linee di trasmissione comunemente utilizzate nel radioamatore utilizzano generalmente un'impedenza caratteristica di $\qty{50}{\ohm}$. Abbiamo anche appreso che nei punti di connessione delle linee di trasmissione si verificano riflessioni indesiderate se l'impedenza caratteristica non corrisponde.

Anche le antenne hanno una proprietà simile all'impedenza caratteristica, che dipende dalla disposizione esatta degli elementi dell'antenna. Questa proprietà è chiamata impedenza di alimentazione o di punto di alimentazione. Come nella connessione di due linee di trasmissione con diversa impedenza caratteristica, vale anche qui: se l'impedenza di alimentazione dell'antenna non corrisponde all'impedenza caratteristica della linea di alimentazione, si verificano riflessioni indesiderate. Una parte della potenza di trasmissione viene riflessa all'apparecchio radio e non può essere irradiata dall'antenna.

Se, d'altra parte, l'impedenza di alimentazione dell'antenna e l'impedenza caratteristica della linea di alimentazione corrispondono, garantendo così una trasmissione ottimale della potenza di trasmissione all'antenna, si parla di *adattamento*.

<margin>
[photo:144:swr_meter:Un semplice misuratore SWR per determinare il rapporto d'onda stazionaria]
</margin>

Quanto sia buono l'adattamento dell'antenna può essere misurato. In parole povere, si determina quanta potenza di trasmissione viene riflessa dall'antenna. Il valore misurato visualizzato dallo strumento di misura è chiamato *rapporto d’onda stazionaria*. Di solito si utilizza l'abbreviazione SWR, derivata dal termine inglese "standing wave ratio". Per determinare l'SWR si utilizza un *misuratore di onde stazionarie*, in breve chiamato *SWR-meter*.

% TODO: Rendere specifico per l'edizione
<indepth>
Un misuratore SWR misura contemporaneamente la potenza di trasmissione in avanti che il trasmettitore invia all'antenna e la potenza riflessa che è stata riflessa. Ciò è chiaramente visibile sul misuratore SWR nella figura [ref:swr_meter_kreuzzeiger], che visualizza separatamente la potenza in avanti e quella riflessa. Tuttavia, l'SWR non indica direttamente il rapporto tra questi due valori misurati, ma viene determinato in modo leggermente più complesso come $\text{SWR} = \frac {\sqrt{P_\text{V}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{V}}-\sqrt{P_\text{R}}}$, dove $P_\text{V}$ è la potenza in avanti e $P_\text{R}$ è la potenza riflessa. Per l'esame della classe N, non è necessario conoscere questa formula.
</indepth>

<margin>
[photo:143:swr_meter_kreuzzeiger:Misuratore SWR con indicatore a croce, indicatore sinistro per la potenza in avanti e indicatore destro per la potenza riflessa; per leggere l'SWR, si segue la linea verde verso il basso all'incrocio dei due indicatori]
</margin>

[question:NI201]

---

<margin>
[photo:67:n_swr_display:Display di un trasmettitore-ricevitore]
</margin>

I trasmettitore-ricevitore moderni hanno già un misuratore SWR integrato. L'indicazione si trova solitamente nel display, vedi [ref:n_swr_display].

<attention>
I misuratori SWR e gli S-meter suonano simili, ma sono diversi: il misuratore SWR misura il rapporto d’onda stazionaria durante la trasmissione e l'S-meter misura la forza del segnale durante la ricezione.
</attention>

% TODO Immagine grande: Indicare "SWR" nel display del trasmettitore-ricevitore
[question:NF101] 

---

Se il trasmettitore-ricevitore non ha un misuratore SWR integrato, si può utilizzare anche un misuratore SWR esterno. Viene collegato tra l'apparecchio radio e l'antenna come mostrato nella figura [ref:n_trx_kabel_swr_antenne]. Si dice anche: "Il misuratore SWR viene inserito tra il trasmettitore-ricevitore e l'antenna".

[question:NI202]

Se un'antenna è perfettamente adattata alla linea di alimentazione (ad esempio, il cavo coassiale), il misuratore SWR indicherà un valore di $\num{1}$. Questo è il miglior valore ottenibile. Nessuna potenza viene riflessa nel trasmettitore.

<margin>
[picture:670:n_trx_kabel_swr_antenne:Schema del misuratore SWR tra trasmettitore-ricevitore e antenna]
</margin>

[question:NG301]
[question:NI203]

---

Se non è collegata alcuna antenna al trasmettitore-ricevitore o se la linea di trasmissione è interrotta o in corto circuito, il valore SWR è quasi infinito ($\infty$). Un cavo aperto o in corto circuito riflette completamente la potenza di trasmissione. Nel peggiore dei casi, ciò può persino danneggiare il trasmettitore nell'apparecchio radio.

<indepth>
Oltre ai due valori *SWR* $\num{1}$ e infinito ($\infty$), sono degni di nota anche i valori $\num{2}$ e $\num{3}$. Con un valore SWR di $\num{2}$, l'$\qty{11}{\percent}$ della potenza di trasmissione viene riflessa nel trasmettitore, con un valore SWR di $\num{3}$, il $\qty{25}{\percent}$. Nei trasmettitore-ricevitore moderni, si previene il danneggiamento del trasmettitore riducendo automaticamente la potenza di trasmissione nell'apparecchio radio.
</indepth>

Un SWR molto scarso, ad esempio vicino all'infinito, può anche verificarsi se l'adattamento dell'antenna è molto scarso o se la linea di trasmissione è danneggiata.

[question:NG302]
[question:NG303]

Se un'antenna con scarso adattamento è collegata a un apparecchio radio con un misuratore SWR tramite un lungo cavo coassiale, il valore SWR visualizzato può essere notevolmente migliore di quanto ci si aspetterebbe a causa del cattivo adattamento. La causa è un'elevata attenuazione del cavo, che riduce non solo il segnale che va all'antenna, ma anche quello riflesso.

[question:NG208]
