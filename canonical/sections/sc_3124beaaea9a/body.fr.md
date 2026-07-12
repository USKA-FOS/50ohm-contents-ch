Le contrôle automatique de gain *(Automatic-Gain-Control, abrégé en AGC)* garantit dans les récepteurs que le signal de sortie AF (volume de réception) reste presque constant même en cas de signal HF d'entrée variable sur le récepteur (par exemple en raison de l'évanouissement) et que les variations de volume sont réduites. À cet effet, le niveau de réception à la sortie de la branche du récepteur est détecté et l'amplification HF est régulée en conséquence, de sorte que le volume de réception peut être influencé après la démodulation. À cet égard, l'AGC ne doit pas être confondue avec l'ALC (Automatic-Level-Control), qui se trouve dans la branche d'émission.

<margin>
[picture:1055:e_agc:AGC dans le récepteur superhétérodyne]
</margin>

---

L'AGC peut, selon l'équipement du récepteur, être adaptée en ce qui concerne son comportement de réponse (temps de réponse, temps de décroissance). Les désignations habituelles à cet effet sont AGC Slow, AGC Normal, AGC Fast, qui esquissent le comportement de réponse dans le temps. Le réglage AGC-Slow ou Normal est généralement utile pour le mode SSB. En mode télégraphie (CW), le réglage AGC-Fast ou Normal est généralement utile afin que les signaux forts ne puissent pas couvrir les signaux faibles et que la régulation suive rapidement. Pour les procédés de transmission numériques, il peut être utile de désactiver l'AGC.

[question:EF211]
[question:EF212]

<tip>
L'AGC peut être complètement désactivée sur certains récepteurs. Il est alors possible de contrôler l'amplification HF, par exemple manuellement en modifiant le régulateur de gain RF. Cela n'est cependant utile que pour des applications particulières (par exemple, surcharge de la partie d'entrée HF en raison de signaux forts), ainsi que éventuellement pour les procédés de transmission numériques.
</tip>