## Amplificatore di potenza HF

* Amplificano il segnale HF proveniente dagli stadi precedenti
* Obiettivo: raggiungere la potenza d’uscita desiderata
* Due tipi: amplificatori HF a banda larga e selettivi

---
### Amplificatori HF a banda larga

<left>
[picture:491:a_verstaerker_breitband_gegentaktverstaerker:Amplificatore push-pull a banda larga]
</left>
<right>
* Amplificazione uniforme su un’ampia banda di frequenza (ad es. $\qtyrange{1}{30}{\mega\hertz}$)
* Riconoscibili grazie ai trasformatori di accoppiamento a banda larga
* Nessun circuito risonante con condensatori in parallelo o in serie
</right>

---
[question:AF412]

---
### Amplificatori HF selettivi

<left>
[picture:778:a_verstaerker_selektiver_hf_verstaerker:Amplificatore HF selettivo]
</left>
<right>
* Massimo guadagno solo in una banda stretta (ad es. una banda amatoriale)
* Progettazione a selettività di frequenza
* Utilizzo di circuiti risonanti in serie o in parallelo nel percorso del segnale HF
</right>

---
[question:AF408]

---
# Amplificatori multistadio

<left>
[picture:764:a_verstaerker_zweistufiger_breitband_hf_verstaerker:Amplificatore HF a banda larga a due stadi]
</left>
<right>
* Gli amplificatori possono essere realizzati con più stadi collegati in cascata
</right>

---
[question:AF413]

---
## Adattamento dell’impedenza tra gli stadi dell’amplificatore

* Necessario per ottenere il massimo guadagno, la minima distorsione e il miglior rendimento
* Evita riflessioni e non linearità

---
### Metodi di adattamento dell’impedenza

* Adattamento a banda larga tramite trasformatore con rapporto di trasformazione adeguato
* Adattamento a selettività di frequenza tramite circuito risonante con presa intermedia

---

[picture:765:a_anpassung_breitbandige_anpassung:Adattamento a banda larga tra due stadi mediante trasformatore con rapporto di trasformazione adeguato]

---
[question:AF414]

---

[picture:786:a_anpassung_mosfet:Adattamento a banda larga in ingresso e uscita su MOSFET a bassa impedenza mediante trasformatori]

---
[question:AF417]

---

[picture:779:a_anpassung_induktiver_spannungsteiler:Adattamento a selettività di frequenza con bobina come partitore di tensione induttivo]

---
[question:AF409]

---

[picture:780:a_anpassung_kapazitiver_spannungsteiler:Adattamento a selettività di frequenza con condensatore come partitore di tensione capacitivo]

---
[question:AF410]

---

[picture:768:a_anpassung_eingang_schwingkreis:Circuito risonante con condensatori variabili per l’adattamento dell’impedenza d’ingresso]

---
[question:AF407]

---

[picture:769:a_anpassung_ausgang_schwingkreis:Circuito risonante con condensatori variabili per l’adattamento dell’impedenza d’uscita]

---
[question:AF406]

---
### Filtro Pi per l’adattamento dell’impedenza

* Adatta le impedenze d’ingresso e d’uscita tramite il rapporto delle capacità
* La bobina definisce, insieme alle capacità, la frequenza di progetto
* Carattere passa-basso che sopprime le armoniche

---
[question:AF405]

---
### Circuito LC dopo l’amplificatore di potenza HF

* Serve per l’adattamento dell’impedenza e la soppressione simultanea delle armoniche

---
[question:AF404]

---
## Rendimento di un amplificatore di potenza HF

* Rapporto tra la potenza d’uscita HF erogata e la potenza di alimentazione in corrente continua fornita

---
[question:AF401]

---
## Tensione di polarizzazione negli amplificatori di potenza

<left>
[picture:786:a_verstaerker_bias_arbeitspunkt:Regolazione del punto di lavoro in un amplificatore tramite un potenziometro]
</left>
<right>
* Regolazione della tensione di servizio tramite partitore di tensione
* Regolazione fine tramite trimmer
* Considerazione in corrente continua: i condensatori vengono ignorati, le bobine considerate come cortocircuiti
</right>

---
[question:AF420]

