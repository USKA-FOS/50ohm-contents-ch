Accanto alle note batterie al piombo (Pb) e al nichel-metallo idruro (NiMH), nella tecnica delle radiofrequenze, ad esempio per l'uso portatile, utilizziamo sempre più spesso batterie agli ioni di litio-ferro-fosfato (LiFePO4). Diamo un'occhiata prima a una batteria e alle sue iscrizioni nella figura [ref:a_akku_lifepo4].

<margin>
[photo:175:a_akku_lifepo4:LiFePO4]
</margin>

<indepth>
* Capacità: $\qty{4200}{\milli\ampere\hour}$
* Tensione: 4S1P / $\qty{13,2}{\volt}$
% * Scarica: 30C costante / 40C burst
% * Connettore di bilanciamento: JST-XH
% * Connettore di scarica: connettore a sfera da $\qty{5.5}{\milli\meter}$

I dati più importanti per noi sono la tensione nominale di $\qty{13,2}{\volt}$ e la configurazione 4S1P. Ciò significa che la tensione nominale di $\qty{13,2}{\volt}$ è composta da 4 celle in serie e 1 cella in parallelo, ovvero tutte e 4 sono collegate in serie. Normalmente le LiFePO4 hanno una tensione nominale di cella compresa tra $\qty{3,2}{\volt}$ e $\qty{3,3}{\volt}$. E quindi si ottiene $\qty{3,3}{\volt} \cdot 4 = \qty{13,2 }{\volt} \cdot 1 = \qty{13,2}{\volt}$.

In un 4S2P sono installate in totale 8 celle. 4 in serie e 2 volte in parallelo. Ciò darebbe una tensione di $\qty{13,2}{\volt}$ ma una capacità di $\qty{8400}{\milli\ampere\hour}$.

</indepth>

Nell'esempio di batteria, la capacità nominale indicata è di $\qty{4200}{\milli\ampere\hour}$. La capacità nominale della batteria $Q$ è chiamata anche carica ed è indicata in $\unit{\ampere\hour}$ o $\unit{\milli\ampere\hour}$.

Per il nostro esempio, ciò corrisponde a $\qty{4,2}{\ampere\hour}$. Ciò significherebbe teoricamente che possiamo caricare la nostra batteria con $\qty{4,2}{\ampere}$ per $\qty{1}{\hour}$ o con $\qty{2,1}{\ampere}$ per $\qty{2}{\hour}$, ecc. Questo è descritto dalla formula:

$t=\frac{Q}{I}$

$t=\frac{\qty{4,2}{\ampere\hour}}{\qty{4,2}{\ampere}} = \qty{1}{\hour}$

[question:AB210]

Ora vogliamo anche sapere quanta energia elettrica è immagazzinata nella batteria. L'energia ($\unit{\watt\hour}$) è la carica $Q$ ($\unit{\ampere\hour}$) della batteria moltiplicata per la tensione totale $U$ in volt.

$\qty{1}{\watt\hour} = \qty{1}{\ampere\hour} \cdot \qty{1}{\volt}$

Per il nostro esempio, calcoliamo $\qty{4,2}{\ampere\hour} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\hour}$ come energia immagazzinata.

[question:AB501]

%La scarica di questa batteria può avvenire con una corrente di scarica costante di "30 C". Ciò significa che la batteria può essere scaricata con 30 volte la capacità Q.
%
%Corrente di scarica: $I = 30 \cdot \qty{4200}{\milli\ampere} = \qty{126}{\ampere}$
%
%Tuttavia, questo è solo un valore teoricamente possibile, poiché la nostra batteria si scaricherebbe in $\qty{108}{\second}$. Anche la sezione del cavo deve essere considerata.
%

Nella serie o collegamento in serie di batterie, come nella figura [ref:a_akku_4S1P], le tensioni si sommano e la capacità rimane la stessa. 
Nel collegamento in parallelo, come nella figura [ref:a_akku_4S2P], la tensione rimane la stessa e le capacità si sommano. 

<margin>
% TODO L'immagine del collegamento in serie è disponibile da DG1HXJ come .tex
[photo:176:a_akku_4S1P:Collegamento in serie]
</margin>

<margin>
% TODO L'immagine del collegamento in parallelo è disponibile da DG1HXJ come .tex
[photo:177:a_akku_4S2P:Collegamento in parallelo]
</margin>

<attention>
Nota che quando si utilizza una LiFePO4 configurata come 4S1P, possono essere presenti tensioni comprese tra $\qty{10}{\volt}$ e $\qty{14,4}{\volt}$. Non tutte le apparecchiature radio possono funzionare con queste tensioni. È anche importante che combiniamo solo celle/batterie con dati uguali, poiché le celle si influenzano reciprocamente e altrimenti potrebbero danneggiarsi. Soprattutto con gli attuali accumulatori al litio, è consigliabile installare un'unità di monitoraggio (bilanciatore, monitor batteria). Questo garantisce, tra l'altro, il necessario bilanciamento delle tensioni delle celle e una carica ottimale.
</attention>

---


% Nella fig. [ref:a_akku_lifepo4_anschluss]
% TODO L'immagine della scatola informativa sui collegamenti della batteria è disponibile da DG1HXJ come .tex
%<margin>
%[photo:178:a_akku_lifepo4_anschluss:Collegamenti LiFePO4]
%</margin>

Per risolvere la seguente domanda, è necessario sapere che la tensione totale corrisponde alla somma delle tensioni delle celle. La carica totale, invece, corrisponde alla carica di una cella.

[question:AB209]

Per la prossima domanda, è necessario determinare prima la quantità di carica estraibile del $\qty{90}{\percent}$.
Il tempo di scarica $t$ si ottiene da: $t=\frac{Q}{I}$

[question:AB211]
