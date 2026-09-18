* Nel campo della tecnica radio, i dispositivi che operano mediante elaborazione digitale del segnale sono detti dispositivi SDR.
* *SDR* sta per Software Defined Radio.
* In questi dispositivi almeno una parte dell’elaborazione del segnale è implementata tramite software.
* Questo comporta un vantaggio in termini di costi e offre una grande flessibilità.

---
[question:EF603]
---
## Convertitore analogico-digitale

* Affinché i dati possano essere elaborati in modo digitale, devono essere prima digitalizzati.
* A questo scopo, il segnale analogico viene convertito in valori digitali tramite un convertitore analogico-digitale (A/D).

---
<left>
* In questo processo, il segnale analogico viene campionato a intervalli di tempo fissi e mappato in un intervallo di valori digitali (ad esempio da $\num{-128}$ a $\num{+127}$).
* I singoli valori misurati del segnale sono detti *samples* (campioni).
</left>
<right>
[picture:411:e_digitale_signalverarbeitung:Rappresentazione semplificata di un’onda sinusoidale composta da $\num{16}$ campioni e $\num{7}$ valori]
</right>
<note>
* Maggiori dettagli nella classe A
</note>

---
[question:EF602]
---
## Convertitore digitale-analogico

* Dopo l’elaborazione digitale del segnale, questo viene riconvertito in un segnale analogico tramite un convertitore digitale-analogico (D/A).


---
[question:EF601]