Les oscillateurs sont l'un des éléments de circuit les plus importants dans le radioamateurisme. Ils constituent, pour ainsi dire, le cœur de tout appareil radio. Les oscillateurs servent à générer des oscillations haute fréquence dans les émetteurs et récepteurs. Il existe différentes manières de réaliser techniquement les oscillateurs.

---

<margin>
[include:applet_schwingkreis]
</margin>

La forme la plus simple d'un oscillateur est l’*oscillateur LC*, qui utilise comme éléments déterminant la fréquence un *circuit oscillant* (composé d'une bobine et d'un condensateur), que nous avons appris à connaître dans le chapitre précédent.


<indepth>
Un oscillateur se compose d’un *élément déterminant la fréquence*, par exemple un *circuit oscillant LC* ou un quartz, d’un *amplificateur* ainsi que d’une *rétroaction positive*. La rétroaction renvoie une partie du signal de sortie en phase avec l’entrée et compense les pertes du circuit oscillant. Cela permet de générer des oscillations non amorties à la fréquence prédéfinie par l’élément déterminant la fréquence.
</indepth>

[question:ED501]

Les oscillateurs LC présentent l’inconvénient que leurs composants déterminant la fréquence (L et C) peuvent varier fortement en fonction de la *température*, ce qui peut entraîner d’importantes déviations de fréquence.


D’après le recueil de formules, la formule de la fréquence d’oscillation (formule du circuit oscillant de Thomson) est la suivante :


$ f_0 = \frac{1}{2\pi \sqrt{L\cdot C}} $


La fréquence d’un oscillateur LC change lorsque la valeur du condensateur ou de la bobine varie, par exemple sous l’effet de la température. On peut le constater dans la formule :

En cas d’*augmentation* de la *capacité* du condensateur ou d’*augmentation* de l’*inductance* de la bobine, la *fréquence* du circuit oscillant *diminue*. Inversement, la *fréquence* du circuit oscillant *augmente* en cas de *diminution* de la *capacité* ou de l’*inductance*.


[question:ED503]
[question:ED505]
[question:ED502]
[question:ED504]

La vitesse de variation de la température détermine également la vitesse de variation de la fréquence d’un oscillateur. Cependant, la fréquence ne change pas de manière abrupte, car les effets thermiques sont toujours soumis à une certaine inertie. Par conséquent, la fréquence d’un oscillateur soumis à des variations de température change généralement lentement dans un sens ou dans l’autre.

[question:EF304]

Un type d’oscillateur bien plus stable en fréquence est l’*oscillateur à quartz*. Dans ce cas, on utilise comme composant déterminant la fréquence un résonateur à quartz dont la *fréquence de résonance* ne dépend que très faiblement de la *température* (par rapport aux oscillateurs LC).


[question:ED506]
[question:ED507]

Pour éviter les rayonnements indésirables, les oscillateurs ainsi que les étages tampons doivent être aussi bien blindés que possible. Cela peut par exemple être réalisé en plaçant l’oscillateur dans un boîtier métallique mis à la terre.


[question:EF207]