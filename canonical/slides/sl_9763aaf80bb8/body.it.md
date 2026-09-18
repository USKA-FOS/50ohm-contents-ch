<left>
[immagine:795:a_raddrizzamento_a_una_sola_onda_raddrizzamento_con_condensatore:Raddrizzamento a una sola onda con condensatore]
</left>
<right>
* Durante la mezza onda positiva il diodo $D$ lascia passare la corrente
* Carica il condensatore $C_L$ al valore di picco della tensione alternata e alimenta la resistenza di carico $R_L$
* Durante la mezza onda negativa il diodo $D$ è in interdizione
* Il condensatore $C_L$ si scarica attraverso la resistenza di carico $R_L$
</right>
---
<left>
[immagine:75:a_ondulazione_rimanente:Ondulazione della tensione continua di uscita $U_L$]
Al terminale della resistenza di carico $R_L$ si ottiene una tensione continua pulsante $U_L$
</left>
<right>
* Maggiore è la capacità, più la tensione continua è smussata
* Le tensioni del trasformatore sono tensioni efficaci
* Per il dimensionamento del condensatore occorre determinare la tensione di picco
* Per il diodo è rilevante la tensione picco-picco
</right>

---
[domanda:AD302]
---
#### Procedimento di soluzione
* dati: $U_\mathrm{eff} = \qty{15}{\volt}$
* cercato: $\hat{U}$

<fragment>
$\hat{U} = U_\mathrm{eff} \cdot \sqrt{2} = \qty{15}{\volt} \cdot 1,41 = \qty{21,21}{\volt}$
</fragment>
---
[domanda:AD303]
---
#### Procedimento di soluzione
* dati: $U_P = \qty{230}{\volt}$
* dati: $r = 20:1$
* cercato: $\hat{U} + \qty{50}{\percent}$

<fragment>
$r = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{r} = \frac{\qty{230}{\volt}}{20} = \qty{11,5}{\volt}$
</fragment>
<fragment>
$\hat{U} = U_S \cdot \sqrt{2} = \qty{11,5}{\volt} \cdot 1,41 \approx \qty{16,26}{\volt}$
</fragment>
<fragment>
$\hat{U} + \qty{50}{\percent} \approx \qty{25}{\volt}$
</fragment>
---
[domanda:AD304]
---
#### Procedimento di soluzione
* dati: $U_P = \qty{230}{\volt}$
* dati: $r = 5:1$
* cercato: $U_{PP} + \qty{20}{\percent}$

<fragment>
$r = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{r} = \frac{\qty{230}{\volt}}{5} = \qty{46}{\volt}$
</fragment>
<fragment>
$\hat{U} = U_S \cdot \sqrt{2} = \qty{46}{\volt} \cdot 1,41 \approx \qty{65,05}{\volt}$
</fragment>
<fragment>
$U_{PP} + \qty{20}{\percent} = 2 \cdot \hat{U} + \qty{20}{\percent} \approx \qty{156}{\volt}$
</fragment>