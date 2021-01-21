#include <config.h>
#include <sys/mman.h>
#include <err.h> 
#include <fcntl.h> 
#include <unistd.h>
#include <stdio.h>

static unsigned GPIO_BASE = 0x3f200000;
//Registers pointers
volatile unsigned int * gpset0;
volatile unsigned int * gpclr0;
volatile unsigned int * gplev0;
//----0:9 pin GPIO'S-------
volatile unsigned int * gpfsel0;
//----10:19 pin GPIO'S-----
volatile unsigned int * gpfsel1;
//----20:29 pin GPIO's-----
volatile unsigned int * gpfsel2;

void init_gpio_pins(){
    int fd;
	if ((fd = open("/dev/mem", O_RDWR, 0)) == -1){
        err(1, "Error opening /dev/mem");
    }
    gpfsel0 = (unsigned int*)mmap(0, getpagesize(), PROT_WRITE, MAP_SHARED, fd, GPIO_BASE);
    //gpfsel1 = (unsigned int*)mmap(0, getpagesize(), PROT_WRITE, MAP_SHARED, fd, GPIO_BASE + 0x4);
    gpfsel1 = gpfsel0 + 0x1;
    //gpfsel2 = (unsigned int*)mmap(0, getpagesize(), PROT_WRITE, MAP_SHARED, fd, GPIO_BASE + 0x8);  
    gpfsel2 = gpfsel0 + 0x2;
    if (gpfsel0 == MAP_FAILED || gpfsel1 == MAP_FAILED || gpfsel2 == MAP_FAILED){
        errx(1, "Error during mapping GPIO");
    }
    gpset0 = gpfsel0 + 0x7;
    gpclr0 = gpfsel0 + 0xA;
    gplev0 = gpfsel0 + 0xD;
}
void set_gpio_mode(int pin, unsigned char mode){
    // Pin as an output
    if (mode == 1){
        if (2 <= pin && pin <= 9){
            if (pin == 2){ // GPIO 2
                *gpfsel0 = *gpfsel0 | 0x40;
            }else if (pin == 3){ // GPIO 3
                *gpfsel0 = *gpfsel0 | 0x200;
            }else if (pin == 4){ // GPIO 4
                *gpfsel0 = *gpfsel0 | 0x1000;
            }else if (pin == 5){ // GPIO 5
                *gpfsel0 = *gpfsel0 | 0x8000;
            }else if (pin == 6){ // GPIO 6
                *gpfsel0 = *gpfsel0 | 0x40000;
            }else if (pin == 7){
                *gpfsel0 = *gpfsel0 | 0x200000;
            }else if (pin == 8){
                *gpfsel0 = *gpfsel0 | 0x1000000;
            }   else if (pin == 9){
                *gpfsel0 = *gpfsel0 | 0x8000000;
            }else{
                printf("El GPIO elegido no es válido1\n");
            } 
        }else if (10 <= pin && pin <= 19){
            if (pin == 10){
                *gpfsel1 = *gpfsel1 | 0x1;
            }else if (pin == 11){
                *gpfsel1 = *gpfsel1 | 0x8;
            }else if (pin == 12){
                *gpfsel1 = *gpfsel1 | 0x40;
            }else if (pin == 13){
                *gpfsel1 = *gpfsel1 | 0x200;
            }else if (pin == 16){
                *gpfsel1 = *gpfsel1 | 0x40000;
            }else if (pin == 17){
                *gpfsel1 = *gpfsel1 | 0x200000;
            }else if (pin == 18){
                *gpfsel1 = *gpfsel1 | 0x1000000;
            }else if (pin == 19){
                *gpfsel1 = *gpfsel1 | 0x8000000;
            }else{
                printf("El GPIO elegido no es válido2\n");
            }
        }else if (20 <= pin && pin <= 27){
            if (pin == 20){
                *gpfsel2 = *gpfsel2 | 0x1;
            }else if (pin == 21){
                *gpfsel2 = *gpfsel2 | 0x8;
            }else if (pin == 22){
                *gpfsel2 = *gpfsel2 | 0x40;
            }else if (pin == 23){
                *gpfsel2 = *gpfsel2 | 0x200;
            }else if (pin == 24){
                *gpfsel2 = *gpfsel2 | 0x1000;
            }else if (pin == 25){
                *gpfsel2 = *gpfsel2 | 0x8000;
            }else if (pin == 26){
                *gpfsel2 = *gpfsel2 | 0x40000;
            }else if (pin == 27){
                *gpfsel2 = *gpfsel2 | 0x200000;
            }else{
                printf("El GPIO elegido no es válido3\n");
            }    
        }else{
            printf("El GPIO elegido no es válido4\n");
        }   
    }else
    // Pin as an input:
    {
        if (2 <= pin && pin <= 9){
            if (pin == 2){ // GPIO 2
                *gpfsel0 = *gpfsel0 & 0xFFFFFFBF; // 1011 1111
            }else if (pin == 3){ // GPIO 3
                *gpfsel0 = *gpfsel0 & 0xFFFFFDFF; // 1101 1111 1111
            }else if (pin == 4){ // GPIO 4
                *gpfsel0 = *gpfsel0 & 0xFFFFEFFF; // 1110 1111 1111 1111
            }else if (pin == 5){ // GPIO 5
                *gpfsel0 = *gpfsel0 & 0xFFFF7FFF; //0111 1111 1111 1111
            }else if (pin == 6){ // GPIO 6
                *gpfsel0 = *gpfsel0 & 0xFFFBFFFF; //1011 1111 1111 1111 1111
            }else if (pin == 7){
                *gpfsel0 = *gpfsel0 & 0xFFDFFFFF; //1101 1111 1111 1111 1111 1111
            }else if (pin == 8){
                *gpfsel0 = *gpfsel0 & 0xFEFFFFFF; // 1110 1111 1111 1111 1111 1111 1111
            }else if (pin == 9){
                *gpfsel0 = *gpfsel0 & 0xF7FFFFFF; // 0111 1111 1111 1111 1111 1111 1111
            }else{
                printf("El GPIO elegido no es válido5\n");
            } 
        }else if(10 <= pin && pin <= 19){
            if (pin == 10){
                *gpfsel1 = *gpfsel1 & 0xFFFFFFFE;
            }else if(pin == 11){
                *gpfsel1 = *gpfsel1 & 0xFFFFFFF7;  
            }else if(pin == 12){
                *gpfsel1 = *gpfsel1 & 0xFFFFFFBF;
            }else if(pin == 13){
                *gpfsel1 = *gpfsel1 & 0xFFFFFDFF;
            }else if(pin == 16){
                *gpfsel1 = *gpfsel1 & 0xFFFBFFFF;
            }else if(pin == 17){
                *gpfsel1 = *gpfsel1 & 0xFFDFFFFF;
            }else if(pin == 18){
                *gpfsel1 = *gpfsel1 & 0xFEFFFFFF;
            }else if(pin == 19){
                *gpfsel1 = *gpfsel1 & 0xF7FFFFFF;
            }else{
                printf("El GPIO elegido no es válido6\n");
            } 
        }else if(20 <= pin && pin <= 27){
            if (pin == 20){
                *gpfsel2 = *gpfsel2 & 0xFFFFFFFE;
            }else if(pin == 21){
                *gpfsel2 = *gpfsel2 & 0xFFFFFFF7;
            }else if(pin == 22){
                *gpfsel2 = *gpfsel2 & 0xFFFFFFBF;
            }else if(pin == 23){
                *gpfsel2 = *gpfsel2 & 0xFFFFFDFF;
            }else if(pin == 24){
                *gpfsel2 = *gpfsel2 & 0xFFFFEFFF;
            }else if(pin == 25){
                *gpfsel2 = *gpfsel2 & 0xFFFF7FFF;
            }else if(pin == 26){
                *gpfsel2 = *gpfsel2 & 0xFFFBFFFF;
            }else if(pin == 27){
                *gpfsel2 = *gpfsel2 & 0xFFDFFFFF;
            }else{
                printf("El GPIO elegido no es válido7\n");
            }
        }else{
            printf("El GPIO elegido no es válido8\n");
        }
    }  
}
void gpio_write(int pin, unsigned char bit){
    if (2 <= pin && pin <= 27){
        if (pin == 2){
            if (bit){
                *gpset0 = 0x4;
            }else{
                *gpclr0 = 0x4;
            }
        }else if (pin == 3){
            if (bit){
                *gpset0 = 0x8;
            }else{
                *gpclr0 = 0x8;
            }
        }else if(pin == 4){
            if (bit){
                *gpset0 = 0x10;
            }else{
                *gpclr0 = 0x10;
            }
        }else if(pin == 5){
            if (bit){
                *gpset0 = 0x20;
            }else{
                *gpclr0 = 0x20;
            }
        }else if(pin == 6){
            if (bit){
                *gpset0 = 0x40;
            }else{
                *gpclr0 = 0x40;
            }
        }else if (pin == 7){
            if (bit){
                *gpset0 = 0x80;
            }else{
                *gpclr0 = 0x80;
            }
        }else if(pin == 8){
            if (bit){
                *gpset0 = 0x100;
            }else{
                *gpclr0 = 0x100;
            }
        }else if(pin == 9){
            if (bit){
                *gpset0 = 0x200;
            }else{
                *gpclr0 = 0x200;
            }
        }else if (pin == 10){
            if (bit){
                *gpset0 = 0x400;
            }else{
                *gpclr0 = 0x400;
            }
        }else if(pin == 11){
            if (bit){
                *gpset0 = 0x800;
            }else{
                *gpclr0 = 0x800;
            }
        }else if(pin == 12){
            if (bit){
                *gpset0 = 0x1000;
            }else{
                *gpclr0 = 0x1000;
            }
        }else if(pin == 13){
            if (bit){
                *gpset0 = 0x2000;
            }else{
                *gpclr0 = 0x2000;
            }
        }else if(pin == 16){
            if (bit){
                *gpset0 = 0x10000;
            }else{
                *gpclr0 = 0x10000;
            }
        }else if(pin == 17){
            if (bit){
                *gpset0 = 0x20000;
            }else{
                *gpclr0 = 0x20000;
            }
        }else if(pin == 18){
            if (bit){
                *gpset0 = 0x40000;
            }else{
                *gpclr0 = 0x40000;
            }
        }else if(pin == 19){
           if (bit){
                *gpset0 = 0x80000;
            }else{
                *gpclr0 = 0x80000;
            } 
        }else if(pin == 20){
            if (bit){
                *gpset0 = 0x100000;
            }else{
                *gpclr0 = 0x100000;
            }
        }else if(pin == 21){
            if (bit){
                *gpset0 = 0x200000;
            }else{
                *gpclr0 = 0x200000;
            }
        }else if(pin == 22){
            if (bit){
                *gpset0 = 0x400000;
            }else{
                *gpclr0 = 0x400000;
            }
        }else if(pin == 23){
            if (bit){
                *gpset0 = 0x800000;
            }else{
                *gpclr0 = 0x800000;
            }
        }else if(pin == 24){
            if (bit){
                *gpset0 = 0x1000000;
            }else{
                *gpclr0 = 0x1000000;
            }
        }else if(pin == 25){
            if (bit){
                *gpset0 = 0x2000000;
            }else{
                *gpclr0 = 0x2000000;
            }
        }else if(pin == 26){
            if (bit){
                *gpset0 = 0x4000000;
            }else{
                *gpclr0 = 0x4000000;
            }
        }else if(pin == 27){
            if (bit){
                *gpset0 = 0x8000000;
            }else{
                *gpclr0 = 0x8000000;
            }
        }else{
            printf("El GPIO elegido no es válido\n");
        } 
    }else{
        printf("El GPIO elegido no es válido\n");
    }
    
}
int gpio_read(int pin){
    int val = *gplev0;
    printf("Val: %i\n", val);
    if (2 <= pin && pin <= 27){
        for (int i = 0; i < pin; i++){
            val = val / 2;
        } 
        printf("El valor de val es: %i\n", val);
        return val & 1;
    }else{
        return -1;
    }      
}
