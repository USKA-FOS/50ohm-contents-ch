Dans la section [sec:uebertrager_1], nous avons déjà appris les bases du transformateur. Il est constitué de deux bobines couplées magnétiquement via un noyau en fer ou en ferrite. Pour distinguer les côtés, on parle du côté primaire avec le nombre de spires $N_P$ et du côté secondaire avec le nombre de spires $N_S$.

Le principe du transformateur repose sur un effet physique fondamental : l'induction électromagnétique. Si le champ magnétique dans une bobine change – comme c'est le cas lorsqu'une tension alternative est appliquée – une tension électrique est induite dans une bobine voisine couplée magnétiquement. Selon la loi d'induction, cette tension est orientée de manière à s'opposer à la cause de sa formation. On parle donc aussi de *contre-induction*.

[question:AC301]

Dans la section [sec:uebertrager_1], nous avons déjà appris la formule du rapport de transformation $r$ :

$r = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Pour les courants, la relation est inversée :

$r = \frac{N_P}{N_S} = \frac{I_S}{I_P} = \frac{U_P}{U_S}$

Avec cette formule, que l'on trouve également dans le recueil de formules, la question suivante peut être résolue :

[question:AC302]

---

Puisque les conducteurs parcourus par un courant ne doivent pas être excessivement chauffés, pour éviter des dommages à l'isolation ou même un rougissement du conducteur, une certaine intensité de courant maximale ne doit pas être dépassée en fonction de la section du conducteur. Si l'on rapporte l'intensité du courant à la section du conducteur en $\unit{\milli\meter\squared}$, on obtient la densité de courant $S$. Pour les transformateurs, selon les normes applicables, une densité de courant maximale d'environ $\qty{2,5}{\ampere\per\milli\meter\squared}$ ne devrait pas être dépassée.

La formule de calcul est (voir recueil de formules - mot-clé : capacité de charge des enroulements) :

$I = S \cdot A_\mathrm{Dr}$

<unit>
Densité de courant $S = \frac{I}{A} $ en  $\unit{\ampere\per\milli\meter\squared}$
</unit>

<law>
La norme d'installation basse tension SN 411000 (NIN) régit les installations électriques en Suisse jusqu'à 1000 V AC ou 1500 V DC et sert à protéger les personnes, les animaux et les biens. Elle est basée sur l'Ordonnance sur les installations basse tension (OIBT) et les normes internationales de l'IEC et du Cenelec.

Pour les conducteurs en cuivre posés librement, l'intensité de courant maximale admissible est fixée à :

- $\qty{6}{\ampere}$ pour une section de $\qty{0,75}{\milli\meter\squared}$.

- $\qty{10}{\ampere}$ pour une section de $\qty{1.00}{\milli\meter\squared}$.

température ambiante max. : 30°C

Conducteurs regroupés sous une gaine de protection

Source : Conducteur en cuivre - Dimensionnement selon NIN 2000
</law>

<attention>
Il est expressément rappelé ici qu'une concession de radioamateurisme **n'autorise pas** la réalisation d'installations basse tension.
</attention>

Essayez maintenant de répondre à la question suivante. Pour cela, vous avez besoin de la formule pour la section d'un conducteur et de la formule pour la capacité de charge des enroulements. Veillez à convertir correctement les unités.

[question:AC307]

---

L'un des domaines d'application les plus importants des transformateurs en technique haute fréquence est l'**adaptation d'impédance**. Ici, les transformateurs sont utilisés comme transformateurs d'adaptation.

Contrairement aux transformateurs de réseau, le noyau de tels transformateurs n'est généralement pas en fer massif, mais en poudre de fer pressée ou en ferrite. Ces matériaux sont mieux adaptés aux hautes fréquences et réduisent les pertes.

