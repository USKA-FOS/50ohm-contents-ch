## Conversione A/D e D/A

* *Convertitori analogico-digitale* (A/D) trasformano segnali analogici in valori digitali
* *Convertitori digitale-analogico* (D/A) trasformano valori digitali in segnali analogici
* Entrambi possiedono solo un numero finito di valori possibili
* Una proprietà importante è quindi la loro *risoluzione*

<note>
I convertitori A/D e D/A rappresentano l'interfaccia tra il mondo analogico e quello digitale.

Il convertitore A/D genera campioni digitali a partire da un segnale di ingresso analogico. Il convertitore D/A esegue l'operazione inversa e produce valori di tensione analogici a partire da dati digitali.
</note>

---
## Quantizzazione nel convertitore A/D

* Il convertitore A/D può generare solo un numero limitato di valori digitali
* I valori di ingresso analogici vengono quindi assegnati a livelli fissi
* I valori intermedi non possono essere rappresentati con precisione
* Si verifica così un *errore di quantizzazione*

<note>
Abbiamo già incontrato la quantizzazione.

Un valore analogico misurato si trova spesso tra due livelli digitali possibili. Il convertitore A/D deve assegnarlo a uno di questi livelli.

La deviazione che si verifica tra il valore reale e quello rappresentato viene chiamata errore di quantizzazione.
</note>

---

[question:AF607]

---
## Risoluzione di un convertitore A/D

* La risoluzione indica il numero di valori digitali distinguibili
* Viene solitamente espressa in *bit*
* $\qty{8}{\bit}$ → $\num{256}$ valori possibili
* $\qty{16}{\bit}$ → $\num{65536}$ valori possibili
* Più bit consentono una rappresentazione più fine dell'ampiezza del segnale

---
## Influenza della risoluzione

<left>
[picture:300:a_adc_4bit:Segnale sinusoidale digitalizzato da un convertitore A/D a 4 bit e successiva conversione D/A]
</left>
<right>
[picture:299:a_adc_12bit:Segnale sinusoidale digitalizzato da un convertitore A/D a 12 bit e successiva conversione D/A]
</right>

* $\qty{4}{\bit}$ → $\num{16}$ valori possibili
* $\qty{12}{\bit}$ → $\num{4096}$ valori possibili
* Risoluzione maggiore → passi di quantizzazione più piccoli

<note>
Qui è possibile confrontare direttamente l'influenza della risoluzione.

Con 4 bit sono disponibili solo 16 valori possibili. La suddivisione è chiaramente visibile nel segnale ricostruito.

Con 12 bit sono già disponibili 4096 valori possibili. Il segnale ricostruito si avvicina quindi molto di più al segnale sinusoidale originale.

Con l'aggiunta di 8 bit, il numero di livelli possibili aumenta di un fattore 256.
</note>

---

[question:AF608]

---
## Jitter

* I campioni dovrebbero essere acquisiti in istanti temporali esattamente definiti
* In pratica, gli istanti di campionamento effettivi possono subire leggere fluttuazioni
* Queste deviazioni temporali vengono chiamate *jitter*
* Il jitter può causare rumore aggiuntivo nel segnale digitalizzato

<note>
Non è importante solo la precisione dell'ampiezza misurata, ma anche la precisione dell'istante di campionamento.

Per questo, il convertitore A/D necessita di un clock il più stabile possibile. Piccole fluttuazioni temporali di questo clock fanno sì che i campioni non vengano acquisiti esattamente negli istanti previsti.

Queste fluttuazioni vengono chiamate jitter.
</note>

---

[question:AF621]

---
## Convertitore D/A

* Il convertitore D/A è l'opposto del convertitore A/D
* Genera valori di tensione analogici a partire da campioni digitali
* Anche un convertitore D/A possiede solo un numero finito di valori di uscita possibili
* La sua risoluzione viene espressa anch'essa in bit

<note>
Nel convertitore D/A il processo avviene nella direzione opposta.

Un valore numerico digitale viene associato a un determinato valore di uscita analogico. Anche in questo caso, la risoluzione determina quanti valori diversi possono essere generati.
</note>

---

[question:AF609]

---
## Intervallo di tensione e risoluzione

* Un convertitore D/A possiede un intervallo di tensione fisso
* Esempio: $\qty{0}{\volt}$ a $\qty{1}{\volt}$
* Con $\qty{4}{\bit}$ sono disponibili $\num{2^4}=\num{16}$ livelli possibili
* In un convertitore D/A lineare, questi sono distribuiti uniformemente sull'intervallo di tensione

---
## Passo

Con $\num{16}$ livelli, ci sono $\num{15}$ intervalli tra i livelli.

Per un intervallo di tensione da $\qty{0}{\volt}$ a $\qty{1}{\volt}$ si ottiene:

$\frac{\qty{1}{\volt}}{16-1}\approx\qty{67}{\milli\volt}$

<fragment>
Il passo è quindi di circa $\qty{67}{\milli\volt}$.
</fragment>

<note>
Qui occorre considerare che tra 16 valori di tensione possibili ci sono solo 15 intervalli.

Questo corrisponde al noto problema della staccionata: tra 10 pali di una staccionata ci sono solo 9 spazi intermedi.

Per questo motivo, in questo esempio l'intervallo di tensione viene diviso per 15 e non per 16.
</note>

---

[question:AF611]

---

[question:AF610]

---
## Convertitori A/D e D/A in un SDR

* I convertitori A/D digitalizzano segnali di ingresso analogici
* Successivamente, i campioni possono essere elaborati digitalmente
* I convertitori D/A generano, se necessario, segnali analogici a partire da questi dati
* Questo principio viene utilizzato in molti punti nei ricevitori e nei transceiver SDR

<note>
Un SDR è un esempio tipico di interazione tra conversione A/D, elaborazione digitale del segnale e conversione D/A.

Il segnale analogico viene prima digitalizzato. Successivamente, ad esempio, possono essere eseguite digitalmente operazioni come filtraggio, demodulazione o modulazione. Se si desidera ottenere nuovamente un segnale analogico, si utilizza un convertitore D/A.
</note>

---
## Utilizzo dell'intervallo di valori

* Un segnale di ingresso piccolo utilizza solo una parte dei livelli disponibili
* Un segnale troppo grande supera l'intervallo di valori rappresentabile
* I valori superiori al massimo non possono più essere rappresentati correttamente
* Il segnale viene troncato in questo punto

<fragment>
Questo effetto viene chiamato *clipping*.
</fragment>

<note>
Per una digitalizzazione ottimale, l'intervallo di valori disponibile dovrebbe essere sfruttato in modo appropriato.

Se il segnale è molto piccolo, vengono utilizzati solo pochi dei livelli disponibili.

Se invece il segnale è troppo grande, il convertitore A/D raggiunge il suo valore massimo rappresentabile. Valori di ingresso ancora più grandi non possono più essere distinti. Le creste del segnale appaiono quindi troncate.

Anche un convertitore D/A non può generare una tensione di uscita al di fuori del suo intervallo di valori previsto.
</note>

---
## Influenza della risoluzione

* Alta risoluzione → molti valori di ampiezza possibili
* Bassa risoluzione → pochi valori di ampiezza possibili
* Più livelli consentono una digitalizzazione e una ricostruzione più precise
* L'intervallo di valori disponibile dovrebbe essere sfruttato al meglio

---

[question:AF613]

---

[question:AF612]

---

[question:AF614]