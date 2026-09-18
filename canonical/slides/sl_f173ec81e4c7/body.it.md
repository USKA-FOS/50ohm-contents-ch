## Misurazioni per radioamatori

* Misurazioni importanti: potenza d’uscita e tensioni RF
* La misurazione della potenza di uscita del trasmettitore richiede un carico definito
* Impedenza comune nel radioamatoriale: $\qty{50}{\ohm}$
* Misurare direttamente nel circuito ha senso solo con potenze ridotte

---
## Misurazione della tensione RF

* La tensione RF viene misurata con una sonda RF
* Rettificazione a diodo e livellamento con un condensatore in serie

---
### Sonda RF con rettificazione semplice



<left>
[picture:576:a_messung_hf_tastkopf_leistungsmessung:Sonda per la misurazione della potenza RF tramite partitore di tensione]
</left>
<right>
* Un diodo all’uscita fornisce la tensione di picco della tensione RF
* Sottraendo la tensione di soglia del diodo e, se necessario, il partitore di tensione
</right>

---
[question:AI608]

---
### Sonda RF con rettificazione a doppia semionda

<left>
[picture:770:a_messung_hf_tastkopf_doppeldiode:Sonda RF con due diodi per entrambe le semionde]
</left>
<right>
* Due diodi per aumentare la precisione di misura, in particolare con potenze ridotte
* Entrambe le semionde vengono rettificate
* Risultato: tensione di picco doppia meno due volte la tensione di soglia dei diodi
</right>

---
[question:AI605]

---
[question:AI604]

---
### Misurare alte potenze RF

* Richiede un attenuatore robusto
* Assorbe gran parte della potenza
* L’attenuatore deve essere considerato nel calcolo

---
[question:AI609]

<note>
Nessun calcolo necessario poiché esiste una sola risposta con attenuatore
</note>

---
## Calibrazione dei circuiti di misura

* Necessaria per misurazioni di potenza precise
* Devono essere creati valori di correzione

---
[question:AI612]

---
### Calcolo di una sonda RF

<left>
[picture:576:a_messung_messschaltung_beispiel_1:Esempio di un circuito di misura RF]
</left>
<right>
* Il segnale d’ingresso viene chiuso su un’impedenza corretta
* La tensione viene dimezzata tramite partitore di tensione
* Dopo la rettificazione a diodo rimane la tensione di picco meno la tensione di soglia
</right>

---
[question:AI610]

--- style="font-size: smaller;"
#### Procedimento di soluzione

* dato: $P_E = \qty{1}{\watt}$
* dato: $U_F = \qty{0,23}{\volt}$
* dato: $R_V = \qty{110}{\ohm}$, $R_T = \qty{330}{\ohm}$
* cercato: $U_A$


<fragment>
$\begin{split}R &= \left(\frac{1}{R_T + R_T} + \frac{1}{R_V} + \frac{1}{R_V}\right)^{-1}\\ &= \left(\frac{1}{\qty{330}{\ohm} + \qty{330}{\ohm}} + \frac{1}{\qty{110}{\ohm}} + \frac{1}{\qty{110}{\ohm}}\right)^{-1}\\ &= \qty{50,77}{\ohm}\end{split}$
</fragment>

--- style="font-size: smaller;"
* dato: $P_E = \qty{1}{\watt}$
* dato: $U_F = \qty{0,23}{\volt}$
* calcolato: $R = \qty{50,77}{\ohm}$
* cercato: $U_A$

<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ \Rightarrow U_{E,eff} &= \sqrt{P_E \cdot R}\\ &= \sqrt{\qty{1}{\watt} \cdot \qty{50,77}{\ohm}}\\ &= \qty{7,125}{\volt}\end{split}$
</fragment>

--- style="font-size: smaller;"
* dato: $U_F = \qty{0,23}{\volt}$
* calcolato: $U_{E,eff} = \qty{7,125}{\volt}$
* cercato: $U_A$

<left>
<fragment>
$\begin{split}U_S &= U_{E,eff} \cdot \sqrt{2}\\ &= \qty{7,071}{\volt} \cdot 1,414\\ &= \qty{10,07}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_A &= \frac{U_S}{2}\,-\,U_F\\ &= \frac{\qty{10,07}{\volt}}{2}\,-\,\qty{0,23}{\volt}\\ &= \qty{5,035}{\volt}\,-\,\qty{0,23}{\volt}\\ &= \qty{4,805}{\volt} \approx \qty{4,8}{\volt}\end{split}$
</fragment>
</right>

---
### Calcolo della potenza d’ingresso dalla tensione continua misurata

<left>
[picture:577:a_messung_messschaltung_beispiel_2:Esempio di un circuito di misura RF]
</left>
<right>
* La tensione sul partitore di tensione corrisponde alla tensione d’uscita più la tensione del diodo
* Calcolare i valori efficaci
* Determinare la potenza d’ingresso tramite la resistenza del circuito
</right>

---
[question:AI611]

