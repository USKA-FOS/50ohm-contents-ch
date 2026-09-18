<margin>
[picture:542:n_digital_voice_repeaternetwork:Réseau de relais pour la voix numérique : station relais DB0FZ avec connexion Internet, hotspot DN9YI et station relais DB0HOB avec liaison par faisceau hertzien vers DB0FZ]
</margin>

La voix peut également être transmise de manière numérique, par exemple avec les procédés de transmission DMR, D-Star, C4FM et M17. Selon le procédé utilisé, cela peut se faire à l’aide d’un ordinateur ou d’un appareil radio adapté. Ainsi, il est possible de communiquer avec des radioamateurs du monde entier via des stations relais VHF ou UHF interconnectées. Lorsque deux ou plusieurs stations relais sont interconnectées, les émissions reçues par l’une d’elles peuvent être relayées via un réseau, par exemple le HAMNET ou Internet, et retransmises sur d’autres stations connectées. Pour accéder à un tel réseau de relais, il est également possible d’exploiter un soi-disant hotspot à domicile. Tant qu’aucune autorisation pour une station télécommandée n’est disponible, l’exploitation d’un hotspot ne peut se faire qu’en station occupée, c’est-à-dire que l’émetteur doit être éteint en l’absence de surveillance sur place. En ondes courtes, les liaisons vocales numériques sont principalement établies directement, par exemple avec FreeDV.

<webmargin>
| l: Abréviation | X: Procédé de transmission |
| D-STAR | Digital Smart Technologies for Amateur Radio |
| C4FM | Continuous 4-level frequency modulation |
| DMR | Digital Mobile Radio |
| M17 | Procédé de transmission open source |
[table:n_dv_uebertragungsverfahren:Procédés de transmission pour la radiotéléphonie numérique fréquemment utilisés]
</webmargin>

[question:NE404]

---

En cas de transmission vocale numérique, les signaux vocaux sont convertis en un flux de données avant l’émission. Plusieurs de ces flux de données peuvent être transmis en alternance rapide et périodique. On appelle cela le TDMA (Time Division Multiple Access) ou multiplexage temporel. Ainsi, deux liaisons vocales ou plus utilisent en apparence simultanément la même fréquence. Pour un appareil radio, cela signifie qu’il doit basculer rapidement en permanence entre l’émission et la réception lorsque la touche PTT est enfoncée, afin de ne pas perdre le rythme.

<margin>
[picture:474:n_digital_voice_tdma:TDMA avec trois liaisons sur une fréquence]
</margin>

<tip>
La plupart des amplificateurs de puissance externes ne peuvent pas basculer aussi rapidement entre l’émission et la réception que nécessaire pour le TDMA. Par conséquent, pour le DMR et d’autres procédés utilisant des créneaux temporels, seuls des amplificateurs de puissance adaptés doivent être utilisés. Sinon, la fréquence risque d’être occupée non seulement pendant le créneau temporel propre, ce qui peut perturber les émissions d’autres stations sur la même fréquence.
</tip>

[question:NE403]

---

Contrairement aux émissions analogiques, pour lesquelles il suffit généralement de connaître la fréquence et le type de modulation pour établir une liaison avec un autre participant, la voix numérique nécessite souvent de prendre en compte davantage de paramètres, par exemple le groupe de parole, l’espace ou le réflecteur pour interconnecter des stations relais, ou encore le créneau TDMA à utiliser.

<indepth>
Selon le procédé, il peut y avoir un grand nombre d’autres paramètres à régler, par exemple pour le DMR le code des couleurs, qui permet à plusieurs groupes d’utilisateurs de partager une fréquence sans s’entendre mutuellement. Ces paramètres doivent être correctement configurés sur l’appareil avant de commencer une liaison pour que celle-ci s’établisse.
</indepth>

[question:NE402]

Les procédés numériques DMR, D-Star ou C4FM sont souvent utilisés en plus de la radiotéléphonie FM via des talkies portables VHF/UHF et via des stations relais.

[question:NE307]

% TODO: Auf die Tabelle wird nicht eingegangen und sie ist nicht komplett ... 
%<webmargin>
%| l: Verfahren | l: Eigene Kennung | l: Gruppenruf | l: Direktruf | X: Sonstige |
%| M17 | Rufzeichen | - | Rufzeichen | Channel Access Number (CAN), Übertragungsrate (1600 oder 3200 Bit/s) |
%| FreeDV | - | - | - | Mode (1600, 700C, 700D, 700E, 2020) |
%| DMR | DMR-ID | Talkgroup | DMR-ID | Color-Code (1 bis 4, im Amateurfunk meist 1), Zeitschlitz (TS 1 oder TS 2) |
%| C4FM | Rufzeichen | Reflektor | - | |
%| D-Star | Rufzeichen | ? | ? | |
%[table:n_digital_voice_verfahren:Verfahren für Digital Voice und mögliche Einstellungen]
%</webmargin>

<latexonly>
\newpage
</latexonly>