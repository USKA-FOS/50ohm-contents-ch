Un amplificatore preleva dalla propria alimentazione elettrica una potenza in corrente continua e ne converte una parte in potenza d’uscita ad alta frequenza (cfr. figura [ref:a_wirkungsgrad_verstaerker]). Un’altra parte viene principalmente dissipata come calore nel transistor e in altri componenti. A ciò contribuisce in particolare la corrente di riposo, che fluisce anche in assenza di segnale d’ingresso, come approfondiremo nel capitolo successivo.

<margin>
[picture:1120:a_wirkungsgrad_verstaerker:Flusso di potenza di un amplificatore con potenza in corrente continua fornita, potenza d’uscita ad alta frequenza e potenza dissipata]
</margin>

Il *rendimento* $\eta$ indica quale frazione della potenza in corrente continua fornita è disponibile come potenza HF utile all’uscita dell’amplificatore:

$\eta = \frac{P_\mathrm{HF}}{P_\mathrm{DC}}$

In questa formula, $P_\mathrm{HF}$ rappresenta la potenza d’uscita ad alta frequenza e $P_\mathrm{DC}$ la potenza in corrente continua assorbita dall’alimentazione. Quest’ultima può essere calcolata dalla tensione di alimentazione e dalla corrente assorbita:

$P_\mathrm{DC} = U_\mathrm{B} \cdot I_\mathrm{B}$

Il rendimento è un rapporto adimensionale e può raggiungere al massimo il valore $\num{1}$. Spesso viene espresso in percentuale:

$\eta_\mathrm{\%} = \eta \cdot \qty{100}{\percent}$

Il rendimento di un amplificatore di potenza HF è quindi definito dal rapporto tra la potenza HF d’uscita fornita dall’amplificatore e la potenza in corrente continua assorbita dall’alimentazione.

[question:AF401]

Un rendimento elevato significa che solo una piccola parte della potenza assorbita viene persa come calore. Con un rendimento basso, invece, occorre dissipare una potenza dissipata maggiore tramite dissipatori termici o altre misure.

<tip>
Nelle domande d’esame seguenti, il rendimento viene considerato come rapporto tra la potenza HF d’uscita e la potenza in corrente continua assorbita. Eventuali valori aggiuntivi di potenza HF d’ingresso forniti non vengono presi in considerazione in questo calcolo semplificato.
</tip>

[question:AD430]
[question:AD429]