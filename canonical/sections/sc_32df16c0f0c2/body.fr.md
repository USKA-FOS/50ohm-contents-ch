Dans la communication sans fil, diverses méthodes d'accès jouent un rôle central pour permettre à plusieurs utilisateurs d'utiliser simultanément un spectre de fréquences commun. Les méthodes courantes sont le multiplexage par répartition de fréquence (FDMA), le multiplexage par répartition dans le temps (TDMA) et le multiplexage par répartition de code (CDMA). Chacune de ces méthodes répartit le spectre de fréquences de différentes manières pour minimiser les interférences et assurer une transmission efficace. Le choix de la méthode dépend des exigences spécifiques en matière de bande passante, du nombre d'utilisateurs et de la sensibilité aux perturbations. Les différences entre ces méthodes sont décrites ci-dessous.

---

Dans la méthode de multiplexage par répartition de fréquence (FDMA – Frequency Division Multiple Access), la bande de fréquences disponible est divisée en plusieurs canaux de fréquence distincts (voir figure [ref:e_fdma]). Chacun de ces canaux est attribué de manière fixe à un utilisateur unique, permettant ainsi l'utilisation simultanée du système par plusieurs participants. La séparation des utilisateurs se fait exclusivement par des fréquences différentes, ce qui empêche les signaux des différents participants de se perturber mutuellement, tant que les écarts entre les canaux sont respectés. Le FDMA est une méthode technologiquement simple et établie depuis de nombreuses années, particulièrement adaptée aux systèmes avec peu d'utilisateurs et un faible besoin d'interférence. Cependant, un inconvénient réside dans l'efficacité relativement faible de la bande passante lorsqu'il y a un grand nombre d'utilisateurs, car chaque participant se voit attribuer en permanence une plage de fréquences réservée, même s'il ne transmet pas de données temporairement. Des exemples typiques d'applications du FDMA sont les anciens systèmes de téléphonie mobile analogique comme AMPS (Advanced Mobile Phone Service) aux États-Unis ou GSM (Global System for Mobile Communications) en Europe, ainsi que diverses formes de communication par satellite.

[question:EE410]

<margin>
[picture:845:e_fdma:Multiplexage par répartition de fréquence]
</margin>

---

Dans la méthode de multiplexage par répartition dans le temps (TDMA – Time Division Multiple Access), plusieurs participants utilisent le même canal de fréquence en se partageant l'accès dans le temps. Chaque utilisateur se voit attribuer des intervalles de temps fixes, appelés créneaux temporels, pendant lesquels il peut émettre et recevoir (voir figure [ref:e_tdma]). Cette séparation temporelle des transmissions empêche les signaux des différents participants de se superposer ou de se perturber mutuellement.

Le TDMA permet une utilisation relativement efficace des ressources de fréquence disponibles, en particulier dans les systèmes avec de nombreux utilisateurs et un trafic de données élevé. Cependant, une synchronisation temporelle très précise de tous les participants est nécessaire pour un fonctionnement fluide, ce qui augmente la complexité technique et le coût du système. Des exemples connus d'applications du TDMA sont le système de téléphonie mobile GSM de deuxième génération, le système de téléphonie sans fil DECT et, dans le domaine du radioamateur, le DMR.

[question:EE409]

<margin>
[picture:844:e_tdma:Multiplexage par répartition dans le temps]
</margin>

---

Dans la méthode de multiplexage par répartition de code (CDMA – Code Division Multiple Access), tous les participants utilisent simultanément la même plage de fréquences et le même temps. La séparation des différents utilisateurs ne se fait pas par la fréquence ou le temps, mais par des codes d'étalement individuels (voir figure [ref:e_cdma]). À chaque utilisateur est attribué un code propre, avec lequel son signal est modulé. Ces codes sont choisis de telle manière que les signaux superposés peuvent être séparés à nouveau au niveau du récepteur, même s'ils sont transmis simultanément dans la même bande de fréquences. Le CDMA se distingue par une grande flexibilité et une grande capacité de système, car de nombreux utilisateurs peuvent être actifs simultanément. De plus, la méthode est très robuste face aux perturbations et à la propagation multi-trajets. Cependant, cela s'accompagne d'un traitement du signal relativement complexe et de exigences accrues pour le matériel, en particulier en cas de grand nombre de participants actifs. Des exemples typiques d'applications du CDMA sont les systèmes de téléphonie mobile de troisième génération comme UMTS ainsi que le système de navigation par satellite GPS.

[question:EE411]

<margin>
[picture:846:e_cdma:Multiplexage par répartition de code]
</margin>

En résumé, on peut dire que le FDMA est la méthode la plus simple, tandis que le TDMA et le CDMA deviennent de plus en plus efficaces et complexes, en particulier dans le cas de l'utilisation de bandes passantes limitées et d'un grand nombre d'utilisateurs. Le CDMA permet la plus grande flexibilité, mais nécessite également la technologie la plus sophistiquée pour sa mise en œuvre.
