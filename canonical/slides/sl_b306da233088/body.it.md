---
## Dalla Diode al Transistor
<left>
La Funzione si può immaginare così:
* Tramite un canale di controllo si regola il flusso di una diga
* Se non scorre acqua nel canale di controllo, la diga è chiusa
</left>
<right>
[picture:835:e_transistor_wehr_geschlossen:Canale di controllo chiude completamente la diga]
</right>

---

## Dalla Diode al Transistor
<left>
La Funzione si può immaginare così:
* Se scorre un po' d'acqua nel canale di controllo, la diga si apre a metà
</left>
<right>
[picture:837:e_transistor_wehr_halb_offen:Il canale di controllo apre la diga a metà]
</right>

---

## Dalla Diode al Transistor
<left>
La Funzione si può immaginare così:
* Se scorre più acqua nel canale di controllo, la diga è completamente aperta
</left>
<right>
[picture:836:e_transistor_wehr_geoeffnet:Il canale di controllo apre completamente la diga]
</right>

---

[question:EC602]

---

[question:EC608]

---

### Transistor bipolare e schema circuitale

<left>
Regola mnemonica per PNP $\rightarrow$ Pfeil Nach Platte (Freccia verso la piastra)
</left>
<right>
[picture:374:e_schaltbild_npn_transistor:Schema NPN transistor]
[picture:375:e_schaltbild_pnp_transistor:Schema PNP transistor]
</right>

---

[question:EC607]

---

[question:EC606]

---

[question:EC605]

---

[question:EC609]

---

### Interruttore o amplificatore?
* L'azionamento può essere impostato in modo che il transistor blocchi o conduca completamente, allora si parla di un transistor di commutazione.
* L'azionamento può essere impostato in modo che il transistor venga controllato in modo continuo, allora si parla di un amplificatore.

---

[question:EC601]

---
[question:EC603]

---

## Tensione di pilotaggio e sua polarità
A seconda del tipo di transistor bipolare si hanno polarità diverse.

* In un transistor NPN è necessaria una Tensione di pilotaggio positiva per la conduzione.
* In un transistor PNP è necessaria una Tensione di pilotaggio negativa per la conduzione.

La Tensione di pilotaggio è, come per una Diode al silicio, di circa $\qty{0,6}{\volt}$.

---

[question:EC610]

---

Poiché oltre alla Corrente del collettore scorre anche la Corrente di base attraverso il transistor, la Corrente maggiore scorre attraverso il terminale dell'emettitore.

---

[question:EC611]

--- style="font-size: smaller;"

### Quando conduce il transistor NPN?
La tensione Base-Emettitore è sufficiente e si trova in potenziale positivo?
Qui bisogna prestare attenzione ai segni e, in caso di segni negativi, ripensare, esempi:

* Base $\qty{+2}{\volt}$ ed Emettitore $\qty{+1,4}{\volt} \rightarrow$ La tensione Base-Emettitore è positiva e ammonta a $\qty{+0,6}{\volt}$
* Base $\qty{-5,6}{\volt}$ ed Emettitore $\qty{-6,2}{\volt} \rightarrow$ La tensione Base-Emettitore è positiva e ammonta a $\qty{+0,6}{\volt}$

---

O si riconosce intuitivamente o si calcola (tenendo conto dei segni).

$U_{ BE } = U_{ B } - U_{ E }$

---

[question:EC612]

---

[question:EC613]

--- style="font-size: smaller;"

### Quando conduce il transistor PNP?
La tensione Base-Emettitore è sufficiente e si trova in potenziale negativo?
Qui bisogna prestare attenzione ai segni e, in caso di segni negativi, ripensare, esempi:

* Base $\qty{+5,6}{\volt}$ ed Emettitore $\qty{+6,2}{\volt} \rightarrow$ La tensione Base-Emettitore è negativa e ammonta a $\qty{-0,6}{\volt}$
* Base $\qty{-2}{\volt}$ ed Emettitore $\qty{-1,4}{\volt} \rightarrow$ La tensione Base-Emettitore è negativa e ammonta a $\qty{-0,6}{\volt}$

---

O si riconosce intuitivamente o si calcola (tenendo conto dei segni).

$U_{ BE } = U_{ B } - U_{ E }$

---

[question:EC614]

---

[question:EC615]

---

## Tipi di transistor
I transistor finora trattati si chiamano *transistor bipolari*. Sono il tipo di transistor che negli anni '50 ha inaugurato una rivoluzione tecnica e ha sostituito la valvola termoionica. A differenza dei transistor bipolari a corrente controllata, i *transistor a effetto di campo (FET)* sono a tensione controllata, quindi nessuna corrente di pilotaggio scorre al loro interno. Con questi ci confronteremo più intensamente nel corso di Classe A.

---

[question:EC604]