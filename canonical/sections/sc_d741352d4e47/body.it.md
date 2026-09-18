Nel capitolo [sec:antennengewinn] abbiamo già incontrato il radiatore isotropico (cfr. figura [ref:e_Kugelstrahler]). Il radiatore isotropico non è un’antenna reale, bensì un modello fisico di un radiatore che distribuisce l’energia in modo uniforme in tutte le direzioni dello spazio. 
La potenza isotropica equivalente irradiata (EIRP) di un’antenna reale si riferisce al radiatore isotropico. In altre parole, la potenza irradiata di un’antenna reale viene confrontata con la potenza irradiata del radiatore isotropico. Per la potenza irradiata conta solo l’energia che effettivamente giunge all’antenna. A causa delle perdite del cavo ecc., la potenza del trasmettitore nella realtà non può essere completamente trasferita all’antenna. Tale potenza persa non deve essere inclusa nel calcolo della potenza irradiata. Il guadagno d’antenna nella direzione preferenziale fa invece parte del calcolo. In formule, ciò si esprime come segue:$P_\mathrm{EIRP} = (P_\mathrm{trasmettitore} - P_\mathrm{perdite}) \cdot G_\mathrm{antenna}$
dove $G_\mathrm{antenna}$ rappresenta il guadagno d’antenna. L’EIRP è quindi il prodotto tra la potenza effettivamente fornita all’antenna e il suo guadagno in una direzione, riferito al radiatore isotropico.<margin>
[picture:751:e_Kugelstrahler:Radiatore isotropico al centro di una sfera, che genera la stessa potenza irradiata in tutti i punti della superficie sferica]
</margin>
<tip>
Prima dell’esame è bene familiarizzare con la propria calcolatrice. Le formule e i calcoli richiesti per le diverse domande d’esame vanno esercitati più volte, in modo da padroneggiare con sicurezza lo strumento e i passaggi di calcolo durante la prova.
</tip>
[question:EG501]Nella domanda successiva, è fondamentale prestare attenzione ai segni delle operazioni. Le perdite vengono *sottratte* dalla potenza di trasmissione e poi moltiplicate per il fattore di guadagno ($G_\mathrm{antenna}$). Poiché si deve calcolare l'EIRP, il riferimento deve essere fatto rispetto al radiatore isotropico.

[question:EG502]

---

Nel capitolo sui decibel [sec:dezibel_1] abbiamo imparato che è utile operare con valori in dB, poiché molte operazioni di calcolo si semplificano notevolmente. Gli amplificatori e gli attenuatori possono essere sommati o sottratti semplicemente in decibel. La figura [ref:e_verstaerkung_daempfung] mostra un impianto radio con diversi stadi di amplificazione e attenuazione. Il guadagno totale di questo impianto si ottiene sommando i singoli contributi: $\qty{-2}{\dB} + \qty{6}{\dB} - \qty{3}{\dB} + \qty{2}{\dB} = \qty{3}{\dB}$, che corrisponde a un fattore di potenza di $\num{2}$.

<margin>
[picture:439:e_verstaerkung_daempfung:Amplificazioni e attenuazioni in un impianto radio]
</margin>

---

Le domande seguenti richiedono il calcolo dell'EIRP. A tal fine, si può utilizzare direttamente una formula oppure, con un po' di pratica, risolvere i problemi completamente a mente. In seguito, mostreremo quindi generalmente entrambi i metodi.

La formula per il calcolo dell'EIRP si ricava dalla raccolta di formule ed è la seguente:

$P_\mathrm{EIRP} = P_\mathrm{trasmettitore} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

<indepth>
Si ottiene la formula per $P_\mathrm{EIRP}$ riarrangiando opportunamente la formula del guadagno presente nella raccolta di formule:
  
$g = 10 \cdot \log_{10}\left(\frac{P_2}{P_1}\right) \unit{\dB}$
  
Poiché deve essere considerata anche un’<b>attenuazione</b> $a$, questa viene sottratta dal <b>guadagno d'antenna</b>. Per $P_1$ inseriamo la <b>potenza d’ingresso</b> $P_\mathrm{Sender}$, poiché rappresenta la potenza d’ingresso, e per $P_2$ la <b>potenza d’uscita</b> $P_\mathrm{EIRP}$, poiché questa è la potenza d’uscita risultante.

