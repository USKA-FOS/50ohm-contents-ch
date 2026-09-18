<margin>
[picture:911:e_digitale_signalverarbeitung_blockschaltbild:Principe du traitement numérique du signal]
</margin>

Au cours des 25 dernières années, le monde a connu une évolution technologique massive. La puissance de calcul des ordinateurs a été multipliée, et de plus en plus de tâches dans les appareils techniques sont réalisées par des microprocesseurs occupant un espace minimal. Cette évolution va se poursuivre à un rythme effréné dans les années à venir. Tout cela change la façon dont les appareils, et en particulier le traitement du signal dans les émetteurs-récepteurs modernes, sont conçus. Le traitement numérique du signal (DSP) est désormais la norme, et chaque appareil moderne repose sur cette technologie. Les processeurs de signal numérique et le principe fondamental du traitement numérique du signal y jouent un rôle essentiel.


Le traitement numérique du signal ne se limite pas au domaine de la radio. De nombreux appareils, qu'il s'agisse de téléphones portables, de chaînes stéréo, de systèmes d'imagerie médicale ou de presque toutes les applications radio modernes, bénéficient de cette technique fascinante et permettent de réaliser à moindre coût des fonctions et des possibilités inédites dans ces appareils.


Dans le domaine de la radio, on parle d'appareils SDR (Software Defined Radio) lorsque les signaux sont traités au moyen du traitement numérique du signal. Dans ces appareils, au moins une partie du traitement du signal est réalisée par logiciel.

[question:EF603]


Pour pouvoir traiter numériquement des signaux analogiques continus, ceux-ci doivent d'abord être échantillonnés et convertis en valeurs numériques à l'aide d'un convertisseur analogique-numérique (A/D). On parle alors de numérisation du signal d'entrée analogique.

[question:EF602]

---
<margin>
[picture:411:e_digitale_signalverarbeitung:Représentation simplifiée d'une onde sinusoïdale composée de $\num{16}$ échantillons et $\num{7}$ valeurs]
</margin>

Ici, le signal analogique est échantillonné à intervalles de temps fixes et représenté dans une plage de valeurs numériques (par exemple de $\num{-128}$ à $\num{+127}$). Chaque valeur représente une tension de signal mesurée spécifique, les valeurs négatives correspondant généralement à des tensions négatives et les valeurs positives à des tensions positives. On peut comparer cela à une caméra filmant une scène à intervalles réguliers : les images capturées ont toujours un intervalle temporel fixe par rapport à l'image précédente et suivante, et représentent la scène à des instants très proches. Ce processus s'appelle l'échantillonnage (en anglais *sampling*). Les valeurs de signal mesurées individuellement sont appelées échantillons. Nous examinerons ce processus plus en détail dans la section suivante.


Après la conversion A/N, les échantillons disponibles sous forme de valeurs numériques peuvent être traités de manière arbitraire par le traitement numérique du signal.


Enfin, après le traitement numérique du signal, on souhaite souvent reconvertir les signaux traités en un signal analogique, par exemple pour une sortie via un haut-parleur ou pour une émission via une antenne. Pour cela, il faut un convertisseur numérique-analogique (D/A), qui constitue en quelque sorte l'inverse du convertisseur A/N décrit précédemment. Le convertisseur D/A convertit les valeurs numériques en valeurs de tension analogiques et permet ainsi de reconstruire un signal analogique à partir des valeurs numériques.

[question:EF601]