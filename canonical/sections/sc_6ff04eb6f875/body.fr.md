La *Synthèse numérique directe*, en anglais *Direct Digital Synthesis* ou DDS [index:Synthèse numérique directe] [index:DDS], sert à générer des signaux périodiques avec une fréquence réglable de manière très fine. Aujourd’hui, elle est utilisée, en plus de la synthèse de fréquence par circuits PLL, dans les équipements modernes de radioamateur. Un avantage majeur de la DDS réside dans le fait que la fréquence de sortie peut être réglée numériquement avec une résolution très élevée. De plus, il est possible de basculer très rapidement entre différentes fréquences, car il n’est pas nécessaire d’attendre qu’une boucle de régulation se stabilise sur une nouvelle fréquence, comme c’est le cas avec une PLL classique.

<margin>
[picture:1082:a_dds_aufbau:Schéma bloc d’une DDS (Direct Digital Synthesizer)]
</margin>

La structure de base d’une DDS est illustrée dans [ref:a_dds_aufbau]. Un générateur d’horloge produit un signal d’horloge à une fréquence fixe $f_\mathrm{Takt}$. À chaque impulsion d’horloge, un accumulateur de phase [index:DDS:Accumulateur de phase], aussi appelé compteur d’adresses, augmente sa valeur de phase actuelle de l’incrément de phase $K$ :

$\varphi_{n+1} = \varphi_n + K$

L’incrément de phase $K$ est également désigné par *Tuning Word*. Il détermine de combien de pas de phase l’accumulateur de phase est incrémenté à chaque impulsion d’horloge. La valeur actuelle de l’accumulateur de phase sert d’adresse pour une table de valeurs, aussi appelée *table de consultation* (*Lookup-Tabelle*). Pour générer une oscillation sinusoïdale, cette table contient les valeurs d’amplitude numériques d’une période sinusoïdale complète. Pour chaque valeur de phase, la valeur d’amplitude correspondante est extraite de la table de sinus. L’incrément de phase $K$ détermine la vitesse à laquelle la table de sinus est parcourue, et donc la fréquence du signal de sortie. L’incrément de phase peut, par exemple, être contrôlé par un microcontrôleur. Un registre reprend la valeur d’amplitude numérique de manière synchrone avec le signal d’horloge et la transmet à un convertisseur numérique-analogique (DAC). Ce dernier convertit la séquence des valeurs d’amplitude numériques en un signal analogique, d’abord en escalier. Un filtre passe-bas en aval élimine les composantes haute fréquence indésirables et lisse le signal de sortie.

---

L’exemple suivant illustre ce principe : avec un incrément de phase $K=1$, la valeur de phase est incrémentée d’un pas à chaque impulsion d’horloge ($\varphi_{n+1} = \varphi_n + 1$). La table de sinus est ainsi parcourue pas à pas. Une fois qu’une période complète est générée, le compteur d’adresses est réinitialisé et l’accumulateur de phase recommence depuis le début. Le signal de sortie obtenu est représenté dans [ref:a_dds_phaseninkrement_k1].

<margin>
[picture:1083:a_dds_phaseninkrement_k1:Signal de comparaison]
</margin>

---

Si l’incrément de phase est doublé à $K=2$, la valeur de phase est incrémentée de deux pas à chaque impulsion d’horloge ($\varphi_{n+1} = \varphi_n + 2$). Ainsi, une valeur de phase sur deux est appelée, et la table de sinus est parcourue deux fois plus vite. La durée d’une période du signal de sortie est divisée par deux, et sa fréquence est doublée. Cela est illustré dans [ref:a_dds_phaseninkrement_k2].

<margin>
[picture:1084:a_dds_phaseninkrement_k2:Incrément de phase doublé et fréquence de sortie doublée]
</margin>

[question:AD620]

<indepth>
Si l’accumulateur de phase a une largeur de $N$ bits, il peut représenter $2^N$ valeurs de phase différentes. Lorsqu’il dépasse la valeur maximale, le compteur se réinitialise et recommence depuis le début :

$\varphi_{n+1} = \left(\varphi_n + K\right) \bmod 2^N$

Ce dépassement correspond à la transition de $\qty{360}{\degree}$ à $\qty{0}{\degree}$. L’incrément de phase $K$ peut être choisi presque arbitrairement et ne doit pas nécessairement être une puissance de deux. Cela permet de générer des fréquences de sortie qui ne sont pas des diviseurs entiers de la fréquence d’horloge.

Une DDS n’est pas non plus limitée aux oscillations sinusoïdales. Si la table de valeurs contient, par exemple, les valeurs d’amplitude d’une oscillation triangulaire ou en dents de scie, la DDS peut également générer ces formes d’onde.

La qualité du signal de sortie dépend principalement de la stabilité et du *jitter* [index:Jitter] du générateur d’horloge, ainsi que de la résolution et de la linéarité du convertisseur numérique-analogique. En raison du nombre limité de valeurs de phase et d’amplitude, des erreurs de quantification et des composantes spectrales supplémentaires apparaissent. Un filtre passe-bas en aval supprime une grande partie de ces composantes indésirables du signal.
</indepth>