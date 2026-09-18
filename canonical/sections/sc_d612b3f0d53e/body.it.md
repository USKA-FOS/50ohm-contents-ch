La frequenza di un VFO dipende direttamente dalla sua tensione di servizio (tensione continua). Questo è dovuto principalmente alla dipendenza del punto di lavoro del transistor nell'oscillatore.  
Per ottenere una stabilità di frequenza il più possibile elevata di un VFO rispetto alle fluttuazioni della tensione di servizio, quest'ultima deve essere stabilizzata il più possibile tramite opportune misure circuitali. La tensione di servizio di un VFO deve quindi essere indipendente dalle tensioni di servizio di altre sezioni (stabilizzata) e deve essere il più possibile filtrata e disaccoppiata. Questo può essere ottenuto, ad esempio, tramite un regolatore di tensione (cfr. figura [ref:a_osc_stab]).

[question:AD612]
[question:AD608]
[question:AD607]

<margin>
[picture:200:a_osc_stab:Regolatore di tensione]
</margin>

---

Con una scarsa stabilizzazione della tensione di servizio, nei trasmettitori CW molto semplici può verificarsi una distorsione della tonalità chiamata *chirp*: all'inizio di ogni singolo punto o linea la tonalità è inizialmente più alta o più bassa e poi si avvicina alla tonalità corretta. La parola inglese "chirp" significa letteralmente "cinguettio". Se la tonalità si avvicina dall'alto, l'effetto acustico ricorda effettivamente un cinguettio.

[question:AD609]

<margin>
Ecco un esempio di un segnale con chirp:

[include:applet_chirp_1]

Un altro esempio, un QSO tra RA1OW e OM3YCY, in cui l'effetto chirp è chiaramente udibile nel secondo passaggio:

[include:applet_chirp_2]

</margin>