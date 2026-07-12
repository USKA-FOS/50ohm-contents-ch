* *Classe di amplificazione A*: Può amplificare l'intero segnale
* *Classe di amplificazione B*: Viene amplificata bene metà del segnale
* *Classe di amplificazione A/B*: Combinazione di A e B con amplificazione di poco più della metà del segnale
* *Classe di amplificazione C*: Viene amplificata bene meno della metà del segnale

<fragment>
Le classi di amplificazione sono determinate dalla scelta del punto di funzionamento
</fragment>

<note>
Le designazioni alfabetiche derivano da una prima classificazione sistematica di amplificatori a valvole e a transistor
</note>
---
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Curva caratteristica di un transistor con punti di funzionamento]
</left>
<right>
* La curva caratteristica del transistor mostra la relazione tra segnale di ingresso e segnale di uscita
* Tensione base-emettitore o gate-source e corrente di collettore o di drenaggio
* Nelle aree lineari la variazione è proporzionale
* Altre aree sono non lineari
</right>
---
### Punto di funzionamento

* Funzionamento ottimale con scelta ottimale del punto di funzionamento sulla curva caratteristica
* Il punto di funzionamento è determinato dalla tensione di polarizzazione sulla base o sul gate
* L'amplificazione agisce quindi attorno al punto di funzionamento desiderato

---
### Corrente di riposo

* La corrente di riposo deriva dalla scelta del punto di funzionamento
* Fluisce anche senza segnale di ingresso
* Influenza l'efficienza di un amplificatore
* Aumenta la potenza dissipata termica
* Riduce il rendimento

--- style="font-size: smaller;"
### AP1
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Curva caratteristica di un transistor con punti di funzionamento]  
</left>
<right>
* Funzionamento in classe C dell'amplificatore
* senza tensione di polarizzazione
* corrente di riposo zero
* rendimento ca. $\qtyrange{80}{87}{\percent}$
* elevata componente di armoniche superiori
</right>
--- style="font-size: smaller;"
### AP2
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Curva caratteristica di un transistor con punti di funzionamento]  
</left>
<right>
* Funzionamento in classe B dell'amplificatore
* Bassa tensione di polarizzazione fino all'inizio della corrente di collettore
* Corrente di riposo quasi zero (bassa)
* Rendimento fino a $\qty{80}{\percent}$
* Bassa componente di armoniche superiori
</right>
--- style="font-size: smaller;"
### AP3
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Curva caratteristica di un transistor con punti di funzionamento]  
</left>
<right>
* Funzionamento in classe A/B dell'amplificatore
* Tensione di polarizzazione più alta rispetto alla classe B, ma inferiore rispetto alla classe A
* Corrente di riposo maggiore rispetto alla classe B, ma significativamente inferiore rispetto alla classe A
* Rendimento tra $\qty{50}{\percent}$ e $\qty{80}{\percent}$
* Bassa componente di armoniche superiori
</right>
--- style="font-size: smaller;"
### AP4
<left>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Curva caratteristica di un transistor con punti di funzionamento]  
</left>
<right>
* Funzionamento in classe A dell'amplificatore
* La tensione di polarizzazione è scelta in modo che la corrente di riposo raggiunga circa il $\qty{50}{\percent}$ del valore massimo consentito
* Rendimento ca. $\qty{40}{\percent}$
* Componente di armoniche superiori molto bassa
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
* Calcolare la potenza di corrente continua
* La potenza d’uscita è il prodotto della potenza di corrente continua e del rendimento

---
[question:AD424]
---
#### Percorso di soluzione
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
#### Percorso di soluzione
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

* È necessaria un'amplificazione lineare
* Amplificazione in classe A, A/B o B
* In caso di sovraeccitazione si verificano distorsioni del segnale $\rightarrow$ splatter sulle frequenze adiacenti

---
[question:AD422]
---
[question:AJ218]
---
[question:AD423]
---
### Funzionamento in classe C

* Il punto di funzionamento non lineare genera armoniche superiori
* Devono essere successivamente soppresse tramite filtraggio
* Schermatura tramite un involucro metallico

---
[question:AF402]
---
[question:AF403]