$g-a = 10 \cdot \log_{10}\left(\frac{P_\mathrm{EIRP}}{P_\mathrm{Sender}}\right) \unit{\dB} \quad\quad\quad | : \qty{10}{\dB}$
  
Dividiamo entrambi i membri per $\qty{10}{\dB}$:
  
$\frac{g-a}{\qty{10}{\dB}} = \log_{10}\left(\frac{P_\mathrm{EIRP}}{P_\mathrm{Sender}}\right) \quad\quad\quad | 10^x$
  
Applichiamo poi $10^x$ a entrambi i membri per risolvere il logaritmo:
  
$10^{\frac{g-a}{\qty{10}{\dB}}} = \frac{P_\mathrm{EIRP}}{P_\mathrm{Sender}} \quad\quad\quad | \cdot P_\mathrm{Sender}$
  
Moltiplicando per $P_\mathrm{Sender}$ si ottiene la formula necessaria:
  
$P_\mathrm{EIRP} = P_\mathrm{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}$
</indepth>

In questo caso $g_i$ è il <b>guadagno d'antenna</b> riferito al <b>radiatore</b> isotropico, mentre $a$ descrive l’<b>attenuazione</b> dovuta ai cavi e ai dispositivi di adattamento.

[question:EG503]

Il primo metodo di calcolo utilizza la formula sopra menzionata. Poiché non ci sono perdite di potenza, l'attenuazione è $a=0$ e la formula si semplifica in: 

$P_\mathrm{EIRP} = P_\mathrm{trasmettitore} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 10^{\frac{\qty{26}{\dBi}}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 398 \approx \qty{100}{\watt}$

---

Il secondo metodo di calcolo possibile sfrutta il fatto che i valori in dB possono essere "scomposti". Nel quesito il guadagno d'antenna è $g = \qty{26}{\dBi}$. Nella raccolta di formule, nella tabella [ref:e_dezibel_leistungsfaktoren] si trova una panoramica dei fattori di potenza per valori dB importanti. Per $\qty{26}{\dB}$ non esiste un valore diretto. Tuttavia, poiché i livelli in decibel possono essere sommati, è possibile suddividere il valore in modo significativo:

$\qty{26}{\dBi} = \qty{20}{\dBi} + \qty{6}{\dB}$

<margin>
| c:dB | c:≈ fattore di potenza |
| $\num{0}$ | $\num{1}$ |
| $\num{1,5}$ | $\sqrt{2} = 1,41$ |
| $\num{2,15}$ | $\num{1,64}$ |
| $\num{3}$ | $\num{2}$ |
| $\num{5}$ | $\sqrt{10} = 3,16$ |
| $\num{6}$ | $\num{4}$ |
| $\num{10}$ | $\num{10}$ |
| $\num{20}$ | $\num{100}$ |
[table:e_dezibel_leistungsfaktoren:Fattori di potenza importanti in dB]
</margin>

<tip>
Altri valori in decibel spesso utili si trovano nel capitolo [sec:dezibel_1].
</tip>

Per $\qty{20}{\dB}$ la tabella indica un fattore di potenza di $\num{100}$, mentre per $\qty{6}{\dB}$ un fattore di $\num{4}$. Con questi dati è possibile calcolare molto semplicemente la potenza isotropica equivalente irradiata:

$P_\mathrm{EIRP} = \qty{250}{\milli\watt} \cdot 100 \cdot 4 = \qty{100}{\watt}$

La risposta corretta è quindi $\qty{100}{\watt}$ EIRP.

Per la domanda successiva possiamo procedere allo stesso modo della domanda precedente.

[question:EG504]

---

Per molti radioamatori è difficile rispettare la distanza di sicurezza necessaria con una potenza di trasmissione di, ad esempio, $\qty{100}{\watt}$. In questi casi, il funzionamento QRP rappresenta una soluzione. Anche con un apparecchio non QRP, è possibile ridurre la potenza d’uscita a un valore specifico, come illustrato nella figura [ref:e_ausgangsleistung_ic].

<margin>
[photo:229:e_ausgangsleistung_ic:In molti ricetrasmettitori la potenza d’uscita può essere regolata in modo continuo o, come in questo caso con l’IC-705, in piccoli passi.]
</margin>

[question:EG511]

L’antenna verticale indicata in questa domanda ha un guadagno $g=\qty{5,15}{\dBi}$, mentre le perdite del cavo vengono trascurate, cioè $a = 0$. Se l’antenna non avesse guadagno ($\qty{0}{\dBi}$), la potenza di trasmissione dovrebbe essere semplicemente limitata a un massimo di $\qty{10}{\watt}$. La potenza irradiata sarebbe quindi solo $\qty{10}{\watt}$ EIRP. Tuttavia, poiché è presente un guadagno d’antenna di $\qty{5,15}{\dBi}$, la potenza di trasmissione deve essere ridotta di conseguenza. La potenza di trasmissione deve essere almeno $\qty{5,15}{\dB}$ inferiore a $\qty{10}{\watt}$.

Anche in questo caso ci sono due possibili metodi di calcolo. Iniziamo con il metodo basato sulla formula nota. Tuttavia, in questo esercizio non si cerca la potenza irradiata $P_\mathrm{EIRP}$, ma la potenza di trasmissione $P_\mathrm{Sender}$. Pertanto, dobbiamo modificare la formula di conseguenza:

$P_\mathrm{EIRP} = P_\mathrm{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}} \quad\quad\quad | : 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

