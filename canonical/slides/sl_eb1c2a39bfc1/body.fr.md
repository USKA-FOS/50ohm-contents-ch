## Transistor bipolaire


[picture:864:a_bauelemente_bipolartransistor:Symbole de circuit d'un transistor bipolaire npn et pnp avec collecteur (C), base (B) et émetteur (E)]

* Trois zones semi-conductrices
* Alternativement dopées n et p
* Transistor npn et transistor pnp

---
[question:AC503]
---
[question:AC504]
---
### Commande de courant et facteur

* La tension base-émetteur $U_{\textrm{BE}}$ commande le courant de collecteur $I_{\textrm{C}}$ de manière exponentielle
* Dans le transistor bipolaire, un courant de base $I_{\textrm{B}}$ exponentiellement dépendant de $U_{\textrm{BE}}$ circule toujours
* Le facteur $B$ est le *facteur d'amplification de courant* du transistor
* Il est d'environ 20 à 500

<fragment>
$B = \frac{I_{\textrm{C}}}{I_{\textrm{B}}}$
</fragment>

<note>
Un facteur plus élevé nécessite un courant de base plus petit pour commander un courant de collecteur plus grand
</note>
---
[question:AC501]
---
### Transistor bipolaire conducteur

* Un courant de collecteur significatif circule
* La diode base-émetteur est polarisée dans le sens direct
* La diode collecteur-base est bloquée, afin que les porteurs de charge ne passent pas du collecteur à la base

---
[question:AC505]
---
[question:AC515]
---
#### Solution
* La valeur de $R_1$ règle le courant de base $I_B$
* $I_B$ est 298 fois plus petit que $I_C$
* Pour la tension aux bornes de $R_1$, la perte du transistor doit être soustraite

---
* donné: $U = \qty{12}{\volt}$
* donné: $I_{\textrm{C}} = \qty{5}{\milli\ampere}$
* donné: $B = 298$
* donné: $U_{\textrm{BE}} = \qty{0,6}{\volt}$
* recherché: $R_1$

<fragment>
$B = \frac{I_{\textrm{C}}}{I_{\textrm{B}}} \Rightarrow I_{\textrm{B}} = \frac{I_{\textrm{C}}}{B} = \frac{\qty{5}{\milli\ampere}}{298} = \qty{16,779}{\micro\ampere}$
</fragment>
<fragment>
$R_1 = \frac{U-U_{\textrm{BE}}}{I_{\textrm{B}}} = \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{16,779}{\micro\ampere}} \approx \qty{680}{\kilo\ohm}$
</fragment>

<note>
L'inconvénient du circuit est une amplification de courant mal contrôlée
</note>
---
[question:AC518]
---
### Stabilisation du point de fonctionnement

<left>
[picture:361:a_bauteile_arbeitspunkteinstellung:Circuit de transistor avec diviseur de tension de base]
</left>
<right>
* Le point de fonctionnement est réglé via le diviseur de tension
* Le courant de fuite à travers $R_2$ doit être suffisamment élevé pour que le courant de base n'ait pas d'influence significative sur le point de fonctionnement
</right>
<note>
Le courant de collecteur dépend exponentiellement de la tension base-émetteur; la tolérance des résistances peut avoir de grands effets sur le courant de collecteur. Une forte dépendance à la température dans le transistor peut influencer le courant de collecteur.
</note>

---
[question:AC516]

--- style="font-size: smaller;"
#### Solution
<left>
* donné: $U = \qty{10}{\volt}$
* donné: $I_{\textrm{C}} = \qty{2}{\milli\ampere}$
* donné: $B = 200$
</left>
<right>
* donné: $U_{\textrm{R2}} = \qty{0,6}{\volt}$
* donné: $I_{\textrm{R2}} = 10 \cdot I_{\textrm{B}}$
* recherché: $R_1$
</right>

<fragment>
$B = \frac{I_{\textrm{C}}}{I_{\textrm{B}}} \Rightarrow I_{\textrm{B}} = \frac{I_{\textrm{C}}}{B} = \frac{\qty{2}{\milli\ampere}}{200} = \qty{10}{\micro\ampere}$
</fragment>
<fragment>
$U_{\textrm{R1}} = U - U_{\textrm{R2}} = \qty{10}{\volt} - \qty{0,6}{\volt} = \qty{9,4}{\volt}$
</fragment>
<fragment>
$I_{\textrm{R1}} = I_{\textrm{B}} + I_{\textrm{R2}} = I_{\textrm{B}} + 10 \cdot I_{\textrm{B}} = \qty{110}{\micro\ampere}$
</fragment>
<fragment>
$R_1 = \frac{U_{\textrm{R1}}}{I_{\textrm{R1}}} = \frac{\qty{9,4}{\volt}}{\qty{110}{\micro\ampere}} \approx \qty{85,5}{\kilo\ohm}$
</fragment>

