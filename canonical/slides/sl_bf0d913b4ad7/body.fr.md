* Les antennes possèdent une **impédance au point d’alimentation** (ou impédance de pied), qui dépend de la configuration exacte des éléments de l’antenne.
* Si celle-ci ne correspond pas à l’**impédance caractéristique** de la ligne d’alimentation, il se produit une *réflexion*.
* La **puissance d’émission** est renvoyée vers l’**émetteur-récepteur** $\rightarrow$ elle ne peut pas être rayonnée par l’antenne.
* Si l’impédance d’alimentation de l’antenne et l’impédance caractéristique de la ligne d’alimentation coïncident, on parle d’*adaptation*.

---

## Rapport d’ondes stationnaires (ROS)

* Valeur de mesure de la qualité de l’adaptation de l’antenne.
* Indique, de manière simplifiée, quelle part de la **puissance d’émission** est réfléchie par l’antenne.
* Abréviation ROS, issue de l’anglais *standing wave ratio*.
* Mesuré à l’aide d’un **ROS-mètre**.

<note>
Calcul précis : $\text{ROS} = \frac {\sqrt{P_\text{incidente}}+\sqrt{P_\text{réfléchi}}} { \sqrt{P_\text{incidente}}-\sqrt{P_\text{réfléchi}}}$ avec $P_\text{incidente}$ puissance incidente et $P_\text{réfléchi}$ puissance réfléchie — non requis pour l’examen de classe N.
</note>

---

## ROS-mètre


Mesure simultanément la **puissance d’émission** envoyée vers l’antenne et la **puissance réfléchie** renvoyée en retour.

<left>
[photo:144:swr_meter:Un ROS-mètre simple pour déterminer le rapport d’ondes stationnaires]
</left>
<right>
[photo:143:swr_meter_kreuzzeiger:ROS-mètre à aiguilles croisées : l’aiguille de gauche indique la puissance incidente, celle de droite la puissance réfléchie ; pour lire le ROS, suivre la ligne verte au point d’intersection des deux aiguilles vers le bas.]
</right>

---

Il est inséré entre l’**émetteur-récepteur** et l’antenne ou intégré directement dans l’**émetteur-récepteur**.


<left>
[picture:670:n_trx_kabel_swr_antenne:Schéma de principe d’un ROS-mètre entre l’émetteur-récepteur et l’antenne]
</left>
<right>
[photo:67:n_swr_display:Écran d’un émetteur-récepteur]
</right>
<note>
ROS-mètre et S-mètre se ressemblent à l’oreille, mais désignent des fonctions différentes : le ROS-mètre mesure le rapport d’ondes stationnaires à l’émission, le S-mètre mesure l’**intensité du signal** à la réception.
</note>

---
[question:NI201]

---
[question:NF101]

---
[question:NI202]

---
## Bonne adaptation


* En cas d’adaptation parfaite, la valeur $\num{1}$ s’affiche.
* C’est la meilleure valeur possible.
* Toute la **puissance** est absorbée par l’antenne.
* Aucune **puissance** n’est renvoyée vers l’émetteur.

---
[question:NG301]

---
[question:NI203]

---
## Mauvaise adaptation


* En cas de mauvaise adaptation, une valeur proche de l’infini ($\infty$) s’affiche.
* Aucune antenne n’est connectée, la ligne de transmission est coupée ou en court-circuit.
* Mauvaise adaptation de l’antenne ou ligne de transmission endommagée.
* Dans le pire des cas, cela peut endommager l’émetteur.

---

* Pour un ROS de $\num{2}$, $\qty{11}{\percent}$ de la **puissance d’émission** est réfléchie.
* Pour un ROS de $\num{3}$, $\qty{25}{\percent}$ de la **puissance d’émission** est réfléchie.
* Les émetteurs modernes réduisent automatiquement la **puissance d’émission** pour protéger l’émetteur.

---
[question:NG302]

---

[question:NG303]

---
## Forte atténuation du câble


* Réduit le signal réfléchi.
* Fausse la mesure.
* Par exemple, dans le cas d’un câble long.
* Le signal est atténué à l’aller comme au retour.

---
[question:NG208]


<note>
* Le ROS semble s’améliorer, mais seule la **puissance réfléchie** est atténuée.
</note>