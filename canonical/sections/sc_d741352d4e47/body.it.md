Nella classe N abbiamo già conosciuto il radiatore isotropo (cfr. figura [ref:e_Kugelstrahler]). Il radiatore isotropo non è un'antenna reale, è un modello fisico per un radiatore che irradia energia uniformemente in tutte le direzioni dello spazio. 

La Potenza Isotropa Effettiva Radiata (EIRP) di un'antenna reale si riferisce al radiatore isotropo. In altre parole, la potenza irradiata di un'antenna reale viene confrontata con la potenza irradiata del radiatore isotropo. Per la potenza irradiata è rilevante solo l'energia che raggiunge effettivamente l'antenna. A causa dell'attenuazione del cavo, ecc., la potenza del trasmettitore non può essere completamente fornita all'antenna nel mondo reale. Questa potenza persa non deve essere inclusa nel calcolo della potenza irradiata. Il guadagno dell'antenna nella direzione preferenziale è naturalmente parte del calcolo. Nelle formule, ciò significa:

$P_\text{EIRP} = (P_\text{Sender} - P_\text{Verluste}) \cdot G_\text{Antenne}$

Dove $G$ rappresenta il guadagno dell'antenna. L'EIRP è quindi il prodotto della potenza effettivamente fornita all'antenna e del suo guadagno in una direzione, rispetto al radiatore isotropo.

<margin>
[picture:751:e_Kugelstrahler:Radiatore isotropo al centro di una sfera, che produce la stessa potenza irradiata in tutti i punti della superficie sferica]
</margin>

<tip>
Prima dell'esame, familiarizza bene con la tua calcolatrice. Le formule e i calcoli nelle varie domande dovrebbero essere esercitati ripetutamente, in modo da padroneggiare con sicurezza l'apparecchio e i passaggi di calcolo durante l'esame.
</tip>

[question:EG501]

Nella domanda successiva, è assolutamente necessario prestare attenzione ai segni di calcolo. Le perdite vengono *sottratte* dalla potenza di trasmissione e poi *moltiplicate* per il fattore di guadagno ($G_{Antenne}$). Poiché si deve calcolare l'EIRP, è necessario fare riferimento al radiatore isotropo.

[question:EG502]

---

Nel capitolo sui decibel abbiamo imparato che è utile calcolare con valori in dB, poiché molti calcoli si semplificano notevolmente. Amplificazioni e attenuazioni possono essere semplicemente sommate o sottratte in decibel. La figura [ref:e_verstaerkung_daempfung] mostra un impianto radio con diversi amplificatori e attenuatori. L'amplificazione totale di questo impianto si ottiene sommando i singoli contributi: $\qty{-2}{\dB} + \qty{6}{\dB} - \qty{3}{\dB} + \qty{2}{\dB} = \qty{3}{\dB}$, che corrisponde a un fattore di potenza di $\num{2}$.

<margin>
[picture:439:e_verstaerkung_daempfung:Amplificazioni e attenuazioni in un impianto radio]
</margin>

---

Le domande seguenti richiedono il calcolo dell'EIRP. A tal fine, si può utilizzare direttamente una formula, oppure i problemi possono essere risolti completamente a mente, con un po' di pratica. Di seguito, mostreremo quindi principalmente entrambi gli approcci.

La formula per il calcolo dell'EIRP deriva dalla raccolta di formule e recita:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

<indepth>
Si ottiene la formula per $P_\text{EIRP}$ riorganizzando la formula di guadagno dalla raccolta di formule:
  
$g = 10 \cdot \log_{10}\left(\frac{P_2}{P_1}\right) \unit{\dB}$
  
Poiché deve essere considerata anche un'attenuazione $a$, questa viene sottratta dal guadagno dell'antenna. Per $P_1$ inseriamo la potenza del trasmettitore $P_\text{Sender}$, poiché rappresenta la potenza di ingresso, e per $P_2$ di conseguenza $P_\text{EIRP}$, poiché questa è la potenza di uscita risultante.

