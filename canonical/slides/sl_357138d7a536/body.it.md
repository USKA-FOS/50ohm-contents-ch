## Frequenza di taglio

Nei filtri passa-alto e passa-basso vale per la frequenza di taglio:

<left>
Nei circuiti RL
$R = X_\text{L}$
$f_\text{g} = \frac{R}{2 \pi \cdot L}$
</left>
<right>
Nei circuiti RC
$R = X_\text{C}$
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C}$
</right>


---
[question:AD201]
---
#### Procedimento di soluzione
* dati: $R = \qty{4,7}{\kilo\ohm}$
* dati: $C = \qty{2,2}{\nano\farad}$
* richiesto: $f_\text{g}$

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C} = \frac{1}{2 \pi \cdot \qty{4,7}{\kilo\ohm} \cdot \qty{2,2}{\nano\farad}} \approx \qty{15,4}{\kilo\hertz}$
</fragment>
---
[question:AD202]
---
#### Procedimento di soluzione
* dati: $R = \qty{10}{\kilo\ohm}$
* dati: $C = \qty{47}{\nano\farad}$
* richiesto: $f_\text{g}$

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C} = \frac{1}{2 \pi \cdot \qty{10}{\kilo\ohm} \cdot \qty{47}{\nano\farad}} \approx \qty{339}{\hertz}$
</fragment>
---
[question:AD203]
---
#### Procedimento di soluzione
* dati: $R_1 = \qty{4,7}{\kilo\ohm}$
* dati: $C_1 = \qty{6,8}{\nano\farad}$
* richiesto: $f_\text{g}$

<fragment>
$C_2$ e tutti gli altri dati sono irrilevanti per il filtro passa-basso.
</fragment>

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R_1 \cdot C_1} = \frac{1}{2 \pi \cdot \qty{4,7}{\kilo\ohm} \cdot \qty{6,8}{\nano\farad}} \approx \qty{5}{\kilo\hertz}$
</fragment>
---
## Frequenza di risonanza

* Collegamento in parallelo o in serie di bobina e condensatore $\rightarrow$ circuito oscillante
* Alte frequenze $\rightarrow$ alta impedenza alla bobina
* Basse frequenze $\rightarrow$ alta impedenza al condensatore
* Esiste una frequenza in cui bobina e condensatore hanno la stessa impedenza $\rightarrow$ *frequenza di risonanza*

---
[question:AD206]
--- style="font-size: smaller;"
## Circuito oscillante parallelo

[picture:233:a_schwingkreis_parallelschwingkreis:Circuito oscillante parallelo e rappresentazione dell'impedenza in funzione della frequenza]

* I componenti ideali si caricano e scaricano continuamente
* In teoria, l'impedenza alla frequenza di risonanza è infinita
* In pratica, il componente con la resistenza più bassa determina l'impedenza totale
* A frequenze superiori e inferiori alla frequenza di risonanza, il circuito oscillante parallelo ha un'impedenza minore

--- style="font-size: smaller;"
## Circuito oscillante serie

[picture:230:a_schwingkreis_reihenschwingkreis:Circuito oscillante serie e rappresentazione dell'impedenza in funzione della frequenza]

* O circuito oscillante in serie
* In teoria, l'impedenza alla frequenza di risonanza è $\qty{0}{\ohm}$
* In pratica, l'impedenza è determinata dalla resistenza ohmica
* A frequenze superiori e inferiori alla frequenza di risonanza, il circuito oscillante serie ha un'impedenza maggiore

---
[question:AD207]
---
[question:AD204]
---
## Caso di risonanza

Per circuiti oscillanti paralleli e serie:

$X_\text{C} = X_\text{L}$

Le impedenze sono di uguale entità.

<fragment>
Frequenza di risonanza con la formula del circuito oscillante di Thomson:

$f_0 = \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}$
</fragment>

<note>
William Thomson, poi Lord Kelvin, nel 1853
</note>
---


[question:AD208]
---
#### Procedimento di soluzione
* dati: $L = \qty{1,2}{\micro\henry}$
* dati: $C = \qty{6,8}{\pico\farad}$
* dati: $R = \qty{10}{\ohm}$
* richiesto: $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{1,2}{\micro\henry} \cdot \qty{6,8}{\pico\farad}}} \approx \qty{55,7}{\mega\hertz} \end{split}$
</fragment>
<fragment>
La resistenza $R$ non è necessaria per il calcolo.
</fragment>
---
[question:AD209]
---
#### Procedimento di soluzione
* dati: $L = \qty{10}{\micro\henry}$
* dati: $C = \qty{1}{\nano\farad}$
* richiesto: $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{10}{\micro\henry} \cdot \qty{1}{\nano\farad}}} \approx \qty{1,592}{\mega\hertz} \end{split}$
</fragment>
---
[question:AD210]
---
#### Procedimento di soluzione
* dati: $L = \qty{100}{\micro\henry}$
* dati: $C = \qty{0,01}{\micro\farad}$
* richiesto: $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{100}{\micro\henry} \cdot \qty{0,01}{\micro\farad}}} \approx \qty{159}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AD211]
---
#### Procedimento di soluzione
* dati: $L = \qty{2,2}{\micro\henry}$
* dati: $C = \qty{56}{\pico\farad}$
* richiesto: $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{2,2}{\micro\henry} \cdot \qty{56}{\pico\farad}}} \approx \qty{14,34}{\mega\hertz} \end{split}$
</fragment>
---
[question:AD212]
--- style="font-size: 0.7em;"
#### Procedimento di soluzione
* dati: $C_1 = \qty{0,1}{\nano\farad}$
* dati: $C_2 = \qty{1,5}{\nano\farad}$
* dati: $C_3 = \qty{220}{\pico\farad}$
* dati: $L = \qty{1,2}{\milli\henry}$
* richiesto: $f_0$

