## Trasformata di Fourier e scomposizione dei segnali

* I segnali possono essere rappresentati sia nel dominio del tempo che in quello della frequenza
  * Nel dominio del tempo: asse X → tempo, asse Y → tensione o potenza
  * Nel dominio della frequenza: asse X → frequenza, asse Y → ampiezza o potenza

---

### Scomposizione dei segnali

* Ogni segnale può essere rappresentato come una sovrapposizione di oscillazioni sinusoidali
* Ogni oscillazione sinusoidale ha una determinata ampiezza e fase
* Questo principio consente di scomporre segnali complessi nei loro componenti fondamentali

---

### Trasformata di Fourier

* Procedimento matematico complesso che analizza un segnale nel tempo
* Mostra quali oscillazioni sinusoidali (frequenze) sono contenute nel segnale
* Il risultato viene rappresentato come uno spettro di frequenza (asse X: frequenza, asse Y: ampiezza/potenza)

---

### Fast Fourier Transform (FFT)

* Calcolo efficiente della trasformata discreta di Fourier (DFT)
* Riduce notevolmente il carico computazionale
* Ampiamente diffuso in software e hardware per l'elaborazione dei segnali

--- style="font-size: smaller;"

## Spettri di forme d'onda tipiche

* *Seno*: solo una frequenza: $f$
* *Onda quadra*: solo multipli dispari: $f$, $3f$, $5f$, $7f$, ...
* *Dente di sega*: tutti i multipli interi: $f$, $2f$, $3f$, $4f$, ...
* *Triangolare*: solo multipli dispari: $f$, $3f$, $5f$, $7f$, ... (le armoniche superiori diminuiscono più rapidamente che nell'onda quadra)

All'esame è necessario saper distinguere solo tra seno e onda quadra.

<note>
Sia il segnale ad onda quadra che quello triangolare contengono solo armoniche dispari. La differenza risiede nella diminuzione delle ampiezze: nel segnale triangolare le armoniche superiori si attenuano molto più rapidamente che nell'onda quadra.
</note>

---

[question:AF630]

---

[question:AB404]

---

[question:AB405]

---

[question:AB406]

---

[question:AB407]
