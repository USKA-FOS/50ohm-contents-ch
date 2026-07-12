%YPA: Voir le numéro 11 de ARK.

Comme nous l'avons appris, la bande passante occupée dépend du type de modulation et, pour la FM, également de la déviation de fréquence. Pour les différentes bandes de fréquences du radioamateur, des largeurs de bande maximales admissibles sont définies. On les trouve dans l'[annexe 1](https://50ohm.de/a1) de l'ordonnance sur le radioamateur, dont nous avons également extrait les limites de bande. Ces largeurs de bande ne doivent pas être dépassées. Chaque radioamateur est lui-même responsable du respect de cette règle.

<webmargin>
| l: Bandes de fréquences | l: Statut | X: Conditions d'utilisation supplémentaires|
| $\qtyrange{135,7}{137,8}{\kilo\hertz}$| S | 1 2 10 |
| $\qtyrange{472}{479}{\kilo\hertz}$| S | 1 |
| $\qtyrange{3500}{3800}{\kilo\hertz}$ | P | 3 |
| $\qtyrange{10100}{10150}{\kilo\hertz}$ | S | 1 10 12 |
| $\qtyrange{28}{29,7}{\mega\hertz}$ | P | 4 13 |
| $\qtyrange{144}{146}{\mega\hertz}$ | P | 6 13 |
| $\qtyrange{430}{440}{\mega\hertz}$ | P | 7 13 |
[table:n_tab_afuv:Extrait AfuV Annexe 1]
</webmargin>

<webmargin>
Les chiffres des conditions d'utilisation supplémentaires dans le tableau mentionné ci-dessus signifient (les chiffres non reproduits sont sans importance pour la largeur de bande) :
* *1* Largeur de bande maximale admissible d'une émission radioamateur : $\qty{800}{\hertz}$.
* *3* Largeur de bande maximale admissible d'une émission radioamateur : $\qty{2,7}{\kilo\hertz}$.
* *4* Largeur de bande maximale admissible d'une émission radioamateur en dessous de $\qty{29}{\mega\hertz}$ : $\qty{7}{\kilo\hertz}$, au-dessus de $\qty{29}{\mega\hertz}$ : $\qty{40}{\kilo\hertz}$.
* *6* Largeur de bande maximale admissible d'une émission radioamateur : $\qty{40}{\kilo\hertz}$.
* *7* Largeur de bande maximale admissible d'une émission radioamateur : $\qty{2}{\mega\hertz}$ ; pour les émissions de télévision modulées en amplitude : $\qty{7}{\mega\hertz}$.
</webmargin>

Les questions suivantes peuvent toutes être résolues à l'aide des notes de bas de page dans l'annexe 1 de l'ordonnance sur le radioamateur, qui - comme déjà mentionné - est disponible comme moyen auxiliaire lors de l'examen. Nous recommandons de se familiariser avec l'annexe avant l'examen !

[question:VD738]
[question:VD739]
[question:VD740]
[question:VD741]
[question:VD742]

---

Il faut faire particulièrement attention aux émissions près des limites des bandes de fréquences du radioamateur. Un exemple : Supposons qu'un signal FM occupe une largeur de bande de $\qty{15}{\kilo\hertz}$, et que nous réglons l'émetteur sur la limite inférieure de bande de la bande des $\qty{70}{\centi\meter}$, donc sur $\qty{430}{\mega\hertz}$. Le signal d'émission se trouve autour de la fréquence porteuse, donc respectivement $\qty{7,5}{\kilo\hertz}$ en dessous et au-dessus. Il s'étendrait donc de $\qty{429,9925}{\mega\hertz}$ à $\qty{430,0075}{\mega\hertz}$. Comme le signal serait ainsi pour moitié en dehors de la bande, nous ne devons pas appuyer sur PTT ! Nous devons donc, pour la FM, mais aussi pour l'AM, toujours maintenir une distance d'au moins la moitié de la largeur de bande occupée par rapport à la limite de bande.

<indepth>
[picture:908:n_bandbreite_falsch:Faux -- Émission en dehors des limites de bande]
[picture:909:n_bandbreite_richtig:Correct -- Émission à l'intérieur des limites de bande]
</indepth>

<indepth>
Dans le cas de la SSB, la situation est un peu différente à la limite de bande. Ici, le signal ne se trouve que d'un côté de la fréquence porteuse (supprimée). Avec la LSB, le signal est entièrement en dessous de la fréquence porteuse, avec la USB, il est entièrement au-dessus de la fréquence porteuse. Si l'on règle donc par exemple la fréquence d'émission sur la limite supérieure de bande, alors on pourrait tout à fait émettre avec la LSB, car le signal entier reste dans la bande. Avec la USB, on ne pourrait cependant pas émettre là-bas, car le signal entier serait en dehors de la bande.
</indepth>

[question:NE305]
[question:BC225]
