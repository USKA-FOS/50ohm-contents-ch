<left>
[picture:965:a_brueckenlgeichrichter:Raddrizzatore a ponte]
</left>
<right>
* Circuito raddrizzatore esteso e frequente
* Entrambe le semionde vengono utilizzate
* Tensione continua pulsante all’uscita con frequenza doppia rispetto a quella d’ingresso
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
* Con condensatore di carica $C_L$ e circuito di filtraggio LC con $C_S$
* Ampiezze più piccole della tensione continua pulsante
* I condensatori si caricano alla tensione di picco secondaria
</right>
<note>
</note>
---
[question:AD306]
---
#### Procedimento di soluzione
* dato: $U_P = \qty{230}{\volt}$
* dato: $r = 8:1$
* dato: $U_D = \qty{0,6}{\volt}$
* cercato: $\hat{U}$

<fragment>
$r = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{r} = \frac{\qty{230}{\volt}}{8} = \qty{28,75}{\volt}$
</fragment>
<fragment>
A vuoto si può trascurare la tensione della diodo.
$\hat{U} = U_S \cdot \sqrt{2} = \qty{28,75}{\volt} \cdot 1,41 \approx \qty{40}{\volt}$
</fragment>
