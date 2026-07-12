Una stazione per il funzionamento remoto è composta da diversi blocchi funzionali logicamente separabili. Nei dispositivi moderni, parte di questi blocchi funzionali possono anche essere integrati in un unico dispositivo (ad es. trasmettitore-ricevitore con connessione di rete e interfaccia remota).

Una configurazione per il funzionamento remoto può essere rappresentata logicamente con i seguenti blocchi funzionali.

---

<margin>
[picture:501:a_remotebetrieb:Schema a blocchi funzionamento remoto]
</margin>

* *Computer e unità di controllo dell'operatore (Blocco 1)*: Serve per controllare la stazione remota. Qui, i segnali audio e i segnali di controllo vengono convertiti localmente in pacchetti di rete e trasmessi alla stazione remota. I segnali di controllo e audio ricevuti dalla stazione remota (che vengono trasmessi tramite rete) vengono resi nuovamente udibili e visibili dal computer/unità di controllo.
* *Rete*: Rete di connessione o reti di connessione tra la posizione dell'operatore e la stazione remota. In questo caso, anche Internet può fungere da rete tra le posizioni.
* *Computer o interfaccia remota nella posizione remota (Blocco 2)*: Questo converte i pacchetti di rete ricevuti dall'operatore in segnali di controllo e segnali audio per l'ulteriore controllo del trasmettitore-ricevitore nella posizione remota e, nel percorso di ritorno, trasmette i segnali audio ricevuti dal trasmettitore-ricevitore tramite la rete all'operatore. Anche le regolazioni del trasmettitore-ricevitore e i segnali di controllo di ritorno vengono trasmessi all'operatore tramite la rete.
* *Trasmettitore-ricevitore/Amplificatore/Tuner/Rotore antenna (Blocco 3)*: Questi dispositivi vengono comandati/segnalati dall'interfaccia remota o da un computer nella posizione remota tramite segnali che l'operatore trasmette all'interfaccia remota tramite la rete.

[question:AF701]
[question:AF702]
[question:AF704]
[question:AF703]
[question:AF705]

Nel funzionamento remoto, a causa dei tempi di percorrenza nella rete e dei tempi di elaborazione nella codifica e decodifica dei segnali audio, si verificano ritardi temporali. Questo deve essere considerato durante il funzionamento radio tramite stazioni remote.

[question:AF709]
[question:AF710]

Per garantire che una stazione remota non cada in uno stato/funzionamento incontrollato in caso di interruzione o disturbo del collegamento dati tra l'utente/unità di controllo e l'interfaccia remota, è necessario un monitoraggio e un feedback permanenti tra l'operatore e la stazione remota tramite un cosiddetto watchdog. In questo caso, ad esempio, a intervalli di pochi secondi, pacchetti di dati vengono inviati dalla stazione remota al computer dell'operatore, che devono essere confermati entro un certo tempo tramite una risposta. Se questa risposta non avviene, la stazione remota sa che la connessione con l'operatore è interrotta e può portare automaticamente il trasmettitore-ricevitore in uno stato sicuro definito (ad es. modalità di ricezione) e interrompere una trasmissione in corso.

[question:AF708]

Poiché anche il trasmettitore-ricevitore stesso può entrare in uno stato indefinito (ad es. a causa di errori software o hardware nel dispositivo), la tensione di alimentazione del trasmettitore-ricevitore dovrebbe essere disattivabile da remoto. Ciò può avvenire, ad esempio, tramite una presa IP che può essere controllata dall'operatore tramite la rete.

[question:AF707]

Durante il funzionamento di una stazione remota, si deve anche considerare e prevedere che i componenti della stazione remota possano essere disturbati dal trasmettitore-ricevitore nella posizione della stazione remota.

[question:AF706]