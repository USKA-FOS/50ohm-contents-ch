Le moyen le plus simple de détecter une erreur consiste à ajouter un bit supplémentaire, le bit de parité. On l'appelle aussi *Parity Bit*. Cette méthode existe sous deux variantes. Avec la *parité paire* (*Even Parity*), la valeur de ce bit est choisie pour chaque bloc de sorte que le nombre de bits à $\num{1}$ soit toujours pair. Avec la *parité impaire* (*Odd Parity*), le nombre doit toujours être impair. L'émetteur et le récepteur doivent convenir de la variante utilisée avant la transmission.

<indepth>
Prenons l'exemple de la transmission d'un octet avec parité paire :

[picture:677:byte:Un octet]

Nous comptons 5 uns, soit un nombre impair. Le bit de parité doit donc être mis à $\num{1}$ pour obtenir un nombre pair de uns :

[picture:678:even_parity:L'octet avec bit de parité paire]

Si une erreur de transmission modifie *un seul* bit (de $\num{1}$ à $\num{0}$ ou inversement), le nombre de uns devient impair. Le récepteur détecte ainsi qu'une erreur s'est produite.

Voici un autre exemple :

[picture:679:even_parity:Octet avec parité paire]

Dans l'octet d'origine, nous comptons 4 uns, ce qui correspond à un nombre pair. Nous devons donc insérer un $\num{0}$ comme bit de parité.
</indepth>

Cette méthode atteint rapidement ses limites, notamment lorsqu'il y a plus d'une erreur lors de la transmission. Si deux bits sont modifiés pendant la transmission, le nombre de uns reste pair. Le récepteur ne peut plus détecter qu'une erreur s'est produite. Si trois erreurs surviennent lors de la transmission, le nombre de uns devient à nouveau impair et le récepteur détecte les erreurs.

La parité impaire fonctionne selon le même principe, avec une seule différence : le nombre de uns doit être impair et non pair. Comme pour la parité paire, seule une quantité impaire de bits mal transmis est détectée. Une transmission sans erreur ne peut pas être distinguée d'un nombre pair d'erreurs.

[question:AE411]
[question:AE412]

Pour détecter des erreurs sur plusieurs bits, on peut ajouter d'autres bits de parité. Cela fonctionne très bien pour des messages de longueur fixe. Si la longueur des données est variable, on utilise souvent des méthodes de somme de contrôle spéciales comme le *contrôle de redondance cyclique (CRC)*, qui permet de détecter des erreurs avec une certaine probabilité résiduelle. Des méthodes similaires sont également utilisées au quotidien, par exemple pour les numéros de carte d'identité ou l'IBAN.

[question:AE410]
