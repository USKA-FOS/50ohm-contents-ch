## Resistenza dei fili

<left>
* I materiali conduttori sono composti da atomi disposti in una struttura (reticolare)
* Gli elettroni sono condivisi e quindi liberi di muoversi
* A seconda del materiale, ci sono più o meno elettroni liberi che urtano contro gli atomi
</left>
<right>
[picture:713:a_leitermodell:Atomi (+) ed elettroni (-) mobili in un conduttore metallico]
</right>

---
### Resistività $\rho$
<left>
$R = \frac{\rho\cdot l}{A_{\textrm{filo}}}$

* $l$: lunghezza del filo
* $A_{\textrm{filo}}$: sezione del filo
* $\rho$: resistività in $\unit{\ohm\cdot\milli\metro\quadrato\per\metro}$
</left>
<right>
<fragment>
* Rame: 0,018
* Alluminio: 0,028
* Oro: 0,022
* Argento: 0,016
* Zinco: 0,11
* Ferro: 0,1
* Ottone: 0,07
</fragment>
</right>
<note>
Con questa formula è possibile calcolare la resistenza ohmica di un filo conoscendo il materiale, la lunghezza e la sezione trasversale
</note>

---
[question:AB101]
--- style="font-size: smaller;"
### Procedimento di soluzione
* dati: $l = \qty{1,8}{\metro}$
* dati: $d = \qty{0,2}{\milli\metro}$
* dati: $\rho = \qty{0,018}{\ohm\cdot\milli\metro\quadrato\per\metro}$
* incognita: $R$

<fragment>
$$A_{\textrm{filo}} = \frac{d^2\cdot \pi}{4} = \frac{(\qty{0,2}{\milli\metro})^2 \cdot \pi}{4} = \frac{\pi}{100}\unit{\milli\metro\quadrato} = \qty{0,0314}{\milli\metro\quadrato}$$
</fragment>
<fragment>
$$R = \frac{\rho\cdot l}{A_{\textrm{filo}}} = \frac{\qty{0,018}{\ohm\cdot\milli\metro\quadrato\per\metro} \cdot \qty{1,8}{\metro}}{\qty{0,0314}{\milli\metro\quadrato}} \approx \qty{1,02}{\ohm}$$
</fragment>
---
[question:AB102]
---
### Procedimento di soluzione
* dati: $A_{\textrm{filo}} = \qty{0,5}{\milli\metro\quadrato}$
* dati: $R = \qty{1,5}{\ohm}$
* dati: $\rho = \qty{0,018}{\ohm\cdot\milli\metro\quadrato\per\metro}$
* incognita: $l$

<fragment>
$\begin{split} R &= \frac{\rho\cdot l}{A_{\textrm{filo}}}\\ \Rightarrow l &= \frac{R\cdot A_{\textrm{filo}}}{\rho} = \frac{\qty{1,5}{\ohm} \cdot \qty{0,5}{\milli\metro\quadrato}}{\qty{0,018}{\ohm\cdot\milli\metro\quadrato\per\metro}} \approx \qty{41,7}{\metro} \end{split}$
</fragment>

---
## Coefficiente di temperatura

* La resistenza dei metalli aumenta con l'aumentare della temperatura
* A temperature più elevate, gli atomi si muovono di più, causando più collisioni con gli elettroni

---
[question:AB103]