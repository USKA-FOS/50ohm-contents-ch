Nella classe N abbiamo già appreso che il funzionamento remoto è consentito solo agli operatori radioamatori di classe A. Pertanto, in questa sezione esamineremo alcuni aspetti tecnici del funzionamento remoto rilevanti per l’utilizzo di una stazione remota.

Una stazione per il funzionamento remoto è composta da diversi blocchi funzionali logicamente separabili. Nei moderni apparecchi, alcune parti di questi blocchi funzionali possono essere integrate in un unico dispositivo (ad esempio, un trasmettitore-ricevitore con connessione di rete e interfaccia remota).

Un sistema per il funzionamento remoto può essere rappresentato logicamente con i seguenti blocchi funzionali.

---

<margin>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</margin>

* *Computer e pannello di controllo dell’operatore (Blocco 1)*: Questo serve per controllare la stazione remota. Qui, i segnali audio locali e i segnali di comando vengono convertiti in pacchetti di rete e trasmessi alla stazione remota. I segnali di comando e audio ricevuti dalla stazione remota (trasmessi tramite rete) vengono resi udibili e visibili nuovamente tramite il computer/pannello di controllo.
* *Rete*: Rete o reti di connessione tra la postazione dell’operatore e la stazione remota. Anche Internet può fungere da rete tra le due postazioni.
* *Computer o interfaccia remota nella postazione remota (Blocco 2)*: Questo converte i pacchetti di rete ricevuti dall’operatore in segnali di comando e audio per il controllo del trasmettitore-ricevitore nella stazione remota e, in direzione opposta, trasmette i segnali audio ricevuti dal trasmettitore-ricevitore tramite la rete all’operatore. Anche le impostazioni del trasmettitore-ricevitore e i segnali di comando di ritorno vengono trasmessi tramite la rete all’operatore.
* *Trasmettitore-ricevitore/amplificatore/tuner/rotore d’antenna (Blocco 3)*: Questi apparecchi vengono controllati o ricevono feedback tramite l’interfaccia remota o un computer nella postazione remota, tramite segnali trasmessi dall’operatore tramite la rete all’interfaccia remota.

[question:AF701]
[question:AF702]
[question:AF704]
[question:AF703]
[question:AF705]

---

Nel funzionamento remoto, a causa dei tempi di latenza nella rete e dei tempi di elaborazione nella codifica e decodifica dei segnali audio, si verificano ritardi temporali. Questo aspetto deve essere tenuto in considerazione durante le trasmissioni tramite stazioni remote.

<tip>
[photo:342:a_remote_station:Stazione remota del DARC e.V.]

Il DARC e.V. gestisce per i suoi membri alcune stazioni club remote distribuite in tutta la Germania. Sul sito [mein.darc.de](https://mein.darc.de/) i membri possono accedere alle stazioni remote tramite Internet e fare funzionamento radio, a condizione di possedere una licenza di classe A. Per le classi N ed E è consentito solo il funzionamento come SWL.

[Diventa ora membro del DARC!](https://50ohm.de/mw)
</tip>

[question:AF709]
[question:AF710]

Per garantire che una stazione remota, in caso di interruzione o disturbo della connessione dati tra l’utente/pannello di controllo e l’interfaccia remota, non cada in uno stato o funzionamento incontrollato, è necessaria una sorveglianza permanente e un feedback tra operatore e stazione remota tramite un cosiddetto *watchdog*. In questo caso, ad esempio a intervalli di pochi secondi, la stazione remota invia pacchetti di dati al computer dell’operatore, che devono essere confermati con una risposta entro un certo tempo. Se la risposta non arriva, la stazione remota rileva l’interruzione della connessione con l’operatore e può portare automaticamente il trasmettitore-ricevitore in uno stato sicuro definito (ad esempio, modalità di ricezione) e interrompere una trasmissione in corso.

[question:AF708]

Poiché anche il trasmettitore-ricevitore stesso può entrare in uno stato indefinito (ad esempio, a causa di errori software o hardware nel dispositivo), la tensione di alimentazione del trasmettitore-ricevitore deve poter essere disattivata da remoto. Questo può essere realizzato, ad esempio, tramite una presa intelligente IP, che può essere controllata dall’operatore tramite la rete.

[question:AF707]

Durante il funzionamento di una stazione remota, è inoltre necessario considerare e prevedere che i componenti della stazione remota possano essere disturbati dal trasmettitore-ricevitore nella postazione della stazione remota.

[question:AF706]