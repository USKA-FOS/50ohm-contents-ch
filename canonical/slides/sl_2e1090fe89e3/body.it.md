## Resistenza dei fili

<left>
* Il materiale conduttivo è composto da atomi in una struttura (reticolare)
* Gli elettroni sono condivisi e quindi liberi di muoversi
* A seconda del materiale, ci sono più o meno elettroni liberi che urtano contro gli atomi
</left>
<right>
[picture:713:a_leitermodell:Atomi (+) ed elettroni mobili (-) in un conduttore metallico]
</right>

---
### Resistività $\rho$
<left>
$R = \frac{\rho\cdot l}{A_{\textrm{Dr}}}$

* $l$: Lunghezza del filo
* $A_{\textrm{Dr}}$: Sezione del filo
* $\rho$: Resistività in $\unit{\ohm\cdot\milli\meter\squared\per\meter}$
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
Ciò consente di calcolare la resistenza ohmica di un filo quando il materiale, la lunghezza e la sezione trasversale sono noti.
</note>

---
[question:AB101]
---
<div style="font-size: smaller;">
### Percorso di soluzione
* Dato: $l = \qty{1,8}{\meter}$
* Dato: $d = \qty{0,2}{\milli\meter}$
* Dato: $\rho = \qty{0,018}{\ohm\cdot\milli\meter\squared\per\meter}$
* Cercato: $R$

<fragment>
$$A_{\textrm{Dr}} = \frac{d^2\cdot \pi}{4} = \frac{(\qty{0,2}{\milli\meter})^2 \cdot \pi}{4} = \frac{\pi}{100}\unit{\milli\meter\squared} = \qty{0,0314}{\milli\meter\squared}$$
</fragment>
<fragment>
$$R = \frac{\rho\cdot l}{A_{\textrm{Dr}}} = \frac{\qty{0,018}{\ohm\cdot\milli\meter\squared\per\meter} \cdot \qty{1,8}{\meter}}{\qty{0,0314}{\milli\meter\squared}} \approx \qty{1,02}{\ohm}$$
</fragment>
</div>
---
[question:AB102]
---
### Percorso di soluzione
* Dato: $A_{\textrm{Dr}} = \qty{0,5}{\milli\meter\squared}$
* Dato: $R = \qty{1,5}{\ohm}$
* Dato: $\rho = \qty{0,018}{\ohm\cdot\milli\meter\squared\per\meter}$
* Cercato: $l$

<fragment>
$\begin{split} R &= \frac{\rho\cdot l}{A_{\textrm{Dr}}}\\ \Rightarrow l &= \frac{R\cdot A_{\textrm{Dr}}}{\rho} = \frac{\qty{1,5}{\ohm} \cdot \qty{0,5}{\milli\meter\squared}}{\qty{0,018}{\ohm\cdot\milli\meter\squared\per\meter}} \approx \qty{41,7}{\meter} \end{split}$
</fragment>

---
## Coefficiente di temperatura

* La resistenza dei metalli aumenta all'aumentare della temperatura
* Gli atomi si muovono di più a temperature più elevate, causando più collisioni con gli elettroni

---
[question:AB103]