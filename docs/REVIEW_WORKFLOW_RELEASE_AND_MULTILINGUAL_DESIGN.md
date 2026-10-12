# Widget de révision des chapitres et sections

État examiné le 12 octobre 2026. Ce document concerne le contenu pédagogique,
pas les campagnes de révision des questions ni la revue des dessins.

## Mécanisme actuel

Le générateur inclut `templates/html/chapter-review-widget.html` dans chaque
page de chapitre et `templates/html/section-review-widget.html` dans chaque page
de section. Le JavaScript demande respectivement
`/review_workflow/api/chapter-widget/<numéro>` et
`/review_workflow/api/widget/<identifiant-section>` sur le serveur de
déploiement. Le serveur renvoie le HTML du widget et reçoit les demandes de
réservation et de changement d'état par `PATCH`. Le bandeau est donc dynamique,
même si les pages publiées sont statiques. En l'absence du service, le script
masque le widget.

Le service `50ohm-review-workflow-tool` charge ses éléments depuis un `HB.json` :
chaque section est identifiée par `ident`, chaque groupe par le numéro du
chapitre. Ses tables SQLite `review_items` et `audit_log` portent le statut,
l'étape, le responsable et l'historique. Aucune langue ne figure dans la clé
ou dans ces tables. Son accès GitHub sert à vérifier la présence de fichiers
dans le dossier configuré ; les changements de statut ne modifient pas Git.

Le bouton d'édition d'une section pointe explicitement vers
`50ohm-contents-ch` sur la branche `review/de/main`, au chemin
`contents/sections/<fichier>.md`. C'est **une autre branche du même dépôt de
contenu**, et non un autre dépôt. Cette édition est distincte de la réservation
dans SQLite et ne modifie pas directement le canonical. Son intégration au
canonical passe par la procédure d'import allemand documentée séparément.

Les trois sites DE/FR/IT embarquaient auparavant ce même JavaScript et le même
lien d'édition allemand. Les pages FR/IT ne disposent donc pas d'une révision
autonome : une réservation de section y reflète l'état allemand, et le bouton
d'édition vise la source allemande. Un simple changement des libellés ne
résoudrait pas cette ambiguïté.

## Comportement du build depuis cette modification

Le widget de chapitre, celui de section, le bouton d'édition et le bouton
« Afficher les modifications » sont absents **par défaut**. La page `diff.html`
n'est pas générée non plus : elle compare directement deux worktrees allemands
exposés par le serveur (`/50ohm-diff-worktrees/main` et `/review`). Le bouton
de feedback GitHub reste visible. Le paramètre
`--enable-review-workflow` restaure explicitement le comportement antérieur
sur les trois langues. Il ne rend pas le workflow multilingue. Le réglage
`review_workflow` est inscrit dans la configuration du générateur, le rapport
du build et le manifeste d'une release. Le générateur lui-même applique aussi
la valeur par défaut `false` lorsqu'aucune configuration ne la précise.

Depuis l'orchestrateur, pour une release ordinaire sans widget :

```bash
pushd 50ohm-contents-ch >/dev/null
uv run --locked python tools/run_multilingual_canonical_build.py \
  --tag Revision_3.0 \
  --release-id <identifiant-unique> --beta \
  --release-output ../50ohm-site-releases
popd >/dev/null
```

Pour un build de test avec le mécanisme actuel :

```bash
pushd 50ohm-contents-ch >/dev/null
uv run --locked python tools/run_multilingual_canonical_build.py \
  --language de --enable-review-workflow
popd >/dev/null
```

Le réglage ne change pas les releases déjà générées : il faut reconstruire
et publier une nouvelle release pour enlever le bandeau actuellement déployé.

## Adaptation future par langue

Le prototype actuel doit d'abord être séparé de son hypothèse allemande.
L'identité d'une tâche de revue devra associer au moins l'identifiant canonique
de l'objet, la langue, le type de contenu et une révision de départ. Le service
devra conserver l'affectation et l'audit pour cette clé composée, et ses routes
devront recevoir la langue explicitement. La réservation d'un chapitre devra
filtrer ses sections par langue. Les liens d'édition devront viser une source
réellement éditable pour FR/IT ; la branche `review/de/main` ne convient pas.

Il faudra ensuite choisir et documenter où vivent les propositions FR/IT :
branches dédiées du dépôt de contenu, campagnes séparées, ou autre format
versionné. Dans tous les cas, l'état approuvé devra revenir au canonical par
une étape d'import explicite avec contrôle de révision de base. Le statut de
révision dans SQLite ne doit pas devenir l'autorité du texte. Il faudra aussi
prévoir les changements de structure et d'identifiants lors des imports
allemands, puis tester l'isolation DE/FR/IT et les droits d'édition avant
d'exposer le contrôle sur une release publique.

Ce travail n'est pas implémenté ici. La désactivation par défaut évite
d'afficher un état allemand trompeur sur les releases multilingues.
