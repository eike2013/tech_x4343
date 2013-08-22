Title: Attiny85 Programming Board
Date: 2013-07-29 19:12
Category: Misc
Tags: attiny85, circuit_board
Author: x4343
Summary: Attiny85 Programming Board

For easy Arduino projects I normally use the smaller Attiny µ-processors instead of the big evaluation board.
Since it's very straight forward to programm this small thing using the Arduino as an ISP programmer, there is nothing to be afraid of *(see links)*!

There are several good tutorials, so I won't repeat the basics here.

The only change you have do make if using an Arduino Ethernet Board is changing the `reset` variable:

``` C
//#define RESET SS
#define RESET     2
```

But that's only necessary for the Ethernet Boards. Normally `Pin 10` is reset. But on the Ethernet Board is reserved for 
The most annoying thing was, that I used a breadboard exclusive for programming. So I came up with this little board...

It contains 3 status leds:
- Heartbeat --> Green
- Error --> Red
- Programming --> Yellow
 
Here is the wiring:

| Description | Pin Arduino Ethernet | Pin Board |
| --- | :---: | :---: |
| GND| GND| 1|
| 5V| 5V | 2|
| SCK|12 | 3|
| MISO| 11| 4|
| MOSI| 10| 5|
| LED Heartbeat| 9| 6|
| LED Error| 8| 7|
| LED Progr.| 7| 8|
| Reset| 2| 9|

# Pictures

![ATTINY_BOARD](/static/pictures/attiny_board/20130216_004b.jpg)
![ATTINY_BOARD](/static/pictures/attiny_board/20130225_002b.jpg)


# Useful Links
 
[1: Attiny Library](http://hlt.media.mit.edu/?p=1695)

[2: Arduino Ethernet Schematic *(.pdf)*](http://arduino.cc/de/uploads/Main/arduino-ethernet-schematic.pdf)

[3: Arduino Ethernet as ISP](http://forum.arduino.cc/index.php?topic=112940.0;wap2)