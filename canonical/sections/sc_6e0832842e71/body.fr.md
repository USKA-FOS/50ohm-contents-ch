Un signal idéalement sinusoïdal ne contient que son *fondamental*, également appelé *1ère harmonique*. Dès qu'un signal s'écarte de la forme sinusoïdale, même légèrement, il contient des *multiples entiers* de sa fréquence fondamentale, appelés *harmoniques supérieures* ou *harmoniques*. Il est important de bien distinguer ces deux notions.

L'illustration [ref:zusammenhang_oberwellen_harmonische] et le tableau [ref:a_harmonische] montrent la relation entre harmoniques supérieures et harmoniques, qu'il suffit de retenir une fois pour toutes. La 1ère harmonique supérieure correspond à la 2ème harmonique du fondamental et se situe à une fréquence double de celle-ci. La 2ème harmonique supérieure correspond à la 3ème harmonique du fondamental et se situe à une fréquence triple de celle-ci. Selon ce principe, toutes les harmoniques et harmoniques supérieures sont référencées par rapport au fondamental et numérotées avec un nombre ordinal $N$.

<margin>
[picture:869:zusammenhang_oberwellen_harmonische:Relation entre harmoniques supérieures et harmoniques]


| l: Multiple de la fréquence fondamentale | l: Harmonique | l: Harmonique supérieure |
| $f_0$ | 1 | ~ |
| $2 \cdot f_0$ | 2 | 1 |
| $3 \cdot f_0$ | 3 | 2 |
| $4 \cdot f_0$ | 4 | 3 |
[table:a_harmonische:Harmoniques et harmoniques supérieures]
</margin>

<indepth>
Selon le type de distorsion d'un signal, le spectre de fréquences contient davantage d'harmoniques supérieures paires ou impaires. Les signaux rectangulaires, qui apparaissent par exemple lors de la surmodulation d'étages amplificateurs (les crêtes d'amplitude sont alors limitées et aplaties), contiennent des harmoniques impaires ou des harmoniques supérieures paires.

<webonly>
[include:applet_rectangle]

Aux points de discontinuité, l'approximation de Fourier fait apparaître le phénomène de Gibbs : même avec un grand nombre d'harmoniques, il subsiste un léger dépassement et une oscillation résiduelle.
</webonly>

Les signaux en dents de scie contiennent principalement des harmoniques paires ou des harmoniques supérieures impaires.
</indepth>

[question:AB403]
[question:AB401]
[question:AB402]


Si la fréquence fondamentale d'un signal est connue, la fréquence de la $N$-ième harmonique s'obtient en multipliant la fréquence fondamentale par le nombre ordinal $N$ :

$f_N = N \cdot f_0$


Pour la $N$-ième harmonique supérieure, on a en revanche :

$f_\mathrm{harmonique\ supérieure,N} = (N+1)\cdot f_0$


[question:AJ201]
[question:AJ205]
[question:AJ202]
[question:AJ206]


Même si un signal semble sinusoïdal à l'oscilloscope, il peut contenir des composantes d'harmoniques supérieures (ou harmoniques du fondamental) non négligeables. Pour évaluer quantitativement et qualitativement la part d'harmoniques supérieures dans un signal, il faut utiliser un *analyseur de spectre* capable de représenter le signal dans le domaine fréquentiel (domaine des fréquences) et d'afficher les amplitudes des différentes harmoniques supérieures de manière logarithmique, afin de mesurer leur contribution au signal global.

[question:AI615]
[question:AI614]
