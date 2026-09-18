Les circuits intégrés sont des circuits complexes réalisés sur un substrat semiconducteur. Ils constituent une aide essentielle pour la réalisation de circuits électroniques.

[question:AC601]

<margin>
[photo:334:a_ic:Émetteur ondes courtes TinyWhisper de la JKU Linz et de la JMU Würzburg, réalisé sous forme de circuit intégré en technologie CMOS 130 nm]
</margin>

Une classe particulière de circuits intégrés est celle des Monolithic Microwave Integrated Circuits (MMIC). Ils intègrent à la fois des composants actifs et passifs sur le même substrat. Ces circuits sont généralement conçus pour une impédance d'entrée et de sortie de $\qty{50}{\ohm}$. Ils permettent d'obtenir un gain large bande élevé avec peu de composants.

[question:AC602]
[question:AC603]
[question:AC604]

---

Pour résoudre les exercices de l'examen, il est utile d'examiner plus en détail le circuit de la figure [ref:a_mmic].

Les condensateurs $C_1$ et $C_3$ servent de condensateurs de couplage. Ils laissent passer les signaux HF mais bloquent la tension continue. Cela empêche la transmission de tensions continues entre les différents étages du circuit et d'influencer le point de fonctionnement.

La bobine d’arrêt sur la ligne d’alimentation de service $U_\mathrm{CC}$ empêche les signaux HF de s’échapper par l’alimentation électrique. Pour la haute fréquence, la bobine d’arrêt présente une impédance élevée et agit donc comme un blocage. Le condensateur $C_2$ sert au découplage HF de la tension d’alimentation. Il évacue les composantes HF résiduelles vers la masse et assure la stabilité HF de la tension d’alimentation. Associé à la bobine d’arrêt, il forme un découplage HF de l’alimentation de service. Ce circuit sera étudié plus tard sous le nom de "Bias-T".

Une particularité de nombreux MMIC est que la tension de service est fournie par la sortie. La résistance $R_\text{BIAS}$ permet de régler le point de fonctionnement du MMIC.

<margin>
[picture:773:a_mmic:Circuit MMIC]
</margin>

Selon l'énoncé, on peut d'abord déterminer la chute de tension aux bornes du MMIC, puis celle aux bornes de la résistance $R_\text{BIAS}$. Avec la valeur connue de la résistance, on peut ensuite calculer le courant traversant le circuit. Ce même courant circule également dans le MMIC, ce qui permet par exemple de déterminer la puissance dissipée thermique.

Les exercices suivants peuvent donc être résolus de manière très similaire aux circuits déjà connus avec des transistors bipolaires.

[question:AF425]
[question:AF426]
[question:AF427]

% Une aide précieuse pour la réalisation de circuits électroniques est l'utilisation de circuits intégrés.
% Un circuit intégré contient dans un boîtier un circuit électronique complexe,
% fabriqué sur une puce.

% "Info supplémentaire" Applications pratiques :
% Amplificateurs opérationnels : voir section ...
% Amplificateurs basse fréquence : voir section ...
% Amplificateurs micro-ondes MMIC : voir section ...
% Circuits mélangeurs et oscillateurs combinés : voir section ...
% Récepteurs complets : voir section ...
% Circuits numériques : voir section ...
% Circuits PLL : voir section ...

% Avec quelques composants externes, on peut réaliser par exemple un amplificateur audio, un oscillateur avec mélangeur ou même un récepteur ondes courtes complet.
% Image d'un CI avec désignation de type et schéma bloc, par exemple LM386
% Pour les fréquences à partir d'environ 100 MHz, on utilise des circuits intégrés monolithiques pour micro-ondes (MMIC).
% Image MMIC MSA 0686 ou ERA 3
% Il s'agit d'un amplificateur capable d'amplifier une bande de fréquences de 100 MHz à 2 GHz de 20 dB
% et adapté en entrée et en sortie pour une charge de 50 ohm.
% Il suffit de régler le courant du point de fonctionnement selon la fiche technique pour éviter toute surchauffe thermique du MMIC.
% Pour cela, avec une tension de service donnée, il faut calculer une résistance et sa charge électrique.

% Comme le MMIC est un boîtier pour la technique CMS, il est nécessaire d'utiliser également un câblage externe en technique CMS.
% La structure globale de l'amplificateur sera donc bien plus petite qu'avec une technique de circuit discret.
% Image comparaison circuit discret et MMIC