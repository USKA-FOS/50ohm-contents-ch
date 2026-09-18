Il terzo componente passivo nella tecnica radio – dopo la resistenza e il condensatore – è la *bobina*. Nelle figure [ref:e_spulen] e [ref:e_schaltsymbole_spulen] sono illustrate diverse tipologie di bobine e i relativi simboli circuitali. Come già appreso nel capitolo sul campo magnetico, in una bobina viene generato un campo magnetico non appena una corrente elettrica fluisce al suo interno. La forma costruttiva più semplice di una bobina è la cosiddetta *bobina cilindrica*, rappresentata nella figura [ref:e_spule_Aufbau].


<margin>
[photo:207:e_spulen:Varie tipologie costruttive di bobine]
[picture:942:e_schaltsymbole_spulen:Simboli circuitali per diverse tipologie di bobine]
[picture:948:e_spule_Aufbau:Struttura di una bobina]
</margin>

---

Una bobina cilindrica possiede una *induttanza* $L$, calcolabile con la seguente formula:


$L = \frac{\mu_0 \cdot \mu_r \cdot N^2 \cdot A_S}{l}$


Analizzando la struttura di una bobina, si identificano le seguenti grandezze:
1. $\mu_0$ è la permeabilità del vuoto, una costante naturale con valore $\qty{1,2566e-6}{\henry\per\meter}$. Il valore può essere sempre consultato nella raccolta di formule.
2. $\mu_r$ è una costante del materiale, poiché il nucleo della bobina può essere realizzato in un materiale specifico in grado di amplificare i campi magnetici.
3. Il numero $N$ di spire della bobina, realizzate con filo di rame smaltato o rame argentato.
4. $A_S$ indica l’area della sezione trasversale del nucleo della bobina.
5. Lunghezza della bobina $l$


[question:EA102]


<indepth>
Il simbolo $L$ è stato scelto in onore del professore Emil Lenz (1804–1864) di San Pietroburgo, che formulò la legge di Lenz.
</indepth>


<unit>
Una bobina possiede un’induttanza $L$ con unità di misura $\qty{1}{\volt\secondo\per\ampere}$, solitamente espressa in *henry* ($\unit{\henry}$). L’unità prende il nome dal fisico statunitense *Joseph Henry* (1797–1878). Un’induttanza di $\qty{1}{\henry}$ si verifica quando una variazione di corrente di $\qty{1}{\ampere}$ in un secondo genera una tensione di autoinduzione di $\qty{1}{\volt}$. In pratica, i valori delle induttanze sono generalmente molto inferiori e vengono tipicamente espressi in $\unit{\milli\henry}$, $\unit{\micro\henry}$ o $\unit{\nano\henry}$.
</unit>

---

Utilizzando la formula e le seguenti relazioni qualitative, è possibile risolvere una serie di domande d’esame:


1. L’induttanza cresce quadraticamente con il numero di spire. Se il numero di spire raddoppia, l’induttanza quadruplica.
2. Se la bobina viene compressa, l’induttanza $L$ aumenta.
3. Se l’area della sezione trasversale viene aumentata, l’induttanza $L$ cresce.
4. Se il campo magnetico nella bobina viene amplificato da un materiale ad alta permeabilità magnetica (ad esempio ferro), l’induttanza $L$ aumenta.

[question:EC305]


Se la bobina viene compressa, $l$ diminuisce. Di conseguenza, l’induttanza $L$ aumenta.


[question:EC306]


Se la lunghezza della bobina $l$ raddoppia, l’induttanza $L$ si dimezza.


[question:EC307]


Se il numero di spire $N$ raddoppia, l’induttanza $L$ quadruplica.


Se il numero di spire viene ridotto, l’induttanza diminuisce, ma anche con mezza spira o un quarto di spira, e persino con un semplice filo dritto, è comunque presente una piccola induttanza parassita.


[question:EC304]


---

Con il termine *ferromagnetico* si indicano particolari materiali che, a livello atomico, contengono piccoli magneti elementari che, sotto l’influenza di un campo magnetico esterno, si allineano e aumentano notevolmente la *densità di flusso magnetico* (argomento che non tratteremo in questa sede). Tra gli elementi chimici puri, solo ferro, cobalto e nichel sono ferromagnetici.