---
[question:AC517]
---
#### Solution

* $U_{\textrm{R2}}$ est égal à $U_{\textrm{BE}} + U_{\textrm{RE}}$
* Le courant de collecteur est principalement déterminé par $R_{\textrm{E}}$
* Circuit très stable

--- style="font-size: smaller;"
<left>
* donné: $U = \qty{10}{\volt}$
* donné: $I_{\textrm{C}} = \qty{2}{\milli\ampere}$
* donné: $B = 200$
</left>
<right>
* donné: $U_{\textrm{BE}} = \qty{0,6}{\volt}$
* donné: $U_{\textrm{RE}} = \qty{1}{\volt}$
* donné: $I_{\textrm{R2}} = 10 \cdot I_{\textrm{B}}$
</right>
* recherché: $R_1$

<fragment>
$B = \frac{I_{\textrm{C}}}{I_{\textrm{B}}} \Rightarrow I_{\textrm{B}} = \frac{I_{\textrm{C}}}{B} = \frac{\qty{2}{\milli\ampere}}{200} = \qty{10}{\micro\ampere}$
</fragment>
<fragment>
$U_{\textrm{R2}} = U_{\textrm{BE}} + U_{R_{\textrm{E}}} = \qty{0,6}{\volt} + \qty{1}{\volt} = \qty{1,6}{\volt}$
</fragment>
<fragment>
$U_{\textrm{R1}} = U - U_{\textrm{R2}} = \qty{10}{\volt} - \qty{1,6}{\volt} = \qty{8,4}{\volt}$
</fragment>
<fragment>
$I_{\textrm{R1}} = I_{\textrm{B}} + I_{\textrm{R2}} = I_{\textrm{B}} + 10 \cdot I_{\textrm{B}} = \qty{110}{\micro\ampere}$
</fragment>
<fragment>
$R_1 = \frac{U_{\textrm{R1}}}{I_{\textrm{R1}}} = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} \approx \qty{76,4}{\kilo\ohm}$
</fragment>

---
[question:AC519]
---
#### Solution

* Pas de courant à travers $R_1 \rightarrow$ pas de tension aux bornes de $R_2$
* La base est au potentiel de masse $\rightarrow$ le transistor est sans courant
* Pas de chute de tension à $R_{\textrm{C}} \rightarrow$ le potentiel du collecteur monte à la tension de service

---
[question:AC520]
---
#### Solution

* $R_2$ est sans courant $\rightarrow$ la base est connectée à la tension de service via $R_1$
* En raison du dimensionnement, le courant de base est maintenant 11 fois plus élevé que prévu
* Le courant de collecteur augmentera fortement $\rightarrow$ la chute de tension à $R_{\textrm{C}}$ augmentera fortement
* $U_{\textrm{CE}}$ chute à la valeur de saturation d'environ $\qty{0,1}{\volt}$

---
## Transistor à effet de champ (FET)

[picture:271:a_bauelemente_fet:Symbole de circuit pour les transistors à effet de champ]

* Structure différente
* Il existe un canal semi-conducteur
* Le flux de courant est commandé par un champ électrique
* Par conséquent, commandé par tension

<note>
La ligne verticale symbolise le canal, le drain (en haut) et la source (en bas) sont en contact; à gauche se trouve la grille et la flèche rappelle une diode
</note>
---
[question:AC502]
---
[question:AC506]
---
### Connexions du FET

* *Source* Source de porteurs de charge dans le canal
* *Drain* Évacuation des porteurs de charge dans le canal
* *Gate* commande le flux de porteurs de charge dans le canal

---
[question:AC513]
---
[question:AC512]
---
[question:AC514]

<note>
Mieux serait: commande le courant de canal au lieu de la résistance, car ce comportement de résistance n'apparaît que pour de petites tensions drain-source
</note>
---
### Types de FET

