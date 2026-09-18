## Emissioni indesiderate causate da prodotti di mescolamento


<left>
[picture:243:a_unerwuenschte_aussendungen_bandpassfilter:Risposta in frequenza di un filtro passa-banda]
</left>
<right>
* Si formano nella preparazione della frequenza dei trasmettitori  
* I prodotti di mescolamento si generano nei mixer  
* I filtri passa-banda sopprimono i segnali indesiderati  
</right>

---

[question:AJ208]


---

[question:AJ211]


---

[question:AJ209]


---


### Armoniche e armoniche superiori


<left>
[picture:868:a_harmonische: Armoniche superiori (OW), armoniche (Harm.) e emissioni parassite (NA)]
</left>
<right>
* Multipli della frequenza fondamentale di un segnale  
* Differenza nella definizione e nel conteggio  
* 1ª armonica = frequenza fondamentale  
* 2ª armonica = 1ª armonica superiore  
* 3ª armonica = 2ª armonica superiore  
</right>

---

[question:AJ204]


---

#### Percorso di soluzione
* dato: $f = \qty{29,5}{\mega\hertz}$
* dato: $n = 3$
* dato: banda radio: $\qtyrange{88,5}{108,0}{\mega\hertz}$


<fragment>
$f \cdot n = \qty{29,5}{\mega\hertz} \cdot 3 = \qty{88,5}{\mega\hertz}$
</fragment>


---

[question:AJ203]


---
#### Percorso di soluzione
* dato: $f = \qty{7,20}{\mega\hertz}$
* dato: $n = 4$
* cercato: 3ª armonica superiore


<fragment>
$f \cdot n = \qty{7,20}{\mega\hertz} \cdot 4 = \qty{28,80}{\mega\hertz}$
</fragment>


---

### Formazione delle armoniche superiori


<left>
[picture:106:a_unerwuenschte_aussendungen_uebersteuerung:Segnale sovraeccitato]
</left>
<right>
* Causa: sovraeccitazione degli stadi amplificatori  
* La limitazione dei picchi di ampiezza porta a distorsioni  
* Le armoniche superiori compaiono quando la forma d'onda sinusoidale non è ideale  
</right>

<note>
Le armoniche superiori e le armoniche si formano sempre quando si verificano deviazioni dalla curva sinusoidale ideale.
</note>

---

[question:AJ207]


---

## Circuiti trappola per la soppressione


* Soppressione di singole armoniche superiori o armoniche  
* Circuito trappola: attenua al massimo una frequenza specifica  
* Le altre frequenze vengono lasciate passare quasi senza attenuazione  


---

[question:AJ210]


---

## Emissioni parassite


* Si verificano in prossimità del segnale trasmesso  
* Difficili da sopprimere con i filtri  
* Causa: sovraeccitazione dell'amplificatore del microfono  
* Allargano involontariamente il segnale trasmesso (emissione parassita, prodotti secondari, "splatter")


---

[question:AJ219]


---

## Disturbi causati da tensione di alimentazione instabile


* Alimentatori scadenti generano tensione di ronzio  
* Può portare a emissioni in AM  
* Interferenze in BF influenzano il trasmettitore  
* Particolarmente problematico nei trasmettitori più vecchi  


---

[question:AJ222]


---

[question:AJ223]


---

## Limiti di legge per armoniche superiori ed emissioni parassite


* I radioamatori devono rispettare i limiti di legge  
* Due bande di frequenza con requisiti diversi  


<note>
Ulteriori informazioni nella [Disposizione 33](http://50ohm.de/vfg33) del 2007.
</note>

---

### Banda HF ($\qtyrange{1,7}{35}{\mega\hertz}$)


* Attenuazione minima di $\qty{40}{\dB}$
* Rilevante la potenza del segnale superiore a $\qty{0,25}{\micro\watt}$


---

[question:AJ224]


---

### Banda VHF/UHF/SHF ($\qtyrange{50}{1000}{\mega\hertz}$)


* Attenuazione minima di $\qty{60}{\dB}$
* Rilevante la potenza del segnale superiore a $\qty{0,25}{\micro\watt}$


---

[question:AJ225]