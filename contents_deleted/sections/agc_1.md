Die Automatische Verstärkungsregelung *(Automatic-Gain-Control, kurz AGC)* sorgt in Empfängern dafür, dass das NF-Ausgangssignal (Empfangslautstärke) auch bei schwankendem HF-Eingangssignal am Empfänger (z.B. wegen Fading) nahezu konstant bleibt und Lautstärke-Schwankungen verringert werden. Hierbei wird der Empfangspegel am Ausgang des Empfängerzweigs erfasst und die HF-Verstärkung entsprechend geregelt, so dass die Empfangslautstärke nach der Demodulation hierdurch beeinflusst werden kann. Hierbei ist die AGC nicht zu verwechseln mit der ALC (Automatic-Level-Control), welche sich im Sendezweig befindet.

<margin>
[picture:1055:e_agc:AGC im Überlagerungsempfänger]
</margin>

---

Die AGC kann, je nach Empfängerausstattung, bzgl. Ihres Ansprechverhaltens (Ansprechzeit, Abfallzeit) angepasst werden. Übliche Bezeichnungen hierfür sind AGC Slow, AGC Normal, AGC Fast, welche das zeitliche Ansprechverhalten skizzieren. Die Einstellung AGC-Slow oder Normal ist hierbei normalerweise für SSB-Betrieb sinnvoll. Bei Betrieb in Telegrafie (CW) ist normalerweise die Einstellung AGC-Fast oder Normal sinnvoll, damit hierbei starke Signale nicht schwache Signale überdecken können und die Regelung schnell nachführt. Für digitale Übertragungsverfahren kann es ggf. sinnvoll sein die AGC zu deaktivieren.

[question:EF211]
[question:EF212]

<tip>
Die AGC kann bei manchen Empfängern auch komplett deaktiviert werden. Dann ist eine Steuerung der HF-Verstärkung z.B. manuell durch Veränderung des RF-Gain-Reglers möglich. Dies ist jedoch nur für besondere Anwendungen (z.b. Übersteuerung des HF-Eingangsteils aufgrund von starken Signalen) sinnvoll, sowie ggf. für digitale Übertragungsverfahren.
</tip>