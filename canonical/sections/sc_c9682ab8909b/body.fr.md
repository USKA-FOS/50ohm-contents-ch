Dans le chapitre précédent, nous avons vu qu’il existe différents types d’oscillateurs offrant une stabilité et une précision en fréquence variables. Les oscillateurs à quartz, notamment sous forme de TCXO et surtout d’OCXO, atteignent une stabilité particulièrement élevée. Les équipements radio modernes, par exemple, atteignent une précision de fréquence de $\pm\qty{0,5}{\ppm}$ avec un TCXO. Pour une fréquence souhaitée de $\qty{10}{\mega\hertz}$, la fréquence réelle se situe ainsi dans la plage de $\qtyrange{9,999995}{10,000005}{\mega\hertz}$, soit au maximum $\pm\qty{5}{\hertz}$ de la fréquence nominale. Cet écart est faible et généralement plus que suffisant pour une exploitation en ondes courtes.


Toutefois, si l’on travaille non pas à $\qty{10}{\mega\hertz}$, mais à $\qty{10}{\giga\hertz}$, l’écart possible s’élève à $\pm\qty{5000}{\hertz}$. Il peut alors déjà dépasser la bande passante d’un filtre SSB classique. Dans une liaison radio sur une fréquence convenue, le signal peut ainsi se situer en dehors de la plage de réception. Pour de telles applications, par exemple pour le satellite géostationnaire QO-100 qui émet à $\qty{10}{\giga\hertz}$, des références de fréquence encore plus précises sont donc nécessaires.


<margin>
[picture:1081:a_gpsdo:Oscillateur discipliné GPS (GPSDO) dans le contexte d’une station QO-100]
</margin>

On pourrait déployer de grands efforts pour stabiliser davantage un OCXO ou utiliser d’autres types d’oscillateurs comme les étalons de fréquence au rubidium, qui offrent une stabilité supérieure aux oscillateurs à quartz sur de plus longues périodes. Cependant, ces étalons présentent souvent des inconvénients tels qu’une consommation de courant plus élevée, des dimensions plus importantes et un prix plus élevé, car ils sont principalement conçus pour des applications professionnelles.


Heureusement, il existe une autre solution : les systèmes de navigation par satellite, en anglais *Global Navigation Satellite Systems* (GNSS), comme le GPS ou Galileo, nécessitent des références temporelles très précises. La position du récepteur est déterminée à partir des temps de propagation des signaux transmis par plusieurs satellites vers le récepteur. Comme toute horloge précise a besoin d’un oscillateur stable comme base de temps, nous pouvons utiliser la référence temporelle extraite des signaux satellites pour stabiliser notre propre TCXO ou OCXO. Un tel oscillateur est appelé oscillateur discipliné GPS ou, en anglais, *GPS-Disciplined Oscillator* (GPSDO). Le fonctionnement technique de cette régulation sera abordé dans un chapitre ultérieur consacré aux boucles à verrouillage de phase (PLL). La figure [ref:a_gpsdo] montre un GPSDO dans le contexte d’une station QO-100, alimentant un récepteur radio logiciel (SDR) avec une fréquence de référence stable. Un module auto-construit est visible à la figure [ref:a_gpsdo_homebrew].


---

On pourrait se demander pourquoi ne pas utiliser directement la référence temporelle fournie par le GPS comme signal d’oscillateur. Le récepteur GPS extrait généralement un signal temporel précis, par exemple une impulsion par seconde, à partir des signaux satellites faibles et modulés. Cependant, l’instant exact de cette impulsion peut fluctuer à court terme en raison du bruit, de la propagation par trajets multiples, des influences atmosphériques et des retards dans le récepteur. Sur de plus longues périodes, la fréquence ainsi dérivée reste très précise.

Un TCXO ou OCXO offre quant à lui une bonne, voire une très bonne stabilité à court terme, mais peut dériver lentement de la fréquence nominale à long terme en raison des influences résiduelles de température et du vieillissement de ses composants. Dans un GPSDO, ces deux propriétés sont donc combinées : l’oscillateur local TCXO ou OCXO fournit un signal de sortie stable et peu bruité à court terme, tandis qu’une boucle de régulation lente corrige son écart à long terme à l’aide de la référence temporelle GPS. Ainsi, un GPSDO atteint à la fois une excellente stabilité à court terme et une haute stabilité et précision en fréquence à long terme.


[question:AD606]