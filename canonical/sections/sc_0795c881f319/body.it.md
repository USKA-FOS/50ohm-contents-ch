% TODO: Quando arriverà il nuovo questionario, alcune domande verranno eliminate!

Abbiamo già incontrato la resistenza elettrica nel contesto della legge di Ohm. Le resistenze possono essere realizzate con materiali diversi. Per questo motivo si distinguono diversi materiali per resistenze, ad esempio:


- Resistenze a filo
- Resistenze a strato di carbone
- Resistenze a strato metallico
- Resistenze a strato di ossido metallico
- ...

<margin>
| l: Resistenza | X: Caratteristica |
| Resistenze a filo | Resistenze di potenza per basse frequenze |
| Resistenze a strato metallico | Bassa tolleranza di fabbricazione e dipendenza dalla temperatura, resistenze di precisione |
| Resistenze a strato di ossido metallico | Per frequenze superiori a $\qty{30}{\mega\hertz}$ |
[table:e_eigenschaften_widerstaende:Panoramica delle caratteristiche]
</margin>

Nei paragrafi seguenti approfondiremo questi materiali; una sintesi è riportata nella tabella [ref:e_eigenschaften_widerstaende].


Le *resistenze a filo* sono tra le forme più antiche di resistenze elettriche. Grazie alle loro proprietà vantaggiose – come l’elevata capacità di carico e il basso coefficiente di temperatura – vengono ancora utilizzate oggi. Spesso sono chiamate anche resistenze avvolte, poiché un filo resistivo isolato (ad esempio in manganina o costantana) viene avvolto su un supporto in ceramica. Tuttavia, una resistenza a filo avvolto in modo semplice funziona anche come bobina e presenta quindi un’elevata induttanza. Le bobine verranno trattate in un capitolo successivo; anticipiamo solo che, a causa di ciò, l’impedenza della resistenza diventa dipendente dalla frequenza. Nella tecnica radio questo comportamento è generalmente indesiderato. Pertanto, le resistenze a filo sono adatte principalmente come resistenze di potenza per corrente continua o per applicazioni a basse frequenze.

%EC101 Resistenze di potenza per basse frequenze -> Resistenza a filo
[question:EC101]

Nelle *resistenze a strato di carbone* uno strato sottile di carbone viene depositato per evaporazione su un supporto. Le resistenze a strato di carbone sono economiche, ma presentano una tolleranza di fabbricazione relativamente ampia.

Nelle *resistenze a strato di ossido metallico* il materiale resistivo viene applicato sotto forma di uno strato sottile su un materiale di supporto. Questo tipo di resistenza è pressoché privo di induttanza e presenta una buona stabilità termica, il che le rende particolarmente adatte per l’impiego a frequenze più elevate, superiori a $\qty{30}{\mega\hertz}$.

%EC103 Prive di induttanza 30 MHz -> Resistenza a strato di ossido metallico
[question:EC103]

Le *resistenze a strato metallico* possono essere prodotte con elevata precisione, cioè con bassa tolleranza di fabbricazione. Sono adatte come resistenze di precisione. Sono indipendenti dalla temperatura, ma meno prive di induttanza.

%EC102 Resistenza di precisione -> Resistenza a strato metallico
[question:EC102]


Le *antenne artificiali*, cioè i carichi fittizi, li abbiamo già incontrati nella classe N. Per alte frequenze (ad esempio VHF) si consiglia di costruire un carico fittizio preferibilmente con resistenze a strato di ossido metallico non avvolte. Per frequenze più basse (ad esempio $\qty{50}{\mega\hertz}$ o $\qty{28}{\mega\hertz}$) possono essere utilizzate anche resistenze a strato di carbone. Ciò che conta è soprattutto che la resistenza non abbia avvolgimenti, cioè non presenti induttanza propria, e quindi non si comporti come una bobina parassita, poiché una tale induttanza renderebbe il valore della resistenza dipendente dalla frequenza – proprio questo è indesiderato in un carico fittizio. La resistenza deve mantenere un valore di circa $\qty{50}{\ohm}$ indipendentemente dalla frequenza. Per questo motivo *non* devono essere utilizzate resistenze a filo. Anche la capacità parassita dovrebbe essere il più bassa possibile per questo motivo. Inoltre, le resistenze impiegate devono essere sufficientemente resistenti alla temperatura, poiché dissipano la potenza assorbita sotto forma di calore.

%EC107 Carico fittizio
[question:EC107]
%EC104 Carico fittizio
[question:EC104]

Per risolvere le domande seguenti è necessario sapere che dieci resistenze da $\qty{500}{\ohm}$ collegate in parallelo danno una resistenza totale di $\qty{50}{\ohm}$. Approfondiremo questo concetto in un capitolo successivo, quando parleremo di collegamenti in serie e in parallelo di resistenze.

%EC106
[question:EC106]
%EC105 Carico fittizio
[question:EC105]