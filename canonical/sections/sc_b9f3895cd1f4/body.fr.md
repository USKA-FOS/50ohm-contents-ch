Un multimètre simple n'est pas adapté pour mesurer des résistances dépendantes de la fréquence. À la place, on peut utiliser un analyseur de réseau vectoriel (VNA). Il s'agit d'un appareil de mesure actif qui détermine, pour une multitude de fréquences (une bande de fréquences réglable), comment le courant et la tension se comportent l'un par rapport à l'autre (rapport des amplitudes et déphasage entre tension et courant).

<margin>
[photo:201:e_vna_tiefpassmessung:Mesure d'un filtre passe-bas de $\qty{0}{\mega\hertz}$ à $\qty{100}{\mega\hertz}$ avec une fréquence de coupure à $\qty{30}{\mega\hertz}$]
</margin>

---

On peut ainsi déterminer, par exemple, à quelle fréquence un circuit oscillant ou un filtre présente une impédance particulièrement élevée ou particulièrement faible (cf. illustration [ref:e_vna_tiefpassmessung]). Il est également possible de déterminer à quelle fréquence une antenne est en résonance en observant le ROS sur une bande de fréquences, comme illustré dans l'image [ref:e_vna_swr].

<margin>
[photo:323:e_vna_swr:Mesure du ROS d'une antenne filaire alimentée en bout. Le ROS est proche de $1$ à $\qty{14}{\mega\hertz}$]
</margin>

[question:EI201]
[question:EI202]
[question:EI203]
[question:EI204]

De nombreux VNA doivent être étalonnés avant utilisation pour obtenir un résultat de mesure aussi précis que possible.

[question:EI205]

---

Pour l'étalonnage ainsi que pour les tests de fonctionnement, on mesure souvent les états « ouvert » (résistance infinie), « court-circuit » (résistance proche de zéro) et « adapté » (résistance de charge correspondant à la résistance de sortie de l'appareil de mesure).

<margin>
[photo:327:e_vna_solt:Kit d'étalonnage SOL(T). De gauche à droite - Load, Open, Closed]
</margin>

Lorsqu'une terminaison de ligne est connectée (par exemple une résistance de terminaison de $\qty{50}{\ohm}$), le VNA doit afficher un ROS proche de $\num{1}$, car aucune puissance n'est réfléchie. Si rien n'est connecté à la prise de mesure ou si celle-ci est court-circuitée, le ROS est proche de l'infini (réflexion totale).

[question:EI206]