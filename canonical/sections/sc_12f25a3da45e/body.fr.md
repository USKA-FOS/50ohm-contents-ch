Un composant très important et fréquemment utilisé dans la technologie radio et l'électronique est le condensateur. Comme le montre la figure [ref:e_kondensator_aufbau], un condensateur est principalement constitué de deux surfaces conductrices (plaques, couches ou électrodes) séparées par un isolant appelé diélectrique.


<margin>
[picture:922:e_kondensator_aufbau:Structure d'un condensateur]
</margin>

Les dimensions géométriques déterminent une propriété importante d'un condensateur, à savoir la capacité à stocker des charges. Cette capacité est désignée par le terme capacité et le symbole $C$ est utilisé pour la représenter. Plus la capacité est grande, plus de charges électriques $Q$ peuvent être stockées. Si la tension appliquée est augmentée, plus de charges sont également stockées.

La formule suivante montre la relation. 

$Q = C \cdot U $ 

Cette formule ne figure pas dans le recueil de formules et n'est pas non plus nécessaire pour l'examen.

<unit>
L'unité de la charge $Q$ est $\unit{\ampere\second}$
</unit>

<unit>
L'unité de la capacité $C$ est $\unit{\ampere\second\per\volt}$ ou brièvement *farad* $\unit{\farad}$ en l'honneur du chercheur anglais Michael Faraday (1791 - 1867). $\qty{1}{\farad}$ est la capacité d'un condensateur dans lequel une charge de $\qty{1}{\ampere\second}$ est stockée à une tension de $\qty{1}{\volt}$.
</unit>

[question:EA101]

Lorsque une tension est appliquée à un condensateur, un champ électrique $E$ se forme entre les plaques conductrices. Nous avons déjà appris ce lien dans le chapitre sur le champ électrique : plus la tension appliquée est élevée et plus la distance entre les plaques est petite, plus le champ électrique est intense. Cela peut s'exprimer mathématiquement par :

$E = \frac{U}{d}$

Pour calculer la capacité du condensateur à partir des dimensions, on utilise la formule suivante du recueil de formules :

---

$C = \frac{\varepsilon_0 \cdot \varepsilon_r \cdot A}{d}$

Dans ce qui suit, les différentes grandeurs de la formule sont détaillées :

- $A$ est la surface opposée des plaques conductrices
- $d$ est la distance entre les surfaces
- $\varepsilon_0 = \qty{0,855e-11}{\ampere\second\per\volt\meter}$ est la permittivité du vide, une constante naturelle
- $\varepsilon_r$ (prononcé : "Epsilon R") est une propriété spéciale de l'isolant (diélectrique) appelée permittivité relative qui dépend du matériau utilisé. Le tableau [ref:e_Dielektrizitätszahl] avec les valeurs des matériaux se trouve également dans le recueil de formules.

<margin>
| Matériau | $\varepsilon_r$  |
| Air (sec) | 1,00059 |
| Polyéthylène (PE) | 2,29 |
| Mousse de PE | 1,5 |
| PTFE (Teflon) | 2,0 |
[table:e_Dielektrizitätszahl:Permittivité relative $\varepsilon_r$ ]
</margin>

Grâce à la formule, on peut déjà résoudre un certain nombre de questions d'examen. On constate tout d'abord que la tension $U$ ne figure pas dans la formule. 

[question:EC205]

La capacité d'un condensateur diminue lorsque la distance entre les plaques augmente. 

[question:EC204]
[question:EC203]

---

Examinons d'abord le condensateur dans le cas du courant continu. La figure [ref:e_stromkreis_kondensator] montre un circuit pour charger un condensateur. On suppose que le condensateur $C$ est initialement déchargé, c'est-à-dire qu'il ne stocke encore aucune charge électrique. Lorsque l'interrupteur est fermé, le condensateur $C$ est connecté à une source de tension continue (batterie) via une résistance $R$.

La tension appliquée crée un champ électrique entre les plaques du condensateur. Ce champ provoque un réarrangement des charges : les électrons sont poussés du pôle négatif de la source de tension vers la plaque de condensateur connectée, de sorte qu'un excès d'électrons s'y forme. Simultanément, les électrons sont retirés de la plaque opposée vers le pôle positif de la source de tension, ce qui entraîne un déficit d'électrons. Bien qu'aucun courant ne circule à travers le diélectrique, cette séparation des charges conduit à la charge du condensateur. 

<margin>
[picture:1015:e_stromkreis_kondensator:Circuit de charge d'un condensateur]
</margin>

---

Cela signifie qu'au début, un courant élevé circule, qui est limité uniquement par la résistance $R$. Avec le temps, de plus en plus de charges sont stockées dans le condensateur. Le courant diminue ainsi en continu, tandis que la tension $U_C$ aux bornes du condensateur augmente, jusqu'à ce que celui-ci soit complètement chargé. À cet état, aucun courant ne circule plus.

Ce processus ne se produit pas instantanément, mais de manière retardée dans le temps. La tension du condensateur augmente selon une fonction exponentielle, comme le montre la figure [ref:e_ladekurve_c]. La durée de ce processus de charge dépend de la résistance en amont : plus la résistance est grande, plus il faut de temps pour que le condensateur soit "complètement" chargé. Avec un oscilloscope, comme le montre la figure [ref:e_lade_entladespannung_mit_oszilloskop], que nous avons déjà rencontré, on peut observer et examiner de manière illustrative cette évolution dans le temps.

<margin>
[picture:185:e_ladekurve_c:Tension de charge d'un condensateur]
</margin>

<margin>
[photo:247:e_lade_entladespannung_mit_oszilloskop:Tension de charge et de décharge d'un condensateur]  
</margin>
 
Lors du processus de décharge, le courant circule dans le sens inverse du courant de charge et la tension aux bornes du condensateur diminue lentement.

[question:EC201]

Dans le cas du courant alternatif et des tensions alternatives, nous devons prendre en compte un autre aspect important : un condensateur se comporte comme une résistance dépendante de la fréquence. Celle-ci peut être décrite par la relation

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

et est appelée résistance réactive capacitive $X_C$ (cf. recueil de formules).

Les détails physiques exacts seront abordés en classe A. Pour la classe E, il est cependant déjà important de savoir que la résistance d'un condensateur est inversement proportionnelle à la fréquence : si la fréquence diminue, la résistance réactive capacitive $X_C$ augmente. Si, en revanche, la fréquence augmente, la résistance diminue en conséquence.

[question:EC202]

---

Nous avons maintenant appris quelques propriétés électriques fondamentales d'un condensateur, et nous allons maintenant nous occuper des différentes formes de construction. La figure [ref:e_kondensatorvarianten] montre différentes variantes de condensateurs.

<margin>
[photo:206:e_kondensatorvarianten:Variantes de condensateurs]
</margin>

Différents matériaux peuvent être utilisés comme diélectrique, c'est-à-dire comme couche isolante :

1.  Air dans le cas du condensateur rotatif à air ou du trimmer à air
2. Film plastique dans le cas du condensateur à film bobiné
3. Céramique pour les condensateurs HF à haute qualité et les condensateurs SMD
4. Oxyde métallique dans le cas du condensateur électrolytique.

Selon la construction, on distingue en outre :

* Condensateurs fixes sous forme de condensateurs céramiques, de condensateurs à film et de condensateurs électrolytiques
* Condensateurs variables sous forme de condensateurs rotatifs et de condensateurs de réglage

---

Les *condensateurs à air* et les *condensateurs céramiques*, comme le montre la figure [ref:e_aufbau_keramik_c], sont par exemple utilisés pour les filtres HF. 
[question:ED216] 

<margin>
[picture:923:e_aufbau_keramik_c: Condensateur céramique]
</margin>

Les *condensateurs électrolytiques* (abréviation ELKO) contiennent une fine feuille d'ALU rugueuse, immergée dans un électrolyte (par exemple du borax). L'électrolyte provoque une oxydation chimique de la surface de l'aluminium. La couche d'oxyde formée est très fine et donc la capacité augmente fortement pour une taille réduite. Cependant, la fine couche n'a qu'une résistance limitée à la tension, qui est indiquée sur l'ELKO.
Les condensateurs électrolytiques ne peuvent être utilisés qu'avec une tension continue. La polarité doit donc être respectée, sinon la couche d'oxyde se dégrade et donc la résistance à la tension diminue. Le condensateur est détruit. Tous les autres condensateurs peuvent également être connectés à une tension alternative.
[question:EC207]

%<margin>
%TODO: Image Elko
%</margin>

Pour les condensateurs à film bobiné, des plastiques sont transformés en films extrêmement fins par des procédés spéciaux, munis d'électrodes et ensuite soit enroulés en une bobine, soit assemblés en couches individuelles et assemblés en un condensateur, comme le montre la figure [ref:e_aufbau_wickel_c]. Outre les condensateurs céramiques et les condensateurs électrolytiques, ils font partie des types de condensateurs les plus couramment utilisés.

<margin>
[picture:49:e_aufbau_wickel_c:Condensateur à film bobiné]
</margin>

Les condensateurs rotatifs sont souvent utilisés dans les étages finaux et les réseaux d'adaptation. Chez eux, la capacité peut être ajustée en montant une partie des plaques du condensateur sur un axe isolé et en les faisant tourner entre des plaques fixes. Cela modifie la surface de chevauchement effective des plaques et donc la capacité, comme le montre la figure [ref:e_drehkondensator]. Les condensateurs de réglage fonctionnent selon un principe similaire, mais ne sont pas prévus pour un réglage régulier. Ils servent plutôt à l'ajustement ponctuel ou occasionnel des circuits, par exemple lors de la mise en service ou de l'étalonnage.

[question:EC206]

<margin>
 [picture:840:e_drehkondensator:Structure d'un condensateur rotatif]
</margin>

Les symboles de circuit utilisés pour les différents condensateurs diffèrent également comme le montre la figure [ref:e_kondensator_schaltzeichen].

<margin>
[picture:924:e_kondensator_schaltzeichen:Symboles de circuit de différents types de condensateurs]

Attribution des symboles de circuit : 
a) Condensateur fixe 
b) Condensateur polarisé/ Condensateur électrolytique (Elko)/Condensateur à tantale
c) Condensateur rotatif (Drehko) 
d) Condensateur de réglage à des fins d'ajustement
</margin>
