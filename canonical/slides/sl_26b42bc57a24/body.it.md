---
## Dezibel spiegato in modo semplice

| l:Cosa | r:Potenza in $\unit{\milli\watt}$ |
| prestazione efficace stazione EME | 100 000 000 |
| trasmettitore-ricevitore standard | 100 000 |
| piccola radio portatile | 1 000 |
| segnale altoparlante (volume da stanza) | 100 |
| segnale cuffie | 1 |
| segnale forte onde corte | 0,000 001 |
| segnale debole onde corte (ingresso antenna RX) | 0,000 000 000 001 |
[table:e_dezibel_leistungen_mw:Potenze in $\unit{\milli\watt}$]

Chiunque abbia a che fare con questi numeri, inizia automaticamente a contare gli zeri.

---
Contiamo gli zeri (e chiamiamo il risultato "Bel")

| l:Cosa | r:Potenza in $\unit{\milli\watt}$ | r:Bel |
| prestazione efficace stazione EME | 100 000 000 | 8 |
| trasmettitore-ricevitore standard | 100 000 | 5 |
| piccola radio portatile | 1 000 | 3 |
| segnale altoparlante (volume da stanza) | 100 | 2 |
| segnale cuffie | 1 | 0 |
| segnale forte onde corte | 0,000 001 | -6 |
| segnale debole onde corte (ingresso antenna RX) | 0,000 000 000 001 | -12 |
[table:e_dezibel_leistungen_bel:Potenze in $\unit{\milli\watt}$ e Bel]

<note>
Secondo Alexander Graham Bell
</note>
---
$\unit{\dBm}$ = decibel riferiti a $\unit{\milli\watt}$

| l:Cosa | r:Potenza in $\unit{\milli\watt}$ | r:Bel | r:$\unit{\dBm}$ |
| prestazione efficace stazione EME | 100 000 000 | 8 | 80 |
| trasmettitore-ricevitore standard | 100 000 | 5 | 50 |
| piccola radio portatile | 1 000 | 3 | 30 |
| segnale altoparlante (volume da stanza) | 100 | 2 | 20 |
| segnale cuffie | 1 | 0 | 0 |
| segnale forte onde corte | 0,000 001 | -6 | -60 |
| segnale debole onde corte (ingresso antenna RX) | 0,000 000 000 001 | -12 | -120 |
[table:e_dezibel_leistungen_bel:Potenze in $\unit{\milli\watt}$ e Bel]

<note>
* Fattore 10
* deci come in decimetro
</note>
---
### Amplificazione di potenza

*Ricevitore*
* segnale di ingresso: $\qty{0,000000000001}{\milli\watt}$
* segnale di uscita: $\qty{100}{\milli\watt}$
* Amplificazione necessaria: $\num{100000000000000}$

*Trasmettitore*
* Stadio di generazione della frequenza (oscillatore): $\qty{10}{\milli\watt}$
* segnale di uscita: $\qty{100000}{\milli\watt}$
* Amplificazione necessaria: $\num{10000}$

---
### Amplificazione di potenza con dB
*Ricevitore*
* segnale di ingresso: $\qty{0,000000000001}{\milli\watt} = \qty{-120}{\dBm}$
* segnale di uscita: $\qty{100}{\milli\watt} = \qty{20}{\dBm}$
* Amplificazione necessaria: $\num{100000000000000} = \qty{140}{\dB}$

*Trasmettitore*
* Stadio di generazione della frequenza (oscillatore): $\qty{10}{\milli\watt} = \qty{10}{\dBm}$
* segnale di uscita: $\qty{100000}{\milli\watt} = \qty{50}{\dBm}$
* Amplificazione necessaria: $\num{10000} = \qty{40}{\dB}$

<note>
* La differenza è l'amplificazione
* L'amplificazione è un fattore e non è riferita al $\unit{mW}$, quindi solo $\unit{\dB}$
</note>

---
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
* Promemoria: 1,64 è il fattore tra un dipolo e un irradiatore isotropo sferico
</note>

---
### Calcolo con calcolatrice

Modelli più vecchi
* Valore fattore $\rightarrow$ tasto *log* $\rightarrow\times 10 \rightarrow\unit{\dB}$
* Valore $\unit{\dB}$ $\rightarrow\div 10 \rightarrow$ tasto *$10^x$* $\rightarrow$ Fattore

Modelli più recenti
* Tasto *$10^x$* $\rightarrow$ Valore $\unit{\dB}$ $\rightarrow \div 10 \rightarrow$ Tasto *=* $\rightarrow$ Fattore
* Tasto *log* $\rightarrow$ Valore fattore $\rightarrow$ Tasto *)* $\rightarrow\times 10 \rightarrow$ Tasto *=* $\rightarrow\unit{\dB}$

---
[question:EA107]