Nella classe N abbiamo già imparato a conoscere la *potenza irradiata effettiva* (ERP). A differenza dell'EIRP, questa non si riferisce a un radiatore isotropico, ma a un dipolo a semionda. Per il calcolo è rilevante solo la potenza che effettivamente arriva al punto di alimentazione dell'antenna. Le perdite nella linea di alimentazione, ad esempio dovute all'attenuazione del cavo, devono quindi essere sottratte dalla potenza di uscita del trasmettitore.

La potenza irradiata effettiva si ottiene dalla potenza fornita all'antenna e dal guadagno d'antenna nella direzione considerata:

$P_\mathrm{ERP}=P_\mathrm{Ant}\cdot G_\mathrm{d}$

In questo caso, $G_\mathrm{d}$ è il guadagno d'antenna riferito a un dipolo a semionda, espresso come fattore lineare.

[question:AG501]

La potenza al punto di alimentazione dell'antenna può essere determinata a partire dalla potenza di uscita del trasmettitore e dall'attenuazione della linea di alimentazione. Per fare ciò, l'attenuazione viene convertita in un fattore di attenuazione lineare $D$. Con un'attenuazione di, ad esempio, $\qty{10}{\dB}$, questo fattore è $\num{0,1}$, per cui solo un decimo della potenza del trasmettitore arriva all'antenna:

$P_\mathrm{Ant}=D\cdot P_\mathrm{Trasmittitore}$

Solo questa potenza effettivamente fornita viene poi moltiplicata per il guadagno d'antenna per calcolare l'ERP.

[question:AK104]

Nella domanda successiva occorre prestare particolare attenzione ai segni delle operazioni. Le perdite vengono sottratte dalla potenza di trasmissione e poi moltiplicate per il fattore di guadagno ($G_\mathrm{Antenna}$).
Poiché si deve calcolare l'ERP, il riferimento deve essere fatto a un dipolo a semionda.

[question:AG502]

Un suggerimento per la soluzione della domanda successiva è già fornito dalla [Allegato 1 dell'AFUV](https://50ohm.de/a1). Qui, per la banda dei $\qty{630}{\meter}$, è indicata una potenza massima di $\qty{1}{\watt}$ di ERP. Un dipolo a semionda per questa frequenza avrebbe una lunghezza di circa $\qty{315}{\meter}$ ed è quindi difficilmente realizzabile per la maggior parte dei radioamatori. In pratica, si utilizzano quindi antenne notevolmente accorciate, il cui rendimento è significativamente inferiore a quello di un dipolo a semionda non accorciato. Un guadagno d'antenna di $\qty{-20}{\dBd}$ è quindi del tutto plausibile. Poiché il cavo coassiale utilizzato ha una lunghezza ridotta, la sua attenuazione può essere trascurata in questa banda di frequenza. Prova ora a risolvere la domanda seguente.

[question:AG503]