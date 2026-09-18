Un alimentatore a commutazione (in inglese *switched-mode power supply*) converte una tensione alternata in una tensione continua stabilizzata. Per farlo, prima rettifica la tensione d’ingresso, poi la commuta molto rapidamente, la trasforma in modo efficiente nella tensione desiderata e infine la livella. Nel corso HB9 approfondiremo il funzionamento dettagliato nel capitolo [sec:schaltnetzteil_2].

<margin>
[foto:308:e_Ferritkerntrafo im Schaltnetzteils:Vista interna di un alimentatore a commutazione da $\qty{13,8}{\volt}$ e $\qty{35}{\ampere}$ con un piccolo trasformatore a nucleo di ferrite tra i due dissipatori, peso $\qty{2}{\kilo\gram}$]
</margin>

L’alimentatore a commutazione presenta diversi vantaggi rispetto a un alimentatore lineare regolato:

* Alto rendimento anche a basse tensioni nominali e con carichi variabili
* Peso e volume ridotti grazie all’uso di trasformatori più piccoli e condensatori di livellamento sul secondario, resi possibili dall’alta frequenza
* Buona regolazione
* Peso inferiore, dissipatori più piccoli e quindi minore ingombro rispetto a un alimentatore lineare regolato (vedi sezione: Stabilizzazione della tensione)

[question:ED302]

Tuttavia, le alte frequenze comportano anche alcuni svantaggi:

* Disturbi ad alta frequenza: a causa del funzionamento a commutazione con frequenze elevate, sono necessarie misure per migliorare la compatibilità elettromagnetica (EMC)
* Circuito complesso: sono necessari più componenti e aumenta la probabilità di guasto

[question:ED303]