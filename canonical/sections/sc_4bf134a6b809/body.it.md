La distanza tra due creste d’onda o due gole d’onda viene chiamata lunghezza d’onda [index:lunghezza d’onda]. La lunghezza d’onda dipende dalla frequenza. Più alta è la frequenza, minore è la lunghezza d’onda. La lunghezza d’onda viene indicata con la lettera greca λ (lambda) ed è solitamente espressa in metri (\unit{\meter}).

[question:NB403]
[question:NA205]

Il rapporto tra frequenza e lunghezza d’onda deriva dalla velocità della luce, pari a \qty{300000}{\kilo\meter\per\second}. Un’onda con una frequenza di \qty{1}{\hertz} si propaga per \qty{300000}{\kilo\meter} prima che una cresta d’onda segua un’altra cresta d’onda. Un’onda con una frequenza di \qty{1000}{\hertz} si propaga solo per \qty{300}{\kilo\meter} prima che una cresta d’onda segua un’altra cresta d’onda. A \qty{1000000}{\hertz}, cioè \qty{1}{\mega\hertz}, sono solo \qty{300}{\meter}.

Da ciò derivano le seguenti formule, che permettono di convertire facilmente tra frequenza $f$ (in \unit{\mega\hertz}) e lunghezza d’onda λ (in metri):

$f[\unit{\mega\hertz}] = \dfrac{300}{\lambda[\unit{\meter}]} \quad\quad\quad \lambda[\unit{\meter}] = \dfrac{300}{f[\unit{\mega\hertz}]}$

Le due formule si trovano anche nella raccolta di formule [index:raccolta di formule], che può essere utilizzata come strumento durante l’esame.

Quindi, dividendo 300 per la lunghezza d’onda in metri, si ottiene la frequenza in \unit{\mega\hertz}. Allo stesso modo, dividendo 300 per la frequenza in \unit{\mega\hertz}, si ottiene la lunghezza d’onda in metri.

Se vogliamo, ad esempio, calcolare la lunghezza d’onda corrispondente alla frequenza di \qty{145,3}{\mega\hertz}, inseriamo questo valore nella seconda formula e risolviamo:

$\lambda[\unit{\meter}] = \dfrac{300}{f[\unit{\mega\hertz}]} = \dfrac{300}{\qty{145,3}{\mega\hertz}} \approx \qty{2,06}{\meter}$

Allo stesso modo funziona anche il procedimento inverso. Inserendo la lunghezza d’onda di 2,06 m nella prima formula, otteniamo la frequenza originale:

$f[\unit{\mega\hertz}] = \dfrac{300}{\lambda[\unit{\meter}]} = \dfrac{300}{\qty{2,06}{\meter}} \approx \qty{145,3}{\mega\hertz}$

[include:applet_lambda_und_f]

---

La lunghezza d’onda arrotondata viene spesso utilizzata quando si parla di bande di frequenza. In questo caso si parla di una banda di frequenza [index:banda di frequenza] o semplicemente banda, ad esempio la banda dei \qty{2}{\meter}. Nella tabella [ref:n_funkwellen_baender] sono riportate, ad esempio, le tre bande radioamatoriali che possono essere utilizzate da radioamatori di tutte le classi.

<margin>
| l: Frequenza | l: Lunghezza d’onda | X: Banda |
| \qtyrange{28}{29,7}{\mega\hertz} | \qtyrange{10,7}{10,1}{\meter} | Banda dei \qty{10}{\meter} |
| \qtyrange{144}{146}{\mega\hertz} | \qtyrange{2,08}{2,05}{\meter} | Banda dei \qty{2}{\meter} |
| \qtyrange{430}{440}{\mega\hertz} | \qtyrange{70}{68}{\centi\meter} | Banda dei \qty{70}{\centi\meter} |
[table:n_funkwellen_baender:Le tre bande radioamatoriali accessibili a tutte le classi]
</margin>

Le seguenti due domande possono essere risolte facilmente con le formule appena presentate.

[question:NB302]
[question:NB303]
