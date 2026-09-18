L'alimentation d'une antenne se fait toujours avec une tension et un courant qui sont dans un rapport déterminé. Ce rapport est appelé résistance d'alimentation.

Pour qu'une puissance puisse être émise, il faut toujours qu'il y ait à la fois tension *et* courant, car la puissance résulte de la multiplication de la tension par le courant. Si la tension ou le courant était nul, il n'y aurait ni émission ni réception de puissance.

Pourtant, on parle de certaines antennes comme d'*antennes alimentées en courant* et d'autres comme d'*antennes alimentées en tension*. Cela signifie que, pour certaines antennes, il y a un courant élevé avec une tension relativement faible au point d'alimentation, ou une tension élevée avec un courant relativement faible.


---

Pour un dipôle demi-onde, la résistance d'alimentation dépend du point où l'alimentation est appliquée. Cela s'explique par le fait que, dans un dipôle, les porteurs de charge oscillent d'avant en arrière, ce qui entraîne un mouvement particulièrement important de charges au centre (que l'on appelle *ventre de courant*), et des tensions particulièrement élevées aux extrémités (que l'on appelle *ventre de tension*). Là où il n'y a pas de mouvement de charges, on parle de *nœud de courant*, et là où la tension est nulle, on parle de *nœud de tension*. L'illustration [ref:e_strom_spannung_speisung_dipol] montre la répartition du courant et de la tension sur le dipôle.

[question:EG203]

<margin>
[picture:787:e_strom_spannung_speisung_dipol:Dipôle demi-onde avec répartition du courant et de la tension]
</margin>

---

Si l'on alimente un dipôle demi-onde au centre, il faut déplacer de nombreuses charges, et on parle alors d'*antenne alimentée en courant* (faible résistance d'alimentation). Un dipôle demi-onde alimenté à l'extrémité est en revanche une *antenne alimentée en tension* (résistance d'alimentation élevée). Pour l'alimentation à l'extrémité, comme illustré dans l'image [ref:e_strom_spannung_speisung_dipol_ende], un élément d'adaptation est nécessaire. Nous aborderons ce point plus en détail dans la partie HB9.

<margin>
[picture:851:e_strom_spannung_speisung_dipol_ende:Dipôle demi-onde alimenté à l'extrémité]
</margin>

---

Les antennes alimentées en courant présentent donc une faible résistance, tandis que les antennes alimentées en tension présentent une résistance élevée.

Cela peut être illustré à l'aide de la loi d'Ohm :

$ R = \frac{U}{I} $

Si l'on alimente un dipôle au centre, on y trouve une tension relativement faible avec un courant élevé. Le quotient de la tension par le courant est donc faible, et la résistance résultante est faible. Si l'alimentation est appliquée à l'extrémité du dipôle, on y trouve une tension élevée tandis que le courant tend vers zéro. Le quotient devient alors très grand, et la résistance résultante prend des valeurs élevées.

Pour les faibles résistances, on parle aussi de comportement *à basse impédance* ($\downarrow\unit{\ohm}$) et pour les résistances élevées, de comportement *à haute impédance* ($\uparrow\unit{\ohm}$).

<indepth>
Un ordre de grandeur courant pour la *résistance d'alimentation* d'une antenne alimentée en courant est par exemple de $\qty{36}{\ohm}$ à $\qty{100}{\ohm}$, et pour les antennes alimentées en tension de $\qty{1500}{\ohm}$ à $\qty{4000}{\ohm}$.
</indepth>

---

<indepth>
La répartition du courant sur un dipôle dépend de la fréquence à laquelle l'antenne est utilisée. L'illustration [ref:e_stromverteilungen] montre la répartition du courant pour des multiples entiers de la fréquence fondamentale $f$ sur un dipôle alimenté au centre. On peut y observer que, pour les multiples pairs de la fréquence fondamentale, un nœud de courant se forme au point d'alimentation. Dans ce cas, le courant y est très faible, tandis que la tension est élevée, et l'antenne apparaît comme à haute impédance au point d'alimentation. C'est pourquoi un dipôle alimenté au centre n'est résonant que pour des multiples impairs de la fréquence fondamentale. L'utilisation de plusieurs bandes peut être obtenue en déplaçant le point d'alimentation, par exemple vers l'un des ventres de courant comme dans l'illustration [ref:e_stromverteilungen]b (par exemple pour l'antenne Windom) ou vers l'extrémité de l'antenne (par exemple pour l'antenne EFHW ou l'antenne Fuchs). Dans ces cas, des dispositifs d'adaptation sont nécessaires, que nous aborderons plus en détail dans la partie HB9.

[picture:1050:e_stromverteilungen:Répartition du courant pour différentes fréquences fondamentales]
</indepth>

[question:EG204]
[question:EG205]
[question:EG206]
