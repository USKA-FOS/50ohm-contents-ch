Les débits de transmission de données atteignables en pratique varient considérablement selon le procédé de transmission et les conditions de propagation. Le WLAN et la 5G supportent, dans des conditions optimales, des débits de transmission de données allant jusqu'à la gamme des gigabits par seconde. FT8, en revanche, peut être utilisé même dans des conditions défavorables, mais ne transmet que quelques bits par seconde.

Le débit de transmission de données atteignable dépend de la bande passante utilisable et du rapport signal / bruit ($P_\text{S}/P_\text{N}$). À partir de ces deux grandeurs, on peut calculer avec la loi de Shannon-Hartley le débit de transmission de données théoriquement maximal atteignable pour un canal de transmission:

$C=B \cdot \log_2 \left(1+{\dfrac{P_\text{S}}{P_\text{N}}}\right) \unit{\bit\per\second}$

[question:AE416]

---

Une valeur facile à retenir se présente pour un rapport signal / bruit de $\qty{0}{\dB}$. Ici, la bande passante en $\unit{\hertz}$ correspond exactement au débit maximal atteignable en $\unit{\bit\per\second}$. Des rapports signal / bruit moins bons permettent des débits de données correspondants plus faibles, des rapports signal / bruit meilleurs permettent des débits de données plus élevés. Avec cette aide mnémotechnique, les questions d'examen correspondantes peuvent également être répondues rapidement sans long calcul.

<margin>
Si nous insérons pour $\frac{P_\text{S}}{P_\text{N}} = \qty{0}{\dB}$, donc le facteur $\num{1}$, nous obtenons:
  
$\begin{split} C&=B \cdot \log_2 \left(1+1\right) \unit{\bit\per\second}\\ C&=B \cdot \log_2 \left(2\right) \unit{\bit\per\second}\\C &= \qty{B}{\bit\per\second}\end{split}$
</margin>

---

Si l'on veut transmettre nettement plus de bits par seconde que la bande passante disponible en $\unit{\hertz}$, le rapport signal / bruit nécessaire augmente fortement. Il n'est donc pas possible d'obtenir des débits de données élevés sur des liaisons à bande étroite sur les ondes courtes. C'est pourquoi le Hamnet, en tant que réseau de données rapide, est généralement exploité dans la gamme supérieure des UHF et inférieure des SHF, où des bandes passantes plus larges sont disponibles.

<indepth>
Ici, seule l'énergie de bruit qui se trouve dans la bande passante utilisée est prise en compte. Certains programmes informatiques, en revanche, utilisent l'énergie de bruit d'un canal de $\qty{2,4}{\kilo\hertz}$ de large, même si le signal utile réel est nettement plus étroit ; il s'agit cependant d'une autre grandeur qui ne peut pas être insérée directement dans la formule pour la loi de Shannon-Hartley.
</indepth>

En réduisant le débit de données, en revanche, il est possible de développer des procédés qui non seulement nécessitent une petite bande passante, mais qui fonctionnent également avec un rapport signal / bruit extrêmement mauvais. Des exemples de cela sont les procédés de transmission numériques tels que WSPR ou FT8, qui n'échangent que quelques caractères par unité de temps. Ainsi, même dans de mauvaises conditions de propagation, la transmission d'un court message est possible.

[question:AE417]
[question:AE418]
[question:AE420]
[question:AE419]

Il est à noter que la loi de Shannon-Hartley ne détermine qu'une limite supérieure pour le débit de transmission de données atteignable. Les débits de données réellement atteignables sont toujours inférieurs à cette limite. Ce n'est qu'au moyen de bons procédés de correction d'erreurs, que nous apprendrons plus tard, que l'on peut se rapprocher de cette limite.
