Si le récepteur détecte une erreur, par exemple grâce à des bits de contrôle, il peut demander à l'émetteur de retransmettre les données pour corriger l'erreur. En revanche, avec la correction d'erreur sans retransmission, souvent aucune nouvelle transmission n'est nécessaire. Pour cela, une redondance supplémentaire est ajoutée aux données, par exemple plusieurs bits de contrôle. Ainsi, non seulement une erreur est détectée, mais aussi son emplacement. La procédure peut donc corriger l'erreur en rectifiant le bit identifié comme erroné. Tu peux lire comment cela fonctionne en détail dans la boîte bonus. Mais ce n'est pas pertinent pour l'examen. En anglais, on parle de Forward Error Correction (FEC).

[question:AE413]
[question:AE414]

<indepth>

Le code de Hamming est un procédé de correction d'erreur qui utilise plusieurs bits de parité. Supposons que nous voulons transmettre les 11 bits suivants :

[picture:683:hamming1: ]

L'objectif est de pouvoir non seulement détecter, mais aussi corriger une erreur de bit. Pour cela, il est utile d'examiner de plus près les positions des différents bits. Nous désignons donc les positions par des lettres :

[picture:682:hamming2: ]

Nous réorganisons ensuite les bits et ajoutons quelques bits supplémentaires :

[picture:684:hamming3: ]

Au lieu d'un seul bit de contrôle, nous utilisons maintenant quatre bits ($p_1$-$p_4$), qui couvrent différentes zones de nos bits de données, de manière similaire à un mot croisé :

[picture:685:hamming4: ]

Chaque bit de contrôle sécurise une certaine zone :

[picture:686:hamming5: ]

Regardons à nouveau l'ensemble avec nos données. Pour chaque zone, nous calculons le bit de contrôle avec une parité paire :

[picture:687:hamming6: ]

Si une erreur se produit lors de la transmission, celle-ci peut être localisée et corrigée grâce à la combinaison des différentes zones. Par exemple, si le bit $k$ est transmis à une $\num{0}$, toutes les vérifications de parité ($p_1$-$p_4$) échouent. L'erreur doit donc se situer au niveau du bit $k$.

Si, par exemple, l'erreur se produit dans le bit $a$, la vérification de parité de $p_1$ et $p_2$ échoue, tandis que celle de $p_3$ et $p_4$ est réussie. L'erreur doit donc se situer au niveau du bit $a$.

Même les erreurs dans les bits de parité peuvent être détectées et corrigées. Par exemple, si l'erreur se produit dans le bit $p_1$, la vérification de parité de $p_1$ échoue, tandis que celle de $p_2$, $p_3$ et $p_4$ est réussie. L'erreur doit donc se situer au niveau du bit $p_1$.

Si plus d'une erreur se produit, le code de Hamming ne peut plus les détecter et les corriger correctement. Mais il existe des extensions du code de Hamming qui peuvent également détecter les erreurs multi-bits.
</indepth>
