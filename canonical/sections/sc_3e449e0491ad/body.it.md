Per stabilire un collegamento radio tra due località tramite onda spaziale, è necessario scegliere una frequenza che venga rifratta in modo affidabile dall’ionosfera verso la terra. In genere, ciò non riguarda una singola frequenza, ma un’intera banda di frequenza. Spesso si opta per la banda radioamatoriale più alta all’interno di questa gamma.

Questa banda di frequenza è limitata superiormente dalla *MUF* (*Maximum Usable Frequency*), cioè dalla frequenza massima che l’ionosfera può ancora rifrangere per la distanza tra trasmettitore e ricevitore.

[question:EH204]

La MUF dipende dalla densità degli elettroni liberi nella regione di rifrazione (in questo caso: regione F2) e dall’angolo di incidenza dell’onda radio nell’ionosfera. La figura [ref:e_muf_luf] mostra la previsione della MUF per una giornata estiva nel luglio 2025. Da essa emerge chiaramente che la MUF dipende dall’ora del giorno: di giorno, la maggiore ionizzazione porta a una MUF più alta, mentre di notte la ionizzazione diminuisce e la MUF si abbassa di conseguenza. Un altro esempio è mostrato nella figura [ref:e_muf_luf2]. Qui la MUF è di circa $\qty{7,5}{\mega\hertz}$. Ciò significa che le frequenze $\qty{3,5}{\mega\hertz}$ e $\qty{7}{\mega\hertz}$ vengono ancora riflesse verso la terra, mentre le frequenze superiori a $\qty{7,5}{\mega\hertz}$ vengono deviate verso lo spazio. Questo è anche il motivo per cui comunichiamo con la Stazione Spaziale Internazionale sulla banda dei $\qty{2}{\meter}$: con $\qty{145,800}{\mega\hertz}$ ci troviamo ben al di sopra di una MUF tipica.


<margin>
[picture:991:e_muf_luf:Previsione di MUF e LUF nel luglio 2025]
</margin>

<margin>
[picture:997:e_muf_luf2:Simulazione delle distanze di salto per diverse frequenze e una MUF di circa $\qty{7,5}{\mega\hertz}$ in una notte di agosto 2024 con un angolo di irradiazione di $\qty{45}{\degree}$]
</margin>

Le relazioni precise tra MUF, ad esempio in relazione all’angolo di irradiazione, verranno trattate solo nel corso per HB9. Per HB3 è importante sapere:


*Maggiore è la ionizzazione dell’ionosfera, maggiore è in genere anche la MUF.*


[question:EH207]
[question:EH206]


Lo strato D l’abbiamo già incontrato nel capitolo *Ionosfera II*. Da esso viene determinata un’ulteriore frequenza di taglio – la cosiddetta LUF (*Lowest Usable Frequency*), cioè la frequenza minima utilizzabile, al di sotto della quale l’attenuazione è troppo elevata.

Verso il basso, la LUF rappresenta quindi il limite. Essa è determinata principalmente dalla ionizzazione nella *regione D*, ma dipende anche dall’attrezzatura (potenza di trasmissione, antenne, sensibilità del ricevitore).


[question:EH209]


In particolare in caso di scarsa attività solare o durante forti tempeste magnetiche può verificarsi il caso speciale in cui, per un determinato percorso del segnale, la LUF superi la MUF. In questa situazione, tra i luoghi interessati non è possibile alcuna comunicazione radio tramite onda spaziale. La figura [ref:e_muf_luf] mostra anche una previsione della LUF per il luglio 2025. Qui si nota chiaramente che tra le 6 e le 12 la LUF è superiore alla MUF e quindi non è possibile operare in onde corte.

Per la propagazione delle onde corte tramite ionosfera, due frequenze di taglio sono particolarmente importanti: la *LUF (Lowest Usable Frequency)* e la *MUF (Maximum Usable Frequency)*. Tra questi due valori è generalmente possibile un collegamento radio tramite ionosfera.

La *LUF (Lowest Usable Frequency)* indica la frequenza minima alla quale un collegamento su una determinata tratta radio è ancora possibile con una qualità del segnale sufficiente. La LUF dipende dalla potenza: aumentando la potenza di trasmissione, un segnale più attenuato può comunque raggiungere il ricevitore con un’intensità di campo sufficiente. Di conseguenza, la LUF si abbassa e diventano utilizzabili anche frequenze più basse.

[question:EH220]


La *MUF (Maximum Usable Frequency)* indica invece la frequenza massima che, su una tratta determinata e in un momento specifico, viene ancora rifratta dall’ionosfera verso la terra. Al di sopra della MUF, l’onda radio non viene più rifratta a sufficienza e attraversa l’ionosfera dirigendosi verso lo spazio. La MUF non dipende dalla potenza di trasmissione.

[question:EH221]


Nota: Le basi fisiche dell’ionosfera e dei suoi strati (strato D, E, F1 e F2) vengono trattate in modo approfondito nei capitoli corrispondenti [sec:ionosphaere_3], [sec:tote_zone_2], [sec:sprungdistanz_2] e [sec:muf_luf_2] sull’ionosfera per HB9. Qui è sufficiente comprendere che la LUF può essere influenzata dall’intensità del segnale, mentre la MUF è determinata esclusivamente dalle condizioni di propagazione dell’ionosfera.

<!-- Review completato, per me va bene così. Vy 73 de Marc -->