*Convertisseur* et *Transverter* sont utilisés dans la radioamateur pour exploiter des bandes de fréquences supplémentaires avec des appareils radio existants qui ne couvrent pas initialement ces bandes. Un *Convertisseur* convertit le signal dans une seule direction, soit dans le chemin d'émission, soit dans le chemin de réception. Un *Transverter*, en revanche, dispose d'une commutation interne d'émission/réception et effectue la conversion de fréquence à la fois en émission et en réception. La conversion de fréquence dans les convertisseurs et les transverters s'effectue toujours par mélange dans un ou plusieurs mélangeurs.

Par exemple, avec un transverter approprié et un émetteur-récepteur à ondes courtes existant, on peut également opérer dans la bande VHF/UHF/SHF. Dans ce cas, on utiliserait par exemple la bande des $\qty{10}{\meter}$ de l'émetteur-récepteur à ondes courtes au moyen d'un transverter pour la convertir dans les deux sens vers $\qty{2}{\meter}$/$\qty{70}{\centi\meter}$ ou $\qty{23}{\centi\meter}$.

[question:EF501]
[question:EF502]

---

Examinons d'abord le schéma bloc d'un convertisseur dans la figure [ref:e_konverter]. Un tel convertisseur pourrait être utilisé, par exemple, pour convertir un signal d'un appareil radio VHF pour le satellite amateur QO-100, qui nécessite une fréquence d'entrée dans la bande des $\qty{2,4}{\giga\hertz}$. Un transverter n'est pas nécessaire ici, car la réception s'effectue via un stick SDR et un LNB.

Le schéma bloc montre qu'une plage de fréquences d'entrée définie est convertie en une autre plage de fréquences de sortie à l'aide d'au moins un mélangeur. Aucune commutation d'émission et de réception n'est prévue. Un convertisseur ne peut donc convertir un signal que dans une direction, soit en réception (RX) soit en émission (TX). Les convertisseurs pour l'émission comportent souvent une commande PTT qui active les étages amplificateurs du convertisseur en cas d'émission.

La bande de fréquences sur laquelle un convertisseur convertit le signal peut être déterminée par calcul à partir de la fréquence de l'oscillateur fournie au mélangeur ainsi que de la fréquence d'entrée ou de sortie. Dans l'exemple concret, la fréquence cible résulte du produit de mélange de
$\qty{144}{\mega\hertz} + \qty{2,256}{\giga\hertz} = \qty{2,4}{\giga\hertz}$,
dans lequel le produit souhaité est ensuite sélectionné par des filtres appropriés.

<margin>
[picture:651:e_konverter:Circuit de convertisseur par exemple pour QO-100]
</margin>

[question:EF504]

---

Le circuit d'un transverter peut être facilement distingué de celui d'un convertisseur. Les figures [ref:e_transverter_rx] et [ref:e_transverter_tx] montrent le diagramme en blocs d'un transverter qui permet d'opérer sur la bande des $\qty{2}{\meter}$ avec un émetteur-récepteur à ondes courtes de $\qty{10}{\meter}$. Pour ce faire, une commutation d'émission/réception ainsi que deux mélangeurs et deux chemins de signal séparés sont utilisés - un pour la réception (RX) et un pour l'émission (TX).

La branche TX convertit en cas d'émission le signal de sortie de l'émetteur-récepteur vers la bande de fréquences souhaitée plus élevée, tandis que la branche RX convertit en cas de réception le signal provenant de l'antenne vers la bande de fréquences adaptée à l'émetteur-récepteur. Les bandes de fréquences entre lesquelles le transverter fonctionne peuvent être déterminées par calcul en connaissant la fréquence de l'oscillateur fournie aux mélangeurs ainsi que les fréquences d'entrée et de sortie respectives. Ces relations sont représentées dans les figures.

L'oscillateur stabilisé par quartz ($G$) génère une fréquence de $\qty{38,666}{\mega\hertz}$, qui est augmentée à $\qty{116}{\mega\hertz}$ à l'aide d'un multiplicateur de fréquence 1:3. En cas de réception, représenté dans la figure [ref:e_transverter_rx], le signal d'entrée de la plage de fréquences $\qtyrange{144}{146}{\mega\hertz}$ est converti vers la plage $\qtyrange{28}{30}{\mega\hertz}$. En cas d'émission, montré dans la figure [ref:e_transverter_tx], le signal de sortie de l'appareil radio de la plage $\qtyrange{28}{30}{\mega\hertz}$ est converti vers la plage de fréquences $\qtyrange{144}{146}{\mega\hertz}$. Comme d'habitude, des filtres appropriés sont utilisés dans les deux chemins de signal pour sélectionner les produits de mélange souhaités, qui ne sont pas représentés ici pour des raisons de clarté.

[question:EF503]

<margin>
[picture:842:e_transverter_rx:Transverter dans le chemin RX]
[picture:843:e_transverter_tx:Transverter dans le chemin TX]
</margin>

Les transverters et convertisseurs conçus pour des fréquences d'entrée ou de sortie élevées (dans la gamme des GHz) doivent disposer d'un oscillateur très stable. Les erreurs dans la fréquence de l'oscillateur entraînent, en raison de la multiplication interne de la fréquence due aux fréquences de sortie élevées dans les modes de fonctionnement à bande étroite ou SSB, des écarts inacceptables dans la fréquence cible. Un écart dans la fréquence de l'oscillateur est également multiplié par sa multiplication. On utilise souvent un TCXO ou un OCXO, qui peut également être synchronisé avec une source de référence externe (par exemple GPS) pour stabiliser au mieux la fréquence de l'oscillateur et maintenir les écarts dans la fréquence cible aussi faibles que possible.

[question:EF505]