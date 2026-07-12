* Stabilizzazione di un oscillatore variabile, potenzialmente instabile (es. VCO) mediante un oscillatore di riferimento stabile
* Confronto di fase tra i due segnali
* La frequenza di uscita corrisponde alla frequenza di riferimento o a un multiplo e rimane stabile

--- style="font-size: smaller;"
[picture:45:a_oszillator_pll_pll:Rappresentazione di un Phase-Locked Loop (PLL)]

* Il *comparatore di fase* confronta le fasi del VCO e dell'oscillatore di riferimento
* Il *filtro passa-basso* converte gli impulsi del comparatore di fase in tensione continua
* Il *VCO* genera la frequenza di uscita in base alla tensione continua dal filtro passa-basso
* Il *divisore di frequenza* (opzionale) sincronizza la frequenza del VCO su un multiplo della frequenza di riferimento

<note>
Il comparatore di fase emette impulsi in caso di deviazioni di fase, che vengono livellati dal filtro passa-basso in una tensione continua. La differenza di fase viene ridotta gradualmente modificando la frequenza del VCO.
</note>

---
[question:AD701]
---
[question:AD702]
---
### Precisione e stabilità

* Dipende dalla qualità dell'oscillatore di riferimento
* Spesso un oscillatore a quarzo

---
[question:AD705]
---
### Divisione di frequenza e sintonizzazione

* Il divisore di frequenza consente di impostare il PLL su frequenze diverse
* La frequenza di uscita è un multiplo intero della frequenza di riferimento
* La frequenza più bassa selezionabile corrisponde all'oscillatore di riferimento

---
[question:AD703]
---
[question:AD704]
--- style="font-size: 0.7em;"
#### Percorso di soluzione
* Dato: $f_\text{Osc} = \qty{12,5}{\kilo\hertz}$
* Dato: $f_\text{Out,low} = \qty{12,000}{\mega\hertz}$
* Dato: $f_\text{Out,high} = \qty{14,000}{\mega\hertz}$
* Cercato: $n$

<fragment>
Con $f_{Out,low} = \qty{12,000}{\mega\hertz}$:
$n = \frac{f_\text{Out,low}}{f_\text{Osc}} = \frac{\qty{12,000}{\mega\hertz}}{\qty{12,5}{\kilo\hertz}} = 960$
</fragment>
<fragment>
Con $f_\text{Out,high} = \qty{14,000}{\mega\hertz}$:
$n = \frac{f_\text{Out,high}}{f_\text{Osc}} = \frac{\qty{14,000}{\mega\hertz}}{\qty{12,5}{\kilo\hertz}} = 1120$
</fragment>