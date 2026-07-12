Il est rare de trouver des appareils radio permettant de mesurer directement la fréquence de réception. Les circuits récepteurs habituels ne présentent aucun point où cette fréquence est disponible. Pour vérifier l'affichage de la fréquence, on connecte un oscillateur ou un générateur de fréquence aussi précis que possible à la prise d'antenne. Sa fréquence est ensuite comparée à l'affichage du récepteur.

<attention>
Un générateur de fréquence directement connecté peut facilement endommager une entrée de récepteur. En cas de doute, la mesure doit être effectuée avec la tension la plus faible du générateur et un atténuateur.
</attention>

Bien entendu, les oscillateurs disciplinés par GPS et les OCXO sont en règle générale plus précis que les circuits plus simples.

[question:AI511]
[question:AI504]

---

La mesure de fréquence est plus simple pour les émetteurs. Un compteur de fréquence est connecté à la prise d'antenne via un atténuateur. Cette mesure n'est naturellement utile que pour une porteuse non modulée.

<indepth>
Les émetteurs SSB ne génèrent aucun signal sans modulation. Pour mesurer leur fréquence d'émission, on peut injecter un signal audio de fréquence connue dans la prise de microphone. La fréquence de la porteuse non émise est obtenue en soustrayant la fréquence audio de la valeur mesurée par le compteur de fréquence à la sortie de l'émetteur pour USB. Pour LSB, elle est ajoutée.
</indepth>

% AI502
[question:AI502]


[question:AI501]


% TODO Le texte sera complété. - DB7YI 2024-04-22

La mesure de fréquence à l'aide d'un oscilloscope n'est qu'une solution de secours, car ces appareils ont rarement une base de temps aussi précise que les compteurs de fréquence.
% AI503
[question:AI503]

Les compteurs de fréquence simples fonctionnent presque toujours avec une soi-disant *temps de porte*. L'appareil active l'entrée pendant une certaine durée, compte les périodes du signal d'entrée et calcule à partir de celles-ci sa fréquence. C'est particulièrement simple avec un temps de porte d'une seconde, car cela donne directement le nombre d'oscillations par seconde et donc la fréquence en hertz.

Le temps de porte peut être réglé sur la plupart des compteurs de fréquence. Un temps de porte court permet de mettre à jour l'affichage à intervalles courts. Un temps de porte long, en revanche, rend la mesure plus précise.

% TODO Image illustrant l'imprécision avec un temps de porte court

%AI505
[question:AI505]

% Cinq questions sur la précision et la tolérance, qui se trouvaient à l'origine ici, ont été déplacées dans la section "Précision de la fréquence". - DB7YI 2024-04-28