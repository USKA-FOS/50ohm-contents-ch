## Onda fondamentale e armoniche

* Un segnale sinusoidale ideale è composto solo dalla sua onda fondamentale (1ª armonica)
* Deviazioni dalla forma sinusoidale generano multipli interi della frequenza fondamentale
* Questi multipli vengono chiamati armoniche

--- style="font-size: smaller;"
### Rappresentazione nello spettro di frequenza

<left>
[picture:869:zusammenhang_oberwellen_harmonische:Relazione tra armoniche superiori e armoniche]
</left>
<right>
* 1ª armonica = frequenza fondamentale
* 2ª armonica = frequenza doppia rispetto alla fondamentale
* 3ª armonica = frequenza tripla rispetto alla fondamentale
* Tutte le armoniche sono numerate con un numero d'ordine (n)
</right>
<note>
A seconda della distorsione del segnale, si generano più armoniche pari o armoniche dispari.
I segnali rettangolari (ad esempio, dovuti alla saturazione dell'amplificatore) contengono principalmente armoniche dispari.
I segnali a dente di sega contengono prevalentemente armoniche pari.
</note>

--- style="font-size: smaller;"
### Armoniche superiori – multipli della frequenza fondamentale

<left>
[picture:595:a_oberwellen:Segnale composto da fondamentale e armoniche superiori]
</left>
<right>
* Un segnale non perfettamente sinusoidale contiene anche armoniche superiori
* Le armoniche superiori sono multipli interi della frequenza fondamentale
* 1ª armonica superiore = 2ª armonica = frequenza doppia rispetto alla fondamentale
* 2ª armonica superiore = 3ª armonica = frequenza tripla rispetto alla fondamentale
</right>

---
[question:AB403]

---
[question:AB401]

---
[question:AB402]

---
## Analisi delle armoniche superiori con l'analizzatore di spettro

* Anche un segnale apparentemente sinusoidale può contenere armoniche superiori significative
* Le componenti delle armoniche superiori vengono misurate con un analizzatore di spettro
* Rappresentazione nel dominio delle frequenze (Frequency-Domain)
* Le ampiezze delle armoniche superiori vengono visualizzate in scala logaritmica

---
[question:AI615]

---
[question:AI614]

---
## Calcolo di armoniche e armoniche superiori

* Frequenze armoniche = frequenza fondamentale × numero d'ordine (n)
* Frequenze delle armoniche superiori = frequenza fondamentale × (n + 1)

---
[question:AJ201]

---
#### Procedimento di soluzione
* dati: $f = \qty{3,730}{\mega\hertz}$
* richiesto: $f$ della 2ª armonica

<fragment>
$2 \cdot f = 2 \cdot \qty{3,730}{\mega\hertz} = \qty{7,460}{\mega\hertz}$
</fragment>

---
[question:AJ205]

---
#### Procedimento di soluzione
* dati: $f = \qty{144,690}{\mega\hertz}$
* richiesto: $f$ come 2ª armonica dispari

<fragment>
2ª armonica dispari = 3ª armonica
  
$3 \cdot f = 3 \cdot \qty{144,690}{\mega\hertz} = \qty{434,070}{\mega\hertz}$
</fragment>
---
[question:AJ202]

---
#### Procedimento di soluzione
* dati: $f = \qty{7,050}{\mega\hertz}$
* richiesto: $f$ come 3ª armonica

<fragment>
$3 \cdot f = 3 \cdot \qty{7,050}{\mega\hertz} = \qty{21,150}{\mega\hertz}$
</fragment>

---
[question:AJ206]

---
#### Procedimento di soluzione
* dati: $f = \qty{144,300}{\mega\hertz}$
* richiesto: più armoniche

<fragment>
$\begin{split}2 \cdot \qty{144,300}{\mega\hertz} &= \qty{288,600}{\mega\hertz}\\ 3 \cdot \qty{144,300}{\mega\hertz} &= \bold{\qty{432,900}{\mega\hertz}}\\ &\vdots\\ 9 \cdot \qty{144,300}{\mega\hertz} &= \bold{\qty{1298,700}{\mega\hertz}}\n\end{split}$
</fragment>