Nous avons appris : si une antenne est parfaitement adaptée à la ligne d'alimentation (par exemple un câble coaxial), le ROS-mètre affiche la valeur 1. C'est le meilleur cas possible, car toute la puissance d'émission est absorbée par l'antenne et aucune puissance n'est réfléchie vers l'émetteur. En revanche, si aucune antenne n'est connectée ou si la ligne de transmission est interrompue ou en court-circuit, la valeur du ROS tend vers l'infini (∞). Dans ces cas, la puissance d'émission est presque entièrement réfléchie. Une telle réflexion totale peut, dans le pire des cas, endommager l'étage final de l'émetteur. Nous approfondissons ici le sujet et abordons également les valeurs comprises entre 1 et ∞.

Le rapport d'ondes stationnaires (ROS), symbolisé par s, peut être calculé à partir de la puissance incidente P<sub>V</sub> et de la puissance réfléchie P<sub>R</sub>. La relation correspondante est la suivante :

s = (√P<sub>V</sub> + √P<sub>R</sub>) / (√P<sub>V</sub> − √P<sub>R</sub>)

Par exemple, si l'émetteur fournit une puissance de P<sub>V</sub> = 100 W et que 25 W sont réfléchis par l'antenne en direction de l'émetteur, on obtient :

s = (√100 + √25) / (√100 − √25) = (10 + 5) / (10 − 5) = 15 / 5 = 3

Cela signifie qu'un ROS de 3 correspond à une réflexion de 25 W / 100 W = 25 %.

D'autres correspondances sont présentées dans le tableau [ref:e_swr_werte].

<margin>
| l: ROS | l: Puissance réfléchie |
| 1 | 0 % |
| 1,5 | 4 % |
| 2 | 11,1 % |
| 2,5 | 18,4 % |
| *3* | *25 %* |
| 4 | 36 % |
| 6 | 51 % |
| 10 | 66,9 % |
| 20 | 81,9 % |
| ∞ | 100 % |
[table:e_swr_werte:Valeurs du ROS en fonction de la puissance réfléchie]
</margin>

---

<tip>
Pour répondre aux questions suivantes, il suffit de savoir qu'un rapport d'ondes stationnaires de 3 correspond à une réflexion de 25 % de l'énergie, c'est-à-dire que l'onde réfléchie transmet un quart de l'énergie de l'onde incidente. Par conséquent, seulement 75 % de l'énergie sont transmis à l'extrémité de la ligne, par exemple vers une antenne ou une résistance de perte (c'est-à-dire non réfléchie).
</tip>

[question:EG401]
[question:EG402]
[question:EG403]

<indepth>
Démonstration de la formule de puissance du ROS utilisée ici, basée sur le recueil de formules de l'OFCOM.

On peut également utiliser directement la formule ci-dessus. Il n'est pas nécessaire de comprendre la démonstration ! 😉

1. Base de départ (recueil de formules de l'OFCOM)

Le recueil de formules de l'OFCOM définit le rapport d'ondes stationnaires (ROS, s) et le coefficient de réflexion (|r|) par les deux équations suivantes :

s = (1 + |r|) / (1 − |r|)

|r| = √P<sub>r</sub> / √P<sub>d</sub>

---

2. Démonstration

Pour simplifier la fraction pour s et remplacer |r|, on multiplie mentalement chaque terme du numérateur et du dénominateur par √P<sub>d</sub>. Le dénominateur de |r| se simplifie alors immédiatement :

1. Le 1 devient :
   1 × √P<sub>d</sub> = √P<sub>d</sub>
2. Le |r| devient :
   (√P<sub>r</sub> / √P<sub>d</sub>) × √P<sub>d</sub> = √P<sub>r</sub>

En substituant ces termes directement dans l'équation du ROS, on obtient immédiatement :

s = (√P<sub>d</sub> + √P<sub>r</sub>) / (√P<sub>d</sub> − √P<sub>r</sub>)

---

3. Adaptation à la notation utilisée ici

En remplaçant les noms des variables (s → ROS et P<sub>d</sub> → P<sub>V</sub> pour la puissance incidente), on obtient exactement la formule cible :

ROS = (√P<sub>V</sub> + √P<sub>R</sub>) / (√P<sub>V</sub> − √P<sub>R</sub>)