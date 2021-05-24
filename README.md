# RaspiMAX31865
Einfache aber genaue Temperaturmessung mit Raspi und MAX31865
Anforderungen:
- von der "Ferne" ablesbar (bis 5m)
- Lebensmittelecht (Sensoren von Sensorshop24.de)


## Toolchain
https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up
https://projects.raspberrypi.org/en/projects/raspberry-pi-using


https://gnutoolchains.com/raspberry/tutorial/


## Schritte zum Start
1) Mit Raspberry Pi Imager OS und SD Karte wählen (auf Windows Rechner) - gewählt: RASPBERRY PI OS (Debian derivat)
2) Problem: Am Display werden nur Striche angezeigt und am Monitor nichts!
Problemlösung: config.txt anpassen
3) Remote auf Raspberry Pi zugreifen: https://www.wintotal.de/tipp/raspberry-pi-remote-desktop/
a) RemoteDesktopVerbindung aufrufen
b) IP Adresse eingeben, z.B. 192.168.2.128
c) pi und Passwort eingeben
4) Touchscreen aktivieren: https://www.youtube.com/watch?v=SUKNdBzfEWc
5) Touchscreen odroid-vu7 plus am raspberry pi: Hier muss Kernel neu kompiliert werden!
6) Autostart Python Skript: https://www.youtube.com/watch?v=cZa1oCSdbUk


## MAX31865 mit dem Raspberry verbinden und programmieren

https://learn.adafruit.com/adafruit-max31865-rtd-pt100-amplifier/python-circuitpython

![Alternativer Text](/Doku/adafruit_products_raspi_max31865_spi_bb.jpg)

Python Bibliothek verwendet. Für die grafische Oberfläche tkinter importiert.

## Troubleshooting
### Odroid Display funktioniert nicht:
https://community.volumio.org/t/raspberry-pi-b-and-odroid-vu-7-plus/6824


    Edit config.txt

Two ways to do it :

    Use a card reader on a mac/linux computer, open /boot/config.txt with your text editor.
    Connect in SSH to the raspberry (enable SSH in volumio.local/dev, use an SSH software like putty on windows) and type sudo nano /boot/config.txt

Once the file is displayed, add the following lines


    #Set output to DVI so the sound won’t be sent through the HDMI cable
    hdmi_drive=1
    #Set HDMI group to 2, no idea what it actually does
    hdmi_group=2
    #Set hdmi_mode to 87 which seems to be « custom resolution »
    hdmi_mode=87
    #Set the screen parameters
    hdmi_cvt=1024 600 60 3 0 0 0

