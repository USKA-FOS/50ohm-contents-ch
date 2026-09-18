* Una delle più importanti configurazioni nel radioamatoriale
* Generazione di oscillazioni ad alta frequenza in trasmettitori e ricevitori
* Cuore di ogni apparecchio radio

---
### Guadagno d’anello

* Elemento di amplificazione il cui segnale di uscita viene reimmesso all’ingresso
* In fase
* Ampiezza almeno uguale $\rightarrow$ *guadagno d’anello maggiore di $1$*
* Necessario per l’autoeccitazione e mantiene l’oscillazione

---
[question:AD613]
---
<left>
[picture:760:a_oszillator_schaltungen_oszillator:Circuito di un oscillatore a tre punti con reazione capacitiva]
</left>
<right>
* Il segnale di uscita viene reimmesso alla base tramite un partitore di tensione capacitivo
* La frequenza è determinata dal circuito oscillante alla base e dal partitore di tensione capacitivo in parallelo
* Oscillatore in circuito a collettore comune
</right>
<note>
I circuiti a transistor verranno trattati più avanti nel capitolo
</note>

---
[question:AD614]
---
[question:AD616]
---
<left>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Circuito di un oscillatore al quarzo in configurazione a collettore comune con funzionamento del quarzo alla frequenza fondamentale]
</left>
<right>
* Il circuito oscillante è sostituito dal quarzo
* Il quarzo può oscillare alla frequenza fondamentale o su armoniche $\rightarrow$ l’amplificatore deve essere progettato in modo selettivo in frequenza, ad esempio con un circuito oscillante
</right>
<note>
In questo caso non è presente un ulteriore circuito oscillante, quindi il quarzo funziona alla frequenza fondamentale
</note>

---
[question:AD617]
---
### Estrazione del segnale

* Sempre nel punto a impedenza più bassa di un oscillatore
* In questo modo l’oscillatore è poco caricato
* In configurazione a collettore comune, all’emettitore del transistor

---
### Stadio buffer

* Inserire uno stadio buffer
* Decoupla l’oscillatore dagli altri componenti del circuito
* La frequenza non viene influenzata dal carico dell’uscita
* Lo stadio buffer è spesso un circuito a collettore comune (come inseguitore di emettitore) e presenta un’elevata impedenza di ingresso

---
[question:AD610]
---
[question:AD615]
---
### Misurazione

* La misurazione dovrebbe essere effettuata dopo lo stadio buffer
* Altrimenti l’oscillatore viene caricato dalle capacità parassite
* La frequenza ne risulta influenzata

---
[question:AD619]
---
[question:AD618]