Un *filtre réjecteur (Notch-Filter)* est un filtre très étroit qui vise à supprimer une fréquence spécifique dans le spectre BF du signal reçu. Cela permet, par exemple, de masquer délibérément une porteuse perturbatrice dans une transmission tout en laissant le reste de la transmission presque inchangé. Les filtres réjecteurs peuvent être réalisés aussi bien dans la bande BF que dans la bande FI. Les filtres dans la bande FI présentent l'*avantage* de pouvoir supprimer plus efficacement les signaux parasites plus forts et de réduire leur influence sur l'ALC (contrôle automatique de gain).

[question:EF215]

<margin>
[picture:242:frequenzverlauf_notchfilter:Caractéristique de fréquence d'un filtre réjecteur]
</margin>

---

La caractéristique de fréquence d'un filtre réjecteur est conçue de telle sorte qu'une petite partie de la fréquence du signal BF est fortement atténuée. Cela crée une encoche dans le spectre. D'où le nom de filtre réjecteur.

[question:EF216]

<tip>
De nombreux appareils modernes réalisent les filtres réjecteurs à l'aide de technologies de filtrage numérique. Dans ce cas, la bande passante ainsi que la caractéristique et la fréquence du filtre peuvent souvent être paramétrées avec précision. Un autre *avantage* de cette approche est la possibilité d'utiliser des filtres réjecteurs automatiques (Auto-Notch), qui détectent automatiquement les composantes de porteuse fixes dans le signal BF et les masquent automatiquement.
</tip>