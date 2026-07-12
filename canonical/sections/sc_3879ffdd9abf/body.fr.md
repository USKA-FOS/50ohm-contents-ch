<margin>
[picture:911:e_digitale_signalverarbeitung_blockschaltbild:Principe du traitement numérique du signal]
</margin>

Au cours des 25 dernières années, le monde a connu des changements technologiques massifs. La puissance de calcul des ordinateurs a augmenté de manière exponentielle, et de plus en plus de tâches dans les appareils techniques sont réalisées par des puces microélectroniques sur un espace minimal. Cette tendance devrait se poursuivre à un rythme rapide dans les années à venir. Tout cela change la manière dont les appareils, en particulier le traitement des signaux dans les appareils radio modernes, sont réalisés. Le traitement numérique du signal est désormais une technologie standard, et chaque appareil moderne repose sur cette technologie. Les processeurs de signal numérique et le principe fondamental du traitement numérique du signal jouent ici un rôle essentiel.

Le traitement numérique du signal ne se limite pas au domaine des technologies radio. De nombreux appareils, qu'il s'agisse de téléphones portables, de chaînes stéréo, de systèmes d'imagerie médicale ou de pratiquement toutes les applications radio modernes, profitent de cette technique fascinante et permettent de réaliser des fonctions et des possibilités inédites dans ces appareils de manière économique.

Dans le domaine des technologies radio, on parle d'appareils SDR pour les appareils qui traitent les signaux au moyen du traitement numérique du signal. Dans ces appareils, au moins une partie du traitement des signaux est réalisée par logiciel.

[question:EF603]

Pour pouvoir traiter numériquement des signaux analogiques continus, ceux-ci doivent d'abord être échantillonnés et convertis en valeurs numériques au moyen d'un convertisseur analogique-numérique (convertisseur A/N). On parle ici de numérisation du signal d'entrée analogique.

[question:EF602]

---
<margin>
[picture:411:e_digitale_signalverarbeitung:Représentation simple d'une onde sinusoïdale composée de $\num{16}$ échantillons et $\num{7}$ valeurs]
</margin>

Ici, le signal analogique est échantillonné à intervalles de temps fixes et représenté dans une plage de valeurs numériques (par exemple de $\num{-128}$ à $\num{+127}$). Chaque valeur représente une tension de signal mesurée déterminée, les valeurs négatives étant généralement associées à des tensions négatives et les valeurs positives à des tensions positives. On peut se faire une idée approximative de ce processus, par exemple, avec une caméra de cinéma qui prend des images d'une scène à intervalles fixes. Les images prises ont toujours un intervalle de temps fixe par rapport à l'image précédente et suivante et représentent la scène momentanée à de petits intervalles de temps. Ce processus s'appelle l'échantillonnage (en allemand, on pourrait traduire cela par le mot échantillonnage). Les valeurs de signal mesurées individuelles sont appelées échantillons. Dans la section suivante, nous examinerons ce processus un peu plus en détail.

Après la conversion A/N, les échantillons présents sous forme de valeurs numériques peuvent être traités de manière quelconque au moyen du traitement numérique du signal.

À la suite du traitement numérique du signal, on voudra à nouveau obtenir un signal analogique à partir des signaux traités numériquement, par exemple pour la sortie via un haut-parleur ou pour l'émission via une antenne. Pour convertir les valeurs numériques en un signal analogique, on a besoin à cet endroit d'un convertisseur numérique-analogique (convertisseur N/A), qui représente pratiquement l'inverse du convertisseur A/N décrit précédemment. Le convertisseur N/A convertit les valeurs numériques en valeurs de tension analogiques et permet ainsi la reconstruction d'un signal analogique à partir des valeurs numériques.

[question:EF601]