--- style="font-size: smaller;"
#### Procedimento di soluzione
* dato: $U_A = \qty{14,9}{\volt}\text{ DC}$
* dato: $U_F = \qty{0,7}{\volt}$
* dato: $R_1 = \qty{54,1}{\ohm}$, $R_T = \qty{330}{\ohm}$
* cercato: $P_E$

<left>
<fragment>
$\begin{split}R &= \left(\frac{1}{R_T + R_T} + \frac{1}{R_1}\right)^{-1}\\ &= \left(\frac{1}{\qty{330}{\ohm} + \qty{330}{\ohm}} + \frac{1}{\qty{54,1}{\ohm}}\right)^{-1}\\ &= \qty{50}{\ohm}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_S &= \left(U_A + U_F\right) \cdot 2\\ &= \left(\qty{14,9}{\volt} + \qty{0,7}{\volt}\right) \cdot 2\\ &= \qty{31,2}{\volt}\end{split}$
</fragment>
</right>

--- style="font-size: smaller;"
<left>
* calcolato: $R = \qty{50}{\ohm}$
* calcolato: $U_S = \qty{31,2}{\volt}$
* cercato: $P_E$

<fragment>
$\begin{split}U_{E,eff}\\ &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{31,2}{\volt}}{1,414}\\ &= \qty{22,06}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ &= \frac{(\qty{22,06}{\volt})^2}{\qty{50}{\ohm}}\\ &\approx \qty{9,7}{\watt}\end{split}$
</fragment>
</right>

---
### Sonda RF con rettificazione a doppia semionda di picco

<left>
[picture:771:a_messung_hf_tastkopf_doppeldiode_2:Sonda RF con rettificazione a doppia semionda di picco]
</left>
<right>
* Calcolo come per la rettificazione semplice
* Considerare la tensione di picco doppia
* Tenere conto della doppia tensione di soglia dei diodi
</right>

---
[question:AI607]

--- style="font-size: smaller;"
#### Procedimento di soluzione

* dato: $U_A = \qty{15,3}{\volt}\text{ DC}$
* dato: $U_F = \qty{0,23}{\volt}$
* dato: $R_{V1} = \qty{56}{\ohm}$, $R_{V2} = \qty{470}{\ohm}$
* cercato: $P_E$

<left>
<fragment>
$\begin{split}R &= \left(\frac{1}{R_{V1}} + \frac{1}{R_{V2}}\right)^{-1}\\ &= \left(\frac{1}{\qty{56}{\ohm}} + \frac{1}{\qty{470}{\ohm}}\right)^{-1}\\ &= \qty{50,04}{\ohm}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_S &= \frac{U_A}{2} + U_F\\ &= \frac{\qty{15,3}{\volt}}{2} + \qty{0,23}{\volt}\\ &= \qty{7,88}{\volt}\end{split}$
</fragment>
</right>

--- style="font-size: smaller;"
<left>
* calcolato: $R = \qty{50,04}{\ohm}$
* calcolato: $U_S = \qty{7,88}{\volt}$
* cercato: $P_E$

<fragment>
$\begin{split}U_{E,eff} &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{7,88}{\volt}}{1,414}\\ &= \qty{5,57}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ &= \frac{{\qty{5,57}{\volt}}^2}{\qty{50,04}{\ohm}}\\ &\approx \qty{600}{\milli\watt}\end{split}$
</fragment>
</right>

---
[question:AI606]

--- style="font-size: smaller;"
#### Procedimento di soluzione

* dato: $U_A = \qty{15,3}{\volt}\text{ DC}$
* dato: $U_F = \qty{0,23}{\volt}$
* dato: $R = \qty{50}{\ohm}$ dal sistema di misura
* cercato: $P_E$

<left>
<fragment>
$\begin{split}U_S &= \frac{U_A}{2} + U_F\\ &= \frac{\qty{15,3}{\volt}}{2} + \qty{0,23}{\volt}\\ &= \qty{7,88}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_{E,eff} &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{7,88}{\volt}}{1,414}\\ &= \qty{5,57}{\volt}\end{split}$
</fragment>
</right>

--- style="font-size: smaller;"
* calcolato: $U_{E,eff} = \qty{5,57}{\volt}$
* dato: $R = \qty{50}{\ohm}$ dal sistema di misura
* cercato: $P_E$

<fragment>
$\begin{split}P_E &= \frac{(U_{E,eff} \cdot 10)^2}{R}\\ &= \frac{(\qty{5,57}{\volt} \cdot 10)^2}{\qty{50}{\ohm}}\\ &\approx \qty{60}{\watt}\end{split}$
</fragment>

---
### Indicatore d’intensità di campo per la misurazione della potenza

<left>
[picture:496:a_messung_feldstaerkeanzeiger:Indicatore d’intensità di campo]
</left>
<right>
* Misurazione della potenza RF tramite un’antenna
* La RF ricevuta viene rettificata e livellata
* Visualizzazione tramite amperometro sensibile
* Maggiore la deviazione dell’indice, maggiore l’intensità di campo RF
* Misurazioni precise richiedono calibrazione
</right>

---
[question:AI613]
