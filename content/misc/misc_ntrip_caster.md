Title: DIY Ntrip Caster
Date: 2013-10-01 20:48
Category: Misc
Tags: ntrip, rtk, gps, lefebure
Author: x4343
Summary: Setting up an own NTRIP caster

*At the moment only available in german!*

# Was ist ein NTRIP Caster bzw. ein NTRIP Netzwerk?

Während der letzten Arbeitstage vor meinem Studium, habe ich versucht mit den vorhandenen GPS Equipment aus unserem Büro einen NTRIP Caster einzurichten.
Ziel war es, das Gesamtkonstrukt des sogenannten RTK Net Korrekturdatendienstes testweise selbst zu betreiben.

'GPS Receiver als RTK-Referenzstation -> RTCM 3.0 -> Computer mit Caster und Server <- Client <- GPS Receiver als Client'

Clientseitig ist dies kein Problem. Für Windowsbenutzer empfiehlt sich das komfortable und ebenso einfache "GNSS Internet Radio".
Wer tiefer ins Detail gehen möchte, guckt sich den "BKG Ntrip Client" an.

Der Client verbindet sich zu einem Server. Logisch. Der Server wiederum listet einen oder mehrere Caster, welche letztendlich den NTRIP Stream versenden.
Verbindet sich der Client mit einem Server, so kann der Benutzer einen der verfügbaren Streams empfangen. Die Streams der Caster sind über Mountingpoints erreichbar.

Der Client muss sich nur noch mit Username und Password authentifizieren. Anschließend wird die aktuelle Position via GGA String an den Caster übermittelt.
Je größer die Entfernung, desto ungenauer die vom Client berechnete Korrektur. Im Idealfall "sehen" Client und Caster dieselbe Satellitenkonstellation (Skyplot).

Als Faustformel kann man festhalten, dass pro 10 km Entfernung die Genauigkeit um 1 cm abnimmt. Somit ist eine dem RTK Standard entsprechende Genauigkeit von 1-3 cm 
nur im Radius von maximal 30 km von der Referenzstation möglich.

Einige kommerzielle Anbieter haben ein entsprechend dichtes Casternetzwerk, das dies problemlos möglich ist. Der Client muss sich lediglich immer mit dem entsprechenden
Mountpoint der am nächsten gelegenen Station verbinden.

Einen eleganteren und genaueren Lösungsansatz bilden virtuelle Referenzstationen. Dabei wird aus den dem Client unmittelbar umgebenen Referenzstationen $ R_{1} \ldots R_{n} $
eine virtuelle Referenzstation $ R_{V} $ an der Position des Clients gebildet. Durch intelligente Mathematik "sieht" $ R_{V} $ im Idealfall die selbe Satellitenkonstellation wie der Client selbst.
Somit ist eine sehr genaue Korrektur möglich, auch wenn $ R_{1} \ldots R_{n} $ einige zehn Kilometer entfernt sind.

# Die Hardware

Als Referenzstation diente ein R220 L2 Receiver von Hemisphere GPS. Im Grunde ein Eclipse Board, leider ohne GLONASS Freischaltung. Dieses kann per Konfigurationstool
SLXmon für RTK Base Betrieb eingerichtet werden. Dann werden die Korrekturdaten im RTCM 3.0
Format via seriell ausgegeben.

Alternativ lassen sich auch RAW Daten ausgeben. Dann können die Korrekturdaten am PC, bspw. mit der RTKLIB berechnet werden.
Leider fehlte mir dazu die entsprechende Freischaltung, sodass ich auf die Hemisphere proprietären Algorithmen vertrauen musste.

Der Client ist ein RTK Net Modul von RMCAN. Als Empfänger dient der Trimble Ag272 L2 Receiver, mit GLONASS Freischaltung. Korrekturdatenformat RTCM 3.0.


# Einrichten des NTRIP Casters

Für den Caster habe ich das Programm von Lefebure genutzt. Es ist Open Source und hat eine nette GUI.
Alles besser als die Shell unter Windows zu nutzen...

Für einfache Testanwendungen kann sogar der implementierte Server genutzt werden. Dieser bietet allerdings kaum Freiraum. So ist bspw. der Port fest eingestellt.

