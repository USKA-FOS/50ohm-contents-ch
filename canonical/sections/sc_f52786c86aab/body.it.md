Abbiamo ora conosciuto la resistenza e la sua unità $\unit{\ohm}$ (Ohm). In pratica, sui resistori non è quasi mai stampato il valore numerico. Vengono invece utilizzati anelli colorati. Questi anelli colorati codificano il valore della resistenza.

<margin>
[picture:665:n_widerstandsfarbcodes: Un resistore con 4 anelli colorati]
</margin>

L'immagine [ref:n_widerstandsfarbcodes] mostra un resistore con quattro anelli colorati. Ogni colore corrisponde a un valore numerico, come mostrato nella tabella [ref:n_widerstandsfarbcodes_tabelle] nella colonna *Valore*:
* Il primo anello colorato corrisponde alla prima cifra, in questo caso *giallo*, quindi quattro.
* Il secondo anello colorato corrisponde alla seconda cifra, nel nostro esempio quindi *viola*, quindi sette.
* Il terzo anello colorato è il cosiddetto Moltiplicatore (vedi tabella [ref:n_widerstandsfarbcodes_tabelle], nel nostro caso *arancione*, quindi il valore 1000.

<webmargin>
| X:Colore | l:Valore | l:Moltiplicatore | l:Tolleranza |
| Argento | - | $\num{0,01}$ | $\qty{\pm 10}{\percent}$ |
| Oro | - | $\num{0,1}$ | $\qty{\pm 5}{\percent}$ |
| Nero | 0 | $\num{1}$ | - |
| Marrone | 1 | $\num{10}$ | $\qty{\pm 1}{\percent}$ |
| Rosso | 2 | $\num{100}$ | $\qty{\pm 2}{\percent}$ |
| Arancione| 3 | $\num{1000}$ | - |
| Giallo | 4 | $\num{10000}$ | - |
| Verde | 5 | $\num{100000}$ | - |
| Blu | 6 | $\num{1000000}$ | $\qty{\pm 0,25}{\percent}$ |
| Viola | 7 | $\num{10000000}$ | $\qty{\pm 0,1}{\percent}$ |
| Grigio | 8 | $\num{100000000}$ | - |
| Bianco | 9 | $\num{1000000000}$ | - |
| Nessuno | - | - | $\qty{\pm 20}{\percent}$ |
[table:n_widerstandsfarbcodes_tabelle:Tabella codici colore resistori]
</webmargin>

Il primo e il secondo anello insieme formano il numero 47. Moltiplicando questo numero per il Moltiplicatore, si può calcolare il valore del resistore:

$ 47 \cdot \qty{1000}{\ohm} = \qty{47000}{\ohm} = \qty{47}{\kilo\ohm} $

---

Rimane un quarto anello colorato. Questo indica la cosiddetta Tolleranza, che specifica quanto il valore effettivo della resistenza può deviare dal valore indicato.
Ulteriori dettagli seguiranno nella classe E.

<indepth>
*Approfondimento:* Nel nostro esempio, l'ultimo anello è *argento*, il che significa una Tolleranza del $\qty{\pm 10}{\percent}$. Il valore reale del resistore può essere $\qty{10}{\percent} \cdot \qty{47}{\kilo\ohm} = \qty{4,7}{\kilo\ohm}$ in più o in meno rispetto al valore indicato. Può quindi variare tra $\qty{42,3}{\kilo\ohm}$ e $\qty{51,7}{\kilo\ohm}$.
</indepth>

---

La tabella con i codici colore non deve essere imparata a memoria. È disponibile come parte della raccolta di formule come ausilio durante l'esame. Tuttavia, si dovrebbe memorizzare la disposizione degli anelli e il loro significato. Per esercitarsi, le seguenti domande possono essere risolte utilizzando il codice colore per acquisire familiarità.

<indepth>
*Approfondimento:* Esistono anche resistori con più di quattro anelli colorati. Tuttavia, questi non sono rilevanti per l'esame. Anche altri componenti sono spesso contrassegnati con anelli colorati.
</indepth>

[question:NC107]
[question:NC105]
[question:NC106]
[question:NC104]
[question:NC103]
[question:NC102]
[question:NC108]
[question:NC109]
[question:NC110]
