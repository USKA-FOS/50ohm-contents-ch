## Demodulazione dei segnali

* La demodulazione converte un segnale RF modulato in un segnale AF udibile
* A seconda della modulazione utilizzata, si sceglie un metodo di demodulazione appropriato
* Obiettivo: ripristinare la NF originale

---
### Demodulazione AM

<left>
[picture:141:demodulator_huellkurvendemodulator_am:Demodulatore ad inviluppo per la demodulazione di segnali AM]
</left>
<right>
* I segnali AM vengono elaborati con un demodulatore ad inviluppo
* Il segnale RF viene selezionato tramite un circuito oscillante e raddrizzato
* Il condensatore si carica $\rightarrow$ la resistenza si scarica con una costante di tempo definita
</right>

---

[question:AD501]

---

<left>
[picture:607:demodulator_huellkurvendemodulator_am_2:Demodulatore ad inviluppo con segnale di ingresso IF]

[picture:146:demodulator_huellkurvendemodulator_am_abbx:Segnale demodulato nel punto X]
</left>
<right>
* Punto X: visualizzazione della tensione di picco raddrizzata
* Leggero calo della tensione dovuto allo scaricamento parallelo
* L’inviluppo corrisponde alla NF modulata, sovrapposta a un segnale a dente di sega
* Un filtro successivo rimuove la componente della portante
</right>

---

[question:AD502]

--- style="font-size: smaller;"
### Demodulazione FM

<left>
[picture:841:demodulator_flankendiskriminator:Circuito oscillante come discriminatore di pendenza]

[picture:149:demodulator_flankendiskriminator_schaltung:Discriminatore di pendenza FM]
</left>
<right>
* Demodulazione FM mediante discriminatore di pendenza
* Il segnale dalla frequenza intermedia (IF) entra in un circuito oscillante
* Circuito oscillante: frequenza di risonanza $f_\text{res}$ leggermente spostata rispetto a $f_\text{IF}$
* Le variazioni di frequenza vengono convertite in variazioni di ampiezza
* Il demodulatore AM successivo fornisce la NF
</right>

---

[question:AD504]

---

#### Demodulazione FM mediante PLL

<left>
[picture:77:a_fm_demodulation_pll:Schema a blocchi di una demodulazione FM mediante PLL]
</left>
<right>
* La PLL utilizza un oscillatore controllato in tensione (VCO) che segue il segnale di ingresso
* La tensione di regolazione corrisponde alla modulazione FM (NF modulata)
* Prelievo del segnale per l’ulteriore elaborazione della NF
</right>

---

[question:AD505]

---
### Demodulazione SSB

* La demodulazione SSB avviene tramite un rivelatore a prodotto
* Il mixer ad anello mescola la frequenza intermedia (IF) con un oscillatore a frequenza battente (BFO)
* Il prodotto di mescolamento risultante è il segnale SSB-NF desiderato
* Il BFO deve essere sintonizzato esattamente sulla portante soppressa

---

[question:AD506]
