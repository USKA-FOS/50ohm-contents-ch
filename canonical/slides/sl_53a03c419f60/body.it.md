## Funzionamento remoto di stazioni radio

* Composto da diversi blocchi funzionali
* Gli apparecchi moderni integrano talvolta più blocchi
* Separazione tra operatore e stazione remota

---

### Schema a blocchi di una stazione remota

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Rappresentazione logica dei blocchi funzionali
* Controllo, connessione di rete, interfaccia remota
* Trasmettitore-ricevitore e apparecchiature collegate
</right>

---

#### Computer e pannello di controllo dell’operatore (Blocco 1)

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Converte i segnali audio e di comando in pacchetti di rete
* I segnali ricevuti vengono resi udibili e visibili
</right>

---

#### Rete

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Collega l’operatore alla stazione remota
* Possibile utilizzo di Internet
</right>

---

#### Interfaccia remota presso la stazione remota (Blocco 2)

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Converte i pacchetti di rete in segnali di comando e audio
* Trasmette i segnali audio ricevuti all’operatore
</right>

---

#### Trasmettitore-ricevitore/amplificatore/tuner/rotore d’antenna (Blocco 3)

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Vengono controllati tramite l’interfaccia remota
* La conferma dei comandi di controllo avviene tramite la rete
</right>

---

[question:AF701]

---

[question:AF702]

---

[question:AF704]

---

[question:AF703]

---

[question:AF705]

---

### Ritardi nel funzionamento remoto

* I tempi di rete e di elaborazione causano latenze
* La codifica e decodifica dei segnali audio introduce ritardi
* Deve essere tenuto in considerazione durante il funzionamento radio

---

[question:AF709]

---

[question:AF710]

---

### Watchdog per il monitoraggio della stazione remota

* Evita stati incontrollati in caso di interruzione della connessione
* Scambio regolare di pacchetti dati tra stazione e operatore
* In caso di mancata risposta, il trasmettitore-ricevitore passa in uno stato sicuro

---

[question:AF708]

---

### Spegnimento remoto dell’alimentazione elettrica

* Il trasmettitore-ricevitore può entrare in uno stato indefinito
* La tensione di alimentazione dovrebbe poter essere spenta da remoto
* Soluzione: presa di rete intelligente per il controllo tramite rete

---

[question:AF707]

---

### Disturbi causati dal trasmettitore-ricevitore

* La stazione remota può essere disturbata dai propri segnali
* Sono necessarie misure adeguate per la soppressione dei disturbi

---

[question:AF706]
