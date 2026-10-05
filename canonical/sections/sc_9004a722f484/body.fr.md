**LES APPLETS NE FONCTIONNENT PAS**

**applet_am_modulator et applet_dsp**

**Il manque dans notre générateur dans /assets le circuitjs/..    issue #54**

Nous avons déjà rencontré les diodes dans divers circuits. Nous allons maintenant examiner comment leur caractéristique non linéaire peut être utilisée pour moduler un signal haute fréquence porteuse avec un signal utile basse fréquence.

Lorsqu'un signal HF et un signal BF sont appliqués simultanément à une diode, comme illustré dans la figure [ref:a_am_modulator], la tension BF influence la conductivité de la diode. Ainsi, le signal HF est transmis plus ou moins fortement en fonction de la valeur instantanée de la BF. Son amplitude varie donc au rythme du signal BF.

À la sortie, cela génère, outre la porteuse HF d'origine, deux bandes latérales au-dessus et en dessous de la fréquence porteuse. Un circuit oscillant accordé sur la fréquence porteuse supprime les composantes de fréquence indésirables supplémentaires. On obtient ainsi à la sortie un signal modulé en amplitude (AM).

<margin>
[picture:772:a_am_modulator:Modulateur AM simple avec diode et circuit oscillant]
</margin>

<webonly>
La simulation suivante montre le fonctionnement du modulateur AM ; les valeurs ont été choisies pour que la HF et la BF soient bien visibles. La BF est à $\qty{500}{\hertz}$, la HF à $\qty{10}{\kilo\hertz}$. L'amplitude du signal HF varie au rythme de la BF. Le circuit oscillant est accordé sur la fréquence porteuse et supprime les composantes de fréquence indésirables. Si l'on retire le circuit oscillant, on voit une multitude de produits de mélange. On peut également régler la fréquence BF sur $\qty{1}{\kilo\hertz}$ pour voir comment les bandes latérales se déplacent.

[include:applet_am_modulator]

</webonly>

<indepth>
Un signal AM peut également être décrit mathématiquement. Pour cela, considérons d'abord un signal BF sinusoïdal normalisé

$m(t)=\cos(\omega t)$

avec la pulsation $\omega=2\pi f_\mathrm{m}$. Avec son amplitude $\hat U_\mathrm{m}$ et une composante continue supplémentaire $U_\mathrm{G}$, on obtient

$U_\mathrm{m}(t)=U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)$

Ce signal est ensuite multiplié par le signal haute fréquence porteuse

$U_\mathrm{T}(t)=\cos(\Omega t)$

avec $\Omega=2\pi f_\mathrm{T}$. Le signal AM est donc :

$U_\mathrm{AM}(t)=\left(U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)\right)\cdot\cos(\Omega t)$

En développant, on obtient :

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\hat U_\mathrm{m}\cdot\cos(\omega t)\cdot\cos(\Omega t)$

En utilisant la relation

$\cos(a)\cdot\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$

le second terme peut être décomposé davantage :

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\frac{\hat U_\mathrm{m}}{2}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

On reconnaît ainsi immédiatement les trois composantes d'un signal AM : Le premier terme décrit la *porteuse* à la fréquence $\Omega$. Les deux autres termes forment la *bande latérale supérieure et inférieure* aux fréquences $\Omega+\omega$ et $\Omega-\omega$.

La composante continue $U_\mathrm{G}$ est responsable du maintien de la porteuse. Même lorsque le signal utile est momentanément nul, un signal porteuse continue d'être généré.

