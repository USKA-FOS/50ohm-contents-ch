## Segnale differenziali e correnti sulla calza

* Idealmente, nei conduttori interno ed esterno di un cavo coassiale circolano correnti di uguale intensità ma opposte in direzione
* La loro somma è nulla – segnale puramente differenziale
* Un segnale puramente differenziale impedisce la formazione di correnti sulla calza

---
### Segnale in modo comune e corrente sulla calza

* Se la somma delle correnti non è nulla, si genera un segnale in modo comune
* La componente in modo comune fluisce sulla superficie esterna del conduttore esterno come corrente sulla calza
* La corrente sulla calza genera un’onda sulla calza intorno al cavo

---
[question:AG425]

---
### Induttanza di modo comune

* Avvolgendo un cavo coassiale intorno a un nucleo di ferrite, si sopprimono le correnti sulla calza
* Questa configurazione è chiamata induttanza di modo comune

---
[question:AG426]

---
## Trasformatore di separazione RF per l’induttanza di modo comune

* Alternativa: trasformatore di separazione RF in cui gli avvolgimenti primario e secondario non sono collegati tra loro
* La corrente che entra in un polo esce quasi con la stessa intensità dall’altro – la componente in modo comune scompare

<note>
Tra le spire della bobina si forma una capacità che non sopprime completamente la componente in modo comune
</note>

---
[question:AJ115]

---
### Tensioni RF e correnti sulla calza

* In assenza di segnali RF in modo comune: il conduttore esterno non presenta tensione ad alta frequenza rispetto a terra
* Con segnali differenziali, il campo elettrico si forma esclusivamente tra conduttore interno ed esterno
* Effetto esterno: le correnti si annullano – nessuna corrente sulla calza
* Le correnti sulla calza sono direttamente correlate alle tensioni RF sul conduttore esterno

---
## Antenne simmetriche e tensione sul conduttore esterno

* In un’antenna simmetrica, ogni ramo del dipolo presenta una tensione rispetto a terra
* Collegando i rami dell’antenna ai conduttori del cavo coassiale si genera una tensione RF sul conduttore esterno

---
### Influenza della messa a terra nelle antenne

* Antenne ben messe a terra (ad esempio, ground plane con radiali accordati o interrati) presentano quasi $\qty{0}{\volt}$ al punto di alimentazione
* Antenne ground plane mal messe a terra possono essere suscettibili alle correnti sulla calza

---
## Accoppiamento senza contatto nello schermo del coassiale

* Le correnti sulla calza possono essere generate da accoppiamento senza contatto
* Se si fa correre un cavo di alimentazione parallelamente a un ramo del dipolo, il campo vicino dell’antenna si accoppia nello schermo del coassiale

---
[question:AG427]

---
### Balun di tensione / autotrasformatore

<left>
[picture:447:a_mantelwellen_spannungsbalun:Struttura di un balun di tensione]
</left>
<right>
* In antenne completamente simmetriche, un balun di tensione può simmetrizzare le correnti nel cavo coassiale
* Tipico autotrasformatore: il cavo coassiale è collegato al centro e alla fine di una bobina, mentre l’antenna è collegata a entrambe le estremità della bobina
</right>

---

<left>
[picture:447:a_mantelwellen_spannungsbalun:Struttura di un balun di tensione]
</left>
<right>
* La tensione raddoppia ($r = 2$) e la corrente si dimezza, ottenendo una trasformazione di impedenza 1:4
* A un cavo coassiale da $\qty{50}{\ohm}$ viene idealmente collegata un’antenna da circa $\qty{200}{\ohm}$
</right>

---
[question:AG421]

---
[question:AG422]

---
## Limitazioni dell’induttanza di modo comune

* Il balun di tensione funziona solo se l’antenna collegata è effettivamente simmetrica
* Un carico asimmetrico può favorire la formazione di correnti sulla calza
* L’accoppiamento senza contatto tramite i campi elettromagnetici vicini rimane possibile
* Un’induttanza di modo comune aggiuntiva con separazione spaziale può fornire supporto

---
[question:AG428]

---
[question:AG429]
