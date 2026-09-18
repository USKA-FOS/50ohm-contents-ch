--- style="font-size: smaller;"

## Filtri nel convertitore A/D e D/A

[picture:1131:a_adc_dac_filter:Conversione A/D e D/A con filtro anti-aliasing e filtro di ricostruzione]

* Prima del convertitore A/D: *filtro anti-aliasing*
* Dopo il convertitore D/A: *filtro di ricostruzione*
* Entrambi i filtri sopprimono componenti di frequenza indesiderate

<note>
La figura mostra l'intera catena del segnale da un segnale di ingresso analogico attraverso l'elaborazione digitale del segnale fino a un segnale di uscita analogico.

Prima del convertitore A/D si trova il filtro anti-aliasing. Dopo il convertitore D/A si trova il filtro di ricostruzione.

Perché entrambi i filtri sono necessari, lo esamineremo ora più nel dettaglio.
</note>

---

## Aliasing al convertitore A/D

* Per il campionamento vale: $f_\mathrm{S}>2\cdot f_\mathrm{max}$
* All'ingresso possono essere presenti anche frequenze più alte indesiderate
* Se la frequenza di campionamento è troppo bassa, si generano frequenze apparenti
* Queste vengono definite *aliasing*

<note>
Tramite un'antenna riceviamo di solito non solo il segnale desiderato, ma anche molte altre componenti di frequenza.

Se la frequenza di campionamento è troppo bassa per una di queste componenti di frequenza, dopo la digitalizzazione può apparire come una frequenza diversa, che non era presente nel segnale originale.

Questo effetto lo abbiamo già incontrato con il teorema di campionamento.
</note>

--- style="font-size: smaller;"

## Filtro anti-aliasing

[picture:1131:a_adc_dac_filter_aa:Conversione A/D e D/A con filtro anti-aliasing e filtro di ricostruzione]

* Il filtro si trova *prima* del convertitore A/D
* Limita la banda di frequenza del segnale di ingresso
* Possono essere utilizzati filtri passa-basso o passa-banda
* Le componenti di frequenza critiche devono essere sufficientemente attenuate

<fragment>
In particolare, le frequenze superiori a $\frac{f_\mathrm{S}}{2}$ non devono raggiungere il convertitore A/D senza essere attenuate.
</fragment>

<note>
Il filtro anti-aliasing impedisce che frequenze che richiederebbero una frequenza di campionamento più alta raggiungano il convertitore A/D.

A seconda dell'applicazione, può essere utilizzato un filtro passa-basso o passa-banda. Per i segnali vocali, ad esempio, un filtro passa-banda può essere utile.

Ciò che conta è che le componenti di frequenza che potrebbero causare aliasing vengano attenuate sufficientemente prima della digitalizzazione.
</note>

---

[question:AF622]

---

[question:AF623]

---

## Generatore di clock

<left>
[picture:1132:a_anit_alias:Filtro anti-aliasing, convertitore A/D e generatore di clock]
</left>
<right>
* Il convertitore A/D necessita di un clock per il campionamento
* Il clock definisce i momenti in cui vengono prelevati i singoli campioni
* La sua frequenza determina la frequenza di campionamento
* La frequenza di clock può essere fissa o controllabile
</right>

<note>
Il generatore di clock determina quando il convertitore A/D preleva un nuovo campione.

La sua frequenza definisce direttamente la frequenza di campionamento. La frequenza di clock può essere fissa o controllata, ad esempio, da un microcontrollore.
</note>

---

[question:AF620]

---

## Ritorno al segnale analogico

* Il convertitore D/A genera di nuovo valori di tensione analogici dai campioni digitali
* I valori vengono emessi a intervalli di tempo fissi
* All'uscita non si ottiene inizialmente un andamento del segnale idealmente liscio
* Le transizioni nette contengono componenti di frequenza elevate

<note>
Sul lato di uscita avviene il processo inverso.

Il convertitore D/A emette i singoli valori digitali come valori di tensione analogici. A causa dell'emissione a tempo discreto, inizialmente non si ottiene un andamento idealmente liscio.

In particolare, le transizioni nette e i bordi contengono componenti di segnale ad alta frequenza aggiuntive.
</note>

--- style="font-size: smaller;"

## Filtro di ricostruzione

<left>
[picture:300:a_adc_4bit:Segnale prima del filtro di ricostruzione]
</left>
<right>
[picture:299:a_adc_12bit:Segnale dopo il filtro di ricostruzione]
</right>

* Il filtro di ricostruzione si trova *dopo* il convertitore D/A
* Lascia passare la banda di frequenza utile desiderata
* Attenua le componenti di segnale ad alta frequenza indesiderate
* Possono essere utilizzati filtri passa-basso o passa-banda

<fragment>
In questo modo si ottiene nuovamente un segnale di uscita analogico il più pulito possibile.
</fragment>

<note>
Il filtro di ricostruzione rimuove le componenti di segnale ad alta frequenza indesiderate all'uscita del convertitore D/A.

A sinistra è mostrato un segnale prima della filtrazione. I bordi chiaramente visibili contengono componenti di frequenza elevate.

Dopo la filtrazione si ottiene un andamento del segnale più liscio, che si avvicina maggiormente al segnale analogico desiderato.

A seconda dell'applicazione, può essere utilizzato un filtro passa-basso o passa-banda.
</note>

---

[question:AF624]

---

[question:AF625]