#BeetBox

This is probably not especially useful to anyone, but may be interesting to those curious about the inner workings of the [Beetbox](http://scott.j38.net/interactive/beetbox/). The code for interfacing with the MPR121 is based on [an Arduino example by Jim Lindblom](http://bildr.org/2011/05/mpr121_arduino/).

##Building Your Own

I'm very open to people recreating the BeetBox as a learning exercise. The code and schematic in this repository are more or less exactly what I used in the project, though you may have to tweak things on your end. The main compontents you need are a [Raspberry Pi](http://www.raspberrypi.org/downloads/) and an [MPR-121](https://www.sparkfun.com/products/9695) capacative touch sensor board from SparkFun. I've also included the schematic for a simple amplifier circuit, but it is totally optional and you can easily use ready-made devices like computer speakers for amplification.

I used the stock [distribution of Raspian](http://www.raspberrypi.org/downloads/) from the Raspberry Pi foundation, though that was some time ago and I'm sure things have changed. The most important thing to make sure of in working with the MPR-121 is that I2C/SMBus connectivity is working properly. Adafruit has a helpful tutorial on [Configuring the Pi for I2C](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/configuring-the-pi-for-i2c).

Once your Pi is communicating with the board properly, you can clone this repository and run the script with something like `sudo python beetbox.py`

##Alternatives

Dealing with the Pi if you're not experienced with Linux can be a big task in itself. If you'd like to experiment with touch-based projects, but aren't quite ready for that level of complexity, there are a few easier ways to get started.

###MaKey Makey

The [MaKey MaKey](http://www.makeymakey.com) works on a different principle (resistance rather than capacitance), but the results are very similar and it's extremely easy to get started with. I'd definitely recommend it for beginners and children.

###Arduino

For the initial prototype of the BeetBox, I used an Arduino connected to an MPR-121 board ([with code and instructions from Jim Lindblom](http://bildr.org/2011/05/mpr121_arduino/)) and plugged it into a laptop running a simple Processing sketch to trigger sounds. Another option would be to skip the sensor board alltogether and try the Arduino [CapSense](http://playground.arduino.cc/Main/CapacitiveSensor?from=Main.CapSense) library.
