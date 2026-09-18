Nella classe N abbiamo già conosciuto l’*S-metro* sia nella sua versione analogica (fig. [ref:a_s_meter_analog]) che in quella digitale (fig. [ref:a_s_meter_digital]). Esso serve per visualizzare la forza del segnale HF presente all’**ingresso del ricevitore**.

La scala di un S-metro va solitamente da S1 a S9. Una variazione di una **livello S** corrisponde a $\qty{6}{\dB}$. Segnali più forti, superiori a S9, non vengono più indicati in ulteriori livelli S, ma in decibel sopra S9, ad esempio come „S9 + $\qty{20}{\dB}$“.

Poiché la scala in decibel è logaritmica, un **aumento** di $\qty{6}{\dB}$ corrisponde a un raddoppio della **tensione d’ingresso** o a un quadruplicamento della **potenza d’ingresso**. Viceversa, una **riduzione** di $\qty{6}{\dB}$ corrisponde a un dimezzamento della tensione o a un quarto della potenza.

<margin>
[picture:578:a_s_meter_digital:Il numero 2 mostra l’S-metro digitale di un ricetrasmettitore]
[picture:420:a_s_meter_analog:S-metro analogico di un ricetrasmettitore]
</margin>

[question:AF101]
[question:AF104]
[question:AF103]
[question:AA113]
[question:AF102]

---

Nel campo delle onde corte fino a $\qty{30}{\mega\hertz}$, un valore S9 corrisponde esattamente a $\qty{50}{\micro\volt}$ su $\qty{50}{\ohm}$.
A partire dalla banda VHF ($\qty{144}{\mega\hertz}$), un valore S9 corrisponde esattamente a $\qty{5}{\micro\volt}$ su $\qty{50}{\ohm}$.

<tip>
Gli S-metro dei dispositivi per onde corte mostrano valori affidabili solo intorno a S9, poiché spesso sono calibrati solo su questo valore. In particolare, i valori S più bassi vengono indicati in modo molto approssimativo. La caratteristica logaritmica di un S-metro viene spesso interpolata in modo insufficiente. Un valore S0 non esiste per definizione, poiché è sempre presente un rumore di fondo o un rumore proprio del ricevitore. Se l’S-metro non mostra alcun valore nella parte bassa della scala, il segnale ricevuto è molto debole, ma non raggiunge mai il valore S0. Pertanto, questo valore non dovrebbe essere trasmesso.
</tip>

[question:AA114]
[question:AF105]