Per stabilire un collegamento radio tra due luoghi tramite l'onda spaziale, deve essere scelta una frequenza che venga rifratta in modo affidabile dalla ionosfera verso la terra. Di solito questo non riguarda una singola frequenza, ma un'intera banda di frequenza. Spesso si sceglie la più alta banda radioamatoriale all'interno di questo intervallo.

Questa banda di frequenza è limitata superiormente dalla *MUF* (*maximal usable frequency*), cioè la frequenza più alta che la ionosfera può ancora rifrangere per la distanza tra trasmettitore e ricevitore.

[question:EH204]

La MUF dipende dalla densità degli elettroni liberi nella regione di rifrazione (qui: regione F2) e dall'angolo di incidenza dell'onda radio nella ionosfera. La figura [ref:e_muf_luf] mostra la previsione della MUF per una giornata estiva nel luglio 2025. Si vede chiaramente che la MUF dipende dall'ora del giorno: durante il giorno, la ionizzazione più forte porta a una MUF più alta, di notte la ionizzazione diminuisce e la MUF scende di conseguenza. Un altro esempio è mostrato nella figura [ref:e_muf_luf2]. La MUF qui è di circa $\qty{7,5}{\mega\hertz}$. Ciò significa che le frequenze $\qty{3,5}{\mega\hertz}$ e $\qty{7}{\mega\hertz}$ vengono ancora rifratte verso la terra, mentre le frequenze superiori a $\qty{7,5}{\mega\hertz}$ vengono deviate verso lo spazio. Questo è anche il motivo per cui comunichiamo con la stazione spaziale ISS nella banda dei $\qty{2}{\meter}$: con $\qty{145,800}{\mega\hertz}$ siamo ben al di sopra di una tipica MUF.

<margin>
[picture:991:e_muf_luf:Previsione di MUF e LUF nel luglio 2025]
</margin>

<margin>
[picture:997:e_muf_luf2:Simulazione delle distanze di salto per diverse frequenze e una MUF di ca. $\qty{7,5}{\mega\hertz}$ in una notte di agosto 2024 con un angolo di irradiazione di $\qty{45}{\degree}$]
</margin>

Le relazioni esatte della MUF, ad esempio in relazione all'angolo di irradiazione, saranno trattate solo nel materiale per HB9. Per HB3 è importante sapere:

*Più forte è la ionizzazione della ionosfera, più alta è in genere anche la MUF.*

[question:EH207]
[question:EH206]

Lo strato D lo abbiamo già conosciuto nel capitolo Ionosfera II. Da esso viene determinata un'altra frequenza di taglio – la cosiddetta LUF (Lowest Usable Frequency), cioè la frequenza più bassa utilizzabile, al di sotto della quale l'attenuazione è troppo forte.
Verso il basso, la LUF rappresenta quindi la limitazione. È determinata principalmente dalla ionizzazione nello *strato D*, ma dipende anche dall'attrezzatura (potenza di trasmissione, antenne, sensibilità del ricevitore).

[question:EH209]

In particolare, con un'attività solare molto bassa o durante forti tempeste magnetiche, può verificarsi il caso speciale che per un determinato percorso del segnale la LUF sia superiore alla MUF. In questo caso, tra i luoghi interessati non è possibile alcun traffico radio tramite l'onda spaziale. La figura [ref:e_muf_luf] mostra anche una previsione della LUF per luglio 2025. Lì si vede chiaramente che tra le 6 e le 12 la LUF è al di sopra della MUF e quindi non è possibile alcuna operazione in onde corte.

Per la propagazione delle onde corte attraverso la ionosfera, due frequenze di taglio sono particolarmente importanti: la *LUF (Lowest Usable Frequency)* e la *MUF (Maximum Usable Frequency)*. Tra questi due valori, un collegamento radio attraverso la ionosfera è fondamentalmente possibile.

La *LUF (Lowest Usable Frequency)* indica la frequenza più bassa alla quale una connessione su un determinato percorso radio è ancora possibile con una qualità del segnale sufficiente. La LUF dipende dalla potenza: se la potenza di trasmissione viene aumentata, un segnale più attenuato può comunque raggiungere il ricevitore con un'intensità di campo sufficiente. Ciò abbassa la LUF, rendendo utilizzabili anche frequenze più basse.

[question:EH220]

La *MUF (Maximum Usable Frequency)* indica invece la frequenza più alta che su una determinata distanza e in un determinato momento viene ancora rifratta dalla ionosfera verso la terra. Al di sopra della MUF, l'onda radio non viene più rifratta sufficientemente e penetra la ionosfera nello spazio. La MUF non dipende dalla potenza di trasmissione.

[question:EH221]

Nota: Le basi fisiche della ionosfera e dei suoi strati (strato D, E, F1 e F2) sono trattate più approfonditamente nelle sezioni corrispondenti [sec:ionosphaere_3], [sec:tote_zone_2], [sec:sprungdistanz_2] e [sec:muf_luf_2] sulla ionosfera per HB9. Qui è sufficiente comprendere che la LUF può essere influenzata dall'intensità del segnale, mentre la MUF è determinata esclusivamente dalle condizioni di propagazione della ionosfera.

