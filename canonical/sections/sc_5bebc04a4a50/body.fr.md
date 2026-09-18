Pour éviter de devoir construire et accorder un oscillateur séparé pour chaque bande de fréquences dans les émetteurs multi-bandes du radioamateurisme, on utilisait le principe de la multiplication de fréquence. Un oscillateur stable fonctionnant à la fréquence de la bande la plus basse (par exemple $\qty{3,5}{\mega\hertz}$) était utilisé, dont le signal de sortie était ensuite converti vers les bandes de radioamateur souhaitées à l'aide de multiplicateurs de fréquence. L'avantage de cette méthode est que les bandes de fréquences sont dans des rapports fixes entre elles (par exemple $\qty{3,5}{\mega\hertz}$, $\qty{7}{\mega\hertz}$, $\qty{14}{\mega\hertz}$, etc.) et sont généralement des multiples entiers de la bande la plus basse. Ainsi, les harmoniques se retrouvent également dans une bande de radioamateur, ce qui est souhaité par les autorités de régulation pour éviter les interférences avec d'autres services. En général, il est plus simple de concevoir et de construire des oscillateurs à basse fréquence avec une stabilité plus élevée qu'à haute fréquence.

---

La figure [ref:n_f_vervielfacher] montre le schéma bloc d'un multiplicateur de fréquence avec un facteur $2$, où la fréquence d'entrée de $\qty{3,5}{\mega\hertz}$ est élevée à $\qty{7}{\mega\hertz}$. Un multiplicateur de fréquence est généralement réalisé à l'aide d'une non-linéarité (par exemple une diode) qui génère intentionnellement des harmoniques du signal d'entrée, parmi lesquelles un filtre passe-bande sélectionne ensuite la fréquence multiple souhaitée.

<margin>
[picture:1042:n_f_vervielfacher:Schéma bloc d'un multiplicateur de fréquence]
</margin>

On utilise souvent une chaîne de multiplicateurs de fréquence pour atteindre les facteurs de multiplication souhaités. Dans ce cas, en en série, les facteurs individuels sont multipliés entre eux.
Inversement, un tel circuit peut bien sûr aussi être utilisé en sens inverse. Il faut alors diviser par les facteurs partiels correspondants.

[question:EF303]
[question:EF302]
[question:EF301]