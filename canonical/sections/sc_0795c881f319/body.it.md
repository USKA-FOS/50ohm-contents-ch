% TODO: Se il catalogo delle domande 4 arriva, allora alcune domande qui cadranno via! 

Abbiamo già conosciuto la resistenza elettrica nel contesto della legge di Ohm. Le resistenze possono essere realizzate con materiali diversi. Per questo motivo si distinguono diversi materiali resistivi, ad es.:

- Resistenze a filo
- Resistenze a strato di carbone
- Resistenze a strato metallico
- Resistenze a strato di ossido metallico
- ...

<margin>
| l: Resistenza | X: Proprietà |
| Resistenze a filo | Resistenze per carichi elevati per basse frequenze |
| Resistenze a strato metallico | Basse tolleranze di produzione e dipendenza dalla temperatura, resistenze di precisione |
| Resistenze a strato di ossido metallico | Per frequenze superiori a $\qty{30}{\mega\hertz}$ |
[table:e_eigenschaften_widerstaende:Panoramica delle proprietà]
</margin>

Di seguito esamineremo più da vicino questi materiali - un riassunto è nella tabella [ref:e_eigenschaften_widerstaende].

Le *resistenze a filo* sono tra le forme più antiche di resistenze elettriche. Grazie alle loro proprietà favorevoli - come l'elevata capacità di sovraccarico e il basso coefficiente di temperatura - sono ancora utilizzate oggi. Spesso vengono anche chiamate resistenze avvolte, poiché un filo resistivo isolato con vernice, ad esempio in Manganin o Costantana, viene avvolto su un corpo di avvolgimento in ceramica. Tuttavia, una resistenza a filo avvolta singolarmente agisce sempre anche come una bobina e possiede quindi un'induttanza relativamente elevata. Tratteremo le bobine più in dettaglio in un capitolo successivo; tuttavia, si noti in anticipo che ciò rende l'impedenza della resistenza dipendente dalla frequenza. Nella tecnica radio, questo comportamento è generalmente indesiderato. Pertanto, le resistenze a filo sono adatte principalmente come resistenze per carichi elevati per corrente continua o per applicazioni a basse frequenze.

%EC101 Alto carico bassa frequenza -> Resistenza a filo
[question:EC101]

Nelle resistenze a strato di carbone, un sottile strato di carbone viene vaporizzato su un supporto come materiale resistivo. Le resistenze a strato di carbone sono economiche, ma presentano una tolleranza di produzione relativamente ampia.

Nelle *resistenze a strato di ossido metallico*, il materiale resistivo viene applicato sotto forma di un sottile strato su un materiale di supporto. Questo tipo di resistenza è in gran parte privo di induttanza e presenta una buona stabilità termica, rendendolo particolarmente adatto per l'uso ad alte frequenze superiori a $\qty{30}{\mega\hertz}$.

%EC103 Basso induttanza 30Mhz -> Ossido metallico
[question:EC103]

Le resistenze a *strato metallico* possono essere prodotte con elevata precisione, vale a dire con bassa tolleranza di produzione. Sono adatte come resistenze di precisione. Sono indipendenti dalla temperatura, ma meno prive di induttanza.

%EC102 Resistenza di precisione > Resistenza a strato metallico
[question:EC102]


Abbiamo già conosciuto le antenne artificiali, cioè i carichi fittizi, nella classe N. Per le alte frequenze (ad es. VHF) si consiglia di costruire un carico fittizio preferibilmente con resistenze a strato di ossido metallico non avvolte. Per le frequenze più basse (ad es. $\qty{50}{\mega\hertz}$ o $\qty{28}{\mega\hertz}$), tuttavia, possono essere utilizzate anche resistenze a strato di carbone. L'importante è soprattutto che la resistenza non abbia spire, cioè nessuna autoinduttanza, e quindi non agisca come una bobina parassita, poiché tale induttanza renderebbe il valore della resistenza dipendente dalla frequenza - esattamente ciò che è indesiderato in un carico fittizio. La resistenza dovrebbe essere sempre di circa $\qty{50}{\ohm}$, indipendentemente dalla frequenza. Pertanto, _non_ dovrebbero essere utilizzate resistenze a filo. Anche la capacità parassita dovrebbe essere il più bassa possibile per questo motivo. Inoltre, le resistenze utilizzate devono essere sufficientemente resistenti al calore, poiché convertono la potenza assorbita in calore.

%EC107 DL
[question:EC107]
%EC104 DL
[question:EC104]

Per risolvere le seguenti domande, è necessario sapere che dieci resistenze collegate in parallelo, ciascuna con $\qty{500}{\ohm}$, producono una resistenza totale di $\qty{50}{\ohm}$. Tratteremo questo rapporto più in dettaglio in un capitolo successivo, quando parleremo di collegamenti in serie e in parallelo di resistenze.

%EC106
[question:EC106]
%EC105 DL
[question:EC105]