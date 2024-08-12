How to Hack: 
        https://wellys.com/posts/rp2040_micropython_debugging/

MicroPython:
        MicroPython v1.20.0 on 2023-04-26; SparkFun Thing Plus RP2040 with RP2040

OLED Display:
        SSD1306 OLED

Radio:  https://lemosint.com/product/rylr896/
        https://reyax.com/products/RYLR896

More reading on PIO:    
        https://asf.microchip.com/docs/latest/sam.drivers.spi.spi_dmac_slave_example.sam3x_ek/html/group__sam__drivers__pio__group.html
        https://docs.micropython.org/en/latest/library/rp2.StateMachine.html
        https://people.ece.cornell.edu/land/courses/ece4760/RP2040/index_rp2040_Micropython.html
        https://docs.micropython.org/en/latest/library/rp2.PIO.html
        https://docs.micropython.org/en/latest/rp2/quickref.html


# after connecting USB to your laptop

```
lsusb | grep MicroPython
```

if you see the device:

```
us 003 Device 007: ID 1b4f:0025 MicroPython Board in FS mode
```

you can connect to it:

```
screen /dev/ttyACM0 -b115200
```

Then press Ctrl+C

You should be given python prompt. To run main program:

```
from main import *
```

