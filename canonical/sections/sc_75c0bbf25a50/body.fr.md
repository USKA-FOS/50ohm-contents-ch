Une alimentation à découpage (en anglais *switched-mode power supply*) convertit une tension alternative en une tension continue stabilisée. Pour cela, elle redresse d'abord la tension d'entrée, la découpe ensuite très rapidement, la transforme ainsi efficacement à la tension souhaitée et la lisse enfin. Nous verrons comment cela fonctionne en détail dans le cours HB9, au chapitre [sec:schaltnetzteil_2].

<margin>
[photo:308:e_Ferritkerntrafo im Schaltnetzteils:Vue intérieure d'une alimentation à découpage pour $\qty{13,8}{\volt}$ et $\qty{35}{\ampere}$ avec un petit transformateur à noyau de ferrite entre les deux dissipateurs thermiques, poids $\qty{2}{\kilo\gram}$]
</margin>

L'alimentation à découpage présente plusieurs avantages par rapport à une alimentation linéaire régulée :

* Haut rendement même à basse tension nominale et sous charge variable
* Poids et volume réduits grâce à l'utilisation de transformateurs plus petits et de condensateurs de filtrage secondaires à haute fréquence
* Bonne régulation
* Poids réduit, dissipateurs thermiques plus petits et donc moins d'espace nécessaire par rapport à une alimentation linéaire régulée (voir section : stabilisation de tension)

[question:ED302]

Mais les hautes fréquences entraînent aussi des inconvénients :

* Perturbations haute fréquence : en raison du découpage à haute fréquence, des mesures d'amélioration de la CEM sont nécessaires
* Circuit complexe : plus de composants nécessaires, probabilité de défaillance accrue

[question:ED303]
