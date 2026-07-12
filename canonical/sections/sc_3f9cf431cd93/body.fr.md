Les oscillateurs sont l'un des éléments de circuit les plus importants en radioamateur. Ils sont en quelque sorte le cœur de chaque appareil radio. Les oscillateurs servent à générer des oscillations à haute fréquence dans les émetteurs et les récepteurs.

Le cœur d'un oscillateur est un élément amplificateur dont le *signal de sortie est à nouveau rétrocouplé à son entrée*.

Pour qu'un oscillateur puisse générer des oscillations non amorties, *deux conditions fondamentales* doivent être remplies.
D'une part, le *signal de sortie doit être rétrocouplé en phase avec le point d'entrée du circuit*.
D'autre part, *l'amplitude du signal rétrocouplé doit être au moins de la même taille* que celle du signal d'entrée. On dit aussi que l'amplification en boucle doit être supérieure à 1 pour qu'une auto-excitation soit possible, ce qui maintient l'oscillation.

[question:AD613]

<margin>
[picture:760:a_oszillator_schaltungen_oszillator:Circuit d'un oscillateur à rétroaction capacitive]
</margin>

%TODO: Peut-être dériver l'image 760 et l'enrichir des 3 points du circuit à trois points (au diviseur de tension capacitif - en haut, au milieu et en bas)

Le circuit représenté dans la figure [ref:a_oszillator_schaltungen_oszillator] représente un oscillateur à trois points à rétroaction capacitive. Le signal de sortie est rétrocouplé de l'émetteur du circuit à la base du transistor via un diviseur de tension capacitif. La fréquence de l'oscillateur est principalement déterminée par le circuit oscillant dans la base (composé d'une bobine et d'un condensateur d'accord) ainsi que par le diviseur de tension capacitif connecté en parallèle au circuit oscillant.
Il s'agit d'un oscillateur en circuit collecteur, car le collecteur est en masse en tension alternative.

[question:AD614]
[question:AD616]

Pour augmenter la stabilité de fréquence d'un oscillateur, sa composante déterminante en fréquence (circuit oscillant) peut être remplacée par un quartz. Les quartz peuvent être excités à la fois à leur fréquence fondamentale et à leurs fréquences harmoniques (harmoniques/surtones). Cependant, pour qu'un quartz puisse fonctionner à une harmonique, l'amplificateur doit être conçu de manière sélective en fréquence (par exemple en utilisant un circuit oscillant). Si celui-ci n'est pas présent, on peut en déduire que le quartz fonctionne à sa fréquence fondamentale (voir figure [ref:a_oszillator_schaltungen_quarzoszillator]).

<margin>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Circuit d'un oscillateur à quartz en circuit collecteur avec fonctionnement du quartz à la fréquence fondamentale]
</margin>

[question:AD617]

Le signal de l'oscillateur doit toujours être découplé au point de plus faible impédance d'un oscillateur afin de le solliciter le moins possible. Dans un circuit collecteur, il s'agit de l'émetteur du transistor.

[question:AD610]

Un oscillateur doit toujours être suivi d'un étage tampon dit, qui garantit que l'oscillateur est découplé des autres parties du circuit et que sa fréquence n'est pas influencée par la charge de la sortie. Un étage tampon est généralement conçu comme un circuit collecteur (suiveur d'émetteur) et a une impédance d'entrée élevée qui ne sollicite l'oscillateur que de manière minimale. À sa sortie, le signal de l'oscillateur peut alors être traité à faible impédance.
Les mesures sur les oscillateurs doivent toujours être effectuées après l'étage tampon, car sinon l'oscillateur est chargé par des capacités parasites et sa fréquence est influencée par celles-ci.

[question:AD615]
[question:AD619]
[question:AD618]