<fragment>
$C = C_1 + C_2 + C_3 = \qty{0,1}{\nano\farad} + \qty{1,5}{\nano\farad} + \qty{220}{\pico\farad} = \qty{1,82}{\nano\farad}$
</fragment>
<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{1,2}{\milli\henry} \cdot \qty{1,82}{\nano\farad}}} \approx \qty{107,7}{\kilo\hertz} \end{split}$
</fragment>
---
### Variazione della frequenza di risonanza

* Bobina o condensatore più grandi $\rightarrow$ frequenza di risonanza minore
* Bobina o condensatore più piccoli $\rightarrow$ frequenza di risonanza maggiore

<fragment>
Aumentare l'induttanza
* Aumentare il numero di spire
* Avvicinare le spire
* Inserire un nucleo in ferrite

</fragment>

---
[question:AD213]
---
[question:AD214]
---
[question:AD215]
---
[question:AD216]
---
[question:AD217]
---
### Circuito oscillante controllato in tensione

[picture:752:a_schwingkreis_potentiometer:Variazione della capacità tramite un varicap]

* Il varicap viene modificato da una tensione di controllo al partitore di tensione resistivo
* Tensione minore al varicap $\rightarrow$ giunzione più piccola nel varicap $\rightarrow$ capacità maggiore
* Condensatori collegati in serie $\rightarrow$ capacità minore $\rightarrow$ frequenza di risonanza maggiore

---
[question:AD218]
--- style="font-size: smaller;"
## Filtro passa-banda

[picture:785:a_schwingkreis_bandpass:Filtro passa-banda composto da più circuiti oscillanti]

* Combinazione di circuiti oscillanti paralleli e serie
* Lascia passare una specifica banda di frequenza
* I circuiti oscillanti paralleli agiscono come resistenze ad alta impedenza
* Il circuito oscillante serie agisce come resistenza a bassa impedenza

---
[question:AD205]
---
## Larghezza di banda

* Grande dipendenza dalla resistenza ohmica
* Indicata in dB rispetto a un valore di riferimento del filtro
* Ad esempio, *larghezza di banda* al valore di *$\qty{-3}{\dB}$*
* Può ancora passare metà della potenza di un segnale
* Oppure la tensione del segnale pari a 0,7 volte

---
[question:AD219]
---
[question:AD220]
---
### Larghezze di banda tipiche

* Banda stretta con $\qty{500}{\hertz}$ per telegrafia (CW)
* Banda larga con $\qty{2,7}{\kilo\hertz}$ per modulazione vocale (SSB)

---
[question:AD221]
---
[question:AD222]
---
## Fattore di qualità di un circuito oscillante

* Anche fattore Q
* Caratteristica della perdita di energia
* Rapporto tra le reattanze e la resistenza ohmica nel caso di risonanza ($X_\text{L} = X_\text{C}$)

<fragment>
<left>
Circuito oscillante serie
$Q = \frac{f_0}{B} = \frac{X_\text{L}}{R_\text{S}}$
</left>
<right>
Circuito oscillante parallelo
$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$
</right>
</fragment>
  
---
[question:AD225]
--- style="font-size: 0.7em;"
#### Procedimento di soluzione
<left>
* dati: $L = \qty{100}{\micro\henry}$
* dati: $C = \qty{0,01}{\micro\farad}$
</left>
<right>
* dati: $R_\text{S} = \qty{10}{\ohm}$
* richiesto: $Q$
</right>

