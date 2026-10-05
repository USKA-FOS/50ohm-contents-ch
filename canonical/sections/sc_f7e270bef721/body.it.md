Nella sezione [sec:dummy_load_1] abbiamo già conosciuto il *carico fittizio*. Un carico fittizio è una resistenza di carico che converte la potenza RF erogata dal trasmettitore in calore. Permette, ad esempio, di testare un trasmettitore o determinare la sua potenza d’uscita senza che un segnale venga irradiato tramite un'antenna. In questa sezione esaminiamo più in dettaglio come può essere realizzata una tale struttura.

Un carico fittizio per la gamma RF è spesso composto da più resistenze individuali. In questo modo, la potenza dissipata risultante può essere distribuita su più componenti, raggiungendo un'elevata capacità di carico totale. Le resistenze possono essere collegate in parallelo, in serie o in una combinazione di collegamenti in serie e parallelo. Se si utilizzano resistenze identiche con la stessa capacità di carico e il circuito è costruito simmetricamente, la potenza dissipata si distribuisce uniformemente sulle singole resistenze. Il numero e il collegamento necessari delle resistenze possono essere determinati con le regole note per i collegamenti in serie e parallelo. In un carico fittizio RF è inoltre importante che il circuito corrisponda il più possibile a una pura resistenza ohmica di $\qty{50}{\ohm}$ anche ad alte frequenze. Pertanto, vengono utilizzate resistenze adatte, il più possibile a bassa induttanza, e i collegamenti vengono realizzati il più corti possibile.

La figura [ref:dummy_load_aufbau1] mostra un carico fittizio completato di 50ohm.de. Qui, ad esempio, $\num{20}$ resistenze da $\qty{1}{\kilo\ohm}$ ciascuna sono collegate in parallelo. Per $n$ resistenze identiche collegate in parallelo vale:

$R_\mathrm{ges} = \frac{R}{n}$

Da cui risulta:

$R_\mathrm{ges} = \frac{\qty{1}{\kilo\ohm}}{20} = \qty{50}{\ohm}$

<warning>
La massima potenza dissipata possibile dell'intero carico fittizio si ottiene approssimativamente dalla somma delle capacità di carico di tutte le resistenze, a condizione che la potenza si distribuisca uniformemente su di esse. Poiché il carico fittizio 50ohm.de non dispone di raffreddamento e non è schermato, dovrebbe essere utilizzato solo per trasmettitori QRP con bassa potenza d’uscita. Per potenze più elevate è necessario un carico fittizio con raffreddamento e schermatura, adatto anche per il funzionamento continuo!
</warning>

Il carico fittizio 50ohm.de possiede inoltre un raddrizzatore del valore di picco composto da un diodo e un condensatore. Con questo, dalla tensione RF presente può essere generata una tensione continua, che può essere misurata, ad esempio, con un multimetro. Tenendo conto del partitore di tensione e della tensione diretta del diodo, da ciò può essere determinata la potenza d’uscita RF del trasmettitore.

[question:AI602]

<margin>
[photo:340:dummy_load_aufbau1:Il carico fittizio 50ohm.de completato]
[photo:341:dummy_load_aufbau2:Struttura del carico fittizio 50ohm.de]

*Visualizzazione:* Vuoi anche costruire un fantastico carico fittizio QRP 50ohm.de? Allora puoi ordinarlo come kit di costruzione presso [DARC-Verlag](https://darcverlag.de/50Ohm-Dummy-Load-DIY-Kit-Bausatz).
</margin>

% ARK: Questo riferimento al DARC è stato lasciato intenzionalmente.
% Eventualmente, questo dovrebbe essere discusso ulteriormente nel team o nella direzione del progetto.

Nella seguente domanda d'esame, il carico fittizio è composto da una combinazione di collegamenti in serie e parallelo. Se in ogni ramo $N_\mathrm{S}$ resistenze uguali sono collegate in serie e successivamente $N_\mathrm{P}$ di tali rami sono collegati in parallelo, la resistenza totale risulta:

$R_\mathrm{ges} = \frac{N_\mathrm{S}}{N_\mathrm{P}} \cdot R$

Il numero totale di resistenze utilizzate è:

$n = N_\mathrm{S} \cdot N_\mathrm{P}$

Se tutte le resistenze sono ugualmente caricate, le loro potenze dissipate ammissibili si sommano. In questo modo, è possibile realizzare un carico fittizio con la resistenza desiderata e contemporaneamente un'elevata capacità di carico.

[question:AI601]

Un'altra possibilità per determinare la potenza d’uscita RF consiste nell'equipaggiare il carico fittizio con una presa intermedia della sua rete di resistenze. Se questa presa intermedia si trova, ad esempio, vicino al collegamento di massa, lì è presente solo una parte dell'intera tensione RF.

Le resistenze formano un partitore di tensione. Se il suo rapporto di divisione è noto, dalla tensione RF misurata alla presa intermedia si può risalire all'intera tensione sul carico fittizio. La tensione parziale può essere misurata, ad esempio, con una sonda RF e un multimetro digitale. Dalla tensione totale così determinata, si può quindi calcolare la potenza RF.

[question:AI603]
