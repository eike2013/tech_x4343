Title: Skript zum Loggen von Leistungsdaten
Date: 2013-06-28 16:20
Category: Raspberry Pi
Tags: raspberry_pi, statistiken, bash, skript
Author: x4343
Summary: Ein Skript das mit einfachen Bordmitteln CPU, RAM und HDD Logs erstellt

## Idee

Als ich meinen Raspberry bekommen habe kam schnell der Wunsch, alle interessanten Parameter zu loggen.
Eigentlich nur, weil ich einerseits ein bisschen Skripten lernen wollte und andererseits *irgendwann* ein paar Auswertungen über die gesammelten Daten machen kann.

Da das ganze *für den Anfang* möglichst einfach sein sollte, habe ich mich für bash entschieden. In Python wäre das ganze sicherlich mit noch mehr Funktionen und verschachtelter etc etc... möglich gewesen,
aber für meine einfachen Zwecke reicht bash vollkommen aus.

Folgende Parameter sollten ständig geloggt werden:

- CPU Auslastung (Load, wenn möglich auch prozentuale Auslastung)
- RAM Auslastung
- Benutzter Festplattenspeicher (SD Karte)
- Spannung / Stromverbrauch, um einen langfristen Leistungsverbrauch berechnen zu können
- Systemtemperatur
- *evtl. externe Sensoren für genauere Temperaturen etc.*

## Realisierung

Das bash Skript soll minütlich alle gewünschten Werte in eine Datenbank schreiben.
Eine einfache .csv Datei kam nicht infrage, da anschließendes Suchen und Filtern zu kompliziert werden würde. Schon allein eine Größe von wenigen MB impliziert einige zehntausend Zeilen.
Diese zu durchsuchen...kein Bock drauf.
Zumal der Raspberry ja nicht nur mit sich selbst beschäftigt sein soll.

Also muss eine adäquate Datenbank her. 

MySQL? Funktioniert sicher gut. Aber ist für meine Anwendung dann doch zuviel des Guten.
Besser SQLite. Selber Syntax (zumindest für die wichtigsten Befehle), leicht, schnell, handlich!

SQLite wird bspw. auch von Firefox, FileZilla etc. benutzt. Reicht also für meine Zwecke vollkommen aus.

Ein großer Vorteil von SQLite: Die gesamte DB befindet sich in einer Datei. Somit ist der Austausch zwischen einzelnen Rechnern schnell gemacht. Auch ein tägliches Backup ist kein Problem: 

``` bash
cp datenbank.db datenbank.backup
```
Schnell ist eine entsprechende Datenbank mit einer Tabelle `tbl1` erstellt.
Anschließend die notwendigen Spalten mit Datentyp hinzufügen. Da bei mir nur Zahlen geloggt werden, reicht als Datentyp *Integer*.

``` sql
CREATE TABLE tbl1(time int, cpu_temp int,cpu_freq int, cpu_freq_min int,\
cpu_freq_max int, cpu_load_1m int, cpu_load_5m int, cpu_load_15m int,\
cpu_perc_user int, cpu_perc_total int)
```

Diese können nun ganz einfach mit Werten gefüllt werden. Dazu werden die Werte via bash in Variablen geschrieben und diese per `INSERT` Befehl in eine neue Zeile der Datenbank geschrieben.

## Befehle

Im Grunde lassen sich alle Parameter mehr oder weniger mit einem Einzeiler in `cat` auslesen.
Die entsprechenden Files befinden sich in `/sys` oder `/proc`.

Für den Arbeitsspeicher ist bspw. folgender Befehl notwendig:

``` bash
cat /proc/meminfo
```

Als Ergebnis bekommt man eine ganze Palette an Informationen zurückgeliefert.

``` bash
MemTotal:        7601364 kB
MemFree:          147184 kB
Buffers:          102844 kB
Cached:          5981016 kB
SwapCached:          140 kB
[...]
DirectMap4k:       64416 kB
DirectMap2M:     7874560 kB
```

Da längst nicht alle benötigt werden, muss noch ein bisschen gefiltert `grep` und gekürzt `cut` werden. Der benutzte Arbeitsspeicher lässt sich einfach mit *let* ausrechnen.

``` bash
MEM_TOTAL=$(cat /proc/meminfo | grep "MemTotal" | tr -s ' ' | cut -d ' ' -f2)
MEM_FREE=$(cat /proc/meminfo | grep "MemFree" | tr -s ' ' | cut -d ' ' -f2)
let "MEM_USED=($MEM_FREE*100) / $MEM_TOTAL" 
```

So ähnlich funktioniert das auch für die entsprechenden Werte der CPU und SD Karte. Und ich bin mir sicher es gibt noch zig weitere interessante Werte die man mal eben so abfragen kann.
(Ich erinnere mich bei meinem N900 kann man auch so den Neigungssensor auslesen. Wäre auch ein interessanter Gnuplot wert. Warum? Weil man es kann!)

