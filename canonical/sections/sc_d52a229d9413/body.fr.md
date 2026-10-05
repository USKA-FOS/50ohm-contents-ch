Dans les procédés de transmission numériques, les bits à transmettre doivent être attribués aux différents symboles possibles. Cette attribution est appelée *mapping*. Le bloc fonctionnel qui effectue cette attribution est appelé *mapper*. Le symbole bloc d'un mapper est représenté dans la figure [ref:a_mapper]. Le mapper reçoit un flux de bits numérique et attribue les combinaisons de bits qu'il contient aux symboles correspondants dans un diagramme de constellation.

<margin>
[picture:1102:a_mapper:Schéma bloc d'un mapper]
</margin>

---

Pour comprendre le principe du mapping, considérons d'abord la *modulation par déplacement d'amplitude* (*Amplitude-Shift Keying*, ASK) déjà connue de la section [sec:ask_fsk_afsk]. La figure [ref:a_ask] montre une ASK binaire dans la représentation temporelle. L'amplitude du signal porteur est commutée entre deux valeurs. Par exemple, une grande amplitude peut représenter le bit $1$ et une petite amplitude le bit $0$.

<margin>
[picture:700:a_ask:ASK (Amplitude-Shift Keying) dans l'évolution temporelle]
</margin>

---

Les deux symboles possibles peuvent également être représentés dans le diagramme de constellation appris précédemment. Comme dans cet exemple seule l'amplitude change et que la phase reste la même, les deux points de signal se trouvent sur l'axe I. La distance différente par rapport à l'origine correspond aux deux amplitudes différentes. Chacun des deux points de signal se voit maintenant attribuer une valeur de bit via le mapping.

<margin>
[picture:1128:a_ask_mapping:ASK (Amplitude-Shift Keying) dans le diagramme de constellation]
</margin>

---

Une modulation par déplacement d'amplitude n'est pas limitée à deux amplitudes possibles. Si, par exemple, quatre amplitudes différentes sont utilisées, quatre symboles différents sont disponibles. Comme deux bits permettent de former quatre combinaisons de bits différentes, chaque symbole peut être attribué à l'une des combinaisons $00$, $01$, $10$ ou $11$.

La figure [ref:a_4_ask] montre une telle *4-ASK* avec quatre amplitudes différentes dans la représentation temporelle. Par exemple, $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$ et $\qty{100}{\percent}$ de l'amplitude maximale peuvent être utilisés. Ainsi, deux bits peuvent être transmis avec chaque symbole.

<margin>
[picture:701:a_4_ask:Modulation par déplacement d'amplitude quaternaire (Quaternary Amplitude-Shift Keying)]
</margin>

Dans le diagramme de constellation, il y a maintenant quatre points de signal possibles. Comme seule l'amplitude change encore, dans cet exemple, les quatre points se trouvent sur l'axe I. Chaque point se voit attribuer une combinaison de bits spécifique.

<margin>
[picture:1129:a_4_ask_mapping:Modulation par déplacement d'amplitude quaternaire (Quaternary Amplitude-Shift Keying) dans le diagramme de constellation]
</margin>
