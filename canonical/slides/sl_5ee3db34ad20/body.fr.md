## Conversion A/D et D/A

* Les *convertisseurs analogique* (A/D) transforment les signaux analogiques en valeurs numériques
* Les *convertisseurs numérique* (D/A) reconvertissent les valeurs numériques en signaux analogiques
* Tous deux ne disposent que d’un nombre fini de valeurs possibles
* Une propriété importante est donc leur *résolution*

<note>
Les convertisseurs A/D et D/A forment l’interface entre le monde analogique et le monde numérique.

Le convertisseur A/D génère des échantillons numériques à partir d’un signal d’entrée analogique. Le convertisseur D/A effectue l’opération inverse et produit des valeurs de tension analogiques à partir de données numériques.
</note>

---
## Quantification dans le convertisseur A/D

* Le convertisseur A/D ne peut générer qu’un nombre limité de valeurs numériques
* Les valeurs d’entrée analogiques sont donc attribuées à des niveaux fixes
* Les valeurs intermédiaires ne peuvent pas être représentées avec exactitude
* Cela entraîne une *erreur de quantification*

<note>
Nous avons déjà abordé le principe de quantification.

Une valeur analogique mesurée se situe souvent entre deux niveaux numériques possibles. Le convertisseur A/D doit l’attribuer à l’un de ces niveaux.

L’écart ainsi créé entre la valeur réelle et la valeur représentée est appelé erreur de quantification.
</note>

---

[question:AF607]

---
## Résolution d’un convertisseur A/D

* La résolution indique le nombre de valeurs numériques distinctes possibles
* Elle est généralement exprimée en *bit*
* $\qty{8}{\bit}$ → $\num{256}$ valeurs possibles
* $\qty{16}{\bit}$ → $\num{65536}$ valeurs possibles
* Plus le nombre de bits est élevé, plus la représentation de l’amplitude du signal est fine

---
## Influence de la résolution

<left>
[picture:300:a_adc_4bit:Signal sinusoïdal numérisé par un convertisseur A/D 4 bits suivi d’une conversion D/A]
</left>
<right>
[picture:299:a_adc_12bit:Signal sinusoïdal numérisé par un convertisseur A/D 12 bits suivi d’une conversion D/A]
</right>

* $\qty{4}{\bit}$ → $\num{16}$ valeurs possibles
* $\qty{12}{\bit}$ → $\num{4096}$ valeurs possibles
* Une résolution plus élevée → des niveaux de quantification plus petits

<note>
Ici, l’influence de la résolution peut être comparée directement.

Avec 4 bits, seuls 16 valeurs sont disponibles. Les paliers sont clairement visibles dans le signal reconstitué.

Avec 12 bits, 4096 valeurs sont disponibles. Le signal reconstitué se rapproche donc beaucoup plus du signal sinusoïdal d’origine.

L’ajout de 8 bits supplémentaires multiplie le nombre de niveaux possibles par 256.
</note>

---

[question:AF608]

---
## Gigue (Jitter)

* Les échantillons doivent être prélevés à des instants précis
* En pratique, les instants d’échantillonnage réels peuvent légèrement varier
* Ces écarts temporels sont appelés *gigue*
* La gigue peut introduire un *bruit* supplémentaire dans le signal numérisé

<note>
Non seulement la précision de l’amplitude mesurée est importante, mais aussi la précision de l’instant d’échantillonnage.

Pour cela, le convertisseur A/D a besoin d’une horloge aussi stable que possible. De légères variations temporelles de cette horloge entraînent le prélèvement des échantillons à des instants non prévus.

Ces variations sont appelées gigue.
</note>

---

[question:AF621]

---
## Convertisseur D/A

* Le convertisseur D/A est l’opposé du convertisseur A/D
* Il génère des valeurs de tension analogiques à partir d’échantillons numériques
* Un convertisseur D/A ne dispose également que d’un nombre fini de valeurs de sortie possibles
* Sa résolution est également exprimée en bits

<note>
Le convertisseur D/A fonctionne selon le principe inverse.

Une valeur numérique est attribuée à une tension de sortie analogique spécifique. Ici aussi, la résolution détermine le nombre de valeurs différentes qui peuvent être générées.
</note>

---

[question:AF609]

---
## Plage de tension et résolution

* Un convertisseur D/A possède une plage de tension définie
* Exemple : $\qty{0}{\volt}$ à $\qty{1}{\volt}$
* Avec $\qty{4}{\bit}$, $\num{2^4}=\num{16}$ niveaux sont disponibles
* Dans un convertisseur D/A linéaire, ces niveaux sont uniformément répartis sur la plage de tension

---
## Pas de quantification

Avec $\num{16}$ niveaux, il y a $\num{15}$ intervalles entre les niveaux.

Pour une plage de tension de $\qty{0}{\volt}$ à $\qty{1}{\volt}$, on obtient :

$\frac{\qty{1}{\volt}}{16-1}\approx\qty{67}{\milli\volt}$

<fragment>
Le pas de quantification est donc d’environ $\qty{67}{\milli\volt}$.
</fragment>

<note>
Il faut ici noter qu’entre 16 valeurs de tension possibles, il n’y a que 15 intervalles.

Cela correspond au problème bien connu de la clôture : entre 10 piquets de clôture, il n’y a que 9 intervalles.

C’est pourquoi, dans cet exemple, la plage de tension est divisée par 15 et non par 16.
</note>

---

[question:AF611]

---

[question:AF610]

---
## Convertisseurs A/D et D/A dans le SDR

* Les convertisseurs A/D numérisent les signaux d’entrée analogiques
* Les échantillons peuvent ensuite être traités numériquement
* Les convertisseurs D/A génèrent, si nécessaire, des signaux analogiques à partir de ces données
* Ce principe est utilisé à de nombreux endroits dans les récepteurs et émetteurs-récepteurs SDR

<note>
Un SDR est un exemple typique de l’interaction entre conversion A/D, traitement numérique du signal et conversion D/A.

Le signal analogique est d’abord numérisé. Ensuite, des opérations comme le filtrage, la démodulation ou la modulation peuvent être effectuées numériquement. Si un signal analogique doit être produit à nouveau, un convertisseur D/A est utilisé.
</note>

---
## Utilisation de la plage de valeurs

* Un petit signal d’entrée n’utilise qu’une partie des niveaux disponibles
* Un signal trop grand dépasse la plage de valeurs représentable
* Les valeurs supérieures au maximum ne peuvent plus être correctement représentées
* Le signal est alors tronqué à cet endroit

<fragment>
Cet effet est appelé *écrêtage*.
</fragment>

<note>
Pour une numérisation optimale, la plage de valeurs disponible doit être utilisée de manière judicieuse.

Si le signal est très faible, seuls quelques niveaux sont utilisés.

Si le signal est trop grand, le convertisseur A/D atteint sa valeur maximale représentable. Les valeurs d’entrée encore plus grandes ne peuvent plus être distinguées. Les pics du signal apparaissent alors tronqués.

Un convertisseur D/A ne peut pas non plus produire une tension de sortie en dehors de sa plage de valeurs prévue.
</note>

---
## Influence de la résolution

* Résolution élevée → de nombreuses valeurs d’amplitude possibles
* Résolution faible → peu de valeurs d’amplitude possibles
* Plus de niveaux permettent une numérisation et une reconstruction plus précises
* La plage de valeurs disponible doit être utilisée de manière optimale

---

[question:AF613]

---

[question:AF612]

---

[question:AF614]