Dans les procédés de transmission numériques, les bits à transmettre doivent être associés à différents symboles possibles. Cette association est appelée *mapping*. Le composant qui effectue cette association est appelé *mappeur*. Le symbole de bloc d’un mappeur est représenté dans la figure [ref:a_mapper]. Le mappeur reçoit un flux de bits numériques et associe les combinaisons de bits contenues aux symboles correspondants dans un diagramme de constellation.

<margin>
[picture:1102:a_mapper:Schéma bloc d’un mappeur]
</margin>

---

Pour comprendre le principe du mapping, commençons par examiner l’*amplitude shift keying* (*ASK*) binaire, déjà connue de la classe E. La figure [ref:a_ask] montre une ASK binaire dans une représentation temporelle. Dans ce cas, l’amplitude du signal porteur est commutée entre deux valeurs. Par exemple, une grande amplitude peut représenter le bit 1 et une petite amplitude le bit 0.

<margin>
[picture:700:a_ask:ASK (Amplitude Shift Keying) en représentation temporelle]
</margin>

---

Les deux symboles possibles peuvent également être représentés dans le diagramme de constellation mentionné précédemment. Comme, dans cet exemple, seule l’amplitude change et la phase reste identique, les deux points de signal se trouvent sur l’axe I. La distance différente par rapport à l’origine correspond aux deux amplitudes différentes. Chaque point de signal se voit maintenant attribuer une valeur binaire via le mapping.

<margin>
[picture:1128:a_ask_mapping:ASK (Amplitude Shift Keying) dans le diagramme de constellation]
</margin>

---

L’amplitude shift keying ne se limite pas à deux amplitudes possibles. Si, par exemple, quatre amplitudes différentes sont utilisées, quatre symboles différents sont disponibles. Comme deux bits permettent de former quatre combinaisons différentes, chaque symbole peut être associé à l’une des combinaisons 00, 01, 10 ou 11.

La figure [ref:a_4_ask] montre une telle *4-ASK* avec quatre amplitudes différentes dans une représentation temporelle. Par exemple, on peut utiliser 25 %, 50 %, 75 % et 100 % de l’amplitude maximale. Chaque symbole permet ainsi de transmettre deux bits.

<margin>
[picture:701:a_4_ask:Amplitude Shift Keying quaternaire (Quaternary Amplitude-Shift Keying)]
</margin>

Dans le diagramme de constellation, il y a maintenant quatre points de signal possibles. Comme seule l’amplitude change dans cet exemple, les quatre points se trouvent sur l’axe I. Chaque point est associé à une combinaison binaire spécifique.

<margin>
[picture:1129:a_4_ask_mapping:Amplitude Shift Keying quaternaire (Quaternary Amplitude-Shift Keying) dans le diagramme de constellation]
</margin>