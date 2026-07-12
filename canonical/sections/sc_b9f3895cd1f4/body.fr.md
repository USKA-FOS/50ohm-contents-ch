Un simple multimètre n'est pas adapté pour mesurer des résistances dépendantes de la fréquence. À la place, on peut utiliser un analyseur de réseau vectoriel (VNA). Il s'agit d'un appareil de mesure actif qui, pour une pluralité de fréquences (une plage de fréquences réglable), détermine comment le courant et la tension se comportent l'un par rapport à l'autre (rapport des amplitudes et le déphasage entre la tension et le courant).

<margin>
[photo:201:e_vna_tiefpassmessung:Mesure d'un filtre passe-bas de $\qty{0}{\mega\hertz}$ à $\qty{100}{\mega\hertz}$ avec une fréquence de coupure à $\qty{30}{\mega\hertz}$]
</margin>

---

Ainsi, on peut par exemple déterminer à quelle fréquence un circuit oscillant ou un filtre présente une résistance particulièrement élevée ou particulièrement faible (ou impédance) (cf. illustration [ref:e_vna_tiefpassmessung]). On peut également déterminer à quelle fréquence une antenne est en résonance en examinant le SWR sur une plage de fréquences, comme le montre la figure [ref:e_vna_swr].

<margin>
[photo:323:e_vna_swr:Mesure SWR d'une antenne filaire alimentée en bout. Le SWR est presque $1$ à $\qty{14}{\mega\hertz}$]
</margin>

[question:EI201]
[question:EI202]
[question:EI203]
[question:EI204]

De nombreux VNA doivent être étalonnés avant utilisation afin d'obtenir un résultat de mesure aussi précis que possible.

[question:EI205]

---

Pour l'étalonnage ainsi que pour le test de fonctionnement, on mesure souvent les états "ouvert" (résistance infinie), "court-circuit" (résistance proche de zéro) et "adapté" (résistance de charge correspondant à la résistance de sortie de l'appareil de mesure).

<margin>
[photo:327:e_vna_solt:Kit d'étalonnage SOL(T). De gauche à droite - Load, Open, Closed]
</margin>

Lorsqu'un terminateur de ligne est connecté (par exemple, une résistance de terminaison de $\qty{50}{\ohm}$), le VNA doit afficher un SWR proche de $\num{1}$, car aucune puissance n'est réfléchie. Si rien n'est connecté à la prise de mesure ou si celle-ci est en court-circuit, un SWR proche de l'infini est obtenu (réflexion totale).

[question:EI206]