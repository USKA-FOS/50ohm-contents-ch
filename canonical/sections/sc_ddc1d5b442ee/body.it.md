La *precisione in frequenza* indica di quanto una frequenza generata, impostata o misurata può discostarsi dal suo valore effettivo. Viene spesso espressa in percentuale ($\unit{\percent}$), in *parti per milione* ($\unit{\ppm}$) o direttamente come scostamento relativo.

In questo caso vale:

$\qty{1}{\percent} = 1 \cdot 10^{-2}$

e

$\qty{1}{\ppm} = 1 \cdot 10^{-6}$

Per un frequenzimetro, la precisione raggiungibile dipende in modo significativo dalla sua *base temporale*. Il frequenzimetro determina la frequenza del segnale di ingresso tramite una frequenza di riferimento interna. Se questa frequenza di riferimento si discosta dal suo valore nominale, tale scostamento si ripercuote direttamente sul risultato della misurazione.

Per questo motivo, come base temporale vengono utilizzati oscillatori il più possibile stabili. Frequenzimetri di alta qualità impiegano, ad esempio, un TCXO o un OCXO. Per misurazioni particolarmente precise, è possibile collegare anche una frequenza di riferimento esterna, ad esempio un oscillatore sincronizzato con GPS (GPSDO).

Se è nota la precisione relativa in frequenza, è possibile calcolare la massima deviazione di frequenza attesa:

$\Delta f = f \cdot a$

In questa formula, $f$ rappresenta la frequenza considerata e $a$ la precisione relativa in frequenza.

<indepth>
  Nota sulla conversione/rappresentazione delle potenze in base 10:
  
  $1 \cdot {\num{10^{-2}}} = \frac{1}{\num{10^2}}$
  $1 \cdot {\num{10^{-6}}} = \frac{1}{\num{10^6}}$
  
  ecc.
</indepth>

[question:AA115]

[question:AA116]

[question:AI508]

[question:AI509]

[question:AI510]

[question:AI506]

[question:AI507]