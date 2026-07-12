## Frequenza di taglio

Per filtri passa-alto e passa-basso, la frequenza di taglio è data da

<left>
Per elementi RL
$R = X_\text{L}$
$f_\text{g} = \frac{R}{2 \pi \cdot L}$
</left>
<right>
Per elementi RC
$R = X_\text{C}$
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C}$
</right>


---
[question:AD201]
---
#### Percorso di soluzione
* dato: $R = \qty{4,7}{\kilo\ohm}$
* dato: $C = \qty{2,2}{\nano\farad}$
* cercato: $f_\text{g}$

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C} = \frac{1}{2 \pi \cdot \qty{4,7}{\kilo\ohm} \cdot \qty{2,2}{\nano\farad}} \approx \qty{15,4}{\kilo\hertz}$
</fragment>
---
[question:AD202]
---
#### Percorso di soluzione
* dato: $R = \qty{10}{\kilo\ohm}$
* dato: $C = \qty{47}{\nano\farad}$
* cercato: $f_\text{g}$

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C} = \frac{1}{2 \pi \cdot \qty{10}{\kilo\ohm} \cdot \qty{47}{\nano\farad}} \approx \qty{339}{\hertz}$
</fragment>
---
[question:AD203]
---
#### Percorso di soluzione
* dato: $R_1 = \qty{4,7}{\kilo\ohm}$
* dato: $C_1 = \qty{6,8}{\nano\farad}$
* cercato: $f_\text{g}$

<fragment>
$C_2$ e tutte le altre informazioni non sono rilevanti per il filtro passa-basso.
</fragment>

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R_1 \cdot C_1} = \frac{1}{2 \pi \cdot \qty{4,7}{\kilo\ohm} \cdot \qty{6,8}{\nano\farad}} \approx \qty{5}{\kilo\hertz}$
</fragment>
---
## Frequenza di risonanza

* Collegamento in parallelo o in serie di bobina e condensatore $\rightarrow$ circuito oscillante
* Alte frequenze $\rightarrow$ alta resistenza sulla bobina
* Basse frequenze $\rightarrow$ alta resistenza sul condensatore
* Esiste una frequenza alla quale la bobina e il condensatore hanno la stessa resistenza $\rightarrow$ *frequenza di risonanza*

---
[question:AD206]
--- style="font-size: smaller;"
## Circuito oscillante parallelo

[picture:233:a_schwingkreis_parallelschwingkreis:Circuito oscillante parallelo e rappresentazione dell'impedenza in funzione della frequenza]

* I componenti ideali si caricano e scaricano continuamente
* Teoricamente, l'impedenza alla frequenza di risonanza è infinitamente alta
* In pratica, il componente con la resistenza più bassa determina l'impedenza totale
* Alle frequenze superiori e inferiori alla frequenza di risonanza, il circuito oscillante parallelo ha un'impedenza inferiore

--- style="font-size: smaller;"
## Circuito oscillante in serie

[picture:230:a_schwingkreis_reihenschwingkreis:Circuito oscillante in serie e rappresentazione dell'impedenza in funzione della frequenza]

* O circuito oscillante in serie
* Teoricamente, l'impedenza alla frequenza di risonanza è $\qty{0}{\ohm}$
* In pratica, l'impedenza è determinata dalla resistenza ohmica
* Alle frequenze superiori e inferiori alla frequenza di risonanza, il circuito oscillante in serie ha un'impedenza maggiore

---
[question:AD207]
---
[question:AD204]
---
## Caso di risonanza

Per circuiti oscillanti paralleli e in serie:

$X_\text{C} = X_\text{L}$

Le impedenze hanno la stessa grandezza.

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
#### Percorso di soluzione
* dato: $L = \qty{1,2}{\micro\henry}$
* dato: $C = \qty{6,8}{\pico\farad}$
* dato: $R = \qty{10}{\ohm}$
* cercato: $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{1,2}{\micro\henry} \cdot \qty{6,8}{\pico\farad}}} \approx \qty{55,7}{\mega\hertz} \end{split}$
</fragment>
<fragment>
La resistenza $R$ non è necessaria per il calcolo.
</fragment>
---
[question:AD209]
---
#### Percorso di soluzione
* dato: $L = \qty{10}{\micro\henry}$
* dato: $C = \qty{1}{\nano\farad}$
* cercato: $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{10}{\micro\henry} \cdot \qty{1}{\nano\farad}}} \approx \qty{1,592}{\mega\hertz} \end{split}$
</fragment>
---
[question:AD210]
---
#### Percorso di soluzione
* dato: $L = \qty{100}{\micro\henry}$
* dato: $C = \qty{0,01}{\micro\farad}$
* cercato: $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{100}{\micro\henry} \cdot \qty{0,01}{\micro\farad}}} \approx \qty{159}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AD211]
---
#### Percorso di soluzione
* dato: $L = \qty{2,2}{\micro\henry}$
* dato: $C = \qty{56}{\pico\farad}$
* cercato: $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{2,2}{\micro\henry} \cdot \qty{56}{\pico\farad}}} \approx \qty{14,34}{\mega\hertz} \end{split}$
</fragment>
---
[question:AD212]
--- style="font-size: 0.7em;"
#### Percorso di soluzione
* dato: $C_1 = \qty{0,1}{\nano\farad}$
* dato: $C_2 = \qty{1,5}{\nano\farad}$
* dato: $C_3 = \qty{220}{\pico\farad}$
* dato: $L = \qty{1,2}{\milli\henry}$
* cercato: $f_0$

