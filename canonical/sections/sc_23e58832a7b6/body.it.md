Come spiegato nei capitoli precedenti, i segnali analogici vengono prima convertiti in valori digitali tramite campionamento. Un segnale analogico può essere misurato solo a intervalli specifici (si dice anche campionato). I valori campionati rappresentano quindi sempre solo uno stato momentaneo al momento del campionamento, e tra i singoli processi di campionamento il segnale analogico può variare arbitrariamente nel tempo. Poiché i segnali analogici non hanno una risoluzione temporale minima e sono quindi continui nel tempo, sono anche definiti tempo-continui. Al contrario, i campioni che consentono solo una risoluzione temporale massima e definita di un segnale sono definiti tempo-discreti, poiché esiste un intervallo temporale massimo possibile e definibile (quindi discreto) tra i singoli valori misurati.

<indepth>
[include:quantisierung_und_sampling]
</indepth>

[question:AF601]
[question:AF603]

Consideriamo il processo di campionamento da un'altra prospettiva. I segnali analogici possono assumere valori di tensione arbitrari e variare tra di essi senza stadi intermedi. Poiché queste variazioni nei segnali analogici possono essere sia piccole che grandi, questa proprietà dei segnali analogici è definita valore-continua. Al contrario, nella digitalizzazione di un segnale analogico, sono disponibili solo gradazioni limitate per la rappresentazione dei valori di tensione misurati (ad esempio, i suddetti da $\num{-128}$ a $\num{+127}$). Pertanto, i campioni digitali sono anche definiti valore-discreti a questo riguardo, poiché solo determinati valori di tensione sotto forma di stadi di tensione sono sempre disponibili durante la misurazione di un valore di segnale analogico. Se, ad esempio, un valore di segnale analogico si trova tra due stadi di tensione, il convertitore A/D deve decidere a quale valore di segnale il valore misurato tende maggiormente. Questo processo è anche chiamato quantizzazione. Il segnale precedentemente continuo viene qui mappato in un numero finito di valori.

A scopo illustrativo, ecco un esempio pratico basato su un dimmer analogico e un interruttore a gradini. Se un dimmer è realizzato con un circuito analogico, è possibile controllarne la luminosità in modo arbitrariamente preciso. Al contrario, con un interruttore a gradini con, ad esempio, $\num{5}$ gradini, è possibile accendere la lampada solo in $\num{5}$ livelli di luminosità; gli stadi intermedi non sono possibili. Pertanto, questo interruttore a gradini sarebbe definito valore-discreto. Se si tenta di riprodurre i livelli di luminosità impostati con il dimmer analogico utilizzando l'interruttore a gradini, si è limitati ai gradini fissi predefiniti. In questo caso, si sceglierebbe l'impostazione più adatta sull'interruttore a gradini, effettuando così una quantizzazione del valore di luminosità analogico.

[question:AF602]
[question:AF604]
