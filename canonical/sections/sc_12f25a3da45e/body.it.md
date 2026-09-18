Un componente molto importante e ampiamente utilizzato nella tecnica radio e nell'elettronica è il condensatore. Come mostrato nella figura [ref:e_kondensator_aufbau], un condensatore è costituito fondamentalmente da due superfici conduttrici (piastre, strati o elettrodi) separate tra loro da un isolante, il cosiddetto materiale dielettrico.


<margin>
[picture:922:e_kondensator_aufbau:Struttura di principio di un condensatore]
</margin>

Le dimensioni geometriche determinano una proprietà fondamentale di un condensatore: la capacità di immagazzinare cariche elettriche. Questa capacità viene chiamata **capacità** e viene indicata con la lettera $C$. Maggiore è la capacità, più cariche elettriche $Q$ possono essere immagazzinate. Se la tensione applicata viene aumentata, verranno immagazzinate anche più cariche.

La formula seguente mostra la relazione tra queste grandezze:

$Q = C \cdot U$

Questa formula non si trova nella raccolta di formule e non è necessaria per l'esame.

<unit>
L'unità di misura della carica $Q$ è $\unit{\ampere\second}$.
</unit>

<unit>
L'unità di misura della capacità $C$ è $\unit{\ampere\second\per\volt}$ o, in breve, *farad* $\unit{\farad}$ in onore del fisico inglese Michael Faraday (1791 - 1867). $\qty{1}{\farad}$ è la capacità di un condensatore in cui viene immagazzinata una carica di $\qty{1}{\ampere\second}$ a una tensione di $\qty{1}{\volt}$.
</unit>

[question:EA101]

Se si applica una tensione a un condensatore, tra le piastre conduttrici si genera un **campo elettrico** $E$. Questa relazione è già stata trattata nel capitolo sul campo elettrico: maggiore è la tensione applicata e minore è la distanza tra le piastre, più intenso è il campo elettrico. Dal punto di vista matematico, questo può essere espresso come:

$E = \frac{U}{d}$

Per calcolare la capacità del condensatore in base alle sue dimensioni, si utilizza la seguente formula tratta dalla raccolta di formule:

---

$C = \frac{\varepsilon_0 \cdot \varepsilon_r \cdot A}{d}$

Di seguito sono spiegate le singole grandezze della formula:

- $A$ è la superficie delle piastre conduttrici che si fronteggiano
- $d$ è la distanza tra le piastre
- $\varepsilon_0 = \qty{0,855e-11}{\ampere\second\per\volt\meter}$ è la **costante dielettrica del vuoto**, una costante naturale
- $\varepsilon_r$ (si legge "Epsilon R") è una proprietà specifica dell'isolante (materiale dielettrico) ed è chiamata **costante dielettrica relativa**, che dipende dal materiale utilizzato. La tabella [ref:e_Dielektrizitätszahl] con i valori dei materiali è disponibile anche nella raccolta di formule.

<margin>
| Materiale | $\varepsilon_r$ |
| aria (secca) | 1,00059 |
| PE solido (polietilene) | 2,29 |
| schiuma PE | 1,5 |
| PTFE (Teflon) | 2,0 |
[table:e_Dielektrizitätszahl:Costante dielettrica relativa $\varepsilon_r$]
</margin>

Con l'aiuto di questa formula, è possibile risolvere una serie di domande d'esame. Innanzitutto, si nota che la tensione $U$ non compare nella formula.

[question:EC205]

La capacità di un condensatore diminuisce se aumenta la distanza tra le piastre.

[question:EC204]
[question:EC203]

---

Consideriamo ora il condensatore in corrente continua. Nella figura [ref:e_stromkreis_kondensator] è rappresentato un circuito per la carica di un condensatore. Si suppone che il condensatore $C$ sia inizialmente scarico, cioè non abbia ancora immagazzinato alcuna carica elettrica. Quando l'interruttore viene chiuso, il condensatore $C$ viene collegato a una sorgente di tensione continua (batteria) tramite una resistenza $R$.

Grazie alla tensione applicata, tra le piastre del condensatore si genera un campo elettrico. Questo campo provoca una ridistribuzione delle cariche: gli elettroni vengono spinti dal polo negativo della sorgente di tensione verso la piastra del condensatore collegata, creando un eccesso di elettroni su di essa. Contemporaneamente, gli elettroni vengono sottratti dalla piastra opposta verso il polo positivo della sorgente di tensione, generando una carenza di elettroni su di essa. Sebbene non ci sia passaggio di corrente attraverso il materiale dielettrico, questa separazione di cariche porta alla carica del condensatore.

<margin>
[picture:1015:e_stromkreis_kondensator:Circuito per la carica di un condensatore]
</margin>

---

Ciò significa che inizialmente scorre una corrente elevata, limitata solo dalla resistenza $R$. Con il passare del tempo, sempre più cariche vengono immagazzinate nel condensatore. Di conseguenza, la corrente diminuisce continuamente, mentre la tensione $U_C$ ai capi del condensatore aumenta fino a quando il condensatore è completamente carico. A questo punto, la corrente cessa del tutto.

