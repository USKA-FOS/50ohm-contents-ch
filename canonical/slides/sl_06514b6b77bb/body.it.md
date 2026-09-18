### Generazione

<left>
[picture:951:a_frequenzmodulation_schaltung:Modulatore per la generazione di FM]
</left>
<right>
* La capacità di un oscillatore viene modificata dal segnale BF
* Ad esempio con un diodo a capacità variabile
* La frequenza di modulazione determina la frequenza di variazione della portante ad alta frequenza
</right>
<note>
Verrà ripreso più avanti nel capitolo Trasmettitore
</note>

---
[question:AE303]
---
[question:AE301]
---
### Vulnerabilità ai disturbi

* Le informazioni da trasmettere sono contenute nella variazione del segnale
* Le fluttuazioni di ampiezza non hanno effetti
* Spesso viene utilizzato un amplificatore limitatore
* Insensibile ai disturbi impulsivi causati da scintille di accensione, motori elettrici o simili

---
[question:AE302]
---
### Deviazione

* Determina di quanto varia la frequenza dell'oscillatore in base all'ampiezza del segnale modulato
* Ampiezza maggiore nel segnale BF $\leftrightarrow$ maggiore escursione nella portante
* Maggiore deviazione $\rightarrow$ volume maggiore nel segnale demodulato

---
[question:AE305]
--- style="font-size: smaller;"
### Larghezza di banda

<left>
[picture:910:a_bandbreite_fm:Larghezza di banda in FM]
$BW \approx 2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}}\right)$
</left>
<right>
* Larghezza di banda occupata: deviazione e frequenza massima di modulazione
* Con deviazione ridotta e frequenza di modulazione bassa $\rightarrow$ *formula di Carson*
* Frequenza di modulazione più alta o deviazione maggiore $\rightarrow$ larghezza di banda maggiore
* Possibili interferenze con canali adiacenti
</right>

<note>
Circa il 99% della potenza di trasmissione si trova all'interno della larghezza di banda
</note>
---
[question:AE306]
---
[question:AE307]
---
[question:AE304]
---
[question:AE309]
---
#### Procedimento di soluzione
* dati: $f_{\textrm{mod max}} = \qty{2}{\kilo\hertz}$
* dati: $\Delta f_{\textrm{T}} = \qty{1,8}{\kilo\hertz}$
* richiesto: $BW$


<fragment>
$\begin{split} BW &\approx 2 \cdot (\Delta f_{\textrm{T}} + f_{\textrm{mod max}})\\ &= 2 \cdot (\qty{1,8}{\kilo\hertz} + \qty{2}{\kilo\hertz}) = \qty{7,6}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AE308]
---
#### Procedimento di soluzione
* dati: $f_{\textrm{mod max}} = \qty{2,7}{\kilo\hertz}$
* dati: $\Delta f_{\textrm{T}} = \qty{2,5}{\kilo\hertz}$
* richiesto: $BW$


<fragment>
$\begin{split} BW &\approx 2 \cdot (\Delta f_{\textrm{T}} + f_{\textrm{mod max}})\\ &= 2 \cdot (\qty{2,5}{\kilo\hertz} + \qty{2,7}{\kilo\hertz}) = \qty{10,4}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AE311]
---
#### Procedimento di soluzione
* dati: $BW = \qty{10}{\kilo\hertz}$
* dati: $\Delta f_{\textrm{T}} = \qty{2,5}{\kilo\hertz}$
* richiesto: $f_{\textrm{mod max}}$


<fragment>
$\begin{split} BW &\approx 2 \cdot (\Delta f_{\textrm{T}} + f_{\textrm{mod max}})\\ \Rightarrow f_{\textrm{mod max}} &= \frac{BW}{2} - \Delta f_T\\ &= \frac{\qty{10}{\kilo\hertz}}{2} - \qty{2,5}{\kilo\hertz} = \qty{2,5}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AE312]
---
#### Procedimento di soluzione
* dati: $BW = \qty{10}{\kilo\hertz}$
* dati: $f_{\textrm{mod max}} = \qty{2,7}{\kilo\hertz}$
* richiesto: $\Delta f_{\textrm{T}}$


<fragment>
$\begin{split} BW &\approx 2 \cdot (\Delta f_{\textrm{T}} + f_{\textrm{mod max}})\\ \Rightarrow \Delta f_T &= \frac{BW}{2} - f_{\textrm{mod max}}\\ &= \frac{\qty{10}{\kilo\hertz}}{2} - \qty{2,7}{\kilo\hertz} = \qty{2,3}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AE310]