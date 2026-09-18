Nous avons déjà rencontré les diodes dans divers circuits. Examinons maintenant comment leur caractéristique non linéaire peut être utilisée pour moduler un signal porteur haute fréquence avec un signal utile basse fréquence.

Si un signal HF et un signal BF sont appliqués ensemble à une diode, comme illustré dans la figure [ref:a_am_modulator], la tension BF influence la conductivité de la diode. Ainsi, le signal HF est transmis avec une amplitude variable selon la valeur instantanée du signal BF. Son amplitude varie donc au rythme du signal BF.

À la sortie, on obtient, en plus de la porteuse HF initiale, deux bandes latérales au-dessus et en dessous de la fréquence porteuse. Un circuit oscillant accordé sur la fréquence porteuse supprime les autres composantes de fréquence indésirables. On obtient ainsi à la sortie un signal modulé en amplitude (AM).

<margin>
[picture:772:a_am_modulator:Modulateur AM simple avec diode et circuit oscillant]
</margin>

<webonly>
La simulation suivante montre le fonctionnement du modulateur AM. Les valeurs ont été choisies pour que les signaux HF et BF soient bien visibles. Le signal BF est à $\qty{500}{\hertz}$, le signal HF à $\qty{10}{\kilo\hertz}$. L’amplitude du signal HF varie au rythme du signal BF. Le circuit oscillant est accordé sur la fréquence porteuse et supprime les composantes de fréquence indésirables. Si l’on retire le circuit oscillant, on observe une multitude de produits de mélange. On peut aussi modifier la fréquence BF à $\qty{1}{\kilo\hertz}$ pour voir comment les bandes latérales se déplacent.

[include:applet_am_modulator]
</webonly>

<indepth>
Un signal AM peut également être décrit mathématiquement. Pour cela, considérons d’abord un signal BF sinusoïdal normalisé

$m(t)=\cos(\omega t)$

avec la pulsation $\omega=2\pi f_\mathrm{m}$. Avec son amplitude $\hat U_\mathrm{m}$ et une composante continue supplémentaire $U_\mathrm{G}$, on obtient

$U_\mathrm{m}(t)=U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)$

Ce signal est ensuite multiplié par le signal porteur haute fréquence

$U_\mathrm{T}(t)=\cos(\Omega t)$

avec $\Omega=2\pi f_\mathrm{T}$. Pour le signal AM, on obtient ainsi :

$U_\mathrm{AM}(t)=\left(U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)\right)\cdot\cos(\Omega t)$

En développant, on obtient :

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\hat U_\mathrm{m}\cdot\cos(\omega t)\cdot\cos(\Omega t)$

En utilisant la relation

$\cos(a)\cdot\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$

le deuxième terme peut être décomposé comme suit :

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\frac{\hat U_\mathrm{m}}{2}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

On reconnaît ainsi directement les trois composantes d’un signal AM : le premier terme décrit la *porteuse* à la fréquence $\Omega$. Les deux autres termes forment les *bandes latérales supérieure et inférieure* aux fréquences $\Omega+\omega$ et $\Omega-\omega$.

La composante continue $U_\mathrm{G}$ est responsable du maintien de la porteuse. Même si le signal utile est momentanément nul, un signal porteur est toujours généré.

[picture:1127:a_am_modulation:Spectre d’un signal AM avec porteuse et deux bandes latérales]

</indepth>

Ce principe est illustré dans la question suivante : une diode est soumise simultanément à un signal BF et à un signal HF, et le signal de sortie est filtré à l’aide d’un circuit LC oscillant.

[question:AD507]

---

Avec quatre diodes disposées en anneau, on peut concevoir un modulateur de telle sorte que la porteuse soit supprimée à la sortie. Un tel circuit a déjà été présenté dans le chapitre « Mélangeurs II » sous le nom de *mélangeur équilibré*. Il y était utilisé pour convertir un signal HF en une fréquence intermédiaire. Dans l’émetteur, nous utilisons le même principe de base pour générer un signal modulé.

<margin>
[picture:759:a_balancemodulator:Modulateur équilibré avec anneau de diodes]
</margin>

On reconnaît généralement un mélangeur équilibré ou un modulateur équilibré à l’anneau de diodes, comme illustré dans la figure [ref:a_balancemodulator]. L’anneau de diodes est commandé par le signal de l’oscillateur à la fréquence $f_\mathrm{OSZ}$. Selon la polarité du signal de l’oscillateur, une des deux paires de diodes opposées conduit.

Ainsi, le signal BF est transmis à la sortie alternativement avec la même polarité ou une polarité inversée. Simplifié, on peut dire que le signal BF est multiplié par le signal de l’oscillateur.

L’avantage décisif de ce circuit symétrique est la *suppression de la porteuse* : les composantes du signal de l’oscillateur s’annulent idéalement à la sortie. Sans signal BF, aucun signal de sortie n’est donc généré. En revanche, si un signal BF est appliqué, les bandes latérales supérieure et inférieure sont générées, tandis que la porteuse est supprimée.

Le signal de sortie est appelé *signal à double bande latérale avec porteuse supprimée* (DSB).

[question:AE206]
[question:AF302]
[question:AF308]
[question:AD510]

<indepth>
La suppression de la porteuse d’un modulateur équilibré peut être décrite de manière simplifiée avec deux branches symétriques :