Ne risulta:$ P_\mathrm{trasmettitore} = \frac{P_\mathrm{EIRP}}{10^{\frac{g_i-a}{\qty{10}{\dB}}}} $Inseriamo i valori:$ P_\mathrm{trasmettitore} = \frac{\qty{10}{\watt}}{10^{\frac{\qty{5,15}{\dBi}}{\qty{10}{\dB}}}} = \frac{\qty{10}{\watt}}{3,27} \approx \qty{3,05}{\watt} $Il calcolo con la calcolatrice fornisce $\qty{3,05}{\watt}$. Con una limitazione a $\qty{3}{\watt}$ si rispetta il limite di meno di $\qty{10}{\watt}$ di EIRP.Il secondo metodo di calcolo procede nuovamente tramite la scomposizione dei valori in dB. Osservando il valore $g=\qty{5,15}{\dBi}$, si nota che è possibile scomporlo in$\qty{5,15}{\dBi} = \qty{3}{\dBi} + \qty{2,15}{\dB}$nella tabella [ref:e_dezibel_leistungsfaktoren] si trova il fattore per $\qty{2,15}{\dB}$ pari a $\num{1,64}$. Quindi, per la potenza di trasmissione massima si ottiene:$P_\mathrm{trasmettitore} = \frac{\qty{10}{\watt}}{2\cdot 1,64} = \frac{\qty{10}{\watt}}{3,28} \approx \qty{3}{\watt}$Come previsto, si giunge allo stesso risultato. Con $\qty{3}{\watt}$ si è al sicuro.La domanda successiva potrebbe essere risolta di nuovo con la raccolta di formule, sostituendo $a=\qty{1}{\dB}$, ma si può fare molto semplicemente a mente. 

[question:EG505]

Come descritto all'inizio del paragrafo, per calcolare la potenza irradiata EIRP si tiene conto del guadagno d'antenna ($\qty{11}{\dBi}$) e della potenza che effettivamente arriva all'antenna. La potenza di trasmissione viene attenuata di $\qty{1}{\dB}$ dal cavo, mentre l'intero sistema d'antenna ha un guadagno reale di $\qty{10}{\dBi}$. Nella nostra tabella [ref:e_dezibel_leistungsfaktoren] nella raccolta di formule, per $\qty{10}{\dB}$ è indicato il fattore $\num{10}$. Da una potenza di trasmissione di $\qty{100}{\watt}$ si ottiene quindi una potenza irradiata di $\qty{1000}{\watt}$.

Per la domanda successiva occorre considerare che viene utilizzata un'antenna dipolo. Anche in questo caso il calcolo può essere fatto molto semplicemente a mente.

[question:EG506]

