Dans les sections [sec:transistor_1] et [sec:transistor_2] sur les transistors, nous avons déjà appris qu'avec un petit courant de base $I_\text{B}$, on peut contrôler un courant de collecteur $I_\text{C}$ nettement plus grand. Ce principe peut être utilisé pour construire un amplificateur pour signaux électriques. Selon le type de circuit, les transistors peuvent amplifier toutes sortes de signaux – qu'il s'agisse de signaux numériques, de signaux basse fréquence (BF) ou haute fréquence (HF). Une amplification signifie que la puissance de sortie d'un signal est supérieure à sa puissance d'entrée, ce qui constitue la caractéristique fondamentale d'un amplificateur.

---

La figure [ref:e_nf_verstaerker] montre un amplificateur basse fréquence (amplificateur BF) destiné à amplifier les signaux audio de l'appareil radio pour un haut-parleur. Cela est facilement reconnaissable au symbole du haut-parleur dans le circuit. Les amplificateurs de puissance HF sont utilisés, par exemple, pour augmenter le signal d'émission.

<margin>
[picture:763:e_nf_verstaerker:Schéma d'un amplificateur BF]
</margin>

[question:ED402]
[question:ED403]

Puisque la puissance de sortie augmente par rapport à la puissance d'entrée, un amplificateur doit toujours être alimenté en énergie. Une source de tension capable de supporter la charge est donc nécessaire.

[question:ED401]

---

Pour qu'un amplificateur soit qualifié de *linéaire*, il doit posséder la propriété suivante : si le signal d'entrée double, le signal de sortie de l'amplificateur double également.
Les écarts de linéarité sont généralement indésirables et ne sont tolérables que pour des modes de fonctionnement comme la FM (où l'information du signal n'est pas transmise par l'amplitude, mais uniquement par la fréquence). Si un amplificateur ne fonctionne pas de manière linéaire, son signal de sortie contient des fréquences qui ne sont pas présentes dans le signal d'entrée (appelées splatter). Dans le domaine BF, ce comportement se manifeste par une distorsion. Dans le domaine HF, des harmoniques du signal amplifié apparaissent. Les deux sont indésirables. La figure [ref:e_verstaerker_linearitaet] montre, à titre d'exemple, comment un signal sinusoïdal est déformé par un comportement non linéaire.

<margin>
[picture:828:e_verstaerker_linearitaet:Le signal d'entrée est amplifié. En cas de limitation due à un manque de linéarité, le signal de sortie est déformé.]
</margin>

[question:EF403]

Pour la linéarité d'un émetteur, une alimentation électrique stabilisée et découplée des autres étages est également nécessaire pour éviter des rétroactions indésirables.

[question:EF405]

On trouve des amplificateurs BF non seulement au haut-parleur de l'appareil radio, mais aussi déjà au microphone. Ils servent ici, par exemple, à amplifier le signal du microphone. Généralement, les composantes de fréquence plus basses (en dessous de $\qty{300}{\hertz}$) et plus élevées (au-dessus de $\qty{3}{\kilo\hertz}$) du signal du microphone sont déjà supprimées à l'intérieur de l'amplificateur de microphone par une caractéristique passe-bande, afin de limiter la bande passante du signal BF et de supprimer les composantes de basse fréquence comme le ronflement du secteur (cf. figure [ref:e_frequenzgang_mikrofonverstaerker]). Pour une bonne intelligibilité de la parole en communication vocale, une bande passante BF d'environ $\qtyrange{2,5}{3}{\kilo\hertz}$ est nécessaire.

<margin>
[picture:246:e_frequenzgang_mikrofonverstaerker:Réponse en fréquence typique pour un amplificateur de microphone de radioamateurisme]
</margin>

[question:EF308]
[question:EF307]
