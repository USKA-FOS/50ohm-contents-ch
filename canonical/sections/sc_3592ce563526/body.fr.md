*Convertisseurs* et *transverters* sont utilisés en radioamateurisme pour exploiter, avec des appareils radio existants, des bandes de fréquences supplémentaires que ces derniers ne couvrent pas à l’origine. Un *convertisseur* ne convertit le signal que dans une seule direction, soit dans le chemin d’émission, soit dans le chemin de réception. Un *transverter*, en revanche, dispose d’un système interne de commutation émission/réception et effectue la conversion de fréquence aussi bien en émission qu’en réception. La conversion de fréquence dans les convertisseurs et transverters s’effectue toujours par mélange dans un ou plusieurs mélangeurs.

Par exemple, avec un transverter adapté et un émetteur-récepteur HF existant, il est possible d’exploiter également la bande VHF/UHF/SHF. Dans ce cas, on pourrait convertir, dans les deux sens, la bande des $\qty{10}{\mètre}$ de l’émetteur-récepteur HF, par exemple sur $\qty{2}{\mètre}$/$\qty{70}{\centi\mètre}$ ou $\qty{23}{\centi\mètre}$ à l’aide d’un transverter.

[question:EF501]
[question:EF502]

---

Examinons d’abord le schéma bloc d’un convertisseur dans l’illustration [ref:e_konverter]. Un tel convertisseur pourrait par exemple servir à convertir un signal issu d’un appareil radio VHF pour le satellite radioamateur QO-100, qui nécessite une fréquence d’entrée dans la bande $\qty{2,4}{\giga\hertz}$. Un transverter n’est pas nécessaire dans ce cas, car la réception s’effectue via une clé SDR et un LNB.

Le schéma bloc montre qu’une bande de fréquences d’entrée définie est convertie, à l’aide d’au moins un mélangeur, vers une autre bande de fréquences de sortie. Une commutation émission/réception n’est pas prévue. Un convertisseur ne peut donc convertir un signal que dans une seule direction, soit en réception (RX), soit en émission (TX). Les convertisseurs destinés au fonctionnement en émission disposent souvent d’une commande PTT qui active les étages amplificateurs du convertisseur en cas d’émission.

La bande de fréquences vers laquelle un convertisseur convertit le signal peut être déterminée par calcul à partir de la fréquence de l’oscillateur appliquée au mélangeur ainsi que de la fréquence d’entrée ou de sortie. Dans l’exemple concret, la fréquence cible résulte du produit de mélange suivant :
$\qty{144}{\méga\hertz} + \qty{2,256}{\giga\hertz} = \qty{2,4}{\giga\hertz}$,
le produit souhaité étant ensuite sélectionné par des filtres adaptés.

<margin>
[picture:651:e_konverter:Schéma d’un convertisseur, par exemple pour QO-100]
</margin>

[question:EF504]

---

Le circuit d’un transverter se distingue bien de celui d’un convertisseur. Les illustrations [ref:e_transverter_rx] et [ref:e_transverter_tx] montrent le diagramme en blocs d’un transverter permettant d’exploiter la bande $\qty{2}{\mètre}$ avec un émetteur-récepteur HF de la bande $\qty{10}{\mètre}$. Pour cela, on utilise une commutation émission/réception ainsi que deux mélangeurs et deux chemins de signal séparés – l’un pour la réception (RX) et l’autre pour l’émission (TX).

En émission, la branche TX convertit le signal de sortie de l’émetteur-récepteur vers la bande de fréquences plus élevée souhaitée, tandis qu’en réception, la branche RX convertit le signal provenant de l’antenne vers la bande de fréquences adaptée à l’émetteur-récepteur. Les bandes de fréquences entre lesquelles le transverter fonctionne peuvent être déterminées par calcul à partir de la fréquence de l’oscillateur appliquée aux mélangeurs ainsi que des fréquences d’entrée et de sortie respectives. Ces relations sont illustrées dans les schémas.

L’oscillateur à quartz stabilisé ($G$) génère une fréquence de $\qty{38,666}{\méga\hertz}$, qui est multipliée par un facteur 1:3 pour atteindre $\qty{116}{\méga\hertz}$. En réception, illustré dans l’illustration [ref:e_transverter_rx], le signal d’entrée de la bande $\qtyrange{144}{146}{\méga\hertz}$ est converti vers la bande $\qtyrange{28}{30}{\méga\hertz}$. En émission, montré dans l’illustration [ref:e_transverter_tx], le signal de sortie de l’appareil radio de la bande $\qtyrange{28}{30}{\méga\hertz}$ est converti vers la bande $\qtyrange{144}{146}{\méga\hertz}$. Comme d’habitude, des filtres adaptés sont utilisés dans les deux chemins de signal pour sélectionner les produits de mélange souhaités, mais ne sont pas représentés ici pour des raisons de clarté.

[question:EF503]

<margin>
[picture:842:e_transverter_rx:Transverter en mode RX]
[picture:843:e_transverter_tx:Transverter en mode TX]
</margin>

<indepth>
*TCXO* (Temperature Compensated Crystal Oscillator) : un oscillateur à quartz compensé en température. Les variations de fréquence dues aux fluctuations de température sont compensées électroniquement.
*OCXO* (Oven Controlled Crystal Oscillator) : un oscillateur à quartz contrôlé par four. Le quartz est maintenu à une température constante dans un petit four régulé en température, ce qui permet d’atteindre une très haute stabilité de fréquence.

La différence essentielle est donc la suivante :

*TCXO* : la température peut varier, l’écart de fréquence est compensé électroniquement.
*OCXO* : la température du quartz est maintenue activement constante. La stabilité de fréquence est généralement plus élevée que celle d’un TCXO.
</indepth>

Les transverters et convertisseurs conçus pour des fréquences d’entrée ou de sortie élevées (dans la gamme des GHz) doivent disposer d’un oscillateur très stable. Les erreurs de fréquence de l’oscillateur, amplifiées par la multiplication interne de fréquence en raison des fréquences de sortie élevées, entraînent des écarts inacceptables de la fréquence cible dans les modes à bande étroite ou en BLU. Un écart de la fréquence de l’oscillateur est multiplié par le même facteur. On utilise souvent un TCXO ou un OCXO, qui peut en outre être synchronisé avec une source de référence externe (par exemple GPS) pour stabiliser au mieux la fréquence de l’oscillateur et minimiser les écarts de la fréquence cible.

[question:EF505]