* *autoconducteur*: Sans tension grille-source, le FET est conducteur
* *autobloquant*: Sans tension grille-source, le FET est bloquant
* *FET à canal n*: Le courant dans le canal est porté par des électrons
* *FET à canal p*: Le courant dans le canal est porté par des trous
* *FET à jonction*: La grille est une diode
* *FET à isolation*: La grille est une structure de condensateur (par exemple, MOSFET)

<note>
MOSFET: metal oxide semiconductor FET
</note>
---
### Symbole de circuit FET

<left>
[picture:273:a_bauelemente_selbstleitender_p_kanal_mosfet:MOSFET à canal p autoconducteur]
[picture:276:a_bauelemente_selbstsperrender_n_kanal_mosfet:MOSFET à canal n autobloquant]
</left>
<right>
* *autoconducteur*/*autobloquant*: grille continue/pointillée
* *canal p*/*canal n*: la flèche s'éloigne du/vers le canal
* *Isolation* (MOSFET): grille et canal comme condensateur
</right>

---
[question:AC507]
---
[question:AC508]
---
[question:AC509]
---
[question:AC510]
---
[question:AC511]
---
[question:AC521]
---
#### Solution

<left>
* donné: $U_{\textrm{B}} = \qty{44}{\volt}$
* donné: $R_1 = \qty{10}{\kilo\ohm}$
* donné: $R_2 = \qty{1}{\kilo\ohm}$
* donné: $R_3 = \qty{2,2}{\kilo\ohm}$
* recherché: $U_{\textrm{GS}}$
* approche: diviseur de tension non chargé sur $R_1$ et $R_2$, avec $U_{\textrm{GS}} = U_{\textrm{R2}}$
</left>
<right>
<fragment>
$\begin{split} \frac{U_{\textrm{R2}}}{U_{\textrm{B}}} &= \frac{R_2}{R_1+R_2}\\ \Rightarrow U_{\textrm{R2}} &= \frac{R_2}{R_1+R_2} \cdot U_{\textrm{B}}\\ &= \frac{\qty{1}{\kilo\ohm}}{\qty{10}{\kilo\ohm}+\qty{1}{\kilo\ohm}} \cdot \qty{44}{\volt}\\ &= \frac{1}{11} \cdot \qty{44}{\volt} = \qty{4}{\volt} \end{split}$
</fragment>
</right>

---
[question:AC522]
---
#### Solution

<left>
* donné: $U_{\textrm{B}} = \qty{44}{\volt}$
* donné: $R_1 = \qty{10}{\kilo\ohm}$
* donné: $R_3 = \qty{2,2}{\kilo\ohm}$
* donné: $U_{\textrm{GS}} = U_{\textrm{R2}} = \qty{2,8}{\volt}$
* donné: $U_{\textrm{B}} = U_{\textrm{R1}} + U_{\textrm{R2}}$
* recherché: $R_2$
</left>
<right>
<fragment>
$\begin{split} \frac{U_{\textrm{R1}}}{U_{\textrm{R2}}} &= \frac{R_1}{R_2}\\ \Rightarrow R_2 &= R_1 \cdot \frac{U_{\textrm{R2}}}{U_{\textrm{R1}}}\\ &= R_1 \cdot \frac{U_{\textrm{R2}}}{U_{\textrm{B}}-U_{\textrm{GS}}}\\ &= \qty{10}{\kilo\ohm} \cdot \frac{\qty{2,8}{\volt}}{\qty{44}{\volt}-\qty{2,8}{\volt}}\\ &\approx \qty{680}{\ohm} \end{split}$
</fragment>
</right>
---
[question:AC523]
---
#### Solution

* donné: $R_{\textrm{DSon}} = \qty{4}{\milli\ohm}$
* donné: $I = \qty{25}{\ampere}$
* recherché: $P$

<fragment>
$P = I^2 \cdot R = (\qty{25}{\ampere})^2 \cdot \qty{4}{\milli\ohm} = \qty{2,5}{\watt}$
</fragment>

<note>
Le MOSFET se comporte comme une résistance ohmique
</note>

---
### Diode de roue libre

* Le relais est actionné via un transistor bipolaire connecté en série
* Le transistor s'enclenche $\rightarrow$ le courant circule à travers la bobine du relais
* Le transistor se désenclenche $\rightarrow$ le courant dans la bobine induit une tension négative au transistor
* Peut entraîner la destruction du transistor
* Prévenir: *diode de roue libre* montée en parallèle avec le relais dans le sens de blocage
* La tension d'induction est limitée à la tension de la diode

---
[question:AC524]