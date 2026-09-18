Si le récepteur détecte une erreur de transmission, par exemple à l’aide de bits de contrôle, il peut demander à l’émetteur de retransmettre les données. Avec la *correction d’erreur directe*, une nouvelle transmission n’est souvent pas nécessaire. Pour cela, des informations supplémentaires, par exemple plusieurs bits de contrôle, sont ajoutées aux données utiles. Ainsi, dans certaines conditions, le récepteur peut non seulement détecter qu’une erreur s’est produite, mais aussi déterminer quel bit est erroné et le corriger. En anglais, cette méthode est appelée *Forward Error Correction* (FEC).

Le détail du fonctionnement est expliqué dans l’approfondissement ci-contre, à l’aide d’un code de Hamming. La procédure exacte n’est pas pertinente pour l’examen.

[question:AE413]
[question:AE414]

<indepth>
Le code de Hamming est une méthode de correction d’erreurs qui utilise plusieurs bits de parité. Supposons que nous voulons transmettre les $\num{11}$ bits de données suivants :

[picture:683:hamming1:]

Pour qu’une erreur sur un seul bit puisse non seulement être détectée, mais aussi corrigée, il faut pouvoir déterminer à quel endroit l’erreur s’est produite. Pour cela, nous commençons par examiner les positions des différents bits et les nommons alphabétiquement :

[picture:682:hamming2:]

Nous réorganisons ensuite les bits de données et ajoutons quatre bits de parité supplémentaires $p_1$ à $p_4$ :

[picture:684:hamming3:]

Les quatre bits de parité contrôlent différents groupes de bits qui se chevauchent :

[picture:685:hamming4:]

Chaque bit de parité protège un groupe spécifique :

[picture:686:hamming5:]

Nous calculons ensuite le bit de parité correspondant pour chacun de ces groupes en utilisant la *parité paire* :

[picture:687:hamming6:]

Si une erreur sur un seul bit survient pendant la transmission, certaines vérifications de parité échouent. La combinaison des vérifications échouées permet de déterminer à quelle position l’erreur s’est produite. Le bit erroné peut ensuite être inversé et ainsi corrigé.

Par exemple, si le bit $k$ est transmis comme un $\num{0}$, les quatre vérifications de parité $p_1$ à $p_4$ échouent. Seul le bit $k$ appartient aux quatre groupes vérifiés. L’erreur doit donc se situer au niveau du bit $k$.

Si une erreur survient dans le bit $a$, seules les vérifications de parité de $p_1$ et $p_2$ échouent, tandis que celles de $p_3$ et $p_4$ réussissent. À partir de ce motif, le récepteur peut déterminer que le bit $a$ est erroné.

Une erreur dans un bit de parité lui-même peut également être détectée et corrigée. Par exemple, si $p_1$ est erroné, seule la vérification de parité associée à $p_1$ échoue, tandis que celles de $p_2$, $p_3$ et $p_4$ réussissent. L’erreur doit donc se situer au niveau de $p_1$.

Le code de Hamming présenté ici est conçu pour corriger une seule erreur de bit. Si plusieurs erreurs de bits surviennent simultanément, il n’est plus possible de déterminer de manière fiable la position réelle de l’erreur à partir des vérifications de parité. Des codes de Hamming étendus permettent en outre de détecter de manière sûre, par exemple, deux erreurs de bits simultanées.
</indepth>