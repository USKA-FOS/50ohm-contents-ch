### Diodi a semiconduttore nei modulatori

* Fino ad ora noti come raddrizzatori
* La tensione BF modifica la resistenza del diodo
* Il segnale BF controlla la corrente del diodo
* Il segnale HF viene modulato in base al ritmo del segnale BF
* La variante più semplice presenta una portante e due bande laterali

---
### Diodo nel modulatore AM
<left>
[picture:772:a_modulatoren_am_modulator:Modulatore AM]
</left>
<right>
* Un diodo viene alimentato contemporaneamente con un segnale BF e uno HF
* Un circuito oscillante LC filtra il segnale di uscita
</right>

---
[question:AD507]

---
### Miscelatore bilanciato per la soppressione della portante
* Quattro diodi disposti ad anello sopprimono la portante
* Un circuito push-pull annulla i segnali della portante
* Rimangono solo le bande laterali
* Già illustrato nel capitolo "Mixer II" come miscelatore bilanciato

---
### Modulatore bilanciato nel modulatore SSB
* Il modulatore bilanciato genera un segnale a doppia banda laterale (DSB)
* Un filtro passa-banda lascia passare solo una banda laterale
* Da ciò deriva un segnale SSB
* Sono necessarie due fasi
 
---
[question:AE206]

---
[question:AF302]

---
### Riconoscimento di un miscelatore bilanciato
<left>
[picture:759:a_modulatoren_dsb:Modulatore per segnali AM con portante soppressa]
</left>
<right>
* Un anello di diodi contraddistingue il miscelatore bilanciato
* Non vi è un’eccitazione push-pull completa
* Un trasformatore fornisce l’equivalente di un centro-tap
</right>

---
[question:AF308]

<note>
* La modulazione BF viene immessa nel ramo del ponte tra il centro-tap di T2 e la massa
* Il segnale dell’oscillatore viene immesso nell’anello di diodi tramite T1
* Il segnale DSB viene disaccoppiato tramite T2
* Senza modulazione i partitori di tensione sono collegati a massa
* In questo modo la portante viene soppressa
* Con la modulazione il potenziale si sposta e la corrente fluisce in T2
* Si genera il segnale di uscita
</note>

---
### Soppressione della portante e bilanciamento

* La soppressione della portante provoca l’annullamento di segnali indesiderati
* Il circuito del modulatore deve essere bilanciato

---
[question:AD510]

---
### Regolazione nel modulatore

<left>
[picture:762:a_modulatoren_rc_traegerunterdrueckung:$R_1$ e $C_1$ per la regolazione della soppressione della portante in base al valore assoluto e alla fase]
</left>
<right>
* Le ampiezze vengono regolate con potenziometri
* Le fasi vengono regolate con trimmer capacitivi
</right>

---
[question:AF309]

---
### Simmetrizzazione nel modulatore

* Il modulatore viene simmetrizzato per sopprimere la portante
* Le bande laterali di modulazione rimangono preservate

---
[question:AF304]

---
[question:AF303]

---
### Seconda fase del modulatore SSB

<left>
[picture:98:a_modulatoren_blockschaltbild_sender:Schema a blocchi di un trasmettitore]
</left>
<right>
* Dopo il modulatore bilanciato segue la seconda fase
* Tramite filtraggio viene selezionata la banda laterale desiderata
</right>

---
[question:AF305]

---
### Frequenza del quarzo e posizione della banda laterale

<left>
[picture:500:a_modulatoren_quarzfilter:Filtro a quarzo per la selezione della banda laterale]
</left>
<right>
* I quarzi determinano la frequenza della portante soppressa
* Per il LSB la portante si trova $\qty{1,5}{\kilo\hertz}$ sopra il centro a $\qty{9}{\mega\hertz}$
* Con una massima $\qty{3}{\kilo\hertz}$ di BF, il LSB si trova $\qty{1,5}{\kilo\hertz}$ sotto il centro
* Per il USB vale il contrario
</right>

---
[question:AF306]

---
[question:AF307]
---
#### Procedimento di soluzione
* dato: $f_Q = \qty{9}{\mega\hertz}$
* dato: $f_{LSB} = \qty{9,0015}{\mega\hertz}$
* cercato: $f_{USB}$

<fragment>
$\begin{split}f_{USB} &= f_Q - (f_{LSB} - f_Q)\\ &= \qty{9}{\mega\hertz} - (\qty{9,0015}{\mega\hertz} - \qty{9}{\mega\hertz})\\ &= \qty{9}{\mega\hertz} - \qty{0,0015}{\mega\hertz}\\ &=\qty{8,9985}{\mega\hertz}\end{split}$ 
</fragment>

---
### Diodi a capacità nei modulatori FM

<left>
[picture:951:a_modulatoren_fm_modulator:Modulatore FM con varicap]
</left>
<right>
* I modulatori FM utilizzano diodi a capacità
* Il diodo fa parte di un circuito oscillante dell’oscillatore
* La tensione inversa imposta una capacità fissa del diodo
* Un segnale BF modifica la frequenza dell’oscillatore in base al ritmo
</right>

---
[question:AD508]

---
### Influenza del diodo a capacità

<left>
[picture:158:a_modulatoren_fm_varicap:Varicap per influenzare la frequenza dell’oscillatore]
</left>
<right>
* Il diodo a capacità influenza la frequenza dell’oscillatore
* È collegato in parallelo al circuito oscillante
</right>

---
[question:AF310]

---
### Limitazione della deviazione FM
* Alte tensioni BF portano a cambiamenti eccessivi di frequenza
* È necessaria una limitazione della deviazione
* Diodi collegati anti-parallel limitano la tensione al valore di soglia

---
[question:AD509]

---
### Analisi del segnale di un diodo
<left>
[picture:142:a_modulatoren_regelspannung:Circuito con un’uscita per una tensione di regolazione]
</left>
<right>
* Un singolo segnale non indica la presenza di un modulatore
* Un condensatore elettrolitico all’uscita indica la presenza di tensione continua
</right>

---
[question:AD503]
