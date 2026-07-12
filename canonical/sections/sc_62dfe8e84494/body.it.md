Il terzo componente passivo in tecnica radio – dopo la resistenza e il condensatore – è la *bobina*. Diverse tipologie di bobine e i loro simboli circuitali sono rappresentati nelle figure [ref:e_spulen] e [ref:e_schaltsymbole_spulen]. Come abbiamo già appreso nel capitolo sul campo magnetico, in una bobina si genera un campo magnetico non appena una corrente elettrica scorre attraverso la bobina. La forma costruttiva più semplice di una bobina è la cosiddetta *bobina cilindrica* diritta, come mostrato nella figura [ref:e_spule_Aufbau].

<margin>
[photo:207:e_spulen:Diverse forme costruttive di bobine]
[picture:942:e_schaltsymbole_spulen:Simboli circuitali per diversi tipi di bobine]
[picture:948:e_spule_Aufbau:Struttura di una bobina]
</margin>

---

Una bobina cilindrica ha una cosiddetta Induttanza $L$, che si calcola secondo la seguente formula:

$L = \frac{\mu_0 \cdot \mu_r \cdot N^2 \cdot A_S}{l}$

Considerando la struttura di una bobina, troviamo quindi le seguenti grandezze:
1. $\mu_0$ è la costante del campo magnetico, una costante naturale con il valore di $\qty{1,2566e-6}{\henry\per\meter}$. Il valore si può sempre trovare nella raccolta di formule.
2. $\mu_r$ è una costante del materiale, poiché il nucleo della bobina può essere costituito da un materiale speciale che può amplificare i campi magnetici.
3. Il numero $N$ di spire della bobina in filo di rame smaltato o filo di rame argentato.
4. $A_S$ indica l'area della sezione trasversale del nucleo della bobina.
5. Lunghezza della bobina $l$

[question:EA102]

<indepth>
La lettera $L$ della formula è stata scelta in onore del professore Emil Lenz (1804–1864) di San Pietroburgo, che formulò la legge di Lenz, che porta il suo nome.
</indepth>

<unit>
Una bobina possiede l'Induttanza $L$ con l'unità di misura $\qty{1}{\volt\second\per\ampere}$, che viene solitamente indicata in *henry* ($\unit{\henry}$). L'unità prende il nome dal fisico americano *Joseph Henry* (1797–1878). Un'Induttanza di $\qty{1}{\henry}$ si ha quando una variazione di corrente di $\qty{1}{\ampere}$ entro un secondo provoca una tensione di autoinduzione di $\qty{1}{\volt}$. In pratica, i valori delle Induttanze sono solitamente molto inferiori e vengono tipicamente indicati in $\unit{\milli\henry}$, $\unit{\micro\henry}$ o $\unit{\nano\henry}$.
</unit>

---

Utilizzando la formula e le seguenti relazioni qualitative, è già possibile risolvere una serie di domande d'esame:

1. L'Induttanza aumenta quadraticamente con il numero di spire. Se il numero di spire viene raddoppiato, l'Induttanza aumenta di quattro volte.
2. Se la bobina viene compressa, l'Induttanza $L$ aumenta.
3. Se l'area della sezione trasversale viene aumentata, l'Induttanza $L$ aumenta.
4. Se il campo magnetico nella bobina viene amplificato da un materiale adatto, conduttore di magnetismo (ad es. ferro), l'Induttanza $L$ aumenta.

[question:EC305]

Se si comprime la bobina, $l$ viene ridotta. Di conseguenza, l'Induttanza $L$ aumenta.

[question:EC306]

Se si raddoppia la lunghezza della bobina $l$, l'Induttanza $L$ deve dimezzarsi.

[question:EC307]

Se il numero di spire $N$ viene raddoppiato, l'Induttanza $L$ quadruplica.

Se il numero di spire viene ridotto, l'Induttanza diminuisce, ma anche con mezzo giro o un quarto di giro e persino con un pezzo di filo dritto è ancora presente una piccola Induttanza parassita.

[question:EC304]

---

Definiamo *ferromagnetici* una determinata classe di materiali che contengono piccoli magneti elementari a livello atomico, i quali si allineano sotto l'influenza di un campo magnetico esterno, aumentando così fortemente la *densità di flusso magnetico* (di cui però non ci occuperemo ancora in questo momento). Tra gli elementi chimici puri, solo ferro, cobalto e nichel sono ferromagnetici.