![NTRIP_CASTER](/static/pictures/ntrip/ntrip_caster.png "Lefebure NTRIP Caster")

Da eben jener Port von der Firewall Policy nicht ausgenommen war, musste der Caster über SSH Portforwarding über meinen heimischen Raspberry Pi geroutet werden.

Kurze Kontrolle, ob der Port 5000 am Raspberry, respektive dem Router, freigegeben und erreichbar ist:

``` bash
pi@raspberrypi ~ $ sudo nmap -sS 0.0.0.0

Starting Nmap 6.00 ( http://nmap.org ) at 2013-08-28 16:40 CEST
Nmap scan report for 0.0.0.0
Host is up (0.00043s latency).
Not shown: 998 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 5.81 seconds
pi@raspberrypi ~ $ sudo nmap -sS 127.0.0.1

Starting Nmap 6.00 ( http://nmap.org ) at 2013-08-28 16:41 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00019s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5000/tcp open  upnp

Nmap done: 1 IP address (1 host up) scanned in 1.24 seconds
```

Und anschließend überprüfen, ob die 'Local Address' korrekt auf 0.0.0.0:5000 läuft:

``` bash
pi@raspberrypi ~ $ netstat -ln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:9040            0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:9050          0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:9051          0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN
udp        0      0 0.0.0.0:1900            0.0.0.0:*
udp        0      0 192.168.178.56:123      0.0.0.0:*
udp        0      0 127.0.0.1:123           0.0.0.0:*
udp        0      0 0.0.0.0:123             0.0.0.0:*
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     STREAM     LISTENING     2859     /var/run/tor/control
unix  2      [ ACC ]     STREAM     LISTENING     2932     /var/run/minissdpd.sock
unix  2      [ ACC ]     STREAM     LISTENING     2497     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     477      /run/udev/control
```
Falls dort 127.0.0.1:5000 steht, muss die GatewayPorts Option im SSH Server entsprechend konfiguriert werden:

``` bash
sudo bash
echo "GatewayPorts clientspecified" >> /etc/ssh/sshd_config
```

Anschließend ist der NTRIP Caster weltweit erreichbar:

``` bash
pi@raspberrypi ~ $ lynx raspiXXXXX.no-ip.org:2170
Looking up  'raspi33609.no-ip.org' first

   SOURCETABLE 200 OK Server: Lefebure NTRIP Caster/2010.02.19
   Content-Type: text/plain Content-Length: 76
   STR;hzu;hzu;RTCM;;2;GPS;LefebureRTK;;41.0;-91.0;0;0;Unknown;none;B;N;96
   00; ENDSOURCETABLE
```

Auch auf meinem Firmenlaptop sah es gut aus:

![NTRIP_CASTER](/static/pictures/ntrip/raspi_ntrip.png "Firefox NTRIP Caster")

Abschließend wurde der finale Feldtest durchgeführt.
Die Caster IP samt Mountpoint und Zugangsdaten wurden ins RTK Net Modem eingetragen. Der Empfang der RTCM Korrekturdaten funktionierte problemlos.

Die eingewählten Clients lassen sich übersichtlich im Caster anzeigen:


![NTRIP_CASTER](/static/pictures/ntrip/ntrip_clientlist.png "NTRIP Clientlist")


# Useful Links
 
[1: Downloadseite des BKG - Bundesamt für Kartographie und Geodäsie](http://igs.bkg.bund.de/ntrip/download)

[2: Open Source NTRIP Caster, Windows](http://lefebure.com/software/ntripcaster/)

[3: Hemisphere Eclipse Board - Datenblatt](http://www.canalgeomatics.com/product_files/hemisphere-gps-eclipse-oem-board-datasheet_195.pdf)

[4: Hemisphere Tools](http://www.hemispheregps.com/Support/MarineOEMSurveyConstruction/Receivers/Software/tabid/558/Default.aspx)

[5: Reverse Port Forwarding via SSH Tunnel](http://toic.org/blog/2009/reverse-ssh-port-forwarding/#.UksoCXhDu5k)

[6: SSH GatewayPorts Description](http://www.snailbook.com/faq/gatewayports.auto.html)



