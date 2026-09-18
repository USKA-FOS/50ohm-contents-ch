---
## Carico fittizio nella gamma HF

<left>
[picture:47:a_dummy_load:Carico fittizio composto da più catene di resistenze]
</left>
<right>
* Spesso composto da più resistenze parziali per un migliore raffreddamento e una maggiore capacità di carico
* Le resistenze possono essere collegate in parallelo, in serie o in combinazione
</right>
---

* Valori identici delle resistenze garantiscono una distribuzione uniforme della potenza dissipata
* Il calcolo viene effettuato secondo la legge di Ohm e le regole per le connessioni in serie e in parallelo

---
[question:AI601]

--- style="font-size: smaller;"
#### Procedimento di soluzione
<left>
* dato: $R = \qty{150}{\ohm}$
* dato: $R_S = 4\cdot \qty{150}{\ohm} = \qty{600}{\ohm}$
</left>
<right>
* dato: $R_{ges} = \qty{50}{\ohm}$
* dato: $P_R = \qty{1}{\watt}$
* cercato: $n$ resistenze, $P$
</right>

<fragment>
Serie con 4 resistenze ciascuna:
$\frac{1}{R_{ges}} = n_S \cdot \frac{1}{R_S} \Rightarrow n_S = \frac{R_S}{R_{ges}} = \frac{\qty{600}{\ohm}}{\qty{50}{\ohm}} = 12$
$n = 4 \cdot n_S = 4 \cdot 12 = 48$
</fragment>
<fragment>
$P = n \cdot P_R = 48 \cdot \qty{1}{\watt} = \qty{48}{\watt}$
</fragment>

---
### Carico fittizio con uscita di misura

* Può essere utilizzato per la misurazione indiretta della potenza d’uscita di un trasmettitore
* Il raddrizzatore del valore di picco converte la tensione HF in tensione continua

---
[question:AI602]

---
### Misurazione della potenza d’uscita HF tramite partitore di tensione

* Un carico fittizio con presa intermedia consente una determinazione approssimativa della potenza
* La tensione HF parziale viene calcolata tramite il rapporto del partitore di tensione
* La misurazione è possibile con una sonda HF e un multimetro

---
[question:AI603]

