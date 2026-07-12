
Voyons de plus près la conversion des signaux numériques (échantillons) en signaux analogiques par un convertisseur analogique. Ici, les données numériques sont reconverties en étapes de tension dans le convertisseur analogique. Cela se fait à un intervalle de temps fixe des échantillons les uns par rapport aux autres. On appelle ce processus également la reconstruction.

En raison de la résolution temporelle discrète due à la fréquence d'échantillonnage limitée d'un convertisseur analogique, un signal en escalier est créé, qui contient des fréquences plus élevées indésirables. Pour éliminer ces parties indésirables et ainsi restaurer le signal d'origine, nous avons besoin, tout comme à l'entrée du convertisseur analogique, d'un filtre passe-bas ou passe-bande. Ce filtre de reconstruction doit ici supprimer efficacement toutes les composantes du signal qui se trouvent au-dessus de la moitié de la fréquence d'échantillonnage (fréquence d'échantillonnage). 

[question:AF624]
[question:AF625]
