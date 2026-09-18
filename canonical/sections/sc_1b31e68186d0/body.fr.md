Dans la classe E, nous avons déjà appris les bases du transformateur. Il se compose de deux bobines couplées magnétiquement par un noyau en fer ou en ferrite. Pour distinguer les deux côtés, on parle de côté primaire avec le nombre de spires $N_P$ et de côté secondaire avec le nombre de spires $N_S$.

Le principe du transformateur repose sur un effet physique fondamental : l'induction électromagnétique. Si le champ magnétique dans une bobine change – ce qui se produit lorsqu'une tension alternative est appliquée – une tension électrique est induite dans une bobine voisine couplée magnétiquement. Selon la loi de l'induction, cette tension est orientée de manière à s'opposer à la cause de sa formation. On parle donc aussi d'*induction mutuelle*.

[question:AC301]

Dans la classe E, nous avons déjà vu la formule du rapport de transformation $ü$ :

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Pour les intensités de courant, la relation inverse s'applique :

$ü = \frac{N_P}{N_S} = \frac{I_S}{I_P} = \frac{U_P}{U_S}$

Avec cette formule, également disponible dans le recueil de formules, la question suivante peut être résolue :

[question:AC302]

---

Comme les conducteurs parcourus par un courant ne doivent pas s'échauffer excessivement pour éviter d'endommager l'isolation ou même de faire rougir le conducteur, une intensité de courant maximale ne doit pas être dépassée en fonction de la section du conducteur. Si l'on met en relation l'intensité du courant avec la section du conducteur en $\unit{\milli\meter\squared}$, on obtient la densité de courant $S$. Pour les transformateurs, selon les normes en vigueur, une densité de courant maximale d'environ $\qty{2,5}{\ampere\per\milli\meter\squared}$ ne doit pas être dépassée.

La formule de calcul est la suivante (voir recueil de formules – mot-clé : capacité de charge des enroulements) :

$I = S \cdot A_\mathrm{Dr}$

<unit>
Densité de courant $S = \frac{I}{A} $ en $\unit{\ampere\per\milli\meter\squared}$
</unit>

<indepth>
Selon la VDE, pour les conducteurs en cuivre posés librement, l'intensité de courant maximale admissible est fixée à $\qty{12}{\ampere}$ pour une section de $\qty{0,75}{\milli\meter\squared}$. Pour les fusibles, la densité de courant peut atteindre jusqu'à $\qty{3000}{\ampere\per\milli\meter\squared}$.
</indepth>

Essayez maintenant de répondre à la question suivante. Pour cela, vous aurez besoin de la formule de la section d'un conducteur et de la formule de la capacité de charge des enroulements. Veillez à convertir correctement les unités.

[question:AC307]

---

L'un des domaines d'application les plus importants des transformateurs en haute fréquence est l'**adaptation d'impédance**. Dans ce cas, les transformateurs sont utilisés comme transformateurs d'adaptation.

Contrairement aux transformateurs de réseau, le noyau de ces transformateurs n'est généralement pas en fer massif, mais en poudre de fer comprimée ou en ferrite. Ces matériaux sont mieux adaptés aux hautes fréquences et réduisent les pertes.

<indepth>
Par *adaptation*, on entend que l'impédance d'une source (par exemple, un émetteur) est adaptée le plus précisément possible à l'impédance de la charge (par exemple, une antenne). Seule une bonne adaptation permet de transmettre la puissance de manière optimale sans qu'une partie de l'énergie ne soit réfléchie.
</indepth>

Un transformateur d'adaptation a donc pour tâche de convertir une impédance donnée en une autre, de sorte que la source et la charge s'adaptent au mieux l'une à l'autre.

---

Dans le recueil de formules, nous trouvons la formule du rapport de transformation $ü$ :

$ü = \sqrt{\frac{Z_p}{Z_s}} = \frac{N_p}{N_s} = \frac{U_p}{U_s}$

Si l'on élève les deux côtés de l'équation au carré, on obtient :

$ü^2 = \frac {Z_p}{Z_s} = \left(\frac{N_p}{N_s}\right)^2 = \left(\frac{U_p}{U_s}\right)^2$

On voit ainsi que le rapport d'impédance est le carré du rapport de tension et donc aussi le carré du rapport du nombre de spires. Autrement dit, un rapport de spires donné conduit à un rapport d'impédance quadratique plus élevé.

<indepth>
Dérivation de la formule de transmission d'impédance :
$ P_p = P_s$
$U_p \cdot I_p = U_s \cdot I_s$
Remplacer $U$ par la loi d'Ohm : $U = I \cdot R$ ;
$R$ est remplacé par $Z$
$(I_p \cdot Z_p) \cdot I_p = (I_s \cdot Z_s) \cdot I_s$
Former le rapport d'impédance d'un côté :
$ \frac{Z_p}{Z_s} = \frac{{I_s}^2}{{I_p}^2} = ü^2$
Alternativement, remplacer $I$ par la loi d'Ohm :
$I = \frac{U}{R}$
$R$ est remplacé par $Z$
$\frac{U_p}{Z_p} \cdot U_p  = \frac{U_s}{Z_s} \cdot U_s$
Former le rapport d'impédance d'un côté :
$ \frac{Z_p}{Z_s} = \frac{{U_p}^2}{{U_s}^2} = ü^2$
</indepth>

---

Prenons comme exemple une antenne alimentée en bout, que nous étudierons plus en détail dans un chapitre ultérieur. Son impédance d'entrée est d'environ $\qty{2450}{\ohm}$ et est donc nettement élevée. Elle doit être adaptée à un émetteur avec une impédance de charge de $\qty{50}{\ohm}$.

<margin>
[picture:260:a_endgespeiste_antenne:Antenne alimentée en bout avec adaptation d'impédance par un transformateur]
</margin>

Pour l'adaptation d'impédance de $\qty{50}{\ohm}$ à $\qty{2450}{\ohm}$, le rapport $Z_p:Z_s = \qty{50}{\ohm}:\qty{2450}{\ohm} = 1:49$. Cela signifie que $ü^2 = 1:49$ et donc $ü=\sqrt{1}:\sqrt{49}=1:7$. Cela signifie que le côté primaire ne doit avoir qu'un septième du nombre de spires du côté secondaire pour que l'adaptation d'impédance fonctionne, par exemple $N_p=1$ et $N_s=7$. En pratique, un rapport de spires de $2:14$ est généralement utilisé (voir figure [ref:a_unun]).

<margin>
[photo:332:a_unun:Exemple d'un transformateur Unun avec un rapport de spires de 2 à 14, où les côtés primaire et secondaire sont bobinés ensemble de manière bifilaire (toronnée)]
</margin>

La tâche suivante correspond essentiellement à l'exemple précédemment examiné. Pour un dipôle alimenté en bout, une impédance d'entrée d'environ $\qty{2,5}{\kilo\ohm}$ est indiquée ici. En pratique, cette valeur varie généralement entre environ $\qty{2}{\kilo\ohm}$ et $\qty{3}{\kilo\ohm}$ en fonction de l'environnement et de la structure. Avec un rapport de spires d'environ $1:7$, une adaptation suffisamment bonne à $\qty{50}{\ohm}$ peut généralement être obtenue.

[question:AC306]

Essayez maintenant de résoudre les questions suivantes par vous-même avec vos connaissances acquises.

[question:AC305]
[question:AC303]
[question:AC304]