<indepth>
Par *adaptation*, on entend que l'impédance d'une source (par exemple, d'un émetteur) correspond le plus précisément possible à l'impédance de la charge (par exemple, d'une antenne). Ce n'est qu'avec une bonne adaptation que la puissance peut être transmise de manière optimale, sans qu'une partie de l'énergie soit réfléchie.
</indepth>

Un transformateur d'adaptation a donc pour tâche de transformer une impédance donnée en une autre, de sorte que la source et la charge correspondent le mieux possible.

---

Dans le recueil de formules, nous trouvons la formule pour le rapport de transformation $r$ :

$r = \sqrt{\frac{Z_p}{Z_s}} = \frac{N_p}{N_s} = \frac{U_p}{U_s}$

En élevant au carré les deux côtés de l'équation, on obtient :

$r^2 = \frac {Z_p}{Z_s} = \left(\frac{N_p}{N_s}\right)^2 = \left(\frac{U_p}{U_s}\right)^2$

On voit ainsi que le rapport d'impédance est le carré du rapport de tension et donc aussi le carré du rapport du nombre de spires. Ou, inversement, un certain rapport de spires conduit à un rapport d'impédance quadratiquement plus élevé.

<indepth>
Dérivation de la formule pour le transfert d'impédance :
$ P_p = P_s$
$U_p \cdot I_p = U_s \cdot I_s$
Remplacer $U$ par la loi d'Ohm : $U = I \cdot R$ ;
$R$ est remplacé par $Z$
$(I_p \cdot Z_p) \cdot I_p = (I_s \cdot Z_s) \cdot I_s$
Former le rapport d'impédance d'un côté :
$ \frac{Z_p}{Z_s} = \frac{{I_s}^2}{{I_p}^2} = r^2$
Alternativement, remplacer $I$ par la loi d'Ohm :
$I = \frac{U}{R}$
$R$ est remplacé par $Z$
$\frac{U_p}{Z_p} \cdot U_p  = \frac{U_s}{Z_s} \cdot U_s$
Former le rapport d'impédance d'un côté :
$ \frac{Z_p}{Z_s} = \frac{{U_p}^2}{{U_s}^2} = r^2$
</indepth>

---

Prenons comme exemple une antenne alimentée à l'extrémité, que nous étudierons plus en détail dans un chapitre ultérieur. Son impédance d'entrée est d'environ $\qty{2450}{\ohm}$ et présente donc une impédance nettement élevée. Elle doit être adaptée à un émetteur avec une impédance de charge de $\qty{50}{\ohm}$.

<margin>
[picture:260:a_endgespeiste_antenne:Antenne alimentée à l'extrémité avec adaptation d'impédance par un transformateur]
</margin>

Pour le transfert d'impédance de $\qty{50}{\ohm}$ à $\qty{2450}{\ohm}$, le rapport $Z_p:Z_s = \qty{50}{\ohm}:\qty{2450}{\ohm} = 1:49$. Cela signifie $r^2 = 1:49$ et donc $r=\sqrt{1}:\sqrt{49}=1:7$. Cela signifie que le côté primaire ne doit avoir qu'un septième des spires du côté secondaire pour que l'adaptation d'impédance réussisse, par exemple $N_p=1$ et $N_s=7$. En pratique, un rapport de spires de $2:14$ est généralement utilisé (cf. figure [ref:a_unun]).

<margin>
[photo:332:a_unun:Exemple d'un transformateur Unun avec un rapport de spires de 2 à 14, où le côté primaire et le côté secondaire sont enroulés ensemble de manière bifilaire (torsadée)]
</margin>

L'exercice suivant correspond essentiellement à l'exemple précédemment considéré. Pour un dipôle alimenté à l'extrémité, une impédance d'entrée d'environ $\qty{2,5}{\kilo\ohm}$ est indiquée ici. En pratique, cette valeur varie cependant, en fonction de l'environnement et de la structure, typiquement dans la plage d'environ $\qty{2}{\kilo\ohm}$ à $\qty{3}{\kilo\ohm}$.
Avec un rapport de spires d'environ $1:7$, on peut néanmoins généralement obtenir une adaptation suffisamment bonne à $\qty{50}{\ohm}$.

[question:AC306]

Essayez maintenant de résoudre les questions suivantes par vous-même avec vos connaissances.

[question:AC305]
[question:AC303]
[question:AC304]
