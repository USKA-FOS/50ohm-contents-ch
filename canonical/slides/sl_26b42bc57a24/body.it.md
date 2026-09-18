--- style="font-size: 0.7em;"
## Decibel spiegato semplicemente

| l:Cosa | r:Potenza in $\unit{\milli\watt}$ |
| potenza effettiva stazione EME | 100 000 000 | 
| trasmettitore-ricevitore standard | 100 000 |
| piccola radio portatile | 1 000 |
| segnale altoparlante (volume ambiente) | 100 |
| segnale cuffie | 1 |
| segnale forte OC | 0,000 001 |
| segnale debole OC (ingresso antenna RX) | 0,000 000 000 001 |
[table:e_dezibel_leistungen_mw:Potenze in $\unit{\milli\watt}$]

Chi lavora con questi numeri inizia automaticamente a contare gli zeri.

--- style="font-size: 0.7em;"
Contiamo gli zeri (e chiamiamo il risultato "Bel")

| l:Cosa | r:Potenza in $\unit{\milli\watt}$ | r:Bel |
| potenza effettiva stazione EME | 100 000 000 | 8 |
| trasmettitore-ricevitore standard | 100 000 | 5 |
| piccola radio portatile | 1 000 | 3 |
| segnale altoparlante (volume ambiente) | 100 | 2 |
| segnale cuffie | 1 | 0 |
| segnale forte OC | 0,000 001 | -6 |
| segnale debole OC (ingresso antenna RX) | 0,000 000 000 001 | -12 |
[table:e_dezibel_leistungen_bel:Potenze in $\unit{\milli\watt}$ e Bel]

<note>
In onore di Alexander Graham Bell
</note>
--- style="font-size: 0.7em;"
$\unit{\dBm}$ = Decibel riferiti a $\unit{\milli\watt}$

| l:Cosa | r:Potenza in $\unit{\milli\watt}$ | r:Bel | r:$\unit{\dBm}$ |
| potenza effettiva stazione EME | 100 000 000 | 8 | 80 |
| trasmettitore-ricevitore standard | 100 000 | 5 | 50 |
| piccola radio portatile | 1 000 | 3 | 30 |
| segnale altoparlante (volume ambiente) | 100 | 2 | 20 |
| segnale cuffie | 1 | 0 | 0 |
| segnale forte OC | 0,000 001 | -6 | -60 |
| segnale debole OC (ingresso antenna RX) | 0,000 000 000 001 | -12 | -120 |
[table:e_dezibel_leistungen_bel:Potenze in $\unit{\milli\watt}$ e Bel]

<note>
* Fattore 10
* "deci" come in decimetro
</note>
---
### Guadagno di potenza

*Ricevitore*
* Segnale di ingresso: $\qty{0,000000000001}{\milli\watt}$
* Segnale di uscita: $\qty{100}{\milli\watt}$
* Guadagno richiesto: $\num{100000000000000}$
 
*Trasmettitore*
* Stadio generatore di frequenza (oscillatore): $\qty{10}{\milli\watt}$
* Segnale di uscita: $\qty{100000}{\milli\watt}$
* Guadagno richiesto: $\num{10000}$
 
---
### Guadagno di potenza con dB
*Ricevitore*
* Segnale di ingresso: $\qty{0,000000000001}{\milli\watt} = \qty{-120}{\dBm}$
* Segnale di uscita: $\qty{100}{\milli\watt} = \qty{20}{\dBm}$
* Guadagno richiesto: $\num{100000000000000} = \qty{140}{\dB}$
 
*Trasmettitore*
* Stadio generatore di frequenza (oscillatore): $\qty{10}{\milli\watt} = \qty{10}{\dBm}$
* Segnale di uscita: $\qty{100000}{\milli\watt} = \qty{50}{\dBm}$
* Guadagno richiesto: $\num{10000} = \qty{40}{\dB}$

<note>
* La differenza è il guadagno
* Il guadagno è un fattore e non riferito a $\unit{\milli\watt}$, per questo solo $\unit{\dB}$
</note>

--- style="font-size: 0.7em;"
## Fattori di potenza importanti

| c:$\unit{dB}$ | c:≈ Fattore di potenza |
| $0$ | $1$ |
| $1,5$ | $\sqrt{2} = 1,41$ |
| $2,15$ | $1,64$ |
| $3$ | $2$ |
| $5$ | $\sqrt{10} = 3,16$ |
| $6$ | $4$ |
| $10$ | $10$ |
| $20$ | $100$ |
[table:e_dezibel_leistungsfaktoren:Fattori di potenza importanti in $\unit{\dB}$]

<note>
* Ricordo: 1,64 è il fattore tra dipolo e radiatore sferico isotropo
</note>

---
### Calcolo con la calcolatrice

Modelli più vecchi
* Valore del fattore $\rightarrow$ tasto *log* $\rightarrow\times 10 \rightarrow\unit{\dB}$
* Valore in $\unit{\dB}$ $\rightarrow\div 10 \rightarrow$ tasto *$10^x$* $\rightarrow$ Fattore

Modelli più recenti
* tasto *log* $\rightarrow$ Valore del fattore $\rightarrow$ tasto *)* $\rightarrow\times 10 \rightarrow$ tasto *=* $\rightarrow\unit{\dB}$
* tasto *$10^x$* $\rightarrow$ Valore in $\unit{\dB}$ $\rightarrow \div 10 \rightarrow$ tasto *=* $\rightarrow$ Fattore

---
[question:EA107]