All'inizio di questo capitolo abbiamo trattato il dipolo come forma base di tutte le antenne. Il dipolo a semionda irradia onde radio perpendicolarmente alla direzione del filo. Altre forme di antenna possono irradiare le loro onde radio preferenzialmente in una o più direzioni a seconda della loro costruzione e meno in altre direzioni:
* Un'antenna Groundplane irradia quasi uniformemente in tutte le direzioni del cielo, ma non verso l'alto o verso il basso.
* Con un'antenna Yagi-Uda, le onde radio vengono concentrate in un fascio in avanti, come con una torcia, e ridotte in tutte le altre direzioni.

I limiti imposti dal metodo di verifica per la protezione delle persone nei campi elettromagnetici devono essere rispettati da un impianto di trasmissione in ogni direzione. Se a una certa distanza dall'antenna i limiti vengono rispettati nella direzione in cui irradia più fortemente, allora i limiti saranno rispettati anche in tutte le altre direzioni alla stessa distanza. Pertanto, siamo particolarmente interessati alla direzione di irradiazione più forte. Questa è chiamata *direzione di irradiazione principale*.

---

Quanto fortemente un'antenna irradia nella sua direzione di irradiazione principale è espresso dal *fattore di guadagno* rispetto al dipolo a semionda. Questo indica quanto meglio un'antenna irradia rispetto a un dipolo a semionda nella rispettiva direzione di irradiazione principale. Un fattore di guadagno di $\num{2}$ rispetto al dipolo a semionda significa, ad esempio, che un'antenna irradia due volte più forte nella direzione di irradiazione principale rispetto a un dipolo a semionda nella sua direzione di irradiazione principale.

<indepth>
% TODO: Rendere specifico per l'edizione
Al posto del fattore di guadagno delle antenne, viene spesso indicato il "guadagno in decibel ($\unit{\dB}$)". Il corso per la classe E tratta l'unità decibel.
</indepth>

---

Per indicare ora quanto irradia un'antenna specifica nella direzione di irradiazione principale quando si immette una determinata potenza di trasmissione, si moltiplica la potenza di trasmissione per il fattore di guadagno relativo al dipolo a semionda. Si ottiene così la *potenza irradiata efficace*, che viene solitamente abbreviata come ERP (dall'inglese "effective radiated power"). Ad esempio, se immettiamo una potenza di trasmissione di $\qty{5}{\watt}$ in un'antenna con un fattore di guadagno di $\num{2}$ rispetto al dipolo a semionda, si ottiene una potenza di irradiazione di $\qty{10}{\watt}$ ERP.

<margin>
Si può anche pensare alla potenza irradiata efficace (ERP) in questo modo: è la potenza che dovrebbe essere immessa in un dipolo a semionda affinché questo irradi con la stessa intensità nella sua direzione di irradiazione principale come l'antenna considerata.
</margin>

Le antenne direzionali possono avere fattori di guadagno molto maggiori. Un'antenna Yagi-Uda a 9 elementi può facilmente raggiungere un fattore di guadagno di $\num{10}$ o più rispetto al dipolo a semionda. Se si immettono, ad esempio, $\qty{100}{\watt}$ in un'antenna del genere, la potenza di irradiazione è già di $\qty{1000}{\watt}$ ERP o più!

[question:NG401]
