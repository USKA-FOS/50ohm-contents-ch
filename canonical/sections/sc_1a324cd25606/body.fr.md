% Semi-conducteurs II
% DF2DR 2024-08-19

La matière première de notre monde moderne est constituée de matériaux semi-conducteurs. Une raison suffisante pour s'y intéresser un peu plus en détail. Les semi-conducteurs ont une structure de réseau cristallin, c'est-à-dire que leurs atomes sont disposés périodiquement. 

<margin>
[picture:854:a_silizium_halbleiter:Semi-conducteur en cristal de silicium]
</margin>

Tous les matériaux semi-conducteurs ont deux propriétés en commun:

---

Il existe une *bande interdite d'énergie*, qui est une conséquence de la structure périodique. Cela signifie que les électrons dans le cristal ne peuvent pas prendre certaines énergies. L'énergie la plus élevée que les électrons liés aux atomes peuvent avoir est appelée *énergie de la bande de valence*. Cependant, comme les électrons sont tous liés aux atomes du réseau, ils ne peuvent pas contribuer au flux de courant. Il existe d'autres états d'énergie que les électrons peuvent atteindre - ils se trouvent dans la *bande de conduction*, qui est située au-dessus du bord de la bande de valence de la quantité de la bande interdite. Les électrons dans la bande de conduction peuvent contribuer au flux de courant lorsque nous appliquons une tension à l'échantillon de semi-conducteur. Pour cela, ils ont besoin d'une énergie supérieure à celle de la bande interdite. Ils peuvent absorber cette énergie sous forme d'énergie thermique, c'est pourquoi les semi-conducteurs très purs sont de très bons isolants à basse température.

[question:AB104]

<margin>
L'énergie de la bande interdite est déterminée par la composition chimique du semi-conducteur. Comparé au Si, le Ge a une énergie de bande interdite nettement plus petite, le GaAs et l'InP une énergie de bande interdite un peu plus grande et le GaN une énergie de bande interdite beaucoup plus grande.
</margin>

Le silicium (Si) et le germanium (Ge) sont des *semi-conducteurs élémentaires* (comme d'ailleurs le diamant, qui est du carbone cristallin). Il existe également des composés chimiques qui sont des semi-conducteurs (*semi-conducteurs composés*), comme l'arséniure de gallium (GaAs), le phosphure d'indium (InP) ou également le nitrure de gallium (GaN). 

---

Les matériaux avec une bande interdite d'énergie ne sont appelés semi-conducteurs que s'ils sont en outre *dopables*. Leur conductivité peut être modifiée dans de larges limites par une impureté ciblée du matériau semi-conducteur très pur. Ainsi, l'arsenic (As), comparé aux semi-conducteurs élémentaires, a un électron de plus dans la couche électronique externe. Cet électron peut devenir très facilement et avec peu d'énergie un électron libre dans la bande de conduction. Un tel dopage est appelé *dopage n*.

<margin>
[picture:855:a_n_dotierung:Dopage n]
</margin>

---

Mais que se passe-t-il si nous contaminons le semi-conducteur avec un matériau qui a un électron de moins dans la couche électronique externe ? Une telle lacune d'électrons est appelée un *trou*. Comme l'atome était neutre auparavant, la lacune d'électrons a une charge positive. Les trous peuvent également se déplacer dans le cristal et contribuer à un flux de courant. Un tel dopage est appelé *dopage p*.

<margin>
[picture:856:a_p_dotierung:Dopage p]
</margin>

En résumé, nous pouvons constater:
* Le dopage n crée un excès d'électrons dans le semi-conducteur.
* Le dopage p crée un excès de trous dans le semi-conducteur.

[question:AB105]
[question:AB106]
[question:AB107]

---

Si l'on combine dans un cristal, mais séparés spatialement, des zones dopées p et n, un échange de porteurs de charge se produit au niveau du contact : les électrons se déplacent de la zone dopée n en direction de la zone dopée p, les trous se déplacent de la zone dopée p en direction de la zone dopée n. Ce mouvement des porteurs de charge, qui est provoqué par les différences de densité d'électrons et de trous, est appelé *courant de diffusion*.

Cette séparation de charge crée d'autre part un *champ électrique* d'effet opposé, qui conduit à un courant de champ. En équilibre (sans tension appliquée de l'extérieur) les effets de la diffusion et du champ électrique s'équilibrent exactement. Entre les zones p et n, il se forme une zone sans porteurs de charge libres, que l'on appelle *zone d'appauvrissement* ou *couche de blocage*. Une telle structure représente une *diode pn*.

[question:AB108]

<margin>
[picture:857:a_pn_uebergang:Transition PN]
</margin>

---

Maintenant, nous appliquons une tension de l'extérieur, qui est plus positive au niveau de la zone p (*anode*) qu'au niveau de la zone n (*cathode*). L'électrode positive attire les électrons à travers la zone d'appauvrissement et l'électrode négative attire les trous. La zone d'appauvrissement est réduite, il se produit un flux de courant. Cela représente le fonctionnement en *sens direct*.

<margin>
[picture:956:a_pn_uebergang_mit_spannung:Transition PN avec tension externe]
</margin>

[question:AC402]

---

Si nous inversons maintenant la tension, la zone d'appauvrissement s'élargit, le flux de courant s'arrête. Il s'agit du *fonctionnement en inverse* de la diode.

<margin>
[picture:957:a_pn_uebergang_mit_spannung:Transition PN avec tension externe]
</margin>


[question:AB109]