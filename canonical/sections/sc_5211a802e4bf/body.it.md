Il rapporto segnale / rumore (SNR) è definito come il rapporto tra il segnale utile e il segnale di rumore (noise), come mostrato nella figura [ref:a_snr]. Più alto è l'SNR di un segnale ricevuto, più il segnale utile si distingue dal rumore per una data larghezza di banda.

<margin>
[picture:1097:a_snr:Signal-to-Noise Ratio (SNR)]
</margin>

[question:AF227]

Il fattore di rumore è spesso specificato per i preamplificatori RF. Questo descrive il deterioramento dell'SNR quando un segnale attraversa questo componente. Qui, il fattore di rumore è determinato come il rapporto tra il valore SNR in ingresso e il valore SNR in uscita. Il fattore di rumore è solitamente espresso in decibel ($\unit{\dB}$) tramite logaritmo. Un fattore di rumore di $\num{2}$ in notazione lineare corrisponde a $\qty{3}{\dB}$ in rappresentazione logaritmica.

[question:AF228]
[question:AF229]

<indepth>
Secondo la norma DIN, il fattore di rumore espresso in $\unit{\decibel}$ è chiamato misura di rumore. Purtroppo esiste un'altra definizione della misura di rumore, quindi questa denominazione non è molto diffusa.
</indepth>

<indepth>
Il *fattore di rumore* descrive quanto un componente elettronico o uno stadio amplificatore deteriora il rapporto segnale / rumore di un segnale.

Un amplificatore dovrebbe amplificare un segnale debole. Tuttavia, nell'amplificatore stesso si genera ulteriore rumore.

Si confronta quindi

- il rapporto segnale / rumore all'ingresso con il

- rapporto segnale / rumore all'uscita.

Il fattore di rumore $F$ è definito come

$F = \frac{(S/N)_\mathrm{Eingang}}{(S/N)_\mathrm{Ausgang}}$

Dove:

- $S$ = potenza del segnale
- $N$ = potenza di rumore
- $F$ = fattore di rumore come grandezza adimensionale

*Fattore di rumore in decibel*

Il fattore di rumore (noise figure, NF) è molto spesso espresso in modo logaritmico in decibel:

$NF = 10 \cdot \log_{10}(F)\;\mathrm{dB}$
</indepth>
