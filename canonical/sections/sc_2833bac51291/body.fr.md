Les circuits intégrés sont des circuits complexes réalisés sur un substrat semi-conducteur. Ils constituent ainsi une aide précieuse pour la construction de circuits électroniques.

[question:AC601]

<margin>
[photo:334:a_ic:Émetteur TinyWhisper des ondes courtes de la JKU Linz et JMU Würzburg réalisé sous forme de circuit intégré en technologie CMOS 130 nm]
</margin>

Une classe spéciale de circuits intégrés est celle des Monolithic Microwave Integrated Circuits (MMIC). Ils combinent à la fois des composants actifs et passifs sur le même substrat. Ils sont généralement conçus pour une impédance d'entrée et de sortie de $\qty{50}{\ohm}$. Ils permettent une amplification à large bande avec peu de composants.

[question:AC602]
[question:AC603]
[question:AC604]

---

Pour calculer les exercices de l'examen, il est utile d'examiner d'abord plus en détail le circuit du schéma [ref:a_mmic].

Les condensateurs $C_1$ et $C_3$ servent de condensateurs de couplage. Ils laissent passer les signaux HF, mais bloquent la tension continue. Cela empêche que les tensions continues soient transmises entre les différents étages du circuit et influencent le point de fonctionnement.

La bobine dans la ligne de tension de service $U_\mathrm{CC}$ empêche que les signaux HF ne puissent s'écouler par l'alimentation électrique. Pour les hautes fréquences, la bobine présente une résistance élevée et agit donc comme un blocage. Le condensateur $C_2$ sert à bloquer les HF de la tension d'alimentation. Il dérive les composantes HF restantes vers la masse et assure que la tension d'alimentation reste stable en HF. Avec la bobine, il forme un découplage HF de la tension de service. Nous apprendrons plus tard à connaître ce circuit sous le nom de "Bias-T".

Une particularité de nombreux MMIC réside dans le fait que la tension d'alimentation est fournie par la sortie. La résistance $R_\text{BIAS}$ règle le point de fonctionnement du MMIC.

<margin>
[picture:773:a_mmic:Circuit MMIC]
</margin>

Selon l'énoncé de l'exercice, on peut d'abord déterminer la chute de tension sur le MMIC à partir de la chute de tension sur la résistance $R_\text{BIAS}$. Avec la valeur de résistance connue, on peut ensuite calculer le courant dans le circuit. Le même courant traverse également le MMIC, de sorte que l'on peut en déduire, par exemple, la puissance dissipée thermique.

Les exercices suivants peuvent donc être résolus de manière très similaire aux circuits déjà connus avec des transistors bipolaires.

[question:AF425]
[question:AF426]
[question:AF427]

% Une aide précieuse pour la construction de circuits électroniques 
% est l'utilisation de circuits intégrés.
% Un circuit intégré contient dans un boîtier un circuit électronique complexe, 
% qui a été fabriqué sur une puce.

% "Info supplémentaire" Applications pratiques:
% Amplificateur opérationnel : voir section ...
% Amplificateur basse fréquence : voir section ...
% Amplificateurs à micro-ondes MMIC : voir section ...
% Circuit mélangeur et oscillateur combiné : voir section ...
% Récepteurs complets : voir section ...
% Circuits numériques : voir section ...
% Circuits PLL : voir section ...

% Avec quelques composants externes, un amplificateur audio, un oscillateur avec mélangeur ou même un récepteur complet % des ondes courtes peut être réalisé.
% Image d'un IC avec désignation de type et schéma bloc par exemple LM386
% Pour les fréquences à partir d'environ 100 MHz, on utilise ce que l'on appelle les Monolithic Microwave Integrated Circuit (MMIC).
% Image MMIC MSA 0686 ou ERA 3
% Il s'agit d'un amplificateur qui peut amplifier à large bande la plage de fréquences de 100 MHz à 2 GHz de 20 dB
% et est adapté côté entrée et sortie pour une charge de 50 Ohm.
% Il suffit de régler le courant pour le point de fonctionnement selon la fiche technique, afin que le MMIC ne soit pas % surchargé thermiquement. 
% Pour cela, il faut calculer une résistance et sa charge électrique pour une tension de service donnée.

% Comme le MMIC possède un boîtier pour la technique SMD, il est nécessaire d'exécuter également le câblage extérieur en technique SMD.
% La structure globale de l'amplificateur sera ainsi nettement plus petite que précédemment en technique de circuit discret.
% Image Comparaison circuit discret et MMIC



