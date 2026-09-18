## Larghezza di banda
<left>
* Al contrario dell'AM, viene utilizzata meno della metà della larghezza di banda
* Massimo $\qty{2,7}{\kilo\hertz}$
* Corrisponde al segnale in BF
</left>
<right>
[picture:743:e_bandbreite_am_ssb:Larghezza di banda di AM, USB e LSB]
</right>

---
[question:EE201]
---
[question:EE202]
---
[question:EJ210]

---

## Modulazione

<left>
* Tramite miscelazione e filtraggio
* Con la selezione preventiva di USB e LSB viene scelta la frequenza portante
* Attraverso il mixer si generano due frequenze
* Nel filtro di banda viene lasciata passare solo una frequenza
</left>
<right>
[picture:500:e_ssb_modulation:Schema a blocchi per la modulazione SSB con il metodo del filtro]
</right>

---
<left>
* Il trucco qui è che il filtro di banda ha solo una frequenza di risonanza
* Spostando la frequenza portante nell'oscillatore, viene lasciata passare la banda laterale desiderata
</left>
<right>
[picture:500:e_ssb_modulation:Schema a blocchi per la modulazione SSB con il metodo del filtro]
</right>
---
<left>
Esempio LSB:
* Microfono: $\qty{300}{\hertz}$ - $\qty{3}{\kilo\hertz}$
* Oscillatore LSB: $\qty{9001,5}{\kilo\hertz}$
* Segnale DSB:<br/> a) $\qtyrange{8998,5}{9001,2}{\kilo\hertz}$<br/> b) $\qtyrange{9001,8}{9004,5}{\kilo\hertz}$
* Filtro: $\qty{9000}{\kilo\hertz}\pm\qty{1,5}{\kilo\hertz}$
* Segnale SSB:<br/> $\qtyrange{8998,5}{9001,2}{\kilo\hertz}$
</left>
<right>
[picture:831:e_ssb_modulation_lsb:Frequenze con il metodo del filtro in LSB]
[picture:940:e_ssb_modulation_lsb_spektrum:Spettro con il metodo del filtro in LSB]
</right>
<note>
* L'interruttore nell'immagine dovrebbe essere su LSB
* Viene lasciata passare solo la frequenza a)
* Il segnale SSB può essere nuovamente miscelato per un'emissione nella banda radioamatoriale
</note>
---
<left>
Esempio USB:
* Microfono: $\qty{300}{\hertz}$ - $\qty{3}{\kilo\hertz}$
* Oscillatore USB: $\qty{8998,5}{\kilo\hertz}$
* Segnale DSB:<br/> a) $\qtyrange{8995,5}{8998,2}{\kilo\hertz}$<br/> b) $\qtyrange{8998,8}{9001,5}{\kilo\hertz}$
* Filtro: $\qty{9000}{\kilo\hertz}\pm\qty{1,5}{\kilo\hertz}$
* Segnale SSB:<br/> $\qtyrange{8998,8}{9001,5}{\kilo\hertz}$
</left>
<right>
[picture:832:e_ssb_modulation_usb:Frequenze con il metodo del filtro in USB]
[picture:941:e_ssb_modulation_usb_spektrum:Spettro con il metodo del filtro in USB]
</right>
<note>
* Viene lasciata passare solo la frequenza b)
* Il segnale SSB può essere nuovamente miscelato per un'emissione nella banda radioamatoriale
</note>

---
[question:EE203]
---
[question:EE204]

---
### Segnale in BF

<left>
* Per la voce è sufficiente tra $\qty{300}{\hertz}$ e $\qty{3000}{\hertz}$
* Corrisponde a $\qty{2,7}{\kilo\hertz}$
* Vengono utilizzati anche filtri più piccoli, ad esempio $\qty{2,4}{\kilo\hertz}$
* Molti ricetrasmettitori permettono di regolare i filtri
</left>
<right>
* Se viene utilizzato un segnale in BF con larghezza di banda maggiore, aumenta la larghezza di banda in HF
* Va evitato per non disturbare i segnali adiacenti
* Prestare attenzione alla larghezza di banda massima nel piano delle bande
</right>

---
[question:EJ211]
<note>
* Se vengono sottratti i $\qty{300}{\hertz}$ inferiori del segnale in BF, si ottengono nuovamente $\qty{2,7}{\kilo\hertz}$
</note>
---
[question:EF310]
---
[question:EE207]

---
## Amplificazione del microfono
* Con la potenza in BF si controlla la potenza in HF
* Un microfono troppo silenzioso riduce la potenza in uscita del trasmettitore
* Un'amplificazione del microfono troppo elevata può causare interferenze con stazioni su frequenze adiacenti

---
[question:EE206]
---
[question:EE205]
---
[question:EJ215]