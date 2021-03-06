Title: Building a Case for the Raspberry Pi, #1
Date: 2013-10-11 10:25
Category: Raspberry Pi
Tags: raspberry_pi, case, diy, oled, ssd1306
Author: x4343
Summary: Building my first case for the Raspberry Pi with OLED SSD1306 from Adafruit

# Introduction

This post is about my first case I used to build some months ago.
The idea was to have some sort of DIY touch and to have the perfect enclosure for my Raspberry Pi which works as a Media Center under my flat screen.
I attached the nice 128x32 SPI OLED SSD1306 from Adafruit, which works perfectly with the libraries provided by [GuyC@Gaugette](http://guy.carpenter.id.au/gaugette/blog/categories/raspberry-pi/).

So this post is more or less just a protocol of the building process, because I think it's worth sharing.
It took my a while to get everything working because a lack of motivation and time...but in some weeks I think, it will be done!
The last part will be to program some status information from the running XBMC like meta data, play/pause/stopp/volume, playback time etc...
It's just for fun, because no one can read it from 2-3 meters distance ;)

PS: It's called Case #1, because I've already another one half finished.

# The Case Building Process 

I used black acryl glass for the up- and downside. I saw it with a huge buzzsaw, so the edges are splintered. I'll never do it again. Even if it has to go fast, 
it's always better to use an handsaw (e.g. a dovetail saw)!

[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_1_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_1.jpg)
[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_2_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_2.jpg)
[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_10_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_10.jpg)

For the sides I used the old perforated metal plates from an Icybox harddrive case. I just had to cut them at the desired length.
I decided to just make two parts and bend them at the edges. So two of the overall edges are very smooth. The other ones are glued together.
For the glueing together I used epoxid-resin. After 12 hours the sides where absolutely steady mounted!
At last I overpainted the broken color with a black marker. It's not visible unless you know where to look exactly.
 
[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_3_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_3.jpg)

I don't need the S-Video output, so now hole is drilled here. But I was unsure about the analog audio output. I don't think I'll used it someday because of the poor quality, 
but I somehow decided to lead it out.

[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_5_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_5.jpg)

The next thing was to drill a hole for the OLED.
This was kind of boring since I don't have had a Dremel at the time.
I drilled a lot of holes and did the rest with a file. Hard hand time!


[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_4_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_4.jpg)
[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_8_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_8.jpg)
[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_9_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_9.jpg)

The last missing part was a small piece of transluscent acryl glass to cover the OLED.
I found one in an old damaged sat receiver. And since I had a Dremel now, it was a 5 minute job to cut it to the perfect size. It really fits without any air holes.
Maybe it doesn't look that good in the pictures due to reflections. But in reality it's quite nice!
Sadly the acryl glass is very thick, so it takes a lot of the shining brightness of the OLED.

[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_6_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_6.jpg)

Here you see the finished case!
Now I just have to connect the OLED again and do all the programming stuff to give it some nice things to display.

[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_7_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_7.jpg)

# UPDATE: Programming Stuff is done!

OLED is now showing CPU load, Mem load and System Temperature. The display intervall can be set manually.
The script will be posted the next days!
For now i've finished my first case!


[ ![CASE_PICTURE](/static/pictures/raspi_case1/thumbs/case1_11_thumb.jpg "Raspberry Pi Case 1") ](/static/pictures/raspi_case1/case1_11.jpg)



