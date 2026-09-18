Les oscillateurs sont l’un des éléments de circuit les plus importants en radioamateurisme. Ils constituent, pour ainsi dire, le cœur de tout appareil radio. Les oscillateurs servent à générer des oscillations haute fréquence dans les émetteurs et les récepteurs.

Le cœur d’un oscillateur est un composant amplificateur dont le *signal de sortie est réinjecté à son entrée*.

Pour qu’un oscillateur puisse générer des oscillations non amorties, *deux conditions fondamentales* doivent être remplies.
D’une part, le *signal de sortie doit être réinjecté en phase au point d’entrée du circuit*.
D’autre part, l’*amplitude du signal réinjecté doit être au moins égale* à celle du signal d’entrée. On dit aussi que le *gain de boucle doit être supérieur à 1* pour qu’un auto-oscillation soit possible et maintienne l’oscillation.

[question:AD613]

<margin>
[picture:760:a_oszillator_schaltungen_oszillator:Schéma d’un oscillateur à couplage capacitif]  
</margin>

%TODO: Peut-être dériver l’image 760 et ajouter les 3 points du circuit à trois points (au diviseur de tension capacitif – en haut, au milieu et en bas)

Le schéma représenté dans l’illustration [ref:a_oszillator_schaltungen_oszillator] montre un oscillateur à trois points à couplage capacitif. Le signal de sortie est réinjecté de l’émetteur du circuit vers la base du transistor par l’intermédiaire d’un diviseur de tension capacitif. La fréquence de l’oscillateur est principalement déterminée par le circuit oscillant à la base (composé d’une bobine et d’un condensateur ajustable) ainsi que par le diviseur de tension capacitif monté en parallèle avec le circuit oscillant.

Il s’agit d’un oscillateur en montage à collecteur commun, car le collecteur est relié à la masse en courant alternatif.

[question:AD614]
[question:AD616]

Pour augmenter la stabilité en fréquence d’un oscillateur, son composant déterminant la fréquence (circuit oscillant) peut être remplacé par un quartz. Les quartz peuvent être excités en oscillation à leur fréquence fondamentale ainsi qu’à leurs fréquences harmoniques (harmoniques ou partiels). Cependant, pour qu’un quartz puisse fonctionner sur une harmonique, l’amplificateur doit être conçu de manière sélective en fréquence (par exemple en utilisant un circuit oscillant). Si ce n’est pas le cas, on peut en déduire que le quartz fonctionne à sa fréquence fondamentale (voir illustration [ref:a_oszillator_schaltungen_quarzoszillator]).

<margin>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Schéma d’un oscillateur à quartz en montage à collecteur commun avec fonctionnement du quartz à la fréquence fondamentale]  
</margin>

[question:AD617]

Le signal de l’oscillateur doit toujours être extrait au point de plus faible impédance d’un oscillateur afin de le solliciter le moins possible. Dans un montage à collecteur commun, ce point est l’émetteur du transistor.

[question:AD610]

Un oscillateur doit toujours être suivi d’un étage tampon qui assure que l’oscillateur est découplé des autres parties du circuit et que sa fréquence n’est pas influencée par la charge de la sortie. Un étage tampon est généralement conçu comme un montage à collecteur commun (émetteur suiveur) et présente une impédance d’entrée élevée, ce qui ne sollicite que très peu l’oscillateur. Le signal de l’oscillateur peut ensuite être traité en basse impédance à sa sortie.

Les mesures sur les oscillateurs doivent toujours être effectuées après l’étage tampon, car sinon l’oscillateur est sollicité par des capacités parasites et sa fréquence en est influencée.

[question:AD615]
[question:AD619]
[question:AD618]