$g-a = 10 \cdot \log_{10}\left(\frac{P_\text{EIRP}}{P_\text{Sender}}\right) \unit{\dB} \quad\quad\quad | : \qty{10}{\dB}$
  
Dividiamo entrambi i lati per $\qty{10}{\dB}$:
  
$\frac{g-a}{\qty{10}{\dB}} = \log_{10}\left(\frac{P_\text{EIRP}}{P_\text{Sender}}\right) \quad\quad\quad | 10^x$
  
Successivamente, applichiamo $10^x$ su entrambi i lati per risolvere il logaritmo:
  
$10^{\frac{g-a}{\qty{10}{\dB}}} = \frac{P_\text{EIRP}}{P_\text{Sender}} \quad\quad\quad | \cdot P_\text{Sender}$
  
Moltiplicando per $P_\text{Sender}$ si ottiene la formula necessaria:
  
$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$
</indepth>

Dove $g_i$ è il guadagno dell'antenna rispetto al radiatore isotropo, mentre $a$ descrive l'attenuazione dovuta ai cavi e ai dispositivi di adattamento.

[question:EG503]

Il primo metodo di calcolo utilizza la formula sopra menzionata. Poiché non ci sono perdite di potenza, l'attenuazione $a=0$ e la formula si semplifica in:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 10^{\frac{\qty{26}{dBi}}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 398 \approx \qty{100}{\watt}$

---

Il secondo metodo di calcolo sfrutta il fatto che i valori in dB possono essere "scomposti". Nella domanda, il guadagno d'antenna è $g = \qty{26}{\dBi}$. Nella raccolta di formule si trova nella tabella [ref:e_dezibel_leistungsfaktoren] una panoramica dei fattori di potenza per valori importanti in dB. Per $\qty{26}{\dB}$ non c'è una voce diretta. Poiché i livelli in decibel possono essere sommati, il valore può essere suddiviso in modo sensato:

$\qty{26}{\dBi} = \qty{20}{\dBi} + \qty{6}{\dB}$

<margin>
| c:dB | c:≈ Fattore di potenza |
| $\num{0}$ | $\num{1}$ |
| $\num{1,5}$ | $\sqrt{2} = 1,41$ |
| $\num{2,15}$ | $\num{1,64}$ |
| $\num{3}$ | $\num{2}$ |
| $\num{5}$ | $\sqrt{10} = 3,16$ |
| $\num{6}$ | $\num{4}$ |
| $\num{10}$ | $\num{10}$ |
| $\num{20}$ | $\num{100}$ |
[table:e_dezibel_leistungsfaktoren:Importanti fattori di potenza in dB]
</margin>

Per $\qty{20}{\dB}$ è indicato in tabella un fattore di potenza di $\num{100}$, per $\qty{6}{\dB}$ un fattore di $\num{4}$. Con questi si può calcolare molto facilmente la potenza isotropa irradiata equivalente:

$P_\text{EIRP} = \qty{250}{\milli\watt} \cdot 100 \cdot 4 = \qty{100}{\watt}$

La risposta corretta è quindi $\qty{100}{\watt}$ EIRP.

Alla domanda successiva possiamo procedere allo stesso modo della precedente. 

[question:EG504]

---

Per molti radioamatori è difficile mantenere la necessaria distanza di sicurezza con una potenza di trasmissione di, ad esempio, $\qty{100}{\watt}$. Il funzionamento QRP è una soluzione in questi casi. Se si rimane al di sotto del limite di $\qty{10}{\watt}$ EIRP con la potenza irradiata, l'indicazione di un impianto radioamatoriale fisso può essere omessa secondo § 9 BEMFV. Anche con un apparecchio non QRP, è possibile ridurre la potenza d'uscita a un valore specifico, come mostrato nella figura [ref:e_ausgangsleistung_ic].

