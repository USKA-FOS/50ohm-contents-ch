Dans le chapitre sur les transistors, nous avons déjà appris qu'un petit courant de base $I_\text{B}$ permet de contrôler un courant de collecteur $I_\text{C}$ nettement plus important. Ce principe peut être utilisé pour construire un amplificateur de signaux électriques. Selon le type de circuit, les transistors peuvent amplifier des signaux de toutes sortes - qu'il s'agisse de signaux numériques, de signaux basse fréquence (BF) ou haute fréquence (HF). Une amplification signifie que la puissance de sortie d'un signal est supérieure à sa puissance d'entrée, ce qui constitue la caractéristique fondamentale d'un amplificateur.

---

La figure [ref:e_nf_verstaerker] montre un amplificateur basse fréquence (amplificateur BF) qui doit amplifier les signaux audio de l'appareil radio pour un haut-parleur. Cela se voit facilement au symbole du haut-parleur dans le circuit. Les amplificateurs de puissance HF sont utilisés, par exemple, pour augmenter le signal d'émission.

<margin>
[picture:763:e_nf_verstaerker:Schaltbild eines NF-Verstärkers]  
</margin>

[question:ED402]
[question:ED403]

Comme la puissance de sortie est supérieure à la puissance d'entrée, un amplificateur doit toujours être alimenté en énergie. Il est donc nécessaire de disposer d'une source de tension suffisamment robuste.

[question:ED401]

---

Pour qu'un amplificateur puisse être désigné comme *linéaire*, il doit avoir la propriété que lorsque le signal d'entrée est doublé, le signal de sortie de l'amplificateur est également doublé.
Les écarts de linéarité sont généralement indésirables et ne sont tolérés que dans les modes de fonctionnement comme la FM (où l'information du signal n'est pas transmise via l'amplitude, mais uniquement via la fréquence). Si un amplificateur ne fonctionne pas de manière linéaire, des fréquences qui ne sont pas présentes dans le signal d'entrée sont présentes dans son signal de sortie (appelé splatter). Dans la plage BF, ce comportement se manifeste par une distorsion. Dans la plage HF, des harmoniques du signal amplifié sont générées. Les deux sont indésirables. La figure [ref:e_verstaerker_linearitaet] montre à titre d'exemple comment un signal sinusoïdal est déformé par un comportement non linéaire. 

<margin>
[picture:828:e_verstaerker_linearitaet:Das Eingangssignal wird verstärkt. Bei Begrenzung durch fehlende Linearität wird das Ausgangssignal verformt.]
</margin>

[question:EF403]

Pour la linéarité d'un émetteur, une alimentation en courant stabilisée et découplée des autres étages est également nécessaire pour éviter les rétroactions indésirables.

[question:EF405]

On ne trouve pas seulement des amplificateurs BF au niveau du haut-parleur de l'appareil radio, mais aussi déjà au niveau du microphone. Ceux-ci servent ici, par exemple, à amplifier le signal du microphone. Habituellement, les composantes de fréquence plus basses (inférieures à $\qty{300}{\hertz}$) et plus élevées (supérieures à $\qty{3}{\kilo\hertz}$) du signal du microphone sont déjà supprimées à l'intérieur de l'amplificateur du microphone par une caractéristique passe-bande, afin de limiter la bande passante du signal BF et de supprimer les composantes de fréquence plus basses comme, par exemple, le bourdonnement du réseau (cf. figure [ref:e_frequenzgang_mikrofonverstaerker]). Pour une bonne intelligibilité de la parole dans les communications vocales, une bande passante BF d'environ $\qtyrange{2,5}{3}{\kilo\hertz}$ est nécessaire.

<margin>
[picture:246:e_frequenzgang_mikrofonverstaerker:Typischer Frequenzgang für einen Amateurfunk-Mikrofonverstärker]
</margin>

[question:EF308]
[question:EF307]