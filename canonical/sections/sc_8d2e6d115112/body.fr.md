Les oscillateurs sont l'un des éléments de circuit les plus importants dans la radioamateur. Ils sont en quelque sorte le cœur de chaque appareil radio. Les oscillateurs servent à générer des oscillations à haute fréquence dans les émetteurs et les récepteurs. Il existe différentes possibilités de réaliser techniquement les oscillateurs.

---

<margin>
[include:applet_schwingkreis]
</margin>

La forme la plus simple d'un oscillateur est l'oscillateur LC, qui contient un circuit oscillant (composé d'une bobine et d'un condensateur), que nous avons appris dans le chapitre précédent.

[question:ED501]

Les oscillateurs LC présentent l'inconvénient que leurs composants déterminant la fréquence (L et C) peuvent varier fortement en fonction de la température, ce qui peut entraîner de grandes déviations de fréquence.

Selon le recueil de formules, la formule pour la fréquence d'oscillation (formule du circuit oscillant de Thomson) est :

$ f_0 = \frac{1}{2\pi \sqrt{L\cdot C}} $

La fréquence d'un oscillateur LC change lorsque la valeur du condensateur ou de la bobine change, par exemple sous l'effet de la température. On peut voir dans la formule comment cela affecte la fréquence : 
Lorsque la capacité du condensateur ou l'inductance de la bobine *augmente*, la fréquence du circuit oscillant *diminue*. Inversement, la fréquence du circuit oscillant *augmente* lorsque la capacité ou l'inductance *diminue*.

[question:ED503]
[question:ED505]
[question:ED502]
[question:ED504]

La vitesse de variation de la température détermine également la vitesse de variation de la fréquence d'un oscillateur. Cependant, la fréquence ne change pas brusquement, car les effets thermiques sont toujours soumis à une certaine inertie. Par conséquent, la fréquence d'un oscillateur soumis à des températures fluctuantes change généralement lentement dans une direction ou une autre.

[question:EF304]

Un type d'oscillateur beaucoup plus stable en fréquence est l'oscillateur à quartz. Dans ce cas, un quartz oscillant est utilisé comme composant déterminant la fréquence, dont la fréquence de résonance ne dépend que dans une très faible mesure de sa température (par rapport aux oscillateurs LC).

[question:ED506]
[question:ED507]

Pour éviter les émissions indésirables, les oscillateurs ainsi que les étages tampons doivent toujours être blindés le plus possible. Cela peut être réalisé, par exemple, en installant l'oscillateur dans un boîtier métallique mis à la terre.

[question:EF207]