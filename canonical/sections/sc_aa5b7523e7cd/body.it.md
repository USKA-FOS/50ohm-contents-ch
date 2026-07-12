<margin>
[picture:666:n_halbleiter_diode_merkhilfe:Merkhilfe Diode]
</margin>

Per generare una tensione continua da una tensione alternata, è necessario un raddrizzatore. La forma più semplice di raddrizzamento avviene tramite un diodo. Come abbiamo già imparato nella classe N, un diodo permette alla corrente di fluire solo in una direzione.

---

Sfruttiamo questa proprietà del diodo per generare una tensione continua da una tensione alternata (cfr. figura [ref:e_einweggleichrichter_ue]). Se si collega una resistenza di carico a una fonte di tensione alternata tramite un diodo collegato in serie (circuito in figura [ref:e_einweggleichrichter]), il diodo conduce corrente solo quando l'anodo è positivo rispetto al catodo. In questo caso, la semionda positiva della tensione alternata viene lasciata passare.

Durante la semionda negativa, il diodo blocca, in modo che la tensione d'uscita rimanga a zero in questo periodo (cfr. figura [ref:e_einweggleichrichter_ul]). Poiché in questo circuito viene utilizzata solo una semionda della tensione alternata sinusoidale, questo viene definito *raddrizzamento a semionda*.

---
<margin>
[picture:797:e_einweggleichrichter:Einweggleichrichter]
[picture:798:e_einweggleichrichter_ue:Eingangsspannung Einweggleichrichter]
[picture:796:e_einweggleichrichter_ul:Lastspannung Einweggleichrichter]
</margin>

[question:ED304]

Se si collega inoltre un condensatore sufficientemente grande in parallelo alla resistenza di carico, questo si carica rapidamente tramite il diodo durante la semionda conduttiva. Nella semionda successiva, in cui il diodo blocca, il condensatore si scarica lentamente attraverso la resistenza. In questo modo, la tensione pulsante viene livellata e si avvicina a una tensione continua.

Oltre al raddrizzamento a semionda, esistono altri circuiti raddrizzatori, ad esempio il raddrizzatore a ponte. Tuttavia, affronteremo queste varianti più in dettaglio solo nella classe A.