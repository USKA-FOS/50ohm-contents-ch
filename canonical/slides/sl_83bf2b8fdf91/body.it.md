* *Classe A*: può amplificare l’intero segnale
* *Classe B*: viene amplificato bene solo il segnale per metà
* *Classe A/B*: combinazione tra A e B con amplificazione di poco più della metà del segnale
* *Classe C*: viene amplificato bene solo meno della metà del segnale

<fragment>
Le classi di amplificazione vengono determinate dalla scelta del punto di funzionamento
</fragment>

<note>
La denominazione con lettere risale a una prima classificazione sistematica di amplificatori a valvole e a transistor
</note>
---
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Kennlinie eines Transistors mit Arbeitspunkten]
</left>
<right>
* La curva caratteristica del transistor mostra la relazione tra segnale di ingresso e segnale di uscita
* Tensione base-emettitore o gate-source e corrente di collettore o drain
* Nelle zone lineari la variazione è proporzionale
* Altre zone sono non lineari
</right>
---
### Punto di funzionamento

* Funzionamento ottimale con scelta ottimale del punto di funzionamento sulla curva caratteristica
* Il punto di funzionamento viene determinato dalla tensione di polarizzazione alla base o al gate
* L’amplificazione agisce quindi intorno al punto di funzionamento desiderato

---
### Corrente di riposo

* La corrente di riposo deriva dalla scelta del punto di funzionamento
* Scorre anche in assenza di segnale di ingresso
* Influenza l’efficienza di un amplificatore
* Aumenta la potenza dissipata termicamente
* Riduce il rendimento

--- style="font-size: smaller;"
### AP1
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Kennlinie eines Transistors mit Arbeitspunkten]  
</left>
<right>
* Funzionamento in classe C dell’amplificatore
* Senza polarizzazione
* Corrente di riposo nulla
* Rendimento circa $\qtyrange{80}{87}{\percent}$
* Alto contenuto di armoniche
</right>
--- style="font-size: smaller;"
### AP2
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Kennlinie eines Transistors mit Arbeitspunkten]  
</left>
<right>
* Funzionamento in classe B dell’amplificatore
* Polarizzazione ridotta fino all’insorgere della corrente di collettore
* Corrente di riposo quasi nulla (minima)
* Rendimento fino a $\qty{80}{\percent}$
* Basso contenuto di armoniche
</right>
--- style="font-size: smaller;"
### AP3
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Kennlinie eines Transistors mit Arbeitspunkten]  
</left>
<right>
* Funzionamento in classe A/B dell’amplificatore
* Polarizzazione più alta che in classe B, ma inferiore a quella in classe A
* Corrente di riposo maggiore che in classe B, ma nettamente inferiore a quella in classe A
* Rendimento tra $\qty{50}{\percent}$ e $\qty{80}{\percent}$
* Basso contenuto di armoniche
</right>
--- style="font-size: smaller;"
### AP4
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Kennlinie eines Transistors mit Arbeitspunkten]  
</left>
<right>
* Funzionamento in classe A dell’amplificatore
* La polarizzazione è scelta in modo che la corrente di riposo raggiunga circa il $\qty{50}{\percent}$ del valore massimo consentito
* Rendimento circa $\qty{40}{\percent}$
* Contenuto di armoniche molto basso
</right>
---
[question:AD416]
---
[question:AD419]
---
[question:AD420]
---
[question:AD421]
---
### Potenza d’uscita

* Conoscendo il punto di funzionamento, il rendimento è noto
* Calcolare la potenza in corrente continua
* La potenza d’uscita è il prodotto tra la potenza in corrente continua e il rendimento

---
[question:AD424]
---
#### Procedimento
* dato: $U=\qty{50}{\volt}$
* dato: $I = \qty{2}{\ampere}$
* dato: $\eta_\text{A} \approx \qty{40}{\percent}$
* cercato: $P_\text{ab}$

<fragment>
$P_\text{zu} = U \cdot I = \qty{50}{\volt} \cdot \qty{2}{\ampere} = \qty{100}{\watt}$
</fragment>
<fragment>
$\eta_\text{A} = \frac{P_\text{ab}}{P_\text{zu}} \Rightarrow P_\text{ab} = \eta_\text{A} \cdot P_\text{zu} = 0,4 \cdot \qty{100}{\watt} = \qty{40}{\watt}$
</fragment>
---
[question:AD425]
---
#### Procedimento
* dato: $U=\qty{50}{\volt}$
* dato: $I = \qty{2}{\ampere}$
* dato: $\eta_\text{C} \approx \qty{85}{\percent}$
* cercato: $P_\text{ab}$

<fragment>
$P_\text{zu} = U \cdot I = \qty{50}{\volt} \cdot \qty{2}{\ampere} = \qty{100}{\watt}$
</fragment>
<fragment>
$\eta_\text{C} = \frac{P_\text{ab}}{P_\text{zu}} \Rightarrow P_\text{ab} = \eta_\text{C} \cdot P_\text{zu} = 0,85 \cdot \qty{100}{\watt} = \qty{85}{\watt}$
</fragment>
---
[question:AD418]
---
[question:AD417]
---
### Funzionamento SSB

* È necessaria un’amplificazione lineare
* Amplificazione in classe A, A/B o B
* In caso di sovraeccitazione si verificano distorsioni del segnale $\rightarrow$ splatter su frequenze adiacenti

---
[question:AD422]
---
[question:AJ218]
---
[question:AD423]
---
### Classe C

* Il punto di funzionamento non lineare genera armoniche
* Devono essere attenuate tramite filtraggio
* Schermatura tramite un involucro metallico

---
[question:AF402]
---
[question:AF403]
