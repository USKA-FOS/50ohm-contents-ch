Dans le chapitre consacré aux transistors, nous avons déjà appris qu’un petit courant de base $I_\text{B}$ permet de contrôler un courant de collecteur $I_\text{C}$ bien plus important. Ce principe peut être exploité pour concevoir un amplificateur de signaux électriques. Selon le type de circuit utilisé, les transistors permettent d’amplifier toutes sortes de signaux : signaux numériques, signaux audio (BF) ou signaux haute fréquence (HF). L’amplification se caractérise par le fait que la puissance de sortie d’un signal est supérieure à sa puissance d’entrée, ce qui constitue la propriété fondamentale d’un amplificateur.

---

L’illustration [ref:e_nf_verstaerker] montre un amplificateur audio (amplificateur BF) conçu pour amplifier les signaux audio issus d’un appareil radio en vue de les envoyer vers un haut-parleur. Cela se reconnaît facilement grâce au symbole du haut-parleur dans le circuit. Les amplificateurs de puissance HF sont par exemple utilisés pour augmenter le signal d’émission.

<margin>
[picture:763:e_nf_verstaerker:Schéma d’un amplificateur BF]  
</margin>

[question:ED402]
[question:ED403]

Puisque la puissance de sortie est supérieure à la puissance d’entrée, un amplificateur doit toujours recevoir de l’énergie. Il nécessite donc une source de tension suffisamment robuste.

[question:ED401]

---

Pour qu’un amplificateur soit qualifié de *linéaire*, il doit présenter la propriété suivante : si le signal d’entrée est doublé, le signal de sortie doit également être doublé. Les écarts à la linéarité sont généralement indésirables et ne sont tolérés que dans certains modes de fonctionnement comme la FM (où l’information du signal n’est pas transmise par l’amplitude, mais uniquement par la fréquence). Si un amplificateur fonctionne de manière non linéaire, des fréquences qui n’étaient pas présentes dans le signal d’entrée apparaissent dans son signal de sortie (appelées *splatter*). En audio, ce comportement se manifeste par des distorsions. En haute fréquence, il génère des harmoniques du signal amplifié. Dans les deux cas, cela est indésirable. L’illustration [ref:e_verstaerker_linearitaet] montre par exemple comment un signal sinusoïdal est déformé par un comportement non linéaire.

<margin>
[picture:828:e_verstaerker_linearitaet:Le signal d’entrée est amplifié. En cas de limitation due à un manque de linéarité, le signal de sortie est déformé.]
</margin>

[question:EF403]

Pour garantir la linéarité d’un émetteur, il est également nécessaire de disposer d’une alimentation électrique stabilisée et découplée des autres étages afin d’éviter les rétroactions indésirables.

[question:EF405]

Les amplificateurs BF ne se trouvent pas uniquement au niveau du haut-parleur d’un appareil radio, mais aussi dès le microphone. Dans ce cas, ils servent par exemple à amplifier le signal du microphone. Généralement, les composantes de fréquence basses (inférieures à $\qty{300}{\hertz}$) et hautes (supérieures à $\qty{3}{\kilo\hertz}$) du signal du microphone sont déjà supprimées par l’amplificateur du microphone grâce à une réponse en fréquence de type passe-bande, afin de limiter la bande passante du signal BF et d’éliminer les composantes de fréquence basse comme le ronflement du secteur (cf. illustration [ref:e_frequenzgang_mikrofonverstaerker]). Pour une bonne intelligibilité de la voix en communication radioamateur, une bande passante audio d’environ $\qtyrange{2,5}{3}{\kilo\hertz}$ est requise.

<margin>
[picture:246:e_frequenzgang_mikrofonverstaerker:Réponse en fréquence typique d’un amplificateur de microphone pour radioamateur]
</margin>

[question:EF308]
[question:EF307]