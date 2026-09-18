## Mappage

* Les bits doivent être associés aux symboles possibles.
* Cette association s’appelle *mappage*.
* Le composant correspondant s’appelle *mappeur*.
* Il convertit les combinaisons de bits en symboles.

[picture:1102:a_mapper:Schéma bloc d’un mappeur]

---

## Exemple : ASK

* Dans l’ASK, les symboles diffèrent par leur amplitude.
* L’ASK binaire utilise deux amplitudes.
* Exemple :
  * amplitude faible → $0$
  * amplitude élevée → $1$

[picture:700:a_ask:ASK (Amplitude-Shift Keying) en fonction du temps]

---

## ASK dans le diagramme de constellation

<left>
* Les deux symboles se trouvent sur l’axe I.
* La phase reste identique.
* La distance par rapport à l’origine décrit l’amplitude.
* Le mappage associe une valeur binaire à chaque point.
</left>
<right>
[picture:1128:a_ask_mapping:ASK (Amplitude-Shift Keying) dans le diagramme de constellation]
</right>

---

## 4ASK

* L’ASK n’est pas limité à deux amplitudes.
* Quatre amplitudes donnent quatre symboles.
* Quatre symboles peuvent transmettre deux bits par symbole : $00$, $01$, $10$, $11$

[picture:701:a_4_ask:Modulation d’amplitude quaternaire]

---

## 4ASK dans le diagramme de constellation

<left>
* Dans le cas du 4ASK également, tous les points se trouvent sur l’axe I.
* Les points ne diffèrent que par leur distance par rapport à l’origine.
* Chaque point est associé à une combinaison binaire.
</left>
<right>
[picture:1129:a_4_ask_mapping:4ASK dans le diagramme de constellation]
</right>