Les antennes multibandes, conçues pour être résonantes sur plusieurs bandes, ont déjà été présentées, par exemple l’antenne à alimentation terminale avec un transformateur 1:49. Revenons à notre exemple de la section « Alimentation en courant et en tension II » : un dipôle demi-onde alimenté au centre peut, en plus de sa fréquence fondamentale, être résonant sur des multiples impairs de cette fréquence. Ainsi, par exemple, un dipôle conçu pour la bande des 80 m avec une fréquence fondamentale de 3,5 MHz possède d’autres résonances proches de 10,5 MHz et 17,5 MHz.


Aux multiples pairs de la fréquence fondamentale, par exemple à 7 MHz ou 14 MHz, il y a en revanche un minimum de courant au point d’alimentation central et donc une impédance élevée. Ces fréquences ne sont donc pas directement exploitables avec un dipôle alimenté au centre simple. Une solution pour créer des résonances supplémentaires à ces fréquences consiste à utiliser un *dipôle à trappes*, aussi appelé *dipôle à circuit bouchon*.


Dans un dipôle à trappes, chaque moitié du dipôle contient au moins un circuit oscillant parallèle composé d’une bobine et d’un condensateur. Un tel circuit oscillant est appelé *trappe* (en anglais *trap*). Un circuit oscillant parallèle est à haute impédance à sa fréquence de résonance (cf. figure [ref:a_sperrkreis]). Il agit alors comme un *circuit bouchon* et empêche presque tout courant de circuler dans la partie extérieure du dipôle. Ainsi, le même dipôle peut présenter différentes longueurs électriques sur plusieurs bandes de fréquences.


<margin>
[picture:1036:a_sperrkreis:Réponse en fréquence qualitative d’un circuit oscillant parallèle (circuit bouchon)]
</margin>

[question:AG109]
[question:AG110]

---

L’effet d’une trappe sur le dipôle dépend du rapport entre la fréquence de fonctionnement et sa fréquence de résonance $f_\mathrm{res}$.


* À $f=f_\mathrm{res}$, le circuit oscillant parallèle est à haute impédance et agit comme un circuit bouchon. La partie extérieure du dipôle est ainsi largement isolée de la partie intérieure.
* À $f<f_\mathrm{res}$, l’effet inductif de la trappe prédomine. Elle agit alors comme une bobine de rallonge et allonge électriquement le radiateur.
* À $f>f_\mathrm{res}$, l’effet capacitif de la trappe prédomine. Le radiateur est alors légèrement raccourci électriquement.


<margin>
Dans cette applet, on peut étudier l’effet d’une trappe sur un dipôle pour différentes fréquences :


[include:applet_traps]
</margin>

Le cas de résonance est particulièrement parlant. Si le dipôle fonctionne à la fréquence de résonance de la trappe (par exemple 7,05 MHz dans notre figure), le circuit oscillant parallèle est à haute impédance. Peu de courant circule donc dans la partie extérieure du dipôle. Le dipôle se comporte alors approximativement comme s’il se terminait à l’emplacement de la trappe.

[question:AG112]


Cette relation peut être exploitée pour concevoir un dipôle bi-bande. Pour la bande à plus haute fréquence, l’écartement entre les deux trappes détermine principalement la longueur efficace du dipôle. À cette fréquence, les morceaux de fil extérieurs sont largement isolés par l’effet de blocage des trappes, comme s’ils n’existaient pas, et le dipôle se comporte comme un dipôle plus court.

[question:AG116]


---

Si le dipôle fonctionne à une fréquence *inférieure* à la fréquence de résonance de la trappe (par exemple 3,5 MHz dans notre figure), le circuit oscillant n’est plus à haute impédance. Son effet inductif prédomine. La trappe agit alors comme une bobine de rallonge et allonge électriquement le dipôle. Ainsi, l’ensemble du dipôle, y compris les morceaux de fil extérieurs, peut être utilisé pour une bande de fréquence plus basse.

[question:AG111]


---

À une fréquence *supérieure* à la fréquence de résonance, l’effet capacitif de la trappe prédomine. La trappe agit alors comme un raccourcisseur électrique et peut même rendre le dipôle résonant, par exemple à 14 MHz. Cet effet doit également être pris en compte lors du dimensionnement d’un dipôle à trappes.

[question:AG113]


---

En utilisant plusieurs paires de trappes, on peut concevoir des dipôles pour encore plus de bandes de fréquences. Les trappes pour les fréquences les plus élevées sont placées le plus près du centre, car elles nécessitent la longueur électrique la plus courte.


La trappe la plus intérieure est donc accordée sur la fréquence la plus élevée prévue. La paire de trappes suivante, plus extérieure, est accordée sur la fréquence immédiatement inférieure, et ainsi de suite. Plus la fréquence de fonctionnement est basse, plus les parties du dipôle deviennent efficaces.

[question:AG115]
[question:AG114]


Les trappes ne sont pas utilisées uniquement dans les antennes dipôles. On les retrouve aussi dans les antennes directives comme les antennes Yagi, où des circuits bouchons sont intégrés dans les différents éléments pour permettre leur utilisation sur plusieurs bandes de fréquences.