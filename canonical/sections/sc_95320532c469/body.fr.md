La puissance d'émission générée dans l'émetteur doit être rayonnée par l'antenne de manière aussi complète et sans pertes que possible. C'est pourquoi des lignes de transmission spéciales sont nécessaires, appelées dans le langage technique *lignes de transmission*.

<margin>
[photo:65:n_Koax_Detail:Câble coaxial en détail]
</margin>

Le câble coaxial (illustration [ref:n_Koax_Detail]) est le plus répandu. Dans le langage courant, on parle souvent simplement de câbles coaxiaux. Les câbles coaxiaux sont composés d'un conducteur intérieur et d'un conducteur extérieur isolés l'un de l'autre. Ils sont de forme tubulaire et entourés d'une gaine de protection. Il existe des câbles coaxiaux de différentes exécutions :
* épais ou fin
* avec conducteur intérieur flexible ou rigide
* avec conducteurs extérieurs en tresse et/ou feuille, voire en tube de cuivre massif

% Supprimé temporairement selon le ticket #20292449
%
%<margin>
%L'*atténuation* peut être illustrée par un jet d'eau sortant d'un tuyau d'arrosage : si le tuyau est court, un jet d'eau puissant sort à l'extrémité. Si le tuyau est très long, le jet d'eau sortant est faible.
%</margin>

<margin>
[photo:66:n_Koaxialkabel:Exemples de câbles coaxiaux couramment utilisés]
</margin>

Mais même dans le meilleur câble coaxial, une partie de la puissance d'émission est convertie en chaleur, ce qui entraîne des pertes. L'importance des pertes d'une ligne de transmission est indiquée par ce qu'on appelle l'*atténuation du câble*, généralement exprimée en décibels ($\unit{\dB}$) par $\qty{100}{\m}$. Plus un câble coaxial est long, plus les pertes par atténuation sont élevées. La fréquence de l'oscillation électrique joue également un rôle : plus la fréquence augmente, plus l'atténuation du câble est importante.

[question:NG207]

Une autre caractéristique importante des lignes de transmission est ce qu'on appelle l'*impédance caractéristique*, exprimée en ohm ($\unit{\ohm}$). Il s'agit d'une propriété qui dépend de la structure de la ligne, notamment de l'espacement entre le conducteur intérieur et le conducteur extérieur. La longueur de la ligne n'a aucune influence sur l'impédance caractéristique.

Si l'on connecte des lignes de transmission ayant des impédances caractéristiques différentes, des réflexions indésirables des oscillations haute fréquence se produisent au niveau de la jonction. Une partie de la puissance d'émission est alors réfléchie vers l'émetteur et ne peut donc pas être rayonnée. Dans le pire des cas, cela peut même endommager l'émetteur.

Le connecteur d'antenne des appareils de radioamateurisme est presque toujours conçu pour une impédance caractéristique de $\qty{50}{\ohm}$. Les câbles coaxiaux couramment utilisés en radioamateurisme ont donc une impédance caractéristique de $\qty{50}{\ohm}$. En télévision, on utilise aussi des câbles coaxiaux d'une impédance caractéristique de $\qty{75}{\ohm}$. Plus rarement, on trouve des câbles coaxiaux de $\qty{60}{\ohm}$.

[question:NG201]