## Misura di corrente e tensione

<left>
* La tensione si misura in parallelo al componente
* La corrente si misura in serie al componente
</left>
<right>
[picture:1003:a_strom_spannung_messung:Misurare la potenza di un amplificatore (PA)]
</right>

---
[question:AI101]
---
[question:AI102]
---
## Precisione di misura

Il valore visualizzato di solito differisce dal valore reale a causa di:
* Resistenza interna dello strumento di misura
* Risoluzione → *risoluzione minima*
* La visualizzazione cambia solo dopo una variazione pari alla risoluzione minima
* Il produttore determina la deviazione
* La deviazione è indicata nella scheda tecnica

---

<left>
[picture:1004:a_reale_spannungsmessung:Schema equivalente di un voltmetro reale]
</left>

<right>
[picture:1007:a_reale_strommessung:Schema equivalente di un amperometro reale]
</right>

---
[question:AI103]
--- style="font-size: smaller;"
### Procedimento di soluzione

* Calcolo percentuale – i valori assoluti non sono rilevanti
* Dati: $U_{\mathrm{dev}}$ con $\qty{95}{\percent}$ del valore reale
* Dati: $I_{\mathrm{dev}}$ con $\qty{95}{\percent}$ del valore reale
* Ricercato: Deviazione della potenza $P = U \cdot I$


<fragment>
$\begin{split} P_{\textrm{dev}} &= 100\% - (U_{\mathrm{dev}} \cdot I_{\mathrm{dev}})\\ &= 100\% - (95\% \cdot 95\%)\\ &= 100\% - 90,25\%\\ &= 9,75\% \end{split}$
</fragment>

---
## Corrente attraverso il multimetro

* Anche durante una misura di tensione scorre corrente attraverso lo strumento di misura
* Si verifica una divisione della corrente
* Grazie all’elevata resistenza interna, la corrente che fluisce è relativamente piccola

---
[question:AI104]
---
### Procedimento di soluzione
* Dati: $U = \qty{0,5}{\volt}$
* Dati: $R = \qty{10}{\mega\ohm}$
* Ricercato: $I$


<fragment>
$$I = \frac{U}{R} = \frac{\qty{0,5}{\volt}}{\qty{10}{\mega\ohm}} = \qty{50}{\nano\ampere}$$
</fragment>
