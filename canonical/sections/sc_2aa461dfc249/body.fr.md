<margin>
[picture:542:n_digital_voice_repeaternetwork:Réseau de relais pour la voix numérique : Relais DB0FZ avec connexion Internet, Hotspot DN9YI et relais DB0HOB avec liaison radio directionnelle vers DB0FZ]
</margin>

La voix peut également être transmise numériquement, par exemple avec les procédés de transmission DMR, D-Star, C4FM et M17. Cela peut se faire, selon le procédé, avec un ordinateur ou également avec un appareil radio approprié. Ainsi, on peut émettre avec des radioamateurs du monde entier via des relais radio VHF ou UHF interconnectés. Lorsque deux ou plusieurs relais radio sont interconnectés, les émissions reçues par l'un des relais peuvent être retransmises via un réseau, par exemple le HAMNET ou Internet, et diffusées à nouveau sur d'autres stations connectées. Pour accéder à un tel réseau de relais, on peut également exploiter chez soi un hotspot appelé. Tant qu'il n'existe pas d'autorisation correspondante pour une station télécommandée, l'exploitation d'un hotspot ne peut être effectuée qu'en tant que station occupée, c'est-à-dire qu'il faut éteindre l'émetteur lorsqu'il n'est pas surveillé sur place. Sur les ondes courtes, les liaisons vocales numériques sont principalement établies directement, par exemple avec FreeDV.

<webmargin>
| l: Abréviation | X: Procédé de transmission |
| D-STAR | Digital Smart Technologies for Amateur Radio |
| C4FM | Modulation de fréquence à quatre niveaux continue |
| DMR | Radio mobile numérique |
| M17 | Procédé de transmission open source |
[table:n_dv_uebertragungsverfahren:Procédés de transmission fréquemment utilisés pour la radiotéléphonie numérique]
</webmargin>

[question:NE404]

---

Lors de la transmission vocale numérique, les signaux vocaux sont convertis en un flux de données avant la transmission. Plusieurs flux de données de ce type peuvent également être transmis en séquence périodique rapide et alternée. On appelle cela TDMA (Time Division Multiple Access) ou procédé de multiplexage temporel. Ainsi, deux ou plusieurs liaisons vocales utilisent quasi simultanément la même fréquence. Pour un appareil radio, cela signifie qu'il doit constamment basculer rapidement entre l'émission et la réception lorsque la touche PTT est enfoncée, afin de ne pas perdre le rythme.

<margin>
[picture:474:n_digital_voice_tdma:TDMA avec trois liaisons sur une fréquence]
</margin>

<tip>
La plupart des amplificateurs de puissance externes ne peuvent pas basculer aussi rapidement entre l'émission et la réception que nécessaire pour le TDMA. C'est pourquoi seuls les amplificateurs de puissance spécialement conçus pour le DMR et d'autres procédés utilisant des créneaux temporels peuvent être utilisés. Sinon, il arrive que la fréquence soit occupée non seulement pendant son propre créneau temporel. Cela peut perturber les émissions d'autres stations sur la même fréquence.
</tip>

[question:NE403]

---

Contrairement aux émissions analogiques, pour lesquelles il suffit généralement de connaître la fréquence et le type de modulation pour établir une liaison avec un autre participant, la langue numérique nécessite souvent plus de réglages, par exemple le groupe de parole, la salle ou le réflecteur pour interconnecter les relais radio ou le créneau temporel TDMA à utiliser.

<indepth>
Selon le procédé, il peut également y avoir de nombreux autres réglages, par exemple pour le DMR le code de couleur, avec lequel plusieurs groupes d'utilisateurs peuvent partager une fréquence sans s'entendre mutuellement. De tels paramètres doivent être correctement réglés sur l'appareil avant le début d'une liaison afin qu'elle puisse être établie.
</indepth>

[question:NE402]

Les procédés numériques DMR, D-Star ou C4FM sont souvent utilisés en plus de la radiotéléphonie FM via des appareils radio portatifs VHF/UHF et via des relais.

[question:NE307]

% TODO: Le tableau n'est pas abordé et il n'est pas complet ... 
%<webmargin>
%| l: Procédé | l: Identifiant personnel | l: Appel de groupe | l: Appel direct | X: Autres |
%| M17 | Indicatif d'appel | - | Indicatif d'appel | Numéro d'accès au canal (CAN), débit de transmission (1600 ou 3200 bit/s) |
%| FreeDV | - | - | - | Mode (1600, 700C, 700D, 700E, 2020) |
%| DMR | DMR-ID | Talkgroup | DMR-ID | Code de couleur (1 à 4, dans le radioamateur généralement 1), créneau temporel (TS 1 ou TS 2) |
%| C4FM | Indicatif d'appel | Réflecteur | - | |
%| D-Star | Indicatif d'appel | ? | ? | |
%[table:n_digital_voice_verfahren:Procédés pour Digital Voice et réglages possibles]
%</webmargin>

<latexonly>
\newpage
</latexonly>