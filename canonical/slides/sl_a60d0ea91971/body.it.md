## Segnale differenziale e onde di mantelletto

* Idealmente, correnti di uguale intensità e opposta direzione scorrono nel conduttore interno ed esterno di un cavo coassiale comune
* La loro somma è zero: segnale differenziale puro
* Un segnale differenziale puro impedisce l'insorgenza di onde di mantelletto

---
### Segnale di modo comune e corrente di mantelletto

* Se la somma delle correnti è diversa da zero, si genera un segnale di modo comune
* La componente di modo comune scorre sulla superficie esterna del conduttore esterno come corrente di mantelletto
* La corrente di mantelletto crea un'onda di mantelletto attorno al cavo

---
[question:AG425]

---
### Bobina a modo comune

* Cavo coassiale comune avvolto attorno a un nucleo di ferrite, sopprime le onde di mantelletto
* Questa configurazione è chiamata bobina a modo comune

---
[question:AG426]

---
## Trasformatore di isolamento HF come trappola per onde di mantelletto

* Alternativa: trasformatore di isolamento HF, in cui l'avvolgimento primario e secondario non sono collegati
* La corrente che entra in un polo esce quasi con la stessa intensità dall'altro: la componente di modo comune viene eliminata

<note>
Tra le spire della bobina si forma una Capacità, che non sopprime completamente la componente di modo comune
</note>

---
[question:AJ115]

---
### Tensioni HF e onde di mantelletto

* In assenza di segnali di modo comune HF: il conduttore esterno non presenta tensione ad alta frequenza rispetto alla terra
* Con segnali differenziali, il campo elettrico si forma esclusivamente tra il conduttore interno e quello esterno
* Effetto esterno: le correnti si annullano - nessuna onda di mantelletto
* Le onde di mantelletto sono direttamente correlate alle tensioni HF sul conduttore esterno

---
## Antenne simmetriche e tensione del conduttore esterno

* In un'antenna simmetrica, ogni elemento del dipolo presenta una tensione rispetto alla terra
* Il collegamento degli elementi dell'antenna ai conduttori del cavo coassiale comune provoca una tensione HF sul conduttore esterno

---
### Influenza della messa a terra nelle antenne

* Antenne ben messe a terra (ad es. Groundplane con radiali accordati o interrati) hanno quasi $\qty{0}{\volt}$ al punto di alimentazione
* Le antenne Groundplane mal messe a terra possono essere suscettibili alle onde di mantelletto

---
## Accoppiamento senza contatto nel schermo del coassiale

* Le onde di mantelletto possono originarsi per accoppiamento senza contatto
* Se si fa passare un cavo di alimentazione parallelamente a un elemento del dipolo, il campo vicino dell'antenna si accoppia nello schermo del coassiale

---
[question:AG427]

---
### Balun di tensione / Trasformatore di impedenza

<left>
[picture:447:a_mantelwellen_spannungsbalun:Struttura di un balun di tensione]
</left>
<right>
* Per antenne completamente simmetriche, un balun di tensione può symmetrizzare le correnti nel cavo coassiale comune
* Tipico trasformatore di impedenza: cavo coassiale comune collegato al centro e a un'estremità di una bobina, antenna collegata a entrambe le estremità della bobina
</right>

---

<left>
[picture:447:a_mantelwellen_spannungsbalun:Struttura di un balun di tensione]
</left>
<right>
* Il raddoppio della Tensione ($ü = 2$) e la dimezzamento della Corrente portano a una trasformazione di Impedenza di 1:4
* A un cavo coassiale comune da $\qty{50}{\ohm}$ viene idealmente collegata un'antenna da circa $\qty{200}{\ohm}$
</right>

---
[question:AG421]

---
[question:AG422]

---
## Limitazioni della trappola per onde di mantelletto


* Il balun di tensione funziona solo se l'antenna collegata è effettivamente simmetrica
* Un carico asimmetrico può favorire le onde di mantelletto
* L'accoppiamento senza contatto tramite i campi vicini elettromagnetici rimane possibile
* Una trappola per onde di mantelletto aggiuntiva con distanza spaziale può agire in modo di supporto

---
[question:AG428]

---
[question:AG429]
