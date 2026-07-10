## Remote-Betrieb von Funkstationen

* Besteht aus mehreren Funktionsblöcken  
* Moderne Geräte integrieren teilweise mehrere Blöcke  
* Trennung zwischen Operator und Remote-Standort  

---

### Blockschaltbild einer Remote-Station

<left>
[picture:501:a_remotebetrieb:Blockschaltbild Remote Betrieb]
</left>
<right>
* Logische Darstellung der Funktionsblöcke  
* Steuerung, Netzwerkverbindung, Remote-Interface  
* Transceiver und angeschlossene Geräte  
</right>

---

#### Computer und Bedienteil des Operators (Block 1)

<left>
[picture:501:a_remotebetrieb:Blockschaltbild Remote Betrieb]
</left>
<right>
* Wandelt Audio- und Steuersignale in Netzwerkpakete  
* Empfangene Signale werden hör- und sichtbar gemacht  
</right>

---

#### Netzwerk

<left>
[picture:501:a_remotebetrieb:Blockschaltbild Remote Betrieb]
</left>
<right>
* Verbindet Operator mit Remote-Standort  
* Nutzung des Internets möglich  
</right>

---

#### Remote-Interface am Remote-Standort (Block 2)

<left>
[picture:501:a_remotebetrieb:Blockschaltbild Remote Betrieb]
</left>
<right>
* Setzt Netzwerkpakete in Steuer- und Audiosignale um  
* Überträgt empfangene Audiosignale zum Operator zurück  
</right>

---

#### Transceiver/Verstärker/Tuner/Antennenrotor (Block 3)

<left>
[picture:501:a_remotebetrieb:Blockschaltbild Remote Betrieb]
</left>
<right>
* Werden über das Remote-Interface gesteuert  
* Rückmeldung der Steuerbefehle erfolgt über das Netzwerk  
</right>

---

[question:AF701]

---

[question:AF702]

---

[question:AF704]

---

[question:AF703]

---

[question:AF705]

---

### Verzögerungen im Remote-Betrieb

* Netzwerk- und Verarbeitungszeiten führen zu Latenzen  
* Codierung und Decodierung von Audiosignalen verursachen Verzögerungen  
* Muss beim Funkbetrieb berücksichtigt werden  

---

[question:AF709]

---

[question:AF710]

---

### Watchdog zur Überwachung der Remote-Station

* Verhindert unkontrollierten Zustand bei Verbindungsabbruch  
* Regelmäßiger Austausch von Datenpaketen zwischen Station und Operator  
* Bei fehlender Rückantwort wechselt der Transceiver in sicheren Zustand  

---

[question:AF708]

---

### Fernabschaltung der Stromversorgung

* Transceiver kann in einen undefinierten Zustand geraten  
* Versorgungsspannung sollte aus der Ferne abschaltbar sein  
* Lösung: IP-Steckdose zur Steuerung über das Netzwerk  

---

[question:AF707]

---

### Störungen durch den Transceiver

* Remote-Station kann durch eigene Signale gestört werden  
* Entsprechende Maßnahmen zur Entstörung erforderlich  

---

[question:AF706]
