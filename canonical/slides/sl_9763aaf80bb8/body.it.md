<left>
[picture:795:a_einweggleichrichtung_c:Raddrizzazione a semionda con condensatore]
</left>
<right>
* Durante la semionda positiva, il diodo $D$ lascia passare la corrente
* Carica il condensatore $C_L$ al valore di picco della tensione alternata e alimenta la resistenza di carico $R_L$
* Durante la semionda negativa, il diodo $D$ blocca
* Il condensatore $C_L$ si scarica attraverso la resistenza di carico $R_L$
</right>
---
<left>
[picture:75:a_Restwelligkeit:Ondulazione della tensione continua di uscita $U_L$]
Alla resistenza di carico $R_L$ si ottiene una tensione continua pulsante $U_L$
</left>
<right>
* Maggiore è la capacità, più smorzata è la tensione continua
* Le tensioni del trasformatore sono tensioni efficaci
* Per la progettazione del condensatore, è necessario determinare la tensione di picco
* Per il diodo, è rilevante la tensione di picco-picco
</right>

---
[question:AD302]
---
#### Percorso di soluzione
* dato: $U_{\mathrm{eff}} = \qty{15}{\volt}$
* cercato: $\hat{U}$

<fragment>
$\hat{U} = U_{\mathrm{eff}} \cdot \sqrt{2} = \qty{15}{\volt} \cdot 1,41 = \qty{21,21}{\volt}$
</fragment>
---
[question:AD303]
---
#### Percorso di soluzione
* dato: $U_P = \qty{230}{\volt}$
* dato: $ü = 20:1$
* cercato: $\hat{U} + \qty{50}{\percent}$

<fragment>
$ü = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{ü} = \frac{\qty{230}{\volt}}{20} = \qty{11,5}{\volt}$
</fragment>
<fragment>
$\hat{U} = U_S \cdot \sqrt{2} = \qty{11,5}{\volt} \cdot 1,41 \approx \qty{16,26}{\volt}$
</fragment>
<fragment>
$\hat{U} + \qty{50}{\percent} \approx \qty{25}{\volt}$
</fragment>
---
[question:AD304]
---
#### Percorso di soluzione
* dato: $U_P = \qty{230}{\volt}$
* dato: $ü = 5:1$
* cercato: $U_{SS} + \qty{20}{\percent}$

<fragment>
$ü = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{ü} = \frac{\qty{230}{\volt}}{5} = \qty{46}{\volt}$
</fragment>
<fragment>
$\hat{U} = U_S \cdot \sqrt{2} = \qty{46}{\volt} \cdot 1,41 \approx \qty{65,05}{\volt}$
</fragment>
<fragment>
$U_{SS} + \qty{20}{\percent} = 2 \cdot \hat{U} + \qty{20}{\percent} \approx \qty{156}{\volt}$
</fragment>