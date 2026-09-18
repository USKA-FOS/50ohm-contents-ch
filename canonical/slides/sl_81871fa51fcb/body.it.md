---

### Simbolo
* Un *simbolo* è uno stato di segnale distinguibile.
* I simboli possono differenziarsi, ad esempio, per ampiezza, frequenza o fase.
* Più simboli possibili consentono di trasmettere più bit per simbolo.

---

### Velocità di simbolo
* La *velocità di simbolo* indica il numero di simboli trasmessi al secondo; l’unità di misura della velocità di simbolo è il *baud*.
* La velocità di trasmissione dati e la velocità di simbolo non sono quindi sempre identiche.
* Se vengono utilizzati solo due simboli e ogni bit viene trasmesso singolarmente, la velocità di simbolo in baud corrisponde alla velocità di trasmissione dati in $\unit{\bit\per\secondo}$.
* Se invece vengono utilizzati più simboli e quindi più bit vengono trasmessi contemporaneamente, la velocità di trasmissione dati è maggiore della velocità di simbolo.

---

**Esempi**

* 2 simboli → 1 bit/simbolo
* 4 simboli → 2 bit/simbolo
* 8 simboli → 3 bit/simbolo

---

* La formula $R_\mathrm{D} = R_\mathrm{S} \cdot N$ rappresenta la relazione:

<fragment>
* $R_\mathrm{D}$ → velocità di trasmissione dati in $\unit{\bit\per\secondo}$
* $R_\mathrm{S}$ → velocità di simbolo in $\unit{\baud}$
* $N$ → dimensione del simbolo in $\unit{\bit\per\simbolo}$
</fragment>

---

[question:AA104]

---

Esempi:

<fragment>
*RTTY*: commutazione tra due frequenze di simbolo, in modo che per ogni simbolo possa essere trasmesso un bit ($\num{0}$ o $\num{1}$).
→ Velocità di trasmissione dati = velocità di simbolo
</fragment>

<fragment>
*FT4*: commutazione tra quattro frequenze di simbolo, in modo che per ogni simbolo possano essere trasmessi due bit ($\num{00}$, $\num{01}$, $\num{10}$ o $\num{11}$).
→ Velocità di trasmissione dati = 2 $\cdot$ velocità di simbolo
</fragment>

---

[question:AE405]

---

#### Procedimento
* dati: $R_S = \qty{45,45}{\baud}$
* dati: $N=\qty{1}{\bit\per\simbolo}$
* richiesto: $R_\mathrm{D}$


<fragment>
$R_\mathrm{D} = R_\mathrm{S} \cdot N = \qty{45,45}{\baud} \cdot \qty{1}{\bit\per\simbolo} = \qty{45,45}{\bit\per\secondo}$
</fragment>

---

[question:AE406]

---

#### Procedimento
* dati: $R_S = \qty{23,4}{\baud}$
* dati: $N=\qty{2}{\bit\per\simbolo}$
* richiesto: $R_\mathrm{D}$


<fragment>
$R_\mathrm{D} = R_\mathrm{S} \cdot N = \qty{23,4}{\baud} \cdot \qty{2}{\bit\per\simbolo} = \qty{46,8}{\bit\per\secondo}$
</fragment>