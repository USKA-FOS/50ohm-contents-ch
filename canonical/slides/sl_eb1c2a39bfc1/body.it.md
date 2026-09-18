## Transistor bipolare


[picture:864:a_bauelemente_bipolartransistor:Schema di un transistor bipolare npn e pnp con collettore (C), base (B) ed emettitore (E)]

* Tre zone semiconduttrici
* Dotate alternativamente di tipo n e p
* Transistor npn e pnp

---
[question:AC503]
---
[question:AC504]
---
### Controllo della corrente e fattore di amplificazione

* La tensione base-emettitore $U_{\textrm{BE}}$ controlla in modo esponenziale la corrente di collettore $I_{\textrm{C}}$
* Nel transistor bipolare scorre sempre una corrente di base $I_{\textrm{B}}$ che dipende in modo esponenziale da $U_{\textrm{BE}}$
* Il fattore $B$ è il *coefficiente di amplificazione di corrente* del transistor
* È compreso tra circa 20 e 500

<fragment>
$B = \frac{I_{\textrm{C}}}{I_{\textrm{B}}}$
</fragment>

<note>
Un fattore più elevato richiede una corrente di base minore per controllare una corrente di collettore maggiore
</note>
---
[question:AC501]
---
### Transistor bipolare in conduzione

* Scorre una corrente di collettore significativa
* Il diodo base-emettitore è in polarizzazione diretta
* Il diodo collettore-base è in interdizione, in modo che non vi siano portatori di carica dal collettore alla base

---
[question:AC505]
---
[question:AC515]
---
#### Procedimento di soluzione
* Il valore di $R_1$ determina la corrente di base $I_B$
* $I_B$ è 298 volte minore di $I_C$
* Per la tensione su $R_1$ occorre sottrarre la caduta di tensione sul transistor

---
* dati: $U = \qty{12}{\volt}$
* dati: $I_{\textrm{C}} = \qty{5}{\milli\ampere}$
* dati: $B = 298$
* dati: $U_{\textrm{BE}} = \qty{0,6}{\volt}$
* incognita: $R_1$

<fragment>
$B = \frac{I_{\textrm{C}}}{I_{\textrm{B}}} \Rightarrow I_{\textrm{B}} = \frac{I_{\textrm{C}}}{B} = \frac{\qty{5}{\milli\ampere}}{298} = \qty{16,779}{\micro\ampere}$
</fragment>
<fragment>
$R_1 = \frac{U-U_{\textrm{BE}}}{I_{\textrm{B}}} = \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{16,779}{\micro\ampere}} \approx \qty{680}{\kilo\ohm}$
</fragment>

<note>
Lo svantaggio di questo circuito è la scarsa controllabilità del coefficiente di amplificazione di corrente
</note>
---
[question:AC518]
---
### Stabilizzazione del punto di funzionamento

<left>
[picture:361:a_bauteile_arbeitspunkteinstellung:Circuito a transistor con partitore di tensione alla base]
</left>
<right>
* Il punto di funzionamento viene impostato tramite il partitore di tensione
* La corrente di perdita attraverso $R_2$ deve essere sufficientemente elevata da rendere trascurabile l’influenza della corrente di base sul punto di funzionamento
</right>
<note>
La corrente di collettore dipende in modo esponenziale dalla tensione base-emettitore; la tolleranza delle resistenze può avere un grande impatto sulla corrente di collettore. La forte dipendenza dalla temperatura nel transistor può influenzare la corrente di collettore.
</note>

---
[question:AC516]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dati: $U = \qty{10}{\volt}$
* dati: $I_{\textrm{C}} = \qty{2}{\milli\ampere}$
* dati: $B = 200$
</left>
<right>
* dati: $U_{\textrm{R2}} = \qty{0,6}{\volt}$
* dati: $I_{\textrm{R2}} = 10 \cdot I_{\textrm{B}}$
* incognita: $R_1$
</right>

<fragment>
$B = \frac{I_{\textrm{C}}}{I_{\textrm{B}}} \Rightarrow I_{\textrm{B}} = \frac{I_{\textrm{C}}}{B} = \frac{\qty{2}{\milli\ampere}}{200} = \qty{10}{\micro\ampere}$
</fragment>
<fragment>
$U_{\textrm{R1}} = U - U_{\textrm{R2}} = \qty{10}{\volt} - \qty{0,6}{\volt} = \qty{9,4}{\volt}$
</fragment>
<fragment>
$I_{\textrm{R1}} = I_{\textrm{B}} + I_{\textrm{R2}} = I_{\textrm{B}} + 10 \cdot I_{\textrm{B}} = \qty{110}{\micro\ampere}$
</fragment>
<fragment>
$R_1 = \frac{U_{\textrm{R1}}}{I_{\textrm{R1}}} = \frac{\qty{9,4}{\volt}}{\qty{110}{\micro\ampere}} \approx \qty{85,5}{\kilo\ohm}$
</fragment>

