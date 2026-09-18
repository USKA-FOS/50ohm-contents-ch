--- data-transition="none"
## Dal diodo al transistor
<left>
La funzione può essere immaginata così:
* Mediante un canale di controllo si regola il flusso di una diga
* Se non scorre acqua nel canale di controllo, la diga è chiusa
</left>
<right>
[picture:835:e_transistor_wehr_geschlossen:Steuerkanal schließt Wehr komplett]
</right>

--- data-transition="none"

## Dal diodo al transistor
<left>
La funzione può essere immaginata così:
* Se scorre un po' d'acqua nel canale di controllo, la diga si apre a metà
</left>
<right>
[picture:837:e_transistor_wehr_halb_offen:Steuerkanal öffnet Wehr halb]
</right>

--- data-transition="none"

## Dal diodo al transistor
<left>
La funzione può essere immaginata così:
* Se scorre più acqua nel canale di controllo, la diga si apre completamente
</left>
<right>
[picture:836:e_transistor_wehr_geoeffnet:Steuerkanal öffnet Wehr komplett]
</right>

---

[question:EC602]

---

[question:EC608]

---

### Transistor bipolare e schema di collegamento

<left>
Regola mnemonica per PNP → Freccia verso la piastra
</left>
<right>
[picture:374:e_schaltbild_npn_transistor:Schaltbild NPN-Transistor]
[picture:375:e_schaltbild_pnp_transistor:Schaltbild PNP-Transistor]
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
* Il pilotaggio può essere regolato in modo che il transistor blocchi o conduca completamente; in questo caso si parla di transistor come interruttore.
* Il pilotaggio può essere regolato in modo che il transistor sia controllato in modo continuo; in questo caso si parla di amplificatore.

---

[question:EC601]

---
[question:EC603]

---

## Tensione di pilotaggio e sua polarità
A seconda del tipo di transistor bipolare, si hanno diverse polarità.

* Per un transistor NPN è necessaria una tensione di controllo positiva per la conduzione.
* Per un transistor PNP è necessaria una tensione di controllo negativa per la conduzione.

La tensione di controllo, come per un diodo al silicio, è di circa $\qty{0,6}{\volt}$.

---

[question:EC610]

---

Poiché oltre alla corrente di collettore anche la corrente di base fluisce attraverso il transistor, la corrente maggiore passa attraverso il terminale dell'emettitore.

---

[question:EC611]

--- style="font-size: smaller;"

### Quando conduce il transistor NPN?
La tensione base-emettitore è sufficiente e si trova a un potenziale positivo?
Qui occorre prestare attenzione ai segni e reinterpretare in caso di valori negativi, esempi:

* Base $\qty{+2}{\volt}$ e emettitore $\qty{+1,4}{\volt} \rightarrow$ La tensione base-emettitore è positiva e ammonta a $\qty{+0,6}{\volt}$
* Base $\qty{-5,6}{\volt}$ e emettitore $\qty{-6,2}{\volt} \rightarrow$ La tensione base-emettitore è positiva e ammonta a $\qty{+0,6}{\volt}$

---

Lo si può intuire o calcolare (tenendo conto dei segni).

$U_{ BE } = U_{ B } - U_{ E }$

---

[question:EC612]

---

[question:EC613]

--- style="font-size: smaller;"

### Quando conduce il transistor PNP?
La tensione base-emettitore è sufficiente e si trova a un potenziale negativo?
Qui occorre prestare attenzione ai segni e reinterpretare in caso di valori negativi, esempi:

* Base $\qty{+5,6}{\volt}$ e emettitore $\qty{+6,2}{\volt} \rightarrow$ La tensione base-emettitore è negativa e ammonta a $\qty{-0,6}{\volt}$
* Base $\qty{-2}{\volt}$ e emettitore $\qty{-1,4}{\volt} \rightarrow$ La tensione base-emettitore è negativa e ammonta a $\qty{-0,6}{\volt}$

---

Lo si può intuire o calcolare (tenendo conto dei segni).

$U_{ BE } = U_{ B } - U_{ E }$

---

[question:EC614]

---

[question:EC615]

---

## Tipi di transistor
I transistor finora trattati vengono chiamati *transistor bipolari*. Sono il tipo di transistor che negli anni '50 hanno avviato una rivoluzione tecnica e hanno sostituito il tubo elettronico. Al contrario dei transistor bipolari controllati in corrente, i *transistor a effetto di campo (FET)* sono controllati in tensione, quindi non vi scorre alcuna corrente di controllo al loro interno. Di questi ci occuperemo in modo approfondito nel corso di classe A.

---

[question:EC604]