<fragment>
$C = C_1 + C_2 + C_3 = \qty{0,1}{\nano\farad} + \qty{1,5}{\nano\farad} + \qty{220}{\pico\farad} = \qty{1,82}{\nano\farad}$
</fragment>
<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{1,2}{\milli\henry} \cdot \qty{1,82}{\nano\farad}}} \approx \qty{107,7}{\kilo\hertz} \end{split}$
</fragment>
---
### Modifica della frequenza di risonanza

* Bobina o condensatore più grandi $\rightarrow$ frequenza di risonanza più bassa
* Bobina o condensatore più piccoli $\rightarrow$ frequenza di risonanza più alta

<fragment>
Aumentare l'induttanza
* Aumentare il numero di spire
* Avvicinare le spire
* Introdurre un nucleo di ferrite

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

[picture:752:a_schwingkreis_potentiometer:Variazione della capacità tramite un Varicap]

* Il Varicap viene modificato da una tensione di controllo sul partitore di tensione resistivo
* Tensione più bassa sul Varicap $\rightarrow$ strato di svuotamento più piccolo nel Varicap $\rightarrow$ capacità maggiore
* Condensatori collegati in serie $\rightarrow$ la capacità diminuisce $\rightarrow$ la frequenza di risonanza aumenta

---
[question:AD218]
--- style="font-size: smaller;"
## Filtro passa-banda

[picture:785:a_schwingkreis_bandpass:Filtro passa-banda composto da più circuiti oscillanti]

* Combinazione di circuiti oscillanti paralleli e in serie
* Lascia passare una determinata banda di frequenza
* I circuiti oscillanti paralleli agiscono come resistenze ad alta impedenza
* Il circuito oscillante in serie agisce come resistenza a bassa impedenza

---
[question:AD205]
---
## Larghezza di banda

* Grande dipendenza dalla resistenza ohmica
* Indicata in dB rispetto a un valore di riferimento del filtro
* Ad esempio, *larghezza di banda* al *valore di $\qty{-3}{\dB}$*
* Metà della potenza di un segnale può ancora attraversare il filtro
* O lo 0,7 volte della tensione del segnale

---
[question:AD219]
---
[question:AD220]
---
### Larghezze di banda comuni

* Stretta con $\qty{500}{\hertz}$ per la telegrafia (CW)
* Ampia con $\qty{2,7}{\kilo\hertz}$ per la modulazione vocale (SSB)

---
[question:AD221]
---
[question:AD222]
---
## Fattore di qualità di un circuito oscillante

* Anche fattore Q
* Indicatore di perdita di energia
* Rapporto tra le reattanze e la resistenza ohmica nel caso di risonanza ($X_\text{L} = X_\text{C}$)

