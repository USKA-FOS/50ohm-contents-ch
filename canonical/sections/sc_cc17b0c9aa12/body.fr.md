[question:AC401]

La diode à jonction (pn) est composée de deux zones semi-conductrices qui, par le processus de dopage, présentent soit un excès d’électrons libres (n), soit de trous libres (p). De part et d’autre de l’interface se forme une zone de charge d’espace, appelée zone de déplétion, qui ne contient pratiquement pas de porteurs de charge libres. La zone n constitue la cathode, la zone p l’anode.

Si la diode est soumise à une tension directe (positive à l’anode, négative à la cathode), les électrons du côté n se déplacent vers la zone p, et les trous du côté p vers la zone n. C’est ainsi que la bonne réponse est obtenue.

Il peut être déroutant de constater que le sens conventionnel du courant est opposé au sens du flux d’électrons. La flèche de courant indique donc un sens allant de l’anode vers la cathode, bien que le flux d’électrons aille de la cathode vers l’anode.

[question:AC403]

Les diodes à jonction présentent une dépendance exponentielle du courant de diode en fonction de la tension aux bornes de la diode. Le courant de saturation augmente avec la température. Cela a pour effet que la tension nécessaire pour un courant de diode donné diminue lorsque la température augmente. La « tension directe » diminue donc (en règle empirique d’environ $\qty{-2}{\milli\volt\per\kelvin}$ d’élévation de température).
<indepth>

Le courant de diode est donné par :

$I_D(T) = I_S(T) \cdot e^{\frac{U_D}{U_T}}$

$I_S$ est le courant de saturation, $U_T = k T/q$ la tension thermique. Ici, $k$ est la constante de Boltzmann, $q$ la charge élémentaire.

Avec l’augmentation de la température, le courant de saturation augmente et la fonction exponentielle diminue. Cependant, c’est la dépendance en température du courant de saturation qui l’emporte.

</indepth>

[question:AC404]

---

La diode à capacité variable (voir figure [ref:a_diode_kapazitaet]) utilise la capacité entre les zones n et p à travers la zone de déplétion, de manière analogue à un condensateur à plaques. Cependant, aucun courant continu notable ne doit circuler, donc la diode doit être polarisée en polarisation inverse.

<margin>
[picture:1068:a_diode_kapazitaet:Symbole de circuit de la diode à capacité variable]
</margin>

Plus la tension aux bornes de la diode est négative (ou plus la tension inverse est élevée), plus la zone de déplétion s’étend et plus la capacité de la diode diminue.

Dans les questions AC405 et AC406, des *diodes antiparallèles* sont utilisées pour limiter l’amplitude d’une tension alternative. De tels circuits sont par exemple employés pour protéger les entrées de récepteurs contre des tensions susceptibles de détruire les transistors d’entrée.

[question:AC405]

Il s’agit ici de diodes en silicium, qui présentent une tension de seuil d’environ $\qty{0,6}{\volt}$. Si la tension d’entrée dépasse $\qty{0,6}{\volt}$, la diode de droite devient passante. Si elle descend en dessous de $\qty{-0,6}{\volt}$, la diode de gauche devient passante.

Lors du premier demi-cycle, la tension nécessaire n’est pas encore atteinte, il est donc transmis sans modification. Les deux demi-cycles suivants, en revanche, ont des amplitudes dépassant la tension de seuil. Les amplitudes sont « écrêtées » à $\qty{\pm 0,6}{\volt}$.

[question:AC406]

La solution suit le même principe que dans la question précédente, mais les diodes utilisées ici sont des *diodes en germanium*, dont la tension de seuil est d’environ $\qty{0,3}{\volt}$. Par conséquent, tous les demi-cycles sont écrêtés.

[question:AC407]

Les composants suivants interagissent avec la lumière : la photorésistance et la photodiode.

La photorésistance est un composant doté de deux contacts non bloquants. Elle se comporte comme une résistance ohmique classique – le courant augmente linéairement avec la tension appliquée. Sa valeur résistive peut être réduite par l’absorption de lumière : les photons absorbés augmentent la densité des porteurs de charge libres. Si aucune tension n’est appliquée, aucun courant ne circule.

---

La photodiode, en revanche, est une diode à jonction (voir figure [ref:a_photodiode]). Ici, la lumière est absorbée dans la zone de déplétion, où elle génère des paires électron-trou qui sont séparées par le champ électrique de cette zone. Ce champ existe même sans polarisation externe. Un courant (courant de court-circuit) circule même pour $U_D=0$. Ce courant circule dans le sens opposé au courant conventionnel de la diode.

<margin>
[picture:1069:a_photodiode:Symbole de circuit de la photodiode]
</margin>

---

[question:AC408]

Les optocoupleurs combinent une diode électroluminescente et une photodiode dans un même boîtier, l’entrée (diode électroluminescente) et la sortie (photodiode) étant isolées l’une de l’autre (séparation galvanique).

Ces composants sont utilisés pour isoler galvaniquement des interfaces, par exemple pour éviter les boucles de masse responsables de ronflements du secteur induits.

<margin>
[picture:1070:a_optokoppler:Symbole de circuit de l'opto-coupleur]
</margin>