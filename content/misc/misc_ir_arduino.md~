Title: Pulsed Infrared Sender / Receiver with Attiny85
Date: 2013-08-05 20:40
Category: Misc
Tags: attiny85, infrared, fluke, pulsed
Author: x4343
Summary: Pulsed Infrared Connection as Stay-Alive Signal using Attiny85, TSOP1138 and CQY99

# The project

I got asked a while ago I can build some lightning which is automatically switched by the staircase lightning.
So if s.o. switches the staircase lightning on, some LEDs should illuminate the wall-attached flower pots.

This could be easily done by switching a 5V power supply.
On the other side of the staircase are also some flower pots, but no power supply at all. As they should also be illuminated, I have to built
something with a battery pack, e.g.

The main question is: **How to switch the LEDs on the other side on and off?**
So this is a typical master/slave communication.

The master is connected to the houses power supply and has constantly the state of the staircase lightning.
If it's on, it has to send a signal to the opposed slave. The opposed slave is switching its LEDs on as long as the signal is transmitted. I name it *stay-alive signal*.

I could have also used a single signal for 'on' and 'off', so only status changes are transmitted. Analog to an edge-triggered oscilloscope.
But there's a huge disadvantage: e.g. the 'off' signal is somehow not sent or received by the slave, it will wrongly stay on as long as some switches the staircase lightning 'on' and 'off' again
(and this may take a long time in the worst case). Since the slave is only powered by a battery pack, this setup may be of short pleasure.

That's so far the project's description.
Overall there a some technical details to clarify:

## What LEDs suit best?

Requirement: Warm, white passive light.

I took some 5 mm waarm white straw hat LEDs with the following characteristics:

* $ U_{LED}=3,3 V $
* $ I_{max}=20 mA $
* $Color Temp.=3000 K$
* $I_{V}= 2000 mcd$
* $\\omega = 100^{\circ}$
* Price: 0.25 EUR pc.

## Master/Slave connection via wireless or infrared?

### Wireless transmitter

Because there are a lot of cheap 433 MHz Transmit-Receiver components at ebay for a few dollars, I first considered using them for the connection between both units.
But since I wanted to keep the solution smart and simple, and the 433 MHz things need an Arduino to work, I discarded the idea.
Even the Attiny85 - which I truly like for small projects - cannot handle the needed library. The 433 MHz things may be nice for further projects to transfer a lot of data instead of a simple
alive-signal, but for this project they a really to much.

The next problem is, that I didn't found anything about power consumption, which should be - at least on the slave - as low as possible.

### Infrared

I came up with the solution to use infrared by pure chance. *"Why not doing it like all the TV manufactures are doing for several decades to switch their devices on and off?"*
Infrared is cheap, easy to implement and widely available. I found an [TSOP 1138](http://www.vishay.com/docs/82013/tsop12xx.pdf) receiver 
in an old television and somewhere near a used IR diode (type CQY 99).
Luckily they are both working together in perfect harmony. I just have to pulse the IR diode in the desired frequency of $f_{IR}=38 kHz$.

# The solution

Picture of the test lab:
[ ![TEST_LAB](/static/pictures/infrared/thumbs/20130713_002b.jpg "TestLab") ](/static/pictures/infrared/20130713_002b.jpg)

# Schematics, Code & Analysis

After some research, I found the following schematics are fulfilling all my needs:

**IR-Sender**

![IR-Sender_Schematic](/static/pictures/infrared/IR_Sender_Schaltplan.png)

**IR-Receiver**

![IR-Receiver_Schematic](/static/pictures/infrared/IR_Receiver_Schaltplan.png)


After the successful practical test, I wanted to make some measurements with my borrowed oscilloscope.

The frequence is nearly 38 kHz (don't care about the measurement errors as they are the *2nd* and *3rd* multiple of the carrier frequency).

![OSIC_spectrum_01](/static/pictures/infrared/fluke/spectrum_01.png)

## Some Graphs 

### Legend: 

Channel A (red) - IR-Sender

Channel B (blue) - IR-Receiver

Carrier frequency 

$ T_{Pulse} = 27,2 \mu s$

$ f_{Pulse} = 36,76 Hz $

![OSIC_graph_01b](/static/pictures/infrared/fluke/graph_01b.png)
![OSIC_graph_01](/static/pictures/infrared/fluke/graph_01.png)

### IR-Receiver processing delay

$ \triangle t_{delay} = 172 \mu s $

![OSIC_graph_02b](/static/pictures/infrared/fluke/graph_02b.png)
![OSIC_graph_02](/static/pictures/infrared/fluke/graph_02.png)

### Duty Cycle
$ t_{off} = 34 ms$

![OSIC_graph_03b](/static/pictures/infrared/fluke/graph_03b.png)
![OSIC_graph_03](/static/pictures/infrared/fluke/graph_03.png)

$ t_{on} = 688 \mu s$

Duty Cycle $D = \frac{0.688 ms}{34.688 ms} = 0,0198 = 20 \% $

![OSIC_graph_04b](/static/pictures/infrared/fluke/graph_04b.png)
![OSIC_graph_04](/static/pictures/infrared/fluke/graph_04.png)

### Voltage peak...
...without the shunt resistor --> a peak of 1,64 V above the high level.
See [here][1] for further explanation.

![OSIC_graph_without_Resistor100b](/static/pictures/infrared/fluke/graph_without_Resistor100b.png)
![OSIC_graph_without_Resistor100](/static/pictures/infrared/fluke/graph_without_Resistor100.png)

...with the shunt resistor $R_2 = 100 \Omega$ --> a small peak about 0,3 V above the high level.

![OSIC_graph_with_Resistor100b](/static/pictures/infrared/fluke/graph_with_Resistor100b.png)
![OSIC_graph_with_Resistor100](/static/pictures/infrared/fluke/graph_with_Resistor100.png)

## Fluke Screenshots

![OSIC_Scr_01](/static/pictures/infrared/fluke/Scr_01.png)
![OSIC_Scr_02](/static/pictures/infrared/fluke/Scr_02.png)
![OSIC_Scr_03](/static/pictures/infrared/fluke/Scr_03.png)
![OSIC_Scr_04](/static/pictures/infrared/fluke/Scr_04.png)
![OSIC_Scr_05](/static/pictures/infrared/fluke/Scr_05.png)
![OSIC_Scr_06](/static/pictures/infrared/fluke/Scr_06.png)
![OSIC_Scr_07](/static/pictures/infrared/fluke/Scr_07.png)
![OSIC_Scr_08](/static/pictures/infrared/fluke/Scr_08.png)




# Installation

# Summary

# Useful Links

[1]: http://andybrown.me.uk/wk/2011/07/09/building-the-phototrap-part-5-the-long-range-infra-red-beam-sensor/

