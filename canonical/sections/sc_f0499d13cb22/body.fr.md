On peut également vérifier l’affichage de la fréquence d’un récepteur. Contrairement à un émetteur, la fréquence de réception réglée ne peut généralement pas être mesurée simplement à une sortie de l’appareil radio à l’aide d’un fréquencemètre. Le signal HF reçu est déjà traité tôt dans le récepteur, par exemple converti en une fréquence intermédiaire.

Pour vérifier l’affichage de la fréquence, on utilise donc un signal de référence aussi précis que possible. Pour cela, un générateur de fréquence ou un oscillateur de référence précis, dont la fréquence est connue, est connecté à l’entrée antenne du récepteur. Ensuite, le récepteur est accordé sur ce signal et son affichage de fréquence est comparé à la fréquence connue du signal de référence.

Plus la référence utilisée est précise, plus l’affichage de la fréquence du récepteur peut être vérifié ou calibré avec précision. Les oscillateurs synchronisés par GPS ou les oscillateurs à quartz stabilisés en température (OCXO) de haute qualité sont particulièrement adaptés.

<attention>
Un générateur de fréquence directement connecté peut facilement endommager l’entrée du récepteur. En cas de doute, la mesure doit commencer avec la tension la plus faible du générateur et un atténuateur.
</attention>

[question:AI511]
[question:AI504]

---

Pour les émetteurs, la mesure de fréquence est plus simple. Un fréquencemètre est connecté à la prise antenne via un atténuateur. Cette mesure n’a bien sûr de sens que pour une porteuse non modulée, c’est-à-dire un sinus aussi pur que possible.

<indepth>
Les émetteurs BLU ne produisent pas de signal sans modulation. Pour mesurer leur fréquence d’émission, on peut injecter un signal audio de fréquence connue dans la prise micro. Pour un USB, la fréquence audio est soustraite de la valeur mesurée par le fréquencemètre à la sortie de l’émetteur afin d’obtenir la fréquence de la porteuse non émise. Pour un LSB, elle est ajoutée.
</indepth>

[question:AI502]
[question:AI501]

Une fréquence peut également être déterminée à l’aide d’un oscilloscope. Pour des mesures de fréquence précises, un oscilloscope est généralement moins adapté qu’un fréquencemètre dédié, car sa base de temps et ses méthodes de mesure sont spécialement conçues pour une haute précision et une résolution élevée de la fréquence.

[question:AI503]

---

Les fréquencemètres simples fonctionnent souvent avec un *temps de porte* appelé. Pendant cette durée, l’appareil compte les périodes, les flancs ou les passages par zéro du signal d’entrée. La fréquence est ensuite calculée à partir du nombre d’oscillations comptées et du temps de porte connu. Exemple : avec un temps de porte d’une seconde, la détermination de la fréquence est particulièrement simple : si l’on compte par exemple 1000 périodes, la fréquence mesurée est de 1000 Hz.

<margin>
[picture:1126:a_frequenzmessung_torzeit:Comptage d’un signal de fréquence 1,1 kHz avec des temps de porte très courts]
</margin>

La *résolution en fréquence* Δf indique la plus petite différence de fréquence entre deux valeurs mesurées que le fréquencemètre peut encore distinguer ou afficher. Pour un fréquencemètre simple à comptage direct, la résolution en fréquence est déterminée par le temps de porte TG :

Δf = 1/TG

L’impact du temps de porte, et donc de la résolution en fréquence, sur le résultat de la mesure est illustré dans l’illustration [ref:a_frequenzmessung_torzeit]. Dans les deux cas, le même signal de fréquence réelle 1,1 kHz est mesuré.

Avec un temps de porte de seulement 1 ms, une seule période est comptée. Le fréquencemètre en déduit une valeur mesurée de 1 kHz. Le court temps de porte ne permet ici qu’une résolution en fréquence de 1 kHz.

Si le temps de porte est porté à 10 ms, 11 périodes peuvent déjà être comptées. Cela donne une valeur mesurée de 1,1 kHz. La résolution en fréquence est désormais de 100 Hz, ce qui permet d’afficher le chiffre supplémentaire de la fréquence.

Plus le temps de porte est long, plus le nombre de périodes comptées est élevé et plus la résolution en fréquence est fine. Un temps de porte court présente en revanche l’avantage de permettre une mise à jour plus fréquente de l’affichage. Le choix du temps de porte implique donc un compromis entre une mise à jour rapide et une haute résolution en fréquence. La précision de la mesure de fréquence ne doit pas être confondue avec la résolution. Elle dépend en particulier de la précision de la base de temps du fréquencemètre.

[question:AI505]