Tuttavia, questo processo non avviene istantaneamente, ma con un ritardo temporale. La tensione del condensatore aumenta secondo una funzione esponenziale, come mostrato nella figura [ref:e_ladekurve_c]. La durata di questo processo di carica dipende dalla resistenza in serie: maggiore è la resistenza, più tempo impiega il condensatore a caricarsi "completamente". Con un oscilloscopio, come mostrato nella figura [ref:e_lade_entladespannung_mit_oszilloskop] e già trattato in precedenza, è possibile osservare e analizzare visivamente questo andamento temporale.

<margin>
[picture:185:e_ladekurve_c:Tensione di carica di un condensatore]
</margin>

<margin>
[photo:247:e_lade_entladespannung_mit_oszilloskop:Tensione di carica e scarica di un condensatore]
</margin>

Durante la scarica, la corrente fluisce in direzione opposta a quella di carica e la tensione ai capi del condensatore diminuisce lentamente.

[question:EC201]

Nel caso di corrente alternata e tensioni alternate, dobbiamo considerare un ulteriore aspetto importante: un condensatore si comporta come una resistenza dipendente dalla frequenza. Questo può essere descritto dalla relazione

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

e viene chiamata **reattanza capacitiva** $X_C$ (cfr. raccolta di formule).

I dettagli fisici di questo comportamento verranno approfonditi solo nel corso di classe A. Tuttavia, per la classe E è già importante sapere che la resistenza di un condensatore è inversamente proporzionale alla frequenza: se si riduce la frequenza, la reattanza capacitiva $X_C$ aumenta. Se invece si aumenta la frequenza, la resistenza diminuisce di conseguenza.

[question:EC202]

---

Abbiamo già imparato alcune proprietà elettriche fondamentali di un condensatore e ora ci concentreremo sulle diverse varianti costruttive. La figura [ref:e_kondensatorvarianten] mostra diverse tipologie di condensatori.

<margin>
[photo:206:e_kondensatorvarianten:Varianti di condensatori]
</margin>

Come materiale dielettrico, cioè strato isolante, possono essere utilizzati materiali diversi:

1. Aria nei condensatori variabili o trimmer ad aria
2. Pellicola di plastica nei condensatori a pellicola avvolti
3. Ceramica per condensatori ad alta frequenza con alto fattore di qualità e nei condensatori SMD
4. Ossido metallico nei condensatori elettrolitici.

A seconda della struttura, si distinguono inoltre:

* Condensatori fissi come condensatori ceramici, a pellicola e elettrolitici
* Condensatori variabili come condensatori variabili e trimmer

---

I *condensatori ad aria* e i *condensatori ceramici*, come mostrato nella figura [ref:e_aufbau_keramik_c], vengono spesso utilizzati, ad esempio, per filtri ad alta frequenza.
[question:ED216]

<margin>
[picture:923:e_aufbau_keramik_c: Condensatore ceramico]
</margin>

I *condensatori elettrolitici* (abbreviato ELKO) contengono una sottile lamina di alluminio ruvida immersa in un elettrolita (ad esempio borace). L'elettrolita provoca un'ossidazione chimica della superficie dell'alluminio. Lo strato di ossido che si forma è molto sottile e, di conseguenza, la capacità aumenta notevolmente a parità di dimensioni. Tuttavia, questo sottile strato ha una tenuta in tensione limitata, che viene indicata sull'ELKO stesso.
I condensatori elettrolitici possono essere utilizzati solo con tensione continua. La polarità deve essere rispettata, poiché in caso contrario lo strato di ossido si degrada, riducendo la tenuta in tensione. Il condensatore viene distrutto. Tutti gli altri condensatori possono essere collegati anche a tensione alternata.
[question:EC207]

%<margin>
%TODO: Immagine ELKO
%</margin>

Nei condensatori a pellicola avvolti, le materie plastiche vengono lavorate in processi speciali per ottenere pellicole estremamente sottili, dotate di elettrodi e poi avvolte in un rotolo o assemblate in strati singoli per formare un condensatore, come mostrato nella figura [ref:e_aufbau_wickel_c]. Insieme ai condensatori ceramici e ai condensatori elettrolitici, rappresentano una delle tipologie di condensatori più utilizzate.

<margin>
[picture:49:e_aufbau_wickel_c:Condensatore a pellicola avvolto]
</margin>

I condensatori variabili vengono spesso utilizzati negli stadi finali e nei circuiti di adattamento. In questi dispositivi, una parte delle piastre del condensatore è montata su un asse isolato e ruota tra piastre fisse. In questo modo, varia la superficie efficace di sovrapposizione delle piastre e, di conseguenza, la capacità, come mostrato nella figura [ref:e_drehkondensator]. I trimmer funzionano secondo un principio simile, ma non sono destinati a regolazioni frequenti. Servono piuttosto per la messa a punto occasionale o la calibrazione dei circuiti, ad esempio durante la messa in servizio.

[question:EC206]

<margin>
[picture:840:e_drehkondensator:Struttura di un condensatore variabile]
</margin>

I diversi simboli di circuito utilizzati per i vari tipi di condensatori sono mostrati nella figura [ref:e_kondensator_schaltzeichen].

<margin>
[picture:924:e_kondensator_schaltzeichen:Simboli di circuito di diversi tipi di condensatori]

Assegnazione dei simboli di circuito:

a) Condensatore fisso
b) Condensatore polarizzato / condensatore elettrolitico (ELKO) / condensatore al tantalio
c) Condensatore variabile (variabile)
d) Trimmer per scopi di taratura
</margin>
