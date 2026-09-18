En pratique, les débits de transmission de données atteignables varient considérablement selon la méthode de transmission et les conditions radio. Le Wi-Fi et la 5G permettent, dans des conditions optimales, des débits de transmission de données allant jusqu’à plusieurs gigabits par seconde. Le FT8, en revanche, peut être utilisé même dans des conditions difficiles, mais ne transmet que quelques bits par seconde.

Le débit de transmission de données réalisable dépend de la bande passante disponible et du rapport signal / bruit ($P_\text{S}/P_\text{N}$). À partir de ces deux grandeurs, la loi de Shannon-Hartley permet de calculer le débit de transmission de données théoriquement maximal pour un canal de transmission :

$C=B \cdot \log_2 \left(1+{\dfrac{P_\text{S}}{P_\text{N}}}\right) \unit{\bit\per\second}$

[question:AE416]

---

Une valeur facile à retenir s’obtient avec un rapport signal / bruit de $\qty{0}{\dB}$. Dans ce cas, la bande passante en $\unit{\hertz}$ correspond exactement au débit de transmission de données maximal en $\unit{\bit\per\second}$. Des rapports signal / bruit moins bons permettent des débits plus faibles, tandis que des rapports meilleurs autorisent des débits plus élevés. Cette astuce permet de répondre rapidement aux questions d’examen correspondantes sans effectuer de longs calculs.

<margin>
Si l’on remplace $\frac{P_\text{S}}{P_\text{N}} = \qty{0}{\dB}$, c’est-à-dire le facteur $\num{1}$, on obtient :
  
$\begin{split} C&=B \cdot \log_2 \left(1+1\right) \unit{\bit\per\second}\\ C&=B \cdot \log_2 \left(2\right) \unit{\bit\per\second}\\C &= \qty{B}{\bit\per\second}\end{split}$
</margin>

---

Si l’on souhaite transmettre nettement plus de bits par seconde que la bande passante disponible en $\unit{\hertz}$, le rapport signal / bruit requis augmente fortement. Il n’est donc pas possible d’obtenir des débits élevés sur des liaisons à bande étroite en ondes courtes. C’est pourquoi le Hamnet, en tant que réseau de données rapide, est généralement exploité dans la partie haute des UHF et la partie basse des SHF, où des bandes passantes plus élevées sont disponibles.

<indepth>
Ici, seule l’énergie de bruit dans la bande passante utilisée est prise en compte. Certains programmes informatiques utilisent cependant l’énergie de bruit d’un canal large de $\qty{2,4}{\kilo\hertz}$, même si le signal utile est bien plus étroit ; il s’agit d’une autre grandeur qui ne peut pas être directement intégrée dans la formule de la loi de Shannon-Hartley.
</indepth>

En revanche, en réduisant le débit de transmission de données, on peut développer des méthodes qui nécessitent non seulement une bande passante réduite, mais qui fonctionnent également avec un rapport signal / bruit extrêmement mauvais. Des exemples en sont les procédés de transmission numérique comme le WSPR ou le FT8, qui n’échangent que quelques caractères par unité de temps. Ainsi, même dans de mauvaises conditions radio, il est possible de transmettre au moins un court message.

[question:AE417]
[question:AE418]
[question:AE420]
[question:AE419]

Il faut noter que la loi de Shannon-Hartley ne détermine qu’une limite supérieure pour le débit de transmission de données atteignable. Les débits réellement atteignables sont toujours inférieurs. Ce n’est qu’avec de bonnes méthodes de correction d’erreurs, que nous apprendrons plus tard, qu’il est possible de s’approcher de cette limite.