Un convertisseur abaisseur à faible bruit (LNB) est souvent utilisé dans le *radioamateurisme* pour traiter des fréquences élevées dans la gamme des $\unit{\giga\hertz}$ lors des communications par satellite. L'illustration [ref:a_lnb] montre une implémentation possible d'une station QO-100. Dans ce cas, la fréquence de réception très élevée, généralement captée par un réflecteur parabolique, est immédiatement transposée vers une fréquence beaucoup plus basse dans le LNB afin d'éviter des pertes de câble élevées qui surviendraient à des fréquences élevées.

<margin>
[picture:1094:a_lnb:LNB (bleu) et Bias-T (rouge) dans un émetteur-récepteur QO-100]
</margin>

[question:AF230]

Un LNB est un composant actif qui nécessite une alimentation électrique. Celle-ci est généralement fournie directement via le câble coaxial menant au LNB. Pour cela, un dispositif appelé Bias-T est inséré dans le câble coaxial au niveau du poste de réception. Sa fonction est d'assurer l’*alimentation en courant continu* du LNB et de séparer la tension continue du signal HF dans la suite de la chaîne de traitement vers le récepteur.
Un LNB peut recevoir des signaux polarisés horizontalement ou verticalement. La commutation entre ces deux directions de polarisation s'effectue en ajustant la *tension de service* fournie au LNB. Les valeurs courantes sont par exemple $\qty{12}{\volt}$ et $\qty{18}{\volt}$.

[question:AF231]