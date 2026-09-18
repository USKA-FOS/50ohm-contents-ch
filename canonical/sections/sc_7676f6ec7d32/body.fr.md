Dans la classe E, nous avons déjà appris à connaître l’AGC (Automatic Gain Control). En présence de signaux d’entrée forts, l’AGC réduit le gain des étages amplificateurs dans la branche réceptrice et l’augmente en cas de signaux faibles. Ainsi, l’amplitude du signal démodulé et donc le volume du signal BF restent constants.

Sans AGC, les signaux forts satureraient la BF et les signaux faibles ne seraient audibles qu’à un volume très bas. Le volume BF devrait alors être constamment ajusté manuellement. L’AGC compense ainsi la dynamique du signal reçu et adapte la sensibilité de la branche réceptrice en fonction des signaux HF d’entrée.

[question:AF224]

<margin>
[picture:1055:e_agc:AGC dans un récepteur superhétérodyne]
</margin>

---

Pour que l’AGC puisse ajuster automatiquement le gain en fonction de l’intensité du signal reçu, elle a besoin d’une information sur son amplitude. Une partie du signal FI peut être redressée puis lissée, comme illustré dans la figure [ref:e_agc_regelspannung].


La diode redresse le signal FI haute fréquence. Un circuit RC en aval supprime les composantes rapides, ce qui génère une tension continue dont la valeur dépend de l’amplitude du signal FI. Plus le signal reçu est fort, plus cette tension est élevée.

Cette *tension de régulation* est renvoyée vers les étages amplificateurs HF ou FI réglables pour y contrôler leur gain. Il en résulte une boucle de régulation fermée : un signal reçu plus fort entraîne une régulation plus marquée et donc un gain réduit.


<margin>
[picture:142:e_agc_regelspannung:Tension de régulation de l’AGC]
</margin>

[question:AD503]
