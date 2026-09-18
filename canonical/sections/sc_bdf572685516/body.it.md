Una linea di alimentazione può essere rappresentata come un circuito composto da molte piccole induttanze e capacità, come illustrato nella figura [ref:a_wellenwiderstand]. Da questi cosiddetti induttanza per unità di lunghezza $L'$ in $\unit{\henry\per\meter}$ e capacità per unità di lunghezza $C'$ in $\unit{\farad\per\meter}$ deriva l'impedenza caratteristica $Z$ della linea. In generale vale:

$Z_0 = \sqrt{\frac{L'}{C'}}.$

<margin>
[picture:1108:a_wellenwiderstand:Impedenza caratteristica di una linea di alimentazione]

| X: Proprietà                  | l: Valore                              |
| Impedenza                    | $\qty{50}{\ohm}$                      |
| Banda di frequenza           | $ < \qty{1}{\giga\hertz}$             |
| Capacità per unità di lunghezza | $\qty{100}{\pico\farad\per\meter}$    |
| Induttanza per unità di lunghezza | $\qty{0,25}{\micro\henry\per\meter}$  |
| Velocità di propagazione     | $\qty{0,66}{\percent}$                |
[table:a_rg58:Dati tecnici estratti da una scheda tecnica di un cavo coassiale RG-58]
</margin>

La tabella [ref:a_rg58] mostra i dati tecnici di un cavo coassiale RG-58. L'impedenza caratteristica è di $\qty{50}{\ohm}$, la capacità per unità di lunghezza è $\qty{100}{\pico\farad\per\meter}$ e l'induttanza per unità di lunghezza è $\qty{0,25}{\micro\henry\per\meter}$. Da questi valori è possibile calcolare l'impedenza caratteristica con la formula sopra riportata:

$Z_0 = \sqrt{\frac{\qty{0,25}{\micro\henry\per\meter}}{\qty{100}{\pico\farad\per\meter}}} = \sqrt{2500} = \qty{50}{\ohm}$

Se questi valori di capacità e induttanza per unità di lunghezza non sono noti, esistono formule nella raccolta di formule che si basano sulle dimensioni geometriche della linea e sulla costante dielettrica relativa del dielettrico.

L'impedenza caratteristica $Z_0$ di una linea bifilare simmetrica dipende, ad esempio, dalla distanza tra i conduttori ($a$) e dal loro diametro ($d$), nonché dalla costante dielettrica relativa $\epsilon_\mathrm{r}$ del dielettrico interposto. L'equazione indicata nella raccolta di formule è valida per $a/d > 2,5$:

$Z_0 = \dfrac{\qty{120}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{2\cdot a}{d}\right)}$

Qui, $\ln$ rappresenta il logaritmo naturale.

[question:AG305]

L'impedenza caratteristica $Z_0$ di una linea coassiale dipende dal rapporto tra il diametro interno del conduttore esterno ($D$) e il diametro del conduttore interno ($d$), nonché dal dielettrico interposto. Dalla raccolta di formule ricaviamo:

$Z_0 = \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{D}{d}\right)}$

Qui, $\ln$ rappresenta il logaritmo naturale e $\epsilon_\mathrm{r}$ la costante dielettrica relativa del dielettrico.

[question:AG306]
[question:AG307]

Se una linea viene chiusa con la sua impedenza caratteristica, cioè se a un'estremità viene collegato un componente o un'antenna che presenta esattamente la stessa resistenza dell'impedenza caratteristica della linea, si parla di adattamento. In questo caso, le onde non vengono riflesse a questa estremità del cavo.

[question:AG304]