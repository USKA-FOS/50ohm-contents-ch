La fréquence d’un oscillateur à fréquence variable (VFO) dépend directement de sa tension de service (tension continue). Cela est principalement dû à la dépendance du point de fonctionnement du transistor dans son oscillateur.
Pour obtenir une stabilité en fréquence aussi élevée que possible face aux variations de la tension de service, celle-ci doit être stabilisée par des mesures techniques appropriées. La tension de service d’un VFO doit donc être indépendante des tensions de service des autres étages (stabilisée) et être aussi bien *filtrée et découplée* que possible. Cela peut par exemple être réalisé au moyen d’un régulateur de tension fixe (voir figure [ref:a_osc_stab]).

[question:AD612]
[question:AD608]
[question:AD607]

<margin>
[picture:200:a_osc_stab:Régulateur de tension fixe]
</margin>

---

En cas de mauvaise stabilisation de la tension de service, il peut se produire, sur des émetteurs CW très simples, une distorsion de la hauteur tonale appelée *« chirp »* : au début de chaque point ou trait, la hauteur tonale est d’abord légèrement plus haute ou plus basse, puis se rapproche de la hauteur tonale réelle. Le mot anglais *« chirp »* signifie littéralement *« gazouillis »*. Si la hauteur tonale se rapproche par le haut, l’effet acoustique ressemble effectivement à un gazouillis.

[question:AD609]

<margin>
Voici un exemple de signal avec chirp :

[include:applet_chirp_1]

Un autre exemple, un QSO entre RA1OW et OM3YCY, où l’effet de chirp est clairement audible lors du deuxième passage :

[include:applet_chirp_2]

</margin>