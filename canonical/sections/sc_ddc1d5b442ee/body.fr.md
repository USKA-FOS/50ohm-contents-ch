La *précision de fréquence* indique dans quelle mesure une fréquence générée, réglée ou mesurée peut s’écarter de sa valeur réelle. Elle est souvent exprimée en pourcentage ($\unit{\percent}$), en *parts per million* ($\unit{\ppm}$) ou directement comme écart relatif.

Dans ce cas, on a :

$\qty{1}{\percent} = 1 \cdot 10^{-2}$

et

$\qty{1}{\ppm} = 1 \cdot 10^{-6}$


Pour un fréquencemètre, la précision atteignable dépend principalement de sa *base de temps*. Le fréquencemètre détermine la fréquence du signal d’entrée à l’aide d’une fréquence de référence interne. Si cette référence s’écarte de sa valeur nominale, cet écart se répercute directement sur le résultat de la mesure.

Pour cette raison, on utilise des oscillateurs aussi stables que possible comme base de temps. Les fréquencemètres de haute qualité emploient par exemple un TCXO ou un OCXO. Pour des mesures particulièrement précises, il est souvent possible de connecter une référence de fréquence externe, par exemple un oscillateur synchronisé par GPS (GPSDO).


Si la précision relative de la fréquence est connue, on peut calculer l’écart maximal de fréquence attendu :

$\Delta f = f \cdot a$


Ici, $f$ représente la fréquence considérée et $a$ la précision relative de la fréquence.


<indepth>
  Remarque concernant la conversion/la représentation des puissances de 10 :
  
  $1 \cdot {\num{10^{-2}}} = \frac{1}{\num{10^2}}$
  $1 \cdot {\num{10^{-6}}} = \frac{1}{\num{10^6}}$
  
  etc.
</indepth>
  
[question:AA115]

[question:AA116]

[question:AI508]

[question:AI509]

[question:AI510]

[question:AI506]

[question:AI507]
