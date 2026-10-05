Dans la section [sec:oszillator_tcxo_ocxo], nous avons vu qu'il existe différents types d'oscillateurs avec des stabilités et précisions de fréquence variables. Les oscillateurs à quartz sous forme de TCXO et surtout d'OCXO atteignent une stabilité particulièrement élevée. Les équipements radio modernes atteignent par exemple, avec un TCXO, une précision de fréquence de $\pm\qty{0,5}{\ppm}$. Pour une fréquence souhaitée de $\qty{10}{\mega\hertz}$, la fréquence réelle se situe donc dans la plage de $\qtyrange{9,999995}{10,000005}{\mega\hertz}$, soit au maximum à $\pm\qty{5}{\hertz}$ de la fréquence nominale. Cet écart est faible et généralement plus que suffisant pour un fonctionnement en ondes courtes.

Cependant, si nous travaillons non pas à $\qty{10}{\mega\hertz}$ mais à $\qty{10}{\giga\hertz}$, l'écart possible augmente à $\pm\qty{5000}{\hertz}$. Il peut ainsi déjà être supérieur à la bande passante d'un filtre SSB typique. Pour une liaison radio sur une fréquence fixe convenue, le signal peut donc se trouver en dehors de la plage de réception. Pour de telles applications, par exemple avec le satellite géostationnaire QO-100 qui émet sur $\qty{10}{\giga\hertz}$, des références de fréquence encore plus précises sont donc nécessaires.

<margin>
[picture:1081:a_gpsdo:Oscillateur discipliné par GPS (GPSDO) dans le contexte d'une station QO-100]
</margin>

On pourrait déployer des efforts considérables pour stabiliser davantage un OCXO, ou utiliser d'autres types d'oscillateurs comme les étalons de fréquence au rubidium, qui atteignent notamment une stabilité supérieure à celle des oscillateurs à quartz sur de longues périodes. Cependant, ces étalons de fréquence présentent souvent des inconvénients comme une consommation de courant plus élevée, des dimensions plus grandes et un prix plus élevé, car ils sont principalement développés pour des applications professionnelles.

Heureusement, il existe une autre possibilité : les systèmes de navigation par satellite, en anglais Global Navigation Satellite Systems (GNSS), comme le GPS ou Galileo, nécessitent des références temporelles très précises. La position du récepteur est déterminée à partir des temps de propagation des signaux transmis par plusieurs satellites vers le récepteur. Comme toute horloge précise nécessite un oscillateur stable comme base de temps, nous pouvons utiliser la référence temporelle obtenue à partir des signaux satellites pour stabiliser notre propre TCXO ou OCXO. Un tel oscillateur est appelé oscillateur synchronisé par GPS ou en anglais GPS-Disciplined Oscillator (GPSDO). Nous examinerons comment cette régulation fonctionne techniquement dans un chapitre ultérieur sur les boucles à verrouillage de phase (PLL). La figure [ref:a_gpsdo] montre un GPSDO dans le contexte d'une station QO-100, qui fournit à la radio logicielle (SDR) une fréquence de référence stable. Un module construit soi-même est visible sur la figure [ref:a_gpsdo_homebrew].

---

On pourrait alors se demander pourquoi nous n'utilisons pas directement la référence temporelle fournie par le GPS comme signal d'oscillateur. Le récepteur GPS extrait généralement des signaux satellites faibles et modulés un signal temporel précis, par exemple une impulsion par seconde. Cependant, l'instant précis de cette impulsion peut fluctuer à court terme en raison du bruit, de la propagation par trajets multiples, des influences atmosphériques et des retards dans le récepteur. Sur de longues périodes, la fréquence dérivée de celle-ci est en revanche très précise.

Un TCXO ou OCXO possède quant à lui une bonne, voire très bonne, stabilité à court terme, mais peut à long terme s'écarter lentement de la fréquence nominale en raison d'influences thermiques résiduelles et du vieillissement de ses composants. Dans un GPSDO, ces deux propriétés sont donc combinées : le TCXO ou OCXO local fournit un signal de sortie stable à court terme et à faible bruit, tandis qu'une boucle de régulation lente corrige son écart à long terme à l'aide de la référence temporelle GPS. De cette manière, un GPSDO atteint à la fois une très bonne stabilité à court terme et une haute stabilité à long terme ainsi qu'une précision de fréquence.

[question:AD606]

<margin>
[photo:335:a_gpsdo_homebrew:GPSDO construit soi-même avec TCXO]
</margin>
