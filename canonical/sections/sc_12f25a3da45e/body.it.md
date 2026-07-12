Un componente molto importante e di uso frequente nella tecnica radio e nell'elettronica è il condensatore. Come mostrato nella figura [ref:e_kondensator_aufbau], un condensatore consiste fondamentalmente di due superfici conduttrici (piastre, strati o elettrodi), separate da un isolante, il cosiddetto dielettrico.


<margin>
[picture:922:e_kondensator_aufbau:Struttura di base di un condensatore]
</margin>

Le dimensioni geometriche determinano una proprietà importante di un condensatore, ovvero la capacità di immagazzinare cariche. Questa capacità è chiamata capacità e il suo simbolo è $C$. Maggiore è la capacità, maggiori sono le cariche elettriche $Q$ che possono essere immagazzinate. Se la tensione applicata viene aumentata, vengono immagazzinate anche più cariche.

La seguente formula mostra la relazione. 

$Q = C \cdot U $ 

Questa formula non si trova nella raccolta di formule e non è necessaria per l'esame.

<unit>
L'unità di misura della carica $Q$ è $\unit{\ampere\second}$
</unit>

<unit>
L'unità di misura della capacità $C$ è $\unit{\ampere\second\per\volt}$ o, in breve, *farad* $\unit{\farad}$, in onore del fisico inglese Michael Faraday (1791-1867). $\qty{1}{\farad}$ è la capacità di un condensatore in cui viene immagazzinata una carica di $\qty{1}{\ampere\second}$ a una tensione di $\qty{1}{\volt}$.
</unit>

[question:EA101]

Quando viene applicata una tensione a un condensatore, si crea un campo elettrico $E$ tra le piastre conduttrici. Abbiamo già incontrato questa relazione nel capitolo sul campo elettrico: maggiore è la tensione applicata e minore è la distanza tra le piastre, più forte è il campo elettrico. Matematicamente, ciò può essere espresso come:

$E = \frac{U}{d}$

Per calcolare la capacità del condensatore dalle dimensioni, viene utilizzata la seguente formula dalla raccolta di formule:

---

$C = \frac{\varepsilon_0 \cdot \varepsilon_r \cdot A}{d}$

Di seguito sono riportate le singole grandezze della formula:

- $A$ è l'area opposta delle piastre conduttrici
- $d$ è la distanza tra le superfici
- $\varepsilon_0 = \qty{0,855e-11}{\ampere\second\per\volt\meter}$ è la costante dielettrica del vuoto, una costante naturale
- $\varepsilon_r$ (si legge "Epsilon R") è una proprietà speciale dell'isolante (dielettrico), chiamata costante dielettrica relativa, che dipende dal materiale utilizzato. La tabella [ref:e_Dielektrizitätszahl] con i valori dei materiali si trova anche nella raccolta di formule.

<margin>
| Materiale | $\varepsilon_r$  |
| Aria (secca) | 1,00059 |
| PE solido (polietilene) | 2,29 |
| Schiuma PE | 1,5 |
| PTFE (Teflon) | 2,0 |
[table:e_Dielektrizitätszahl:Costante dielettrica relativa $\varepsilon_r$ ]
</margin>

Con l'aiuto della formula, è già possibile risolvere una serie di domande d'esame. Si osserva innanzitutto che la tensione $U$ non compare nella formula. 

[question:EC205]

La capacità di un condensatore diminuisce all'aumentare della distanza tra le piastre. 

[question:EC204]
[question:EC203]

---

Consideriamo innanzitutto il condensatore nel caso di corrente continua. Nella figura [ref:e_stromkreis_kondensator] è mostrato un circuito per la carica di un condensatore. Si presume che il condensatore $C$ sia inizialmente scarico, cioè non abbia ancora immagazzinato alcuna carica elettrica. Se l'interruttore viene chiuso, il condensatore $C$ viene collegato a una fonte di tensione continua (batteria) tramite una resistenza $R$.

La tensione applicata crea un campo elettrico tra le piastre del condensatore. Questo campo provoca una riorganizzazione delle cariche: gli elettroni vengono spinti dal polo negativo della fonte di tensione sulla piastra del condensatore collegata, formando un eccesso di elettroni. Contemporaneamente, gli elettroni vengono attratti dalla piastra opposta verso il polo positivo della fonte di tensione, creando una carenza di elettroni. Sebbene non scorra corrente attraverso il dielettrico, questa separazione di carica porta alla carica del condensatore. 

<margin>
[picture:1015:e_stromkreis_kondensator:Circuito per la carica di un condensatore]
</margin>

---

Ciò significa che all'inizio scorre una corrente elevata, limitata solo dalla resistenza $R$. Con il tempo, sempre più cariche vengono immagazzinate nel condensatore. Di conseguenza, la corrente diminuisce continuamente, mentre la tensione $U_C$ sul condensatore aumenta fino a quando questo non è completamente carico. In questo stato, alla fine non scorre più corrente.

Questo processo, tuttavia, non avviene istantaneamente, ma con un ritardo temporale. La tensione del condensatore aumenta secondo una cosiddetta funzione esponenziale, come mostrato nella figura [ref:e_ladekurve_c]. La durata di questo processo di carica dipende dalla resistenza collegata in serie: maggiore è la resistenza, maggiore è il tempo necessario affinché il condensatore sia "completamente" carico. Con un oscilloscopio, come mostrato nella figura [ref:e_lade_entladespannung_mit_oszilloskop], che abbiamo già incontrato, questo andamento temporale può essere osservato e studiato in modo efficace.