[picture:1127:a_am_modulation:Spectre d'un signal AM avec porteuse et deux bandes latérales]

</indepth>

Ce principe est illustré dans la question suivante : Une diode est excitée simultanément par un signal BF et un signal HF, et le signal de sortie est filtré par un circuit oscillant LC.

[question:AD507]

---

Avec quatre diodes disposées en anneau, on peut construire un modulateur de manière à supprimer la porteuse en sortie. Nous avons déjà rencontré un tel circuit dans le chapitre « Mélangeur II » en tant que *mélangeur équilibré*. Il était utilisé pour transposer un signal HF sur une fréquence intermédiaire. Dans l'émetteur, nous utilisons maintenant le même principe de base pour générer un signal modulé.

<margin>
[picture:759:a_balancemodulator:Modulateur équilibré avec anneau de diodes]
</margin>

On reconnaît typiquement un mélangeur équilibré ou modulateur équilibré à l'anneau de diodes, comme représenté dans la figure [ref:a_balancemodulator]. L'anneau de diodes est commandé par le signal de l'oscillateur $f_\mathrm{OSZ}$. Selon la polarité du signal de l'oscillateur, l'une des deux paires de diodes opposées conduit.

Ainsi, le signal BF est transmis alternativement à la sortie avec la même polarité ou une polarité inversée. En simplifiant, le signal BF est donc multiplié par le signal de l'oscillateur.

L'avantage décisif du circuit symétrique est la *suppression de la porteuse* : Les composantes du signal de l'oscillateur s'annulent idéalement mutuellement en sortie. Sans signal BF, aucun signal de sortie n'est donc généré. En revanche, lorsqu'un signal BF est appliqué, les bandes latérales supérieure et inférieure sont générées, tandis que la porteuse reste supprimée.

Le signal de sortie est appelé *signal à bandes latérales doubles avec porteuse supprimée* (DSB).

[question:AE206]
[question:AF302]
[question:AF308]
[question:AD510]

<indepth>
La suppression de la porteuse d'un modulateur équilibré peut être décrite de manière simplifiée avec deux branches symétriques :

$u_1(t)=\left(U_G+\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

$u_2(t)=\left(U_G-\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

En sortie, les deux signaux sont soustraits l'un de l'autre :

$u_\mathrm{out}(t)=u_1(t)-u_2(t)$

On obtient ainsi :

$u_\mathrm{out}(t)=U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)-U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Les deux composantes de la porteuse $U_G\cos(\Omega t)$ s'annulent. Il reste :

$u_\mathrm{out}(t)=2\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Avec $\cos(a)\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$, on obtient :

$u_\mathrm{out}(t)=\hat U_\mathrm{m}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

Le signal de sortie ne contient donc plus que la bande latérale supérieure et la bande latérale inférieure. La porteuse à $\Omega$ est supprimée.
</indepth>

---

Pour que le signal de l'oscillateur s'annule le plus complètement possible en sortie, le circuit doit être symétrique, c'est-à-dire *équilibré*. De petites différences d'amplitude ou de phase entre les deux voies de signal suffisent à laisser un résidu de la porteuse en sortie. La symétrie d'amplitude peut par exemple être ajustée avec un potentiomètre. Pour l'équilibrage de phase, un condensateur ajustable est parfois utilisé dans certains circuits. L'objectif de l'équilibrage est d'obtenir une suppression de la porteuse la plus élevée possible, tout en conservant les deux bandes latérales de modulation.

<webonly>
L'applet suivante montre l'équilibrage de la porteuse. Lorsque le curseur sur le côté droit est déplacé, la porteuse apparaît soudainement dans le spectre.

[include:applet_dsp]
</webonly>

[question:AF309]

---

Le modulateur équilibré constitue le premier étage d'un modulateur BLU et génère un signal DSB. Derrière le modulateur équilibré, un filtre passe-bande étroit suit comme deuxième étage, comme dans la figure [ref:a_ssb_modulation]. Il ne laisse passer qu'une des deux bandes latérales et supprime l'autre. En sortie, un signal à bande latérale unique (BLU) est ainsi généré.

<margin>
[picture:500:a_ssb_modulation:Schéma bloc pour la modulation BLU avec la méthode par filtrage]
</margin>

[question:AF306]
[question:AF304]
[question:AF303]
[question:AF305]

---

Une bonne implémentation pour un appareil radio devant générer à la fois USB et LSB consiste à concevoir le filtre passe-bande pour une bande de fréquences spécifique. Le fait que la bande latérale supérieure ou inférieure soit filtrée n'est pas déterminé par un changement du filtre, mais par la fréquence de l'oscillateur dans le modulateur équilibré. Pour cela, deux oscillateurs à quartz différents sont disponibles.

Par exemple, si la fréquence de l'oscillateur $\qty{8998,5}{\kilo\hertz}$ est choisie pour USB, la modulation génère deux bandes latérales. La bande latérale supérieure est alors exactement décalée dans la bande passante du filtre constant, tandis que la bande latérale inférieure se trouve en dehors de la bande passante et est supprimée.

Pour LSB, on commute sur l'autre fréquence quartz de $\qty{9001,5}{\kilo\hertz}$. Ainsi, le spectre DSB entier se décale de sorte que c'est maintenant la bande latérale inférieure qui se trouve dans la bande passante du même filtre, et la bande latérale supérieure est supprimée.

L'astuce décisive consiste donc à laisser le filtre inchangé et à décaler la position du signal DSB par des fréquences d'oscillateur différentes. Similairement à la fréquence intermédiaire d'un récepteur, cela permet d'utiliser un filtre de haute qualité, fixe et accordé, pour différentes positions de fréquence.

[question:AF307]

<margin>
<latexonly>
[picture:831:a_ssb_modulation_lsb:Fréquences avec la méthode par filtrage pour LSB]
[picture:940:a_ssb_modulation_lsb:Spectre avec la méthode par filtrage pour LSB]
[picture:832:a_ssb_modulation_usb:Fréquences avec la méthode par filtrage pour USB]
[picture:941:a_ssb_modulation_usb:Spectre avec la méthode par filtrage pour USB]
</latexonly>
<webonly>
[include:applet_dsp_filter]
</webonly>
</margin>

---

Pour la génération d'un signal modulé en fréquence (FM), une *diode à capacité variable* peut être utilisée. Elle est reconnaissable dans les schémas électriques par le petit symbole de condensateur à côté de la diode, comme dans la figure [ref:a_fm_modulator].

Une diode à capacité variable est utilisée en polarisation inverse. Sa capacité dépend alors de la tension inverse appliquée. Lorsqu'elle est utilisée comme partie du circuit oscillant déterminant la fréquence d'un oscillateur, une variation de cette tension modifie la fréquence de résonance du circuit oscillant et donc la fréquence de l'oscillateur.

Pour la modulation de fréquence, le signal BF est superposé à la tension continue de la diode à capacité variable. Ainsi, sa capacité varie au rythme du signal BF et la fréquence de l'oscillateur est décalée vers le haut et vers le bas en conséquence. De cette manière, un signal modulé en fréquence est généré.

<margin>
[picture:155:a_fm_modulator:Modulateur FM avec diode à capacité variable]
</margin>

[question:AD508]
[question:AF310]

---

Avec de grandes tensions BF, on peut facilement provoquer des variations de fréquence de l'oscillateur beaucoup plus importantes (excursion FM) que ce qui est autorisé. Par conséquent, une limitation de l'excursion par un réglage et une limitation de l'amplitude BF est nécessaire. Des diodes montées en antiparallèle limitent la tension à environ la tension de seuil des diodes. Les figures [ref:a_fm_modulator_hub1] et [ref:a_fm_modulator_hub2] en montrent un exemple.

<margin>
[picture:44:a_fm_modulator_hub1:Circuit de limitation d'excursion]
[picture:828:a_fm_modulator_hub2:Limitation du signal]
</margin>

[question:AD509]