$u_1(t)=\left(U_G+\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

$u_2(t)=\left(U_G-\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

Les deux signaux sont soustraits à la sortie :

$u_\mathrm{out}(t)=u_1(t)-u_2(t)$

On obtient ainsi :

$u_\mathrm{out}(t)=U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)-U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Les deux composantes porteuses $U_G\cos(\Omega t)$ s’annulent. Il reste :

$u_\mathrm{out}(t)=2\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Avec $\cos(a)\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$, on obtient :

$u_\mathrm{out}(t)=\hat U_\mathrm{m}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

Le signal de sortie ne contient donc plus que les bandes latérales supérieure et inférieure. La porteuse à $\Omega$ est supprimée.
</indepth>

---

Pour que le signal de l’oscillateur s’annule le plus possible à la sortie, le circuit doit être symétrique, c’est-à-dire *équilibré*. De petites différences d’amplitude ou de phase entre les deux voies de signal entraînent qu’une partie de la porteuse subsiste à la sortie. L’équilibrage de l’amplitude peut par exemple être réalisé avec un potentiomètre. Pour l’ajustement de phase, certains circuits utilisent en plus un condensateur ajustable. L’objectif de cet ajustement est d’obtenir une suppression de la porteuse aussi élevée que possible, tout en conservant les deux bandes latérales de modulation.

<webonly>
L’applet suivant montre l’ajustement de la porteuse. Si le curseur est déplacé vers la droite, la porteuse apparaît soudainement dans le spectre.

[include:applet_dsp]
</webonly>

[question:AF309]

---

Le modulateur équilibré constitue le premier étage d’un modulateur BLU et génère un signal DSB. En aval du modulateur équilibré, un filtre passe-bande étroit, comme illustré dans la figure [ref:a_ssb_modulation], suit comme deuxième étage. Il ne laisse passer qu’une seule des deux bandes latérales et supprime l’autre. On obtient ainsi à la sortie un signal BLU (bande latérale unique).

<margin>
[picture:500:a_ssb_modulation:Schéma bloc pour la modulation BLU avec la méthode de filtrage]
</margin>

[question:AF306]
[question:AF304]
[question:AF303]
[question:AF305]

---

Une bonne implémentation pour un appareil radio capable de générer à la fois USB et LSB consiste à concevoir le filtre passe-bande pour une plage de fréquences fixe. Le choix entre la bande latérale supérieure ou inférieure à filtrer n’est pas déterminé par une modification du filtre, mais par la fréquence de l’oscillateur dans le modulateur équilibré. Pour cela, deux oscillateurs à quartz différents sont disponibles.

Par exemple, pour l’USB, on choisit la fréquence de l’oscillateur à $\qty{8998,5}{\kilo\hertz}$. La modulation génère alors deux bandes latérales. La bande latérale supérieure est déplacée exactement dans la bande passante constante du filtre, tandis que la bande latérale inférieure se situe en dehors de la bande passante et est supprimée.

Pour le LSB, on commute sur l’autre fréquence de quartz de $\qty{9001,5}{\kilo\hertz}$. Le spectre DSB entier est ainsi décalé de sorte que la bande latérale inférieure tombe dans la bande passante du même filtre et que la bande latérale supérieure soit supprimée.

L’astuce consiste donc à laisser le filtre inchangé et à décaler la position du signal DSB en utilisant différentes fréquences d’oscillateur. Comme pour la fréquence intermédiaire d’un récepteur, un filtre fixe de haute qualité peut ainsi être utilisé pour différentes positions de fréquence.

[question:AF307]

<margin>
<latexonly>
[picture:831:a_ssb_modulation_lsb:Fréquences avec la méthode de filtrage en LSB]
[picture:940:a_ssb_modulation_lsb:Spectre avec la méthode de filtrage en LSB]
[picture:832:a_ssb_modulation_usb:Fréquences avec la méthode de filtrage en USB]
[picture:941:a_ssb_modulation_usb:Spectre avec la méthode de filtrage en USB]
</latexonly>
<webonly>
[include:applet_dsp_filter]
</webonly>
</margin>

---

Pour générer un signal modulé en fréquence (FM), on peut utiliser une *diode à capacité variable*. Dans les schémas, elle est reconnaissable au petit symbole de condensateur à côté de la diode, comme illustré dans la figure [ref:a_fm_modulator].

Une diode à capacité variable fonctionne en polarisation inverse. Sa capacité dépend de la tension inverse appliquée. Si elle est utilisée comme partie du circuit oscillant déterminant la fréquence d’un oscillateur, une variation de cette tension modifie la fréquence de résonance du circuit oscillant et donc la fréquence de l’oscillateur.

Pour la modulation de fréquence, le signal BF est superposé à la tension continue aux bornes de la diode à capacité variable. Ainsi, sa capacité varie au rythme du signal BF et la fréquence de l’oscillateur est décalée vers le haut et vers le bas en conséquence. Un signal modulé en fréquence est ainsi généré.

<margin>
[picture:155:a_fm_modulator:Modulateur FM avec diode à capacité variable]
</margin>

[question:AD508]
[question:AF310]

---

Avec des tensions BF élevées, il est facile d’obtenir des variations de fréquence de l’oscillateur (excursion FM) plus importantes que ce qui est autorisé. C’est pourquoi une *limitation de l’excursion* est nécessaire, en ajustant et limitant l’amplitude du signal BF. Des diodes montées en antiparallèle limitent la tension à environ la tension de seuil de la diode. Un exemple est montré dans les figures [ref:a_fm_modulator_hub1] et [ref:a_fm_modulator_hub2].

<margin>
[picture:44:a_fm_modulator_hub1:Circuit de limitation de l’excursion]
[picture:828:a_fm_modulator_hub2:Limitation du signal]
</margin>

[question:AD509]