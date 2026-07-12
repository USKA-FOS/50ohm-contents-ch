Un *filtre coupe-bande (Notch-Filter)* est un filtre à bande très étroite qui doit supprimer une fréquence spécifique dans le spectre BF du signal reçu. Cela sert par exemple à masquer de manière ciblée un porteuse perturbatrice dans une transmission, tout en laissant le reste de la transmission presque inchangée. Les filtres coupe-bande peuvent être réalisés aussi bien dans la plage BF que dans la plage ZF. Les filtres dans la plage ZF ont ici l'avantage de pouvoir supprimer de manière plus efficace les signaux perturbateurs plus forts et de réduire leur influence sur l'AGC.

[question:EF215]

<margin>
[picture:242:frequenzverlauf_notchfilter:Caractéristique de filtre d'un filtre coupe-bande]
</margin>

---

La caractéristique de filtre d'un filtre coupe-bande est conçue de telle sorte qu'une petite partie de la fréquence du signal BF est très fortement supprimée. Cela donne une encoche dans le spectre. D'où le nom de filtre coupe-bande.

[question:EF216]

<tip>
De nombreux appareils modernes réalisent des filtres coupe-bande au moyen de la technologie de filtrage numérique. Ici, la bande passante ainsi que la caractéristique de filtre et la fréquence peuvent souvent être paramétrées avec précision. Un autre avantage dans ce contexte sont les filtres coupe-bande automatiques, qui peuvent reconnaître automatiquement les composantes porteuses fixes dans le signal BF et les masquer automatiquement.
</tip>