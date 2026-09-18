* Stabilizzazione di un oscillatore variabile e potenzialmente instabile (ad esempio VCO) tramite un oscillatore di riferimento stabile
* Confronto di fase tra i due segnali
* La frequenza di uscita corrisponde a quella di riferimento o a un suo multiplo e rimane stabile

--- style="font-size: smaller;"
[picture:45:a_oszillator_pll_pll:Rappresentazione di un anello ad aggancio di fase (PLL)]

* Il *comparatore di fase* confronta le fasi del VCO e dell'oscillatore di riferimento
* Il *filtro passa-basso* converte gli impulsi del comparatore di fase in tensione continua
* Il *VCO* genera la frequenza di uscita in base alla tensione continua proveniente dal filtro passa-basso
* Il *divisore di frequenza* (opzionale) sincronizza la frequenza del VCO a un multiplo della frequenza di riferimento

<note>
Il comparatore di fase emette impulsi in caso di scostamenti di fase, che vengono livellati dal filtro passa-basso in una tensione continua. La variazione di frequenza al VCO riduce progressivamente la differenza di fase.
</note>

---
[question:AD701]
---
[question:AD702]
---
### Precisione e stabilità

* Dipendono dalla qualità dell'oscillatore di riferimento
* Spesso si tratta di un oscillatore a quarzo

---
[question:AD705]
---
### Divisione di frequenza e sintonizzabilità

* Il divisore di frequenza consente di impostare la PLL su diverse frequenze
* La frequenza di uscita è un multiplo intero della frequenza di riferimento
* La frequenza minima selezionabile corrisponde a quella dell'oscillatore di riferimento

---
[question:AD703]
---
[question:AD704]
--- style="font-size: 0.7em;"
#### Procedimento
* dati: $f_\text{Osc} = \qty{12,5}{\kilo\hertz}$
* dati: $f_\text{Out,low} = \qty{12,000}{\mega\hertz}$
* dati: $f_\text{Out,high} = \qty{14,000}{\mega\hertz}$
* richiesto: $n$

<fragment>
Per $f_{Out,low} = \qty{12,000}{\mega\hertz}$:
$n = \frac{f_\text{Out,low}}{f_\text{Osc}} = \frac{\qty{12,000}{\mega\hertz}}{\qty{12,5}{\kilo\hertz}} = 960$
</fragment>
<fragment>
Per $f_\text{Out,high} = \qty{14,000}{\mega\hertz}$:
$n = \frac{f_\text{Out,high}}{f_\text{Osc}} = \frac{\qty{14,000}{\mega\hertz}}{\qty{12,5}{\kilo\hertz}} = 1120$
</fragment>