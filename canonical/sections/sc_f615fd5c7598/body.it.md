I Transistor hanno una *caratteristica* che rappresenta la *relazione tra il segnale di ingresso (tensione base-emettitore o gate-source) e il segnale di uscita (corrente di collettore/drenaggio)*. Ci sono diverse sezioni nell'area della caratteristica in cui il transistor ha una *caratteristica lineare o non lineare*.
Le aree lineari della caratteristica, in cui una variazione della grandezza di controllo provoca una variazione proporzionale della grandezza di uscita, sono definite lineari.
Altre aree della caratteristica, in cui una variazione della grandezza di controllo **non** provoca una variazione proporzionale della grandezza di uscita, sono definite non lineari.

<margin>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Caratteristica di un transistor con punti di funzionamento]  
</margin>

Per un funzionamento ottimale dell'amplificatore in termini di rendimento e assenza di armoniche del segnale amplificato, è necessaria una scelta ottimale del punto di funzionamento dell'amplificatore sulla sua caratteristica.
Questo punto di funzionamento è determinato da una tensione ausiliaria appropriata (tensione di polarizzazione) sulla base o sul gate.

L'amplificazione del segnale di ingresso avviene quindi attorno al punto di funzionamento desiderato, che definisce il centro dell'area di lavoro.
La scelta del punto di funzionamento determina una corrente di riposo corrispondente del transistor. Questa scorre anche in assenza di un segnale di ingresso. La corrente di riposo influenza in modo significativo l'efficienza di un amplificatore, poiché aumenta la sua potenza dissipata termica e quindi ne riduce il rendimento.

Tutti i segnali la cui informazione di modulazione si trova nella loro ampiezza devono essere amplificati linearmente per trasmettere l'informazione trasmessa senza distorsioni (SSB, AM, ecc.). I segnali la cui informazione di modulazione non si trova nell'ampiezza ma solo nella frequenza possono essere amplificati anche nella zona non lineare di un amplificatore (FM, ecc.) e successivamente filtrati.

A seconda del modo operativo, si distinguono i possibili punti di funzionamento e la loro denominazione sulla caratteristica (vedi figura [ref:a_kennlinien_transistor_arbeitspunkt] ):

AP1: Classe C dell'amplificatore
- senza tensione di polarizzazione
- corrente di riposo nulla
- rendimento ca. $\qtyrange{80}{87}{\percent}$
- elevata componente armonica

AP2: Classe B dell'amplificatore
- Bassa tensione di polarizzazione fino all'inizio della corrente di collettore
- corrente di riposo quasi nulla (bassa)
- rendimento ca. fino a $\qty{80}{\percent}$
- bassa componente armonica

AP3: Classe A/B dell'amplificatore
- Tensione di polarizzazione più alta rispetto alla classe B, ma inferiore rispetto alla classe A
- corrente di riposo maggiore rispetto alla classe B, ma significativamente inferiore rispetto alla classe A
- rendimento tra $\qty{50}{\percent}$ e $\qty{80}{\percent}$
- bassa componente armonica

AP4: Classe A dell'amplificatore
- La tensione di polarizzazione è scelta in modo tale che la corrente di riposo raggiunga circa il $\qty{50}{\percent}$ del valore massimo consentito
- rendimento ca. $\qty{40}{\percent}$
- componente armonica molto bassa

[question:AD416]
[question:AD419]
[question:AD420]
[question:AD421]

La potenza d'uscita di un amplificatore può essere calcolata approssimativamente conoscendo il punto di funzionamento e quindi il suo rendimento approssimativo. Innanzitutto, si calcola la potenza di corrente continua dal prodotto di tensione e corrente fornita all'amplificatore. Successivamente, si moltiplica questa potenza per il fattore numerico del rendimento, dove $\qty{100}{\percent}$ corrisponde a un rendimento di $1$. Ad esempio, un rendimento del $\qty{40}{\percent}$ corrisponde a un fattore di $0,4$.

[question:AD424]
[question:AD425]
[question:AD418]
[question:AD417]

Affinché un amplificatore possa essere utilizzato per il funzionamento SSB (amplificazione lineare), il suo punto di funzionamento deve trovarsi in classe A/AB o B. Fondamentalmente, il funzionamento in classe A è possibile grazie all'elevata linearità, ma non è efficiente ad alte potenze. In questo caso, si collegano 2 transistor in una cosiddetta configurazione push-pull, in modo che ciascuno dei due transistor amplifichi solo una semionda (positiva o negativa). Ciò consente anche il funzionamento AB o B con un rendimento aumentato dell'amplificatore.
Nel funzionamento in classe C, tuttavia, il segnale viene sempre distorto. Pertanto, un trasmettitore SSB non può funzionare in classe C.
In particolare nel funzionamento AB o B di un amplificatore, è necessario evitare la sovraeccitazione, poiché questa può portare rapidamente a distorsioni del segnale. Nel caso di SSB, queste si manifestano sotto forma di splatter su frequenze adiacenti.

[question:AD422]
[question:AJ218]
[question:AD423]

Gli amplificatori in classe C generano elevate componenti armoniche a causa del loro punto di funzionamento fortemente non lineare, che devono essere soppresse nel percorso del segnale successivo, ad esempio tramite filtraggio (filtro passa-basso).
Poiché negli amplificatori di potenza in classe C sono presenti anche componenti armoniche con elevate ampiezze e potenze nell'amplificatore e nel filtro successivo, sia l'amplificatore che il filtro devono essere utilizzati in un involucro metallico ben schermato, in modo da non causare disturbi dovuti alle componenti armoniche.

[question:AF402]
[question:AF403]