<margin>
[photo:229:e_ausgangsleistung_ic:Su molti ricetrasmettitori è possibile regolare la potenza d'uscita in modo continuo, o come qui sull'IC-705, a piccoli passi.]
</margin>

[question:EG511]

L'antenna verticale indicata in questa domanda ha un guadagno di $g=\qty{5,15}{\dBi}$, le perdite del cavo sono trascurabili, cioè $a = 0$. Se l'antenna non avesse guadagno ($\qty{0}{\dBi}$), la potenza di trasmissione dovrebbe semplicemente essere limitata a un massimo di $\qty{10}{\watt}$. La potenza irradiata sarebbe quindi solo $\qty{10}{\watt}$ EIRP. Poiché tuttavia è presente un guadagno d'antenna di $\qty{5,15}{\dBi}$, la potenza di trasmissione deve essere adeguatamente ridotta. La potenza di trasmissione deve essere almeno $\qty{5,15}{\dB}$ inferiore a $\qty{10}{\watt}$.

Anche qui ci sono due possibili metodi di calcolo. Iniziamo con il metodo tramite la formula conosciuta. In questo compito, tuttavia, non viene cercata la potenza irradiata $P_\text{EIRP}$, ma la potenza di trasmissione $P_\text{Sender}$. Pertanto, dobbiamo riorganizzare la formula di conseguenza:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}} \quad\quad\quad | : 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

Si ottiene quindi:

$ P_\text{Sender} = \frac{P_\text{EIRP}}{10^{\frac{g_i-a}{\qty{10}{\dB}}}} $

Inseriamo i valori:

$ P_\text{Sender} = \frac{\qty{10}{\watt}}{10^{\frac{\qty{5,15}{\dBi}}{\qty{10}{\dB}}}} = \frac{\qty{10}{\watt}}{3,27} \approx \qty{3,05}{\watt} $

Il calcolo con la calcolatrice dà $\qty{3,05}{\watt}$. Con una limitazione a $\qty{3}{\watt}$ si rimane entro il valore limite di meno di $\qty{10}{\watt}$ EIRP.

Il secondo metodo di calcolo passa nuovamente attraverso la scomposizione dei valori in dB. Guardando il valore $g=\qty{5,15}{\dBi}$ si riconosce che questo valore può essere scomposto in

$\qty{5,15}{\dBi} = \qty{3}{\dBi} + \qty{2,15}{\dB}$

Nella tabella [ref:e_dezibel_leistungsfaktoren] si trova il fattore per $\qty{2,15}{\dB}$ come $\num{1,64}$. Pertanto, per la potenza di trasmissione massima si ottiene:

$P_\text{Sender} = \frac{\qty{10}{\watt}}{2\cdot 1,64} = \frac{\qty{10}{\watt}}{3,28} \approx \qty{3}{\watt}$

Come previsto, si ottiene lo stesso risultato. Con $\qty{3}{\watt}$ si è al sicuro.

La domanda successiva potrebbe essere risolta nuovamente con la raccolta di formule, inserendo $a=\qty{1}{\dB}$, ma si può fare anche a mente. 

[question:EG505]

Come descritto all'inizio della sezione, per la potenza irradiata EIRP si considerano il guadagno d'antenna ($\qty{11}{\dBi}$) e la potenza che effettivamente arriva all'antenna. La potenza di trasmissione viene attenuata dal cavo di $\qty{1}{\dB}$, l'intero sistema d'antenna ha in realtà un guadagno di $\qty{10}{\dBi}$. Nella nostra tabella [ref:e_dezibel_leistungsfaktoren] nella raccolta di formule, per $\qty{10}{\dB}$ viene indicato il fattore $\num{10}$. Dalla potenza di trasmissione di $\qty{100}{\watt}$ si ottiene una potenza irradiata di $\qty{1000}{\watt}$.

Per la domanda successiva, si deve prestare attenzione al fatto che viene utilizzata un'antenna dipolo. Anche questa può essere calcolata facilmente a mente.

[question:EG506]

