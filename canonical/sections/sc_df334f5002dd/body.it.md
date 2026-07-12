I componenti SMD sono grandi solo pochi millimetri. SMD sta per Surface-Mounted Device (in tedesco: componente montato in superficie). A differenza dei componenti classici, non hanno connessioni a filo, ma vengono saldati direttamente sulla scheda a circuito stampato, senza alcuna foratura passante. Di seguito, ci occuperemo della marcatura delle resistenze SMD.

<margin>
[photo:318:e_platine_smd:Scheda a circuito stampato con componenti SMD]
</margin>

---

La figura [ref:e_smd] mostra una resistenza SMD. Per indicare il valore della resistenza, sono stampate delle cifre – in questo caso le cifre 113. La grandezza della resistenza si ottiene quindi come segue: Tutte le cifre tranne l'*ultima* vengono prese come puro valore numerico. Nell'esempio 113, si ottiene quindi *11* come valore numerico. L'*ultima* cifra indica la *potenza di dieci* per cui le altre cifre devono essere moltiplicate. Un 1 sta per la prima potenza di dieci $10^1$, un 2 per la seconda potenza di dieci $10^2$, ecc.

<margin>
[picture:1006:e_smd:Componente SMD]
</margin>

Nel nostro esempio, otteniamo quindi: $11 \cdot 10^3$ ovvero $\qty{11000}{\ohm}$ Ohm o $\qty{11}{\kilo\ohm}$.

[question:EC114]
[question:EC115]
[question:EC116]
[question:EC117]