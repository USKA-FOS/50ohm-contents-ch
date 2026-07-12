Il controllo automatico del guadagno (AGC - Automatic-Gain-Control) nei ricevitori assicura che il segnale di uscita in bassa frequenza (volume di ricezione) rimanga quasi costante anche con segnali di ingresso RF fluttuanti al ricevitore (ad esempio, a causa del fading), riducendo le fluttuazioni del volume. Il livello di ricezione viene rilevato all'uscita del ramo del ricevitore e il guadagno RF viene regolato di conseguenza, in modo che il volume di ricezione dopo la demodulazione possa essere influenzato. L'AGC non deve essere confuso con l'ALC (Automatic-Level-Control), che si trova nel ramo di trasmissione.

<margin>
[picture:1055:e_agc:AGC in un ricevitore supereterodina]
</margin>

---

L'AGC può essere regolato, a seconda dell'equipaggiamento del ricevitore, per quanto riguarda il suo comportamento di risposta (tempo di attacco, tempo di decadimento). Denominazioni comuni per questo sono AGC Slow, AGC Normal, AGC Fast, che descrivono il comportamento di risposta temporale. L'impostazione AGC-Slow o Normal è normalmente sensata per il funzionamento SSB. Per il funzionamento in telegrafia (CW), l'impostazione AGC-Fast o Normal è normalmente sensata, in modo che i segnali forti non possano coprire i segnali deboli e la regolazione si adegui rapidamente. Per i metodi di trasmissione digitale, potrebbe essere sensato disattivare l'AGC.

[question:EF211]
[question:EF212]

<tip>
In alcuni ricevitori, l'AGC può anche essere completamente disattivato. In tal caso, è possibile controllare il guadagno RF, ad esempio, manualmente modificando la manopola RF-Gain. Tuttavia, ciò è sensato solo per applicazioni speciali (ad esempio, sovraeccitazione della sezione di ingresso RF a causa di segnali forti), nonché eventualmente per metodi di trasmissione digitale.
</tip>