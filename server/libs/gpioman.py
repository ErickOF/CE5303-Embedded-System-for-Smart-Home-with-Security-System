from ctypes import *

from config import constants


gpioman_lib = CDLL(constants.SRC_LIB)


# int export_command(int PIN);
#def export_command(pin: int) -> int:
#    _export_command = gpioman_lib.export_command
#    _export_command.restype = c_int

#    return _export_command(c_int(pin))

# void init_gpio_pins();
def init_gpio_pins() -> None:
    _init_gpio_pins = gpioman_lib.init_gpio_pins
    _init_gpio_pins.restype = None
    
    _init_gpio_pins()
    return

# int pinMode(int PIN, int DIRECTION);
#def pin_mode(pin: int, direction: int) -> int:
#    _pin_mode = gpioman_lib.pinMode
#    _pin_mode.restype = c_int

#    return _pin_mode(c_int(pin), c_int(direction))

# void set_gpio_mode(int pin, unsigned char mode);
def set_gpio_mode(pin: int, mode: int) -> None:
    _set_gpio_mode = gpioman_lib.set_gpio_mode
    _set_gpio_mode.restype = None
    
    _set_gpio_mode(c_int(pin), c_ubyte(mode))
    return

# int digitalWrite(int pin, int value);
#def digital_write(pin: int, direction: int) -> int:
#    _digital_write = gpioman_lib.digitalWrite
#    _digital_write.restype = c_int

#    return _digital_write(c_int(pin), c_int(direction))

# void gpio_write(int pin, unsigned char bit);
def gpio_write(pin: int, bit: int) -> None:
    _gpio_write = gpioman_lib.gpio_write
    _gpio_write.restype = None
    
    _gpio_write(c_int(pin), c_ubyte(bit))
    return

# int digitalRead(int pin);
#def digital_read(pin: int) -> int:
#    _digital_read = gpioman_lib.digitalRead
#    _digital_read.restype = c_int

#    return _digital_read(c_int(pin))

# int gpio_read(int pin);
def gpio_read(pin: int) -> int:
    _gpio_read = gpioman_lib.gpio_read
    _gpio_read.restype = c_int
    
    return _gpio_read(c_int(pin))

# int blink(int pin, float freq, double duration);
#def blink(pin: int, freq: float, duration: float) -> int:
#    _blink = gpioman_lib.blink
#    _blink.restype = c_int
    
#    return _blink(c_int(pin), c_float(freq), c_double(duration))

# int unexport_command(int PIN);
#def unexport_command(pin: int) -> int:
#    _unexport_command = gpioman_lib.unexport_command
#    _unexport_command.restype = c_int

#    return _unexport_command(c_int(pin))

