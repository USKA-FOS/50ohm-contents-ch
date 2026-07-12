## Misurazione di corrente e tensione

<left>
* La tensione viene misurata in parallelo al componente
* La corrente viene misurata in serie con il componente
</left>
<right>
[picture:1003:a_strom_spannung_messung:Misurazione della potenza di un amplificatore (PA)]
</right>

---
[question:AI101]
---
[question:AI102]
---
## Precisione di misurazione

Il valore misurato visualizzato differisce solitamente dal valore effettivo
* Resistenza interna dello strumento di misura
* Capacità di risoluzione $\rightarrow$ *risoluzione più piccola*
* L'indicazione cambia solo dopo una variazione pari alla risoluzione più piccola
* Il produttore determina la deviazione
* La deviazione è indicata nella scheda tecnica

---

<left>
[picture:1004:a_reale_spannungsmessung:Schema di equivalenza strumento di misura della tensione reale]
</left>

<right>
[picture:1007:a_reale_strommessung:Schema di equivalenza strumento di misura della corrente reale]
</right>

---
[question:AI103]
--- style="font-size: smaller;"
### Percorso di soluzione

* Calcolo percentuale – i valori assoluti non sono rilevanti
* dato: $U_{\mathrm{Abw}}$ con $\qty{95}{\percent}$ del valore reale
* dato: $I_{\mathrm{Abw}}$ con $\qty{95}{\percent}$ del valore reale
* cercato: deviazione della potenza $P = U \cdot I$

<fragment>
$\begin{split} P_{\textrm{Abw}} &= 100\% - (U_{\mathrm{Abw}} \cdot I_{\mathrm{Abw}})\\ &= 100\% - (95\% \cdot 95\%)\\ &= 100\% - 90,25\%\\ &= 9,75\% \end{split}$
</fragment>

---
## Corrente attraverso il multimetro

* Anche durante una misurazione di tensione, una corrente scorre attraverso uno strumento di misura
* Avviene una divisione della corrente
* A causa dell'elevata Resistenza interna, la corrente che scorre via è relativamente piccola

---
[question:AI104]
---
### Percorso di soluzione
* dato: $U = \qty{0,5}{\volt}$
* dato: $R = \qty{10}{\mega\ohm}$
* cercato: $I$

<fragment>
$$I = \frac{U}{R} = \frac{\qty{0,5}{\volt}}{\qty{10}{\mega\ohm}} = \qty{50}{\nano\ampere}$$
</fragment>