## Das Skript

``` bash
#!/bin/bash

#	Funktion zur Umwandlung von Dateigroessen (e.g. 3.6G, 24.1M, 340K) in Kilobyte ohne Angabe der Einheit (-> 3774873, 24678, 340)
function calc()
{
 #	Uebergabe des ersten Arguments [$1] an (lokale) Variable
 __resultvar=$1

 case "${__resultvar: -1}" in	 #	Switch-Case Auswertung des letzten Zeichens (e.g. 3.6G -> G) (Groesseneinheit)

  K) #	Kilobyte
     __resultvar=$(echo $__resultvar | sed 's/K//g')	#	Loesche Indikator (K)
     __resultvar=$(echo $__resultvar | cut -d. -f1)	#	Abschneiden der Nachkommastellen
     echo $__resultvar
     ;;					#	Rueckgabewert

  M)
     __resultvar=$(echo $__resultvar | sed 's/M//g')
     __resultvar=$(echo $__resultvar*1024 | bc -l)	#	Umrechnung von Megabyte in Kilobyte
     __resultvar=$(echo $__resultvar | cut -d. -f1)
     echo $__resultvar
     ;;

  G) #	Gigabyte
     __resultvar=$(echo $__resultvar | sed 's/G//g')
     __resultvar=$(echo $__resultvar*1024*1024 | bc -l)
     __resultvar=$(echo $__resultvar | cut -d. -f1)
     echo $__resultvar
     ;;

  T) #	Terabyte
     __resultvar=$(echo $__resultvar | sed 's/T//g')
     __resultvar=$(echo $__resultvar*1024*1024*1024 | bc -l)
     __resultvar=$(echo $__resultvar | cut -d. -f1)
     echo $__resultvar
     ;;

 esac
}

#Initializing global variables
FILE=$HOME/skripte/log.txt

#Getting System Data

#Time
TIME=$(date +%s)

#	CPU
CPU_TEMP=$(cat /sys/class/thermal/thermal_zone0/temp)
CPU_FREQ=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)
CPU_FREQ_MIN=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq)
CPU_FREQ_MAX=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq)
CPU_LOAD_1M=$(cat /proc/loadavg | cut -d ' ' -f1)
CPU_LOAD_5M=$(cat /proc/loadavg | cut -d ' ' -f2)
CPU_LOAD_15M=$(cat /proc/loadavg | cut -d ' ' -f3)
CPU_PERC_USER=$(cat /proc/stat | grep cpu0 | tr -s ' ' | cut -d ' ' -f2)
CPU_PERC_NICE=$(cat /proc/stat | grep cpu0 | tr -s ' ' | cut -d ' ' -f3)
CPU_PERC_SYSTEM=$(cat /proc/stat | grep cpu0 | tr -s ' ' | cut -d ' ' -f4)
CPU_PERC_IDLE=$(cat /proc/stat | grep u0 | tr -s ' ' | cut -d ' ' -f5)

#	RAM
MEM_TOTAL=$(cat /proc/meminfo | grep "MemTotal" | tr -s ' ' | cut -d ' ' -f2)
MEM_FREE=$(cat /proc/meminfo | grep "MemFree" | tr -s ' ' | cut -d ' ' -f2)
let "MEM_USED=($MEM_FREE*100) / $MEM_TOTAL" 

#	SD Speicherkapazitaet
ROOTFS_TOTAL=$(df -h | grep "rootfs" | tr -s ' ' | cut -d ' ' -f2)
ROOTFS_TOTAL=$(calc $ROOTFS_TOTAL)

ROOTFS_USED=$(df -h | grep "rootfs" | tr -s ' ' | cut -d ' ' -f3)
ROOTFS_USED=$(calc $ROOTFS_USED)

ROOTFS_FREE=$(df -h | grep "rootfs" | tr -s ' ' | cut -d ' ' -f4)
ROOTFS_FREE=$(calc $ROOTFS_FREE)

#	Writing to SQLite
sqlite3 $HOME/skripte/mon.db "insert into tbl1 values ($TIME,$CPU_TEMP,$CPU_FREQ,$CPU_FREQ_MIN,$CPU_FREQ_MAX,\
$CPU_LOAD_1M,$CPU_LOAD_5M,$CPU_LOAD_15M,$CPU_PERC_USER,$CPU_PERC_NICE,$CPU_PERC_SYSTEM,$CPU_PERC_IDLE,$MEM_TOTAL,\
$MEM_FREE,$MEM_USED,$ROOTFS_TOTAL,$ROOTFS_USED,$ROOTFS_FREE);"

#echo "Total: $ROOTFS_TOTAL\nUsed: $ROOTFS_USED\nFree: $ROOTFS_FREE"

``` 

