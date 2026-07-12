Examinons maintenant plus en détail le convertisseur de données, l'antagoniste du convertisseur analogique/numérique. Le convertisseur de données génère à partir d'un flux de données (échantillons) présent sous forme de données numériques un signal analogique. Ici, le convertisseur de données ne peut pas, tout comme le convertisseur analogique/numérique, générer des valeurs d'amplitude arbitrairement précises, mais a, tout comme le convertisseur analogique/numérique, une résolution maximale (en bits). Il en résulte à nouveau un nombre fini de valeurs de signal analogiques que le convertisseur de données peut générer. Le nombre de paliers possibles se calcule comme décrit précédemment pour le convertisseur analogique/numérique.

[question:AF609]

Un convertisseur de données ne peut toujours générer que des tensions dans une plage de tensions déterminée (par exemple de $\qty{0}{\volt}$ à $\qty{1}{\volt}$ ou de $\qty{-2}{\volt}$ à $\qty{2}{\volt}$). Ici, le nombre de paliers décrits précédemment (résolution du convertisseur de données) se répartit sur la plage de tensions pour un convertisseur de données à fonctionnement linéaire (linéaire signifie ici que la distance entre les paliers individuels est toujours la même). Si le convertisseur de données a par exemple une résolution de seulement $\qty{4}{\bit}$, nous avons $\num{16}$ paliers possibles. Ceux-ci se répartissent alors par exemple sur une plage de tensions (plage de valeurs) de $\qty{0}{\volt}$ à $\qty{1}{\volt}$. Pour calculer le pas entre deux paliers, il suffit de diviser la plage de tensions par le nombre de paliers possibles. Cela donne par exemple, dans notre exemple précédent, une distance (pas) de $\qty{6,25}{\milli\volt}$.

[question:AF611]
[question:AF610]

