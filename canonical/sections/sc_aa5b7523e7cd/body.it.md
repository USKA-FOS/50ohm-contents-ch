<margin>
[picture:666:n_halbleiter_diode_merkhilfe:guida per la memoria diodo]
</margin>

Per convertire una tensione alternata in una tensione continua è necessario un raddrizzatore. La forma più semplice di raddrizzamento avviene tramite un diodo. Come già appreso nel capitolo [sec:diode_1], un diodo permette il flusso di corrente solo in una direzione.

---

Questa proprietà del diodo viene sfruttata per generare una tensione continua da una tensione alternata (cfr. figura [ref:e_einweggleichrichter_ue]). Se si collega una resistenza di carico in serie a un diodo collegato a una sorgente di tensione alternata (circuito in figura [ref:e_einweggleichrichter]), il diodo conduce la corrente solo quando l’anodo è positivo rispetto al catodo. In questo caso, la semionda positiva della tensione alternata viene lasciata passare.

Durante la semionda negativa il diodo blocca la corrente, quindi la tensione d’uscita in questo intervallo rimane a zero (cfr. figura [ref:e_einweggleichrichter_ul]). Poiché in questo circuito viene utilizzata solo una semionda della tensione alternata sinusoidale, questa configurazione viene chiamata *raddrizzamento a semionda*.

---
<margin>
[picture:797:e_einweggleichrichter:raddrizzatore a semionda]
[picture:798:e_einweggleichrichter_ue:tensione d’ingresso raddrizzatore a semionda]
[picture:796:e_einweggleichrichter_ul:tensione di carico raddrizzatore a semionda]
</margin>

[question:ED304]

Se si collega in parallelo alla resistenza di carico un condensatore di capacità sufficientemente grande, questo si carica rapidamente durante la semionda conduttrice tramite il diodo. Nella semionda successiva, in cui il diodo è in blocco, il condensatore si scarica lentamente attraverso la resistenza. In questo modo la tensione pulsante viene livellata e si avvicina a una tensione continua.

Oltre al raddrizzamento a semionda esistono altre configurazioni di raddrizzatori, ad esempio il raddrizzatore a ponte. Tuttavia, queste varianti verranno trattate in modo approfondito solo nel corso per HB9 nei capitoli [sec:gleichrichter_2] e [sec:brueckengleichrichter].