Il guadagno di un'antenna dipolo rispetto al radiatore sferico è di $\qty{2,15}{\dB}$. Questo corrisponde a un fattore di $\num{1,64}$. Questo valore è riportato anche nella raccolta di formule:

$P_\mathrm{EIRP} = P_\mathrm{ERP} + \qty{2,15}{\dB}$

ovvero come fattore:

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 1,64$

dove $P_\mathrm{ERP}$ rappresenta la potenza irradiata riferita al dipolo. 

Il guadagno del dipolo è di $\qty{2,15}{\dBi}$, che in questo caso corrisponde esattamente all’attenuazione del cavo nella domanda. Entrambi si compensano quindi a vicenda. L’antenna dipolo irradia una potenza isotropica equivalente irradiata (EIRP) di $\qty{75}{\watt}$.

Nella domanda successiva è nuovamente prevista un’antenna dipolo come antenna.

[question:EG507]

Si ricerca la potenza isotropica equivalente irradiata $P_\mathrm{EIRP}$. Inizialmente occorre considerare l’attenuazione del cavo. Un’attenuazione di $\qty{10}{\dB}$ corrisponde a un rapporto di potenza di $\num{0,1}$. Con questo fattore di attenuazione e il fattore di guadagno dell’antenna dipolo di $\num{1,64}$, la potenza irradiata può essere calcolata successivamente.

$P_\mathrm{EIRP} = \qty{100}{\watt} \cdot 0,1 \cdot 1,64 = \qty{16,4}{\watt}$

Per la domanda successiva, nella raccolta di formule si trova direttamente una formula applicabile. Poiché abbiamo un’antenna direzionale il cui guadagno è indicato rispetto al dipolo (ERP), per il calcolo di $P_\mathrm{EIRP}$ occorre aggiungere $\qty{2,15}{\dB}$:

$P_\mathrm{EIRP} = P_\mathrm{trasmettitore} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}}$

[question:EG508]

---

Inserendo i valori nella formula si può risolvere rapidamente la domanda. Tuttavia, è possibile farlo anche mentalmente. Calcoliamo il guadagno totale del sistema e lo scomponiamo di conseguenza:

$\qty{-2}{\dB} + \qty{5}{\dB} + \qty{2,15}{\dB} = \qty{3}{\dB} + \qty{2,15}{\dB}$ 

Ora possiamo leggere di nuovo i fattori dalla tabella:

$P_\mathrm{EIRP} = \qty{5}{\watt} \cdot 2 \cdot 1,64 = \qty{16,4}{\watt}$

Anche il prossimo quesito può essere risolto allo stesso modo. Bisogna solo fare attenzione che il guadagno sia riferito al dipolo.

[question:EG509]

Calcoliamo di nuovo il guadagno totale e scomponiamolo:

$\qty{-1}{\dB} + \qty{11}{\dB} + \qty{2,15}{\dB} = \qty{10}{\dB} + \qty{2,15}{\dB}$ 

Ora possiamo leggere di nuovo i fattori dalla tabella:

$P_\mathrm{EIRP} = \qty{0,6}{\watt} \cdot 10 \cdot 1,64 = \qty{9,8}{\watt}$

Nel prossimo quesito è indicata un'antenna con un guadagno di $\qty{0}{\dB}$ riferito al dipolo. Ciò non significa altro che si tratta di un dipolo.

[question:EG510]

Qui si può nuovamente utilizzare la formula dalla [raccolta di formule](#):

$P_\mathrm{EIRP} = P_\mathrm{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{8,5}{\watt} \cdot 10^{\frac{\qty{0}{\dB}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{9,9}{\watt}$

A mente si può approssimare: se si calcola il guadagno totale del sistema, questo risulta essere solo $\qty{0,65}{\dB}$, quindi meno di $\qty{1}{\dB}$. Secondo la nostra tabella [ref:e_dezibel_leistungsfaktoren], $\qty{1}{\dB}$ corrisponde a un fattore di $\num{1,26}$. Il valore obiettivo deve quindi essere compreso tra $\qty{8,5}{\watt}$ e $\qty{10,71}{\watt}$. Solo i $\qty{9,9}{\watt}$ sono quindi possibili.