Il guadagno di un'antenna dipolo rispetto all'omnidirezionale è di $\qty{2,15}{\dB}$. Questo corrisponde al fattore di $\num{1,64}$. Questo è anche indicato nella raccolta di formule:

$P_\text{EIRP} = P_\text{ERP} + \qty{2,15}{\dB}$

o come fattore:

$P_\text{EIRP} = P_\text{ERP} \cdot 1,64$

Dove $P_\text{ERP}$ è la potenza irradiata riferita al dipolo. 

Il guadagno del dipolo è di $\qty{2,15}{\dBi}$, che in questo caso corrisponde esattamente all'attenuazione del cavo nella domanda. Si annullano quindi a vicenda. L'antenna dipolo irradia $\qty{75}{\watt}$ EIRP.

Nella domanda successiva viene nuovamente fornita un'antenna dipolo. 

[question:EG507]

Si cerca la potenza isotropa irradiata equivalente $P_\text{EIRP}$. Innanzitutto, è necessario considerare l'attenuazione del cavo. Un'attenuazione di $\qty{10}{\dB}$ corrisponde a un rapporto di potenza di $\num{0,1}$. Con questo fattore di attenuazione e il fattore di guadagno d'antenna del dipolo di $\num{1,64}$, si può quindi calcolare la potenza irradiata.

$P_\text{EIRP} = \qty{100}{\watt} \cdot 0,1 \cdot 1,64 = \qty{16,4}{\watt}$


Per la domanda successiva, nella raccolta di formule si trova direttamente una formula applicabile. Poiché abbiamo un'antenna direttiva il cui guadagno è indicato rispetto al dipolo (ERP), per il calcolo di $P_\text{EIRP}$ devono essere aggiunti $\qty{2,15}{\dB}$:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}}$

[question:EG508]

---

Inserendo nella formula si può risolvere rapidamente la domanda. Ma anche qui si può fare a mente. Calcoliamo il guadagno totale del sistema e scomponiamo nuovamente di conseguenza:

$\qty{-2}{\dB} + \qty{5}{\dB} + \qty{2,15}{\dB} = \qty{3}{\dB} + \qty{2,15}{\dB}$ 

Ora possiamo leggere i fattori dalla tabella:

$P_\text{EIRP} = \qty{5}{\watt} \cdot 2 \cdot 1,64 = \qty{16,4}{\watt}$

Anche la domanda successiva può essere risolta allo stesso modo. Bisogna solo prestare attenzione al fatto che il guadagno è dato rispetto al dipolo. 

[question:EG509]

Calcoliamo nuovamente il guadagno totale e scomponiamo:

$\qty{-1}{\dB} + \qty{11}{\dB} + \qty{2,15}{\dB} = \qty{10}{\dB} + \qty{2,15}{\dB}$ 

Ora possiamo leggere di nuovo i fattori dalla tabella:

$P_\text{EIRP} = \qty{0,6}{\watt} \cdot 10 \cdot 1,64 = \qty{9,8}{\watt}$

Nella domanda successiva viene indicata un'antenna con un guadagno di $\qty{0}{\dB}$ rispetto al dipolo. Ciò significa semplicemente che questa antenna è un dipolo. 

[question:EG510]

Qui si può usare di nuovo la formula dalla raccolta di formule:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{8,5}{\watt} \cdot 10^{\frac{\qty{0}{\dB}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{9,9}{\watt}$

A mente si può anche fare una stima: se si ricalcola il guadagno totale del sistema, questo è solo $\qty{0,65}{\dB}$, quindi meno di $\qty{1}{\dB}$. Secondo la nostra tabella [ref:e_dezibel_leistungsfaktoren], $\qty{1}{\dB}$ corrisponde a un fattore di $\num{1,26}$. Il valore target deve quindi trovarsi tra $\qty{8,5}{\watt}$ e $\qty{10,71}{\watt}$. Solo i $\qty{9,9}{\watt}$ sono quindi plausibili.