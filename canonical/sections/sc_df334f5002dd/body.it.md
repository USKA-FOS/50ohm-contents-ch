I componenti SMD sono grandi solo pochi millimetri. SMD sta per Surface-Mounted Device (in tedesco: componente montato in superficie). A differenza dei componenti classici, non hanno terminali filiformi, ma vengono saldati direttamente sulla scheda a circuito stampato, senza necessità di fori di passaggio. Di seguito ci occupiamo della marcatura dei resistori SMD.

<margin>
[photo:318:e_platine_smd:Scheda con componenti SMD]
</margin>

---

La figura [ref:e_smd] mostra un resistore SMD. Per la marcatura del valore di resistenza sono stampate delle cifre – in questo caso le cifre 113. Il valore della resistenza si ricava come segue: tutte le cifre tranne l’*ultima* vengono prese come valore numerico puro. Nell’esempio 113, quindi, si ottiene *11* come valore numerico. L’*ultima* cifra indica la *potenza di dieci* con cui moltiplicare le altre cifre. Una 1 corrisponde alla prima potenza di dieci $10^1$, una 2 alla seconda potenza di dieci $10^2$ e così via.

<margin>
[picture:1006:e_smd:Componente SMD]
</margin>

Nel nostro esempio otteniamo quindi: $11 \cdot 10^3$ cioè $\qty{11000}{\ohm}$ o $\qty{11}{\kilo\ohm}$.

[question:EC114]
[question:EC115]
[question:EC116]
[question:EC117]