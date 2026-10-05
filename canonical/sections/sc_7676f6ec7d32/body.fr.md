Dans la section [sec:agc_1], nous avons déjà abordé l'AGC (Automatic Gain Control). Pour les signaux d'entrée forts, l'AGC réduit le gain des étages amplificateurs dans la branche de réception, et pour les signaux d'entrée faibles, il l'augmente en conséquence. Ainsi, l'amplitude du signal démodulé et donc le volume du signal BF sont maintenus constants.

Sans AGC, les signaux forts satureraient la BF et les signaux faibles ne seraient audibles en BF qu'à très faible volume. Le volume BF devrait toujours être réglé manuellement. L'AGC compense ainsi la dynamique du signal reçu et ajuste dynamiquement la sensibilité de la branche de réception en fonction des signaux d'entrée HF.

[question:AF224]

<margin>
[picture:1055:e_agc:AGC dans le récepteur superhétérodyne]
</margin>

---

Pour que l'AGC puisse ajuster automatiquement le gain en fonction de l'intensité du signal reçu, il a besoin d'une information sur son amplitude. Pour cela, une partie du signal FI peut être redressée puis lissée, comme illustré dans la figure [ref:e_agc_regelspannung].

La diode redresse le signal FI haute fréquence. Un circuit RC en aval supprime les composantes alternatives rapides, de sorte qu'une tension continue est générée, dont la valeur dépend de l'amplitude du signal FI. Plus le signal reçu est fort, plus la valeur absolue de cette tension est grande.

Cette *tension de commande* est renvoyée aux étages amplificateurs HF ou FI réglables et utilisée pour contrôler leur gain. De cette manière, une boucle de régulation fermée est créée : un signal reçu plus fort entraîne une action de régulation plus forte et donc un gain plus faible.

<margin>
[picture:142:e_agc_regelspannung:Tension de commande AGC]
</margin>

[question:AD503]
