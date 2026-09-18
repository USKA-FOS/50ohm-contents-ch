Dans la classe N, nous avons déjà étudié le *S-mètre* sous sa forme analogique (fig. [ref:a_s_meter_analog]) et sous sa forme numérique (fig. [ref:a_s_meter_digital]).* Il sert à indiquer la force du signal HF présent à l'entrée du récepteur.

L'échelle d'un S-mètre s'étend généralement de S1 à S9. Une variation d'une *points S* correspond à $\qty{6}{\dB}$. Les signaux plus forts que S9 ne sont plus indiqués en points S supplémentaires, mais en décibels au-dessus de S9, par exemple « S9 + $\qty{20}{\dB}$ ».

Comme l'échelle en décibels est logarithmique, une augmentation de $\qty{6}{\dB}$ correspond à un doublement de la tension d'entrée ou à une multiplication par quatre de la puissance d'entrée. À l'inverse, une réduction de $\qty{6}{\dB}$ correspond à une division par deux de la tension ou à une division par quatre de la puissance.

<margin>
[picture:578:a_s_meter_digital:Le chiffre 2 montre le S-mètre numérique d'un émetteur-récepteur]
[picture:420:a_s_meter_analog:S-mètre analogique d'un émetteur-récepteur]
</margin>

[question:AF101]
[question:AF104]
[question:AF103]
[question:AA113]
[question:AF102]

---

Dans la bande des ondes courtes jusqu'à $\qty{30}{\mega\hertz}$, une valeur S de S9 correspond exactement à $\qty{50}{\micro\volt}$ sur $\qty{50}{\ohm}$.
À partir de la bande VHF ($
\qty{144}{\mega\hertz}$), une valeur S de S9 correspond exactement à $\qty{5}{\micro\volt}$ sur $\qty{50}{\ohm}$.

<tip>
Les S-mètres des appareils ondes courtes n'affichent généralement des valeurs fiables qu'autour de S9, car ils sont souvent calibrés uniquement pour cette valeur. En particulier, les valeurs plus faibles ne sont indiquées qu'avec une faible précision. La caractéristique logarithmique d'un S-mètre est souvent mal interpolée. Une valeur S de S0 n'existe pas par définition, car il y a toujours un bruit de fond ou un bruit propre du récepteur. Si le S-mètre n'affiche aucune valeur dans la partie inférieure de l'échelle, le signal reçu est très faible, mais il n'atteint jamais la valeur S0. Cette valeur ne doit donc pas être transmise.
</tip>

[question:AA114]
[question:AF105]