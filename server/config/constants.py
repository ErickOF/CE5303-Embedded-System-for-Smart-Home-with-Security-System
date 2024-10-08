# Dynamic library path
SRC_LIB: str = '/usr/lib/libgpiodriver.so.0'


# When writing out one logic voltage
HIGH: int = 1
# When writing out zero logic voltage
LOW: int = 0


# When setting pin_mode to read values
INPUT_MODE: int = 0
# When setting pin_mode to write values
OUTPUT_MODE: int = 1
# When some function does not reach the goal, returns -1


FAIL: int = -1
# When some function reaches the goal, returns 0
SUCCESS: int = 0


# Pins values
PINS: dict = {
    'rooms': {
        'pass': 3,
        'block': 4
    },
    'doors': {
        '1': 2
    }
}
