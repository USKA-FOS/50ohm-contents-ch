Dans les communications sans fil, différents procédés d’accès jouent un rôle central pour permettre à plusieurs utilisateurs d’exploiter simultanément un spectre de fréquences commun. Les procédés couramment utilisés sont le multiplexage en fréquence (FDMA), le multiplexage temporel (TDMA) et le multiplexage par code (CDMA). Chacun de ces procédés divise le spectre de fréquences de manière différente afin de minimiser les interférences et d’assurer une transmission efficace. Le choix du procédé dépend des exigences spécifiques en matière de bande passante, de nombre d’utilisateurs et de sensibilité aux interférences. Les différences entre ces procédés sont décrites ci-dessous.

---

Dans le procédé de multiplexage en fréquence (FDMA – Frequency Division Multiple Access), la bande de fréquences disponible est divisée en plusieurs canaux de fréquence distincts (cf. illustration [ref:e_fdma]). Chaque canal est attribué de manière fixe à un utilisateur unique, ce qui permet à plusieurs participants d’utiliser le système simultanément. La séparation des utilisateurs repose exclusivement sur des fréquences différentes, ce qui empêche les signaux des différents participants de se perturber mutuellement, à condition que les écarts entre les canaux soient respectés. Le FDMA est un procédé techniquement simple et établi depuis de nombreuses années, particulièrement adapté aux systèmes comptant peu d’utilisateurs et nécessitant peu d’interférences. Un inconvénient réside cependant dans une efficacité médiocre en termes de bande passante lorsque le nombre d’utilisateurs est élevé, car chaque participant se voit réserver en permanence une bande de fréquences propre, même s’il n’émet pas de données pendant un certain temps. Des exemples d’application typiques du FDMA incluent les premiers systèmes de téléphonie mobile analogique comme l’AMPS (Advanced Mobile Phone Service) aux États-Unis ou le GSM (Global System for Mobile Communications) en Europe, ainsi que diverses formes de communication par satellite.

[question:EE410]

<margin>
[picture:845:e_fdma:Multiplexage en fréquence]
</margin>

---

Dans le procédé de multiplexage temporel (TDMA – Time Division Multiple Access), plusieurs utilisateurs partagent le même canal de fréquence en se voyant attribuer des intervalles de temps définis, appelés créneaux temporels, pendant lesquels ils peuvent émettre et recevoir (cf. illustration [ref:e_tdma]). Cette séparation temporelle des transmissions empêche les signaux des différents utilisateurs de se chevaucher ou de se perturber.

Le TDMA permet une utilisation relativement efficace des ressources de fréquences disponibles, en particulier dans les systèmes comptant de nombreux utilisateurs et un trafic de données élevé. Cependant, son bon fonctionnement nécessite une synchronisation temporelle très précise de tous les participants, ce qui augmente la complexité technique et les coûts du système. Des exemples d’application connus du TDMA incluent le système de téléphonie mobile GSM de deuxième génération, le système de téléphone sans fil DECT et, en radioamateurisme, le DMR.

[question:EE409]

<margin>
[picture:844:e_tdma:Multiplexage temporel]
</margin>

---

Dans le procédé de multiplexage par code (CDMA – Code Division Multiple Access), tous les utilisateurs exploitent simultanément la même bande de fréquences et le même intervalle de temps. La séparation des utilisateurs ne repose ni sur la fréquence ni sur le temps, mais sur des codes d’étalement individuels (cf. illustration [ref:e_cdma]). Chaque utilisateur se voit attribuer un code propre, qui module son signal. Ces codes sont choisis de manière à ce que les signaux superposés puissent être séparés au niveau du récepteur, bien qu’ils soient transmis simultanément dans la même bande de fréquences. Le CDMA se distingue par une grande flexibilité et une capacité système élevée, car de nombreux utilisateurs peuvent être actifs simultanément. De plus, ce procédé est très robuste face aux interférences et à la propagation par trajets multiples. En contrepartie, il nécessite un traitement du signal relativement complexe ainsi que des exigences accrues en matière de matériel, notamment lorsque le nombre d’utilisateurs actifs est important. Des exemples d’application typiques du CDMA incluent les systèmes de téléphonie mobile de troisième génération comme l’UMTS, ainsi que le système de navigation par satellite GPS.

[question:EE411]

<margin>
[picture:846:e_cdma:Multiplexage par code]
</margin>

En résumé, le FDMA représente la méthode la plus simple, tandis que le TDMA et le CDMA deviennent de plus en plus efficaces et complexes, notamment lors de l’utilisation de bandes passantes limitées et d’un grand nombre d’utilisateurs. Le CDMA offre la plus grande flexibilité, mais nécessite également la technologie la plus sophistiquée pour sa mise en œuvre.