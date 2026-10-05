Dans la section [sec:rst], nous avons déjà rencontré le *S-mètre* à la fois dans sa version analogique (Fig. [ref:a_s_meter_analog]) et dans sa version numérique (Fig. [ref:a_s_meter_digital]). Il sert à afficher l'intensité du signal HF présent à l'entrée du récepteur.

L'échelle d'un S-mètre va généralement de S1 à S9. Un changement d'un point S correspond à $\qty{6}{\dB}$. Les signaux plus forts au-dessus de S9 ne sont plus indiqués en points S supplémentaires, mais en décibels au-dessus de S9, par exemple comme « S9 + $\qty{20}{\dB}$ ».

Comme l'échelle en décibels est logarithmique, une augmentation de $\qty{6}{\dB}$ correspond à un doublement de la tension d'entrée ou à un quadruplement de la puissance d'entrée. Inversement, une réduction de $\qty{6}{\dB}$ correspond à une réduction de moitié de la tension ou à un quart de la puissance.

<margin>
[picture:578:a_s_meter_digital:Le numéro 2 montre le S-mètre numérique d'un TRX]
[picture:420:a_s_meter_analog:S-mètre analogique d'un TRX]
</margin>

[question:AF101]
[question:AF104]
[question:AF103]
[question:AA113]
[question:AF102]

---

Dans la bande des ondes courtes jusqu'à $\qty{30}{\mega\hertz}$, une valeur S de S9 correspond exactement à $\qty{50}{\micro\volt}$ sur $\qty{50}{\ohm}$.
À partir de la bande VHF ($\qty{144}{\mega\hertz}$), une valeur S de S9 correspond exactement à $\qty{5}{\micro\volt}$ sur $\qty{50}{\ohm}$.

<tip>
Les S-mètres des appareils ondes courtes n'indiquent généralement les valeurs autour de S9 que de manière à peu près fiable, car ils sont souvent calibrés uniquement sur cette valeur. En particulier, les petites valeurs S sont indiquées très imprécisément. La caractéristique logarithmique d'un S-mètre est souvent interpolée de manière insuffisante. Par définition, il n'existe pas de valeur S de S0, car il y a toujours un bruit de fond ou un bruit propre du récepteur. Si le S-mètre n'affiche aucune valeur dans la partie inférieure, le signal reçu est très faible, mais il n'a jamais la valeur S0. Celle-ci ne devrait donc pas non plus être transmise.
</tip>

[question:AA114]
[question:AF105]
