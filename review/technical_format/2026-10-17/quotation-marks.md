# Retrait des guillemets ajoutés — 17 octobre 2026

Sur instruction explicite de l’utilisateur, 55 paires de guillemets ajoutées par
les traductions ont été retirées dans 46 corps Markdown français et italiens.
La référence de départ est le commit `efe7058a41016ae4b20c6b7a7eb41f907b6a8fe9`.

Seuls les guillemets approuvés, leurs échappements éventuels et leurs espaces
typographiques intérieurs ont été supprimés. Les mots, les apostrophes, les
formules et les marques Markdown existantes ont été conservés. Les autres
propositions de l’arbitrage DARCdown ne sont pas appliquées par cette opération.
Tous les corps allemands sont inchangés.

Le fichier `quotation-marks-applied.json` conserve les textes avant/après,
les opérations exactes, leurs motifs, les empreintes SHA-256 et l’autorisation.
Les corrections ont été réappariées aux originaux : les copies de l’arbitrage
contenaient aussi des propositions de formatage distinctes et n’ont donc pas
été recopiées intégralement dans le canonical.

Les 55 opérations ont été validées avant écriture, puis leurs résultats vérifiés.
Le parseur DARCdown de production accepte les 46 résultats. Le modèle canonical
reste valide, avec zéro erreur et les 29 avertissements de métadonnées déjà
présents. Les deux espaces de fin de ligne Markdown préexistants dans les
solutions FR/IT `s_77c8a33f87f6` sont conservés : ils représentent un saut de ligne.

Aucun commit, tag, push, appel de traduction IA ou build n’est effectué par
cette opération.
