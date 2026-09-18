Une ligne de Lecher, dite aussi *ligne de mesure*, est composée de deux conducteurs parallèles sur lesquels, par superposition d’une onde incidente et d’une onde **réfléchie**, s’établissent des ondes stationnaires HF. Elle peut être terminée soit en circuit ouvert (cf. figure [ref:a_lecherleitung_offen]), soit en court-circuit (cf. figure [ref:a_lecherleitung_kurzgeschlossen]). Dans les deux cas, il se forme des distributions caractéristiques de courant et de tension, qui peuvent par exemple servir à déterminer la longueur d’onde λ.

<margin>
[picture:1112:a_lecherleitung_offen:Ligne de Lecher avec extrémité ouverte]
</margin>

Dans le cas d’une ligne de Lecher terminée en circuit ouvert, aucun courant ne peut circuler à l’extrémité de la ligne. On y observe donc un minimum de courant et simultanément un maximum de tension. D’après la loi d’Ohm

$R=\frac{U}{I}$

il s’ensuit qu’à cet endroit, le rapport tension/courant devient idéalement infini, soit $R=\infty$. Le courant et la tension sont décalés spatialement l’un par rapport à l’autre de $\frac{\lambda}{4}$ le long de la ligne. À une distance de $\frac{\lambda}{4}$ de l’extrémité ouverte de la ligne, on trouve donc un maximum de courant et simultanément un minimum de tension. Comme la tension y tend idéalement vers zéro, la loi d’Ohm donne alors $R=0$. Après chaque intervalle supplémentaire de $\frac{\lambda}{4}$, les maxima de courant et de tension alternent. Après une distance de $\frac{\lambda}{2}$, la distribution du courant et de la tension est identique à celle représentée dans la figure [ref:a_lecherleitung_offen].

---

Dans le cas d’une ligne de Lecher terminée par un court-circuit, les deux conducteurs ne peuvent présenter de différence de tension à l’extrémité de la ligne. On a donc $U=0$ à cet endroit. Il s’y trouve un minimum de tension et simultanément un maximum de courant. Avec $R=\frac{U}{I}$, on obtient idéalement $R=0$. À une distance de $\frac{\lambda}{4}$ du court-circuit, on trouve en revanche un maximum de tension et simultanément un minimum de courant. Comme le courant y tend idéalement vers zéro, le rapport $\frac{U}{I}$ devient très grand et l’on a idéalement $R=\infty$. Ici aussi, les maxima de courant et de tension alternent tous les $\frac{\lambda}{4}$. Après une distance de $\frac{\lambda}{2}$, la distribution du courant et de la tension est identique à celle représentée dans la figure [ref:a_lecherleitung_kurzgeschlossen].

<margin>
[picture:1111:a_lecherleitung_kurzgeschlossen:Ligne de Lecher avec extrémité en court-circuit]
</margin>

La fréquence qui s’établit en résonance sur une ligne de Lecher dépend principalement de sa longueur. Si la longueur de la ligne change, la fréquence de résonance change également.

[question:AG320]

Pour une longueur de ligne de $\frac{\lambda}{2}$, la distribution du courant et de la tension se répète intégralement. Une impédance de charge placée à l’extrémité de la ligne apparaît donc à l’entrée de la ligne avec la même valeur.

Un cas particulier important se produit lorsque la ligne de Lecher possède, à la fréquence considérée, une longueur électrique exactement égale à $\frac{\lambda}{4}$. Comme nous l’avons vu dans les distributions de courant et de tension, un maximum de courant et un maximum de tension s’échangent sur une distance de $\frac{\lambda}{4}$. Cela permet de transformer une impédance élevée en une impédance faible et vice versa.

Dans le cas d’une ligne de $\frac{\lambda}{4}$ terminée en circuit ouvert, l’impédance à l’extrémité de la ligne est idéalement infinie. Après une distance de $\frac{\lambda}{4}$, on trouve à l’entrée de la ligne un minimum de tension et un maximum de courant. L’impédance d’entrée est donc quasi nulle ($Z_\mathrm{in} \approx \qty{0}{\ohm}$). Une extrémité de ligne ouverte est donc transformée approximativement en un court-circuit par une ligne de $\frac{\lambda}{4}$.

---

[question:AG411]

Inversement, une ligne terminée par un court-circuit possède à son extrémité une impédance de $\qty{0}{\ohm}$. Après une distance de $\frac{\lambda}{4}$, on trouve à l’entrée de la ligne un maximum de tension et un minimum de courant. L’impédance d’entrée y devient donc très grande ($Z_\mathrm{in} \rightarrow \infty$). Un court-circuit à l’extrémité de la ligne est ainsi transformé approximativement en un circuit ouvert par une ligne de $\frac{\lambda}{4}$.

<indepth>
Le comportement d’une ligne de $\frac{\lambda}{4}$ peut aussi être comparé à celui de circuits résonants. Une ligne de $\frac{\lambda}{4}$ ouverte possède à son entrée une impédance très faible et se comporte alors de manière similaire à un *circuit résonant série* en résonance. Une ligne de $\frac{\lambda}{4}$ en court-circuit possède en revanche à son entrée une impédance très élevée et se comporte de manière similaire à un *circuit résonant parallèle* en résonance.
</indepth>

Dans la section suivante, nous examinerons comment réaliser des transformations d’impédance ciblées à l’aide de lignes de $\frac{\lambda}{4}$.