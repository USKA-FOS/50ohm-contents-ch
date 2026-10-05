Nella sezione [sec:rst] abbiamo già conosciuto l'*S-metro* sia nella sua variante analogica (Fig. [ref:a_s_meter_analog]) che in quella digitale (Fig. [ref:a_s_meter_digital]). Serve a visualizzare l'intensità del segnale HF presente all'ingresso del ricevitore.

La scala di un S-metro di solito va da S1 a S9. Una variazione di un livello S corrisponde a $\qty{6}{\dB}$. Segnali più forti al di sopra di S9 non sono più indicati in ulteriori livelli S, ma in decibel sopra S9, ad esempio come "S9 + $\qty{20}{\dB}$".

Poiché la scala in decibel è logaritmica, un aumento di $\qty{6}{\dB}$ corrisponde a un raddoppio della tensione d'ingresso o a una quadruplicazione della potenza d'ingresso. Al contrario, una riduzione di $\qty{6}{\dB}$ corrisponde a un dimezzamento della tensione o a un quarto della potenza.

<margin>
[picture:578:a_s_meter_digital:Il numero 2 mostra l'S-metro digitale di un TRX]
[picture:420:a_s_meter_analog:S-metro analogico di un TRX]
</margin>

[question:AF101]
[question:AF104]
[question:AF103]
[question:AA113]
[question:AF102]

---

Nella gamma delle onde corte fino a $\qty{30}{\mega\hertz}$, un valore S di S9 corrisponde esattamente a $\qty{50}{\micro\volt}$ su $\qty{50}{\ohm}$.
A partire dalla gamma VHF ($\qty{144}{\mega\hertz}$), un valore S di S9 corrisponde esattamente a $\qty{5}{\micro\volt}$ su $\qty{50}{\ohm}$.

<tip>
Gli S-metri dei dispositivi in onde corte di solito mostrano valori intorno a S9 in modo abbastanza affidabile, poiché spesso sono calibrati solo su questo singolo valore. In particolare, i valori S più piccoli vengono visualizzati in modo molto impreciso. La caratteristica logaritmica di un S-metro viene spesso interpolata in modo insufficiente. Per definizione, non esiste un valore S di S0, poiché è sempre presente un rumore di fondo o rumore proprio del ricevitore. Se l'S-metro non mostra alcun valore nella parte inferiore, il segnale ricevuto è molto debole, ma non ha mai il valore S0. Questo valore non dovrebbe quindi essere trasmesso.
</tip>

[question:AA114]
[question:AF105]