---
[question:AC517]
---
#### Procedimento di soluzione

* $U_{\textrm{R2}}$ è pari a $U_{\textrm{BE}} + U_{\textrm{RE}}$
* La corrente di collettore è determinata principalmente da $R_{\textrm{E}}$
* Circuito molto stabile

--- style="font-size: smaller;"
<left>
* dati: $U = \qty{10}{\volt}$
* dati: $I_{\textrm{C}} = \qty{2}{\milli\ampere}$
* dati: $B = 200$
</left>
<right>
* dati: $U_{\textrm{BE}} = \qty{0,6}{\volt}$
* dati: $U_{\textrm{RE}} = \qty{1}{\volt}$
* dati: $I_{\textrm{R2}} = 10 \cdot I_{\textrm{B}}$
</right>
* incognita: $R_1$

<fragment>
$B = \frac{I_{\textrm{C}}}{I_{\textrm{B}}} \Rightarrow I_{\textrm{B}} = \frac{I_{\textrm{C}}}{B} = \frac{\qty{2}{\milli\ampere}}{200} = \qty{10}{\micro\ampere}$
</fragment>
<fragment>
$U_{\textrm{R2}} = U_{\textrm{BE}} + U_{R_{\textrm{E}}} = \qty{0,6}{\volt} + \qty{1}{\volt} = \qty{1,6}{\volt}$
</fragment>
<fragment>
$U_{\textrm{R1}} = U - U_{\textrm{R2}} = \qty{10}{\volt} - \qty{1,6}{\volt} = \qty{8,4}{\volt}$
</fragment>
<fragment>
$I_{\textrm{R1}} = I_{\textrm{B}} + I_{\textrm{R2}} = I_{\textrm{B}} + 10 \cdot I_{\textrm{B}} = \qty{110}{\micro\ampere}$
</fragment>
<fragment>
$R_1 = \frac{U_{\textrm{R1}}}{I_{\textrm{R1}}} = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} \approx \qty{76,4}{\kilo\ohm}$
</fragment>

---
[question:AC519]
---
#### Procedimento di soluzione

* Nessuna corrente attraverso $R_1$ → nessuna tensione su $R_2$
* La base è al potenziale di massa → il transistor è in stato di interdizione
* Nessuna caduta di tensione su $R_{\textrm{C}}$ → il potenziale del collettore sale alla tensione di servizio

---
[question:AC520]
---
#### Procedimento di soluzione

* $R_2$ non è attraversata da corrente → la base è collegata alla tensione di servizio tramite $R_1$
* A causa della sua dimensione, la corrente di base è ora 11 volte superiore a quella prevista
* La corrente di collettore aumenterà notevolmente → la caduta di tensione su $R_{\textrm{C}}$ aumenterà notevolmente
* $U_{\textrm{CE}}$ scende al valore di saturazione di circa $\qty{0,1}{\volt}$

---
## Transistor ad effetto di campo (FET)

[picture:271:a_bauelemente_fet:Schemi di transistor ad effetto di campo]

* Struttura diversa
* Presenta un canale semiconduttore
* Il flusso di corrente è controllato da un campo elettrico
* Pertanto, è controllato in tensione

<note>
La linea verticale simboleggia il canale, che collega drain (in alto) e source (in basso); a sinistra si trova il gate e la freccia ricorda un diodo
</note>
---
[question:AC502]
---
[question:AC506]
---
### Terminali del FET

* *Source*: sorgente dei portatori di carica nel canale
* *Drain*: drenaggio dei portatori di carica nel canale
* *Gate*: controlla il flusso dei portatori di carica nel canale

---
[question:AC513]
---
[question:AC512]
---
[question:AC514]

<note>
Meglio sarebbe: controlla la corrente del canale invece della resistenza, poiché questo comportamento resistivo si verifica solo a basse tensioni drain-source
</note>
---
### Tipologie di FET

