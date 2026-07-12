## Campionamento: Da analogico a digitale

* I segnali analogici vengono convertiti in valori digitali tramite campionamento  
* Il campionamento avviene in intervalli di tempo definiti – vengono misurati solo gli stati istantanei  
* I segnali analogici sono continui nel tempo, poiché non hanno una risoluzione temporale minima  
* I campioni digitali sono discreti nel tempo, poiché esiste un intervallo di campionamento fisso

---

[include:quantisierung_und_sampling]

---

## Continuità di valore vs. Discretizzazione di valore

* I segnali analogici possono assumere valori di tensione arbitrari – sono continui nel valore  
* Nella digitalizzazione ci sono solo gradazioni limitate (ad es. $\num{-128}$ a $\num{+127}$) – i campioni sono discreti nel valore
* Tra due stadi di tensione, il convertitore A/D deve prendere una decisione (quantizzazione)

---

## Esempio pratico: Dimmer vs. Interruttore a gradini

* Un dimmer analogico consente regolazioni di luminosità fini e continue  
* Un interruttore a gradini (ad es. $\num{5}$ livelli) consente solo valori di luminosità fissi – i livelli intermedi non sono possibili
* Quantizzazione: Selezione del livello più vicino per rappresentare il valore analogico

---

[question:AF601]

---

[question:AF603]

---

[question:AF602]

---

[question:AF604]