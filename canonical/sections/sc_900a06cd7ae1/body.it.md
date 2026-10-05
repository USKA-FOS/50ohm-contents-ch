Nella sezione [sec:remote_stationen] abbiamo già appreso i requisiti formali per la messa in servizio e l'utilizzo di un impianto radioamatoriale telecomandato. In questa sezione esamineremo alcuni aspetti tecnici del funzionamento remoto, rilevanti per l'operazione e l'uso di una stazione remota.

Una stazione per il funzionamento remoto è composta da diversi blocchi funzionali logicamente separabili. Nei dispositivi moderni, parti di questi blocchi funzionali possono essere integrate in un unico apparecchio (ad esempio, un trasmettitore-ricevitore con connessione di rete e interfaccia remota).

Una configurazione per il funzionamento remoto può essere rappresentata logicamente con i seguenti blocchi funzionali.

---

<margin>
[picture:501:a_remotebetrieb:schema a blocchi funzionamento remoto]
</margin>

* *Computer e unità di controllo dell'operatore (Blocco 1)*: Serve per controllare la stazione remota. Qui, i segnali audio locali e i segnali di comando vengono convertiti in pacchetti di dati di rete e trasmessi alla stazione remota. I segnali di comando e audio ricevuti dalla stazione remota (trasmessi via rete) vengono resi nuovamente udibili e visibili dal computer/dall'unità di controllo.
* *Rete*: Rete di connessione o reti di connessione tra la sede dell'operatore e la stazione remota. Anche Internet può servire come rete tra le sedi.
* *Computer o interfaccia remota presso la sede remota (Blocco 2)*: Questo converte i pacchetti di dati di rete ricevuti dall'operatore in segnali di comando e segnali audio per il controllo successivo del trasmettitore-ricevitore presso la sede remota e, in ritorno, trasmette i segnali audio ricevuti dal trasmettitore-ricevitore via rete all'operatore. Anche le impostazioni del trasmettitore-ricevitore e i segnali di comando di ritorno vengono trasmessi via rete all'operatore.
* *Trasmettitore-ricevitore/amplificatore/tuner/rotore d’antenna (Blocco 3)*: Questi apparecchi vengono controllati e il loro stato viene segnalato dall'interfaccia remota o da un computer presso la sede remota tramite segnali che l'operatore trasmette via rete all'interfaccia remota.

[question:AF701]
[question:AF702]
[question:AF704]
[question:AF703]
[question:AF705]

---

Nel funzionamento remoto, i tempi di propagazione nella rete e i tempi di elaborazione per la codifica e decodifica dei segnali audio causano ritardi temporali. Questo deve essere considerato nell'operazione radio tramite stazioni remote.

<indepth>
Particolarità nel funzionamento remoto

- Nelle comunicazioni vocali, i ritardi sono generalmente poco problematici.

- Nelle comunicazioni telegrafiche (Morse), i ritardi - specialmente nell'operazione in contest - possono manifestarsi come disturbanti a seconda del concetto di manipolazione.

- Per le modalità operative digitali basate sull'emissione di toni, è da notare che il codec vocale può potenzialmente influenzare i segnali in modo disturbante.

</indepth>

<tip>
Le stazioni remote sono talvolta offerte dalle [sezioni USKA](https://uska.ch/de/funkamateure/die-uska/sektionen/) o da associazioni per i loro membri. Altre stazioni remote appartengono a gruppi di utenti chiusi. Idealmente, le stazioni remote si trovano in posizioni vantaggiose per le antenne.

[Diventa ora membro dell'USKA!](https://uska.ch/de/uska-beitreten/)
</tip>

[question:AF709]
[question:AF710]

Per garantire che una stazione remota non entri in uno stato/operazione incontrollata in caso di interruzione o disturbo della connessione dati tra utente/unità di controllo e interfaccia remota, è necessaria una sorveglianza permanente e una retroazione tra operatore e stazione remota tramite un cosiddetto watchdog. Qui, ad esempio, a intervalli di pochi secondi, pacchetti di dati vengono inviati dalla stazione remota al computer dell'operatore, che devono essere confermati con una risposta di ritorno entro un certo tempo. Se questa risposta di ritorno non avviene, la stazione remota sa che la connessione con l'operatore è interrotta e può portare automaticamente il trasmettitore-ricevitore in uno stato sicuro definito (ad esempio, modalità ricezione) e interrompere una trasmissione in corso.

[question:AF708]

Poiché anche il trasmettitore-ricevitore stesso può entrare in uno stato indefinito (ad esempio, a causa di errori software o hardware nell'apparecchio), la tensione di alimentazione del trasmettitore-ricevitore dovrebbe essere disattivabile da remoto. Questo può avvenire, ad esempio, tramite una presa IP, che può essere controllata dall'operatore via rete.

<tip>
Alcuni trasmettitori-ricevitori hanno una funzione "Transmit Timeout Timer" (TOT), con cui la durata massima di trasmissione ininterrotta può essere limitata a un tempo regolabile. Questo costituisce una protezione aggiuntiva contro la trasmissione continua.
</tip>

[question:AF707]

Nell'operazione di una stazione remota, è anche da considerare e da prevedere che i componenti della stazione remota possano essere disturbati dal trasmettitore-ricevitore presso la sede della stazione remota.

[question:AF706]
