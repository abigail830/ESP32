import machine
import ssd1306
spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 64, spi, machine.Pin(5), machine.Pin(4), machine.Pin(6))

oled.text('Hello World',1,1)
oled.show()

oled.pixel(1,31,1)
oled.show()


