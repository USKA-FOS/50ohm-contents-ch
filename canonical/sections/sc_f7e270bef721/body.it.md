Nella classe E abbiamo già incontrato il *carico fittizio*. Un carico fittizio è una resistenza di carico che converte la potenza HF emessa dal trasmettitore in calore. Esso consente, ad esempio, di testare un trasmettitore o di determinare la sua potenza d’uscita senza che il segnale venga irradiato tramite un’antenna. Nella classe A esaminiamo ora più nel dettaglio come costruire un simile carico fittizio.

Un carico fittizio per la banda HF viene spesso realizzato combinando più resistenze individuali. In questo modo la potenza dissipata viene distribuita su più componenti, consentendo di raggiungere una capacità di carico complessivamente elevata. Le resistenze possono essere collegate in parallelo, in serie o in una combinazione di collegamenti in serie e in parallelo. Se si utilizzano resistenze identiche con la stessa capacità di carico e si realizza il circuito in modo simmetrico, la potenza dissipata si distribuisce uniformemente tra le singole resistenze. Il numero e il collegamento delle resistenze necessari possono essere determinati con le note regole per i collegamenti in serie e in parallelo. Per un carico fittizio HF è inoltre importante che il circuito, anche a frequenze elevate, si avvicini il più possibile a una resistenza puramente ohmica di $\qty{50}{\ohm}$. Per questo motivo si utilizzano resistenze adatte, il più possibile prive di induttanza, e si realizzano i collegamenti il più possibile brevi.

La figura [ref:dummy_load_aufbau1] mostra un carico fittizio da 50 ohm già assemblato da 50ohm.de. Qui, ad esempio, $\num{20}$ resistenze da $\qty{1}{\kilo\ohm}$ ciascuna sono collegate in parallelo. Per $n$ resistenze identiche collegate in parallelo vale:

$R_\mathrm{ges} = \frac{R}{n}$

Da cui si ottiene:

$R_\mathrm{ges} = \frac{\qty{1}{\kilo\ohm}}{20} = \qty{50}{\ohm}$

<warning>
La potenza dissipabile massima dell’intero carico fittizio si ottiene approssimativamente sommando le capacità di carico di tutte le resistenze, a condizione che la potenza si distribuisca uniformemente tra di esse. Poiché il carico fittizio di 50ohm.de non dispone di raffreddamento e non è schermato, dovrebbe essere utilizzato solo con trasmettitori QRP a bassa potenza d’uscita. Per potenze più elevate è necessario un carico fittizio con raffreddamento e schermatura, adatto anche al funzionamento continuo!
</warning>

Il carico fittizio di 50ohm.de dispone inoltre di un raddrizzatore del valore di picco composto da un diodo e un condensatore. Con questo circuito è possibile generare una tensione continua partendo dalla tensione HF applicata, che può essere misurata, ad esempio, con un multimetro. Tenendo conto del partitore di tensione e della tensione diretta del diodo, è possibile determinare la potenza d’uscita HF del trasmettitore.

[question:AI602]

<margin>
[photo:340:dummy_load_aufbau1:Il carico fittizio 50ohm.de già assemblato]
[photo:341:dummy_load_aufbau2:Struttura del carico fittizio 50ohm.de]

*Visualizzazione:* Vuoi costruire anche tu un interessante carico fittizio QRP 50ohm.de? Puoi ordinarlo come kit di montaggio presso il [DARC-Verlag](https://darcverlag.de/50Ohm-Dummy-Load-DIY-Kit-Bausatz).
</margin>

Nella domanda d’esame seguente il carico fittizio è composto da una combinazione di collegamenti in serie e in parallelo. Se in ogni ramo vengono collegati in serie $N_\mathrm{S}$ resistenze identiche e poi vengono collegati in parallelo $N_\mathrm{P}$ di questi rami, la resistenza totale risulta:

$R_\mathrm{ges} = \frac{N_\mathrm{S}}{N_\mathrm{P}} \cdot R$

Il numero totale di resistenze utilizzate è invece:

$n = N_\mathrm{S} \cdot N_\mathrm{P}$

Se tutte le resistenze sono ugualmente caricate, le loro potenze dissipabili ammissibili si sommano. In questo modo è possibile costruire un carico fittizio con la resistenza desiderata e, al contempo, un’elevata capacità di carico.

[question:AI601]

Un’altra possibilità per determinare la potenza d’uscita HF consiste nell’equipaggiare il carico fittizio con una presa intermedia della sua rete di resistenze. Se questa presa intermedia si trova, ad esempio, vicino al morsetto di massa, lì è presente solo una parte della tensione HF totale.

Le resistenze formano in questo caso un partitore di tensione. Se si conosce il rapporto di divisione, dalla tensione HF misurata alla presa intermedia è possibile risalire alla tensione totale presente sul carico fittizio. La tensione parziale può essere misurata, ad esempio, con una sonda HF e un multimetro digitale. Dalla tensione totale così determinata è poi possibile calcolare la potenza HF.

[question:AI603]