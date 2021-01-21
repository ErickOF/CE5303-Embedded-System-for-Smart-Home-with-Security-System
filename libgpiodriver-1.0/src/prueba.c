#include <gpio_driver.h>
#include <stdio.h>
#include <unistd.h>

int main(){
    printf("--------GPIO DRIVER-----------\n");
    printf("Init the pointers.\n");
    init_gpio_pins();

    printf("Setting the pin 2 in output mode.\n");
    set_gpio_mode(2, 1);
    printf("Writting 1 to the 2 pin.\n");
    gpio_write(2, 1);
    usleep(1000000);
    printf("Writting 0 to the 2 pin.\n");
    gpio_write(2, 0);

    usleep(1000000);

    printf("Setting the pin 17 in ouput mode.\n");
    set_gpio_mode(17, 1);
    printf("Writting 0 to the 17 pin.\n");
    gpio_write(17, 0);
    usleep(1000000);
    printf("Writting 1 to the 17 pin.\n");
    gpio_write(17, 1);


    printf("Setting the pin 3 in input mode.\n");
    set_gpio_mode(3, 0);
    int i = 0;
    while (i <= 20){
        printf("The value of 3 pin is: %i.\n", gpio_read(3));
        usleep(1000000);
        i++;
    }
    
}
