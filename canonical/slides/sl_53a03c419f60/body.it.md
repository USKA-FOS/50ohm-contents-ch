## Funzionamento remoto di stazioni radio

* Costituito da diversi blocchi funzionali
* Apparecchi moderni integrano parzialmente più blocchi
* Separazione tra operatore e postazione remota

---

### Schema a blocchi di una stazione remota

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Rappresentazione logica dei blocchi funzionali
* Controllo, connessione di rete, interfaccia remota
* Trasmettitore-ricevitore e apparecchi collegati
</right>

---

#### Computer e unità di controllo dell'operatore (Blocco 1)

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Converte segnali audio e di controllo in pacchetti di rete
* I segnali ricevuti vengono resi udibili e visibili
</right>

---

#### Rete

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Collega l'operatore alla postazione remota
* Possibilità di utilizzare Internet
</right>

---

#### Interfaccia remota presso la postazione remota (Blocco 2)

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Converte i pacchetti di rete in segnali di controllo e audio
* Trasmette i segnali audio ricevuti nuovamente all'operatore
</right>

---

#### Trasmettitore-ricevitore/Amplificatore/Sintonizzatore/Rotore antenna (Blocco 3)

<left>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</left>
<right>
* Vengono controllati tramite l'interfaccia remota
* Il feedback dei comandi di controllo avviene tramite la rete
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

* I tempi di rete ed elaborazione causano latenze
* La codifica e decodifica dei segnali audio causano ritardi
* Deve essere considerato durante il funzionamento radio

---

[question:AF709]

---

[question:AF710]

---

### Watchdog per il monitoraggio della stazione remota

* Impedisce uno stato incontrollato in caso di interruzione della connessione
* Scambio regolare di pacchetti di dati tra stazione e operatore
* In assenza di risposta, il trasmettitore-ricevitore passa a uno stato sicuro

---

[question:AF708]

---

### Spegnimento remoto dell'alimentazione

* Il trasmettitore-ricevitore può entrare in uno stato indefinito
* La tensione di alimentazione dovrebbe essere disattivabile da remoto
* Soluzione: Presa IP per il controllo tramite rete

---

[question:AF707]

---

### Disturbi causati dal trasmettitore-ricevitore

* La stazione remota può essere disturbata dai propri segnali
* Sono necessarie misure appropriate per la soppressione dei disturbi

---

[question:AF706]
