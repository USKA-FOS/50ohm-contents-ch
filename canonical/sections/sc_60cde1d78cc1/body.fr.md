La manière la plus simple de détecter les erreurs est réalisée en ajoutant un bit supplémentaire, le bit de contrôle. Il est également appelé *bit de parité*. Il existe deux variantes de cette procédure. Dans le cas de la *parité paire*, la valeur de ce bit est choisie pour chaque bloc de telle sorte que le nombre de bits mis à $\num{1}$ soit toujours pair. Dans le cas de la *parité impaire*, en revanche, le nombre doit toujours être impair. L'émetteur et le récepteur doivent se mettre d'accord avant la transmission sur la variante à utiliser.

<indepth>
Supposons que nous voulions transmettre l'octet suivant avec une parité paire :

[picture:677:byte:Un octet]

Nous comptons 5 uns, donc un nombre impair. Le bit de contrôle doit donc être mis à $\num{1}$ pour obtenir un nombre pair de uns :

[picture:678:even_parity:L'octet avec le bit de parité paire]

Si une erreur de transmission modifie *un* bit (de $\num{1}$ à $\num{0}$ ou inversement), alors le nombre de uns devient impair. Le récepteur reconnaît ainsi qu'une erreur s'est produite.

Un autre exemple suit ici : 

[picture:679:even_parity:Octet avec parité paire]

Dans l'octet d'origine, nous comptons 4 uns, ce qui correspond à un nombre pair. C'est pourquoi nous devons insérer un $\num{0}$ comme bit de contrôle.
</indepth>

Cette procédure atteint rapidement ses limites, à savoir lorsque plus d'une erreur se produit lors de la transmission. Si deux bits sont modifiés lors de la transmission, le nombre de uns reste pair. Le récepteur ne peut plus reconnaître qu'une erreur s'est produite. Si trois erreurs se produisent lors de la transmission, un nombre impair de uns est à nouveau créé et le récepteur reconnaît les erreurs.

La parité impaire fonctionne en principe de la même manière, avec une seule différence : le nombre de uns doit être impair et non pair. Pour la parité impaire, comme pour la parité paire, seul un nombre impair de bits transmis de manière incorrecte est détecté. Une transmission sans erreur ne peut cependant pas être distinguée d'un nombre pair d'erreurs.

[question:AE411]
[question:AE412]

Pour détecter les erreurs de plusieurs bits, on peut ajouter d'autres bits de contrôle. Cela fonctionne très bien pour les messages de longueur fixe. Si la longueur des données est variable, on utilise souvent des procédures de somme de contrôle spéciales comme la *vérification de redondance cyclique (CRC)*, qui détectent les erreurs jusqu'à une certaine probabilité résiduelle. Des procédures similaires sont également rencontrées dans la vie quotidienne, par exemple avec les numéros d'identification ou l'IBAN.

[question:AE410]
