Pour ne pas avoir à construire et accorder des oscillateurs individuels pour chaque bande de fréquences dans les anciens émetteurs radioamateurs multibandes, on utilisait le principe de la multiplication de fréquence. Un oscillateur stable était alors utilisé à la fréquence de la bande la plus basse (par exemple, $\qty{3,5}{\mega\hertz}$), dont le signal de sortie était ensuite converti à l'aide de multiplicateurs de fréquence dans les bandes de radioamateur souhaitées. Il est avantageux que les différentes bandes de fréquences soient dans des rapports fixes entre elles (par exemple, $\qty{3,5}{\mega\hertz}$, $\qty{7}{\mega\hertz}$, $\qty{14}{\mega\hertz}$ etc.) et soient généralement des multiples entiers de la bande la plus basse. Cela permet également aux harmoniques supérieures de tomber dans une bande de radioamateur, ce qui est souhaité par les autorités de régulation pour éviter les perturbations d'autres services par les harmoniques supérieures. En général, on peut construire des oscillateurs à basses fréquences avec une stabilité plus élevée plus simplement que ceux à hautes fréquences.

---

La figure [ref:n_f_vervielfacher] montre le schéma bloc d'un multiplicateur de fréquence avec le facteur $2$ où la fréquence d'entrée de $\qty{3,5}{\mega\hertz}$ est élevée à $\qty{7}{\mega\hertz}$. Un multiplicateur de fréquence est généralement produit par une non-linéarité (par exemple, une diode) qui génère intentionnellement des harmoniques supérieures du signal d'entrée, à partir desquelles la fréquence multiple souhaitée est ensuite sélectionnée avec un filtre passe-bande.

<margin>
[picture:1042:n_f_vervielfacher:Schéma bloc d'un multiplicateur de fréquence]
</margin>

Souvent, on utilise une chaîne de multiplicateurs de fréquence pour atteindre les facteurs de multiplication souhaités. Dans ce cas, lors du montage en série de multiplicateurs, les facteurs individuels sont multipliés entre eux.
Inversement, un tel circuit peut bien sûr aussi être calculé à rebours. Dans ce cas, il faut alors diviser par les facteurs partiels correspondants.

[question:EF303]
[question:EF302]
[question:EF301]