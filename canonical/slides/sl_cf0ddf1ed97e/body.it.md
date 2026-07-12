<left>
[photo:212:a_oszilloskop:Oscilloscopio digitale]
</left>
<right>
* Mostra l'andamento temporale delle tensioni
* Misura la forma del segnale
</right>
---
[question:AI301]
---
[question:AI304]
---
### Larghezza dell'impulso

<left>
[picture:1005:a_impulsbreite:Determinazione della larghezza dell'impulso di un segnale a onda quadra non ideale]
</left>
<right>
Definizione: La larghezza dell'impulso si misura al 50% del valore di picco
</right>
---
[question:AI303]
---
### Trigger

<left>
[photo:219:a_oszilloskop_x-ablenkung:Senza tensione di ingresso, su uno schermo di oscilloscopio analogico un punto si muove da sinistra a destra, qui a una velocità di una divisione per secondo.]
</left>
<right>
* Il trigger analizza il segnale in ingresso
* Ad esempio, la tensione attraversa da negativo a positivo lo zero
* In questo modo è possibile visualizzare un'immagine fissa di un'onda
</right>
---
[question:AI302]
---
### Sonde

<left>
[photo:223:a_oszilloskop_tastkoepfe:Sonde con diverse punte di prova. Le pinze a coccodrillo sono state rimosse per questa ripresa.]
</left>
<right>
* Per la misurazione della tensione
* Punta costruita come uncino o ago
* Massa di riferimento solitamente tramite un morsetto a coccodrillo separato
* Le sonde 10:1 dividono la tensione per dieci
</right>
---
### Misurazione con un oscilloscopio

[photo:224:a_oszilloskop_messung:Misurazione con una sonda. Tra i diodi D1 e D2 si vede la punta di prova e più a sinistra il morsetto a coccodrillo per il collegamento di massa.]
---
[question:AI305]
---
### Percorso di soluzione
* dato: $R=50\Omega$
* dato: (dalla rappresentazione) $\hat{U} = 100V$
* cercato: $P_{\textrm{PEP}}$

<fragment>
$\begin{split} P_{\textrm{PEP}} &= \frac{U_{\textrm{eff}}^2}{R} = \frac{\left(\frac{\qty{100}{\volt}}{\sqrt{2}}\right)^2}{\qty{50}{\ohm}}\\ &=\frac{\frac{(\qty{100}{\volt})^2}{2}}{\qty{50}{\ohm}} = \frac{\qty{5000}{\volt}^2}{\qty{50}{\ohm}} = \qty{100}{\watt} \end{split}$
</fragment>
---
[question:AI306]
---
### Percorso di soluzione
* dato: $R=\qty{50}{\ohm}$
* dato: (dalla rappresentazione con sonda 10:1) $\hat{U} = \qty{6}{\volt}\cdot 10$
* cercato: $P_{\textrm{PEP}}$

<fragment>
$\begin{split} P_{\textrm{PEP}} &= \frac{U_{\textrm{eff}}^2}{R} = \frac{\left(\frac{\qty{6}{\volt}\cdot 10}{\sqrt{2}}\right)^2}{\qty{50}{\ohm}}\\ &=\frac{\frac{(\qty{60}{\volt})^2}{2}}{\qty{50}{\ohm}} = \qty{36}{\watt} \end{split}$
</fragment>

---
## Impulso

<left>
* Un segnale salta da un valore a uno più alto e in un secondo momento ritorna indietro
* La durata dell'impulso viene misurata dalla metà del fianco ascendente alla metà del fianco discendente
</left>
<right>
[picture:57:e_impuls:Impulso in un oscilloscopio] 
</right>
---
[question:EI303]