<margin>
[picture:185:e_ladekurve_c:Tensione di carica di un condensatore]
</margin>

<margin>
[photo:247:e_lade_entladespannung_mit_oszilloskop:Tensione di carica e scarica su un condensatore]  
</margin>
 
Durante il processo di scarica, la corrente scorre nella direzione opposta alla corrente di carica e la tensione sul condensatore diminuisce lentamente.

[question:EC201]

Nel caso di corrente alternata e tensioni alternate, dobbiamo considerare un altro aspetto importante: un condensatore si comporta come una resistenza dipendente dalla frequenza. Questa può essere descritta dalla relazione

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

e è chiamata reattanza capacitiva $X_C$ (cfr. raccolta di formule).

Le esatte basi fisiche di ciò verranno apprese solo nella classe A. Per la classe E, tuttavia, è già importante sapere che la resistenza di un condensatore è inversamente proporzionale alla frequenza: se si diminuisce la frequenza, la reattanza capacitiva $X_C$ aumenta. Se invece si aumenta la frequenza, la resistenza diminuisce di conseguenza.

[question:EC202]

---

Abbiamo ora appreso alcune proprietà elettriche fondamentali di un condensatore e di seguito esamineremo le diverse forme costruttive. La figura [ref:e_kondensatorvarianten] mostra diverse varianti di condensatori.

<margin>
[photo:206:e_kondensatorvarianten:Varianti di condensatori]
</margin>

Come dielettrico, cioè strato isolante, possono essere utilizzati diversi materiali:

1. Aria nel condensatore variabile ad aria o trimmer ad aria
2. Pellicola di plastica nel condensatore a film avvolto
3. Ceramica per condensatori ad alta frequenza con alto fattore di qualità e per condensatori SMD.
4. Ossido metallico nel condensatore elettrolitico.

A seconda della costruzione, si distingue inoltre tra:

* Condensatori fissi sotto forma di condensatori ceramici, condensatori a film e condensatori elettrolitici
* Condensatori variabili sotto forma di condensatori variabili e trimmer

---

I *condensatori ad aria* e i *condensatori ceramici*, come mostrato nella figura [ref:e_aufbau_keramik_c], sono spesso utilizzati, ad esempio, per filtri ad alta frequenza. 
[question:ED216] 

<margin>
[picture:923:e_aufbau_keramik_c: Condensatore ceramico]
</margin>

I *condensatori elettrolitici* (in breve ELKO) contengono una sottile lamina di alluminio ruvida, immersa in un elettrolita (ad esempio, borace). L'elettrolita provoca un'ossidazione chimica della superficie dell'alluminio. Lo strato di ossido risultante è molto sottile, il che porta a un forte aumento della capacità con dimensioni ridotte. Tuttavia, lo strato sottile ha solo una resistenza di tensione limitata, che è indicata sull'ELKO.
I condensatori elettrolitici possono essere utilizzati solo con tensione continua. Pertanto, è necessario prestare attenzione alla polarità, altrimenti lo strato di ossido si degrada e la resistenza di tensione diminuisce. Il condensatore viene distrutto. Tutti gli altri condensatori possono essere collegati anche a tensione alternata.
[question:EC207]

%<margin>
%TODO: Immagine Elko
%</margin>

Per i condensatori a film avvolto, le materie plastiche vengono trasformate in pellicole estremamente sottili mediante processi speciali, dotate di elettrodi e quindi avvolte a spirale o stratificate da singoli strati e assemblate in un condensatore, come mostrato nella figura [ref:e_aufbau_wickel_c]. Oltre ai condensatori ceramici ed elettrolitici, sono tra i tipi di condensatori più utilizzati.

<margin>
[picture:49:e_aufbau_wickel_c:Condensatore a film avvolto]
</margin>

I condensatori variabili sono spesso utilizzati negli stadi finali e nelle reti di adattamento. La loro capacità può essere regolata ruotando una parte delle piastre del condensatore su un asse isolato tra le piastre fisse. Ciò modifica l'area di sovrapposizione effettiva delle piastre e quindi la capacità, come mostrato nella figura [ref:e_drehkondensator]. I trimmer funzionano secondo un principio simile, ma non sono destinati a una regolazione continua. Servono piuttosto per la calibrazione occasionale o una tantum dei circuiti, ad esempio durante la messa in servizio o la calibrazione.

[question:EC206]

<margin>
 [picture:840:e_drehkondensator:Struttura di un condensatore variabile]
</margin>

I simboli di circuito utilizzati per i diversi condensatori differiscono anche, come mostrato nella figura [ref:e_kondensator_schaltzeichen].

<margin>
[picture:924:e_kondensator_schaltzeichen:Simboli di circuito di diversi tipi di condensatori]

Assegnazione dei simboli di circuito: 
a) Condensatore fisso 
b) Condensatore polarizzato/Condensatore elettrolitico (Elko)/Condensatore al tantalio
c) Condensatore variabile (Drehko) 
d) Trimmer per scopi di calibrazione
</margin>
