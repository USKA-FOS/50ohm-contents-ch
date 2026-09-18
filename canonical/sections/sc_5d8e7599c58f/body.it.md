Come abbiamo imparato in precedenza, gli apparecchi radioamatoriali e le linee di alimentazione comunemente utilizzate nel radioamatoriale hanno solitamente un’impedenza caratteristica di $\qty{50}{\ohm}$. Abbiamo anche imparato che, nei punti di connessione delle linee di alimentazione, si verificano riflessioni indesiderate se l’impedenza caratteristica non corrisponde.

Anche le antenne hanno una proprietà simile all’impedenza caratteristica, che dipende dall’esatta disposizione degli elementi dell’antenna. Questa proprietà è chiamata impedenza di alimentazione o impedenza al punto di alimentazione. Come nel caso della connessione di due linee di alimentazione con impedenza caratteristica diversa, vale anche qui: se l’impedenza di alimentazione dell’antenna non corrisponde all’impedenza caratteristica della linea di alimentazione, si verificano riflessioni indesiderate. Una parte della potenza di trasmissione viene riflessa verso l’apparecchio radio e non può essere irradiata dall’antenna.

Se, invece, l’impedenza di alimentazione dell’antenna e l’impedenza caratteristica della linea di alimentazione corrispondono e, quindi, è garantita una trasmissione ottimale della potenza di trasmissione all’antenna, si parla di *adattamento*.

<margin>
[photo:144:swr_meter:Un semplice rosmetro per determinare il rapporto d’onda stazionaria]
</margin>

La qualità dell’adattamento dell’antenna può essere misurata. In modo semplificato, si determina quanta potenza di trasmissione viene riflessa dall’antenna. Il valore misurato visualizzato dallo strumento di misura viene chiamato *rapporto d’onda stazionaria*. Spesso si utilizza l’abbreviazione SWR, derivata dall’inglese "standing wave ratio". Per determinare il SWR si utilizza un *misuratore di ROS*, detto brevemente *rosmetro*.

% TODO: Specifico per l’edizione
<indepth>
Un rosmetro misura contemporaneamente la potenza di trasmissione incidente, inviata dal trasmettitore all’antenna, e la potenza riflessa. Questo può essere osservato chiaramente nel rosmetro mostrato nella figura [ref:swr_meter_kreuzzeiger], che visualizza separatamente la potenza incidente e quella riflessa. Tuttavia, il SWR non indica direttamente il rapporto tra questi due valori di misura, ma viene calcolato in modo più complesso come $\text{SWR} = \frac {\sqrt{P_\text{I}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{I}}-\sqrt{P_\text{R}}}$, dove $P_\text{I}$ è la potenza incidente e $P_\text{R}$ è la potenza riflessa.
</indepth>

<margin>
[photo:143:swr_meter_kreuzzeiger:Rosmetro con indice a croce: l’indice di sinistra indica la potenza incidente, quello di destra la potenza riflessa; per leggere il SWR, si segue la linea verde fino al punto di intersezione dei due indici verso il basso]
</margin>

[question:NI201]

---

<margin>
[photo:67:n_swr_display:Display di un trasmettitore-ricevitore]
</margin>

I moderni trasmettitori-ricevitori hanno già un rosmetro integrato. La visualizzazione si trova solitamente nel display, come mostrato in [ref:n_swr_display].

<attention>
Rosmetro e S-metro sembrano simili, ma sono diversi: il rosmetro misura il rapporto d’onda stazionaria durante la trasmissione, mentre l’S-metro misura l’intensità del segnale durante la ricezione.
</attention>

% TODO Big Picture: Nel display Trx_Display contrassegnare "SWR"
[question:NF101]

---

Se un trasmettitore-ricevitore non ha un rosmetro integrato, è possibile utilizzare un rosmetro esterno. Questo viene collegato tra l’apparecchio radio e l’antenna, come mostrato nella figura [ref:n_trx_kabel_swr_antenne]. Si dice anche: "Il rosmetro viene inserito tra trasmettitore-ricevitore e antenna".

[question:NI202]

Se un’antenna è perfettamente adattata alla linea di alimentazione (ad esempio, al cavo coassiale), il rosmetro indica un valore di $\num{1}$. Questo è il valore migliore possibile. In questo caso, l’antenna assorbe tutta la potenza e non viene riflessa alcuna potenza verso il trasmettitore.

<margin>
[picture:670:n_trx_kabel_swr_antenne:Schema di principio di un rosmetro tra trasmettitore-ricevitore e antenna]
</margin>

[question:NG301]
[question:NI203]

---

Se al trasmettitore-ricevitore non è collegata alcuna antenna o se la linea di alimentazione è interrotta o in corto circuito, il valore SWR è quasi infinito ($\infty$). Un cavo aperto o in corto circuito riflette infatti completamente la potenza di trasmissione. Nel peggiore dei casi, ciò può addirittura danneggiare il trasmettitore nell’apparecchio radio.

<indepth>
Oltre ai due valori SWR $\num{1}$ e infinito ($\infty$), sono particolarmente significativi anche i valori $\num{2}$ e $\num{3}$. Con un valore SWR di $\num{2}$, il $\qty{11}{\percent}$ della potenza di trasmissione viene riflesso verso il trasmettitore, mentre con un valore SWR di $\num{3}$, il $\qty{25}{\percent}$ della potenza di trasmissione viene riflesso. Nei trasmettitori-ricevitori moderni, per prevenire danni al trasmettitore, la potenza di trasmissione viene automaticamente ridotta nell’apparecchio radio.
</indepth>

Un valore SWR molto elevato, ad esempio vicino all’infinito, può essere ottenuto anche in caso di un adattamento molto scarso dell’antenna o se la linea di alimentazione è danneggiata.

[question:NG302]
[question:NG303]

Se a un apparecchio radio con rosmetro è collegata un’antenna con un adattamento scarso tramite un lungo cavo coassiale, il valore SWR visualizzato può essere notevolmente migliore di quanto ci si aspetterebbe in base allo scarso adattamento. La causa di ciò è l’elevata attenuazione del cavo, che riduce non solo il segnale diretto verso l’antenna, ma anche quello riflesso.

[question:NG208]