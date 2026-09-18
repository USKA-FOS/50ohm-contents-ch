Oltre agli ormai noti accumulatori al piombo (Pb) e agli accumulatori al nichel-metallo idruro (NiMH), nella tecnica radio, ad esempio per l'uso portatile, si utilizzano sempre più spesso gli accumulatori al litio-ferro-fosfato (LiFePO4). Iniziamo quindi con l'analisi di un accumulatore e delle sue etichette nell'immagine [ref:a_akku_lifepo4].


<margin>
[photo:175:a_akku_lifepo4:LiFePO4]
</margin>

<indepth>
* Capacità: $\qty{4200}{\milli\ampere\ora}$
* Tensione: 4S1P / $\qty{13,2}{\volt}$
% * Scarica: 30C Constant / 40C Burst
% * Connettore di bilanciamento: JST-XH
% * Connettore di scarico: $\qty{5.5}{\milli\metro}$ spina a sfera

I dati tecnici più importanti per noi sono la tensione nominale $\qty{13,2}{\volt}$ e il collegamento 4S1P. Questo significa che la tensione nominale di $\qty{13,2}{\volt}$ deriva da 4 celle collegate in serie e 1 volta in parallelo, quindi tutte e 4 collegate in serie. Generalmente, i LiFePO4 hanno una tensione nominale per cella di $\qty{3,2}{\volt}$ fino a $\qty{3,3}{\volt}$. Quindi si ottiene $\qty{3,3}{\volt} \cdot 4 = \qty{13,2}{\volt} \cdot 1 = \qty{13,2}{\volt}$.


Nel caso di un 4S2P sono installate in totale 8 celle: 4 in serie e 2 volte in parallelo. Questo comporterebbe una tensione di $\qty{13,2}{\volt}$, ma una capacità di $\qty{8400}{\milli\ampere\ora}$.


</indepth>

Per l'accumulatore dell'esempio è indicata una capacità nominale di $\qty{4200}{\milli\ampere\ora}$. La capacità nominale $Q$ dell'accumulatore è anche chiamata carica ed è espressa in $\unit{\ampere\ora}$ o $\unit{\milli\ampere\ora}$.


Per il nostro accumulatore di esempio, questo corrisponde a $\qty{4,2}{\ampere\ora}$. Teoricamente, ciò significa che possiamo caricare l'accumulatore per $\qty{1}{\ora}$ con $\qty{4,2}{\ampere}$ o per $\qty{2}{\ora}$ con $\qty{2,1}{\ampere}$, ecc. Questo viene descritto dalla formula:


$t=\frac{Q}{I}$


$t=\frac{\qty{4,2}{\ampere\ora}}{\qty{4,2}{\ampere}} = \qty{1}{\ora}$


[question:AB210]


Ora vogliamo anche sapere quanta energia elettrica è immagazzinata nell'accumulatore. L'energia ($\unit{\watt\ora}$) è la carica $Q$ ($\unit{\ampere\ora}$) dell'accumulatore moltiplicata per la tensione totale $U$ in volt.


$\qty{1}{\watt\ora} = \qty{1}{\ampere\ora} \cdot \qty{1}{\volt}$


Per il nostro esempio calcoliamo $\qty{4,2}{\ampere\ora} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\ora}$ come energia immagazzinata.


[question:AB501]


Nel collegamento in serie di accumulatori, come mostrato nell'immagine [ref:a_akku_4S1P], le tensioni si sommano e la capacità rimane invariata. Nel collegamento in parallelo, come mostrato nell'immagine [ref:a_akku_4S2P], la tensione rimane invariata e le capacità si sommano.


<margin>
% TODO Immagine collegamento in serie disponibile presso DG1HXJ come .tex
[photo:176:a_akku_4S1P:collegamento in serie]
</margin>

<margin>
% TODO Immagine collegamento in parallelo disponibile presso DG1HXJ come .tex
[photo:177:a_akku_4S2P:collegamento in parallelo]
</margin>

<attention>
Quando si utilizza un LiFePO4 collegato come 4S1P, è necessario considerare che le tensioni possono variare tra $\qty{10}{\volt}$ e $\qty{14,4}{\volt}$. Non tutti gli apparecchi radio possono funzionare con queste tensioni. È importante anche collegare solo celle/accumulatori con gli stessi dati tecnici, poiché le celle si influenzano reciprocamente e potrebbero danneggiarsi. In particolare con gli attuali accumulatori al litio, è consigliabile installare un dispositivo di monitoraggio (bilanciatore, monitor della batteria). Questo garantisce, tra l'altro, l'equilibrio necessario delle tensioni delle celle e una carica ottimale.
</attention>

---


Per risolvere la domanda successiva, è necessario sapere che la tensione totale corrisponde alla somma delle tensioni delle singole celle. La carica totale, invece, corrisponde alla carica di una singola cella.

[question:AB209]


Per la domanda successiva, è necessario calcolare prima la quantità di carica prelevabile pari al $\qty{90}{\percento}$.
La durata della scarica $t$ si ottiene da: $t=\frac{Q}{I}$


[question:AB211]