<indepth>
$\mu_r$, detta anche permeabilità relativa, nei materiali ferromagnetici è molto elevata (nel ferro, ad esempio, nell’ordine di $300\dots\num{10000}$).
</indepth>

[question:EB204]


Se si inserisce un materiale ferromagnetico come il ferro nella bobina, il campo magnetico viene amplificato e l’induttanza aumenta. Se invece si inserisce un nucleo realizzato in un metallo buon conduttore (non ferromagnetico) come alluminio o rame, l’induttanza della bobina diminuisce. Questo accade perché il campo magnetico ad alta frequenza della bobina induce correnti, dette correnti parassite, nel nucleo. Queste correnti secondarie generano a loro volta campi magnetici che si oppongono a quelli della bobina. Per questo motivo l’induttanza diminuisce. Il campo magnetico all’interno del nucleo viene così ridotto.

La risposta considerata corretta nella domanda seguente è quella secondo cui il campo magnetico non può penetrare nel nucleo, riducendo così la sezione del campo. Tuttavia, questa non è esattamente ciò che accade fisicamente. Basta ricordare la "risposta corretta".

[question:EB205]


---

Analizziamo, come già fatto per il condensatore, il comportamento della bobina in corrente continua. La bobina viene collegata a un generatore di tensione continua tramite una resistenza in serie, come illustrato nella figura [ref:e_spule_einschalten]. Al momento dell’accensione, l’aumento della corrente viene inizialmente ritardato, per cui la corrente non sale istantaneamente al suo valore massimo, ma gradualmente.

La causa è la legge di Lenz: durante l’aumento della corrente, la bobina genera una tensione di autoinduzione che si oppone alla variazione di corrente – e quindi alla sua causa. Questo limita l’aumento della corrente. Poiché inizialmente non scorre corrente, inizialmente quasi tutta la tensione applicata cade sulla bobina. Con l’aumentare della corrente, questa tensione di induzione diminuisce mentre la corrente continua a salire.

Una volta raggiunto lo stato stazionario, la bobina si comporta, in corrente continua, approssimativamente come un semplice filo. La tensione ai suoi capi è quindi praticamente nulla. L’andamento temporale della tensione sulla bobina è illustrato nella figura [ref:e_spule_einschalten_spannung].


<margin>
[picture:1016:e_spule_einschalten:Circuito per lo studio di una bobina]
</margin>
<margin>
[picture:186:e_spule_einschalten_spannung:Andamento della tensione all’accensione]
</margin>

[question:EC301]


---

Al momento dello spegnimento, la tensione di autoinduzione cerca di mantenere il flusso di corrente. La bobina si comporta quindi come un generatore, la cui tensione di induzione si genera con polarità opposta rispetto a quella precedente. La bobina si comporta quindi esattamente al contrario del condensatore. Questi fenomeni possono essere osservati agevolmente con un oscilloscopio, come illustrato nella figura [ref:e_Spulenstrom].


<margin>
[photo:257:e_Spulenstrom:Comportamento della tensione e della corrente della bobina all’accensione e allo spegnimento]
</margin>

Per questo motivo, le bobine possono essere utilizzate anche per introdurre un *ritardo*. Nella domanda seguente, la corrente attraverso la lampada 2 aumenta più lentamente rispetto a quella attraverso la lampada 1, poiché è presente una bobina in serie la cui tensione di autoinduzione limita lentamente l’aumento della corrente all’accensione.

[question:EC302]


Come per il condensatore, anche la bobina si comporta diversamente se collegata a tensione continua o alternata. Nella tecnica radio, è soprattutto importante il comportamento in corrente alternata. Per questo motivo, analizziamo ora il comportamento in corrente alternata.

La bobina, analogamente al condensatore, presenta una *impedenza* $X_{\textrm{L}}$, vale a dire che, nonostante il filo della bobina possieda solo una piccola resistenza ohmica (resistenza del conduttore), scorre una corrente che diminuisce all’aumentare della frequenza della tensione alternata:


$X_{L} = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$


Dalla formula si deduce che l’impedenza aumenta all’aumentare della frequenza e diminuisce al diminuire della frequenza.


[question:EC303]