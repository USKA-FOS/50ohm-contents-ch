Techniquement, un multiplicateur de fréquence est réalisé en alimentant d'abord le signal d'entrée dans un étage de distorsion non linéaire. Il peut s'agir, par exemple, d'un amplificateur de classe C. Ensuite, à partir du mélange de signaux, la harmonique souhaitée du signal est sélectionnée au moyen de filtres et transmise à l'étage suivant. Comme la multiplication de fréquence est basée sur les harmoniques, seuls les multiples entiers de la fréquence fondamentale sont possibles. En pratique, (à l'exception de quelques cas) seule la 2ème harmonique ou la 3ème harmonique de la fréquence fondamentale est utilisée (doublement, triplement).
Pour obtenir des multiplications de fréquence plus élevées, des étages de doublement ou de triplement sont donc connectés en série, de sorte que leurs facteurs se multiplient ensuite.

[question:AF311]

Par multiplication de fréquence et, le cas échéant, par leur connexion en série, des fréquences intermédiaires sont générées, qui peuvent souvent entraîner des perturbations. C'est pourquoi les étages de multiplication de fréquence doivent être très bien blindés afin de réduire au maximum les rayonnements indésirables.

[question:AF313]

Un circuit de multiplication typique (voir figure [ref:a_frequenzvervielfacher_schaltung] ) contient un étage amplificateur qui est délibérément exploité sans tension de base. Cela crée un amplificateur en mode classe C qui distord fortement le signal d'entrée et dont le signal est prélevé à la sortie au moyen de filtres. Des circuits oscillants appropriés sont utilisés pour les filtres, qui sont en résonance à la fréquence souhaitée et sont généralement accordables.

<margin>
[picture:489:a_frequenzvervielfacher_schaltung:Exemple de circuit d'un multiplicateur de fréquence avec amplificateur de classe C sans tension de base]
</margin>

[question:AF312]

Si plusieurs étages de multiplication sont connectés en série à l'intérieur d'un appareil, des perturbations peuvent survenir sur des fréquences qui se forment entre les différents étages de multiplication. Pour déterminer ces fréquences, il faut calculer le chemin du signal à travers les différents étages et les fréquences qui en résultent. C'est pourquoi l'ordre des étages de multiplication correspondants est décisif pour la détermination des fréquences parasites.

[question:AF314]
