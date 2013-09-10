Title: Rescue a Fused-to-Death-Attiny85
Date: 2013-09-10 22:57
Category: Misc
Tags: attiny85, fuses, high voltage programming
Author: x4343
Summary: Rescue an fused-to-death-Attiny85 with simple high voltage programming

I accidentally destroyed my Attiny85. I wanted to use an external 16 MHz crystal to speed it up.
But in a hurry I accidentally burned the bootloader for 20 MHz to it.
Burning a bootloader via ArduinoISP programmer to the Attiny does also mean that the internal 'fuses' are set up to the preselected frequency.
So once the Attiny's fuses a set to external 20 MHz (FE DF FF), there is no way to connect to it without this 20 MHz crystal.
Unfortunatly I don't have one. But I don't want to throw it away, either.
So I found a very suitable solution to reset the Attiny to factory settings (62 DF FF) with so called 'high voltage programming'.

This can be easily done with the Arduino as ISP Programmer. The only thing you need is a NPN transistor, 5x 1k resistor (current protection for the Arduino Pins),
 1x 10k resistor and a 12V power supply (eponymous for 'high voltage programming').

[ ![Screenshot](/static/pictures/attiny_fuses/attiny_fuses_rescued.png "Screenshot") ](/static/pictures/attiny_fuses/attiny_fuses_rescued.png)

# Useful Links
 
[1: German Instruction](http://www.elektronik-labor.de/Arduino/Fuses.html)

[2: English Instruction](http://www.rickety.us/2010/03/arduino-avr-high-voltage-serial-programmer/)

Here's the used code:

[3: Arduino Code](http://www.rickety.us/wp-content/uploads/2010/03/hv_serial_prog.pde)

To get a hint what the hex values are representing, I strongly recommend the Atmel AVR Fuse Calculator:

[4: Atmel AVR Fuse Calculator](http://www.engbedded.com/fusecalc/)
