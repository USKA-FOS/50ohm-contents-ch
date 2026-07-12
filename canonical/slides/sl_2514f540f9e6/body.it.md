<left>
[picture:965:a_brueckenlgeichrichter:Raddrizzatore a ponte]
</left>
<right>
* Circuito raddrizzatore esteso e comune
* Entrambe le semionde vengono utilizzate
* Tensione continua pulsante all'uscita con frequenza doppia rispetto alla tensione d'ingresso
</right>
--- style="font-size: smaller;"
[include:applet_gleichrichter_2]

---
[question:AD305]
---
### Filtraggio
<left>
[picture:66:a_netzteil_Ucs:Circuito raddrizzatore con filtraggio]
</left>
<right>
* Con condensatore di carica $C_L$ e elemento di filtro LC con $C_S$
* Ampiezze più piccole della tensione continua pulsante
* I condensatori si caricano fino alla tensione di picco secondaria
</right>
<note>
</note>
---
[question:AD306]
---
#### Percorso di soluzione
* dato: $U_P = \qty{230}{\volt}$
* dato: $ü = 8:1$
* dato: $U_D = \qty{0,6}{\volt}$
* cercato: $\hat{U}$

<fragment>
$ü = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{ü} = \frac{\qty{230}{\volt}}{8} = \qty{28,75}{\volt}$
</fragment>
<fragment>
A vuoto, la tensione del diodo può essere trascurata.
$\hat{U} = U_S \cdot \sqrt{2} = \qty{28,75}{\volt} \cdot 1,41 \approx \qty{40}{\volt}$
</fragment>
