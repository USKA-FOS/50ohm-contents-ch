La régulation automatique du gain *(Automatic Gain Control, AGC)* permet, dans les récepteurs, de maintenir le signal audio de sortie (volume de réception) presque constant malgré les variations du signal HF d'entrée (par exemple dues au fading). Elle réduit ainsi les fluctuations de volume. Pour cela, le niveau de réception est mesuré à la sortie de la branche réceptrice et le gain HF est ajusté en conséquence, influençant ainsi le volume après démodulation. Il ne faut pas confondre l'AGC avec l'ALC *(Automatic Level Control)*, qui se trouve dans la branche d'émission.

<margin>
[picture:1055:e_agc:AGC dans un récepteur superhétérodyne]
</margin>

---

Selon l'équipement du récepteur, l'AGC peut être ajustée en termes de comportement de réponse (temps de montée, temps de descente). Les réglages courants sont AGC Slow, AGC Normal et AGC Fast, qui décrivent le comportement temporel. Le réglage AGC Slow ou Normal est généralement adapté pour le trafic en BLU. Pour la télégraphie (CW), le réglage AGC Fast ou Normal est généralement recommandé afin que les signaux forts n'écrasent pas les signaux faibles et que la régulation suive rapidement. Pour les modes de transmission numériques, il peut être judicieux de désactiver l'AGC.

[question:EF211]
[question:EF212]

<tip>
Sur certains récepteurs, l'AGC peut être entièrement désactivée. Il est alors possible de régler manuellement le gain HF via le contrôle RF-Gain. Cette option n'est utile que pour des applications particulières (par exemple, éviter la surmodulation de l'étage d'entrée HF due à des signaux puissants) ou éventuellement pour les modes de transmission numériques.
</tip>