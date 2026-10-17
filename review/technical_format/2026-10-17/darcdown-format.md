# Corrections DARCdown acceptées — Revision_3.0.4

L'utilisateur a accepté les propositions de formatage et les décisions DD-S01
et DD-S03 dans `work/darcdown_review/2026-10-17/review-strict/Arbitrage_reduit.xlsx`.
Il a précisé ensuite que **DD-S02 est reporté** : les réviseurs adapteront d'abord
l'allemand, puis une nouvelle traduction sera effectuée. L'objet
`sections/sc_f4725cf6fede` reste donc inchangé dans les trois langues, y compris
ses écarts de contenu connus. Ce report n'est pas une validation de son contenu.

Le retrait antérieur de 55 paires de guillemets est conservé au commit
`a0d6befef535103c616dae4b9280f51a59b4c0ac`, point de départ propre de cette
application. Les originaux, propositions et classeurs historiques restent dans
`work/` sans écrasement. Les données durables de l'arbitrage sont ici :

- `darcdown-arbitration.json` : décisions exactes, justifications, opérations et
  preuves du plan de formatage proposé ; son étape historique reste indiquée.
- `darcdown-format-approved.json` : 547 corrections supplémentaires, textes
  avant/après, SHA-256, décisions humaines finales et empreinte du classeur.
- `darcdown-format-applied.json` : reçu d'application et vérification des
  3476 corps inventoriés, y compris ceux restés inchangés.

DD-S01 supprime exclusivement le reliquat allemand répété/tronqué après la
définition complète de *Modulationssignal*. DD-S03 conserve le sens italien et
ajoute les mots mnémotechniques allemands avec B/Z en italique dans la section
et les diapositives concernées. Aucun statut de revue n'est modifié.

Les autres corrections rétablissent les styles, commentaires en colonne une,
commandes et références protégées, éléments omis, séparateurs de diapositives
et structures de tableaux/listes selon le plan arbitré. Elles ne constituent
pas une nouvelle validation technique des calculs allemands repris en référence.
Les questions du catalogue ne sont pas modifiées par cette opération.

## Application contrôlée

Depuis l'orchestrateur, ces commandes utilisent le Python verrouillé du contenu.
La première est à blanc ; seule la seconde écrit le canonical. Le script exige
le commit de départ propre et toutes les empreintes du plan ; il refuse de
réappliquer une opération déjà effectuée. Ne pas le relancer sur une autre révision.

```bash
pushd 50ohm-contents-ch >/dev/null
uv run --locked python review/technical_format/2026-10-17/apply-approved-format.py
uv run --locked python review/technical_format/2026-10-17/apply-approved-format.py --apply
uv run --locked python tools/validate_canonical_model.py
git -c core.whitespace=-blank-at-eol diff --check
popd >/dev/null
```

Les espaces de fin de ligne Markdown préexistants dans `s_77c8a33f87f6` sont des
sauts de ligne voulus et sont conservés. Les PDF et sites sont des sorties
distinctes, générées après commit et création du tag `Revision_3.0.4`.