<fragment>
Prima calcolare $f_0$
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{100}{\micro\henry} \cdot \qty{0,01}{\micro\farad}}} \approx \qty{159,2}{\kilo\hertz} \end{split}$
</fragment>
<fragment>
Poi calcolare $B$ o $X_\text{L}$
$\begin{split} X_\text{L} &= \omega \cdot L = 2 \pi \cdot f_0 \cdot L\\ &= 2 \pi \cdot \qty{159,2}{\kilo\hertz} \cdot \qty{100}{\micro\henry} \approx \qty{100,03}{\ohm} \end{split}$
</fragment>
<fragment>
$Q = \frac{X_\text{L}}{R_\text{S}} = \frac{\qty{100,03}{\ohm}}{\qty{10}{\ohm}} \approx 10$
</fragment>
---
[question:AD226]
--- style="font-size: 0.7em;"
#### Procedimento di soluzione
<left>
* dati: $L = \qty{2,2}{\micro\henry}$
* dati: $C = \qty{56}{\pico\farad}$
</left>
<right>
* dati: $R_\text{P} = \qty{1}{\kilo\ohm}$
* richiesto: $Q$
</right>

<fragment>
Prima calcolare $f_0$
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{2,2}{\micro\henry} \cdot \qty{56}{\pico\farad}}} \approx \qty{14,34}{\mega\hertz} \end{split}$
</fragment>
<fragment>
Poi calcolare $B$ o $X_\text{L}$
$\begin{split} X_\text{L} &= \omega \cdot L = 2 \pi \cdot f_0 \cdot L\\ &= 2 \pi \cdot \qty{14,34}{\mega\hertz} \cdot \qty{2,2}{\micro\henry} \approx \qty{198,2}{\ohm} \end{split}$
</fragment>
<fragment>
$Q = \frac{R_\text{P}}{X_\text{L}} = \frac{\qty{1}{\kilo\ohm}}{\qty{198,2}{\ohm}} \approx 5$
</fragment>
---
### Calcolo della larghezza di banda

Tramite frequenza di risonanza e fattore di qualità

$Q = \frac{f_0}{B} \Rightarrow B = \frac{f_0}{Q}$

<fragment>
Oppure inserendo la formula del circuito oscillante di Thomson

<left>
Circuito oscillante serie
$B = \frac{R_\text{S}}{2 \pi \cdot L}$
</left>
<right>
Circuito oscillante parallelo
$B = \frac{1}{2 \pi \cdot R_\text{P} \cdot C}$
</right>
</fragment>
<note>
Dimostrazione non mostrata
</note>

---
[question:AD224]
---
#### Procedimento di soluzione
* dati: $L = \qty{2,2}{\micro\henry}$
* dati: $C = \qty{56}{\pico\farad}$
* dati: $R_\text{P} = \qty{1}{\kilo\ohm}$
* richiesto: $B$

<fragment>
$\begin{split} B &= \frac{1}{2 \pi \cdot R_\text{P} \cdot C}\\ &= \frac{1}{2 \pi \cdot \qty{1}{\kilo\ohm} \cdot \qty{56}{\pico\farad}} \approx \qty{2,84}{\mega\hertz} \end{split}$
</fragment>

---
[question:AD223]
---
#### Procedimento di soluzione
* dati: $L = \qty{100}{\micro\henry}$
* dati: $C = \qty{0,01}{\micro\farad}$
* dati: $R_\text{S} = \qty{10}{\ohm}$
* richiesto: $B$

<fragment>
$B = \frac{R_\text{S}}{2 \pi \cdot L} = \frac{\qty{10}{\ohm}}{2 \pi \cdot \qty{100}{\micro\henry}} \approx \qty{15,9}{\kilo\hertz}$
</fragment>
--- style="font-size: 0.7em;" data-transition="none"
## Accoppiamento

[picture:184:a_schwingkreis_kopplung:Accoppiamento induttivo di due circuiti oscillanti e diagramma della tensione in funzione della frequenza]

* Tra stadi di circuito o filtri vengono spesso utilizzati circuiti oscillanti accoppiati
* Due circuiti oscillanti accoppiati induttivamente o capacitivamente
* Il grado di accoppiamento determina l'influenza reciproca, la larghezza di banda e la curva di attenuazione

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Accoppiamento induttivo di due circuiti oscillanti e diagramma della tensione in funzione della frequenza]

* d: *accoppiamento lasco* $\rightarrow$ scarsa influenza reciproca, attenuazione d’inserzione molto elevata e larghezza di banda molto ridotta
* c: *accoppiamento sottocritico* $\rightarrow$ scarsa influenza reciproca, attenuazione d’inserzione elevata e larghezza di banda ridotta

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Accoppiamento induttivo di due circuiti oscillanti e diagramma della tensione in funzione della frequenza]

* b: *accoppiamento critico* $\rightarrow$ qualche influenza reciproca, curva di attenuazione piatta con attenuazione ridotta e plateau nella banda passante nonché buona larghezza di banda

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Accoppiamento induttivo di due circuiti oscillanti e diagramma della tensione in funzione della frequenza]
* a: *accoppiamento sovracritico* $\rightarrow$ forte influenza reciproca, variazione delle frequenze di risonanza, grande larghezza di banda e distorsione della curva di attenuazione nella banda passante con "avvallamenti"

---
[question:AD227]
---
[question:AD228]
---
[question:AD229]
