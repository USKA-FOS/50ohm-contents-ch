## Demodulazione dei segnali

* La demodulazione converte un segnale HF modulato in un segnale NF udibile  
* A seconda della modulazione utilizzata, viene scelto un metodo di demodulazione appropriato  
* Obiettivo: Ripristino della NF originale

---
### Demodulazione AM

<left>
[picture:141:demodulator_huellkurvendemodulator_am:Demodulatore di inviluppo per la demodulazione di segnali AM]
</left>
<right>
* I segnali AM vengono elaborati con un demodulatore di inviluppo  
* Il segnale HF viene selezionato tramite un circuito oscillante e raddrizzato  
* Il condensatore si carica $\rightarrow$ la resistenza si scarica con una costante di tempo definita
</right>

---

[question:AD501]

---

<left>
[picture:607:demodulator_huellkurvendemodulator_am_2:Demodulatore di inviluppo con segnale di ingresso IF]

[picture:146:demodulator_huellkurvendemodulator_am_abbx:Segnale demodulato al punto X]
</left>
<right>
* Collegamento X: Visualizzazione della tensione di picco raddrizzata  
* Leggera diminuzione della tensione dovuta alla scarica parallela  
* L'inviluppo corrisponde alla NF modulata, sovrapposta a un segnale a dente di sega  
* Un filtro successivo rimuove la componente portante
</right>

---

[question:AD502]

--- style="font-size: smaller;"
### Demodulazione FM

<left>
[picture:841:demodulator_flankendiskriminator:Circuito oscillante come discriminatore di fianco]

[picture:149:demodulator_flankendiskriminator_schaltung:Discriminatore di fianco FM]
</left>
<right>
* Demodulazione FM tramite discriminatore di fianco  
* Il segnale dalla frequenza intermedia entra in un circuito oscillante  
* Circuito oscillante: Frequenza di risonanza $f_\text{res}$ leggermente spostata rispetto a $f_\text{IF}$
* Le variazioni di frequenza vengono convertite in variazioni di ampiezza  
* Un demodulatore AM a valle fornisce la NF
</right>

---

[question:AD504]

---

#### Demodulazione FM tramite PLL  

<left>
[picture:77:a_fm_demodulation_pll:Schema a blocchi di una demodulazione FM tramite PLL]
</left>
<right>
* La PLL utilizza un oscillatore controllato in tensione (VCO) che segue il segnale di ingresso  
* La tensione di controllo corrisponde alla modulazione FM (NF modulata)
* Prelievo del segnale per ulteriore elaborazione NF
</right>

---

[question:AD505]

---
### Demodulazione SSB

* Demodulazione SSB tramite detettore di prodotto  
* Il mixer ad anello miscela la frequenza intermedia (IF) con un oscillatore a frequenza di battimento (BFO)  
* Il prodotto di miscelazione risultante è il segnale SSB NF desiderato  
* Il BFO deve essere sintonizzato esattamente sulla portante soppressa

---

[question:AD506]

