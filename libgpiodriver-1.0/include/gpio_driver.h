#ifndef _GPIO_DRIVER_H
#define _GPIO_DRIVER_H
void init_gpio_pins();
void set_gpio_mode(int pin, unsigned char mode);
void gpio_write(int pin, unsigned char bit);
int gpio_read(int pin);
#endif