<fragment>
<left>
Circuito oscillante in serie
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
#### Percorso di soluzione
<left>
* dato: $L = \qty{100}{\micro\henry}$
* dato: $C = \qty{0,01}{\micro\farad}$
</left>
<right>
* dato: $R_\text{S} = \qty{10}{\ohm}$
* cercato: $Q$
</right>

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{100}{\micro\henry} \cdot \qty{0,01}{\micro\farad}}} \approx \qty{159,2}{\kilo\hertz} \end{split}$
</fragment>
<fragment>
Calcolare $B$ o $X_\text{L}$
$\begin{split} X_\text{L} &= \omega \cdot L = 2 \pi \cdot f_0 \cdot L\\ &= 2 \pi \cdot \qty{159,2}{\kilo\hertz} \cdot \qty{100}{\micro\henry} \approx \qty{100,03}{\ohm} \end{split}$
</fragment>
<fragment>
$Q = \frac{X_\text{L}}{R_\text{S}} = \frac{\qty{100,03}{\ohm}}{\qty{10}{\ohm}} \approx 10$
</fragment>
---
[question:AD226]
--- style="font-size: 0.7em;"
#### Percorso di soluzione
<left>
* dato: $L = \qty{2,2}{\micro\henry}$
* dato: $C = \qty{56}{\pico\farad}$
</left>
<right>
* dato: $R_\text{P} = \qty{1}{\kilo\ohm}$
* cercato: $Q$
</right>
  
<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{2,2}{\micro\henry} \cdot \qty{56}{\pico\farad}}} \approx \qty{14,34}{\mega\hertz} \end{split}$
</fragment>
<fragment>
Calcolare $B$ o $X_\text{L}$
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
O inserito con la formula del circuito oscillante di Thomson

<left>
Circuito oscillante in serie
$B = \frac{R_\text{S}}{2 \pi \cdot L}$
</left>
<right>
Circuito oscillante parallelo
$B = \frac{1}{2 \pi \cdot R_\text{P} \cdot C}$
</right>
</fragment>
<note>
Derivazione non mostrata
</note>

---
[question:AD224]
---
#### Percorso di soluzione
* dato: $L = \qty{2,2}{\micro\henry}$
* dato: $C = \qty{56}{\pico\farad}$
* dato: $R_\text{P} = \qty{1}{\kilo\ohm}$
* cercato: $B$

<fragment>
$\begin{split} B &= \frac{1}{2 \pi \cdot R_\text{P} \cdot C}\\ &= \frac{1}{2 \pi \cdot \qty{1}{\kilo\ohm} \cdot \qty{56}{\pico\farad}} \approx \qty{2,84}{\mega\hertz} \end{split}$
</fragment>

---
[question:AD223]
---
#### Percorso di soluzione
* dato: $L = \qty{100}{\micro\henry}$
* dato: $C = \qty{0,01}{\micro\farad}$
* dato: $R_\text{S} = \qty{10}{\ohm}$
* cercato: $B$

<fragment>
$B = \frac{R_\text{S}}{2 \pi \cdot L} = \frac{\qty{10}{\ohm}}{2 \pi \cdot \qty{100}{\micro\henry}} \approx \qty{15,9}{\kilo\hertz}$
</fragment>
--- style="font-size: 0.7em;" data-transition="none"
## Accoppiamento

[picture:184:a_schwingkreis_kopplung:Accoppiamento induttivo di due circuiti oscillanti e il diagramma di tensione in funzione della frequenza]

* Tra stadi di circuito o filtri vengono spesso utilizzati circuiti oscillanti accoppiati
* Due circuiti oscillanti accoppiati induttivamente o capacitivamente
* Il grado di accoppiamento determina l'influenza reciproca, la larghezza di banda e la curva di trasmissione

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Accoppiamento induttivo di due circuiti oscillanti e il diagramma di tensione in funzione della frequenza]

* d: *accoppiamento debole* $\rightarrow$ quasi nessuna influenza reciproca, attenuazione di trasmissione molto alta e larghezza di banda molto ridotta
* c: *accoppiamento sottocritico* $\rightarrow$ quasi nessuna influenza reciproca, attenuazione di trasmissione alta e larghezza di banda ridotta

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Accoppiamento induttivo di due circuiti oscillanti e il diagramma di tensione in funzione della frequenza]

* b: *accoppiamento critico* $\rightarrow$ leggera influenza reciproca, curva di trasmissione piatta con bassa attenuazione e plateau nella banda passante, nonché buona larghezza di banda

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Accoppiamento induttivo di due circuiti oscillanti e il diagramma di tensione in funzione della frequenza]
* a: *accoppiamento supercritico* $\rightarrow$ forte influenza reciproca, modifica delle frequenze di risonanza, ampia larghezza di banda e distorsione della curva di trasmissione nella banda passante con "incavi"

---
[question:AD227]
---
[question:AD228]
---
[question:AD229]
