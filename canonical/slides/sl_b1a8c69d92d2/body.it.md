## Campionamento e quantizzazione

Quando si digitalizza un segnale analogico, è necessario considerare due proprietà:

* **Quando** viene misurato il segnale?
  * Campionamento
  * a tempo continuo → a tempo discreto
* **Quanto precisamente** viene rappresentato il valore misurato?
  * Quantizzazione
  * a valori continui → a valori discreti

<note>
Campionamento e quantizzazione sono due passaggi distinti.

Nel campionamento viene discretizzata l'asse temporale: il segnale viene considerato solo in determinati istanti di campionamento.

Nella quantizzazione, invece, viene discretizzato l'asse dei valori: un valore misurato viene assegnato a uno di un numero finito di livelli possibili.
</note>

---

## Segnale analogico

[picture:408:a_wertkont_zeitkont:Segnale a valori e tempo continui]

* In qualsiasi istante è presente un valore del segnale
* Il valore del segnale può assumere qualsiasi valore intermedio
* Un segnale analogico ideale è quindi *a tempo e a valori continui*

--- style="font-size: smaller;"

## Campionamento

<left>
[picture:408:a_wertkont_zeitkont:Segnale a valori e tempo continui]
</left>
<right>
[picture:409:a_wertkont_zeitdisk:Segnale a valori continui e tempo discreto]
</right>

<fragment>
* Il segnale viene campionato solo in determinati istanti di tempo
* I singoli valori di campionamento sono chiamati *campioni*
* Da un segnale a tempo continuo si ottiene un segnale *a tempo discreto*
* I valori stessi possono inizialmente assumere ancora qualsiasi valore
</fragment>

<note>
Nel campionamento idealizzato, inizialmente viene modificata solo l'asse temporale.

Prima del campionamento, il segnale è definito in ogni istante. Successivamente, sono disponibili valori solo in determinati istanti di campionamento.

I singoli valori dei campioni non devono ancora essere quantizzati in questa fase. Pertanto, il segnale a destra è a tempo discreto, ma ancora a valori continui.
</note>

---

[question:AF601]

---

[question:AF603]

---

## Campionamento

* Il processo di campionamento temporale è chiamato *campionamento*
* I singoli valori di campionamento sono chiamati *campioni*
* Tra due campioni, il segnale analogico può continuare a variare

<fragment>
Il campionamento significa quindi:

**a tempo continuo → a tempo discreto**
</fragment>

---

[question:AF606]

---

## Frequenza di campionamento

* La *frequenza di campionamento* o *Abtastrate* indica quante campioni vengono acquisiti per unità di tempo
* Unità: campioni per secondo

<fragment>
Esempio CD audio:

$\num{44100}$ campioni per secondo

corrispondono a

$\qty{44,1}{\kilo\sps}$
</fragment>

<note>
Più alta è la frequenza di campionamento, minore è l'intervallo temporale tra due campioni consecutivi.

Quale frequenza di campionamento sia necessaria almeno, verrà trattato successivamente con il teorema di campionamento.
</note>

---

[question:AF615]

---

## Quantizzazione

* I valori dei segnali analogici possono assumere qualsiasi valore intermedio: *a valori continui*
* In digitale sono disponibili solo un numero finito di valori possibili: *a valori discreti*
* Un valore misurato deve essere assegnato a uno dei livelli disponibili

<fragment>
Questo processo è chiamato *quantizzazione*.
</fragment>

<note>
Dopo il campionamento, sappiamo in quali istanti considerare il segnale.

Ora dobbiamo decidere con quale valore numerico digitale rappresentare il valore analogico misurato.

Se il valore effettivo si trova tra due livelli possibili, viene assegnato a un livello appropriato.
</note>

--- style="font-size: smaller;"

## A valori continui e a valori discreti

<left>
[picture:410:a_wertdisk_zeitkont:Segnale a valori discreti e tempo continuo]
</left>
<right>
[picture:411:a_wertdisk_zeitdisk:Segnale a valori e tempo discreti]
</right>

* A sinistra: i valori sono già discreti, il tempo è ancora continuo
* A destra: valori e tempo sono discreti

<fragment>
Combinando **campionamento e quantizzazione** si ottiene la rappresentazione digitale di un segnale analogico.
</fragment>

<note>
La rappresentazione a sinistra serve principalmente a mostrare che la discrezione temporale e quella dei valori sono due proprietà indipendenti.

Per la digitalizzazione è particolarmente importante la rappresentazione a destra: dopo il campionamento e la quantizzazione, sono disponibili solo singoli campioni che possono assumere solo un numero finito di valori possibili.
</note>

---

[question:AF602]

---

[question:AF604]

---

[question:AF605]

---

## Esempio pratico: Dimmer vs. interruttore a gradini

* Un dimmer analogico consente regolazioni fini e senza gradini della luminosità
* Un interruttore a gradini (ad esempio $\num{5}$ gradini) permette solo valori di luminosità fissi – non sono possibili valori intermedi
* Quantizzazione: selezione del gradino più adatto per rappresentare il valore analogico

---
## Riepilogo

<left>
[include:quantisierung_und_sampling]
</left>
<right>
* Il campionamento determina **quando** viene considerato un valore
* La quantizzazione determina **quale valore digitale** ne risulta
* Solo entrambi i passaggi insieme danno origine a un segnale a tempo e a valori discreti
</right>

<note>
Con l'applet è possibile osservare insieme campionamento e quantizzazione.

La frequenza di campionamento influisce sull'intervallo temporale tra i campioni. La quantizzazione, invece, determina quali valori possibili possono assumere i campioni.

In questo modo, i due passaggi inizialmente indipendenti possono essere compresi insieme.
</note>