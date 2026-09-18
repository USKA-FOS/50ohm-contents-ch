Un composant très important et fréquemment utilisé en radioélectricité et en électronique est le condensateur. Comme illustré dans la figure [ref:e_kondensator_aufbau], un condensateur est constitué en principe de deux surfaces conductrices (plaques, couches ou électrodes) séparées par un isolant – appelé diélectrique.


<margin>
[picture:922:e_kondensator_aufbau:Structure de principe d'un condensateur]
</margin>

Les dimensions géométriques déterminent une propriété essentielle d'un condensateur : sa capacité à stocker des charges électriques. Cette capacité est appelée capacité et est désignée par la lettre $C$. Plus la capacité est élevée, plus le condensateur peut stocker de charges électriques $Q$. Si la tension appliquée augmente, davantage de charges sont stockées.

La formule suivante montre cette relation :

$Q = C \cdot U$

Cette formule ne figure pas dans le recueil de formules et n'est pas nécessaire pour l'examen.

<unit>
L'unité de la charge $Q$ est $\unit{\ampere\second}$
</unit>

<unit>
L'unité de la capacité $C$ est $\unit{\ampere\second\per\volt}$ ou, en abrégé, *farad* $\unit{\farad}$ en l'honneur du physicien anglais Michael Faraday (1791 - 1867). $\qty{1}{\farad}$ est la capacité d'un condensateur dans lequel une charge de $\qty{1}{\ampere\second}$ est stockée sous une tension de $\qty{1}{\volt}$.
</unit>

[question:EA101]

Lorsqu'une tension est appliquée à un condensateur, un champ électrique $E$ se forme entre les plaques conductrices. Nous avons déjà abordé cette relation dans le chapitre sur le champ électrique : plus la tension appliquée est élevée et plus la distance entre les plaques est faible, plus le champ électrique est intense. Mathématiquement, cela s'exprime par :

$E = \frac{U}{d}$

Pour calculer la capacité d'un condensateur à partir de ses dimensions, on utilise la formule suivante, tirée du recueil de formules :

---

$C = \frac{\varepsilon_0 \cdot \varepsilon_r \cdot A}{d}$

Voici l'explication des différentes grandeurs de la formule :

- $A$ est la surface en regard des plaques conductrices
- $d$ est la distance entre les plaques
- $\varepsilon_0 = \qty{0,855e-11}{\ampere\second\per\volt\meter}$ est la permittivité du vide, une constante naturelle
- $\varepsilon_r$ (prononcé « epsilon R ») est une propriété spécifique de l'isolant (diélectrique) appelée permittivité relative, qui dépend du matériau utilisé. Le tableau [ref:e_Dielektrizitätszahl] avec les valeurs des matériaux se trouve également dans le recueil de formules.

<margin>
| Matériau | $\varepsilon_r$ |
| air (sec) | 1,00059 |
| PE plein (polyéthylène) | 2,29 |
| mousse de PE | 1,5 |
| PTFE (Teflon) | 2,0 |
[table:e_Dielektrizitätszahl:Permittivité relative $\varepsilon_r$]
</margin>

À l'aide de cette formule, on peut déjà résoudre un certain nombre de questions d'examen. On constate d'abord que la tension $U$ n'apparaît pas dans la formule.

[question:EC205]

La capacité d'un condensateur diminue lorsque la distance entre les plaques augmente.

[question:EC204]
[question:EC203]

---

Considérons d'abord le condensateur en courant continu. La figure [ref:e_stromkreis_kondensator] montre un circuit pour charger un condensateur. On suppose que le condensateur $C$ est initialement déchargé, c'est-à-dire qu'il n'a pas encore stocké de charge électrique. Lorsque l'interrupteur est fermé, le condensateur $C$ est connecté à une source de tension continue (batterie) via une résistance $R$.

La tension appliquée crée un champ électrique entre les plaques du condensateur. Ce champ provoque une redistribution des charges : des électrons sont repoussés par le pôle négatif de la source de tension vers la plaque du condensateur qui y est connectée, créant ainsi un excès d'électrons sur cette plaque. Simultanément, des électrons sont attirés depuis la plaque opposée vers le pôle positif de la source de tension, créant un déficit d'électrons sur cette plaque. Bien qu'aucun courant ne traverse le diélectrique, cette séparation de charges entraîne la charge du condensateur.

<margin>
[picture:1015:e_stromkreis_kondensator:Circuit de charge d'un condensateur]
</margin>

---

Cela signifie qu'au début, un courant élevé circule, limité uniquement par la résistance $R$. Avec le temps, de plus en plus de charges sont stockées dans le condensateur. Le courant diminue donc continuellement, tandis que la tension $U_C$ aux bornes du condensateur augmente jusqu'à ce qu'il soit complètement chargé. À ce stade, plus aucun courant ne circule.

Cependant, ce processus ne se produit pas instantanément, mais avec un retard temporel. La tension du condensateur augmente alors selon une fonction exponentielle, comme illustré dans la figure [ref:e_ladekurve_c]. La durée de ce processus de charge dépend de la résistance en série : plus la résistance est grande, plus le temps nécessaire pour charger complètement le condensateur est long. Avec un oscilloscope, comme montré dans la figure [ref:e_lade_entladespannung_mit_oszilloskop], que nous avons déjà présenté, on peut observer et étudier visuellement cette évolution temporelle.

<margin>
[picture:185:e_ladekurve_c:Tension de charge d'un condensateur]
</margin>

<margin>
[photo:247:e_lade_entladespannung_mit_oszilloskop:Tension de charge et de décharge d'un condensateur]
</margin>

Lors de la décharge, le courant circule dans le sens inverse de celui de la charge, et la tension aux bornes du condensateur diminue progressivement.

[question:EC201]

Dans le cas du courant alternatif et des tensions alternatives, il faut prendre en compte un autre aspect important : un condensateur se comporte comme une résistance dépendant de la fréquence. Cette résistance peut être décrite par la relation

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

et est appelée réactance capacitive $X_C$ (voir recueil de formules).

Les détails physiques précis seront abordés dans la classe A. Pour la classe E, il est déjà important de savoir que la résistance d'un condensateur est inversement proportionnelle à la fréquence : si l'on diminue la fréquence, la réactance capacitive $X_C$ augmente. Si l'on augmente la fréquence, la résistance diminue en conséquence.

[question:EC202]

---

Nous avons maintenant appris quelques propriétés électriques fondamentales d'un condensateur, et nous allons maintenant nous intéresser aux différentes formes constructives. La figure [ref:e_kondensatorvarianten] montre différentes variantes de condensateurs.

<margin>
[photo:206:e_kondensatorvarianten:Variantes de condensateurs]
</margin>

Différents matériaux peuvent être utilisés comme diélectrique, c'est-à-dire comme couche isolante :

1. L'air dans les condensateurs variables à air ou les trimmers à air
2. Les films plastiques dans les condensateurs à film enroulé
3. La céramique pour les condensateurs HF à haute qualité et les condensateurs CMS
4. Les oxydes métalliques dans les condensateurs électrolytiques.

Selon leur structure, on distingue également :

* Les condensateurs fixes, sous forme de condensateurs céramiques, de condensateurs à film et de condensateurs électrolytiques
* Les condensateurs variables, sous forme de condensateurs variables et de trimmers

---

Les *condensateurs à air* et les *condensateurs céramiques*, comme illustré dans la figure [ref:e_aufbau_keramik_c], sont par exemple souvent utilisés pour les filtres HF. [question:ED216]

<margin>
[picture:923:e_aufbau_keramik_c: Condensateur céramique]
</margin>

Les *condensateurs électrolytiques* (abrégés ELKO) contiennent une fine feuille d'aluminium rugosifiée, immergée dans un électrolyte (par exemple du borax). L'électrolyte provoque une oxydation chimique de la surface de l'aluminium. La couche d'oxyde ainsi formée est très fine, ce qui augmente considérablement la capacité pour une taille réduite. Cependant, cette fine couche n'a qu'une tenue en tension limitée, indiquée sur l'ELKO.

Les condensateurs électrolytiques ne doivent être utilisés qu'en courant continu. La polarité doit être respectée, car sinon la couche d'oxyde se dégrade, ce qui réduit la tenue en tension. Le condensateur est alors détruit. Tous les autres condensateurs peuvent être connectés en courant alternatif.
[question:EC207]

%<margin>
%TODO: Bild Elko
%</margin>

Pour les condensateurs à film enroulé, des plastiques sont transformés en films extrêmement fins selon des procédés spéciaux, pourvus d'électrodes, puis soit enroulés en un bobinage, soit empilés en couches individuelles et assemblés pour former un condensateur, comme illustré dans la figure [ref:e_aufbau_wickel_c]. Outre les condensateurs céramiques et les condensateurs électrolytiques, ils comptent parmi les types de condensateurs les plus couramment utilisés.

<margin>
[picture:49:e_aufbau_wickel_c:Condensateur à film enroulé]
</margin>

Les condensateurs variables sont souvent utilisés dans les étages de puissance et les réseaux d'adaptation. Leur capacité peut être ajustée en montant une partie des plaques du condensateur sur un axe isolé qui tourne entre des plaques fixes. Cela modifie la surface effective de chevauchement des plaques et donc la capacité, comme illustré dans la figure [ref:e_drehkondensator]. Les trimmers fonctionnent selon un principe similaire, mais ne sont pas conçus pour un réglage régulier. Ils servent plutôt à l'ajustement ponctuel ou occasionnel de circuits, par exemple lors de la mise en service ou de l'étalonnage.

[question:EC206]

<margin>
[picture:840:e_drehkondensator:Structure d'un condensateur variable]
</margin>

Les symboles de circuit utilisés pour les différents types de condensateurs diffèrent également, comme illustré dans la figure [ref:e_kondensator_schaltzeichen].

<margin>
[picture:924:e_kondensator_schaltzeichen:Symboles de circuit pour différents types de condensateurs]

Correspondance des symboles :

a) Condensateur fixe
b) Condensateur polarisé / condensateur électrolytique (ELKO) / condensateur au tantale
c) Condensateur variable (drehko)
d) Trimmer pour ajustement
</margin>