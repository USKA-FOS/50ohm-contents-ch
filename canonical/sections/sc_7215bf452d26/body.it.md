All’inizio di questo capitolo abbiamo trattato il dipolo come forma base di tutte le antenne. Il dipolo a semionda irradia onde radio perpendicolarmente alla direzione del filo. Altre tipologie di antenna possono irradiare le onde radio, a seconda della loro struttura, preferibilmente in una o più direzioni e meno in altre:
* Un’antenna Groundplane irradia in modo quasi uniforme in tutte le direzioni orizzontali, ma non verso l’alto o verso il basso.
* In un’antenna Yagi-Uda, le onde radio vengono concentrate come in una torcia elettrica in un fascio diretto in avanti e ridotte in tutte le altre direzioni.

---

<law>
I valori limite che un impianto trasmittente deve rispettare sono definiti dall’Ordinanza sulla protezione dalle radiazioni non ionizzanti [ORNI](https://www.fedlex.admin.ch/eli/cc/2000/38/it). L’*ORNI* è piuttosto estesa e riguarda anche i servizi di radiocomunicazione commerciali. Pertanto, qui di seguito è riportato un riassunto dei requisiti rilevanti per gli impianti radioamatoriali:

*Valori limite per impianti radioamatoriali*

Gli impianti radioamatoriali devono rispettare i *valori limite di immissione* dell’ORNI. A seconda della frequenza, questi valori variano tra 28 e 87 [V/m].
Per calcolare le distanze da rispettare, nell’area riservata ai membri della USKA sono disponibili programmi o fogli Excel appositi:

[Strumenti per il calcolo ORNI](https://uska.ch/emissions-berechnung/)

Inoltre, *non è necessario rispettare alcun valore limite dell’impianto* a condizione che la durata di esercizio sia *inferiore a 800 ore all’anno*. Questo è praticamente sempre il caso delle applicazioni radioamatoriali. Se un impianto trasmette eccezionalmente di più, deve rispettare un valore limite dell’impianto in luoghi con utilizzo sensibile (OMEN). Tale valore è pari a 8,5 V/m per trasmettitori in onde lunghe e onde medie e a 3,0 V/m per tutte le altre bande di frequenza.
[Fonte](https://www.bafu.admin.ch/it/amateurfunk-als-elektrosmog-quelle)

Con il termine "luoghi con utilizzo sensibile" (OMEN) si intendono luoghi in cui le persone soggiornano regolarmente per periodi prolungati.
</law>

---

I valori limite prescritti dalla procedura di valutazione per la protezione delle persone dai campi elettromagnetici devono essere rispettati da un impianto trasmittente in ogni direzione. Se a una certa distanza dall’antenna i valori limite vengono rispettati nella direzione di massima irradiazione, allora verranno rispettati anche alla stessa distanza in tutte le altre direzioni. Pertanto, ci interessa in particolare la direzione di massima irradiazione. Questa viene definita come *direzione principale di irradiazione*.

---

La potenza con cui un’antenna irradia nella sua direzione principale di irradiazione è espressa dal *fattore di guadagno* riferito al dipolo a semionda. Questo indica quanto un’antenna irradia meglio rispetto a un dipolo a semionda nella rispettiva direzione principale di irradiazione. Un fattore di guadagno di <span class="math inline">\num{2}</span> rispetto al dipolo a semionda significa, ad esempio, che un’antenna irradia il doppio rispetto a un dipolo a semionda nella sua direzione principale di irradiazione.

<indepth>
% TODO: Specifico per edizione
Al posto del fattore di guadagno delle antenne, spesso viene indicato il "guadagno in decibel (<span class="math inline">\unit{\dB}</span>")". Il corso tratta l’unità di misura decibel nel capitolo [sec:dezibel_1].
</indepth>

---

Per indicare quanta potenza irradia un’antenna concreta nella sua direzione principale di irradiazione quando si imposta una certa potenza di trasmissione, si moltiplica la potenza di trasmissione per il fattore di guadagno riferito al dipolo a semionda. Si ottiene così la *potenza irradiata effettiva*, che viene solitamente abbreviata come ERP (dall’inglese *effective radiated power*). Ad esempio, se si inserisce una potenza di trasmissione di <span class="math inline">\qty{5}{\watt}</span> in un’antenna con un fattore di guadagno di <span class="math inline">\num{2}</span> rispetto al dipolo a semionda, si ottiene una potenza irradiata di <span class="math inline">\qty{10}{\watt}</span> ERP.

<margin>
La potenza irradiata effettiva (ERP) può essere immaginata anche come segue: è la potenza che bisognerebbe inserire in un dipolo a semionda affinché questo irradia nella sua direzione principale di irradiazione con la stessa intensità dell’antenna considerata.
</margin>

Le antenne direttive possono avere fattori di guadagno molto più elevati. Un’antenna Yagi-Uda a 9 elementi, ad esempio, può facilmente raggiungere un fattore di guadagno di <span class="math inline">\num{10}</span> o più rispetto al dipolo a semionda. Se si inserisce, ad esempio, <span class="math inline">\qty{100}{\watt}</span> in una tale antenna, la potenza irradiata raggiunge già <span class="math inline">\qty{1000}{\watt}</span> ERP o più!

[question:NG401]