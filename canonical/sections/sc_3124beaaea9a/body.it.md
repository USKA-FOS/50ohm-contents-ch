Il controllo automatico del guadagno *(Automatic Gain Control, abbreviato AGC)* nei ricevitore garantisce che il segnale di uscita in BF (volume di ricezione) rimanga quasi costante anche in presenza di un segnale di ingresso RF variabile all’ingresso del ricevitore (ad esempio a causa di fading), riducendo così le fluttuazioni del volume. A tal fine, il livello di ricezione all’uscita del ramo ricevente viene rilevato e il guadagno RF viene regolato di conseguenza, influenzando così il volume di ricezione dopo la demodulazione. È importante non confondere l’AGC con l’ALC (Automatic Level Control), che si trova invece nel ramo di trasmissione.

<margin>
[picture:1055:e_agc:AGC nel ricevitore supereterodina]
</margin>

---

A seconda dell’apparecchiatura del ricevitore, l’AGC può essere regolata in base al suo comportamento di risposta (tempo di attivazione, tempo di decadimento). Le denominazioni usuali sono AGC Slow, AGC Normal e AGC Fast, che descrivono il comportamento temporale di risposta. Normalmente, la configurazione AGC Slow o Normal è adatta per l’uso in SSB. Per la telegrafia (CW), di solito è consigliabile la configurazione AGC Fast o Normal, in modo che i segnali forti non coprano quelli deboli e la regolazione segua rapidamente. Per i modi di trasmissione digitali, può essere utile disattivare l’AGC.

[question:EF211]
[question:EF212]

<tip>
In alcuni ricevitore, l’AGC può essere completamente disattivata. In questo caso, è possibile controllare manualmente il guadagno RF, ad esempio agendo sul regolatore RF-Gain. Tuttavia, questa modalità è utile solo per applicazioni particolari (ad esempio, per evitare la sovraeccitazione della parte di ingresso RF a causa di segnali forti) e, eventualmente, per i modi di trasmissione digitali.
</tip>