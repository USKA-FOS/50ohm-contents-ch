* Le antenne hanno una resistenza di alimentazione o di base, a seconda dell’esatta disposizione degli elementi dell’antenna
* Se questa non corrisponde all’impedenza caratteristica della linea di alimentazione, si verifica una *riflessione*
* La potenza di trasmissione viene riflessa verso l’apparecchio radio $\rightarrow$ non può essere irradiata dall’antenna
* Se la resistenza di alimentazione dell’antenna e l’impedenza caratteristica della linea di alimentazione coincidono, si ha un *adattamento*

---

## Rapporto d’onda stazionaria (ROS)

* Valore di misura per la qualità dell’adattamento dell’antenna
* Indica in modo semplificato quanta potenza di trasmissione viene riflessa dall’antenna
* Abbreviazione ROS dal termine inglese *standing wave ratio*
* Misurato con un *misuratore di ROS*, abbreviato in *rosmetro*

<note>
Calcolo preciso: $\text{ROS} = \frac {\sqrt{P_\text{V}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{V}}-\sqrt{P_\text{R}}}$ con $P_\text{V}$ potenza incidente e $P_\text{R}$ potenza riflessa — non richiesto per l’esame di classe N
</note>

---

## Rosmetro

Misura contemporaneamente la potenza di trasmissione verso l’antenna e la potenza riflessa

<left>
[photo:144:swr_meter:Un semplice rosmetro per determinare il rapporto d’onda stazionaria]
</left>
<right>
[photo:143:swr_meter_kreuzzeiger:Rosmetro con indice a croce; l’indice di sinistra indica la potenza incidente, quello di destra la potenza riflessa. Per leggere il ROS, si segue la linea verde fino all’intersezione dei due indici verso il basso]
</right>
---
Viene inserito tra trasmettitore-ricevitore e antenna o è già integrato nel trasmettitore-ricevitore

<left>
[picture:670:n_trx_kabel_swr_antenne:Schema di principio di un rosmetro tra trasmettitore-ricevitore e antenna]
</left>
<right>
[photo:67:n_swr_display:Display di un trasmettitore-ricevitore]
</right>
<note>
Rosmetro e S-metro hanno un nome simile, ma sono diversi: il rosmetro misura il rapporto d’onda stazionaria durante la trasmissione, l’S-metro l’intensità del segnale durante la ricezione
</note>

---
[question:NI201]

---
[question:NF101]

---
[question:NI202]

---
## Adattamento ottimale

* In caso di adattamento perfetto viene visualizzato il valore $\num{1}$
* Il valore migliore raggiungibile
* L’intera potenza viene assorbita dall’antenna
* Nessuna potenza viene riflessa verso il trasmettitore

---
[question:NG301]

---
[question:NI203]

---
## Adattamento scadente

* In caso di adattamento scadente viene visualizzato un valore prossimo all’infinito ($\infty$)
* Nessuna antenna collegata, linea di trasmissione interrotta o in corto circuito
* Adattamento scadente dell’antenna o linea di trasmissione danneggiata
* Nel caso peggiore può danneggiare il trasmettitore

---

* Con ROS $\num{2}$ viene riflessa il $\qty{11}{\percent}$ della potenza di trasmissione
* Con ROS $\num{3}$ viene riflessa il $\qty{25}{\percent}$ della potenza di trasmissione
* I trasmettitori-ricevitori moderni riducono automaticamente la potenza di trasmissione per proteggere il trasmettitore

---
[question:NG302]

---
[question:NG303]

---
## Elevata attenuazione del cavo

* Riduce il segnale riflesso
* Porta a una distorsione della misurazione
* Ad esempio in caso di cavo lungo
* Il segnale viene attenuato sia all’andata che al ritorno

---
[question:NG208]

<note>
* Il ROS sembra migliorare, ma solo la potenza riflessa viene attenuata
</note>