---
[question:AF423]

---
[question:AF424]

---
### Calcolo della tensione di polarizzazione

* Applicazione della legge di Ohm
* Considerazione di collegamenti in parallelo e in serie di resistenze
* I terminali di gate dei transistor sono capacitivi e trascurabili nella considerazione in corrente continua

---
[question:AF421]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dato: $U_Z = \qty{6,2}{\volt}$
* dato: $R_2 = \qty{270}{\ohm}$
* dato: $R_3 = \qty{220}{\ohm}$
</left>
<right>
* dato: $R_4 = \qty{6,8}{\kilo\ohm}$
* dato: $R_6 = \qty{150}{\ohm}$
* cercato: $U_{GS}$
</right>

<left>
<fragment>
$\begin{split}R_E &= \frac{(R_3+R_6) \cdot R_4}{(R_3 + R_6) + R_4}\\ &= \frac{(\qty{220}{\ohm} + \qty{150}{\ohm}) \cdot \qty{6,8}{\kilo\ohm}}{\qty{220}{\ohm} + \qty{150}{\ohm} + \qty{6,8}{\kilo\ohm}}\\ &= \frac{\qty{2,516}{\mega\ohm}^2}{\qty{7170}{\ohm}}\\ &= \qty{351}{\ohm}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}\frac{U_Z}{U_{GS}} &= \frac{R_2 + R_E}{R_E}\\ \Rightarrow \frac{\qty{6,2}{\volt}}{U_{GS}} &= \frac{\qty{270}{\ohm}+\qty{351}{\ohm}}{\qty{351}{\ohm}}\\ &= 1,77\\ \Rightarrow U_{GS} &= \frac{\qty{6,2}{\volt}}{1,77}\\ &= \qty{3,50}{\volt}\end{split}$
</fragment>
</right>

---
## Disaccoppiamento HF della tensione di servizio

* Evita retroazioni tra gli stadi dell’amplificatore (ad es. tendenza all’oscillazione)
* Realizzazione tramite induttanze in serie e condensatori di blocco
* Carattere passa-basso: la tensione continua rimane invariata, la HF viene bloccata

---

[picture:781:a_entkopplung_drossel:Bobina d’arresto per il disaccoppiamento della HF dalla tensione di servizio]

---
[question:AF411]

---
[question:AF422]

---

[picture:786:a_entkopplung_abblock_kondensatoren:Condensatori di blocco per il disaccoppiamento della HF dalla tensione di servizio con carattere passa-basso]

---
[question:AF419]

---
[question:AF418]

---
## Proprietà HF dei condensatori

* Grandi capacità (ad es. condensatori elettrolitici) utilizzabili solo a basse frequenze
* Per applicazioni HF, combinazione di diversi valori di capacità per coprire un’ampia banda di frequenza

---
[question:AF415]

---
## Guadagno totale di un amplificatore di potenza

<left>
[picture:470:a_verstaerker_gesamtverstaerkung:Schema a blocchi di un amplificatore con guadagno e perdita per ogni stadio]
</left>
<right>
* Determinato dalla differenza tra potenza d’uscita e potenza d’ingresso
* Calcolo tramite sottrazione con segno dei valori in dBm
</right>

---
[question:AF428]
---
#### Procedimento di soluzione

* dato: $P_1 = \qty{0,3}{\milli\watt}$ oppure $\qty{-5}{\dBm}$
* dato: $P_2 = \qty{20}{\watt}$ oppure $\qty{43}{\dBm}$
* cercato: $g$

<left>
<fragment>
$\begin{split}g &= P_2 - P_1\\ &= \qty{43}{\dBm} - (\qty{-5}{\dBm})\\ &= \qty{43}{\dBm} + \qty{5}{\dBm}\\ &= \qty{48}{\dB}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}g &= \qty{10 \cdot \log_{10}{\left(\frac{P_2}{P_1}\right)}}{\dB}\\ &= \qty{10 \cdot \log_{10}{\left(\frac{\qty{20}{\watt}}{\qty{0,3}{\milli\watt}}\right)}}{\dB} \\ &\approx \qty{48}{\dB}\end{split}$
</fragment>
</right>