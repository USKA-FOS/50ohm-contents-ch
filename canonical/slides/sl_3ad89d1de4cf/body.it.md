* Uno dei circuiti più importanti nel radioamatore
* Generazione di oscillazioni ad alta frequenza nei trasmettitori e ricevitori
* Cuore di ogni apparecchio radio

---
### Guadagno d'anello

* Elemento amplificatore il cui segnale di uscita viene retroazionato all'ingresso
* In fase
* Ampiezza almeno uguale $\rightarrow$ *guadagno d'anello maggiore di $1$*
* Necessario per l'auto-eccitazione e mantiene l'oscillazione

---
[question:AD613]
---
<left>
[picture:760:a_oszillator_schaltungen_oszillator:Circuito di un oscillatore a tre punti con retroazione capacitiva]
</left>
<right>
* Il segnale di uscita viene retroazionato alla base dall'emettitore tramite un partitore di tensione capacitivo
* La frequenza è determinata dal circuito oscillante nella base e dal partitore di tensione capacitivo collegato in parallelo
* Oscillatore in configurazione collettore
</right>
<note>
Le configurazioni dei transistor verranno trattate più avanti nel capitolo
</note>

---
[question:AD614]
---
[question:AD616]
---
<left>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Circuito di un oscillatore a quarzo in configurazione collettore con funzionamento del quarzo sulla frequenza fondamentale]
</left>
<right>
* Il circuito oscillante è sostituito da un quarzo
* Il quarzo può oscillare sulla frequenza fondamentale o sulle armoniche $\rightarrow$ l'amplificatore deve essere progettato per essere selettivo in frequenza, ad esempio con un circuito oscillante
</right>
<note>
Qui non è presente un ulteriore circuito oscillante, quindi il quarzo viene utilizzato sulla frequenza fondamentale
</note>

---
[question:AD617]
---
### Estrazione del segnale

* Sempre nel punto a più bassa impedenza di un oscillatore
* In questo modo, l'oscillatore viene poco caricato
* Nella configurazione collettore, sull'emettitore del transistor

---
### Stadio buffer

* Collegare uno stadio buffer
* Disaccoppia l'oscillatore da altre parti del circuito
* La frequenza non viene influenzata dal carico dell'uscita
* Lo stadio buffer è spesso una configurazione collettore (come inseguitore di emettitore) e ha un'alta impedenza di ingresso

---
[question:AD610]
---
[question:AD615]
---
### Misurazione

* Una misurazione dovrebbe essere eseguita dopo lo stadio buffer
* Altrimenti, l'oscillatore viene caricato dalle capacità parassite
* La frequenza viene influenzata da ciò

---
[question:AD619]
---
[question:AD618]
