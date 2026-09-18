## Problématique

* Communiquer sa position, par exemple pour des mesures de distance
* Il n’y a pas toujours une ville à proximité
* Les coordonnées GPS sont trop longues
* Une position approximative suffit souvent

---

## Locator Maidenhead

<left>
* La surface de la terre est divisée en $\num{18662400}$ cases
* Une case correspond en Allemagne à une précision d’environ $\qty{5}{\kilo\meter}\times\qty{5}{\kilo\meter}$
* Ces cases sont appelées *Subsquares*
* Au-dessus, on trouve les *Squares* et les *Fields*
</left>
<right>
[photo:4:n_locator_welt:Locator Maidenhead dans le monde. Données cartographiques © contributeurs OpenStreetMap, SRTM. Carte © OpenTopoMap (CC-BY-SA)]
</right>

<note>
* Nommé d’après la ville de *Maidenhead*, située à l’ouest de Londres au Royaume-Uni.
* En 1980, une conférence technique de l’IARU s’y est tenue et a réformé le système de locator QRA précédemment utilisé.
</note>

---
[photo:2:n_locator_jo:Le champ JO du système de locator Maidenhead. Données cartographiques © contributeurs OpenStreetMap, SRTM. Carte © OpenTopoMap (CC-BY-SA)]


<note>
Les *Squares* du champ JO sont représentés.
</note>

--- style="font-size: 0.7em;"
## Niveaux du locator Maidenhead


| X : Désignation | l : Traduction | l : Désignation alternative | c : | c : Exemple |
| Field | Champ | Grand champ | AA-RR | JO |
| Square | Carré | Grand carré | 00-99 | 41 |
| Subsquare | Sous-carré | Petit carré | AA-XX | RG |
[table:n_locator_stufen:Les différents niveaux du locator Maidenhead]

<fragment>
On obtient par exemple *JO41RG* pour le siège de la DARC à Baunatal près de Cassel.
</fragment>
<note>
* Des cases encore plus petites sont possibles
* [Carte interactive](https://f5len.org/tools/locator/)
</note>

---
[question:BE111]


