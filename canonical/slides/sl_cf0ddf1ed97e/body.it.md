<left>
[photo:212:a_oszilloskop:Oscilloscopio digitale]
</left>
<right>
* Mostra l’andamento temporale delle tensioni
* Misura la forma del segnale
</right>
---
[question:AI301]
---
[question:AI304]
---
### Larghezza dell’impulso

<left>
[picture:1005:a_impulsbreite:Determinazione della larghezza dell’impulso di un segnale rettangolare non ideale]
</left>
<right>
Definizione: la larghezza dell’impulso è al 50% del valore di picco
</right>
---
[question:AI303]
---
### Trigger

<left>
[photo:219:a_oszilloskop_x-ablenkung:Senza tensione d’ingresso, su uno schermo di un oscilloscopio analogico si sposta solo un punto da sinistra a destra, qui con una velocità di un divisione per secondo.]
</left>
<right>
* Il trigger valuta il segnale in ingresso
* Ad esempio, la tensione 0 che passa da negativa a positiva
* In questo modo, per un’onda, è possibile visualizzare un’immagine stabile
</right>
---
[question:AI302]
---
### Puntali

<left>
[photo:223:a_oscilloskop_tastkoepfe:Puntali con diverse punte di prova. Per questa foto, le pinze a coccodrillo sono state rimosse.]
</left>
<right>
* Per misurare la tensione
* Punta realizzata come gancio o ago
* Massa di riferimento solitamente tramite una pinza a coccodrillo separata
* I puntali 10:1 dividono la tensione in un decimo
</right>
---
### Misurazione con un oscilloscopio

[photo:224:a_oszilloskop_messung:Misurazione con un puntale. Tra i diodi D1 e D2 si vede la punta di prova e, più a sinistra, la pinza a coccodrillo per il collegamento di massa.]
---
[question:AI305]
---
### Procedimento di soluzione
* dato: $R=\qty{50}{\ohm}$
* dato: (dalla rappresentazione) $\hat{U} = \qty{100}{\volt}$
* cercato: $P_{\textrm{PEP}}$

<fragment>
$\begin{split} P_{\textrm{PEP}} &= \frac{U_{\textrm{eff}}^2}{R} = \frac{\left(\frac{\qty{100}{\volt}}{\sqrt{2}}\right)^2}{\qty{50}{\ohm}}\\ &=\frac{\frac{(\qty{100}{\volt})^2}{2}}{\qty{50}{\ohm}} = \frac{\qty{5000}{\volt}^2}{\qty{50}{\ohm}} = \qty{100}{\watt} \end{split}$
</fragment>
---
[question:AI306]
---
### Procedimento di soluzione
* dato: $R=\qty{50}{\ohm}$
* dato: (dalla rappresentazione con puntale 10:1) $\hat{U} = \qty{6}{\volt}\cdot 10$
* cercato: $P_{\textrm{PEP}}$

<fragment>
$\begin{split} P_{\textrm{PEP}} &= \frac{U_{\textrm{eff}}^2}{R} = \frac{\left(\frac{\qty{6}{\volt}\cdot 10}{\sqrt{2}}\right)^2}{\qty{50}{\ohm}}\\ &=\frac{\frac{(\qty{60}{\volt})^2}{2}}{\qty{50}{\ohm}} = \qty{36}{\watt} \end{split}$
</fragment>

---
## Impulso

<left>
* Un segnale passa da un valore a uno più alto e, in un secondo momento, torna al valore iniziale
* La durata dell’impulso viene misurata dal centro del fronte di salita al centro del fronte di discesa
</left>
<right>
[picture:57:e_impuls:Impulso visualizzato su un oscilloscopio]
</right>
---
[question:EI303]