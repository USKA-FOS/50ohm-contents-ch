Pourquoi existe-t-il un réseau de **tension alternative** de $\qty{230}{\volt}$ ? La tension alternative offre un avantage décisif par rapport à la tension continue : elle peut être facilement convertie en d'autres valeurs de tension à l'aide de transformateurs, avec de faibles pertes. Cela permet une adaptation efficace de la tension pour la transmission et l'utilisation.

En raison de l'auto-induction dans les bobines, l'énergie peut être transmise entre deux bobines en courant alternatif, comme illustré dans la figure [ref:e_netztrafo]. Cela donne naissance à un nouveau composant : le *transmetteur* ou *transformateur*, appelé plus simplement *trafo*. Il est constitué de deux bobines couplées magnétiquement par un noyau en fer ou en ferrite. Pour distinguer les deux côtés, on parle de côté **primaire** avec un nombre de spires $N_P$ et de côté secondaire avec un nombre de spires $N_S$.

<margin>
[picture:1017:e_netztrafo:Schéma de principe du transformateur]
</margin>

<margin>
[photo:239:e_Trafo mit getrennten Wicklungen:Transformateur avec enroulements séparés]
</margin>

Un transformateur sert à convertir une tension alternative élevée, par exemple $\qty{230}{\volt}$, en une tension alternative plus basse, par exemple $\qty{13,8}{\volt}$. Un transformateur ne peut transmettre que des tensions alternatives. Si l'on applique par erreur une tension continue à un transformateur, celui-ci agit, en raison de la faible résistance ohmique de l'enroulement primaire, comme un court-circuit. Le transformateur peut alors surchauffer fortement et, dans le pire des cas, brûler.

---

Le **rapport de transformation** d'un transformateur peut être exprimé comme suit :

$r = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Le rapport des nombres de spires correspond donc au rapport des tensions. En réarrangeant cette équation de base, on peut calculer les tensions $U$ ainsi que les nombres de spires $N$ du côté primaire ou secondaire.

<indepth>
Ces relations s'appliquent dans le cas idéal d'un transformateur non chargé, c'est-à-dire en circuit ouvert. Le circuit ouvert signifie qu'aucune charge n'est connectée au côté secondaire.
</indepth>

[question:EC401]

Calculons :

$\begin{align*}r = \frac{15}{1} = 15 &= \frac{\qty{230}{\volt}}{U_S} &\quad\quad\quad &|~\cdot~U_S\\[1.5ex]15 \cdot U_S &= \qty{230}{\volt} &\quad\quad\quad &|~:~15\\[1.5ex]U_S &= \frac{\qty{230}{\volt}}{15} = \qty{15,33}{\volt}\end{align*}$

[question:EC402]

Nous constatons d'abord que $N_P = 5\cdot N_S$ et que $U_P = \qty{230}{\volt}$ est donné. On cherche à nouveau la tension $U_S$.

$r = \frac{5\cdot N_S}{N_S} = \frac{\qty{230}{\volt}}{U_S}$ 

Les $N_S$ s'annulent, il reste :

$r = 5 = \frac{\qty{230}{\volt}}{U_S}$ 

Nous multiplions des deux côtés par $U_S$ et divisons des deux côtés par 5.

$U_S = \frac{\qty{230}{\volt}}{5}$ 

Dans la question suivante, on cherche le nombre de spires secondaires.

[question:EC403]

On donne $N_P=600$, $U_P=\qty{230}{\volt}$ et $U_S=\qty{11,5}{\volt}$. On cherche le nombre de spires secondaires $N_S$.

$\frac{600}{N_S} = \frac{\qty{230}{\volt}}{\qty{11,5}{\volt}}$ 

Cela se simplifie en :

$\frac{600}{N_S} = 20$ 

Nous multiplions des deux côtés par $N_S$ et divisons des deux côtés par $20$.

$N_S = \frac{600}{20} = 30$

Le transformateur suivant élève la **tension de sortie** $U_S$, c'est pourquoi le nombre de spires secondaires doit être supérieur à celui du côté primaire.

[question:EC404]

On donne $N_P= 150$, $U_P=\qty{45}{\volt}$ et $U_S=\qty{180}{\volt}$. On cherche $N_S$.

Nous insérons :

$ \frac{150}{N_S} = \frac{\qty{45}{\volt}}{\qty{180}{\volt}}$

Cela se simplifie en :

$ \frac{150}{N_S} =0,25 $

Nous multiplions à nouveau des deux côtés par $N_S$ et divisons des deux côtés par $0,25$.

$ N_S= \frac{150}{0,25} = 600$