<indepth>
$\mu_r$, detta anche permeabilità relativa, è molto grande per i materiali ferromagnetici (per il ferro, ad esempio, nell'intervallo da $300\dots\num{10000}$).
</indepth>


[question:EB204]

Se si introduce un materiale ferromagnetico come il ferro nella bobina, il campo magnetico viene amplificato e l'Induttanza aumenta.

Se invece introduciamo in una bobina cilindrica un nucleo di un metallo buon conduttore (non ferromagnetico) come alluminio o rame, l'Induttanza della bobina diminuisce. Ciò è dovuto al fatto che il campo magnetico ad alta frequenza della bobina genera ("induce") correnti nel nucleo, le cosiddette correnti parassite. Queste correnti secondarie generano a loro volta campi magnetici che contrastano il campo magnetico della bobina. Pertanto, l'Induttanza diminuisce. Il campo magnetico all'interno del nucleo viene ridotto.

La risposta considerata corretta nella seguente domanda è che il campo magnetico non può penetrare nel nucleo e quindi la sezione trasversale del campo viene ridotta. Ma non è esattamente ciò che accade fisicamente. Basta memorizzare la risposta "corretta".

[question:EB205]

---

Come per il condensatore, esaminiamo prima il comportamento della bobina in corrente continua: la bobina viene collegata tramite una resistenza in serie a una fonte di tensione continua, come mostrato nella figura [ref:e_spule_einschalten]. Al momento dell'accensione, l'aumento della corrente viene inizialmente ritardato, in modo che la corrente non aumenti bruscamente, ma solo gradualmente fino al suo valore massimo.

La causa di ciò è la legge di Lenz: durante l'aumento della corrente, la bobina genera una tensione di autoinduzione che contrasta la variazione di corrente – e quindi la causa. In questo modo, l'aumento della corrente viene limitato. Poiché all'inizio non scorre ancora alcuna corrente, inizialmente quasi tutta la tensione applicata cade sulla bobina. Con l'aumento della corrente, questa tensione di induzione diminuisce, mentre la corrente continua ad aumentare.

Una volta raggiunto lo stato stazionario, la bobina si comporta approssimativamente come un pezzo di filo in corrente continua. La tensione che cade su di essa è quindi praticamente nulla. L'andamento temporale della tensione sulla bobina è mostrato nella figura [ref:e_spule_einschalten_spannung].

<margin>
[picture:1016:e_spule_einschalten:Circuito per l'indagine di una bobina]
</margin>
<margin>
[picture:186:e_spule_einschalten_spannung:Andamento della tensione all'accensione]
</margin>

[question:EC301]

---

Nel momento dello spegnimento, la tensione di autoinduzione vuole mantenere il flusso di corrente. La bobina agisce quindi come un generatore, la cui tensione di induzione si genera in direzione opposta alla polarità precedente. Pertanto, la bobina si comporta esattamente in modo opposto al condensatore. Questi processi possono essere ben osservati con un oscilloscopio, come mostrato nella figura [ref:e_Spulenstrom].

<margin>
[photo:257:e_Spulenstrom:Comportamento all'accensione e allo spegnimento della tensione e della corrente della bobina]
</margin>

Si possono quindi utilizzare le bobine anche per creare ritardi. Nella domanda seguente, il flusso di corrente attraverso la lampada 2 aumenta più lentamente che attraverso la lampada 1, poiché è collegata una bobina in serie, la cui tensione di autoinduzione fa aumentare lentamente la corrente di accensione.

[question:EC302]

Similmente al condensatore, una bobina si comporta diversamente se collegata a tensione continua o a tensione alternata. In tecnica radio, è soprattutto importante il comportamento in tensione alternata. Pertanto, esaminiamo ora il comportamento in corrente alternata.

La bobina mostra, analogamente a un condensatore, una resistenza in corrente alternata $X_{\textrm{L}}$, il che significa che, sebbene il filo della bobina abbia solo una resistenza ohmica molto piccola (resistenza del conduttore), scorre una corrente, ma questa diminuisce all'aumentare della frequenza della tensione alternata:

$X_{L} = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$

Dalla formula si può vedere che la resistenza in corrente alternata aumenta con la frequenza crescente e diminuisce con la frequenza decrescente.

[question:EC303]