* *FET a svuotamento*: senza tensione gate-source il FET è in conduzione
* *FET autobloccante*: senza tensione gate-source il FET è in interdizione
* *FET a canale n*: la corrente nel canale è trasportata da elettroni
* *FET a canale p*: la corrente nel canale è trasportata da lacune
* *JFET*: il gate è un diodo
* *FET a gate isolato*: il gate è una struttura a condensatore (ad esempio MOSFET)

<note>
MOSFET: metal oxide semiconductor FET
</note>
---
### Simboli del FET

<left>
[picture:273:a_bauelemente_selbstleitender_p_kanal_mosfet:MOSFET a canale p autobloccante]
[picture:276:a_bauelemente_selbstsperrender_n_kanal_mosfet:MOSFET a canale n autobloccante]
</left>
<right>
* *autobloccante*/*a svuotamento*: gate continuo/tratteggiato
* *canale p*/*canale n*: la freccia punta verso l’esterno/dall’interno del canale
* *gate isolato* (MOSFET): gate e canale come condensatore
</right>

---
[question:AC507]
---
[question:AC508]
---
[question:AC509]
---
[question:AC510]
---
[question:AC511]
---
[question:AC521]
---
#### Procedimento di soluzione

<left>
* dati: $U_{\textrm{B}} = \qty{44}{\volt}$
* dati: $R_1 = \qty{10}{\kilo\ohm}$
* dati: $R_2 = \qty{1}{\kilo\ohm}$
* dati: $R_3 = \qty{2,2}{\kilo\ohm}$
* incognita: $U_{\textrm{GS}}$
* approccio: Partitore di tensione non caricato su $R_1$ e $R_2$, con $U_{\textrm{GS}} = U_{\textrm{R2}}$
</left>
<right>
<fragment>
$\begin{split} \frac{U_{\textrm{R2}}}{U_{\textrm{B}}} &= \frac{R_2}{R_1+R_2}\\ \Rightarrow U_{\textrm{R2}} &= \frac{R_2}{R_1+R_2} \cdot U_{\textrm{B}}\\ &= \frac{\qty{1}{\kilo\ohm}}{\qty{10}{\kilo\ohm}+\qty{1}{\kilo\ohm}} \cdot \qty{44}{\volt}\\ &= \frac{1}{11} \cdot \qty{44}{\volt} = \qty{4}{\volt} \end{split}$
</fragment>
</right>

---
[question:AC522]
---
#### Procedimento di soluzione

<left>
* dati: $U_{\textrm{B}} = \qty{44}{\volt}$
* dati: $R_1 = \qty{10}{\kilo\ohm}$
* dati: $R_3 = \qty{2,2}{\kilo\ohm}$
* dati: $U_{\textrm{GS}} = U_{\textrm{R2}} = \qty{2,8}{\volt}$
* dati: $U_{\textrm{B}} = U_{\textrm{R1}} + U_{\textrm{R2}}$
* incognita: $R_2$
</left>
<right>
<fragment>
$\begin{split} \frac{U_{\textrm{R1}}}{U_{\textrm{R2}}} &= \frac{R_1}{R_2}\\ \Rightarrow R_2 &= R_1 \cdot \frac{U_{\textrm{R2}}}{U_{\textrm{R1}}}\\ &= R_1 \cdot \frac{U_{\textrm{R2}}}{U_{\textrm{B}}-U_{\textrm{GS}}}\\ &= \qty{10}{\kilo\ohm} \cdot \frac{\qty{2,8}{\volt}}{\qty{44}{\volt}-\qty{2,8}{\volt}}\\ &\approx \qty{680}{\ohm} \end{split}$
</fragment>
</right>
---
[question:AC523]
---
#### Procedimento di soluzione

* dati: $R_{\textrm{DSon}} = \qty{4}{\milli\ohm}$
* dati: $I = \qty{25}{\ampere}$
* incognita: $P$

<fragment>
$P = I^2 \cdot R = (\qty{25}{\ampere})^2 \cdot \qty{4}{\milli\ohm} = \qty{2,5}{\watt}$
</fragment>

<note>
Il MOSFET si comporta come una resistenza ohmica
</note>

---
### Diodo di protezione

* Un relè viene azionato tramite un transistor bipolare in serie
* Il transistor si accende → la corrente scorre attraverso la bobina del relè
* Il transistor si spegne → la corrente nella bobina induce una tensione negativa sul transistor
* Può portare alla distruzione del transistor
* Prevenzione: montare un *diodo di protezione* in parallelo al relè, in polarizzazione inversa
* La tensione di induzione viene limitata alla tensione del diodo

---
[question:AC524]