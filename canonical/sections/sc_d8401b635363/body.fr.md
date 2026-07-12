L'alimentation d'une antenne se fait toujours avec une tension et un courant qui sont dans un certain rapport l'un à l'autre. Ce rapport est appelé impédance d'alimentation.

Pour qu'une puissance puisse être délivrée, il faut toujours qu'il y ait une tension *et* un courant, car la puissance résulte de la multiplication de la tension et du courant. Si la tension ou le courant est nul, il n'y a pas de puissance délivrée ou reçue.

Cependant, nous parlons de certaines antennes comme étant des antennes *alimentées par le courant* et d'autres comme étant des antennes *alimentées par la tension*. Cela signifie que pour certaines antennes, un courant élevé est présent à la pointe d'alimentation avec une tension relativement faible, ou une tension élevée avec un courant relativement faible.

---

Pour un dipôle demi-onde, l'impédance d'alimentation dépend de l'endroit où l'alimentation est effectuée. Cela est dû au fait que dans le dipôle, les porteurs de charge oscillent et qu'au milieu, il y a particulièrement beaucoup de porteurs de charge en mouvement, que nous appelons ventre de courant, et aux extrémités, des tensions particulièrement élevées se produisent, que nous appelons ventre de tension. Là où aucune charge n'est déplacée, nous parlons d'un nœud de courant, et là où la tension est nulle, nous parlons d'un nœud de tension. La figure [ref:e_strom_spannung_speisung_dipol] montre la distribution du courant et de la tension sur le dipôle.

[question:EG203]

<margin>
[picture:787:e_strom_spannung_speisung_dipol:Dipôle demi-onde avec distribution de tension et de courant]
</margin>

---

Si nous alimentons donc un dipôle demi-onde au milieu, de nombreuses charges doivent être déplacées et nous parlons d'une antenne alimentée par le courant (basse impédance d'alimentation). Un dipôle demi-onde alimenté à l'extrémité, en revanche, est une antenne alimentée par la tension (haute impédance d'alimentation). Pour l'alimentation à l'extrémité, comme le montre la figure [ref:e_strom_spannung_speisung_dipol_ende], un élément d'adaptation est nécessaire. Nous en discuterons plus en détail dans la partie HB9.

<margin>
[picture:851:e_strom_spannung_speisung_dipol_ende:Dipôle demi-onde alimenté à l'extrémité]
</margin>

---

Les antennes alimentées par le courant présentent donc une résistance faible et les antennes alimentées par la tension une résistance élevée.

Cela peut être bien illustré à l'aide de la loi d'Ohm:

$ R = \frac{U}{I} $

Si l'on alimente un dipôle au milieu, une tension relativement faible est présente avec un courant simultanément élevé. Le quotient de la tension et du courant est donc petit, la résistance résultante étant faible. Si l'alimentation est effectuée à l'extrémité du dipôle, une tension élevée est présente, tandis que le courant tend vers zéro. Ainsi, le quotient devient très grand, et la résistance résultante prend des valeurs très élevées.

Pour les résistances faibles, nous parlons également d'un comportement *faible impédance* ($\downarrow\unit{\ohm}$) et pour les résistances élevées, d'un comportement *haute impédance* ($\uparrow\unit{\ohm}$).

<indepth>
Un ordre de grandeur habituel pour l'*impédance d'alimentation* d'une antenne alimentée par le courant est par exemple $\qty{36}{\ohm}$ à $\qty{100}{\ohm}$ et pour les antennes alimentées par la tension $\qty{1500}{\ohm}$ à $\qty{4000}{\ohm}$.
</indepth>

---

<indepth>
La distribution du courant sur un dipôle dépend de la fréquence à laquelle l'antenne est utilisée. La figure [ref:e_stromverteilungen] montre la distribution du courant pour des multiples entiers de la fréquence fondamentale $f$ dans un dipôle alimenté au milieu. On peut voir que pour les multiples pairs de la fréquence fondamentale, un nœud de courant se produit au point d'alimentation. Dans ce cas, le courant y est très faible, la tension est élevée, et l'antenne apparaît haute impédance au point d'alimentation. C'est pourquoi un dipôle alimenté au milieu n'est résonant que pour les multiples entiers impairs de la fréquence fondamentale. Une utilisation de plusieurs bandes peut être réalisée en déplaçant le point d'alimentation, par exemple vers l'un des ventres de courant comme dans la figure [ref:e_stromverteilungen]b (par exemple pour l'antenne Windom) ou vers l'extrémité de l'antenne (par exemple pour l'antenne EFHW ou Fuchs). Dans ces cas, cependant, des dispositifs d'adaptation sont nécessaires, que nous aborderons plus en détail dans la partie HB9.

[picture:1050:e_stromverteilungen:Distributions de courant à différentes fréquences fondamentales]
</indepth>

[question:EG204]
[question:EG205]
[question:EG206]
